# inbound chat qualification flow

- Category: Lead Intelligence / Conversion
- Product mechanic: design chat questions, qualification logic, handoff moments, and fallback messages
- Output: chat qualification flow
- Evidence surfaces: inbound-chat-qualification

## When To Use

Qualify inbound chat without damaging handoff quality.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `inbound-chat-qualification` | questions, answer branches, qualification rules, fallback copy, handoff notes, and booking path | Which visitors book, route to a human, nurture, or exit; Which questions are necessary versus conversion friction |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Inbound chat qualification: Target visitor, qualification criteria, required fields, and disqualifiers
- Inbound chat qualification: Chat questions, routing rules, handoff owner, fallback message, and booking path
- Specific constraints, examples, and existing assets for inbound chat qualification flow

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Inbound chat qualification: Which visitors book, route to a human, nurture, or exit
- Inbound chat qualification: Which questions are necessary versus conversion friction
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `design chat questions, qualification logic, handoff moments, and fallback messages` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Inbound chat qualification; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return chat qualification flow with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for inbound chat qualification flow
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: chat qualification flow.
- Organizing mechanic: design chat questions, qualification logic, handoff moments, and fallback messages.
- Core fields or sections: question, branch, qualification rule, score, route, fallback, booking path, handoff note.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Inbound chat qualification: question, answer branch, qualification rule, score, route, fallback, handoff note

## Decision Gates

- Inbound chat qualification: do not mark the artifact ready until each question changes routing or qualification.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Inbound chat qualification: Each question changes routing or qualification.
- Inbound chat qualification: Fallback and handoff messages preserve context for the next owner.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Inbound chat qualification: Asking chat questions that do not change route or handoff quality.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Inbound chat qualification: qualified handoff rate
- Inbound chat qualification: booking completion and fallback rate

## Example Prompt

Use $inbound-chat-qualification-flow to create chat qualification flow for a marketing task in Lead Intelligence / Conversion. Apply the Inbound chat qualification mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
