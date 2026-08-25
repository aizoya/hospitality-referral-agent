# Hospitality Referral Agent — Judge Readiness Review

This document tracks the competition build against the five equally weighted Agents for Humans judging dimensions.

## 1. Technical Implementation

Current strengths:

- Real AWS Strands `Agent` orchestration
- Real `@tool` implementation
- Deterministic scoring separated from model reasoning
- Amazon Bedrock default model path
- AWS preflight and live validation scripts
- Automated tests and GitHub Actions CI
- Explicit human-approval guardrail

Remaining gaps:

- Capture a successful live AWS/Bedrock validation run
- Add a judge-friendly product surface or hosted live demo
- Decide whether AgentCore adds enough scoring value after the core flow is stable

Competition decision: BUILD live validation and product surface; TEST AgentCore only after those are green.

## 2. Design

Current strengths:

- Coherent referral-to-follow-up workflow
- Clear output contract: PRIORITY, WHY, NEXT ACTION, DRAFT, APPROVAL STATUS
- Human approval is part of the experience rather than an afterthought

Remaining gap:

- Current experience is primarily CLI/code-facing. Judges explicitly reward a complete product experience, so the demo should expose the workflow through a simple, focused interface rather than relying only on terminal output.

Competition decision: BUILD one narrow demo interface. DEFER CRM, multi-tenant expansion, referral payouts, calling, and unrelated product modules.

## 3. Potential Impact

Current strengths:

- Specific audience: independent hospitality and food businesses
- Specific pain: referral opportunities get lost during operations
- Direct business outcome: faster, more consistent follow-up on warm opportunities
- Human-control design fits relationship-driven hospitality sales

Evidence to strengthen before submission:

- One concise operator story showing how a referral can be missed during service
- One measurable target such as referral response time, percentage of referrals followed up, or owner time saved
- If available, a small sample-based before/after demonstration clearly labeled as illustrative rather than production evidence

Competition decision: TEST the pitch with measurable outcomes; do not fabricate traction.

## 4. Creativity & Originality

Current strengths:

- Hospitality-specific agent rather than a general-purpose sales bot
- Deterministic business scoring plus model reasoning
- Owner approval as a hard architectural boundary
- Designed around relationship-sensitive referral workflows

Risk:

- If presented as merely “lead scoring + message drafting,” the idea may feel generic.

Presentation requirement:

Explain that the novelty is the complete owner-controlled referral workflow for hospitality operators: context intake → transparent prioritization → reasoning → timing → draft → explicit decision checkpoint.

Competition decision: PRESERVE the narrow workflow and strengthen the story instead of adding unrelated features.

## 5. Presentation

Current strengths:

- A 3–5 minute demo script already exists
- Architecture diagram exists
- Sample referral exists
- Green CI can be shown

Remaining gaps:

- Record the actual working agent, not only slides
- Show Strands code briefly and visibly
- Show a successful live Bedrock run
- Show the human approval boundary
- Use a product-facing interface if available
- Upload a public YouTube or Vimeo video under five minutes

Competition decision: BUILD a repeatable demo sequence before recording.

## Aizoya OS competition score

Current estimated readiness: **78 / 100**

- Technical implementation: 18 / 20
- Design/product completeness: 12 / 20
- Potential impact: 16 / 20
- Creativity/originality: 16 / 20
- Presentation readiness: 16 / 20

This is an internal readiness score, not an official Devpost score.

### Path to 90+

1. Complete and capture live AWS/Bedrock validation.
2. Add a small judge-friendly product interface and, if practical, a live demo URL.
3. Add one measurable impact hypothesis and concise operator scenario.
4. Rehearse and record the under-five-minute end-to-end video.
5. Run final repo/privacy/license/setup verification.
6. Only then evaluate AgentCore as an incremental technical-score enhancement.

## Council of Excellence recommendation

**Build:** live validation evidence, focused demo interface, final submission copy, measurable impact framing, recording assets.

**Patch:** README competition positioning and judge navigation.

**Test:** reproducibility, guardrails, Bedrock access, demo timing, public-repo secrets/privacy.

**Defer:** Twilio, full CRM, referral payouts, sponsor intelligence, multi-tenant expansion, broad analytics.

**AgentCore:** conditional test/build after the core demo is stable.

**Kill for competition scope:** any feature that does not visibly improve one of the five judging criteria before the deadline.

## Failure Council

Primary failure modes to prevent:

1. **Looks like a prototype instead of a product** — mitigate with a focused interface.
2. **Claims AWS/Bedrock capability without showing it working** — mitigate with captured live validation.
3. **Strands use is invisible in the demo** — show `Agent`, `@tool`, and actual tool-driven output.
4. **Overbuilding consumes the schedule** — enforce the narrow vertical slice.
5. **AgentCore breaks a stable build** — keep it behind a decision gate.
6. **Submission fails an administrative requirement** — use the submission checklist.
7. **Accidental secret/private data exposure** — perform a final public-repo audit before submission.

## Founder Challenge

Do not confuse “more features” with “more competitive.” The best next work is the work a judge can see, run, understand, and score. A stable Strands workflow with a polished demo, evidence, and clear business impact is more valuable than a broad unfinished hospitality platform.
