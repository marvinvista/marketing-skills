# attribution diagnostic

- Category: Lifecycle / Ops / Analytics
- Product mechanic: find attribution gaps across source capture, conversion events, identity, routing, and reporting
- Output: attribution diagnostic
- Evidence surfaces: campaign-analytics-qa

## When To Use

Diagnose attribution before making performance decisions from campaign data.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `campaign-analytics-qa` | UTMs, events, conversion paths, dashboards, attribution fields, expected values, and readout decisions | Which metrics are trustworthy enough for a decision; Which tracking gaps block launch or interpretation |

## Required Inputs

- Campaign, lifecycle, or data workflow boundary
- Events, properties, audiences, consent rules, and owners
- Tools, destinations, templates, and rollback constraints
- Measurement question and decision cadence
- Campaign analytics QA: Campaign plan, channels, events, conversion definition, dashboard, and owner
- Campaign analytics QA: Expected values, test records, attribution rules, data freshness, and decision cadence
- Specific constraints, examples, and existing assets for attribution diagnostic

## Decision Rules

- Define the data contract before evaluating performance.
- QA audiences, assets, tracking, and rollback before launch.
- Separate plumbing failures from campaign-performance interpretation.
- Campaign analytics QA: Which metrics are trustworthy enough for a decision
- Campaign analytics QA: Which tracking gaps block launch or interpretation
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `find attribution gaps across source capture, conversion events, identity, routing, and reporting` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Campaign analytics QA; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return attribution diagnostic with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for attribution diagnostic
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: attribution diagnostic.
- Organizing mechanic: find attribution gaps across source capture, conversion events, identity, routing, and reporting.
- Core fields or sections: touchpoint, source capture, identity link, conversion event, attribution rule, gap, fix owner.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Campaign analytics QA: event, parameter, expected value, observed value, owner, status, decision impact

## Decision Gates

- Campaign analytics QA: do not mark the artifact ready until tracking is tested before performance interpretation.

## QA Checks

- Every field, audience, event, and destination has an owner and check.
- Consent, suppression, and rollback are visible in the artifact.
- The readout says what decision the metric will change.
- Campaign analytics QA: Tracking is tested before performance interpretation.
- Campaign analytics QA: Each metric states the decision it can change.

## Failure Modes

- Reading performance before verifying event and audience integrity.
- Launching without suppression or rollback coverage.
- Building dashboards that do not map to an operating decision.
- Campaign analytics QA: Reading campaign performance before verifying event and attribution integrity.

## Proof Metrics

- QA pass rate
- Audience sync accuracy
- Decision latency
- Lifecycle movement or reactivation lift
- Campaign analytics QA: QA pass rate
- Campaign analytics QA: attribution coverage and data freshness

## Example Prompt

Use $attribution-diagnostic to create attribution diagnostic for a marketing task in Lifecycle / Ops / Analytics. Apply the Campaign analytics QA mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
