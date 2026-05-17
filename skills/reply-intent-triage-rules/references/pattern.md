# reply intent triage rules

- Category: Lead Intelligence / Conversion
- Product mechanic: classify replies into interest, objection, referral, timing, unsubscribe, or support paths
- Output: reply triage rules
- Evidence surfaces: inbound-chat-qualification, outbound-cadence-automation

## When To Use

Route replies into the right next action.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `inbound-chat-qualification` | questions, answer branches, qualification rules, fallback copy, handoff notes, and booking path | Which visitors book, route to a human, nurture, or exit; Which questions are necessary versus conversion friction |
| `outbound-cadence-automation` | trigger, channel sequence, wait states, personalization, stop rules, replies, and owner handoff | Which step runs, stops, or escalates based on signal; Which personalization is strong enough to use |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Inbound chat qualification: Target visitor, qualification criteria, required fields, and disqualifiers
- Inbound chat qualification: Chat questions, routing rules, handoff owner, fallback message, and booking path
- Outbound cadence automation: Target segment, trigger, proof point, channel mix, and reply route
- Outbound cadence automation: Suppression rules, step timing, stop conditions, owner, and fallback copy
- Specific constraints, examples, and existing assets for reply intent triage rules

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Inbound chat qualification: Which visitors book, route to a human, nurture, or exit
- Inbound chat qualification: Which questions are necessary versus conversion friction
- Outbound cadence automation: Which step runs, stops, or escalates based on signal
- Outbound cadence automation: Which personalization is strong enough to use
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `classify replies into interest, objection, referral, timing, unsubscribe, or support paths` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Inbound chat qualification, Outbound cadence automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return reply triage rules with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for reply intent triage rules
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: reply triage rules.
- Organizing mechanic: classify replies into interest, objection, referral, timing, unsubscribe, or support paths.
- Core fields or sections: reply text, intent class, urgency, objection, route, owner, response SLA, stop flag.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Inbound chat qualification: question, answer branch, qualification rule, score, route, fallback, handoff note
- Outbound cadence automation: step, channel, trigger, message angle, wait, stop rule, route

## Decision Gates

- Inbound chat qualification: do not mark the artifact ready until each question changes routing or qualification.
- Outbound cadence automation: do not mark the artifact ready until every step has a trigger, wait rule, stop rule, and reply route.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Inbound chat qualification: Each question changes routing or qualification.
- Inbound chat qualification: Fallback and handoff messages preserve context for the next owner.
- Outbound cadence automation: Every step has a trigger, wait rule, stop rule, and reply route.
- Outbound cadence automation: Suppression and unsubscribe paths are handled before sending.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Inbound chat qualification: Asking chat questions that do not change route or handoff quality.
- Outbound cadence automation: Automating follow-up before reply handling and stop rules are defined.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Inbound chat qualification: qualified handoff rate
- Inbound chat qualification: booking completion and fallback rate
- Outbound cadence automation: positive reply rate
- Outbound cadence automation: booking rate and unsubscribe rate

## Example Prompt

Use $reply-intent-triage-rules to create reply triage rules for a marketing task in Lead Intelligence / Conversion. Apply the Inbound chat qualification, Outbound cadence automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
