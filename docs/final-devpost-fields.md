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

**Submitter Type — approved and saved September 13, 2026**
Individual. The founder confirmed AIZOYA is not yet legally formed and explicitly approved changing the existing draft to Individual. The saved selection was verified after reopening the form.

**Country of Residence**
United States

**Organization field**
Not applicable — individual entrant.

Devpost retained the previous text when an empty value was saved; the explicit not-applicable value was saved and verified after reopening. AIZOYA remains the project branding. Final submission has not occurred.

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
Expected GitHub Pages URL: https://aizoya.github.io/hospitality-referral-agent/

GitHub's `pages build and deployment` workflow completed successfully from `main` after Pages was configured to publish `/docs`. Treat deployment as verified. Before entering the URL into Devpost, perform one normal-browser render check and confirm the demo loads and the synthetic referral interaction works as documented.

Do not claim a browser-render verification that has not actually been observed.

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

The public demo link and AgentCore deployment are optional. The official rules still require a functioning Strands project. Path B is an internally approved disclosure/release contingency, not an organizer waiver or a guarantee of eligibility; successful end-to-end Strands execution remains unverified. Never simulate a successful live response.

## Testing instructions

Public judge demo:
Open the public demo link after browser verification and use the included synthetic hospitality referral. The browser demo performs deterministic referral scoring and displays priority, recommended timing, and the human-approval checkpoint.

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

Fresh September 13 CloudShell validation confirms:

- AWS credentials resolve successfully.
- Bedrock model discovery succeeds in `us-east-2` with 90 models listed.
- The Strands runtime reaches Amazon Bedrock `ConverseStream`.
- Bedrock rejects the live request with `ThrottlingException: Too many tokens per day, please wait before trying again.`
- The Strands SDK surfaces the same condition as `ModelThrottledException`.
- AWS Support previously confirmed the account is under internal review for account-level Bedrock inference eligibility/provisioning, and the founder sent a fresh evidence update on September 13.

This is classified as an external AWS account/provisioning blocker, not an application-logic defect. Do not retry repeatedly, broaden IAM, create long-lived access keys, switch models merely to bypass the restriction, or claim successful live inference.

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

- [x] Public repository loads without login
- [x] Default branch contains the competition build
- [x] README and architecture are visible
- [x] MIT license is visible
- [x] Strands Agents is named in Built With and project story
- [x] Submitter type corrected to Individual and saved
- [x] GitHub Pages deployment workflow completed successfully
- [x] Fresh AWS validation reaches Bedrock runtime and records the external throttle truthfully
- [ ] Normal-browser public demo render and interaction verified
- [ ] AWS Builder ID/profile information confirmed in final form
- [ ] Public YouTube/Vimeo video is under 5 minutes
- [ ] Video shows the working project, not only slides
- [ ] Video explains problem, audience, why it matters, Strands use, and human decision boundary
- [ ] No private AWS account/support information is visible
- [ ] All required Devpost fields are complete
- [ ] Professional Agents track selected
- [ ] Architecture diagram uploaded and legible
- [ ] Pre-existing work disclosure accurate
- [ ] No unsupported traction/revenue/production-readiness claims
- [ ] All five judging dimensions have visible evidence
- [ ] Terms reviewed and accepted by the founder
- [ ] Final project submitted and confirmation captured
- [ ] Absolute deadline remains September 14, 2026 at 5:00 PM PDT

After the deadline, do not modify the submitted project, repository, form, or video until organizer rules permit it.
