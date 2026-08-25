# Hospitality Referral Agent — Demo Script

Target runtime: 3–5 minutes.

## 1. Problem — 30 seconds

Hospitality operators receive referrals from customers, events, vendors, and partners, but busy owners often lose track of which opportunities deserve attention first. Hospitality Referral Agent turns a raw referral into a prioritized, explainable, owner-approved follow-up workflow.

## 2. Show the input — 30 seconds

Open `examples/sample_referral.json` and point out:

- Oakland event venue
- referred by an existing catering client
- immediate catering-partner need
- high urgency
- complete contact information

## 3. Show Strands clearly — 45 seconds

Open `src/referral_agent.py` and show:

- `from strands import Agent, tool`
- `@tool` on `score_referral`
- `Agent(...)` with the scoring tool
- the system prompt requiring tool use and owner approval

State clearly: AWS Strands Agents orchestrates the referral-analysis workflow and calls a transparent business scoring tool before generating the owner-facing recommendation.

## 4. Run the agent — 60 seconds

First show the deterministic score-only path:

```bash
python -m scripts.run_demo --score-only
```

Then, with AWS/Bedrock credentials configured, run:

```bash
python -m scripts.live_validation --region us-west-2
```

Highlight the output sections:

- PRIORITY
- WHY
- NEXT ACTION
- DRAFT
- APPROVAL STATUS

## 5. Human approval guardrail — 45 seconds

Emphasize that the agent can analyze, prioritize, explain, recommend, and draft, but it cannot send outreach.

Point to:

- `approval_required: true`
- `DRAFT_ONLY_NOT_SENT`
- the system prompt rule forbidding claims that anything was sent, scheduled, called, or delivered

## 6. Architecture and tests — 45 seconds

Open `docs/architecture.md` and show the referral → Strands Agent → scoring tool → recommendation → owner approval flow.

Open GitHub Actions and show the green CI run:

- tests pass
- deterministic demo smoke test passes

## 7. Close — 30 seconds

Hospitality Referral Agent turns referrals into follow-ups without taking control away from the owner. The MVP proves a real end-to-end Strands workflow: intake, prioritization, explanation, next action, draft, and human approval.

## Recording checklist

- Keep the full video under five minutes.
- Show Strands code on screen.
- Show the actual agent flow, not only slides.
- Show green CI.
- Show the owner-approval boundary.
- End with the dedicated repository and project name visible.
