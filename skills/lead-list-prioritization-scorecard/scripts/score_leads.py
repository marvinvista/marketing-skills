#!/usr/bin/env python3
"""Score lead records deterministically."""

from __future__ import annotations

import argparse
import csv
import sys


SCORE_FIELDS = ["fit", "intent", "evidence", "urgency"]


def to_int(value: str | None) -> int:
    try:
        return max(0, min(5, int((value or "0").strip())))
    except ValueError:
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Score lead records from CSV.")
    parser.add_argument("csv_path", help="CSV with account, fit, intent, evidence, urgency, route")
    args = parser.parse_args()

    with open(args.csv_path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    fieldnames = list(rows[0].keys()) if rows else ["account", *SCORE_FIELDS, "route"]
    output_fields = [*fieldnames, "priority_score", "priority_tier"]
    writer = csv.DictWriter(sys.stdout, fieldnames=output_fields)
    writer.writeheader()
    for row in rows:
        score = sum(to_int(row.get(field)) for field in SCORE_FIELDS)
        row["priority_score"] = str(score)
        row["priority_tier"] = "high" if score >= 16 else "medium" if score >= 10 else "low"
        writer.writerow(row)
    return 0


if __name__ == "__main__":
    sys.exit(main())
