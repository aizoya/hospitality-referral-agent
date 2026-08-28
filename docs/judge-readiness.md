# Hospitality Referral Agent — AIZOYA OS 2.0 Judge Readiness Review

This document tracks the competition build against the five equally weighted Agents for Humans judging dimensions using the current AIZOYA OS 2.0 evidence standard.

## Current decision

**PATCH → TEST → DEPLOY → SUBMIT**

The competition concept and vertical slice are approved. Do not broaden the product scope before submission.

## 1. Technical Implementation

### Green

- Real AWS Strands `Agent` orchestration
- Real `@tool` implementation
- Deterministic scoring separated from model reasoning
- Amazon Bedrock default model path
- AWS preflight and one-command live validation scripts
- Automated tests
- GitHub Actions CI successfully completed on the competition branch
- Explicit human-approval guardrail
- No autonomous outbound communication capability

### Remaining gates

- Capture one successful live AWS/Bedrock validation run
- Confirm final model/region configuration used for the recorded demo
- Evaluate AgentCore only after the live Bedrock baseline is proven

**OS 2.0 decision:** TEST live Bedrock first. BUILD AgentCore only if it improves visible judge evidence without destabilizing the baseline.

## 2. Design

### Green

- Coherent referral-to-follow-up workflow
- Clear output contract: PRIORITY, WHY, NEXT ACTION, DRAFT, APPROVAL STATUS
- Human approval is part of the product experience
- Judge-facing browser interface exists
- Browser interface supports deterministic offline analysis without AWS credentials
- Browser interface supports a live Strands + Bedrock path when AWS access is configured

### Remaining gate

- Host a public judge-accessible demo or provide an equally reliable public demonstration path.

**OS 2.0 decision:** DEPLOY the existing narrow interface. DEFER CRM, multi-tenant expansion, referral payouts, calling, and unrelated modules.

## 3. Potential Impact

### Green

- Specific audience: independent hospitality and food businesses
- Specific pain: referral opportunities get lost during operations
- Direct business outcome: faster and more consistent follow-up on warm opportunities
- Human-control design fits relationship-driven hospitality sales

### Evidence to strengthen

Use one clearly labeled impact hypothesis in the pitch. Recommended competition metric:

**Referral response time:** reduce the time from referral capture to an owner-ready follow-up draft from hours or days to minutes.

Do not claim production traction or measured revenue impact unless evidence exists.

**OS 2.0 decision:** PRESERVE evidence discipline. Demonstrate the workflow and state measurable hypotheses as hypotheses.

## 4. Creativity & Originality

### Green

- Hospitality-specific agent rather than a general sales chatbot
- Deterministic business scoring plus model reasoning
- Owner approval as a hard architectural boundary
- Designed around relationship-sensitive referral workflows
- The agent performs a complete professional workflow instead of merely chatting

### Presentation risk

If described only as “lead scoring + message drafting,” the project may sound generic.

Use the stronger framing:

**Hospitality Referral Agent is an AI referral operator that converts fragmented hospitality referrals into prioritized, explainable, owner-approved follow-up work.**

## 5. Presentation

### Green

- Under-five-minute demo script exists
- Architecture diagram exists
- Synthetic sample referral exists
- Browser demo exists
- Green GitHub Actions CI can be shown
- Strands implementation is concise enough to show directly

### Remaining gates

- Capture successful live Bedrock execution
- Record the actual working product, not only slides
- Show `Agent`, `@tool`, and tool-driven output briefly
- Show the owner-approval boundary
- Publish the final public video under five minutes

## AIZOYA OS 2.0 internal readiness score

Current estimated readiness: **84 / 100**

- Technical implementation: 18 / 20
- Design/product completeness: 17 / 20
- Potential impact: 17 / 20
- Creativity/originality: 17 / 20
- Presentation readiness: 15 / 20

This is an internal readiness score, not an official Devpost score.

### Path to 90+

1. Complete and capture live AWS/Bedrock validation.
2. Host the existing browser demo or establish a reliable public judge path.
3. Merge the verified competition branch to the default branch after final review.
4. Record and publish the under-five-minute end-to-end video.
5. Complete final Devpost and AWS Builder ID checks.
6. Test AgentCore only after the baseline is stable.
7. Publish up to three quality Builder Center posts if time permits and the competition bonus remains available.

## Council of Excellence

**Build:** deployment evidence, recording assets, final submission evidence.

**Patch:** stale competition documentation, judge navigation, final README release state.

**Test:** reproducibility, guardrails, Bedrock access, demo timing, public-repo privacy, deployment rollback.

**Defer:** Twilio, full CRM, referral payouts, sponsor intelligence, multi-tenant expansion, broad analytics.

**Conditional:** AgentCore after live Bedrock validation.

**Kill for competition scope:** any feature that does not visibly improve a judging dimension before the deadline.

## Failure Council

Primary failure modes to prevent:

1. **Default branch looks unfinished** — merge only after final validation, then ensure `main` is the judge-facing source of truth.
2. **Claims AWS/Bedrock capability without proof** — capture a successful live validation.
3. **Strands use is invisible in the demo** — show `Agent`, `@tool`, and actual tool-driven output.
4. **Overbuilding consumes the schedule** — enforce the locked vertical slice.
5. **AgentCore destabilizes a working build** — maintain the non-AgentCore rollback path.
6. **Submission misses an administrative requirement** — use the submission checklist.
7. **Secret/private-data exposure** — complete the final public-repo audit before merge/submission.
8. **Video explains instead of demonstrates** — show the live workflow early and keep architecture commentary concise.

## Founder Challenge

Do not confuse “more features” with “more competitive.” The highest-value remaining work is evidence: a live AWS run, a reliable public demo, a clean default branch, and a concise working-product video.
