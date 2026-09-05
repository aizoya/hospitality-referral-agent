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

The real Strands + Bedrock workflow remains in `src/referral_agent.py` and is demonstrated from the controlled live environment/video.

## Recommended hosting: GitHub Pages

After the verified competition branch is merged to `main`:

1. Open the repository on GitHub.
2. Open **Settings**.
3. Open **Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch **main**.
6. Select folder **/docs**.
7. Save.
8. Wait for GitHub Pages to report the published URL.
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

For the real agent proof, use one of these controlled paths:

```bash
python -m scripts.live_validation --region us-west-2
```

or, after AWS preflight succeeds:

```bash
python -m scripts.run_web_demo --enable-live
```

The competition video should visibly establish that this is the real Strands + Amazon Bedrock execution path.

## Rollback

If Pages introduces any unexpected issue, do not block the competition submission on it. Preserve the repository, video, and controlled live validation as the required proof path. The static demo is an enhancement, not permission to weaken the live-agent evidence standard.
