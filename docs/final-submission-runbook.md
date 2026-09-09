# Hospitality Referral Agent — Final Submission Runbook

Purpose: secure a complete, truthful, judge-ready Devpost submission whether or not AWS Bedrock live-inference eligibility is restored before the deadline, while preserving existing security and human-approval guardrails.

## Schedule authority

- Official deadline: September 14, 2026 at 5:00 PM PDT.
- AIZOYA internal submission target: September 13, 2026.
- September 14 is correction/recovery buffer only, not planned feature time.

## Current external AWS gate

AWS Support has confirmed that the live-inference restriction is an account-level eligibility restriction associated with the newly created account. The request is under Bedrock service-team review.

Known evidence in `us-east-2`:

- AWS credentials valid
- Bedrock model discovery succeeds
- Strands reaches Bedrock `ConverseStream`
- earlier AWS account-verification gate cleared
- Anthropic FTU/use-case gate cleared
- Claude Sonnet 4.6 runtime quotas remain `0`
- latest read-only quota re-check shows `L-B29C9321 = 0` and `L-248E47B7 = 0`
- runtime failure: `ThrottlingException: Too many tokens per day, please wait before trying again.`

Do not broaden IAM, create long-lived access keys, switch models merely to bypass the restriction, or claim successful live inference without captured evidence.

## Submission must not depend on AWS restoration

Live Bedrock success is a score enhancer, not a hard prerequisite for a truthful competition submission.

Two release paths are authorized:

### Path A — AWS restored before release lock

1. Re-check quota.
2. Run one controlled live validation.
3. Capture safe evidence.
4. Re-run deterministic tests.
5. Record evidence in PR #1.
6. Merge the verified branch.
7. Enable/verify GitHub Pages.
8. Record the preferred live-proof video.
9. Complete and submit Devpost.

### Path B — AWS still externally blocked at release lock

Use this path no later than the September 13 internal target if AWS has not restored usable inference eligibility.

1. Confirm deterministic/local tests and CI remain green.
2. Confirm the public repository contains the real Strands `Agent`, real `@tool`, architecture, setup instructions, MIT license, and truthful AWS disclosure.
3. Confirm the static judge demo makes no AWS/network requests and visibly preserves owner approval.
4. Record PR #1 evidence that live AWS execution remains externally blocked by account-level quota/eligibility, with no IAM broadening or model switch.
5. Merge the competition branch to `main` once the deterministic release baseline is green and the public package is truthful.
6. Enable and verify GitHub Pages from `main` → `/docs`.
7. Record the fallback working-product video using the deterministic browser demo, Strands implementation, architecture, CI, human-approval boundary, and concise external-quota disclosure.
8. Complete and submit Devpost before the internal target.

Do not let an optional live-cloud proof become a single point of failure for an otherwise compliant submission.

## Controlled live-validation sequence

Run only when AWS indicates the restriction has changed or a read-only quota check shows a non-zero usable quota.

### 1. Re-check quota

```bash
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-2 \
  --query "Quotas[?contains(QuotaName, 'Claude Sonnet 4.6')].[QuotaName,Value,Adjustable,QuotaCode]" \
  --output table
```

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

Capture safe evidence only. Never expose account IDs, ARNs, credentials, session tokens, billing data, support-case details, or private information.

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

## Judge-evidence lock before submission

Every judging dimension must have direct evidence:

| Judging dimension | Required visible evidence |
| --- | --- |
| Technical Implementation | Strands `Agent`, `@tool`, deterministic scoring, Bedrock path evidence, tests/CI, human-approval control |
| Design | Clear referral → priority → explanation → next action → draft → approval flow |
| Potential Impact | Specific hospitality user and clearly labeled response-time hypothesis |
| Creativity & Originality | Hospitality-specific referral operator, deterministic business logic + model reasoning, human decision boundary |
| Presentation | Working product first, concise architecture, end-to-end proof, under-five-minute public video |

If a claim cannot be tied to product, demo, repository, CI, architecture, or other direct evidence, remove or qualify it.

## Final video sequence

Target: 3:30–4:30. Hard maximum: five minutes.

### Preferred path

1. Product/problem in first 10 seconds
2. Deterministic workflow
3. Strands `Agent` + `@tool` proof
4. Successful live Strands + Bedrock proof
5. Human-approval boundary
6. Architecture + green CI
7. Public repository/demo close

### Fallback path

1. Product/problem in first 10 seconds
2. Working deterministic/browser workflow
3. Strands `Agent` + `@tool` proof
4. Brief factual AWS account-level quota disclosure
5. Human-approval boundary
6. Architecture + green CI
7. Public repository/demo close

Never simulate or imply a successful live inference that did not occur.

## Final Devpost checklist

Confirm before submission:

- public repository URL loads without login
- default branch contains the competition build
- README, setup instructions, architecture, source, and MIT license are visible
- public GitHub Pages demo is verified if included
- public YouTube/Vimeo video is under five minutes
- video demonstrates the working product, not only slides
- Strands use is visible and correctly described
- Professional Agents track is selected
- AWS Builder ID/profile information is entered correctly
- technology list is accurate
- architecture diagram is uploaded
- screenshots are safe and current
- pre-existing work disclosure is accurate
- no unsupported traction, revenue, safety, or production-readiness claims
- no private AWS account/support information is visible
- all five judging dimensions have visible evidence
- internal target: September 13, 2026
- official deadline: September 14, 2026 at 5:00 PM PDT

## Stop conditions

Stop and re-diagnose if any of the following appears:

- new IAM/AccessDenied error
- FTU reappears
- live output violates the owner-approval boundary
- tests regress
- CI fails
- secret/private data is exposed
- public demo diverges materially from documented deterministic scoring
- a submission claim exceeds available evidence

Do not compensate for a failed gate by weakening controls or expanding scope.
