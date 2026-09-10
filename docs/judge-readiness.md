# Hospitality Referral Agent — AIZOYA OS 2.4 Judge Readiness Review

This document tracks the competition build against the five equally weighted Agents for Humans judging dimensions using the current AIZOYA OS 2.4 evidence standard.

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
- Bedrock credentials and model discovery validated
- Live Strands request reaches Bedrock `ConverseStream`
- Earlier account-verification and Anthropic FTU gates have cleared

### Remaining gate

- Capture one successful live AWS/Bedrock model response after AWS restores a non-zero daily-token quota.

Current external condition: Service Quotas shows Claude Sonnet 4.6 daily-token quotas at `0`, including non-adjustable daily-token quotas, and runtime returns `ThrottlingException: Too many tokens per day`. AWS Support is reviewing account-level provisioning. This is not classified as an application or IAM defect.

**OS 2.4 decision:** preserve the verified Strands + Bedrock architecture, keep IAM narrow, and do not switch models merely to hide an account-level quota gate. BUILD AgentCore only if the live Bedrock baseline becomes stable and it visibly improves judge evidence.

## 2. Design

### Green

- Coherent referral-to-follow-up workflow
- Clear output contract: PRIORITY, WHY, NEXT ACTION, DRAFT, APPROVAL STATUS
- Human approval is part of the product experience
- Judge-facing browser interface exists
- Browser interface supports deterministic offline analysis without AWS credentials
- Browser interface supports a live Strands + Bedrock path when AWS runtime quota is available
- Pages-ready public static demo exists and makes no AWS/network requests

### Remaining gate

- Enable and verify the public GitHub Pages surface after the verified branch is merged to `main`.

**OS 2.4 decision:** DEPLOY the existing narrow interface. DEFER CRM, multi-tenant expansion, referral payouts, calling, and unrelated modules.

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

**OS 2.4 decision:** PRESERVE evidence discipline. Demonstrate the workflow and state measurable hypotheses as hypotheses.

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
- Truthful quota-contingency recording path exists
- Architecture diagram exists
- Synthetic sample referral exists
- Browser demo exists
- Green GitHub Actions CI can be shown
- Strands implementation is concise enough to show directly

### Remaining gates

- Preferably capture successful live Bedrock execution after quota restoration
- Record the actual working product, not only slides
- Show `Agent`, `@tool`, and tool-driven design briefly
- Show the owner-approval boundary
- If AWS quota remains externally blocked, disclose it accurately and do not simulate success
- Publish the final public video under five minutes

## AIZOYA OS 2.4 internal readiness score

Current estimated readiness: **86 / 100**

- Technical implementation: 18 / 20
- Design/product completeness: 18 / 20
- Potential impact: 17 / 20
- Creativity/originality: 17 / 20
- Presentation readiness: 16 / 20

This is an internal readiness score, not an official Devpost score.

### Path to 90+

1. Capture a successful live AWS/Bedrock response if AWS restores quota before recording.
2. Merge the verified competition branch to the default branch after the live-release gate is satisfied.
3. Enable and verify the public GitHub Pages demo.
4. Record and publish the under-five-minute end-to-end video.
5. Complete final Devpost and AWS Builder ID checks.
6. Test AgentCore only after the baseline is stable.
7. Publish optional Builder Center posts only if they do not threaten submission readiness.

## Council of Excellence

**Build:** recording assets, final submission evidence, public judge path after release gate clears.

**Patch:** stale competition documentation, judge navigation, final README release state.

**Test:** reproducibility, guardrails, Bedrock quota restoration, demo timing, public-repo privacy, deployment rollback.

**Defer:** Twilio, full CRM, referral payouts, sponsor intelligence, multi-tenant expansion, broad analytics.

**Conditional:** AgentCore after live Bedrock validation.

**Kill for competition scope:** any feature that does not visibly improve a judging dimension before the deadline.

## Failure Council

Primary failure modes to prevent:

1. **Default branch looks unfinished** — merge only after the release gate is satisfied, then ensure `main` is the judge-facing source of truth.
2. **Claims AWS/Bedrock capability beyond evidence** — capture live success when available; otherwise disclose the external quota gate accurately.
3. **Strands use is invisible in the demo** — show `Agent`, `@tool`, and the tool-driven architecture.
4. **Overbuilding consumes the schedule** — enforce the locked vertical slice.
5. **AgentCore destabilizes the baseline** — maintain the non-AgentCore rollback path.
6. **Submission misses an administrative requirement** — use the submission checklist.
7. **Secret/private-data exposure** — complete the final public-repo audit before merge/submission.
8. **Video explains instead of demonstrates** — show the working product early and keep architecture commentary concise.
9. **External quota issue consumes the entire schedule** — continue nonblocked submission work in parallel and preserve a truthful fallback recording path.

## Founder Challenge

Do not confuse “more features” with “more competitive.” The highest-value remaining work is evidence and release readiness: a live AWS response if quota is restored, a reliable public demo, a clean default branch, and a concise working-product video.
