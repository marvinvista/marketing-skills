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

- Sharpened all skill frontmatter descriptions into concise `Use when...` trigger language.
- Added a skill-specific checklist and boundary to every `SKILL.md` wrapper so the entry layer is no longer just category-level boilerplate.
- Added prompt-to-artifact behavior contracts for all skills, including deep edge-case fixtures for the 10 highest-risk skills.
- Added focused script behavior tests for the four helper-backed skills.
- Reduced helper script readability warnings that showed up in the initial eval pass.
- Kept detailed mechanics in `references/pattern.md` and left `SKILL.md` compact.

## Full Plugin Eval Pass

The full per-skill Plugin Eval run is stored in `evals/plugin_eval_all_skills.md` and `evals/plugin_eval_all_skills.json`.

- Skills evaluated individually: 116
- Gate failures: 0
- Low-risk skills: 116
- Minimum score: 100/100
- Maximum active budget: 532 tokens
- Maximum trigger cost: 52 tokens

## Behavior Contract Pass

The prompt-to-artifact contracts are stored in `evals/all_skill_behavior_contracts.md` and `evals/all_skill_behavior_contracts.json`.

- Skills with contracts: 116
- Deep edge-case fixtures: 10
- Covered fixtures: meta-eval quality, agent autonomy, hallucinated claims, voice drift, answer scoring, share-of-answer aggregation, creative compliance, visitor routing, audience sync, and consent rollback.

## Real Codex Smoke Test

`prompt-rank-monitor` was run in a fresh ephemeral Codex process with a fictional B2B analytics prompt. The run selected the installed skill, loaded `references/pattern.md`, and returned a prompt-rank monitoring artifact with assumptions, required inputs, QA checks, failure modes, proof metric, and next action.

Token note: the smoke test consumed 30,001 tokens, so the rest of this pass used deterministic local evals instead of running four more full Codex processes.

## Reusable Prompt Set

The prompt set is stored in `evals/high_value_skill_prompts.json`. Each prompt uses fictional inputs and checks for concrete artifacts, QA coverage, failure modes, proof metrics, and next actions.
