# Hospitality Referral Agent — Final Submission Runbook

Purpose: minimize elapsed time between AWS Bedrock quota restoration and final Devpost submission while preserving the existing release and security guardrails.

## Current external gate

AWS Support has confirmed that the Bedrock restriction is associated with the account being newly created and has submitted the request to the Bedrock service team for review.

Known evidence in `us-east-2`:

- AWS credentials valid
- Bedrock model discovery succeeds
- Strands reaches Bedrock `ConverseStream`
- Anthropic FTU/use-case gate cleared
- Claude Sonnet 4.6 daily-token quota currently `0`
- runtime failure: `ThrottlingException: Too many tokens per day, please wait before trying again.`

Do not broaden IAM, create long-lived access keys, switch models merely to bypass the restriction, or merge PR #1 while this gate remains unresolved.

## Trigger to resume release

Resume this runbook only after AWS indicates the restriction has been reviewed/changed, or after a read-only quota check shows a non-zero usable quota.

### 1. Re-check quota

```bash
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-2 \
  --query "Quotas[?contains(QuotaName, 'Claude Sonnet 4.6')].[QuotaName,Value,Adjustable,QuotaCode]" \
  --output table
```

Acceptance: the relevant runtime quota is no longer zero, or AWS explicitly confirms the account is enabled for live inference.

### 2. Run one controlled live validation

```bash
cd ~/hospitality-referral-agent
source .venv/bin/activate
python -m scripts.live_validation --region us-east-2
```

Acceptance:

- AWS/Bedrock preflight passes
- Strands live invocation returns a valid model response
- no FTU, account-verification, IAM, or daily-token error appears
- output remains owner-controlled and draft-only

Capture safe evidence only. Do not expose account IDs, ARNs, credentials, session tokens, billing data, or private information.

### 3. Re-run deterministic baseline

```bash
pytest -q
python -m scripts.run_demo --score-only
```

Acceptance:

- full test suite passes
- deterministic sample remains stable
- `approval_required` remains true
- outbound status remains `DRAFT_ONLY_NOT_SENT`

### 4. Record release evidence in PR #1

Record:

- quota status after AWS review
- successful live validation timestamp/result
- local test result
- CI status
- confirmation that no IAM broadening/model switch was used

### 5. Merge PR #1

Only after steps 1–4 are green.

Merge the verified competition branch into `main`. Do not add new feature scope during this step.

### 6. Enable and verify GitHub Pages

Source: `main` → `/docs`

Verify:

- public page loads on desktop and mobile
- synthetic sample is clearly labeled
- deterministic analysis works
- no network/AWS requests are made by the static public demo
- owner-approval language is visible
- no secrets/private data are exposed

### 7. Record final video

Target: under five minutes.

Required sequence:

1. Product/problem in first 10 seconds
2. Static/offline deterministic workflow
3. Strands `Agent` + `@tool` proof
4. Successful live Strands + Bedrock proof
5. Human-approval boundary
6. Architecture + latest green CI
7. Public repository/demo close

If AWS remains externally blocked near the deadline, use the truthful contingency in `docs/demo-script.md`; do not simulate or claim a successful live inference that did not occur.

### 8. Final Devpost checklist

Confirm before submission:

- public repository URL
- public demo URL
- public YouTube/Vimeo video under five minutes
- final project description proofread
- Professional Agents track selection verified
- AWS Builder ID entered
- technology list accurate
- screenshots safe and current
- pre-existing work disclosure accurate
- no unsupported traction/revenue claims
- deadline: September 14, 2026 at 5:00 PM PDT

## Stop conditions

Stop and re-diagnose if any of the following appears:

- a new IAM/AccessDenied error
- FTU reappears
- quota remains zero after AWS says provisioning is complete
- live output violates the owner-approval boundary
- tests regress
- any secret/private data is exposed

Do not compensate for a failed gate by weakening controls.
