# chat lead routing flow

- Category: Lead Intelligence / Conversion
- Product mechanic: turn chat qualification answers into list membership, owner routing, follow-up timing, and suppression-aware actions
- Output: chat lead routing flow
- Evidence surfaces: inbound-chat-qualification, lead-list-building

## When To Use

Move chat-qualified visitors into the right list and follow-up path.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `inbound-chat-qualification` | questions, answer branches, qualification rules, fallback copy, handoff notes, and booking path | Which visitors book, route to a human, nurture, or exit; Which questions are necessary versus conversion friction |
| `lead-list-building` | segment rules, account criteria, exclusions, dedupe logic, and owner routing | Which records qualify for action now; Which gaps block enrichment, routing, or outreach |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Inbound chat qualification: Target visitor, qualification criteria, required fields, and disqualifiers
- Inbound chat qualification: Chat questions, routing rules, handoff owner, fallback message, and booking path
- Lead list building: ICP or segment definition, triggers, disqualifiers, and territory or market limits
- Lead list building: Required list fields, evidence standard, dedupe rule, and owner route
- Specific constraints, examples, and existing assets for chat lead routing flow

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Inbound chat qualification: Which visitors book, route to a human, nurture, or exit
- Inbound chat qualification: Which questions are necessary versus conversion friction
- Lead list building: Which records qualify for action now
- Lead list building: Which gaps block enrichment, routing, or outreach
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn chat qualification answers into list membership, owner routing, follow-up timing, and suppression-aware actions` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Inbound chat qualification, Lead list building; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return chat lead routing flow with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for chat lead routing flow
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: chat lead routing flow.
- Organizing mechanic: turn chat qualification answers into list membership, owner routing, follow-up timing, and suppression-aware actions.
- Core fields or sections: chat answer, qualification score, list membership, fit rule, owner route, follow-up timing, suppression, handoff note.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Inbound chat qualification: question, answer branch, qualification rule, score, route, fallback, handoff note
- Lead list building: account or lead, segment, fit reason, trigger, evidence, disqualifier, route

## Decision Gates

- Inbound chat qualification: do not mark the artifact ready until each question changes routing or qualification.
- Lead list building: do not mark the artifact ready until every accepted record has fit, trigger, evidence, and a route.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Inbound chat qualification: Each question changes routing or qualification.
- Inbound chat qualification: Fallback and handoff messages preserve context for the next owner.
- Lead list building: Every accepted record has fit, trigger, evidence, and a route.
- Lead list building: Disqualified records state the rule that removed them.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Inbound chat qualification: Asking chat questions that do not change route or handoff quality.
- Lead list building: Building a large list before defining exclusions and evidence standards.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Inbound chat qualification: qualified handoff rate
- Inbound chat qualification: booking completion and fallback rate
- Lead list building: qualified record count
- Lead list building: owner acceptance rate

## Example Prompt

Use $chat-lead-routing-flow to create chat lead routing flow for a marketing task in Lead Intelligence / Conversion. Apply the Inbound chat qualification, Lead list building mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
