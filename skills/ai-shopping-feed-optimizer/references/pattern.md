# AI shopping feed optimizer

- Category: AI Search / Agent Discovery
- Product mechanic: optimize product feed, PDP, FAQ, image, and checkout signals for AI shopping inclusion
- Output: shopping feed optimization plan
- Evidence surfaces: ai-search-visibility-monitoring, product-image-generation, seo-content-briefing

## When To Use

Improve product inclusion and ranking in AI shopping answers.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-search-visibility-monitoring` | priority prompts, answer text, rank, entity mention, citations, and next-action paths | Which prompts need monitoring, remediation, or new proof; Which answer gaps matter enough to ship work this cycle |
| `product-image-generation` | shot type, product fidelity, merchandising context, prompts, negative constraints, and visual QA | Which image prompts are ready for generation or retouching; Which visual defects block commerce or ad use |
| `seo-content-briefing` | questions, search intent, answer gaps, proof, page type, schema, and crawl paths | Which page, section, or proof asset should be created or refreshed; Which structured data or crawl fix must ship with content |

## Required Inputs

- Brand, product, category, and buyer question set
- Answer engines or agent surfaces to inspect
- Known competitors, preferred proof, and exclusion rules
- Current crawlable pages, docs, feeds, listings, and media assets
- AI search visibility monitoring: Prompt set with persona, intent, market, and answer surface
- AI search visibility monitoring: Observed answers, ranks, citations, alternatives, and target next action
- Product image generation: Product details, required shot types, usage context, dimensions, and brand rules
- Product image generation: Prompt constraints, unacceptable artifacts, approval owner, and retouching path
- SEO content briefing: Target queries or questions, page inventory, audience intent, and desired answer
- SEO content briefing: Proof assets, comparison gaps, schema needs, internal links, and crawl constraints
- Specific constraints, examples, and existing assets for AI shopping feed optimizer

## Decision Rules

- Separate visibility, answer accuracy, citation quality, and downstream intent.
- Treat a missing citation as an evidence problem before calling it a ranking problem.
- Prioritize changes that improve the answer, the cited proof, and the next user action together.
- AI search visibility monitoring: Which prompts need monitoring, remediation, or new proof
- AI search visibility monitoring: Which answer gaps matter enough to ship work this cycle
- Product image generation: Which image prompts are ready for generation or retouching
- Product image generation: Which visual defects block commerce or ad use
- SEO content briefing: Which page, section, or proof asset should be created or refreshed
- SEO content briefing: Which structured data or crawl fix must ship with content
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `optimize product feed, PDP, FAQ, image, and checkout signals for AI shopping inclusion` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI search visibility monitoring, Product image generation, SEO content briefing; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return shopping feed optimization plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for AI shopping feed optimizer
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: shopping feed optimization plan.
- Organizing mechanic: optimize product feed, PDP, FAQ, image, and checkout signals for AI shopping inclusion.
- Core fields or sections: product, feed field, PDP proof, image signal, FAQ gap, checkout signal, answer inclusion risk, fix.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI search visibility monitoring: prompt, surface, rank or inclusion, answer summary, citation status, gap, action
- Product image generation: product, shot type, context, prompt, negative constraint, QA note, approval
- SEO content briefing: query or question, intent, page type, answer block, proof, schema, link action

## Decision Gates

- AI search visibility monitoring: do not mark the artifact ready until observed answer text is separated from interpretation.
- Product image generation: do not mark the artifact ready until product details, scale, text, and prohibited artifacts are checked.
- SEO content briefing: do not mark the artifact ready until each brief includes the answer, proof, schema need, and indexability check.

## QA Checks

- Every recommendation names the answer surface, query class, expected user, and proof asset.
- The artifact distinguishes observed answer text from inferred optimization work.
- No private evidence identities or unpublished links appear in output.
- AI search visibility monitoring: Observed answer text is separated from interpretation.
- AI search visibility monitoring: Every visibility gap has a matching proof or content action.
- Product image generation: Product details, scale, text, and prohibited artifacts are checked.
- Product image generation: Each asset has a usage context and approval state.
- SEO content briefing: Each brief includes the answer, proof, schema need, and indexability check.
- SEO content briefing: The content gap is tied to a specific question or intent.

## Failure Modes

- Optimizing pages without first defining the answer questions.
- Counting mentions while ignoring whether the answer is accurate or useful.
- Publishing generic content that does not add citable proof.
- AI search visibility monitoring: Counting mentions without checking answer accuracy and next-action usefulness.
- Product image generation: Generating appealing images that fail product fidelity or merchandising needs.
- SEO content briefing: Writing generic content that does not create citable proof or answer structure.

## Proof Metrics

- Share of answer for priority questions
- Citation inclusion and citation quality
- Referral or assisted-conversion signal
- Remediation shipped per cycle
- AI search visibility monitoring: share of answer
- AI search visibility monitoring: citation inclusion and quality
- Product image generation: asset acceptance rate
- Product image generation: visual defect rate
- SEO content briefing: indexed proof coverage
- SEO content briefing: answer inclusion and citation quality

## Example Prompt

Use $ai-shopping-feed-optimizer to create shopping feed optimization plan for a marketing task in AI Search / Agent Discovery. Apply the AI search visibility monitoring, Product image generation, SEO content briefing mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
