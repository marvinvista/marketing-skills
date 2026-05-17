from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_prompt_rank_table.py"


class PromptRankTableTest(unittest.TestCase):
    def test_builds_markdown_table(self) -> None:
        with tempfile.NamedTemporaryFile("w", newline="", suffix=".csv") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["prompt", "engine", "mentioned", "rank", "citations", "note"],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "prompt": "best tools",
                    "engine": "answer-engine",
                    "mentioned": "yes",
                    "rank": "2",
                    "citations": "2",
                    "note": "Alpha | Beta",
                }
            )
            handle.flush()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), handle.name],
                text=True,
                capture_output=True,
                check=True,
            )
        self.assertIn("| best tools | answer-engine | yes | 2 | 2 | Alpha / Beta |", result.stdout)


if __name__ == "__main__":
    unittest.main()
