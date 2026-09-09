# Hospitality Referral Agent — Final Submission Runbook

Purpose: minimize elapsed time between AWS Bedrock eligibility restoration and final Devpost submission while preserving the existing release and security guardrails.

## Current external gate

AWS Support has confirmed that the live-inference restriction is an account-level eligibility restriction associated with the account being newly created. The request is under Bedrock service-team review.

Known evidence in `us-east-2`:

- AWS credentials valid
- Bedrock model discovery succeeds
- Strands reaches Bedrock `ConverseStream`
- earlier AWS account-verification gate cleared
- Anthropic FTU/use-case gate cleared
- Claude Sonnet 4.6 runtime quotas remain `0`
- latest read-only quota re-check still shows `L-B29C9321 = 0` and `L-248E47B7 = 0`
- runtime failure: `ThrottlingException: Too many tokens per day, please wait before trying again.`
- AWS Support case status text may change during review; do not treat a support workflow label as proof that invocation eligibility is restored

Do not broaden IAM, create long-lived access keys, switch models merely to bypass the restriction, or merge PR #1 while this gate remains unresolved.

## Work that can proceed while AWS review is pending

Do not wait idly on AWS. Continue the submission package in parallel:

- complete all Devpost fields that do not require a final video URL
- prepare the public image gallery and architecture upload
- keep the public repository clean and CI green
- prepare the final video shot list, narration, and truthful contingency wording
- verify AWS Builder ID / Builder Center profile information
- prepare final public-link and submission QA

A video may be recorded using the working deterministic/browser product path if needed. If AWS live inference is still externally blocked at recording time, disclose that condition briefly and accurately; never simulate or imply a successful live response.

## Trigger to resume live-release sequence

Resume the live-release sequence only after AWS indicates the restriction has been reviewed/changed, or after a read-only quota check shows a non-zero usable quota.

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
- no FTU, account-verification, IAM, eligibility, or daily-token error appears
- output remains owner-controlled and draft-only

Capture safe evidence only. Do not expose account IDs, ARNs, credentials, session tokens, billing data, support-case details, or private information.

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

- quota / eligibility status after AWS review
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

Preferred sequence if AWS eligibility is restored:

1. Product/problem in first 10 seconds
2. Static/offline deterministic workflow
3. Strands `Agent` + `@tool` proof
4. Successful live Strands + Bedrock proof
5. Human-approval boundary
6. Architecture + latest green CI
7. Public repository/demo close

Fallback sequence if AWS remains externally blocked:

1. Product/problem in first 10 seconds
2. Working deterministic/browser workflow
3. Strands `Agent` + `@tool` implementation proof
4. Brief factual disclosure that the new AWS account is under Bedrock invocation eligibility review
5. Human-approval boundary
6. Architecture + latest green CI
7. Public repository/demo close

Never simulate or claim a successful live inference that did not occur.

### 8. Final Devpost checklist

Confirm before submission:

- public repository URL
- public demo URL if available
- public YouTube/Vimeo video under five minutes
- final project description proofread
- Professional Agents track selection verified
- AWS Builder ID entered
- technology list accurate
- screenshots safe and current
- architecture diagram uploaded
- pre-existing work disclosure accurate
- no unsupported traction/revenue claims
- deadline: September 14, 2026 at 5:00 PM PDT

## Stop conditions

Stop and re-diagnose if any of the following appears:

- a new IAM/AccessDenied error
- FTU reappears
- quota remains zero after AWS says provisioning/eligibility is complete
- live output violates the owner-approval boundary
- tests regress
- any secret/private data is exposed

Do not compensate for a failed gate by weakening controls.
