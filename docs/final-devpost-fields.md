# Hospitality Referral Agent — Final Devpost Field Sheet

Use this as the single source of truth when entering or re-entering the Agents for Humans Devpost submission.

## Schedule

- AIZOYA internal target: September 13, 2026.
- Official deadline: September 14, 2026 at 5:00 PM PDT.
- September 14 is correction/recovery buffer, not planned feature time.

## General info

**Project name**
Hospitality Referral Agent

**Elevator pitch**
Turn hospitality referrals into prioritized, explainable, owner-approved follow-up—without auto-sending outreach.

## Submitter

**Submitter Type**
Organization

**Country of Residence**
United States

**Organization name**
AIZOYA

**Track**
Professional Agents

## Public code repository

https://github.com/aizoya/hospitality-referral-agent

## Built With

- AWS Strands Agents SDK
- Amazon Bedrock
- Python
- Pytest
- GitHub Actions
- HTML
- JavaScript
- Human-in-the-loop AI
- Generative AI
- AI Agents

If Devpost autocomplete provides `Strands Agents SDK`, prefer that exact tag.

## AWS Builder identity

Builder Center profile:
https://builder.aws.com/community/@aizoya

Builder ID account email is managed outside this public repository. Do not publish passwords, verification codes, account IDs, or private AWS credentials.

## Project story

Use `docs/submission-package.md` as the authoritative long-form project story and keep all claims aligned to current runtime evidence.

Preferred judge framing:

**Hospitality Referral Agent is an AI referral operator that converts fragmented hospitality referrals into prioritized, explainable, owner-approved follow-up work.**

Do not reduce the story to generic “lead scoring + message drafting.”

## Try it out links

**Code:**
https://github.com/aizoya/hospitality-referral-agent

**Public demo:**
Add only after GitHub Pages is enabled and the URL is verified.

Do not publish a fake or unverified live URL.

## Architecture diagram

Use the current architecture artifact derived from `docs/architecture.md` or the approved AIZOYA-branded architecture image prepared for the submission gallery.

The diagram should make the human decision boundary visible:

Referral → Strands Agent → deterministic scoring tool → priority/explanation → next action → draft → owner approval.

## Video demo

Required public YouTube or Vimeo video, under five minutes.

Use `docs/video-recording-package.md` and `docs/final-submission-runbook.md`.

Two authorized paths:

- Path A: show a successful live Strands + Bedrock response only if AWS eligibility is restored and verified.
- Path B: if AWS remains externally blocked, show the working deterministic/browser product, real Strands implementation, architecture, CI, and human-approval boundary while briefly disclosing the external account-level quota/eligibility restriction.

Live Bedrock success is a score enhancer, not a prerequisite for a truthful submission. Never simulate a successful live response.

## Testing instructions

Public judge demo:
Open the public demo link when available and use the included synthetic hospitality referral. The browser demo performs deterministic referral scoring and displays priority, recommended timing, and the human-approval checkpoint.

Local deterministic test:
1. Clone the public repository.
2. Create and activate a Python virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run `pytest -q`.
5. Run `python -m scripts.run_demo --score-only`.

Local browser demo:
Run `python -m scripts.run_web_demo` and select **Analyze referral offline**.

Live AWS Strands + Bedrock path:
Run `python -m scripts.live_validation --region us-east-2` only after AWS account-level eligibility is restored or a read-only quota check shows a usable non-zero quota.

No email, SMS, voice call, or other outbound communication is sent automatically. All generated outreach remains `DRAFT_ONLY_NOT_SENT` and requires explicit owner approval.

## Current AWS disclosure

At submission-preparation time, the newly created AWS account remains under Amazon Bedrock account-level eligibility review. Credentials resolve, Bedrock model discovery succeeds, and the Strands request reaches Bedrock `ConverseStream`, but live inference remains blocked while the relevant daily-token quotas remain `0`.

This is an external account-eligibility condition, not currently classified as an application logic or IAM defect.

## Judge-traceability lock

Before clicking Submit, confirm that the project story and video visibly support all five judging dimensions:

- **Technical Implementation:** real Strands `Agent`, real `@tool`, deterministic scoring, Bedrock path evidence, tests/CI, owner-approval guardrail.
- **Design:** clear referral → priority → why → next action → draft → approval workflow.
- **Potential Impact:** specific hospitality audience and response-time hypothesis clearly labeled as a hypothesis.
- **Creativity & Originality:** hospitality-specific referral operator, deterministic business logic + model reasoning, relationship-sensitive human control.
- **Presentation:** working product appears immediately, end-to-end flow is understandable, architecture is concise, video is under five minutes.

Remove or qualify any claim that cannot be tied to direct evidence.

## Optional bonus blog

Leave blank unless an actual builder.aws post is published with `Agents for Humans` in the title.

## Final pre-submit QA

- [ ] Public repository loads without login
- [ ] Default branch contains the competition build
- [ ] README and architecture are visible
- [ ] MIT license is visible
- [ ] Strands Agents is named in Built With and project story
- [ ] AWS Builder ID/profile information is entered correctly
- [ ] Public demo URL is verified if included
- [ ] Public YouTube/Vimeo video is under 5 minutes
- [ ] Video shows the working project, not only slides
- [ ] Video explains problem, audience, why it matters, Strands use, and human decision boundary
- [ ] No private AWS account/support information is visible
- [ ] All required Devpost fields are complete
- [ ] Professional Agents track selected
- [ ] Architecture diagram uploaded
- [ ] Pre-existing work disclosure accurate
- [ ] No unsupported traction/revenue/production-readiness claims
- [ ] All five judging dimensions have visible evidence
- [ ] Target submission completed by September 13, 2026
- [ ] Absolute deadline remains September 14, 2026 at 5:00 PM PDT

After the deadline, do not modify the submitted project, repository, form, or video until organizer rules permit it.
