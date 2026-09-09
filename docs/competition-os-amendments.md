# AIZOYA Competition Intelligence Amendments

Applies to the Hospitality Referral Agent submission and future AIZOYA hackathon/competition work under AIZOYA OS 2.4.

## Purpose

Convert competition guidance into repeatable operating controls. These amendments do not broaden product scope. They govern prioritization, evidence, presentation, release readiness, and judge traceability.

## 1. COMPETITION-RUBRIC-FIRST

Before feature work is prioritized, map the competition into:

1. eligibility,
2. required technologies,
3. required submission artifacts,
4. judging criteria,
5. optional bonus criteria,
6. official deadline and timezone,
7. evidence required to prove each claim.

A feature or task that does not materially improve a judging dimension, satisfy a submission requirement, reduce a release risk, or strengthen reproducible evidence is lower priority.

## 2. JUDGE-TRACEABILITY MATRIX

Maintain a direct mapping from each judging criterion to evidence.

| Judging dimension | Product evidence | Demo evidence | Submission evidence |
| --- | --- | --- | --- |
| Technical Implementation | Real Strands `Agent`, real `@tool`, deterministic scoring, Bedrock path, tests, human-approval guardrail | Show `Agent`, `@tool`, deterministic tool result, live Bedrock response when available or truthful external-quota evidence | Public repository, architecture, implementation description, validation evidence |
| Design | Narrow referral-to-follow-up workflow, explicit owner approval, judge-facing browser flow | Show referral input → priority → why → next action → draft → approval state | Explain user flow and why the human decision boundary exists |
| Potential Impact | Hospitality-specific use case and measurable response-time hypothesis | Show one realistic synthetic referral and the shortened path to owner-ready follow-up | State impact as a hypothesis unless production evidence exists |
| Creativity & Originality | Agentic referral operator, deterministic business scoring plus model reasoning, relationship-sensitive human control | Contrast autonomous routine work with explicit owner decision points | Avoid generic “lead scoring chatbot” framing |
| Presentation | Working browser demo, architecture diagram, concise implementation | Product first, end-to-end flow, visible guardrail, concise architecture, repository at close | Under-five-minute public video and complete submission fields |

## 3. DETERMINISM-BEFORE-BREADTH

For agent competitions, the default sequence after a working vertical slice is:

**Working → Deterministic → Observable → Demonstrable → Polished → Expanded**

Do not prioritize speculative feature count over predictable behavior, guardrails, tests, execution evidence, recovery paths, and presentation clarity.

For this project, the deterministic `score_referral` tool and owner-approval boundary are competition strengths and should remain visible to judges.

## 4. VISIBLE-GUARDRAILS

Safety and control mechanisms must be demonstrable, not only described.

At least one demo moment should show:

**condition → control → outcome/escalation**

For Hospitality Referral Agent:

- the agent may analyze, prioritize, explain, recommend, and draft;
- outbound communication remains `DRAFT_ONLY_NOT_SENT`;
- owner approval is required before any real-world outreach.

## 5. HUMAN-DECISION-BOUNDARY

Every autonomous-agent competition architecture must explicitly define:

### Agent executes

Routine, bounded, reversible or reviewable work that the system is authorized to perform.

### Human decides

Actions involving consequential judgment, approval, release, sending, payment, legal/contractual commitment, or other owner-only decisions.

The boundary must appear in the architecture, demo, and submission narrative when relevant.

## 6. SUBMISSION-FIRST

Create the submission shell and artifact checklist early. Maintain it continuously as implementation evolves.

Do not defer repository cleanup, README accuracy, architecture, demo script, privacy review, licensing, or final submission fields until the last day.

## 7. HARD-CUTOFF BUFFER

The official competition deadline remains authoritative. AIZOYA's internal target should precede the official cutoff sufficiently to preserve a correction buffer.

For Agents for Humans:

- official submission deadline: September 14, 2026;
- internal target: September 13, 2026;
- September 14 is reserved for correction, verification, and emergency submission recovery rather than planned feature work.

## 8. EVIDENCE-OVER-CLAIMS

Never claim successful cloud execution, deployment, traction, revenue impact, performance, safety, or production readiness without direct evidence.

If a third-party or account-level blocker prevents live proof:

1. classify the blocker accurately,
2. preserve secure architecture and guardrails,
3. show the strongest reproducible evidence available,
4. disclose the limitation succinctly,
5. continue nonblocked submission work in parallel.

For the current AWS Bedrock quota restriction, do not broaden IAM, create long-lived keys, switch models merely to bypass the gate, or simulate a successful response.

## 9. OPTIONAL-BONUS-GATE

Bonus work such as AgentCore deployment or Builder Center content is conditional.

Proceed only after the baseline submission is stable and when the bonus work has a positive expected judging value without threatening release readiness.

## 10. PRESENTATION-FIRST-PROOF

A judge-facing demo should prioritize:

1. problem and user,
2. working product immediately,
3. end-to-end agent workflow,
4. required technology made visible,
5. deterministic control / human decision boundary,
6. concise architecture and quality evidence,
7. impact and originality,
8. clear close.

Do not lead with founder biography, corporate history, a large feature inventory, or lengthy slides before showing the product.

## Project-specific decision

Hospitality Referral Agent remains scope-frozen. The highest-value remaining work is release and evidence readiness:

- successful live Bedrock response if AWS restores usable quota,
- deterministic/local retest after live success,
- verified merge to `main`,
- public judge-facing demo,
- under-five-minute working-product video,
- final Devpost completeness and privacy checks.

AgentCore, additional skills, broader CRM features, calling, payouts, multi-tenant expansion, and unrelated integrations remain deferred unless the baseline is already safe and a direct judging benefit is proven.
