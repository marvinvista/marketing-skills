# Repository Guidance

This is a public Codex skill pack. Keep each skill folder lean, installable, and safe to publish:

- Put only `SKILL.md`, `agents/openai.yaml`, `references/pattern.md`, and justified helper scripts in each skill.
- Treat frontmatter `description` as a routing trigger, not long-form documentation.
- Keep `SKILL.md` concise and operational; put detailed decision rules, artifact templates, QA checks, failure modes, and examples in `references/pattern.md`.
- For helper-backed skills, keep the matching `tests/test_*.py` focused on script behavior only.
- Do not add private research inputs, unpublished links, or identity clues to this repository.
- Keep public wording useful to a marketer or operator who has no background context.
- Do not add per-skill READMEs or process notes.
- Keep the current single `skills/` layout; do not introduce `.system` or `.curated` splits.
- Validate with `python3 scripts/validate_skills.py` before committing.
