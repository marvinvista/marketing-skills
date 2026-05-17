from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_campaign_qa.py"


class CampaignQaTest(unittest.TestCase):
    def test_builds_channel_checks(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--channels", "email,paid"],
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("# Campaign Preflight QA", result.stdout)
        self.assertIn("- [ ] email: Template variables render", result.stdout)
        self.assertIn("- [ ] paid: Landing page message match verified", result.stdout)


if __name__ == "__main__":
    unittest.main()
