from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "score_leads.py"


class ScoreLeadsTest(unittest.TestCase):
    def test_scores_priority_tiers(self) -> None:
        with tempfile.NamedTemporaryFile("w", newline="", suffix=".csv") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["account", "fit", "intent", "evidence", "urgency", "route"],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "account": "A",
                    "fit": "5",
                    "intent": "5",
                    "evidence": "4",
                    "urgency": "4",
                    "route": "sales",
                }
            )
            writer.writerow(
                {
                    "account": "B",
                    "fit": "1",
                    "intent": "2",
                    "evidence": "1",
                    "urgency": "0",
                    "route": "nurture",
                }
            )
            handle.flush()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), handle.name],
                text=True,
                capture_output=True,
                check=True,
            )
        self.assertIn("A,5,5,4,4,sales,18,high", result.stdout)
        self.assertIn("B,1,2,1,0,nurture,4,low", result.stdout)


if __name__ == "__main__":
    unittest.main()
