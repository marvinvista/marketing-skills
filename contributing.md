# Contributing

## Values

- Keep contributions practical, respectful, and focused on repeatable marketing work.
- Improve the skill pack by making skills easier to trigger, run, validate, and review.
- Prefer small, reviewable changes over broad rewrites.

## Skill Rules

- Keep each skill self-contained and installable.
- Put routing context in the `description` frontmatter.
- Keep `SKILL.md` concise; put detailed rules, templates, checks, and examples in `references/pattern.md`.
- Add scripts only when deterministic execution is meaningfully better than instructions.
- Do not add private research inputs, unpublished links, or identity clues.
- Do not add per-skill README files or process notes.
- Keep the single `skills/` layout.

## Validation

Before opening a pull request, run:

```sh
python3 scripts/validate_skills.py
python3 scripts/smoke_install_skill.py
```

For helper-backed skills, also run the matching tests in `skills/*/tests/`.
