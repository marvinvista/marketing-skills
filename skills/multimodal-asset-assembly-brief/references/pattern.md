# multimodal asset assembly brief

- Category: Creative / Ads / Assets
- Product mechanic: compose image, video, voice, copy, captions, and landing proof into one coherent asset plan
- Output: multimodal assembly brief
- Evidence surfaces: ad-creative-generation, video-ad-production, product-image-generation, brand-governance-review

## When To Use

Plan multimodal ad assets across formats and review states.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |
| `video-ad-production` | hook, scene order, shot list, product moments, captions, voice, timing, and edit notes | Which moments belong in the first seconds versus proof body; Which shots, claims, or edits need production review |
| `product-image-generation` | shot type, product fidelity, merchandising context, prompts, negative constraints, and visual QA | Which image prompts are ready for generation or retouching; Which visual defects block commerce or ad use |
| `brand-governance-review` | claims, proof, voice, compliance risk, platform limits, and approval state | What can publish, what needs edits, and what needs explicit approval; Which recurring issue should be added to voice or claim memory |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Video ad production: Audience, platform, duration, format, offer, proof, and production constraints
- Video ad production: Required shots, voice style, caption style, legal notes, and review owner
- Product image generation: Product details, required shot types, usage context, dimensions, and brand rules
- Product image generation: Prompt constraints, unacceptable artifacts, approval owner, and retouching path
- Brand governance review: Brand voice, approved claims, banned patterns, legal or policy constraints
- Brand governance review: Draft asset, channel, proof links or notes, reviewer, and required approval level
- Specific constraints, examples, and existing assets for multimodal asset assembly brief

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- Video ad production: Which moments belong in the first seconds versus proof body
- Video ad production: Which shots, claims, or edits need production review
- Product image generation: Which image prompts are ready for generation or retouching
- Product image generation: Which visual defects block commerce or ad use
- Brand governance review: What can publish, what needs edits, and what needs explicit approval
- Brand governance review: Which recurring issue should be added to voice or claim memory
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `compose image, video, voice, copy, captions, and landing proof into one coherent asset plan` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Ad creative generation, Video ad production, Product image generation, Brand governance review; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return multimodal assembly brief with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for multimodal asset assembly brief
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: multimodal assembly brief.
- Organizing mechanic: compose image, video, voice, copy, captions, and landing proof into one coherent asset plan.
- Core fields or sections: format, image, video, voice, copy, caption, landing proof, review state, assembly owner.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state
- Video ad production: scene, hook, shot, line, visual, caption, edit note, review flag
- Product image generation: product, shot type, context, prompt, negative constraint, QA note, approval
- Brand governance review: claim, proof, risk level, voice issue, required edit, owner, approval state

## Decision Gates

- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.
- Video ad production: do not mark the artifact ready until the storyboard names timing, visual, line, caption, and cta.
- Product image generation: do not mark the artifact ready until product details, scale, text, and prohibited artifacts are checked.
- Brand governance review: do not mark the artifact ready until unsupported claims are blocked or rewritten before launch.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.
- Video ad production: The storyboard names timing, visual, line, caption, and CTA.
- Video ad production: Claims and product depictions are reviewable before editing starts.
- Product image generation: Product details, scale, text, and prohibited artifacts are checked.
- Product image generation: Each asset has a usage context and approval state.
- Brand governance review: Unsupported claims are blocked or rewritten before launch.
- Brand governance review: Edits preserve intent while removing risk.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Ad creative generation: Generating asset volume without a hypothesis and review state.
- Video ad production: Writing a script without shot, timing, and review instructions.
- Product image generation: Generating appealing images that fail product fidelity or merchandising needs.
- Brand governance review: Treating brand review as tone cleanup while ignoring proof and risk.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time
- Video ad production: hook retention
- Video ad production: asset completion and approval rate
- Product image generation: asset acceptance rate
- Product image generation: visual defect rate
- Brand governance review: review issue count
- Brand governance review: approval turnaround time

## Example Prompt

Use $multimodal-asset-assembly-brief to create multimodal assembly brief for a marketing task in Creative / Ads / Assets. Apply the Ad creative generation, Video ad production, Product image generation, Brand governance review mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
