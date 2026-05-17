# marketing dashboard spec

- Category: Lifecycle / Ops / Analytics
- Product mechanic: specify dashboard metrics, dimensions, data checks, thresholds, and operating decisions
- Output: dashboard spec
- Evidence surfaces: campaign-analytics-qa, marketing-ops-orchestration

## When To Use

Design dashboards that drive marketing operating decisions.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `campaign-analytics-qa` | UTMs, events, conversion paths, dashboards, attribution fields, expected values, and readout decisions | Which metrics are trustworthy enough for a decision; Which tracking gaps block launch or interpretation |
| `marketing-ops-orchestration` | owners, dependencies, systems, approvals, launch states, fallback paths, and rollback | Which work can launch, wait, or roll back; Which owner or dependency blocks the next action |

## Required Inputs

- Campaign, lifecycle, or data workflow boundary
- Events, properties, audiences, consent rules, and owners
- Tools, destinations, templates, and rollback constraints
- Measurement question and decision cadence
- Campaign analytics QA: Campaign plan, channels, events, conversion definition, dashboard, and owner
- Campaign analytics QA: Expected values, test records, attribution rules, data freshness, and decision cadence
- Marketing ops orchestration: Workflow boundary, systems involved, owner map, launch date, and dependency list
- Marketing ops orchestration: Approval needs, fallback path, rollback trigger, and status reporting cadence
- Specific constraints, examples, and existing assets for marketing dashboard spec

## Decision Rules

- Define the data contract before evaluating performance.
- QA audiences, assets, tracking, and rollback before launch.
- Separate plumbing failures from campaign-performance interpretation.
- Campaign analytics QA: Which metrics are trustworthy enough for a decision
- Campaign analytics QA: Which tracking gaps block launch or interpretation
- Marketing ops orchestration: Which work can launch, wait, or roll back
- Marketing ops orchestration: Which owner or dependency blocks the next action
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `specify dashboard metrics, dimensions, data checks, thresholds, and operating decisions` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Campaign analytics QA, Marketing ops orchestration; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return dashboard spec with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for marketing dashboard spec
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: dashboard spec.
- Organizing mechanic: specify dashboard metrics, dimensions, data checks, thresholds, and operating decisions.
- Core fields or sections: metric, dimension, threshold, data check, owner, decision, cadence, caveat.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Campaign analytics QA: event, parameter, expected value, observed value, owner, status, decision impact
- Marketing ops orchestration: workstream, owner, dependency, system, approval, fallback, rollback, status

## Decision Gates

- Campaign analytics QA: do not mark the artifact ready until tracking is tested before performance interpretation.
- Marketing ops orchestration: do not mark the artifact ready until every dependency has an owner and failure fallback.

## QA Checks

- Every field, audience, event, and destination has an owner and check.
- Consent, suppression, and rollback are visible in the artifact.
- The readout says what decision the metric will change.
- Campaign analytics QA: Tracking is tested before performance interpretation.
- Campaign analytics QA: Each metric states the decision it can change.
- Marketing ops orchestration: Every dependency has an owner and failure fallback.
- Marketing ops orchestration: Launch and rollback criteria are visible before execution.

## Failure Modes

- Reading performance before verifying event and audience integrity.
- Launching without suppression or rollback coverage.
- Building dashboards that do not map to an operating decision.
- Campaign analytics QA: Reading campaign performance before verifying event and attribution integrity.
- Marketing ops orchestration: Shipping a workflow with unclear ownership or rollback responsibility.

## Proof Metrics

- QA pass rate
- Audience sync accuracy
- Decision latency
- Lifecycle movement or reactivation lift
- Campaign analytics QA: QA pass rate
- Campaign analytics QA: attribution coverage and data freshness
- Marketing ops orchestration: cycle time
- Marketing ops orchestration: handoff completion and rollback readiness

## Example Prompt

Use $marketing-dashboard-spec to create dashboard spec for a marketing task in Lifecycle / Ops / Analytics. Apply the Campaign analytics QA, Marketing ops orchestration mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
