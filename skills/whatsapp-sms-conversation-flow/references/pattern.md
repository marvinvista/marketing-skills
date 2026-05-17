# WhatsApp SMS conversation flow

- Category: Lifecycle / Ops / Analytics
- Product mechanic: design compliant conversational flows for SMS, WhatsApp, or messaging channels
- Output: messaging conversation flow
- Evidence surfaces: marketing-ops-orchestration, outbound-cadence-automation, inbound-chat-qualification

## When To Use

Build messaging campaign flows with compliance and handoff checks.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `marketing-ops-orchestration` | owners, dependencies, systems, approvals, launch states, fallback paths, and rollback | Which work can launch, wait, or roll back; Which owner or dependency blocks the next action |
| `outbound-cadence-automation` | trigger, channel sequence, wait states, personalization, stop rules, replies, and owner handoff | Which step runs, stops, or escalates based on signal; Which personalization is strong enough to use |
| `inbound-chat-qualification` | questions, answer branches, qualification rules, fallback copy, handoff notes, and booking path | Which visitors book, route to a human, nurture, or exit; Which questions are necessary versus conversion friction |

## Required Inputs

- Campaign, lifecycle, or data workflow boundary
- Events, properties, audiences, consent rules, and owners
- Tools, destinations, templates, and rollback constraints
- Measurement question and decision cadence
- Marketing ops orchestration: Workflow boundary, systems involved, owner map, launch date, and dependency list
- Marketing ops orchestration: Approval needs, fallback path, rollback trigger, and status reporting cadence
- Outbound cadence automation: Target segment, trigger, proof point, channel mix, and reply route
- Outbound cadence automation: Suppression rules, step timing, stop conditions, owner, and fallback copy
- Inbound chat qualification: Target visitor, qualification criteria, required fields, and disqualifiers
- Inbound chat qualification: Chat questions, routing rules, handoff owner, fallback message, and booking path
- Specific constraints, examples, and existing assets for WhatsApp SMS conversation flow

## Decision Rules

- Define the data contract before evaluating performance.
- QA audiences, assets, tracking, and rollback before launch.
- Separate plumbing failures from campaign-performance interpretation.
- Marketing ops orchestration: Which work can launch, wait, or roll back
- Marketing ops orchestration: Which owner or dependency blocks the next action
- Outbound cadence automation: Which step runs, stops, or escalates based on signal
- Outbound cadence automation: Which personalization is strong enough to use
- Inbound chat qualification: Which visitors book, route to a human, nurture, or exit
- Inbound chat qualification: Which questions are necessary versus conversion friction
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `design compliant conversational flows for SMS, WhatsApp, or messaging channels` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Marketing ops orchestration, Outbound cadence automation, Inbound chat qualification; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return messaging conversation flow with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for WhatsApp SMS conversation flow
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: messaging conversation flow.
- Organizing mechanic: design compliant conversational flows for SMS, WhatsApp, or messaging channels.
- Core fields or sections: channel, consent state, message step, branch, quiet-hour rule, handoff, fallback, opt-out.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Marketing ops orchestration: workstream, owner, dependency, system, approval, fallback, rollback, status
- Outbound cadence automation: step, channel, trigger, message angle, wait, stop rule, route
- Inbound chat qualification: question, answer branch, qualification rule, score, route, fallback, handoff note

## Decision Gates

- Marketing ops orchestration: do not mark the artifact ready until every dependency has an owner and failure fallback.
- Outbound cadence automation: do not mark the artifact ready until every step has a trigger, wait rule, stop rule, and reply route.
- Inbound chat qualification: do not mark the artifact ready until each question changes routing or qualification.

## QA Checks

- Every field, audience, event, and destination has an owner and check.
- Consent, suppression, and rollback are visible in the artifact.
- The readout says what decision the metric will change.
- Marketing ops orchestration: Every dependency has an owner and failure fallback.
- Marketing ops orchestration: Launch and rollback criteria are visible before execution.
- Outbound cadence automation: Every step has a trigger, wait rule, stop rule, and reply route.
- Outbound cadence automation: Suppression and unsubscribe paths are handled before sending.
- Inbound chat qualification: Each question changes routing or qualification.
- Inbound chat qualification: Fallback and handoff messages preserve context for the next owner.

## Failure Modes

- Reading performance before verifying event and audience integrity.
- Launching without suppression or rollback coverage.
- Building dashboards that do not map to an operating decision.
- Marketing ops orchestration: Shipping a workflow with unclear ownership or rollback responsibility.
- Outbound cadence automation: Automating follow-up before reply handling and stop rules are defined.
- Inbound chat qualification: Asking chat questions that do not change route or handoff quality.

## Proof Metrics

- QA pass rate
- Audience sync accuracy
- Decision latency
- Lifecycle movement or reactivation lift
- Marketing ops orchestration: cycle time
- Marketing ops orchestration: handoff completion and rollback readiness
- Outbound cadence automation: positive reply rate
- Outbound cadence automation: booking rate and unsubscribe rate
- Inbound chat qualification: qualified handoff rate
- Inbound chat qualification: booking completion and fallback rate

## Example Prompt

Use $whatsapp-sms-conversation-flow to create messaging conversation flow for a marketing task in Lifecycle / Ops / Analytics. Apply the Marketing ops orchestration, Outbound cadence automation, Inbound chat qualification mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
