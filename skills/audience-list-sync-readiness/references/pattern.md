# audience list sync readiness

- Category: Lead Intelligence / Conversion
- Product mechanic: align audience segments, list criteria, join keys, consent status, exclusions, destinations, and count checks
- Output: audience list sync readiness check
- Evidence surfaces: audience-data-sync, lead-list-building

## When To Use

Check whether a lead list is ready for audience activation.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `audience-data-sync` | fields, joins, freshness, destinations, exclusions, consent, owner checks, and sync failures | Which audience is eligible for activation; Which sync gap blocks launch or needs rollback |
| `lead-list-building` | segment rules, account criteria, exclusions, dedupe logic, and owner routing | Which records qualify for action now; Which gaps block enrichment, routing, or outreach |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Audience data sync: Audience definition, field mapping, refresh cadence, destination, and owner
- Audience data sync: Consent, suppression, join keys, exclusion rules, and expected row counts
- Lead list building: ICP or segment definition, triggers, disqualifiers, and territory or market limits
- Lead list building: Required list fields, evidence standard, dedupe rule, and owner route
- Specific constraints, examples, and existing assets for audience list sync readiness

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Audience data sync: Which audience is eligible for activation
- Audience data sync: Which sync gap blocks launch or needs rollback
- Lead list building: Which records qualify for action now
- Lead list building: Which gaps block enrichment, routing, or outreach
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `align audience segments, list criteria, join keys, consent status, exclusions, destinations, and count checks` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Audience data sync, Lead list building; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return audience list sync readiness check with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for audience list sync readiness
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: audience list sync readiness check.
- Organizing mechanic: align audience segments, list criteria, join keys, consent status, exclusions, destinations, and count checks.
- Core fields or sections: audience segment, list criterion, join key, consent status, exclusion, destination, count check, owner.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Audience data sync: audience, field, join key, destination, refresh, exclusion, owner, check
- Lead list building: account or lead, segment, fit reason, trigger, evidence, disqualifier, route

## Decision Gates

- Audience data sync: do not mark the artifact ready until expected and actual counts are checked before activation.
- Lead list building: do not mark the artifact ready until every accepted record has fit, trigger, evidence, and a route.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Audience data sync: Expected and actual counts are checked before activation.
- Audience data sync: Consent and suppression rules are visible in the contract.
- Lead list building: Every accepted record has fit, trigger, evidence, and a route.
- Lead list building: Disqualified records state the rule that removed them.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Audience data sync: Activating an audience before validating fields, counts, and exclusions.
- Lead list building: Building a large list before defining exclusions and evidence standards.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Audience data sync: match rate
- Audience data sync: sync latency and error rate
- Lead list building: qualified record count
- Lead list building: owner acceptance rate

## Example Prompt

Use $audience-list-sync-readiness to create audience list sync readiness check for a marketing task in Lead Intelligence / Conversion. Apply the Audience data sync, Lead list building mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
