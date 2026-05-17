# consent suppression rollback plan

- Category: Lifecycle / Ops / Analytics
- Product mechanic: define consent checks, suppression rules, privacy review, rollback path, and incident owner
- Output: consent and rollback plan
- Evidence surfaces: marketing-ops-orchestration, brand-governance-review

## When To Use

Protect campaign operations with consent and rollback rules.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `marketing-ops-orchestration` | owners, dependencies, systems, approvals, launch states, fallback paths, and rollback | Which work can launch, wait, or roll back; Which owner or dependency blocks the next action |
| `brand-governance-review` | claims, proof, voice, compliance risk, platform limits, and approval state | What can publish, what needs edits, and what needs explicit approval; Which recurring issue should be added to voice or claim memory |

## Required Inputs

- Campaign, lifecycle, or data workflow boundary
- Events, properties, audiences, consent rules, and owners
- Tools, destinations, templates, and rollback constraints
- Measurement question and decision cadence
- Marketing ops orchestration: Workflow boundary, systems involved, owner map, launch date, and dependency list
- Marketing ops orchestration: Approval needs, fallback path, rollback trigger, and status reporting cadence
- Brand governance review: Brand voice, approved claims, banned patterns, legal or policy constraints
- Brand governance review: Draft asset, channel, proof links or notes, reviewer, and required approval level
- Specific constraints, examples, and existing assets for consent suppression rollback plan

## Decision Rules

- Define the data contract before evaluating performance.
- QA audiences, assets, tracking, and rollback before launch.
- Separate plumbing failures from campaign-performance interpretation.
- Marketing ops orchestration: Which work can launch, wait, or roll back
- Marketing ops orchestration: Which owner or dependency blocks the next action
- Brand governance review: What can publish, what needs edits, and what needs explicit approval
- Brand governance review: Which recurring issue should be added to voice or claim memory
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `define consent checks, suppression rules, privacy review, rollback path, and incident owner` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Marketing ops orchestration, Brand governance review; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return consent and rollback plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for consent suppression rollback plan
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: consent and rollback plan.
- Organizing mechanic: define consent checks, suppression rules, privacy review, rollback path, and incident owner.
- Core fields or sections: consent rule, suppression list, risky action, rollback trigger, incident owner, test, approval.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Marketing ops orchestration: workstream, owner, dependency, system, approval, fallback, rollback, status
- Brand governance review: claim, proof, risk level, voice issue, required edit, owner, approval state

## Decision Gates

- Marketing ops orchestration: do not mark the artifact ready until every dependency has an owner and failure fallback.
- Brand governance review: do not mark the artifact ready until unsupported claims are blocked or rewritten before launch.

## QA Checks

- Every field, audience, event, and destination has an owner and check.
- Consent, suppression, and rollback are visible in the artifact.
- The readout says what decision the metric will change.
- Marketing ops orchestration: Every dependency has an owner and failure fallback.
- Marketing ops orchestration: Launch and rollback criteria are visible before execution.
- Brand governance review: Unsupported claims are blocked or rewritten before launch.
- Brand governance review: Edits preserve intent while removing risk.

## Failure Modes

- Reading performance before verifying event and audience integrity.
- Launching without suppression or rollback coverage.
- Building dashboards that do not map to an operating decision.
- Marketing ops orchestration: Shipping a workflow with unclear ownership or rollback responsibility.
- Brand governance review: Treating brand review as tone cleanup while ignoring proof and risk.

## Proof Metrics

- QA pass rate
- Audience sync accuracy
- Decision latency
- Lifecycle movement or reactivation lift
- Marketing ops orchestration: cycle time
- Marketing ops orchestration: handoff completion and rollback readiness
- Brand governance review: review issue count
- Brand governance review: approval turnaround time

## Example Prompt

Use $consent-suppression-rollback-plan to create consent and rollback plan for a marketing task in Lifecycle / Ops / Analytics. Apply the Marketing ops orchestration, Brand governance review mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
