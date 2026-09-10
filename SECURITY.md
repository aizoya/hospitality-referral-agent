# Security Policy — Competition Build

Hospitality Referral Agent is intentionally designed with a narrow human-in-the-loop boundary.

## Core safety boundary

The competition build may:

- analyze referral data
- score and prioritize a referral
- explain scoring factors
- recommend a next action and timing
- draft follow-up text

The competition build may **not** send, schedule, call, or otherwise execute outbound communication. Every follow-up remains draft-only and requires explicit owner approval.

## Credentials and private data

Do not commit or publish:

- AWS access keys or secret keys
- AWS session tokens
- private account identifiers
- private customer or referral records
- real contact details used without permission
- `.env` files or local credential files

Use synthetic referral data for public demonstrations.

The AWS preflight helper intentionally avoids printing caller ARNs and AWS account IDs.

## Public demo deployment

The included browser server is a competition demo surface, not a production web server.

### Safe public baseline

A public judge-facing deployment may expose deterministic offline referral analysis because that path does not require AWS credentials or paid model invocation.

### Live Bedrock path

Do **not** expose an unrestricted public endpoint that can invoke Amazon Bedrock with project credentials. Before enabling live cloud invocation on a public URL, add at minimum:

- authentication or an equivalent judge-access control
- request throttling / rate limiting
- bounded input size
- AWS budget and usage monitoring
- generic user-facing error handling
- server-side credentials only

For the competition video, the live Strands + Bedrock path may be demonstrated from a controlled local or protected environment.

## Error handling

Public deployments should not return raw AWS exceptions or infrastructure details to unauthenticated users. Log operational detail privately and return a generic user-facing failure message.

## Dependency and CI policy

Competition changes should continue to pass:

```bash
pytest -q
python -m scripts.run_demo --score-only
```

GitHub Actions runs these checks on the competition branch and pull requests.

## Reporting a vulnerability

During the competition period, do not publish exploit details in a public issue. Report security concerns privately to the repository owner through an appropriate private channel.
