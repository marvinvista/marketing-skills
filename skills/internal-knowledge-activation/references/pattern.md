# internal knowledge activation

- Category: Marketing Agents / Governance
- Product mechanic: turn approved docs, calls, data, and research into safe inputs for AI-assisted marketing
- Output: knowledge activation plan
- Evidence surfaces: ai-marketing-agent-workflow, customer-research-synthesis

## When To Use

Activate internal knowledge for marketing AI workflows.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-marketing-agent-workflow` | bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry | What the agent may draft, route, decide, or escalate; Which gate must pass before expanding autonomy |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |

## Required Inputs

- Bounded marketing job, allowed tools, and final artifact
- Human judgment points, review owners, and escalation rules
- Brand memory, prompt library, evidence base, and eval criteria
- Telemetry needs, rollout stage, and risk tolerance
- AI marketing agent workflow: Job boundary, final artifact, allowed tools, and unavailable actions
- AI marketing agent workflow: Review owner, escalation rule, eval criteria, telemetry need, and rollout stage
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Specific constraints, examples, and existing assets for internal knowledge activation

## Decision Rules

- Scope the agent by job, artifact, allowed actions, and failure mode.
- Put review gates where factuality, claim risk, brand fit, or spend can fail.
- Use evals before expanding autonomy or tool access.
- AI marketing agent workflow: What the agent may draft, route, decide, or escalate
- AI marketing agent workflow: Which gate must pass before expanding autonomy
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn approved docs, calls, data, and research into safe inputs for AI-assisted marketing` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI marketing agent workflow, Customer research synthesis; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return knowledge activation plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for internal knowledge activation
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: knowledge activation plan.
- Organizing mechanic: turn approved docs, calls, data, and research into safe inputs for AI-assisted marketing.
- Core fields or sections: approved doc, insight, access boundary, allowed use, claim extraction, owner, freshness, caveat.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI marketing agent workflow: job, input, tool, action right, review gate, fallback, telemetry
- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence

## Decision Gates

- AI marketing agent workflow: do not mark the artifact ready until every tool action has an input, output, owner, and fallback.
- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.

## QA Checks

- The workflow states what the agent can decide, draft, route, or never do.
- Each tool call has an input, output, owner, and failure fallback.
- Telemetry captures quality, acceptance, rework, and business impact.
- AI marketing agent workflow: Every tool action has an input, output, owner, and fallback.
- AI marketing agent workflow: Risky actions are blocked by review or eval gates.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.

## Failure Modes

- Designing an agent around a vague role instead of a bounded job.
- Skipping approval because the first demos look plausible.
- Measuring volume without quality, acceptance, or risk metrics.
- AI marketing agent workflow: Defining an agent role without a bounded job and final artifact.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.

## Proof Metrics

- Acceptance rate
- Review burden and rework rate
- Eval pass rate
- Time saved with quality preserved
- AI marketing agent workflow: eval pass rate
- AI marketing agent workflow: acceptance rate and rework rate
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence

## Example Prompt

Use $internal-knowledge-activation to create knowledge activation plan for a marketing task in Marketing Agents / Governance. Apply the AI marketing agent workflow, Customer research synthesis mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
