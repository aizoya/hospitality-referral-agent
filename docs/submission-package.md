# Hospitality Referral Agent — Competition Submission Package

Competition: AWS Agents for Humans Hackathon
Recommended track: Professional Agents
Submission deadline: September 14, 2026 at 5:00 PM PDT

## One-line pitch

Hospitality Referral Agent turns a raw hospitality referral into a prioritized, explainable, owner-approved follow-up workflow using AWS Strands Agents—without auto-sending outreach.

## Problem

Hospitality and food-business owners receive referrals through customers, events, vendors, partners, texts, calls, and conversations. During active operations, those opportunities are easy to lose or follow up too late.

## Who it is for

Independent restaurants, caterers, food trucks, hospitality operators, venue partners, and other owner-operated hospitality businesses that depend on referrals but do not have dedicated sales operations.

## Why it matters

A missed referral can mean lost catering revenue, venue relationships, recurring business, or community partnerships. The agent reduces the cognitive load of deciding what deserves attention while preserving human control over outbound communication.

## What the project does

1. Accepts a structured hospitality referral.
2. Uses a Strands tool to score the referral across transparent business factors.
3. Returns a 0–100 score and HIGH / MEDIUM / LOW priority.
4. Explains why the referral matters.
5. Recommends one next action and timing.
6. Drafts a concise follow-up.
7. Stops at an explicit owner-approval checkpoint.

The project does not autonomously send email, SMS, calls, or other outbound communication.

## Required technology

- AWS Strands Agents SDK for orchestration and tool use
- Amazon Bedrock as the default model provider
- Python 3.10+
- Pytest
- GitHub Actions

## Strands implementation evidence

Judges should be shown the following directly in `src/referral_agent.py`:

- `from strands import Agent, tool`
- `@tool` applied to `score_referral`
- a Strands `Agent(...)` configured with the scoring tool
- a system prompt that requires tool use and owner approval

## Architecture summary

Referral input → Strands Agent → deterministic scoring tool → score and priority → explanation → recommended next action → draft → owner approval.

See `docs/architecture.md` for the architecture diagram and implementation boundary.

## Product surface

The repository includes a zero-dependency browser demo:

```bash
python -m scripts.run_web_demo
```

It exposes two explicit paths:

- deterministic offline analysis with no AWS credentials required
- live Strands + Bedrock execution when AWS access is configured

Both paths preserve the owner-approval boundary and do not send outreach.

## Recommended demonstration flow

1. Open the browser demo and show the hospitality referral problem.
2. Load or enter the sample referral.
3. Run deterministic analysis and show transparent scoring.
4. Briefly show the real Strands `Agent` and `@tool` code.
5. Run the live AWS/Bedrock path after credentials and model access are confirmed.
6. Highlight PRIORITY, WHY, NEXT ACTION, DRAFT, and APPROVAL STATUS.
7. Show the successful GitHub Actions CI run.
8. Close on the business impact, owner-control boundary, and public repository.

The final video must remain under five minutes.

## Devpost description draft

Hospitality Referral Agent is a human-in-the-loop AI agent built with AWS Strands Agents for independent hospitality and food businesses. It helps busy operators turn referral opportunities into consistent follow-up without giving up control of customer communication.

A referral enters the workflow with business context, need, urgency, referral strength, and contact completeness. A transparent Strands tool scores the opportunity, assigns a priority, and returns the factors behind the score. The Strands agent then explains why the referral matters, recommends a next action and timing, and drafts a professional follow-up.

The workflow ends at an explicit owner-approval checkpoint. No message, call, or other outbound action is sent automatically.

The project is intentionally narrow: it demonstrates one complete, auditable referral-to-follow-up workflow rather than a general-purpose chatbot or full CRM. The implementation includes deterministic scoring, a browser demo, live Amazon Bedrock validation support, automated tests, CI, an architecture diagram, sample data, and reproducible setup instructions.

## Creativity and differentiation

The project is not a generic lead-scoring chatbot. Its differentiator is an owner-controlled hospitality workflow that combines deterministic business scoring with model reasoning and a hard approval boundary. The system is designed around how hospitality operators actually work: time-constrained, relationship-driven, and sensitive to inappropriate automated outreach.

Preferred framing for judges:

**An AI referral operator for hospitality businesses: capture context, prioritize transparently, explain the opportunity, prepare the follow-up, and surface the exact moment where the owner must decide.**

## Potential-impact hypothesis

Use this as a measurable hypothesis, not as a production claim:

**Reduce referral response time from hours or days to minutes by converting a referral into an owner-ready, prioritized follow-up draft in one workflow.**

Do not claim measured revenue, conversion, time savings, or production traction unless supporting evidence exists.

## Safety and trust story

- No autonomous outbound communication
- Explicit owner approval required
- Transparent scoring components
- Missing information is surfaced rather than invented
- Synthetic sample data is used for competition demonstration
- CI verifies key guardrails

## Submission requirements checklist

- [x] Public GitHub repository
- [x] Competition README on build branch
- [x] MIT license file on build branch
- [x] Architecture diagram
- [x] Strands implementation
- [x] Reproducible setup instructions
- [x] Automated tests
- [x] Successful GitHub Actions CI on competition branch
- [x] Local product-facing browser demo
- [x] Demo script
- [ ] Successful live AWS/Bedrock validation captured for evidence
- [ ] Public judge-accessible hosted demo or equivalent reliable public demo path
- [ ] Verified competition branch merged to default `main`
- [ ] Public YouTube or Vimeo video, maximum five minutes
- [ ] Final Devpost text entered and proofread
- [ ] AWS Builder ID entered
- [ ] Repository About section confirms visible competition description
- [ ] Final public-repo privacy/secrets review completed
- [ ] Optional AgentCore deployment decision completed
- [ ] Optional Builder Center bonus posts published before deadline

## Pre-existing work disclosure

This dedicated competition repository and Strands vertical slice were created during the hackathon submission period. If any concept, sample structure, or code is reused from another AIZOYA project, disclose that reuse accurately in the final submission. Do not claim pre-existing work was created during the competition period.

## AgentCore decision gate

AgentCore is optional and may strengthen Technical Implementation. Add it only after:

1. local and CI validation are green,
2. the live Bedrock agent run succeeds,
3. the demo flow is stable,
4. deployment can be completed without weakening the human-approval boundary or creating unnecessary cost/risk.

Until those gates are met, the core Strands workflow remains the competition priority.
