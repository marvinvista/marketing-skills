from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_variant_matrix.py"


class VariantMatrixTest(unittest.TestCase):
    def test_limits_variant_rows(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--hooks",
                "speed,proof",
                "--proof",
                "case study",
                "--formats",
                "static,video",
                "--ctas",
                "book demo",
                "--limit",
                "3",
            ],
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("variant_id,hook,proof,format,cta,hypothesis", result.stdout)
        self.assertIn("variant-003", result.stdout)
        self.assertNotIn("variant-004", result.stdout)


if __name__ == "__main__":
    unittest.main()
