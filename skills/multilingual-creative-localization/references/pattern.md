# multilingual creative localization

- Category: Creative / Ads / Assets
- Product mechanic: localize campaign copy, video, voice, and proof while preserving intent and claim boundaries
- Output: localized creative plan
- Evidence surfaces: social-content-automation, brand-governance-review, video-ad-production

## When To Use

Localize campaign creative without losing meaning or compliance.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |
| `brand-governance-review` | claims, proof, voice, compliance risk, platform limits, and approval state | What can publish, what needs edits, and what needs explicit approval; Which recurring issue should be added to voice or claim memory |
| `video-ad-production` | hook, scene order, shot list, product moments, captions, voice, timing, and edit notes | Which moments belong in the first seconds versus proof body; Which shots, claims, or edits need production review |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Brand governance review: Brand voice, approved claims, banned patterns, legal or policy constraints
- Brand governance review: Draft asset, channel, proof links or notes, reviewer, and required approval level
- Video ad production: Audience, platform, duration, format, offer, proof, and production constraints
- Video ad production: Required shots, voice style, caption style, legal notes, and review owner
- Specific constraints, examples, and existing assets for multilingual creative localization

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- Brand governance review: What can publish, what needs edits, and what needs explicit approval
- Brand governance review: Which recurring issue should be added to voice or claim memory
- Video ad production: Which moments belong in the first seconds versus proof body
- Video ad production: Which shots, claims, or edits need production review
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `localize campaign copy, video, voice, and proof while preserving intent and claim boundaries` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Social content automation, Brand governance review, Video ad production; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return localized creative plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for multilingual creative localization
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: localized creative plan.
- Organizing mechanic: localize campaign copy, video, voice, and proof while preserving intent and claim boundaries.
- Core fields or sections: locale, original intent, claim, proof, idiom risk, voice note, reviewer, localized CTA.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner
- Brand governance review: claim, proof, risk level, voice issue, required edit, owner, approval state
- Video ad production: scene, hook, shot, line, visual, caption, edit note, review flag

## Decision Gates

- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.
- Brand governance review: do not mark the artifact ready until unsupported claims are blocked or rewritten before launch.
- Video ad production: do not mark the artifact ready until the storyboard names timing, visual, line, caption, and cta.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.
- Brand governance review: Unsupported claims are blocked or rewritten before launch.
- Brand governance review: Edits preserve intent while removing risk.
- Video ad production: The storyboard names timing, visual, line, caption, and CTA.
- Video ad production: Claims and product depictions are reviewable before editing starts.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Social content automation: Creating a calendar before defining the repeatable content loop.
- Brand governance review: Treating brand review as tone cleanup while ignoring proof and risk.
- Video ad production: Writing a script without shot, timing, and review instructions.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume
- Brand governance review: review issue count
- Brand governance review: approval turnaround time
- Video ad production: hook retention
- Video ad production: asset completion and approval rate

## Example Prompt

Use $multilingual-creative-localization to create localized creative plan for a marketing task in Creative / Ads / Assets. Apply the Social content automation, Brand governance review, Video ad production mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
