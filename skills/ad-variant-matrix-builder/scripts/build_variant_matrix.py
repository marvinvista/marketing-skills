#!/usr/bin/env python3
"""Build a creative variant matrix."""

from __future__ import annotations

import argparse
import csv
import itertools
import sys


def split_options(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate creative variants.")
    parser.add_argument("--hooks", required=True, help="comma-separated hooks")
    parser.add_argument("--proof", required=True, help="comma-separated proof points")
    parser.add_argument("--formats", required=True, help="comma-separated formats")
    parser.add_argument("--ctas", required=True, help="comma-separated CTAs")
    parser.add_argument("--limit", type=int, default=60, help="maximum rows")
    args = parser.parse_args()

    rows = itertools.product(
        split_options(args.hooks),
        split_options(args.proof),
        split_options(args.formats),
        split_options(args.ctas),
    )
    writer = csv.writer(sys.stdout)
    writer.writerow(["variant_id", "hook", "proof", "format", "cta", "hypothesis"])
    for index, (hook, proof, fmt, cta) in enumerate(rows, 1):
        if index > args.limit:
            break
        writer.writerow([f"variant-{index:03d}", hook, proof, fmt, cta, f"{hook} plus {proof} should improve {cta}"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
