# SEO social content brief

- Category: Content / Creator / Social
- Product mechanic: blend search questions, social hooks, proof, and distribution into one content brief
- Output: SEO/social content brief
- Evidence surfaces: seo-content-briefing, social-content-automation

## When To Use

Create content briefs that work for search and social.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `seo-content-briefing` | questions, search intent, answer gaps, proof, page type, schema, and crawl paths | Which page, section, or proof asset should be created or refreshed; Which structured data or crawl fix must ship with content |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- SEO content briefing: Target queries or questions, page inventory, audience intent, and desired answer
- SEO content briefing: Proof assets, comparison gaps, schema needs, internal links, and crawl constraints
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Specific constraints, examples, and existing assets for SEO social content brief

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- SEO content briefing: Which page, section, or proof asset should be created or refreshed
- SEO content briefing: Which structured data or crawl fix must ship with content
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `blend search questions, social hooks, proof, and distribution into one content brief` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for SEO content briefing, Social content automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return SEO/social content brief with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for SEO social content brief
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: SEO/social content brief.
- Organizing mechanic: blend search questions, social hooks, proof, and distribution into one content brief.
- Core fields or sections: search question, social hook, proof, content angle, channel cut, schema need, distribution step.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- SEO content briefing: query or question, intent, page type, answer block, proof, schema, link action
- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner

## Decision Gates

- SEO content briefing: do not mark the artifact ready until each brief includes the answer, proof, schema need, and indexability check.
- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- SEO content briefing: Each brief includes the answer, proof, schema need, and indexability check.
- SEO content briefing: The content gap is tied to a specific question or intent.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- SEO content briefing: Writing generic content that does not create citable proof or answer structure.
- Social content automation: Creating a calendar before defining the repeatable content loop.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- SEO content briefing: indexed proof coverage
- SEO content briefing: answer inclusion and citation quality
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume

## Example Prompt

Use $seo-social-content-brief to create SEO/social content brief for a marketing task in Content / Creator / Social. Apply the SEO content briefing, Social content automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
