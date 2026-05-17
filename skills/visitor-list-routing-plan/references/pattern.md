# visitor list routing plan

- Category: Lead Intelligence / Conversion
- Product mechanic: connect visit signals, list membership, intent thresholds, confidence, suppression, and follow-up routing
- Output: visitor list routing plan
- Evidence surfaces: website-visitor-identification, lead-list-building

## When To Use

Route website visitor signals into list and owner actions.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `website-visitor-identification` | visit pattern, account match, intent level, page path, evidence, owner route, and follow-up timing | Which visits trigger sales, nurture, retargeting, or no action; Which matches are too uncertain for direct outreach |
| `lead-list-building` | segment rules, account criteria, exclusions, dedupe logic, and owner routing | Which records qualify for action now; Which gaps block enrichment, routing, or outreach |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Website visitor identification: Visitor or account matching method, page events, intent threshold, and freshness window
- Website visitor identification: Routing owner, CRM fields, follow-up rule, and confidence fallback
- Lead list building: ICP or segment definition, triggers, disqualifiers, and territory or market limits
- Lead list building: Required list fields, evidence standard, dedupe rule, and owner route
- Specific constraints, examples, and existing assets for visitor list routing plan

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Website visitor identification: Which visits trigger sales, nurture, retargeting, or no action
- Website visitor identification: Which matches are too uncertain for direct outreach
- Lead list building: Which records qualify for action now
- Lead list building: Which gaps block enrichment, routing, or outreach
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `connect visit signals, list membership, intent thresholds, confidence, suppression, and follow-up routing` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Website visitor identification, Lead list building; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return visitor list routing plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for visitor list routing plan
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: visitor list routing plan.
- Organizing mechanic: connect visit signals, list membership, intent thresholds, confidence, suppression, and follow-up routing.
- Core fields or sections: visit signal, matched account, list membership, intent threshold, route, confidence, follow-up, suppression.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Website visitor identification: visit, matched account, intent level, evidence, confidence, owner, follow-up
- Lead list building: account or lead, segment, fit reason, trigger, evidence, disqualifier, route

## Decision Gates

- Website visitor identification: do not mark the artifact ready until confidence level and evidence are visible before routing.
- Lead list building: do not mark the artifact ready until every accepted record has fit, trigger, evidence, and a route.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Website visitor identification: Confidence level and evidence are visible before routing.
- Website visitor identification: Follow-up timing matches observed intent, not just page view volume.
- Lead list building: Every accepted record has fit, trigger, evidence, and a route.
- Lead list building: Disqualified records state the rule that removed them.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Website visitor identification: Routing anonymous visits without confidence and intent thresholds.
- Lead list building: Building a large list before defining exclusions and evidence standards.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Website visitor identification: match rate
- Website visitor identification: signal-to-action latency
- Lead list building: qualified record count
- Lead list building: owner acceptance rate

## Example Prompt

Use $visitor-list-routing-plan to create visitor list routing plan for a marketing task in Lead Intelligence / Conversion. Apply the Website visitor identification, Lead list building mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
