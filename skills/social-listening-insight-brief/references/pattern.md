# social listening insight brief

- Category: Content / Creator / Social
- Product mechanic: turn reviews, social posts, comments, and communities into message and campaign insights
- Output: social listening brief
- Evidence surfaces: customer-research-synthesis, social-content-automation

## When To Use

Extract marketing insights from social and community signals.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Specific constraints, examples, and existing assets for social listening insight brief

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn reviews, social posts, comments, and communities into message and campaign insights` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Customer research synthesis, Social content automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return social listening brief with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for social listening insight brief
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: social listening brief.
- Organizing mechanic: turn reviews, social posts, comments, and communities into message and campaign insights.
- Core fields or sections: channel, post or comment, pain, language, objection, segment, implication, campaign action.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence
- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner

## Decision Gates

- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.
- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.
- Social content automation: Creating a calendar before defining the repeatable content loop.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume

## Example Prompt

Use $social-listening-insight-brief to create social listening brief for a marketing task in Content / Creator / Social. Apply the Customer research synthesis, Social content automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
