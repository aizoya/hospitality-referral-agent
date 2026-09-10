# Hospitality Referral Agent — Final Demo Video Recording Package

Target: public YouTube or Vimeo video, under 5 minutes, showing the working project and explaining the problem, audience, solution, and AWS Strands Agents implementation.

## Recording strategy

Use the strongest truthful path available at recording time.

### Path A — AWS eligibility restored

Show the working deterministic/browser demo, the real Strands `Agent` + `@tool` implementation, and one successful live Strands + Bedrock invocation.

### Path B — AWS eligibility still externally blocked

Show the working deterministic/browser demo and the real Strands implementation. Briefly disclose that the newly created AWS account is under AWS account-level Bedrock eligibility review and that the live request reaches `ConverseStream` but cannot complete while the applied account quota remains `0`.

Do not simulate a successful live Bedrock response.

## Teleprompter script

### 0:00–0:25 — Problem

Open on the product, not a title slide.

Hospitality businesses receive valuable referrals through customers, venues, vendors, events, texts, calls, and conversations. During active operations, those opportunities are easy to lose or follow up too late. Hospitality Referral Agent turns a raw referral into prioritized, explainable, owner-ready follow-up work.

### 0:25–1:10 — Working public product

Use the synthetic referral in the public deterministic demo.

Show:
- referral context
- deterministic score and HIGH / MEDIUM / LOW priority
- recommended timing
- transparent scoring components
- `OWNER APPROVAL REQUIRED`
- `DRAFT ONLY — NOTHING HAS BEEN SENT`

Say:

This public judge path proves the deterministic business logic and the human decision boundary without requiring credentials or making any network request. It does not generate or send a message. The live Strands agent is the component that explains the opportunity and prepares a follow-up draft for owner review.

### 1:10–1:55 — Strands implementation

Open `src/referral_agent.py` and show:
- `from strands import Agent, tool`
- `@tool` on `score_referral`
- `Agent(...)` configured with the scoring tool
- system prompt rules requiring tool use and owner approval

Say:

AWS Strands Agents orchestrates the agentic workflow. Before assigning priority, the model must call a transparent deterministic scoring tool. Strands then uses the result to explain the opportunity, recommend the next action, and prepare the draft.

### 1:55–2:40 — AWS / Bedrock proof

#### Path A — successful live inference

Run the controlled Strands + Bedrock path and show the returned response. Highlight the explanation, recommended next action, draft, and approval status.

Say:

This is the real Strands plus Amazon Bedrock path. The agent uses the deterministic score, reasons over the referral context, and prepares an owner-reviewable draft while preserving the approval boundary.

#### Path B — account eligibility still pending

Show only safe, factual evidence: Bedrock preflight/model discovery, Strands implementation, and the externally blocked runtime condition. Do not show account identifiers or support-case details.

Say:

The application path is validated through the Bedrock runtime boundary. AWS credentials resolve, Bedrock model discovery succeeds, and the Strands request reaches Bedrock `ConverseStream`. This newly created AWS account is currently under AWS service-team review for account-level model-invocation eligibility, so I am not presenting a simulated live response.

Keep this explanation under 20 seconds.

### 2:40–3:15 — Human-control architecture

Show the architecture diagram.

Say:

The architecture intentionally separates deterministic business scoring from model reasoning and places a hard human-approval boundary before any outbound action. No email, SMS, call, or message is sent automatically.

### 3:15–3:40 — Quality evidence

Show the latest green GitHub Actions run.

Say:

The project includes automated tests for scoring behavior, the approval boundary, the offline browser path, live-validation control flow, and the static public demo.

### 3:40–4:10 — Why it matters

Say:

Independent hospitality operators are time-constrained and relationship-driven. A warm referral that sits too long can become a missed opportunity. This agent removes repetitive preparation work while preserving the judgment call that belongs to the owner.

### 4:10–4:25 — Close

Say:

Hospitality Referral Agent is an AI referral operator for hospitality businesses: capture context, prioritize transparently, explain the opportunity, prepare the follow-up, and surface the exact moment where a human decision is required.

End with the public repository and project name visible.

## Judge-proof sequence

The recording should visibly establish all five judging dimensions:

1. **Technical Implementation** — real Strands `Agent`, real `@tool`, deterministic scoring, tests, and Bedrock path evidence.
2. **Design** — one coherent referral-to-follow-up workflow with an explicit owner checkpoint.
3. **Potential Impact** — a realistic hospitality workflow and a clearly labeled response-time hypothesis rather than unsupported traction claims.
4. **Creativity & Originality** — a hospitality-specific referral operator combining deterministic business logic with agent reasoning and human control.
5. **Presentation** — product first, end-to-end proof, concise architecture, and a clean close under five minutes.

## Capture checklist

Before recording:
- close unrelated browser tabs
- hide AWS account IDs, billing data, support case information, ARNs, credentials, session tokens, and private customer information
- use synthetic referral data only
- verify the repo is public
- verify the demo is stable
- verify latest CI is green

During recording:
- show the product in the first 10 seconds
- show real working interaction, not only slides
- explicitly name AWS Strands Agents
- show `Agent` and `@tool`
- distinguish the deterministic public demo from the live Strands drafting path
- show the owner-approval checkpoint
- keep AWS support/quota explanation concise if needed
- do not claim a live Bedrock response unless one actually succeeds

Before publishing:
- runtime under 5:00
- audio intelligible
- no private AWS/account information visible
- public YouTube or Vimeo visibility enabled
- title clearly identifies Hospitality Referral Agent / Agents for Humans
- description links to the public repository

## Recommended public video title

Hospitality Referral Agent — AWS Agents for Humans Hackathon | AIZOYA

## Recommended description

Hospitality Referral Agent is a human-in-the-loop AI agent built with AWS Strands Agents for independent hospitality and food businesses. It converts referral context into transparent priority scoring, recommended next actions, and an owner-reviewable follow-up workflow while preserving explicit human approval before any outbound communication.

Public repository: https://github.com/aizoya/hospitality-referral-agent

Built with AWS Strands Agents, Amazon Bedrock, Python, Pytest, and GitHub Actions.

## Stop conditions

Stop the recording and fix the issue if:
- any account ID, credential, token, billing information, or private support-case detail is visible
- the demo behaves differently from the documented workflow
- the approval boundary is missing
- narration claims the public static demo generated a draft or performed a live cloud action
- a live AWS error appears and would require unsupported claims to explain
- runtime exceeds 5 minutes
