# creator performance reuse readout

- Category: Content / Creator / Social
- Product mechanic: evaluate creator assets for performance, learning, renewal, and paid reuse decisions
- Output: creator performance readout
- Evidence surfaces: ugc-creator-workflow, social-content-automation, campaign-analytics-qa

## When To Use

Decide which creator assets to reuse or renew.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ugc-creator-workflow` | creator fit, deliverables, asset intake, rights, approvals, revisions, tagging, and reuse | Which creators or assets are approved, revised, renewed, or reused; Which rights or approvals block paid amplification |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |
| `campaign-analytics-qa` | UTMs, events, conversion paths, dashboards, attribution fields, expected values, and readout decisions | Which metrics are trustworthy enough for a decision; Which tracking gaps block launch or interpretation |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- UGC creator workflow: Creator criteria, offer, deliverables, asset examples, and usage rights
- UGC creator workflow: Approval path, revision rule, tagging taxonomy, and paid reuse constraints
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Campaign analytics QA: Campaign plan, channels, events, conversion definition, dashboard, and owner
- Campaign analytics QA: Expected values, test records, attribution rules, data freshness, and decision cadence
- Specific constraints, examples, and existing assets for creator performance reuse readout

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- UGC creator workflow: Which creators or assets are approved, revised, renewed, or reused
- UGC creator workflow: Which rights or approvals block paid amplification
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- Campaign analytics QA: Which metrics are trustworthy enough for a decision
- Campaign analytics QA: Which tracking gaps block launch or interpretation
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `evaluate creator assets for performance, learning, renewal, and paid reuse decisions` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for UGC creator workflow, Social content automation, Campaign analytics QA; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return creator performance readout with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for creator performance reuse readout
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: creator performance readout.
- Organizing mechanic: evaluate creator assets for performance, learning, renewal, and paid reuse decisions.
- Core fields or sections: creator asset, spend or organic context, performance signal, learning, reuse decision, renewal decision, rights check.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- UGC creator workflow: creator, deliverable, hook, proof, rights, revision, approval, reuse state
- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner
- Campaign analytics QA: event, parameter, expected value, observed value, owner, status, decision impact

## Decision Gates

- UGC creator workflow: do not mark the artifact ready until rights, usage windows, and edit permissions are explicit.
- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.
- Campaign analytics QA: do not mark the artifact ready until tracking is tested before performance interpretation.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- UGC creator workflow: Rights, usage windows, and edit permissions are explicit.
- UGC creator workflow: Creator fit is scored beyond follower count.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.
- Campaign analytics QA: Tracking is tested before performance interpretation.
- Campaign analytics QA: Each metric states the decision it can change.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- UGC creator workflow: Collecting creator assets without rights, tagging, and reuse rules.
- Social content automation: Creating a calendar before defining the repeatable content loop.
- Campaign analytics QA: Reading campaign performance before verifying event and attribution integrity.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- UGC creator workflow: approved asset rate
- UGC creator workflow: creator renewal or reuse rate
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume
- Campaign analytics QA: QA pass rate
- Campaign analytics QA: attribution coverage and data freshness

## Example Prompt

Use $creator-performance-reuse-readout to create creator performance readout for a marketing task in Content / Creator / Social. Apply the UGC creator workflow, Social content automation, Campaign analytics QA mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
