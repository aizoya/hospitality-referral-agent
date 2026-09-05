"""Run the Hospitality Referral Agent against the included sample referral."""

import argparse
import json
import os
from pathlib import Path

from src.referral_agent import Referral, analyze_referral, score_referral_record


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sample",
        default="examples/sample_referral.json",
        help="Path to a referral JSON file",
    )
    parser.add_argument(
        "--score-only",
        action="store_true",
        help="Run deterministic scoring without AWS/Bedrock credentials",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Optional Bedrock model ID; omit to use Strands default",
    )
    parser.add_argument(
        "--region",
        default=None,
        help="Optional AWS region to use for the live Strands/Bedrock invocation",
    )
    args = parser.parse_args()

    payload = json.loads(Path(args.sample).read_text())

    if args.score_only:
        print(json.dumps(score_referral_record(payload), indent=2))
        return

    if args.region:
        # Keep the live invocation in the exact region that passed preflight.
        os.environ["AWS_REGION"] = args.region
        os.environ["AWS_DEFAULT_REGION"] = args.region

    referral = Referral(**payload)
    print(analyze_referral(referral, model=args.model))


if __name__ == "__main__":
    main()
