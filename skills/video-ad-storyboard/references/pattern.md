# video ad storyboard

- Category: Creative / Ads / Assets
- Product mechanic: structure video ads into hook, proof, product moment, objection, CTA, and edit notes
- Output: video storyboard and shot list
- Evidence surfaces: video-ad-production, ad-creative-generation

## When To Use

Storyboard video ads from campaign inputs and production constraints.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `video-ad-production` | hook, scene order, shot list, product moments, captions, voice, timing, and edit notes | Which moments belong in the first seconds versus proof body; Which shots, claims, or edits need production review |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Video ad production: Audience, platform, duration, format, offer, proof, and production constraints
- Video ad production: Required shots, voice style, caption style, legal notes, and review owner
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Specific constraints, examples, and existing assets for video ad storyboard

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Video ad production: Which moments belong in the first seconds versus proof body
- Video ad production: Which shots, claims, or edits need production review
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `structure video ads into hook, proof, product moment, objection, CTA, and edit notes` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Video ad production, Ad creative generation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return video storyboard and shot list with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for video ad storyboard
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: video storyboard and shot list.
- Organizing mechanic: structure video ads into hook, proof, product moment, objection, CTA, and edit notes.
- Core fields or sections: scene, hook, product moment, proof line, objection, visual cue, caption, CTA, edit note.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Video ad production: scene, hook, shot, line, visual, caption, edit note, review flag
- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state

## Decision Gates

- Video ad production: do not mark the artifact ready until the storyboard names timing, visual, line, caption, and cta.
- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Video ad production: The storyboard names timing, visual, line, caption, and CTA.
- Video ad production: Claims and product depictions are reviewable before editing starts.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Video ad production: Writing a script without shot, timing, and review instructions.
- Ad creative generation: Generating asset volume without a hypothesis and review state.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Video ad production: hook retention
- Video ad production: asset completion and approval rate
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time

## Example Prompt

Use $video-ad-storyboard to create video storyboard and shot list for a marketing task in Creative / Ads / Assets. Apply the Video ad production, Ad creative generation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
