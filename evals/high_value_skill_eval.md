# High Value Skill Eval

Run date: 2026-05-17

## Scope

Representative skills evaluated:

| Skill | Surface | Result |
| --- | --- | --- |
| `prompt-rank-monitor` | AI Search / Agent Discovery | 100/100, grade A, low risk |
| `ad-variant-matrix-builder` | Creative / Ads / Assets | 100/100, grade A, low risk |
| `lead-list-prioritization-scorecard` | Lead Intelligence / Conversion | 100/100, grade A, low risk |
| `campaign-preflight-qa-checklist` | Lifecycle / Ops / Analytics | 100/100, grade A, low risk |
| `marketing-agent-workflow-spec` | Marketing Agents / Governance | 100/100, grade A, low risk |

## What Changed

- Sharpened all skill frontmatter descriptions into explicit `Use when...` trigger language.
- Added focused script behavior tests for the four helper-backed skills.
- Reduced helper script readability warnings that showed up in the initial eval pass.
- Kept detailed mechanics in `references/pattern.md` and left `SKILL.md` compact.

## Real Codex Smoke Test

`prompt-rank-monitor` was run in a fresh ephemeral Codex process with a fictional B2B analytics prompt. The run selected the installed skill, loaded `references/pattern.md`, and returned a prompt-rank monitoring artifact with assumptions, required inputs, QA checks, failure modes, proof metric, and next action.

Token note: the smoke test consumed 30,001 tokens, so the rest of this pass used deterministic local evals instead of running four more full Codex processes.

## Reusable Prompt Set

The prompt set is stored in `evals/high_value_skill_prompts.json`. Each prompt uses fictional inputs and checks for concrete artifacts, QA coverage, failure modes, proof metrics, and next actions.
