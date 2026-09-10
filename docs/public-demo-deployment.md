# Public Judge Demo Deployment

## Goal

Provide judges a public, zero-cost, offline-safe product surface without exposing project AWS credentials or creating an unrestricted Amazon Bedrock invocation endpoint.

## Prepared asset

`docs/index.html` is a static interactive demo that:

- uses synthetic hospitality referral data
- runs deterministic referral scoring entirely in the browser
- shows score, priority, timing, and scoring components
- displays `OWNER APPROVAL REQUIRED`
- displays `DRAFT ONLY — NOTHING HAS BEEN SENT`
- makes no network or AWS requests
- does not generate or send outbound communication

The real Strands + Bedrock workflow remains in `src/referral_agent.py` and is demonstrated from the controlled environment when live AWS eligibility is available.

## Recommended hosting: GitHub Pages

After the verified competition branch is merged to `main`:

1. Open the repository on GitHub.
2. Open **Settings**.
3. Open **Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch **main**.
6. Select folder **/docs**.
7. Save.
8. Confirm GitHub Pages reports the published URL.
9. Open the URL on mobile and desktop.
10. Submit the form once and confirm the result is visible.

## Release QA

Before putting the URL in Devpost:

- confirm the page loads without authentication
- confirm no AWS credentials are required
- confirm no network/model request occurs when analyzing the referral
- confirm the sample data is synthetic
- confirm score and priority render
- confirm `OWNER APPROVAL REQUIRED` is visible
- confirm `DRAFT ONLY — NOTHING HAS BEEN SENT` is visible
- confirm layout works on a phone-sized viewport
- confirm the public repository link used in Devpost points to `main`

## Live AWS demonstration

Do not modify the static public demo to embed AWS credentials or call Bedrock directly from client-side JavaScript.

The verified project region is **`us-east-2`**. Preserve that path unless a separately validated change is intentionally approved.

### Path A — AWS live eligibility restored

Use one of these controlled paths:

```bash
python -m scripts.live_validation --region us-east-2
```

or, after AWS preflight succeeds:

```bash
python -m scripts.run_web_demo --enable-live
```

The competition video may then show the actual successful Strands + Amazon Bedrock execution path.

### Path B — AWS account-level eligibility still externally blocked

Do not switch regions, broaden IAM, create access keys, switch models merely to bypass the restriction, or simulate a successful live response.

Use the deterministic public demo, real Strands implementation, architecture, green CI, and concise truthful disclosure of the external Bedrock eligibility/quota condition as the judge evidence path.

## Rollback

If Pages introduces any unexpected issue, do not block the competition submission on it. Preserve the public repository, video, deterministic test evidence, and controlled Strands implementation as the core proof package. The static demo is a scoring enhancement, not permission to weaken security or make unsupported cloud-execution claims.
