# Hospitality Referral Agent — Final Devpost Field Sheet

Use this as the single source of truth when entering or re-entering the Agents for Humans Devpost submission.

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

Use `docs/submission-package.md` as the authoritative long-form project story and keep all claims aligned to the current runtime evidence.

## Try it out links

**Code:**
https://github.com/aizoya/hospitality-referral-agent

**Public demo:**
Add only after GitHub Pages is enabled and the URL is verified.

Do not publish a fake or unverified live URL.

## Architecture diagram

Use the current architecture artifact derived from `docs/architecture.md` or the approved AIZOYA-branded architecture image prepared for the submission gallery.

## Video demo

Required public YouTube or Vimeo video, under five minutes.

Use `docs/video-recording-package.md`.

Two allowed recording paths:

- Path A: show a successful live Strands + Bedrock response only if AWS eligibility is restored and verified.
- Path B: if AWS eligibility remains blocked, show the working deterministic/browser product, actual Strands implementation, architecture, and CI while briefly disclosing the external account-level eligibility restriction.

Never simulate a successful live Bedrock response.

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

## Optional bonus blog

Leave blank unless an actual builder.aws post is published with `Agents for Humans` in the title.

## Final pre-submit QA

- [ ] Public repository loads without login
- [ ] README and architecture are visible
- [ ] MIT license is visible
- [ ] Strands Agents is named in Built With and project story
- [ ] AWS Builder ID/profile information is entered correctly
- [ ] Public demo URL is verified if included
- [ ] Public YouTube/Vimeo video is under 5 minutes
- [ ] Video shows the working project, not only slides
- [ ] Video explains problem, solution, audience, and Strands usage
- [ ] No private AWS account/support information is visible
- [ ] All required Devpost fields are complete
- [ ] Professional Agents track selected
- [ ] Final submission occurs before September 14, 2026 at 5:00 PM PDT

After the deadline, do not modify the submitted project, repository, form, or video until organizer rules permit it.
