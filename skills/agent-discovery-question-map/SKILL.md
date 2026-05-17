---
name: agent-discovery-question-map
description: Use when you need question map, prompt set, and proof inventory to map buyer questions to the answer engines, agents, and proof assets that can influence discovery.
---

# agent discovery question map

## Quick Start

- Produce question map, prompt set, and proof inventory.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: buyer question, persona, intent stage, answer surface.
- Use the artifact to decide: Which prompts need monitoring, remediation, or new proof.
- Do not mark ready until: Observed answer text is separated from interpretation.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return question map, prompt set, and proof inventory. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not question map, prompt set, and proof inventory, the main decision is outside ai-search-visibility-monitoring, answer-source-remediation, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
