# buying signal listener spec

- Category: Lead Intelligence / Conversion
- Product mechanic: specify web, product, social, hiring, funding, content, and CRM signals that trigger action
- Output: signal listener spec
- Evidence surfaces: website-visitor-identification, lead-enrichment-and-research, audience-data-sync

## When To Use

Detect buying intent from observable signals and route actions.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `website-visitor-identification` | visit pattern, account match, intent level, page path, evidence, owner route, and follow-up timing | Which visits trigger sales, nurture, retargeting, or no action; Which matches are too uncertain for direct outreach |
| `lead-enrichment-and-research` | fields, evidence freshness, confidence, role pain, trigger, message use, and fallback behavior | Which fields change score, route, or message; Which missing fields require manual research or conservative fallback |
| `audience-data-sync` | fields, joins, freshness, destinations, exclusions, consent, owner checks, and sync failures | Which audience is eligible for activation; Which sync gap blocks launch or needs rollback |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Website visitor identification: Visitor or account matching method, page events, intent threshold, and freshness window
- Website visitor identification: Routing owner, CRM fields, follow-up rule, and confidence fallback
- Lead enrichment and research: Target records, required enrichment fields, freshness rule, and source priority
- Lead enrichment and research: Usage rule for routing, personalization, scoring, and fallback when a field is missing
- Audience data sync: Audience definition, field mapping, refresh cadence, destination, and owner
- Audience data sync: Consent, suppression, join keys, exclusion rules, and expected row counts
- Specific constraints, examples, and existing assets for buying signal listener spec

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Website visitor identification: Which visits trigger sales, nurture, retargeting, or no action
- Website visitor identification: Which matches are too uncertain for direct outreach
- Lead enrichment and research: Which fields change score, route, or message
- Lead enrichment and research: Which missing fields require manual research or conservative fallback
- Audience data sync: Which audience is eligible for activation
- Audience data sync: Which sync gap blocks launch or needs rollback
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `specify web, product, social, hiring, funding, content, and CRM signals that trigger action` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Website visitor identification, Lead enrichment and research, Audience data sync; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return signal listener spec with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for buying signal listener spec
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: signal listener spec.
- Organizing mechanic: specify web, product, social, hiring, funding, content, and CRM signals that trigger action.
- Core fields or sections: signal type, event, threshold, source, freshness, route, action, false-positive check.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Website visitor identification: visit, matched account, intent level, evidence, confidence, owner, follow-up
- Lead enrichment and research: record, field, value, confidence, freshness, message use, fallback
- Audience data sync: audience, field, join key, destination, refresh, exclusion, owner, check

## Decision Gates

- Website visitor identification: do not mark the artifact ready until confidence level and evidence are visible before routing.
- Lead enrichment and research: do not mark the artifact ready until every enrichment field has a usage rule and freshness standard.
- Audience data sync: do not mark the artifact ready until expected and actual counts are checked before activation.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Website visitor identification: Confidence level and evidence are visible before routing.
- Website visitor identification: Follow-up timing matches observed intent, not just page view volume.
- Lead enrichment and research: Every enrichment field has a usage rule and freshness standard.
- Lead enrichment and research: Low-confidence values are not used for strong personalization.
- Audience data sync: Expected and actual counts are checked before activation.
- Audience data sync: Consent and suppression rules are visible in the contract.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Website visitor identification: Routing anonymous visits without confidence and intent thresholds.
- Lead enrichment and research: Collecting enrichment data that does not change routing or messaging.
- Audience data sync: Activating an audience before validating fields, counts, and exclusions.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Website visitor identification: match rate
- Website visitor identification: signal-to-action latency
- Lead enrichment and research: field completion rate
- Lead enrichment and research: freshness and confidence coverage
- Audience data sync: match rate
- Audience data sync: sync latency and error rate

## Example Prompt

Use $buying-signal-listener-spec to create signal listener spec for a marketing task in Lead Intelligence / Conversion. Apply the Website visitor identification, Lead enrichment and research, Audience data sync mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
