# short-form hook bank

- Category: Creative / Ads / Assets
- Product mechanic: generate platform-specific hooks for short-form video while preserving proof and CTA
- Output: hook bank and test notes
- Evidence surfaces: video-ad-production, social-content-automation

## When To Use

Build a hook bank for short-form creative testing.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `video-ad-production` | hook, scene order, shot list, product moments, captions, voice, timing, and edit notes | Which moments belong in the first seconds versus proof body; Which shots, claims, or edits need production review |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Video ad production: Audience, platform, duration, format, offer, proof, and production constraints
- Video ad production: Required shots, voice style, caption style, legal notes, and review owner
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Specific constraints, examples, and existing assets for short-form hook bank

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Video ad production: Which moments belong in the first seconds versus proof body
- Video ad production: Which shots, claims, or edits need production review
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `generate platform-specific hooks for short-form video while preserving proof and CTA` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Video ad production, Social content automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return hook bank and test notes with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for short-form hook bank
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: hook bank and test notes.
- Organizing mechanic: generate platform-specific hooks for short-form video while preserving proof and CTA.
- Core fields or sections: platform, hook type, opening line, proof cue, retention beat, CTA, test note.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Video ad production: scene, hook, shot, line, visual, caption, edit note, review flag
- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner

## Decision Gates

- Video ad production: do not mark the artifact ready until the storyboard names timing, visual, line, caption, and cta.
- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Video ad production: The storyboard names timing, visual, line, caption, and CTA.
- Video ad production: Claims and product depictions are reviewable before editing starts.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Video ad production: Writing a script without shot, timing, and review instructions.
- Social content automation: Creating a calendar before defining the repeatable content loop.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Video ad production: hook retention
- Video ad production: asset completion and approval rate
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume

## Example Prompt

Use $short-form-hook-bank to create hook bank and test notes for a marketing task in Creative / Ads / Assets. Apply the Video ad production, Social content automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
