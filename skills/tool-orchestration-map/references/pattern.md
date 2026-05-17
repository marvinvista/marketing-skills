# tool orchestration map

- Category: Marketing Agents / Governance
- Product mechanic: map model calls, tools, data access, human handoffs, and fallback paths
- Output: tool orchestration map
- Evidence surfaces: ai-marketing-agent-workflow

## When To Use

Plan tool use inside marketing workflows with fallback paths.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-marketing-agent-workflow` | bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry | What the agent may draft, route, decide, or escalate; Which gate must pass before expanding autonomy |

## Required Inputs

- Bounded marketing job, allowed tools, and final artifact
- Human judgment points, review owners, and escalation rules
- Brand memory, prompt library, evidence base, and eval criteria
- Telemetry needs, rollout stage, and risk tolerance
- AI marketing agent workflow: Job boundary, final artifact, allowed tools, and unavailable actions
- AI marketing agent workflow: Review owner, escalation rule, eval criteria, telemetry need, and rollout stage
- Specific constraints, examples, and existing assets for tool orchestration map

## Decision Rules

- Scope the agent by job, artifact, allowed actions, and failure mode.
- Put review gates where factuality, claim risk, brand fit, or spend can fail.
- Use evals before expanding autonomy or tool access.
- AI marketing agent workflow: What the agent may draft, route, decide, or escalate
- AI marketing agent workflow: Which gate must pass before expanding autonomy
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `map model calls, tools, data access, human handoffs, and fallback paths` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI marketing agent workflow; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return tool orchestration map with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for tool orchestration map
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: tool orchestration map.
- Organizing mechanic: map model calls, tools, data access, human handoffs, and fallback paths.
- Core fields or sections: model call, tool, input, output, owner, failure mode, fallback, handoff.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI marketing agent workflow: job, input, tool, action right, review gate, fallback, telemetry

## Decision Gates

- AI marketing agent workflow: do not mark the artifact ready until every tool action has an input, output, owner, and fallback.

## QA Checks

- The workflow states what the agent can decide, draft, route, or never do.
- Each tool call has an input, output, owner, and failure fallback.
- Telemetry captures quality, acceptance, rework, and business impact.
- AI marketing agent workflow: Every tool action has an input, output, owner, and fallback.
- AI marketing agent workflow: Risky actions are blocked by review or eval gates.

## Failure Modes

- Designing an agent around a vague role instead of a bounded job.
- Skipping approval because the first demos look plausible.
- Measuring volume without quality, acceptance, or risk metrics.
- AI marketing agent workflow: Defining an agent role without a bounded job and final artifact.

## Proof Metrics

- Acceptance rate
- Review burden and rework rate
- Eval pass rate
- Time saved with quality preserved
- AI marketing agent workflow: eval pass rate
- AI marketing agent workflow: acceptance rate and rework rate

## Example Prompt

Use $tool-orchestration-map to create tool orchestration map for a marketing task in Marketing Agents / Governance. Apply the AI marketing agent workflow mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
