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

Any action that can create paid infrastructure, change account-level permissions, or enable a paid service requires an explicit human decision first.

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
