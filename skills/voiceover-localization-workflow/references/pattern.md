# voiceover localization workflow

- Category: Content / Creator / Social
- Product mechanic: plan translated or localized voice assets with tone, timing, proof, and review checks
- Output: voiceover localization workflow
- Evidence surfaces: video-ad-production, social-content-automation

## When To Use

Localize voiceover assets for marketing use with review checks.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `video-ad-production` | hook, scene order, shot list, product moments, captions, voice, timing, and edit notes | Which moments belong in the first seconds versus proof body; Which shots, claims, or edits need production review |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- Video ad production: Audience, platform, duration, format, offer, proof, and production constraints
- Video ad production: Required shots, voice style, caption style, legal notes, and review owner
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Specific constraints, examples, and existing assets for voiceover localization workflow

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- Video ad production: Which moments belong in the first seconds versus proof body
- Video ad production: Which shots, claims, or edits need production review
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `plan translated or localized voice assets with tone, timing, proof, and review checks` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Video ad production, Social content automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return voiceover localization workflow with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for voiceover localization workflow
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: voiceover localization workflow.
- Organizing mechanic: plan translated or localized voice assets with tone, timing, proof, and review checks.
- Core fields or sections: source script, locale, timing, tone, pronunciation, proof, reviewer, approval state.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Video ad production: scene, hook, shot, line, visual, caption, edit note, review flag
- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner

## Decision Gates

- Video ad production: do not mark the artifact ready until the storyboard names timing, visual, line, caption, and cta.
- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- Video ad production: The storyboard names timing, visual, line, caption, and CTA.
- Video ad production: Claims and product depictions are reviewable before editing starts.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- Video ad production: Writing a script without shot, timing, and review instructions.
- Social content automation: Creating a calendar before defining the repeatable content loop.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- Video ad production: hook retention
- Video ad production: asset completion and approval rate
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume

## Example Prompt

Use $voiceover-localization-workflow to create voiceover localization workflow for a marketing task in Content / Creator / Social. Apply the Video ad production, Social content automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
