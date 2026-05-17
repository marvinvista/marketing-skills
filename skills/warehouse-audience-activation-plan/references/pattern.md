# warehouse audience activation plan

- Category: Lifecycle / Ops / Analytics
- Product mechanic: turn warehouse tables into campaign audiences with joins, QA, consent, and refresh rules
- Output: warehouse activation plan
- Evidence surfaces: audience-data-sync

## When To Use

Activate warehouse data for campaigns with QA rules.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `audience-data-sync` | fields, joins, freshness, destinations, exclusions, consent, owner checks, and sync failures | Which audience is eligible for activation; Which sync gap blocks launch or needs rollback |

## Required Inputs

- Campaign, lifecycle, or data workflow boundary
- Events, properties, audiences, consent rules, and owners
- Tools, destinations, templates, and rollback constraints
- Measurement question and decision cadence
- Audience data sync: Audience definition, field mapping, refresh cadence, destination, and owner
- Audience data sync: Consent, suppression, join keys, exclusion rules, and expected row counts
- Specific constraints, examples, and existing assets for warehouse audience activation plan

## Decision Rules

- Define the data contract before evaluating performance.
- QA audiences, assets, tracking, and rollback before launch.
- Separate plumbing failures from campaign-performance interpretation.
- Audience data sync: Which audience is eligible for activation
- Audience data sync: Which sync gap blocks launch or needs rollback
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn warehouse tables into campaign audiences with joins, QA, consent, and refresh rules` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Audience data sync; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return warehouse activation plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for warehouse audience activation plan
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: warehouse activation plan.
- Organizing mechanic: turn warehouse tables into campaign audiences with joins, QA, consent, and refresh rules.
- Core fields or sections: table, join key, segment rule, consent, exclusion, destination, count check, refresh.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Audience data sync: audience, field, join key, destination, refresh, exclusion, owner, check

## Decision Gates

- Audience data sync: do not mark the artifact ready until expected and actual counts are checked before activation.

## QA Checks

- Every field, audience, event, and destination has an owner and check.
- Consent, suppression, and rollback are visible in the artifact.
- The readout says what decision the metric will change.
- Audience data sync: Expected and actual counts are checked before activation.
- Audience data sync: Consent and suppression rules are visible in the contract.

## Failure Modes

- Reading performance before verifying event and audience integrity.
- Launching without suppression or rollback coverage.
- Building dashboards that do not map to an operating decision.
- Audience data sync: Activating an audience before validating fields, counts, and exclusions.

## Proof Metrics

- QA pass rate
- Audience sync accuracy
- Decision latency
- Lifecycle movement or reactivation lift
- Audience data sync: match rate
- Audience data sync: sync latency and error rate

## Example Prompt

Use $warehouse-audience-activation-plan to create warehouse activation plan for a marketing task in Lifecycle / Ops / Analytics. Apply the Audience data sync mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
