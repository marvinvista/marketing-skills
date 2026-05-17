# citable proof asset kit

- Category: AI Search / Agent Discovery
- Product mechanic: package claims, proof, press, docs, FAQs, and comparison assets so answers have better evidence to cite
- Output: proof kit and publishing checklist
- Evidence surfaces: answer-source-remediation, brand-governance-review

## When To Use

Create citable proof assets for AI answers and search surfaces.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `answer-source-remediation` | cited assets, missing proof, stale claims, crawl exposure, correction paths, and owner actions | Which proof, page, listing, or data fix ships first; Which answer risk needs correction before optimization work |
| `brand-governance-review` | claims, proof, voice, compliance risk, platform limits, and approval state | What can publish, what needs edits, and what needs explicit approval; Which recurring issue should be added to voice or claim memory |

## Required Inputs

- Brand, product, category, and buyer question set
- Answer engines or agent surfaces to inspect
- Known competitors, preferred proof, and exclusion rules
- Current crawlable pages, docs, feeds, listings, and media assets
- Answer source remediation: Observed answer gaps, cited assets, missing proof, stale pages, and desired correction
- Answer source remediation: Publishing owner, content or data action, review need, and expected answer change
- Brand governance review: Brand voice, approved claims, banned patterns, legal or policy constraints
- Brand governance review: Draft asset, channel, proof links or notes, reviewer, and required approval level
- Specific constraints, examples, and existing assets for citable proof asset kit

## Decision Rules

- Separate visibility, answer accuracy, citation quality, and downstream intent.
- Treat a missing citation as an evidence problem before calling it a ranking problem.
- Prioritize changes that improve the answer, the cited proof, and the next user action together.
- Answer source remediation: Which proof, page, listing, or data fix ships first
- Answer source remediation: Which answer risk needs correction before optimization work
- Brand governance review: What can publish, what needs edits, and what needs explicit approval
- Brand governance review: Which recurring issue should be added to voice or claim memory
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `package claims, proof, press, docs, FAQs, and comparison assets so answers have better evidence to cite` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Answer source remediation, Brand governance review; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return proof kit and publishing checklist with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for citable proof asset kit
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: proof kit and publishing checklist.
- Organizing mechanic: package claims, proof, press, docs, FAQs, and comparison assets so answers have better evidence to cite.
- Core fields or sections: claim, proof asset, format, audience question, citation target, publishing owner, review state, refresh date.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Answer source remediation: answer gap, claim, current proof, missing proof, fix, owner, status
- Brand governance review: claim, proof, risk level, voice issue, required edit, owner, approval state

## Decision Gates

- Answer source remediation: do not mark the artifact ready until every remediation item ties to a specific answer gap.
- Brand governance review: do not mark the artifact ready until unsupported claims are blocked or rewritten before launch.

## QA Checks

- Every recommendation names the answer surface, query class, expected user, and proof asset.
- The artifact distinguishes observed answer text from inferred optimization work.
- No private evidence identities or unpublished links appear in output.
- Answer source remediation: Every remediation item ties to a specific answer gap.
- Answer source remediation: The fix improves evidence quality, not just keyword coverage.
- Brand governance review: Unsupported claims are blocked or rewritten before launch.
- Brand governance review: Edits preserve intent while removing risk.

## Failure Modes

- Optimizing pages without first defining the answer questions.
- Counting mentions while ignoring whether the answer is accurate or useful.
- Publishing generic content that does not add citable proof.
- Answer source remediation: Calling a ranking problem before checking whether answer evidence is missing or stale.
- Brand governance review: Treating brand review as tone cleanup while ignoring proof and risk.

## Proof Metrics

- Share of answer for priority questions
- Citation inclusion and citation quality
- Referral or assisted-conversion signal
- Remediation shipped per cycle
- Answer source remediation: remediation shipped
- Answer source remediation: citation coverage and accuracy
- Brand governance review: review issue count
- Brand governance review: approval turnaround time

## Example Prompt

Use $citable-proof-asset-kit to create proof kit and publishing checklist for a marketing task in AI Search / Agent Discovery. Apply the Answer source remediation, Brand governance review mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
