#!/usr/bin/env python3
"""Validate the anonymized AI marketing skill pack."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
DATA_FILE = REPO_ROOT / "data" / "marketing_skills.json"
SMOKE_INSTALL_SCRIPT = REPO_ROOT / "scripts" / "smoke_install_skill.py"
INSTALL_TEST_SCRIPT = REPO_ROOT / "scripts" / "test_install_sh.py"
INSTALL_SCRIPT = REPO_ROOT / "install.sh"
PUBLIC_REPO_URL = "https://github.com/marvinvista/marketing-skills.git"
PUBLIC_SERVICE_URL = "https://2066labs.com"
ALLOWED_PUBLIC_URLS = [PUBLIC_REPO_URL, PUBLIC_SERVICE_URL]
MIN_SKILL_COUNT = 90
BASE_EXPECTED_FILES = {"SKILL.md", "LICENSE.txt", "agents/openai.yaml", "references/pattern.md"}
REQUIRED_REFERENCE_SECTIONS = [
    "## When To Use",
    "## Product Mechanics",
    "## Required Inputs",
    "## Decision Rules",
    "## Procedure",
    "## Artifact Template",
    "## Skill-Specific Work Product",
    "## Artifact Fields",
    "## Decision Gates",
    "## QA Checks",
    "## Failure Modes",
    "## Proof Metrics",
    "## Example Prompt",
    "## Optional Helper",
    "## Evidence Boundary",
]
LEGACY_FILES = [
    REPO_ROOT / "data" / "marketing_skill_patterns.json",
    REPO_ROOT / "data" / ("y" + "c_ai_marketing_" + "com" + "pan" + "ies.json"),
    REPO_ROOT / "scripts" / "build_yc_ai_marketing_pack.py",
]
DISALLOWED_SKILL_LAYOUT_DIRS = [SKILLS_DIR / ".system", SKILLS_DIR / ".curated"]


IDENTITY_PATTERNS = [
    re.compile(r"com" + r"pan" + r"(?:y|ies)", re.IGNORECASE),
    re.compile(r"y\s+combinator", re.IGNORECASE),
    re.compile(r"y" + r"combinator", re.IGNORECASE),
    re.compile(r"\byc\s+ai\b", re.IGNORECASE),
    re.compile(r"\byc\s+marketing\b", re.IGNORECASE),
    re.compile(r"holo" + r"cron", re.IGNORECASE),
    re.compile(r"private\s+urls?", re.IGNORECASE),
    re.compile(r"source\s+names?", re.IGNORECASE),
    re.compile(r"https?://", re.IGNORECASE),
]
PUBLIC_ID_PATTERNS = [
    re.compile("Feature " + "ID"),
    re.compile("feature" + "_id"),
    re.compile(r"feature-" + r"\d{3}"),
]


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    if set(values) != {"name", "description"}:
        fail(f"frontmatter must contain only name and description: {values.keys()}")
    return values


def openai_yaml_values(text: str) -> dict[str, str]:
    if not text.startswith("interface:\n"):
        fail("agents/openai.yaml must start with interface")
    values: dict[str, str] = {}
    for line in text.splitlines()[1:]:
        if not line.strip():
            continue
        match = re.fullmatch(r"  ([a-z_]+): \"(.*)\"", line)
        if not match:
            fail(f"invalid agents/openai.yaml line: {line}")
        values[match.group(1)] = match.group(2)
    return values


def iter_repo_text_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.suffix in {".pyc", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}:
            continue
        files.append(path)
    return files


def validate_identity_boundary() -> None:
    for path in iter_repo_text_files():
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        for url in ALLOWED_PUBLIC_URLS:
            text = text.replace(url, "")
        for pattern in IDENTITY_PATTERNS:
            if pattern.search(text):
                rel = path.relative_to(REPO_ROOT)
                fail(f"identity boundary term found in {rel}: {pattern.pattern}")


def validate_public_identifier_cleanup() -> None:
    for path in iter_repo_text_files():
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        for pattern in PUBLIC_ID_PATTERNS:
            if pattern.search(text):
                rel = path.relative_to(REPO_ROOT)
                fail(f"public feature identifier found in {rel}")


def validate_skill_files(skill: dict) -> None:
    name = skill["name"]
    skill_dir = SKILLS_DIR / name
    required = [
        skill_dir / "SKILL.md",
        skill_dir / "LICENSE.txt",
        skill_dir / "agents" / "openai.yaml",
        skill_dir / "references" / "pattern.md",
    ]
    if not all(path.exists() for path in required):
        fail(f"missing required skill files for {name}")
    if (skill_dir / "README.md").exists():
        fail(f"per-skill README found in {name}")

    expected_files = set(BASE_EXPECTED_FILES)
    if skill.get("script"):
        expected_files.add(f"scripts/{skill['script']}")
        test_name = f"tests/test_{Path(skill['script']).stem}.py"
        expected_files.add(test_name)
    actual_files = {path.relative_to(skill_dir).as_posix() for path in skill_dir.rglob("*") if path.is_file()}
    unexpected_files = sorted(actual_files - expected_files)
    if unexpected_files:
        fail(f"unexpected files in {name}: {unexpected_files[:5]}")
    if skill.get("script") and f"scripts/{skill['script']}" not in actual_files:
        fail(f"script metadata without script file in {name}")

    skill_md = read(skill_dir / "SKILL.md")
    agent_yaml = read(skill_dir / "agents" / "openai.yaml")
    pattern_md = read(skill_dir / "references" / "pattern.md")
    fm = frontmatter(skill_md)
    if fm["name"] != name:
        fail(f"frontmatter name mismatch in {name}")
    if not fm["description"].startswith("Use when "):
        fail(f"frontmatter description missing trigger phrase in {name}")
    if len(fm["description"]) > 500:
        fail(f"frontmatter description too long in {name}")
    if skill["output"] not in fm["description"]:
        fail(f"frontmatter description missing output trigger in {name}")
    if skill["mechanic"] not in fm["description"]:
        fail(f"frontmatter description missing mechanic trigger in {name}")
    openai_values = openai_yaml_values(agent_yaml)
    if set(openai_values) != {"display_name", "short_description", "default_prompt"}:
        fail(f"agents/openai.yaml fields mismatch in {name}: {sorted(openai_values)}")
    if openai_values["display_name"] != skill["display_name"]:
        fail(f"agents/openai.yaml display_name mismatch in {name}")
    if not openai_values["short_description"]:
        fail(f"agents/openai.yaml short_description missing in {name}")
    if f"${name}" not in openai_values["default_prompt"]:
        fail(f"agents/openai.yaml default_prompt does not mention ${name}")
    if "Product mechanic:" in skill_md:
        fail(f"SKILL.md duplicates product mechanic detail in {name}")
    if "Product mechanic:" not in pattern_md:
        fail(f"references/pattern.md missing product mechanic in {name}")
    license_text = read(skill_dir / "LICENSE.txt")
    if "MIT License" not in license_text or "Marvin Vista" not in license_text:
        fail(f"LICENSE.txt missing expected license text in {name}")
    for section in REQUIRED_REFERENCE_SECTIONS:
        if section not in pattern_md:
            fail(f"references/pattern.md missing {section} in {name}")
    for surface in skill["surfaces"]:
        if surface not in pattern_md:
            fail(f"references/pattern.md missing surface mechanic {surface} in {name}")
    if f"Final artifact: {skill['output']}" not in pattern_md:
        fail(f"references/pattern.md missing skill-specific final artifact in {name}")
    if f"Organizing mechanic: {skill['mechanic']}" not in pattern_md:
        fail(f"references/pattern.md missing skill-specific organizing mechanic in {name}")
    if "Core fields or sections:" not in pattern_md:
        fail(f"references/pattern.md missing skill-specific core fields in {name}")
    if len(pattern_md.splitlines()) < 88:
        fail(f"references/pattern.md too thin for {name}")
    if len(skill_md.splitlines()) > 160:
        fail(f"SKILL.md too long for {name}")
    if skill.get("script"):
        script_path = skill_dir / "scripts" / skill["script"]
        if script_path.suffix != ".py":
            fail(f"helper script must be Python in {name}")
        compile(script_path.read_text(encoding="utf-8"), str(script_path), "exec")
        test_path = skill_dir / "tests" / f"test_{script_path.stem}.py"
        if not test_path.exists():
            fail(f"helper script missing test file in {name}")
        compile(test_path.read_text(encoding="utf-8"), str(test_path), "exec")


def main() -> int:
    if not DATA_FILE.exists():
        fail("missing data/marketing_skills.json")
    for path in LEGACY_FILES:
        if path.exists():
            fail(f"legacy source-shaped file is still present: {path.relative_to(REPO_ROOT)}")
    for path in DISALLOWED_SKILL_LAYOUT_DIRS:
        if path.exists():
            fail(f"unsupported split skill layout found: {path.relative_to(REPO_ROOT)}")

    data = json.loads(read(DATA_FILE))
    skills = data.get("skills", [])
    if data.get("skill_count") != len(skills):
        fail("skill_count does not match skills list")
    if len(skills) < MIN_SKILL_COUNT:
        fail(f"expected at least {MIN_SKILL_COUNT} skills")

    seen_names: set[str] = set()
    skill_dirs = {path.name for path in SKILLS_DIR.iterdir() if path.is_dir()}
    expected_dirs = {item["name"] for item in skills}
    if skill_dirs != expected_dirs:
        missing = sorted(expected_dirs - skill_dirs)[:5]
        extra = sorted(skill_dirs - expected_dirs)[:5]
        fail(f"skill directory mismatch missing={missing} extra={extra}")

    for item in skills:
        name = item["name"]
        if name in seen_names:
            fail(f"duplicate skill name: {name}")
        seen_names.add(name)
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", name):
            fail(f"invalid skill name: {name}")
        for key in ["display_name", "category", "mechanic", "one_line_description", "output", "surfaces"]:
            if not item.get(key):
                fail(f"missing {key} for {name}")
        if len(item["mechanic"].split()) < 8:
            fail(f"mechanic is too generic for {name}")
        if len(item["one_line_description"].split()) < 7:
            fail(f"description is too generic for {name}")
        validate_skill_files(item)

    readme = read(REPO_ROOT / "README.md")
    if not (REPO_ROOT / "contributing.md").exists():
        fail("missing contributing.md")
    if not (REPO_ROOT / "LICENSE").exists():
        fail("missing root LICENSE")
    if not SMOKE_INSTALL_SCRIPT.exists():
        fail("missing installer smoke test")
    if not INSTALL_TEST_SCRIPT.exists():
        fail("missing install.sh smoke test")
    if not INSTALL_SCRIPT.exists():
        fail("missing root install.sh")
    compile(read(SMOKE_INSTALL_SCRIPT), str(SMOKE_INSTALL_SCRIPT), "exec")
    compile(read(INSTALL_TEST_SCRIPT), str(INSTALL_TEST_SCRIPT), "exec")
    install_text = read(INSTALL_SCRIPT)
    if not install_text.startswith("#!/usr/bin/env bash\n"):
        fail("install.sh must use a bash shebang")
    if "CODEX_SKILLS_DIR" not in install_text:
        fail("install.sh must support CODEX_SKILLS_DIR for testable installs")
    if "ln -s" not in install_text:
        fail("install.sh must symlink skill folders")
    if "valid_skill_name" not in install_text or "[a-z0-9][a-z0-9-]{0,63}" not in install_text:
        fail("install.sh must reject path-like or invalid skill names")
    if "## Best First Skills" in readme:
        fail("README still includes Best First Skills")
    if "| Skill | Description |" not in readme:
        fail("README skills table header missing")
    if "| Skill | Category | Description |" in readme:
        fail("README still uses a flat category column instead of grouped categories")
    if "| Skill | Feature | Category | Description |" in readme:
        fail("README still exposes feature column")
    if not readme.startswith("# Marketing Skills\n"):
        fail("README title must be Marketing Skills")
    if ("# AI Marketing " + "Feature Skills") in readme:
        fail("README still uses feature-oriented title")
    if "<details" in readme or "<summary>" in readme or "</details>" in readme:
        fail("README skill catalog must not use expand/collapse details")
    if "## Skill Catalog" in readme:
        fail("README still uses Skill Catalog heading")
    if "## Skills" not in readme:
        fail("README skills section is missing")
    if "Built by Marvin Vista. Need hands-on help? I help teams build AI-ready marketing systems at [2066 Labs](https://2066labs.com)." not in readme:
        fail("README missing public service line")
    if "## Install" not in readme:
        fail("README install section is missing")
    if "./install.sh" not in readme:
        fail("README must use the root install.sh")
    if 'for skill in "$PWD"/skills/*' in readme:
        fail("README still exposes the full install loop")
    if "Manual install:" not in readme:
        fail("README must include a manual install fallback")
    if "## License" not in readme:
        fail("README license section is missing")
    if readme.index("## Skills") > readme.index("## Install"):
        fail("README skills section must appear before install")
    if readme.index("## Skills") > readme.index("## License"):
        fail("README skills section must appear before license")
    catalog = readme.split("## Skills", 1)[1].split("## Install", 1)[0]
    for category in {skill["category"] for skill in skills}:
        if f"### {category}" not in catalog:
            fail(f"README missing category heading: {category}")
    if catalog.count("| [") != len(skills):
        fail("README does not list every skill")
    if "| Source |" in readme:
        fail("README exposes identity columns")

    validate_public_identifier_cleanup()
    validate_identity_boundary()
    print(f"Validated {len(skills)} anonymized marketing skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
