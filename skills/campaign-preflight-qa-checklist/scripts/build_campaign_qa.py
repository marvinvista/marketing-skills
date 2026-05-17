#!/usr/bin/env python3
"""Build a campaign preflight QA checklist."""

from __future__ import annotations

import argparse
import sys


BASE_CHECKS = [
    "Audience/exclusions verified",
    "Tracking parameters/events tested",
    "Claim, brand, channel approvals complete",
    "Owner, route, fallback defined",
    "Suppression, consent, rollback confirmed",
]

CHANNEL_CHECKS = {
    "email": ["Template variables render", "Reply route plus unsubscribe work"],
    "paid": ["Budget, bid, conversion event match plan", "Landing page message match verified"],
    "sms": ["Consent status plus quiet hours checked", "Short links plus replies tested"],
    "chat": ["Qualification questions plus human handoff tested", "Fallback response reviewed"],
    "social": ["Post format, tags, approval state checked", "Comment response owner assigned"],
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown campaign QA checklist.")
    parser.add_argument("--channels", required=True, help="comma-separated channels")
    args = parser.parse_args()

    channels = [item.strip().lower() for item in args.channels.split(",") if item.strip()]
    print("# Campaign Preflight QA")
    print("")
    for check in BASE_CHECKS:
        print(f"- [ ] {check}")
    for channel in channels:
        for check in CHANNEL_CHECKS.get(channel, []):
            print(f"- [ ] {channel}: {check}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
