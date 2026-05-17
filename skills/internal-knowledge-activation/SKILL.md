---
name: internal-knowledge-activation
description: Use when you need knowledge activation plan to turn approved docs, calls, data, and research into safe inputs for AI-assisted marketing.
---

# internal knowledge activation

## Quick Start

- Produce knowledge activation plan.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: approved doc, insight, access boundary, allowed use.
- Use the artifact to decide: What the agent may draft, route, decide, or escalate.
- Do not mark ready until: Every tool action has an input, output, owner, and fallback.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return knowledge activation plan. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not knowledge activation plan, the main decision is outside ai-marketing-agent-workflow, customer-research-synthesis, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
