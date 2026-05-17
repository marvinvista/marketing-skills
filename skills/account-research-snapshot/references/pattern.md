# account research snapshot

- Category: Lead Intelligence / Conversion
- Product mechanic: summarize account context, role pain, trigger, proof match, objection, and first message angle
- Output: account research snapshot
- Evidence surfaces: lead-enrichment-and-research, customer-research-synthesis

## When To Use

Create concise account research for personalized outbound outreach.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `lead-enrichment-and-research` | fields, evidence freshness, confidence, role pain, trigger, message use, and fallback behavior | Which fields change score, route, or message; Which missing fields require manual research or conservative fallback |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Lead enrichment and research: Target records, required enrichment fields, freshness rule, and source priority
- Lead enrichment and research: Usage rule for routing, personalization, scoring, and fallback when a field is missing
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Specific constraints, examples, and existing assets for account research snapshot

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Lead enrichment and research: Which fields change score, route, or message
- Lead enrichment and research: Which missing fields require manual research or conservative fallback
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `summarize account context, role pain, trigger, proof match, objection, and first message angle` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Lead enrichment and research, Customer research synthesis; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return account research snapshot with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for account research snapshot
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: account research snapshot.
- Organizing mechanic: summarize account context, role pain, trigger, proof match, objection, and first message angle.
- Core fields or sections: account context, role pain, trigger, proof match, objection, first message angle, confidence.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Lead enrichment and research: record, field, value, confidence, freshness, message use, fallback
- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence

## Decision Gates

- Lead enrichment and research: do not mark the artifact ready until every enrichment field has a usage rule and freshness standard.
- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Lead enrichment and research: Every enrichment field has a usage rule and freshness standard.
- Lead enrichment and research: Low-confidence values are not used for strong personalization.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Lead enrichment and research: Collecting enrichment data that does not change routing or messaging.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Lead enrichment and research: field completion rate
- Lead enrichment and research: freshness and confidence coverage
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence

## Example Prompt

Use $account-research-snapshot to create account research snapshot for a marketing task in Lead Intelligence / Conversion. Apply the Lead enrichment and research, Customer research synthesis mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
