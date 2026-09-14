# AWS / Bedrock validation evidence — September 13, 2026

Status: `AWS_EXTERNAL_BLOCKER`

This evidence records the latest controlled validation for the Hospitality Referral Agent. It does not claim successful model output.

## AWS Support evidence

AWS Support confirmed that the current Bedrock invocation problem is tied to an account-level eligibility/provisioning restriction and that a request for Amazon Bedrock inference quota provisioning in `us-east-2` was submitted to the internal service team for review. AWS Support also noted the September 14, 2026 hackathon deadline. The review remained pending when this evidence was captured.

The full support correspondence should remain private unless organizers specifically request it.

## Controlled CloudShell validation

Command used:

```bash
cd ~/hospitality-referral-agent && python -m scripts.live_validation --region us-east-2
```

The first attempt exposed a local environment dependency gap (`ModuleNotFoundError: No module named 'strands'`). The repository-declared dependencies were then installed from `requirements.txt`, including `strands-agents`.

After dependency installation, the controlled validation produced the following verified sequence:

1. AWS credentials resolved successfully.
2. Bedrock model discovery succeeded in `us-east-2`.
3. Preflight reported `ready_for_live_attempt: true` and discovered 90 models.
4. The repository's real Strands agent executed far enough to call Amazon Bedrock `ConverseStream`.
5. Bedrock rejected the call with `ThrottlingException: Too many tokens per day, please wait before trying again.`
6. Strands surfaced the rejection as `ModelThrottledException`.
7. No successful live model response was produced.

This establishes the execution path:

`CloudShell -> repository code -> Strands Agents SDK -> authenticated AWS -> Amazon Bedrock ConverseStream -> account-level daily-token throttle`

## Interpretation

The fresh run confirms that the current failure is not the earlier missing-package condition and not a deterministic application test failure. The application reaches the Bedrock runtime and is blocked at the account-level daily-token quota/eligibility gate that AWS Support is already reviewing.

Classification: **external AWS account/provisioning blocker**.

Do not weaken the implementation or security posture to bypass this condition. Specifically:

- do not broaden IAM permissions;
- do not create long-lived access keys;
- do not switch models merely to evade the account restriction;
- do not claim successful live Bedrock inference;
- do not repeatedly retry while AWS Support reports provisioning is pending.

## Local environment note

Installing the current Strands dependency globally in CloudShell upgraded `watchdog` to 6.0.0 while the installed AWS SAM CLI declares `watchdog==4.0.2`. This warning did not prevent the Hospitality Referral Agent validation from reaching Bedrock, but unrelated SAM CLI work should use an isolated environment or restore its expected dependency before relying on that global Python installation.

## Submission-safe statement

AWS Support confirmed an account-level Bedrock eligibility/provisioning restriction and escalated the `us-east-2` inference request for internal review. A fresh controlled CloudShell run on September 13 successfully passed AWS/Bedrock preflight and reached the Bedrock `ConverseStream` runtime through the real Strands agent, where AWS rejected the request with a daily-token throttling error. The project therefore does not claim successful live model output; deterministic functionality, repository implementation, automated tests, and the human-approval boundary are demonstrated separately.
