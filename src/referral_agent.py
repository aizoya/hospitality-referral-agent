"""Hospitality Referral Agent vertical slice powered by Strands Agents.

The deterministic scoring tool is intentionally separated from model reasoning so
priority behavior can be tested without AWS credentials. The Strands agent uses
that tool, explains the result, recommends a next action, and drafts follow-up
copy while enforcing owner approval before any outbound action.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Any

from strands import Agent, tool


@dataclass(frozen=True)
class Referral:
    business_name: str
    contact_name: str
    business_type: str
    location: str
    referral_source: str
    stated_need: str
    urgency: str = "medium"
    contact_complete: bool = True
    referral_strength: str = "warm"
    notes: str = ""


def _bounded(value: int, low: int = 0, high: int = 100) -> int:
    return max(low, min(high, value))


def score_referral_record(referral: dict[str, Any]) -> dict[str, Any]:
    """Return deterministic priority scoring and component explanations."""
    urgency = str(referral.get("urgency", "")).lower()
    strength = str(referral.get("referral_strength", "")).lower()
    need = str(referral.get("stated_need", "")).strip()
    business_type = str(referral.get("business_type", "")).strip()
    contact_complete = bool(referral.get("contact_complete", False))

    need_points = 30 if need else 5
    referral_points = {"hot": 20, "warm": 16, "cold": 8}.get(strength, 10)
    urgency_points = {"high": 20, "medium": 12, "low": 5}.get(urgency, 8)
    fit_points = 20 if business_type else 5
    contact_points = 10 if contact_complete else 3

    score = _bounded(
        need_points
        + referral_points
        + urgency_points
        + fit_points
        + contact_points
    )

    if score >= 80:
        priority = "HIGH"
        timing = "within 24 hours"
    elif score >= 60:
        priority = "MEDIUM"
        timing = "within 3 business days"
    else:
        priority = "LOW"
        timing = "within 7 business days"

    return {
        "score": score,
        "priority": priority,
        "recommended_timing": timing,
        "components": {
            "need_intent": need_points,
            "referral_quality": referral_points,
            "urgency": urgency_points,
            "business_fit": fit_points,
            "contact_completeness": contact_points,
        },
        "approval_required": True,
        "outbound_status": "DRAFT_ONLY_NOT_SENT",
    }


@tool
def score_referral(referral_json: str) -> str:
    """Score one hospitality referral and return transparent priority factors.

    Args:
        referral_json: JSON object containing the referral fields.
    """
    referral = json.loads(referral_json)
    return json.dumps(score_referral_record(referral), indent=2)


SYSTEM_PROMPT = """
You are the Hospitality Referral Agent, an owner-controlled referral follow-up
assistant for food and hospitality businesses.

For every referral:
1. Call score_referral before giving a priority.
2. Preserve the tool's numeric score and HIGH/MEDIUM/LOW priority exactly.
3. Explain the strongest factors in concise business language.
4. Recommend one next action and use the tool's recommended timing.
5. Draft a short professional follow-up message appropriate to the referral.
6. Clearly label the message DRAFT ONLY — OWNER APPROVAL REQUIRED.
7. Never claim a message was sent, scheduled, called, or delivered.
8. Never bypass owner approval. No autonomous outbound communication is allowed.
9. If material information is missing, identify it rather than inventing it.

Return sections: PRIORITY, WHY, NEXT ACTION, DRAFT, APPROVAL STATUS.
""".strip()


def build_agent(model: str | None = None) -> Agent:
    """Construct the Strands agent. Bedrock is used by default when model is None."""
    kwargs: dict[str, Any] = {
        "system_prompt": SYSTEM_PROMPT,
        "tools": [score_referral],
    }
    if model:
        kwargs["model"] = model
    return Agent(**kwargs)


def analyze_referral(referral: Referral, model: str | None = None) -> str:
    """Run one referral through the Strands agent and return its text response."""
    agent = build_agent(model=model)
    prompt = (
        "Analyze this referral. Use the scoring tool before responding.\n\n"
        + json.dumps(asdict(referral), indent=2)
    )
    return str(agent(prompt))
