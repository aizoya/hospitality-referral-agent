# AWS Evening Runbook — Hospitality Referral Agent

Purpose: complete the human-required AWS work in a controlled order after the no-cost competition foundation is green.

## Success criteria

A successful session should produce evidence for judges and reusable learning for future AIZOYA agents:

1. AWS identity and region are confirmed.
2. Amazon Bedrock model access is confirmed in that same region.
3. The repository's one-command live validation succeeds.
4. The browser demo successfully invokes the real Strands agent through Bedrock in an explicitly enabled controlled session.
5. Evidence is captured without exposing credentials or private account data.
6. AgentCore is evaluated only after the core path is stable.

## Human-required gate

Do not paste AWS access keys, secret keys, session tokens, billing identifiers, account IDs, or private credentials into public issues, source files, screenshots, videos, or the repository.

Any action that can create paid infrastructure, change account-level permissions, accept provider terms, submit external company/use-case information, or enable a paid service requires an explicit human decision first.

## Phase 1 — Bedrock proof first

From the repository checkout on `build/strands-vertical-slice`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python -m scripts.live_validation --region <verified-region>
```

Replace `<verified-region>` with the AWS region you intentionally selected and verified for Bedrock access. The live-validation helper now keeps both the preflight and live Strands invocation in that exact same region.

If the configured model requires an explicit model ID, use the repository-supported model argument rather than editing source code.

Expected proof:

- AWS preflight succeeds.
- Strands initializes.
- The scoring tool is used.
- Bedrock returns the agent response.
- The response contains PRIORITY, WHY, NEXT ACTION, DRAFT, and APPROVAL STATUS.
- The output clearly remains draft-only and owner-controlled.

### Account-verification troubleshooting

A successful model-list preflight does not guarantee that Bedrock runtime invocation is immediately enabled for a newly created AWS account.

If the preflight succeeds but the live Strands invocation fails with an `AccessDeniedException` stating that the AWS account is currently being verified:

1. Treat the failure as an AWS account-activation gate, not as an application-code or IAM-policy defect.
2. Do not broaden IAM permissions, create access keys, or change models merely to bypass the message.
3. Wait the interval specified by AWS in the error message, then retry the same command in the same verified region.
4. If the same verification message remains after the stated interval, contact the AWS verification address named in the runtime error.
5. Never include passwords, access keys, MFA secrets, account recovery material, or private credentials in support correspondence.

For the September 5, 2026 validation attempt, the repository tests and read-only Bedrock preflight passed in `us-east-2`, and the first live Strands request reached Bedrock `ConverseStream` before AWS rejected it because the account was still being verified. This is evidence that the local application path and Bedrock discovery path were functioning up to the external account-verification gate.

### Anthropic First Time Use (FTU) gate

After the AWS account-verification message cleared, the next live attempt reached Bedrock and returned a provider-specific `ResourceNotFoundException` stating that use-case details had not yet been submitted for Anthropic models. Treat this as a one-time provider-access gate, not a code failure.

AWS documents that first-time Anthropic customers must submit use-case details once per account or AWS organization before invoking Anthropic models through the Bedrock runtime. The form requires an intended-use description and a website or project URL. Access is expected after the form is successfully submitted.

For this project, the truthful intended-use description should stay narrow and match the competition implementation:

> AIZOYA is building a human-in-the-loop Hospitality Referral Agent for the AWS Agents for Humans Hackathon. The agent helps independent hospitality and food-business operators turn structured referral information into a transparent priority score, explanation, recommended next action, and draft follow-up. The workflow uses AWS Strands Agents and Amazon Bedrock. It does not autonomously send email, SMS, calls, or other outreach; outbound communication remains draft-only and requires explicit owner approval. The project uses synthetic demonstration data for the hackathon and is intended to reduce missed or delayed referral follow-up while preserving human control.

Recommended project URL: the public competition repository or an official AIZOYA website page that accurately describes the project.

Submitting the FTU form is a human-owned external representation and provider-terms gate. Do not submit it automatically.

As of the September 7, 2026 controlled retry, the FTU error no longer recurs. Treat FTU as cleared unless AWS returns that specific provider-onboarding error again.

### Daily-token quota / provisioning troubleshooting

If preflight passes and the live call reaches `Converse` or `ConverseStream` but fails with:

```text
ThrottlingException: Too many tokens per day, please wait before trying again.
```

classify the failure as a Bedrock token-quota or account-provisioning gate rather than an application defect.

Current Strands uses Amazon Bedrock by default and, when this project does not pass an explicit model ID, resolves to the Strands default Claude Sonnet 4.6 inference model. AWS documents that Bedrock runtime inference is controlled by model-level token quotas and that new AWS accounts can receive reduced token-per-day quotas.

For the September 7, 2026 retry in `us-east-2`:

- Bedrock preflight passed.
- AWS credentials were valid.
- Bedrock model discovery succeeded with 91 models visible.
- The live Strands request reached Bedrock `ConverseStream`.
- The earlier Anthropic FTU error did not recur.
- Bedrock rejected the request only with `Too many tokens per day` after its normal retry sequence.

Safe diagnostic sequence:

1. Inspect Amazon Bedrock quotas in **Service Quotas** for the active region.
2. Compare the applied quota with the AWS default for Claude Sonnet 4.6, especially token-per-day and token-per-minute entries.
3. If an applied token-per-day quota is `0` or materially reduced, treat that as account provisioning/quota state.
4. Do not broaden IAM permissions, create access keys, or switch models merely to bypass this condition.
5. Do not request or accept any paid/provisioned capacity change without explicit owner approval.
6. After quota availability changes, rerun the exact same controlled validation command before making application changes.

Read-only CloudShell inspection, when the current IAM role permits Service Quotas reads:

```bash
aws service-quotas list-service-quotas \
  --service-code bedrock \
  --region us-east-2 \
  --query "Quotas[?contains(QuotaName, 'Claude Sonnet 4.6')].[QuotaName,Value,Adjustable,QuotaCode]" \
  --output table
```

This command only reads quota metadata; it does not request or change a quota. If it returns an authorization error, use the AWS Console instead rather than broadening IAM solely for this diagnostic.

## Phase 2 — Browser demonstration

Start the browser in its default offline-safe mode first:

```bash
python -m scripts.run_web_demo
```

Open the printed local address and verify **Analyze referral offline**.

After Phase 1 has passed and only for the controlled AWS session, restart with:

```bash
python -m scripts.run_web_demo --enable-live
```

Then demonstrate **Run live Strands + Bedrock**.

The `--enable-live` flag is intentional. Do not expose an unrestricted public Bedrock invocation endpoint with project credentials.

Capture evidence showing the product surface and agent response, but crop or omit terminal/account information that could reveal private AWS details.

## Phase 3 — AgentCore decision gate

AgentCore is an enhancement, not a prerequisite for the core submission. Evaluate it only when Bedrock validation, tests, and the browser demo are already green.

### Proceed only if

- No change is required to weaken the owner-approval boundary.
- The implementation can be isolated cleanly.
- Estimated AWS cost is understood and acceptable to the human owner.
- Required IAM permissions are understood before changing them.
- The integration can be explained in the demo in one concise sentence.
- The stable non-AgentCore path remains preserved as a rollback point.

### Stop / defer if

- Setup becomes the dominant remaining engineering task.
- It requires broad or unclear IAM permissions.
- Cost cannot be bounded.
- It destabilizes the current working Strands/Bedrock path.
- Judges would not visibly understand the improvement.

## Evidence checklist

Capture only safe evidence:

- successful test result
- successful live validation output
- browser demo showing referral input
- transparent priority score
- live Strands/Bedrock response
- OWNER APPROVAL REQUIRED checkpoint
- architecture diagram
- green GitHub Actions run

Never capture:

- AWS access keys
- secret keys or session tokens
- full account identifiers unless required and safe
- private customer information
- billing/payment details

## Learning log

After the live AWS session, record these items for reuse across future AIZOYA projects:

- exact Strands version used
- Bedrock model and region used
- minimum IAM capabilities actually required
- setup friction encountered
- runtime latency observed
- failure modes encountered
- AgentCore value versus setup complexity
- reusable deployment/security patterns
- reusable human-in-the-loop guardrails

The objective is not only to earn competition points. It is to produce a repeatable AIZOYA reference architecture for future AWS agent projects.
