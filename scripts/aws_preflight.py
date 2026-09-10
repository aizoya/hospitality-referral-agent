"""AWS/Bedrock preflight for the Hospitality Referral Agent.

This script performs read-only checks. It does not invoke a model, send outreach,
or create AWS resources. It also avoids printing AWS account IDs or caller ARNs
so terminal output is safer to show during a competition demo.
"""

from __future__ import annotations

import argparse
import json
import sys

import boto3
from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only AWS credential and Bedrock availability preflight"
    )
    parser.add_argument("--region", default="us-west-2", help="AWS region")
    parser.add_argument(
        "--model",
        default=None,
        help="Optional model ID to confirm is listed in the selected region",
    )
    args = parser.parse_args()

    result: dict[str, object] = {
        "region": args.region,
        "credentials": False,
        "bedrock_list_models": False,
        "model_listed": None,
        "ready_for_live_attempt": False,
        "invoke_permission_verified": False,
    }

    try:
        session = boto3.Session(region_name=args.region)
        session.client("sts").get_caller_identity()
        result["credentials"] = True

        bedrock = session.client("bedrock")
        response = bedrock.list_foundation_models()
        models = [
            item.get("modelId")
            for item in response.get("modelSummaries", [])
            if item.get("modelId")
        ]
        result["bedrock_list_models"] = True
        result["model_count"] = len(models)

        if args.model:
            result["model_listed"] = args.model in models
            result["ready_for_live_attempt"] = bool(result["model_listed"])
        else:
            result["ready_for_live_attempt"] = len(models) > 0

        print(json.dumps(result, indent=2))
        return 0 if result["ready_for_live_attempt"] else 2

    except NoCredentialsError:
        result["error"] = "AWS credentials were not found."
    except (ClientError, BotoCoreError) as exc:
        result["error"] = str(exc)

    print(json.dumps(result, indent=2))
    return 1


if __name__ == "__main__":
    sys.exit(main())
