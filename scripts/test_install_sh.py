#!/usr/bin/env python3
"""Exercise install.sh against a temporary skills destination."""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
INSTALL_SCRIPT = REPO_ROOT / "install.sh"
DEFAULT_SKILL = "prompt-rank-monitor"


def run_installer(dest: Path, *args: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["CODEX_SKILLS_DIR"] = str(dest)
    return subprocess.run(
        [str(INSTALL_SCRIPT), *args],
        cwd=REPO_ROOT,
        env=env,
        check=True,
        text=True,
        capture_output=True,
    )


def assert_link(dest: Path, skill_name: str) -> None:
    link = dest / skill_name
    expected = REPO_ROOT / "skills" / skill_name
    if not link.is_symlink():
        raise SystemExit(f"expected symlink: {link}")
    if link.resolve() != expected.resolve():
        raise SystemExit(f"wrong symlink target for {skill_name}: {link.resolve()}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="marketing-skills-install-") as tmp:
        dest = Path(tmp) / "skills"

        one = run_installer(dest, DEFAULT_SKILL)
        if f"Installed: {DEFAULT_SKILL}" not in one.stdout:
            raise SystemExit("single-skill install did not report installation")
        assert_link(dest, DEFAULT_SKILL)

        again = run_installer(dest, DEFAULT_SKILL)
        if f"Already installed: {DEFAULT_SKILL}" not in again.stdout:
            raise SystemExit("single-skill reinstall was not idempotent")

        all_result = run_installer(dest)
        if "Installed " not in all_result.stdout:
            raise SystemExit("all-skill install did not print a summary")

        skill_count = len([path for path in (REPO_ROOT / "skills").iterdir() if path.is_dir()])
        installed_count = len([path for path in dest.iterdir() if path.is_symlink()])
        if installed_count != skill_count:
            raise SystemExit(f"installed {installed_count} symlinks, expected {skill_count}")

        invalid = subprocess.run(
            [str(INSTALL_SCRIPT), "../data"],
            cwd=REPO_ROOT,
            env={**os.environ, "CODEX_SKILLS_DIR": str(dest)},
            text=True,
            capture_output=True,
        )
        if invalid.returncode == 0:
            raise SystemExit("invalid skill name unexpectedly succeeded")
        if (Path(tmp) / "data").exists():
            raise SystemExit("invalid skill name created a path outside the skills destination")

    print("install.sh smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
