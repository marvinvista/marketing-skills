# agentic SEO briefing workflow

- Category: Marketing Agents / Governance
- Product mechanic: scope an AI workflow for target queries, proof lookup, brief drafting, schema actions, review gates, and publish handoff
- Output: agentic SEO briefing workflow
- Evidence surfaces: ai-marketing-agent-workflow, seo-content-briefing

## When To Use

Design agent-assisted SEO and answer-ready content briefing.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-marketing-agent-workflow` | bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry | What the agent may draft, route, decide, or escalate; Which gate must pass before expanding autonomy |
| `seo-content-briefing` | questions, search intent, answer gaps, proof, page type, schema, and crawl paths | Which page, section, or proof asset should be created or refreshed; Which structured data or crawl fix must ship with content |

## Required Inputs

- Bounded marketing job, allowed tools, and final artifact
- Human judgment points, review owners, and escalation rules
- Brand memory, prompt library, evidence base, and eval criteria
- Telemetry needs, rollout stage, and risk tolerance
- AI marketing agent workflow: Job boundary, final artifact, allowed tools, and unavailable actions
- AI marketing agent workflow: Review owner, escalation rule, eval criteria, telemetry need, and rollout stage
- SEO content briefing: Target queries or questions, page inventory, audience intent, and desired answer
- SEO content briefing: Proof assets, comparison gaps, schema needs, internal links, and crawl constraints
- Specific constraints, examples, and existing assets for agentic SEO briefing workflow

## Decision Rules

- Scope the agent by job, artifact, allowed actions, and failure mode.
- Put review gates where factuality, claim risk, brand fit, or spend can fail.
- Use evals before expanding autonomy or tool access.
- AI marketing agent workflow: What the agent may draft, route, decide, or escalate
- AI marketing agent workflow: Which gate must pass before expanding autonomy
- SEO content briefing: Which page, section, or proof asset should be created or refreshed
- SEO content briefing: Which structured data or crawl fix must ship with content
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `scope an AI workflow for target queries, proof lookup, brief drafting, schema actions, review gates, and publish handoff` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI marketing agent workflow, SEO content briefing; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return agentic SEO briefing workflow with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for agentic SEO briefing workflow
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: agentic SEO briefing workflow.
- Organizing mechanic: scope an AI workflow for target queries, proof lookup, brief drafting, schema actions, review gates, and publish handoff.
- Core fields or sections: agent job, target query, brief input, proof lookup, schema action, review gate, publish handoff, telemetry.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI marketing agent workflow: job, input, tool, action right, review gate, fallback, telemetry
- SEO content briefing: query or question, intent, page type, answer block, proof, schema, link action

## Decision Gates

- AI marketing agent workflow: do not mark the artifact ready until every tool action has an input, output, owner, and fallback.
- SEO content briefing: do not mark the artifact ready until each brief includes the answer, proof, schema need, and indexability check.

## QA Checks

- The workflow states what the agent can decide, draft, route, or never do.
- Each tool call has an input, output, owner, and failure fallback.
- Telemetry captures quality, acceptance, rework, and business impact.
- AI marketing agent workflow: Every tool action has an input, output, owner, and fallback.
- AI marketing agent workflow: Risky actions are blocked by review or eval gates.
- SEO content briefing: Each brief includes the answer, proof, schema need, and indexability check.
- SEO content briefing: The content gap is tied to a specific question or intent.

## Failure Modes

- Designing an agent around a vague role instead of a bounded job.
- Skipping approval because the first demos look plausible.
- Measuring volume without quality, acceptance, or risk metrics.
- AI marketing agent workflow: Defining an agent role without a bounded job and final artifact.
- SEO content briefing: Writing generic content that does not create citable proof or answer structure.

## Proof Metrics

- Acceptance rate
- Review burden and rework rate
- Eval pass rate
- Time saved with quality preserved
- AI marketing agent workflow: eval pass rate
- AI marketing agent workflow: acceptance rate and rework rate
- SEO content briefing: indexed proof coverage
- SEO content briefing: answer inclusion and citation quality

## Example Prompt

Use $agentic-seo-briefing-workflow to create agentic SEO briefing workflow for a marketing task in Marketing Agents / Governance. Apply the AI marketing agent workflow, SEO content briefing mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
