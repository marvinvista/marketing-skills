# agentic list building workflow

- Category: Lead Intelligence / Conversion
- Product mechanic: scope an AI workflow for list criteria, evidence lookup, disqualification, routing actions, and review gates
- Output: agentic list building workflow
- Evidence surfaces: ai-marketing-agent-workflow, lead-list-building

## When To Use

Design agent-assisted list building with evidence and routing controls.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-marketing-agent-workflow` | bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry | What the agent may draft, route, decide, or escalate; Which gate must pass before expanding autonomy |
| `lead-list-building` | segment rules, account criteria, exclusions, dedupe logic, and owner routing | Which records qualify for action now; Which gaps block enrichment, routing, or outreach |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- AI marketing agent workflow: Job boundary, final artifact, allowed tools, and unavailable actions
- AI marketing agent workflow: Review owner, escalation rule, eval criteria, telemetry need, and rollout stage
- Lead list building: ICP or segment definition, triggers, disqualifiers, and territory or market limits
- Lead list building: Required list fields, evidence standard, dedupe rule, and owner route
- Specific constraints, examples, and existing assets for agentic list building workflow

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- AI marketing agent workflow: What the agent may draft, route, decide, or escalate
- AI marketing agent workflow: Which gate must pass before expanding autonomy
- Lead list building: Which records qualify for action now
- Lead list building: Which gaps block enrichment, routing, or outreach
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `scope an AI workflow for list criteria, evidence lookup, disqualification, routing actions, and review gates` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI marketing agent workflow, Lead list building; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return agentic list building workflow with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for agentic list building workflow
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: agentic list building workflow.
- Organizing mechanic: scope an AI workflow for list criteria, evidence lookup, disqualification, routing actions, and review gates.
- Core fields or sections: agent job, target segment, list criteria, evidence lookup, disqualifier, routing action, review gate, audit field.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI marketing agent workflow: job, input, tool, action right, review gate, fallback, telemetry
- Lead list building: account or lead, segment, fit reason, trigger, evidence, disqualifier, route

## Decision Gates

- AI marketing agent workflow: do not mark the artifact ready until every tool action has an input, output, owner, and fallback.
- Lead list building: do not mark the artifact ready until every accepted record has fit, trigger, evidence, and a route.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- AI marketing agent workflow: Every tool action has an input, output, owner, and fallback.
- AI marketing agent workflow: Risky actions are blocked by review or eval gates.
- Lead list building: Every accepted record has fit, trigger, evidence, and a route.
- Lead list building: Disqualified records state the rule that removed them.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- AI marketing agent workflow: Defining an agent role without a bounded job and final artifact.
- Lead list building: Building a large list before defining exclusions and evidence standards.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- AI marketing agent workflow: eval pass rate
- AI marketing agent workflow: acceptance rate and rework rate
- Lead list building: qualified record count
- Lead list building: owner acceptance rate

## Example Prompt

Use $agentic-list-building-workflow to create agentic list building workflow for a marketing task in Lead Intelligence / Conversion. Apply the AI marketing agent workflow, Lead list building mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
