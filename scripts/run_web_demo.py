"""Zero-dependency browser demo for the Hospitality Referral Agent.

The default server exposes deterministic scoring without AWS credentials. A live
Strands/Bedrock action is available only when the server is started explicitly
with --enable-live. No outbound communication is ever sent.
"""

from __future__ import annotations

import argparse
import html
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs

from src.referral_agent import Referral, analyze_referral, score_referral_record


MAX_BODY_BYTES = 16_384

SAMPLE = {
    "business_name": "Harbor Hall",
    "contact_name": "Maya Chen",
    "business_type": "Event venue",
    "location": "Oakland, CA",
    "referral_source": "Existing catering client",
    "stated_need": "Needs a preferred catering partner for upcoming private events",
    "urgency": "high",
    "referral_strength": "warm",
    "contact_complete": True,
    "notes": "First event is expected next month.",
}


def _field(name: str, value: str, label: str) -> str:
    return (
        f'<label>{html.escape(label)}<input name="{html.escape(name)}" '
        f'value="{html.escape(value, quote=True)}" required></label>'
    )


def render_page(
    data: dict | None = None,
    result: dict | None = None,
    error: str = "",
    *,
    live_enabled: bool = False,
) -> str:
    data = {**SAMPLE, **(data or {})}
    score = result.get("score") if result else None
    priority = result.get("priority") if result else None
    timing = result.get("recommended_timing") if result else None
    live_output = result.get("live_output") if result else None
    components = result.get("components") if result else None

    result_html = ""
    if result:
        component_rows = "".join(
            f"<li><strong>{html.escape(key.replace('_', ' ').title())}</strong>: {value}</li>"
            for key, value in (components or {}).items()
        )
        live_section = (
            f"<section><h3>Live Strands / Bedrock output</h3><pre>{html.escape(str(live_output))}</pre></section>"
            if live_output
            else ""
        )
        result_html = f"""
        <section class="result">
          <div class="score"><span>Priority</span><strong>{html.escape(str(priority))}</strong><b>{score}/100</b></div>
          <div><h3>Recommended timing</h3><p>{html.escape(str(timing))}</p></div>
          <div><h3>Transparent scoring</h3><ul>{component_rows}</ul></div>
          <div class="guardrail"><strong>OWNER APPROVAL REQUIRED</strong><br>DRAFT ONLY — NOTHING HAS BEEN SENT</div>
          {live_section}
        </section>
        """

    error_html = f'<div class="error">{html.escape(error)}</div>' if error else ""
    live_button = (
        '<button class="secondary" name="action" value="live" type="submit">Run live Strands + Bedrock</button>'
        if live_enabled
        else ""
    )
    mode_note = (
        "Offline analysis is deterministic and credential-free. Live analysis is enabled for this controlled session and uses the real Strands agent and Amazon Bedrock."
        if live_enabled
        else "Offline analysis is deterministic and credential-free. Live Bedrock invocation is disabled by default; start the server with --enable-live only in a controlled environment."
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hospitality Referral Agent</title>
<style>
:root {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color:#172033; background:#f6f7fb; }}
body {{ margin:0; }} main {{ max-width:980px; margin:0 auto; padding:32px 20px 60px; }}
.hero {{ background:#111827; color:white; border-radius:20px; padding:28px; margin-bottom:20px; }}
.hero p {{ color:#d1d5db; max-width:720px; }}
.card, .result {{ background:white; border:1px solid #e5e7eb; border-radius:18px; padding:22px; box-shadow:0 8px 24px rgba(17,24,39,.05); }}
form {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px; }}
label {{ display:flex; flex-direction:column; gap:7px; font-size:13px; font-weight:700; }}
input, select, textarea {{ box-sizing:border-box; width:100%; border:1px solid #cbd5e1; border-radius:10px; padding:11px; font:inherit; background:white; }}
textarea {{ min-height:92px; resize:vertical; }} .wide {{ grid-column:1/-1; }}
.actions {{ grid-column:1/-1; display:flex; flex-wrap:wrap; gap:10px; margin-top:4px; }}
button {{ border:0; border-radius:10px; padding:12px 16px; font-weight:800; cursor:pointer; }}
button.primary {{ background:#111827; color:white; }} button.secondary {{ background:#e5e7eb; color:#111827; }}
.result {{ margin-top:20px; display:grid; gap:16px; }}
.score {{ display:flex; align-items:baseline; gap:14px; flex-wrap:wrap; }} .score span {{ color:#64748b; }} .score strong {{ font-size:28px; }} .score b {{ font-size:20px; }}
.guardrail {{ border:1px solid #f59e0b; background:#fffbeb; border-radius:12px; padding:14px; }}
pre {{ white-space:pre-wrap; word-wrap:break-word; background:#0f172a; color:#e2e8f0; border-radius:12px; padding:16px; overflow:auto; }}
.error {{ background:#fef2f2; color:#991b1b; border:1px solid #fecaca; border-radius:12px; padding:12px; margin-bottom:14px; }}
small {{ color:#64748b; }}
@media (max-width:700px) {{ form {{ grid-template-columns:1fr; }} .wide {{ grid-column:auto; }} }}
</style>
</head>
<body><main>
<section class="hero">
  <h1>Hospitality Referral Agent</h1>
  <p>Turn a warm hospitality referral into an explainable priority, recommended next action, and owner-controlled follow-up draft. The agent never sends outreach automatically.</p>
</section>
{error_html}
<section class="card">
<form method="post">
  {_field('business_name', str(data['business_name']), 'Business name')}
  {_field('contact_name', str(data['contact_name']), 'Contact name')}
  {_field('business_type', str(data['business_type']), 'Business type')}
  {_field('location', str(data['location']), 'Location')}
  {_field('referral_source', str(data['referral_source']), 'Referral source')}
  <label>Urgency<select name="urgency"><option {'selected' if data['urgency']=='high' else ''}>high</option><option {'selected' if data['urgency']=='medium' else ''}>medium</option><option {'selected' if data['urgency']=='low' else ''}>low</option></select></label>
  <label>Referral strength<select name="referral_strength"><option {'selected' if data['referral_strength']=='hot' else ''}>hot</option><option {'selected' if data['referral_strength']=='warm' else ''}>warm</option><option {'selected' if data['referral_strength']=='cold' else ''}>cold</option></select></label>
  <label>Contact information<select name="contact_complete"><option value="true" {'selected' if data['contact_complete'] else ''}>Complete</option><option value="false" {'selected' if not data['contact_complete'] else ''}>Incomplete</option></select></label>
  <label class="wide">Stated need<textarea name="stated_need" required>{html.escape(str(data['stated_need']))}</textarea></label>
  <label class="wide">Notes<textarea name="notes">{html.escape(str(data['notes']))}</textarea></label>
  <div class="actions">
    <button class="primary" name="action" value="score" type="submit">Analyze referral offline</button>
    {live_button}
  </div>
</form>
<small>{html.escape(mode_note)}</small>
</section>
{result_html}
</main></body></html>"""


def _parse_form(body: bytes) -> dict:
    raw = parse_qs(body.decode("utf-8"), keep_blank_values=True)
    value = lambda key, default="": raw.get(key, [default])[0]
    return {
        "business_name": value("business_name"),
        "contact_name": value("contact_name"),
        "business_type": value("business_type"),
        "location": value("location"),
        "referral_source": value("referral_source"),
        "stated_need": value("stated_need"),
        "urgency": value("urgency", "medium").lower(),
        "referral_strength": value("referral_strength", "warm").lower(),
        "contact_complete": value("contact_complete", "false") == "true",
        "notes": value("notes"),
        "action": value("action", "score"),
    }


def evaluate(data: dict, *, live_enabled: bool = False) -> dict:
    result = score_referral_record(data)
    if data.get("action") == "live":
        if not live_enabled:
            raise PermissionError("Live Bedrock invocation is disabled for this server session.")
        referral_fields = {k: v for k, v in data.items() if k != "action"}
        result["live_output"] = analyze_referral(Referral(**referral_fields))
    return result


class DemoHandler(BaseHTTPRequestHandler):
    live_enabled = False

    def _send(self, page: str, status: int = 200) -> None:
        payload = page.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:  # noqa: N802
        self._send(render_page(live_enabled=self.live_enabled))

    def do_POST(self) -> None:  # noqa: N802
        data = SAMPLE
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 0 or length > MAX_BODY_BYTES:
                self._send(
                    render_page(
                        data,
                        error="Request is too large for the competition demo.",
                        live_enabled=self.live_enabled,
                    ),
                    413,
                )
                return
            data = _parse_form(self.rfile.read(length))
            result = evaluate(data, live_enabled=self.live_enabled)
            self._send(render_page(data, result, live_enabled=self.live_enabled))
        except Exception as exc:  # fail visibly without leaking infrastructure detail
            print(f"Demo analysis error: {type(exc).__name__}")
            self._send(
                render_page(
                    data,
                    error="Analysis could not complete. Check the controlled demo environment and try again.",
                    live_enabled=self.live_enabled,
                ),
                500,
            )

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the local judge-facing browser demo")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument(
        "--enable-live",
        action="store_true",
        help="Expose the live Strands + Bedrock action for a controlled session",
    )
    args = parser.parse_args()
    DemoHandler.live_enabled = args.enable_live
    server = ThreadingHTTPServer((args.host, args.port), DemoHandler)
    print(f"Hospitality Referral Agent demo: http://{args.host}:{args.port}")
    print(f"Live Strands + Bedrock: {'ENABLED' if args.enable_live else 'DISABLED'}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
