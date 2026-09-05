"""Run the read-only AWS preflight followed by the live Strands demo.

This helper is intended for the final human-operated verification gate. It does
not merge, publish, change repository visibility, or send outbound messages.
"""

from __future__ import annotations

import argparse
import subprocess
import sys


def run_step(label: str, command: list[str]) -> int:
    print(f"\n=== {label} ===")
    print("$ " + " ".join(command))
    completed = subprocess.run(command, check=False)
    if completed.returncode == 0:
        print(f"{label}: PASS")
    else:
        print(f"{label}: FAIL (exit {completed.returncode})")
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", default="us-west-2")
    parser.add_argument("--model", default=None)
    args = parser.parse_args()

    preflight = [
        sys.executable,
        "-m",
        "scripts.aws_preflight",
        "--region",
        args.region,
    ]
    if args.model:
        preflight.extend(["--model", args.model])

    if run_step("AWS / Bedrock preflight", preflight) != 0:
        print("\nLIVE VALIDATION: BLOCKED")
        print("Reason: preflight failed. Do not continue to the model invocation.")
        return 1

    demo = [
        sys.executable,
        "-m",
        "scripts.run_demo",
        "--region",
        args.region,
    ]
    if args.model:
        demo.extend(["--model", args.model])

    if run_step("Live Strands demo", demo) != 0:
        print("\nLIVE VALIDATION: FAIL")
        print("Reason: live Strands/Bedrock invocation failed.")
        return 1

    print("\nLIVE VALIDATION: TECHNICAL PASS")
    print("Human review still required: verify score, priority, reasoning, next action,")
    print("draft-only status, and OWNER APPROVAL REQUIRED before any merge/public release.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
