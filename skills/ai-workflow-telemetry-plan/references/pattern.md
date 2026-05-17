# AI workflow telemetry plan

- Category: Marketing Agents / Governance
- Product mechanic: define quality, throughput, review, acceptance, rework, and business-impact telemetry
- Output: AI workflow telemetry plan
- Evidence surfaces: ai-marketing-agent-workflow, campaign-analytics-qa

## When To Use

Measure AI workflow performance beyond output volume.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-marketing-agent-workflow` | bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry | What the agent may draft, route, decide, or escalate; Which gate must pass before expanding autonomy |
| `campaign-analytics-qa` | UTMs, events, conversion paths, dashboards, attribution fields, expected values, and readout decisions | Which metrics are trustworthy enough for a decision; Which tracking gaps block launch or interpretation |

## Required Inputs

- Bounded marketing job, allowed tools, and final artifact
- Human judgment points, review owners, and escalation rules
- Brand memory, prompt library, evidence base, and eval criteria
- Telemetry needs, rollout stage, and risk tolerance
- AI marketing agent workflow: Job boundary, final artifact, allowed tools, and unavailable actions
- AI marketing agent workflow: Review owner, escalation rule, eval criteria, telemetry need, and rollout stage
- Campaign analytics QA: Campaign plan, channels, events, conversion definition, dashboard, and owner
- Campaign analytics QA: Expected values, test records, attribution rules, data freshness, and decision cadence
- Specific constraints, examples, and existing assets for AI workflow telemetry plan

## Decision Rules

- Scope the agent by job, artifact, allowed actions, and failure mode.
- Put review gates where factuality, claim risk, brand fit, or spend can fail.
- Use evals before expanding autonomy or tool access.
- AI marketing agent workflow: What the agent may draft, route, decide, or escalate
- AI marketing agent workflow: Which gate must pass before expanding autonomy
- Campaign analytics QA: Which metrics are trustworthy enough for a decision
- Campaign analytics QA: Which tracking gaps block launch or interpretation
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `define quality, throughput, review, acceptance, rework, and business-impact telemetry` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI marketing agent workflow, Campaign analytics QA; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return AI workflow telemetry plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for AI workflow telemetry plan
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: AI workflow telemetry plan.
- Organizing mechanic: define quality, throughput, review, acceptance, rework, and business-impact telemetry.
- Core fields or sections: workflow step, quality metric, acceptance signal, rework reason, throughput, business impact, review cadence.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI marketing agent workflow: job, input, tool, action right, review gate, fallback, telemetry
- Campaign analytics QA: event, parameter, expected value, observed value, owner, status, decision impact

## Decision Gates

- AI marketing agent workflow: do not mark the artifact ready until every tool action has an input, output, owner, and fallback.
- Campaign analytics QA: do not mark the artifact ready until tracking is tested before performance interpretation.

## QA Checks

- The workflow states what the agent can decide, draft, route, or never do.
- Each tool call has an input, output, owner, and failure fallback.
- Telemetry captures quality, acceptance, rework, and business impact.
- AI marketing agent workflow: Every tool action has an input, output, owner, and fallback.
- AI marketing agent workflow: Risky actions are blocked by review or eval gates.
- Campaign analytics QA: Tracking is tested before performance interpretation.
- Campaign analytics QA: Each metric states the decision it can change.

## Failure Modes

- Designing an agent around a vague role instead of a bounded job.
- Skipping approval because the first demos look plausible.
- Measuring volume without quality, acceptance, or risk metrics.
- AI marketing agent workflow: Defining an agent role without a bounded job and final artifact.
- Campaign analytics QA: Reading campaign performance before verifying event and attribution integrity.

## Proof Metrics

- Acceptance rate
- Review burden and rework rate
- Eval pass rate
- Time saved with quality preserved
- AI marketing agent workflow: eval pass rate
- AI marketing agent workflow: acceptance rate and rework rate
- Campaign analytics QA: QA pass rate
- Campaign analytics QA: attribution coverage and data freshness

## Example Prompt

Use $ai-workflow-telemetry-plan to create AI workflow telemetry plan for a marketing task in Marketing Agents / Governance. Apply the AI marketing agent workflow, Campaign analytics QA mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
