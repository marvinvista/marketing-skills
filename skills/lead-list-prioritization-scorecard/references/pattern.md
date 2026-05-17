# lead list prioritization scorecard

- Category: Lead Intelligence / Conversion
- Product mechanic: score leads by fit, trigger, intent, evidence strength, urgency, and route
- Output: lead scoring table and routing notes
- Evidence surfaces: lead-list-building, lead-enrichment-and-research

## When To Use

Prioritize leads before outreach using fit and intent evidence.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `lead-list-building` | segment rules, account criteria, exclusions, dedupe logic, and owner routing | Which records qualify for action now; Which gaps block enrichment, routing, or outreach |
| `lead-enrichment-and-research` | fields, evidence freshness, confidence, role pain, trigger, message use, and fallback behavior | Which fields change score, route, or message; Which missing fields require manual research or conservative fallback |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Lead list building: ICP or segment definition, triggers, disqualifiers, and territory or market limits
- Lead list building: Required list fields, evidence standard, dedupe rule, and owner route
- Lead enrichment and research: Target records, required enrichment fields, freshness rule, and source priority
- Lead enrichment and research: Usage rule for routing, personalization, scoring, and fallback when a field is missing
- Specific constraints, examples, and existing assets for lead list prioritization scorecard

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Lead list building: Which records qualify for action now
- Lead list building: Which gaps block enrichment, routing, or outreach
- Lead enrichment and research: Which fields change score, route, or message
- Lead enrichment and research: Which missing fields require manual research or conservative fallback
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `score leads by fit, trigger, intent, evidence strength, urgency, and route` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Lead list building, Lead enrichment and research; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return lead scoring table and routing notes with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for lead list prioritization scorecard
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: lead scoring table and routing notes.
- Organizing mechanic: score leads by fit, trigger, intent, evidence strength, urgency, and route.
- Core fields or sections: record, fit score, intent score, evidence strength, urgency, route, next action.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Lead list building: account or lead, segment, fit reason, trigger, evidence, disqualifier, route
- Lead enrichment and research: record, field, value, confidence, freshness, message use, fallback

## Decision Gates

- Lead list building: do not mark the artifact ready until every accepted record has fit, trigger, evidence, and a route.
- Lead enrichment and research: do not mark the artifact ready until every enrichment field has a usage rule and freshness standard.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Lead list building: Every accepted record has fit, trigger, evidence, and a route.
- Lead list building: Disqualified records state the rule that removed them.
- Lead enrichment and research: Every enrichment field has a usage rule and freshness standard.
- Lead enrichment and research: Low-confidence values are not used for strong personalization.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Lead list building: Building a large list before defining exclusions and evidence standards.
- Lead enrichment and research: Collecting enrichment data that does not change routing or messaging.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Lead list building: qualified record count
- Lead list building: owner acceptance rate
- Lead enrichment and research: field completion rate
- Lead enrichment and research: freshness and confidence coverage

## Example Prompt

Use $lead-list-prioritization-scorecard to create lead scoring table and routing notes for a marketing task in Lead Intelligence / Conversion. Apply the Lead list building, Lead enrichment and research mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

Use `scripts/score_leads.py` when inputs are structured. Score lead records from CSV using fit, intent, evidence, and urgency fields.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
