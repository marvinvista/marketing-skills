# CRM handoff QA

- Category: Lead Intelligence / Conversion
- Product mechanic: check campaign response, enrichment, owner assignment, next step, and reporting fields
- Output: CRM handoff QA checklist
- Evidence surfaces: marketing-ops-orchestration, audience-data-sync

## When To Use

QA the handoff from marketing signal to CRM action.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `marketing-ops-orchestration` | owners, dependencies, systems, approvals, launch states, fallback paths, and rollback | Which work can launch, wait, or roll back; Which owner or dependency blocks the next action |
| `audience-data-sync` | fields, joins, freshness, destinations, exclusions, consent, owner checks, and sync failures | Which audience is eligible for activation; Which sync gap blocks launch or needs rollback |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Marketing ops orchestration: Workflow boundary, systems involved, owner map, launch date, and dependency list
- Marketing ops orchestration: Approval needs, fallback path, rollback trigger, and status reporting cadence
- Audience data sync: Audience definition, field mapping, refresh cadence, destination, and owner
- Audience data sync: Consent, suppression, join keys, exclusion rules, and expected row counts
- Specific constraints, examples, and existing assets for CRM handoff QA

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Marketing ops orchestration: Which work can launch, wait, or roll back
- Marketing ops orchestration: Which owner or dependency blocks the next action
- Audience data sync: Which audience is eligible for activation
- Audience data sync: Which sync gap blocks launch or needs rollback
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `check campaign response, enrichment, owner assignment, next step, and reporting fields` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Marketing ops orchestration, Audience data sync; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return CRM handoff QA checklist with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for CRM handoff QA
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: CRM handoff QA checklist.
- Organizing mechanic: check campaign response, enrichment, owner assignment, next step, and reporting fields.
- Core fields or sections: record, owner, route, next step, enrichment field, reporting field, missing data, fix.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Marketing ops orchestration: workstream, owner, dependency, system, approval, fallback, rollback, status
- Audience data sync: audience, field, join key, destination, refresh, exclusion, owner, check

## Decision Gates

- Marketing ops orchestration: do not mark the artifact ready until every dependency has an owner and failure fallback.
- Audience data sync: do not mark the artifact ready until expected and actual counts are checked before activation.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Marketing ops orchestration: Every dependency has an owner and failure fallback.
- Marketing ops orchestration: Launch and rollback criteria are visible before execution.
- Audience data sync: Expected and actual counts are checked before activation.
- Audience data sync: Consent and suppression rules are visible in the contract.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Marketing ops orchestration: Shipping a workflow with unclear ownership or rollback responsibility.
- Audience data sync: Activating an audience before validating fields, counts, and exclusions.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Marketing ops orchestration: cycle time
- Marketing ops orchestration: handoff completion and rollback readiness
- Audience data sync: match rate
- Audience data sync: sync latency and error rate

## Example Prompt

Use $crm-handoff-qa to create CRM handoff QA checklist for a marketing task in Lead Intelligence / Conversion. Apply the Marketing ops orchestration, Audience data sync mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
