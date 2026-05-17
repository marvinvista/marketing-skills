# brand voice memory

- Category: Marketing Agents / Governance
- Product mechanic: distill approved voice, claims, examples, banned patterns, and review notes into reusable memory
- Output: brand voice memory
- Evidence surfaces: brand-governance-review, social-content-automation

## When To Use

Build reusable brand voice guidance for AI workflows.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `brand-governance-review` | claims, proof, voice, compliance risk, platform limits, and approval state | What can publish, what needs edits, and what needs explicit approval; Which recurring issue should be added to voice or claim memory |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |

## Required Inputs

- Bounded marketing job, allowed tools, and final artifact
- Human judgment points, review owners, and escalation rules
- Brand memory, prompt library, evidence base, and eval criteria
- Telemetry needs, rollout stage, and risk tolerance
- Brand governance review: Brand voice, approved claims, banned patterns, legal or policy constraints
- Brand governance review: Draft asset, channel, proof links or notes, reviewer, and required approval level
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Specific constraints, examples, and existing assets for brand voice memory

## Decision Rules

- Scope the agent by job, artifact, allowed actions, and failure mode.
- Put review gates where factuality, claim risk, brand fit, or spend can fail.
- Use evals before expanding autonomy or tool access.
- Brand governance review: What can publish, what needs edits, and what needs explicit approval
- Brand governance review: Which recurring issue should be added to voice or claim memory
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `distill approved voice, claims, examples, banned patterns, and review notes into reusable memory` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Brand governance review, Social content automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return brand voice memory with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for brand voice memory
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: brand voice memory.
- Organizing mechanic: distill approved voice, claims, examples, banned patterns, and review notes into reusable memory.
- Core fields or sections: approved phrase, banned pattern, claim, proof, example, reviewer, update rule, conflict note.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Brand governance review: claim, proof, risk level, voice issue, required edit, owner, approval state
- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner

## Decision Gates

- Brand governance review: do not mark the artifact ready until unsupported claims are blocked or rewritten before launch.
- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.

## QA Checks

- The workflow states what the agent can decide, draft, route, or never do.
- Each tool call has an input, output, owner, and failure fallback.
- Telemetry captures quality, acceptance, rework, and business impact.
- Brand governance review: Unsupported claims are blocked or rewritten before launch.
- Brand governance review: Edits preserve intent while removing risk.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.

## Failure Modes

- Designing an agent around a vague role instead of a bounded job.
- Skipping approval because the first demos look plausible.
- Measuring volume without quality, acceptance, or risk metrics.
- Brand governance review: Treating brand review as tone cleanup while ignoring proof and risk.
- Social content automation: Creating a calendar before defining the repeatable content loop.

## Proof Metrics

- Acceptance rate
- Review burden and rework rate
- Eval pass rate
- Time saved with quality preserved
- Brand governance review: review issue count
- Brand governance review: approval turnaround time
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume

## Example Prompt

Use $brand-voice-memory to create brand voice memory for a marketing task in Marketing Agents / Governance. Apply the Brand governance review, Social content automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
