#!/usr/bin/env python3
"""Smoke-test that a skill folder can be installed from this pack layout."""

from __future__ import annotations

import argparse
import shutil
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL = "prompt-rank-monitor"
REPO_PATH = "marvinvista/marketing-skills"
REF = "main"


def fail(message: str) -> None:
    raise SystemExit(f"smoke install failed: {message}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def skill_name_from_frontmatter(skill_md: str) -> str:
    if not skill_md.startswith("---\n"):
        fail("installed SKILL.md missing frontmatter")
    end = skill_md.find("\n---\n", 4)
    if end == -1:
        fail("installed SKILL.md frontmatter is not closed")
    for line in skill_md[4:end].splitlines():
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip()
    fail("installed SKILL.md missing name")


def smoke_install(skill_name: str, dest_root: Path) -> Path:
    skill_path = REPO_ROOT / "skills" / skill_name
    if not skill_path.is_dir():
        fail(f"missing skill path: skills/{skill_name}")

    dest = dest_root / skill_name
    if dest.exists():
        fail(f"destination already exists: {dest}")
    shutil.copytree(skill_path, dest)

    required = [
        dest / "SKILL.md",
        dest / "LICENSE.txt",
        dest / "agents" / "openai.yaml",
        dest / "references" / "pattern.md",
    ]
    missing = [path.relative_to(dest).as_posix() for path in required if not path.exists()]
    if missing:
        fail(f"installed skill missing files: {missing}")

    installed_name = skill_name_from_frontmatter(read(dest / "SKILL.md"))
    if installed_name != skill_name:
        fail(f"installed skill name mismatch: {installed_name}")

    openai_yaml = read(dest / "agents" / "openai.yaml")
    if f"${skill_name}" not in openai_yaml:
        fail("installed agents/openai.yaml default prompt does not mention the skill")

    return dest


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-test local installability for one marketing skill")
    parser.add_argument("--skill", default=DEFAULT_SKILL, help="skill folder name to smoke-test")
    parser.add_argument("--dest", type=Path, help="optional destination root, defaults to a temporary directory")
    args = parser.parse_args()

    if args.dest:
        args.dest.mkdir(parents=True, exist_ok=True)
        installed = smoke_install(args.skill, args.dest)
        print(f"Installed {args.skill} into {installed}")
    else:
        with tempfile.TemporaryDirectory(prefix="marketing-skills-install-") as tmp:
            installed = smoke_install(args.skill, Path(tmp))
            print(f"Installed {args.skill} into {installed}")

    print(f"GitHub path checked: {REPO_PATH}/tree/{REF}/skills/{args.skill}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
