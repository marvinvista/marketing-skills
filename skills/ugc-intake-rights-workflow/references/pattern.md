# UGC intake rights workflow

- Category: Content / Creator / Social
- Product mechanic: manage creator asset intake, rights, tagging, approvals, edits, and paid reuse
- Output: UGC intake and rights workflow
- Evidence surfaces: ugc-creator-workflow, ad-creative-generation

## When To Use

Turn UGC into reusable approved assets with rights tracking.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ugc-creator-workflow` | creator fit, deliverables, asset intake, rights, approvals, revisions, tagging, and reuse | Which creators or assets are approved, revised, renewed, or reused; Which rights or approvals block paid amplification |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- UGC creator workflow: Creator criteria, offer, deliverables, asset examples, and usage rights
- UGC creator workflow: Approval path, revision rule, tagging taxonomy, and paid reuse constraints
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Specific constraints, examples, and existing assets for UGC intake rights workflow

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- UGC creator workflow: Which creators or assets are approved, revised, renewed, or reused
- UGC creator workflow: Which rights or approvals block paid amplification
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `manage creator asset intake, rights, tagging, approvals, edits, and paid reuse` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for UGC creator workflow, Ad creative generation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return UGC intake and rights workflow with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for UGC intake rights workflow
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: UGC intake and rights workflow.
- Organizing mechanic: manage creator asset intake, rights, tagging, approvals, edits, and paid reuse.
- Core fields or sections: asset, creator, rights window, edit permission, tag, approval state, reuse channel, renewal note.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- UGC creator workflow: creator, deliverable, hook, proof, rights, revision, approval, reuse state
- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state

## Decision Gates

- UGC creator workflow: do not mark the artifact ready until rights, usage windows, and edit permissions are explicit.
- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- UGC creator workflow: Rights, usage windows, and edit permissions are explicit.
- UGC creator workflow: Creator fit is scored beyond follower count.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- UGC creator workflow: Collecting creator assets without rights, tagging, and reuse rules.
- Ad creative generation: Generating asset volume without a hypothesis and review state.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- UGC creator workflow: approved asset rate
- UGC creator workflow: creator renewal or reuse rate
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time

## Example Prompt

Use $ugc-intake-rights-workflow to create UGC intake and rights workflow for a marketing task in Content / Creator / Social. Apply the UGC creator workflow, Ad creative generation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
