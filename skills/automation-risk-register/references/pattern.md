# automation risk register

- Category: Marketing Agents / Governance
- Product mechanic: identify automation risks, mitigations, owners, monitoring, escalation, and rollback
- Output: automation risk register
- Evidence surfaces: ai-marketing-agent-workflow, brand-governance-review, marketing-ops-orchestration

## When To Use

Manage risk in marketing automation and AI workflows.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-marketing-agent-workflow` | bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry | What the agent may draft, route, decide, or escalate; Which gate must pass before expanding autonomy |
| `brand-governance-review` | claims, proof, voice, compliance risk, platform limits, and approval state | What can publish, what needs edits, and what needs explicit approval; Which recurring issue should be added to voice or claim memory |
| `marketing-ops-orchestration` | owners, dependencies, systems, approvals, launch states, fallback paths, and rollback | Which work can launch, wait, or roll back; Which owner or dependency blocks the next action |

## Required Inputs

- Bounded marketing job, allowed tools, and final artifact
- Human judgment points, review owners, and escalation rules
- Brand memory, prompt library, evidence base, and eval criteria
- Telemetry needs, rollout stage, and risk tolerance
- AI marketing agent workflow: Job boundary, final artifact, allowed tools, and unavailable actions
- AI marketing agent workflow: Review owner, escalation rule, eval criteria, telemetry need, and rollout stage
- Brand governance review: Brand voice, approved claims, banned patterns, legal or policy constraints
- Brand governance review: Draft asset, channel, proof links or notes, reviewer, and required approval level
- Marketing ops orchestration: Workflow boundary, systems involved, owner map, launch date, and dependency list
- Marketing ops orchestration: Approval needs, fallback path, rollback trigger, and status reporting cadence
- Specific constraints, examples, and existing assets for automation risk register

## Decision Rules

- Scope the agent by job, artifact, allowed actions, and failure mode.
- Put review gates where factuality, claim risk, brand fit, or spend can fail.
- Use evals before expanding autonomy or tool access.
- AI marketing agent workflow: What the agent may draft, route, decide, or escalate
- AI marketing agent workflow: Which gate must pass before expanding autonomy
- Brand governance review: What can publish, what needs edits, and what needs explicit approval
- Brand governance review: Which recurring issue should be added to voice or claim memory
- Marketing ops orchestration: Which work can launch, wait, or roll back
- Marketing ops orchestration: Which owner or dependency blocks the next action
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `identify automation risks, mitigations, owners, monitoring, escalation, and rollback` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI marketing agent workflow, Brand governance review, Marketing ops orchestration; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return automation risk register with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for automation risk register
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: automation risk register.
- Organizing mechanic: identify automation risks, mitigations, owners, monitoring, escalation, and rollback.
- Core fields or sections: risk, trigger, affected workflow, mitigation, owner, monitor, escalation, rollback.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI marketing agent workflow: job, input, tool, action right, review gate, fallback, telemetry
- Brand governance review: claim, proof, risk level, voice issue, required edit, owner, approval state
- Marketing ops orchestration: workstream, owner, dependency, system, approval, fallback, rollback, status

## Decision Gates

- AI marketing agent workflow: do not mark the artifact ready until every tool action has an input, output, owner, and fallback.
- Brand governance review: do not mark the artifact ready until unsupported claims are blocked or rewritten before launch.
- Marketing ops orchestration: do not mark the artifact ready until every dependency has an owner and failure fallback.

## QA Checks

- The workflow states what the agent can decide, draft, route, or never do.
- Each tool call has an input, output, owner, and failure fallback.
- Telemetry captures quality, acceptance, rework, and business impact.
- AI marketing agent workflow: Every tool action has an input, output, owner, and fallback.
- AI marketing agent workflow: Risky actions are blocked by review or eval gates.
- Brand governance review: Unsupported claims are blocked or rewritten before launch.
- Brand governance review: Edits preserve intent while removing risk.
- Marketing ops orchestration: Every dependency has an owner and failure fallback.
- Marketing ops orchestration: Launch and rollback criteria are visible before execution.

## Failure Modes

- Designing an agent around a vague role instead of a bounded job.
- Skipping approval because the first demos look plausible.
- Measuring volume without quality, acceptance, or risk metrics.
- AI marketing agent workflow: Defining an agent role without a bounded job and final artifact.
- Brand governance review: Treating brand review as tone cleanup while ignoring proof and risk.
- Marketing ops orchestration: Shipping a workflow with unclear ownership or rollback responsibility.

## Proof Metrics

- Acceptance rate
- Review burden and rework rate
- Eval pass rate
- Time saved with quality preserved
- AI marketing agent workflow: eval pass rate
- AI marketing agent workflow: acceptance rate and rework rate
- Brand governance review: review issue count
- Brand governance review: approval turnaround time
- Marketing ops orchestration: cycle time
- Marketing ops orchestration: handoff completion and rollback readiness

## Example Prompt

Use $automation-risk-register to create automation risk register for a marketing task in Marketing Agents / Governance. Apply the AI marketing agent workflow, Brand governance review, Marketing ops orchestration mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
