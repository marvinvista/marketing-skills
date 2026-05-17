#!/usr/bin/env python3
"""Build a prompt-rank table from answer observations."""

from __future__ import annotations

import argparse
import csv
import sys


FIELDS = ["prompt", "engine", "mentioned", "rank", "citations", "note"]


def clean(value: str | None) -> str:
    return (value or "").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Markdown prompt-rank table from CSV.")
    parser.add_argument("csv_path", help="CSV with prompt, engine, mentioned, rank, citations, note")
    args = parser.parse_args()

    with open(args.csv_path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    missing = [field for field in FIELDS if rows and field not in rows[0]]
    if missing:
        raise SystemExit(f"missing columns: {', '.join(missing)}")

    print("| Prompt | Engine | Mentioned | Rank | Citations | Note |")
    print("| --- | --- | --- | ---: | --- | --- |")
    for row in rows:
        values = [clean(row.get(field)).replace("|", "/") for field in FIELDS]
        values[3] = values[3] or "0"
        print("| " + " | ".join(values) + " |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
