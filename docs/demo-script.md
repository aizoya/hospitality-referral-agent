# Hospitality Referral Agent — Competition Demo Script

Target runtime: **3:30–4:30**. Hard maximum: five minutes.

## 1. Problem + product — 30 seconds

Open the browser demo first.

Say:

> Hospitality operators receive valuable referrals through customers, venues, vendors, events, and partners, but during service those opportunities are easy to lose or follow up too late. Hospitality Referral Agent turns one referral into a prioritized, explainable, owner-ready follow-up workflow.

Do not begin with slides or terminal output. Show the product immediately.

## 2. Referral input + offline analysis — 45 seconds

Run the default offline-safe browser mode:

```bash
python -m scripts.run_web_demo
```

Show the synthetic Oakland venue referral and click **Analyze referral offline**.

Highlight:

- score and HIGH / MEDIUM / LOW priority
- transparent scoring factors
- recommended timing
- **OWNER APPROVAL REQUIRED**
- **DRAFT ONLY — NOTHING HAS BEEN SENT**

State that this deterministic path is credential-free and gives judges a reliable fallback even if cloud access is unavailable.

## 3. Show Strands clearly — 40 seconds

Open `src/referral_agent.py` and show only the key lines:

- `from strands import Agent, tool`
- `@tool` on `score_referral`
- `Agent(...)` configured with the scoring tool
- system-prompt rules requiring tool use and owner approval

Say:

> Strands orchestrates the agentic loop. The model must call a transparent business scoring tool before assigning priority, then it explains the result, recommends the next action, and prepares the draft.

Avoid reading code line by line.

## 4. Live Strands + Bedrock proof — 60 seconds

### Preferred path — quota available

After the AWS preflight has already been confirmed, use the controlled live browser mode:

```bash
python -m scripts.run_web_demo --enable-live
```

Click **Run live Strands + Bedrock**.

Alternatively, use the one-command validation path in the verified region:

```bash
python -m scripts.live_validation --region us-east-2
```

Highlight:

- PRIORITY
- WHY
- NEXT ACTION
- DRAFT
- APPROVAL STATUS

State explicitly that this is the real Strands + Amazon Bedrock path.

### Contingency path — AWS account quota still externally blocked

If AWS Support has not restored a non-zero Bedrock daily-token quota before recording, **do not simulate or claim a successful live response**.

Instead, keep this section under 45 seconds and show only safe evidence:

1. the successful AWS/Bedrock preflight (`credentials=true`, model discovery succeeds),
2. the Strands implementation in `src/referral_agent.py`,
3. the controlled runtime error showing Bedrock receives the request but rejects it at the account daily-token quota,
4. the zero/non-adjustable daily-token quota evidence, with account identifiers cropped,
5. the public deterministic demo and green CI as the reproducible judge path.

Say:

> The live request reaches Amazon Bedrock through Strands, but this AWS account currently has a zero, non-adjustable daily-token quota. AWS Support is reviewing that account-level provisioning issue. I am not weakening IAM or switching models to hide the external gate, so the public judge demo stays deterministic and reproducible while preserving the exact same scoring and human-approval boundary.

Do not show the AWS Support case ID, account number, ARNs, credentials, billing details, or private console metadata in the video.

## 5. Human-control boundary — 35 seconds

Point to the visible approval status.

Say:

> The agent can analyze, prioritize, explain, recommend, and draft. It cannot send the message. The owner decides whether to approve, edit, or reject the follow-up.

Show, briefly:

- `approval_required: true`
- `DRAFT_ONLY_NOT_SENT`
- the prompt rule forbidding claims that anything was sent, scheduled, called, or delivered

## 6. Architecture + proof of quality — 35 seconds

Open `docs/architecture.md` and show the narrow referral → Strands → scoring tool → recommendation → approval architecture.

Then show the latest green GitHub Actions run:

- automated tests pass
- deterministic smoke demo passes
- browser safety boundaries are tested

Do not spend time narrating CI internals.

## 7. Close — 25 seconds

Say:

> Hospitality Referral Agent is an AI referral operator for hospitality businesses. It converts fragmented referral context into prioritized, explainable follow-up work and surfaces the exact moment where a human decision is required.

End with the public repository and project name visible.

## Optional AgentCore line

Use this only if AgentCore has been successfully deployed and verified:

> We also deployed the agent through Amazon Bedrock AgentCore to strengthen the production execution path while preserving the same owner-approval boundary.

Do not mention AgentCore as implemented unless it is actually working and demonstrable.

## Recording checklist

- [ ] Total runtime under five minutes
- [ ] Product appears in first 10 seconds
- [ ] Synthetic referral clearly identified
- [ ] Strands `Agent` and `@tool` visible
- [ ] Successful live Bedrock execution visible **or** the external quota gate is disclosed accurately without claiming success
- [ ] Owner-approval boundary visible
- [ ] Green CI visible
- [ ] No AWS account IDs, ARNs, credentials, tokens, support case IDs, private customer data, or billing information visible
- [ ] Public repository visible at close
- [ ] No unsupported production-impact claims
