# LinkedIn prospecting cadence

- Category: Lead Intelligence / Conversion
- Product mechanic: create connection, message, follow-up, and stop rules for LinkedIn prospecting
- Output: LinkedIn cadence
- Evidence surfaces: outbound-cadence-automation

## When To Use

Build LinkedIn outreach flows for target accounts.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `outbound-cadence-automation` | trigger, channel sequence, wait states, personalization, stop rules, replies, and owner handoff | Which step runs, stops, or escalates based on signal; Which personalization is strong enough to use |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Outbound cadence automation: Target segment, trigger, proof point, channel mix, and reply route
- Outbound cadence automation: Suppression rules, step timing, stop conditions, owner, and fallback copy
- Specific constraints, examples, and existing assets for LinkedIn prospecting cadence

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Outbound cadence automation: Which step runs, stops, or escalates based on signal
- Outbound cadence automation: Which personalization is strong enough to use
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `create connection, message, follow-up, and stop rules for LinkedIn prospecting` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Outbound cadence automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return LinkedIn cadence with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for LinkedIn prospecting cadence
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: LinkedIn cadence.
- Organizing mechanic: create connection, message, follow-up, and stop rules for LinkedIn prospecting.
- Core fields or sections: connection reason, first note, follow-up step, proof, wait, stop rule, handoff.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Outbound cadence automation: step, channel, trigger, message angle, wait, stop rule, route

## Decision Gates

- Outbound cadence automation: do not mark the artifact ready until every step has a trigger, wait rule, stop rule, and reply route.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Outbound cadence automation: Every step has a trigger, wait rule, stop rule, and reply route.
- Outbound cadence automation: Suppression and unsubscribe paths are handled before sending.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Outbound cadence automation: Automating follow-up before reply handling and stop rules are defined.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Outbound cadence automation: positive reply rate
- Outbound cadence automation: booking rate and unsubscribe rate

## Example Prompt

Use $linkedin-prospecting-cadence to create LinkedIn cadence for a marketing task in Lead Intelligence / Conversion. Apply the Outbound cadence automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
