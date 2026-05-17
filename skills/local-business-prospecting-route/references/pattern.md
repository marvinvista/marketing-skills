# local business prospecting route

- Category: Lead Intelligence / Conversion
- Product mechanic: find local accounts or locations, prioritize routes, and prepare direct outreach
- Output: local prospecting route
- Evidence surfaces: local-storefront-growth, lead-list-building

## When To Use

Prioritize local prospects for direct outreach and route planning.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `local-storefront-growth` | locations, radius, local offer, route plan, reviews, community proof, and owner follow-up | Which local targets get field action versus digital follow-up; Which local proof or listing gap blocks trust |
| `lead-list-building` | segment rules, account criteria, exclusions, dedupe logic, and owner routing | Which records qualify for action now; Which gaps block enrichment, routing, or outreach |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Local storefront growth: Target location set, radius, category, offer, local proof, and field owner
- Local storefront growth: Route constraints, review signals, storefront data, and follow-up channel
- Lead list building: ICP or segment definition, triggers, disqualifiers, and territory or market limits
- Lead list building: Required list fields, evidence standard, dedupe rule, and owner route
- Specific constraints, examples, and existing assets for local business prospecting route

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Local storefront growth: Which local targets get field action versus digital follow-up
- Local storefront growth: Which local proof or listing gap blocks trust
- Lead list building: Which records qualify for action now
- Lead list building: Which gaps block enrichment, routing, or outreach
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `find local accounts or locations, prioritize routes, and prepare direct outreach` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Local storefront growth, Lead list building; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return local prospecting route with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for local business prospecting route
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: local prospecting route.
- Organizing mechanic: find local accounts or locations, prioritize routes, and prepare direct outreach.
- Core fields or sections: location, category, fit, local proof, route order, contact path, owner, follow-up.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Local storefront growth: location, radius, offer, local proof, route, owner, follow-up
- Lead list building: account or lead, segment, fit reason, trigger, evidence, disqualifier, route

## Decision Gates

- Local storefront growth: do not mark the artifact ready until routes are prioritized by fit, proximity, and actionability.
- Lead list building: do not mark the artifact ready until every accepted record has fit, trigger, evidence, and a route.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Local storefront growth: Routes are prioritized by fit, proximity, and actionability.
- Local storefront growth: Local proof is tied to the offer and outreach path.
- Lead list building: Every accepted record has fit, trigger, evidence, and a route.
- Lead list building: Disqualified records state the rule that removed them.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Local storefront growth: Treating local prospecting as a generic list without route and proof context.
- Lead list building: Building a large list before defining exclusions and evidence standards.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Local storefront growth: route completion
- Local storefront growth: local response or conversion rate
- Lead list building: qualified record count
- Lead list building: owner acceptance rate

## Example Prompt

Use $local-business-prospecting-route to create local prospecting route for a marketing task in Lead Intelligence / Conversion. Apply the Local storefront growth, Lead list building mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
