#!/usr/bin/env python3
"""Generate anonymized AI marketing product-mechanic skills."""

from __future__ import annotations

import argparse
import json
import shutil
import textwrap
from dataclasses import asdict, dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
DATA_DIR = REPO_ROOT / "data"
DATA_FILE = DATA_DIR / "marketing_skills.json"

COMPILED_ON = "2026-05-17"
LICENSE_TEXT = """MIT License

Copyright (c) 2026 Marvin Vista

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


@dataclass(frozen=True)
class SkillSpec:
    name: str
    display_name: str
    category: str
    mechanic: str
    one_line_description: str
    output: str
    surfaces: tuple[str, ...]
    script: str | None = None


CATEGORY_CONFIG = {
    "AI Search / Agent Discovery": {
        "inputs": [
            "Brand, product, category, and buyer question set",
            "Answer engines or agent surfaces to inspect",
            "Known competitors, preferred proof, and exclusion rules",
            "Current crawlable pages, docs, feeds, listings, and media assets",
        ],
        "rules": [
            "Separate visibility, answer accuracy, citation quality, and downstream intent.",
            "Treat a missing citation as an evidence problem before calling it a ranking problem.",
            "Prioritize changes that improve the answer, the cited proof, and the next user action together.",
        ],
        "qa": [
            "Every recommendation names the answer surface, query class, expected user, and proof asset.",
            "The artifact distinguishes observed answer text from inferred optimization work.",
            "No private evidence identities or unpublished links appear in output.",
        ],
        "failures": [
            "Optimizing pages without first defining the answer questions.",
            "Counting mentions while ignoring whether the answer is accurate or useful.",
            "Publishing generic content that does not add citable proof.",
        ],
        "metrics": [
            "Share of answer for priority questions",
            "Citation inclusion and citation quality",
            "Referral or assisted-conversion signal",
            "Remediation shipped per cycle",
        ],
    },
    "Creative / Ads / Assets": {
        "inputs": [
            "Audience, offer, channel, format, and conversion event",
            "Allowed claims, proof points, brand rules, and risk constraints",
            "Existing winners, losers, competitor examples, and performance readouts",
            "Production limits for copy, image, video, voice, landing page, or catalog assets",
        ],
        "rules": [
            "Change one primary variable at a time unless the task is exploratory ideation.",
            "Tie every creative angle to a buyer belief, proof point, and next action.",
            "Separate creative quality from media budget, targeting, and tracking effects.",
        ],
        "qa": [
            "Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.",
            "Unsupported claims are flagged before assets are promoted to production.",
            "The output is ready for a designer, editor, media buyer, or reviewer to use.",
        ],
        "failures": [
            "Generating many variants without a testable hypothesis matrix.",
            "Letting style changes masquerade as positioning tests.",
            "Ignoring platform, legal, or brand constraints until final review.",
        ],
        "metrics": [
            "Creative holdout or lift signal",
            "Hook, thumb-stop, click, and conversion movement",
            "Approval cycle time",
            "Reusable winning assets created",
        ],
    },
    "Content / Creator / Social": {
        "inputs": [
            "Audience, channel, creator type, content format, and cadence",
            "Message pillars, proof, brand voice, and claim boundaries",
            "Source asset or campaign moment to repurpose",
            "Distribution path, usage rights, and review cadence",
        ],
        "rules": [
            "Make the content mechanic explicit before writing posts or scripts.",
            "Preserve the claim and proof when adapting across channels or languages.",
            "Separate creator sourcing, asset intake, approval, and reuse rights.",
        ],
        "qa": [
            "The asset can be produced without hidden context.",
            "Hooks, examples, captions, CTAs, and review notes are channel-specific.",
            "Reuse rights, attribution needs, and approval checkpoints are visible.",
        ],
        "failures": [
            "Writing a calendar before defining the repeatable content loop.",
            "Treating creator fit as follower count alone.",
            "Repurposing content without adapting the proof or CTA to the channel.",
        ],
        "metrics": [
            "Qualified engagement",
            "Reusable asset volume",
            "Creator acceptance and renewal signal",
            "Downstream lead or sales-assist signal",
        ],
    },
    "Lead Intelligence / Conversion": {
        "inputs": [
            "Target account or lead segment, trigger, and disqualifiers",
            "Available lists, enrichment fields, intent signals, and consent limits",
            "Sales handoff owner, CRM fields, and next-step rules",
            "Message library, proof, and routing or booking path",
        ],
        "rules": [
            "Do not enrich or sequence leads until the qualification rule is explicit.",
            "Tie personalization to a real trigger, pain, role, or account event.",
            "Route every reply, visit, or chat outcome to a named next action.",
        ],
        "qa": [
            "Every record has fit, intent, evidence, and next-step fields or a clear gap.",
            "Outreach respects suppression, consent, and channel-specific risk.",
            "The handoff is auditable from signal to owner to next step.",
        ],
        "failures": [
            "Building large lists with no disqualification logic.",
            "Using enrichment fields that do not change the message or route.",
            "Automating follow-up before reply handling is defined.",
        ],
        "metrics": [
            "Qualified records created",
            "Positive reply or booking rate",
            "Signal-to-action latency",
            "Handoff completion and CRM accuracy",
        ],
    },
    "Research / Audience Simulation": {
        "inputs": [
            "Decision to improve and audience segment under study",
            "Known assumptions, hypotheses, and prior evidence",
            "Research method, respondent criteria, and confidence threshold",
            "Synthesis format required for a campaign, product, or positioning decision",
        ],
        "rules": [
            "Frame the decision before collecting or simulating responses.",
            "Keep observed evidence, synthetic output, and inference separate.",
            "Translate findings into a decision, not just themes.",
        ],
        "qa": [
            "The artifact states sample, segment, assumption, and confidence limits.",
            "Findings include implications, objections, and next evidence to collect.",
            "Quotes or examples are labeled by evidence type.",
        ],
        "failures": [
            "Treating synthetic responses as proof without validation.",
            "Summarizing interviews without a decision framework.",
            "Averaging segments that need different messages or channels.",
        ],
        "metrics": [
            "Decision confidence",
            "Assumptions validated or rejected",
            "Segment or message clarity",
            "Next evidence cost reduced",
        ],
    },
    "Lifecycle / Ops / Analytics": {
        "inputs": [
            "Campaign, lifecycle, or data workflow boundary",
            "Events, properties, audiences, consent rules, and owners",
            "Tools, destinations, templates, and rollback constraints",
            "Measurement question and decision cadence",
        ],
        "rules": [
            "Define the data contract before evaluating performance.",
            "QA audiences, assets, tracking, and rollback before launch.",
            "Separate plumbing failures from campaign-performance interpretation.",
        ],
        "qa": [
            "Every field, audience, event, and destination has an owner and check.",
            "Consent, suppression, and rollback are visible in the artifact.",
            "The readout says what decision the metric will change.",
        ],
        "failures": [
            "Reading performance before verifying event and audience integrity.",
            "Launching without suppression or rollback coverage.",
            "Building dashboards that do not map to an operating decision.",
        ],
        "metrics": [
            "QA pass rate",
            "Audience sync accuracy",
            "Decision latency",
            "Lifecycle movement or reactivation lift",
        ],
    },
    "Marketing Agents / Governance": {
        "inputs": [
            "Bounded marketing job, allowed tools, and final artifact",
            "Human judgment points, review owners, and escalation rules",
            "Brand memory, prompt library, evidence base, and eval criteria",
            "Telemetry needs, rollout stage, and risk tolerance",
        ],
        "rules": [
            "Scope the agent by job, artifact, allowed actions, and failure mode.",
            "Put review gates where factuality, claim risk, brand fit, or spend can fail.",
            "Use evals before expanding autonomy or tool access.",
        ],
        "qa": [
            "The workflow states what the agent can decide, draft, route, or never do.",
            "Each tool call has an input, output, owner, and failure fallback.",
            "Telemetry captures quality, acceptance, rework, and business impact.",
        ],
        "failures": [
            "Designing an agent around a vague role instead of a bounded job.",
            "Skipping approval because the first demos look plausible.",
            "Measuring volume without quality, acceptance, or risk metrics.",
        ],
        "metrics": [
            "Acceptance rate",
            "Review burden and rework rate",
            "Eval pass rate",
            "Time saved with quality preserved",
        ],
    },
}


SURFACE_CONFIG = {
    "ad-creative-generation": {
        "label": "Ad creative generation",
        "inspect": "hooks, angles, proof, formats, offers, CTAs, and channel limits",
        "inputs": [
            "Audience belief, offer, channel, format, and conversion event",
            "Approved proof points, claim limits, brand rules, and prior creative results",
        ],
        "artifact_fields": ["angle", "hook", "proof point", "format", "CTA", "hypothesis", "review state"],
        "decisions": [
            "Which variable changes in the next creative test",
            "Which claim or proof needs review before production",
        ],
        "qa": [
            "Each creative variant changes one declared variable or is marked exploratory.",
            "Each claim connects to an approved proof point.",
        ],
        "failures": ["Generating asset volume without a hypothesis and review state."],
        "metrics": ["hook rate, click rate, conversion rate, and winning-asset reuse", "approval cycle time"],
    },
    "lead-list-building": {
        "label": "Lead list building",
        "inspect": "segment rules, account criteria, exclusions, dedupe logic, and owner routing",
        "inputs": [
            "ICP or segment definition, triggers, disqualifiers, and territory or market limits",
            "Required list fields, evidence standard, dedupe rule, and owner route",
        ],
        "artifact_fields": ["account or lead", "segment", "fit reason", "trigger", "evidence", "disqualifier", "route"],
        "decisions": [
            "Which records qualify for action now",
            "Which gaps block enrichment, routing, or outreach",
        ],
        "qa": [
            "Every accepted record has fit, trigger, evidence, and a route.",
            "Disqualified records state the rule that removed them.",
        ],
        "failures": ["Building a large list before defining exclusions and evidence standards."],
        "metrics": ["qualified record count", "owner acceptance rate"],
    },
    "ai-search-visibility-monitoring": {
        "label": "AI search visibility monitoring",
        "inspect": "priority prompts, answer text, rank, entity mention, citations, and next-action paths",
        "inputs": [
            "Prompt set with persona, intent, market, and answer surface",
            "Observed answers, ranks, citations, alternatives, and target next action",
        ],
        "artifact_fields": ["prompt", "surface", "rank or inclusion", "answer summary", "citation status", "gap", "action"],
        "decisions": [
            "Which prompts need monitoring, remediation, or new proof",
            "Which answer gaps matter enough to ship work this cycle",
        ],
        "qa": [
            "Observed answer text is separated from interpretation.",
            "Every visibility gap has a matching proof or content action.",
        ],
        "failures": ["Counting mentions without checking answer accuracy and next-action usefulness."],
        "metrics": ["share of answer", "citation inclusion and quality"],
    },
    "customer-research-synthesis": {
        "label": "Customer research synthesis",
        "inspect": "interviews, reviews, calls, surveys, comments, objections, and segment language",
        "inputs": [
            "Research question, target segment, decision to support, and confidence threshold",
            "Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels",
        ],
        "artifact_fields": ["theme", "evidence", "segment", "confidence", "objection", "implication", "next evidence"],
        "decisions": [
            "Which message, segment, or channel assumption changes",
            "Which evidence gap must be resolved before launch",
        ],
        "qa": [
            "Observed evidence, synthesis, and recommendation are labeled separately.",
            "Findings state confidence limits and the next evidence to collect.",
        ],
        "failures": ["Turning research into themes without a decision or confidence boundary."],
        "metrics": ["assumptions validated or rejected", "decision confidence"],
    },
    "ai-marketing-agent-workflow": {
        "label": "AI marketing agent workflow",
        "inspect": "bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry",
        "inputs": [
            "Job boundary, final artifact, allowed tools, and unavailable actions",
            "Review owner, escalation rule, eval criteria, telemetry need, and rollout stage",
        ],
        "artifact_fields": ["job", "input", "tool", "action right", "review gate", "fallback", "telemetry"],
        "decisions": [
            "What the agent may draft, route, decide, or escalate",
            "Which gate must pass before expanding autonomy",
        ],
        "qa": [
            "Every tool action has an input, output, owner, and fallback.",
            "Risky actions are blocked by review or eval gates.",
        ],
        "failures": ["Defining an agent role without a bounded job and final artifact."],
        "metrics": ["eval pass rate", "acceptance rate and rework rate"],
    },
    "social-content-automation": {
        "label": "Social content automation",
        "inspect": "channel rules, cadence, hooks, captions, media, voice, approvals, and response loops",
        "inputs": [
            "Channels, cadence, voice rules, message pillars, and campaign moment",
            "Asset inventory, approval owner, comment handling rule, and distribution path",
        ],
        "artifact_fields": ["channel", "post type", "hook", "proof", "caption", "CTA", "asset state", "owner"],
        "decisions": [
            "Which content repeats as a system versus a one-off post",
            "Which approvals or response rules block scheduling",
        ],
        "qa": [
            "Hooks, examples, CTAs, and review notes are channel-specific.",
            "The content can be produced without hidden context.",
        ],
        "failures": ["Creating a calendar before defining the repeatable content loop."],
        "metrics": ["publishing reliability", "qualified engagement and reusable asset volume"],
    },
    "seo-content-briefing": {
        "label": "SEO content briefing",
        "inspect": "questions, search intent, answer gaps, proof, page type, schema, and crawl paths",
        "inputs": [
            "Target queries or questions, page inventory, audience intent, and desired answer",
            "Proof assets, comparison gaps, schema needs, internal links, and crawl constraints",
        ],
        "artifact_fields": ["query or question", "intent", "page type", "answer block", "proof", "schema", "link action"],
        "decisions": [
            "Which page, section, or proof asset should be created or refreshed",
            "Which structured data or crawl fix must ship with content",
        ],
        "qa": [
            "Each brief includes the answer, proof, schema need, and indexability check.",
            "The content gap is tied to a specific question or intent.",
        ],
        "failures": ["Writing generic content that does not create citable proof or answer structure."],
        "metrics": ["indexed proof coverage", "answer inclusion and citation quality"],
    },
    "brand-governance-review": {
        "label": "Brand governance review",
        "inspect": "claims, proof, voice, compliance risk, platform limits, and approval state",
        "inputs": [
            "Brand voice, approved claims, banned patterns, legal or policy constraints",
            "Draft asset, channel, proof links or notes, reviewer, and required approval level",
        ],
        "artifact_fields": ["claim", "proof", "risk level", "voice issue", "required edit", "owner", "approval state"],
        "decisions": [
            "What can publish, what needs edits, and what needs explicit approval",
            "Which recurring issue should be added to voice or claim memory",
        ],
        "qa": [
            "Unsupported claims are blocked or rewritten before launch.",
            "Edits preserve intent while removing risk.",
        ],
        "failures": ["Treating brand review as tone cleanup while ignoring proof and risk."],
        "metrics": ["review issue count", "approval turnaround time"],
    },
    "lead-enrichment-and-research": {
        "label": "Lead enrichment and research",
        "inspect": "fields, evidence freshness, confidence, role pain, trigger, message use, and fallback behavior",
        "inputs": [
            "Target records, required enrichment fields, freshness rule, and source priority",
            "Usage rule for routing, personalization, scoring, and fallback when a field is missing",
        ],
        "artifact_fields": ["record", "field", "value", "confidence", "freshness", "message use", "fallback"],
        "decisions": [
            "Which fields change score, route, or message",
            "Which missing fields require manual research or conservative fallback",
        ],
        "qa": [
            "Every enrichment field has a usage rule and freshness standard.",
            "Low-confidence values are not used for strong personalization.",
        ],
        "failures": ["Collecting enrichment data that does not change routing or messaging."],
        "metrics": ["field completion rate", "freshness and confidence coverage"],
    },
    "video-ad-production": {
        "label": "Video ad production",
        "inspect": "hook, scene order, shot list, product moments, captions, voice, timing, and edit notes",
        "inputs": [
            "Audience, platform, duration, format, offer, proof, and production constraints",
            "Required shots, voice style, caption style, legal notes, and review owner",
        ],
        "artifact_fields": ["scene", "hook", "shot", "line", "visual", "caption", "edit note", "review flag"],
        "decisions": [
            "Which moments belong in the first seconds versus proof body",
            "Which shots, claims, or edits need production review",
        ],
        "qa": [
            "The storyboard names timing, visual, line, caption, and CTA.",
            "Claims and product depictions are reviewable before editing starts.",
        ],
        "failures": ["Writing a script without shot, timing, and review instructions."],
        "metrics": ["hook retention", "asset completion and approval rate"],
    },
    "audience-data-sync": {
        "label": "Audience data sync",
        "inspect": "fields, joins, freshness, destinations, exclusions, consent, owner checks, and sync failures",
        "inputs": [
            "Audience definition, field mapping, refresh cadence, destination, and owner",
            "Consent, suppression, join keys, exclusion rules, and expected row counts",
        ],
        "artifact_fields": ["audience", "field", "join key", "destination", "refresh", "exclusion", "owner", "check"],
        "decisions": [
            "Which audience is eligible for activation",
            "Which sync gap blocks launch or needs rollback",
        ],
        "qa": [
            "Expected and actual counts are checked before activation.",
            "Consent and suppression rules are visible in the contract.",
        ],
        "failures": ["Activating an audience before validating fields, counts, and exclusions."],
        "metrics": ["match rate", "sync latency and error rate"],
    },
    "outbound-cadence-automation": {
        "label": "Outbound cadence automation",
        "inspect": "trigger, channel sequence, wait states, personalization, stop rules, replies, and owner handoff",
        "inputs": [
            "Target segment, trigger, proof point, channel mix, and reply route",
            "Suppression rules, step timing, stop conditions, owner, and fallback copy",
        ],
        "artifact_fields": ["step", "channel", "trigger", "message angle", "wait", "stop rule", "route"],
        "decisions": [
            "Which step runs, stops, or escalates based on signal",
            "Which personalization is strong enough to use",
        ],
        "qa": [
            "Every step has a trigger, wait rule, stop rule, and reply route.",
            "Suppression and unsubscribe paths are handled before sending.",
        ],
        "failures": ["Automating follow-up before reply handling and stop rules are defined."],
        "metrics": ["positive reply rate", "booking rate and unsubscribe rate"],
    },
    "answer-source-remediation": {
        "label": "Answer source remediation",
        "inspect": "cited assets, missing proof, stale claims, crawl exposure, correction paths, and owner actions",
        "inputs": [
            "Observed answer gaps, cited assets, missing proof, stale pages, and desired correction",
            "Publishing owner, content or data action, review need, and expected answer change",
        ],
        "artifact_fields": ["answer gap", "claim", "current proof", "missing proof", "fix", "owner", "status"],
        "decisions": [
            "Which proof, page, listing, or data fix ships first",
            "Which answer risk needs correction before optimization work",
        ],
        "qa": [
            "Every remediation item ties to a specific answer gap.",
            "The fix improves evidence quality, not just keyword coverage.",
        ],
        "failures": ["Calling a ranking problem before checking whether answer evidence is missing or stale."],
        "metrics": ["remediation shipped", "citation coverage and accuracy"],
    },
    "marketing-ops-orchestration": {
        "label": "Marketing ops orchestration",
        "inspect": "owners, dependencies, systems, approvals, launch states, fallback paths, and rollback",
        "inputs": [
            "Workflow boundary, systems involved, owner map, launch date, and dependency list",
            "Approval needs, fallback path, rollback trigger, and status reporting cadence",
        ],
        "artifact_fields": ["workstream", "owner", "dependency", "system", "approval", "fallback", "rollback", "status"],
        "decisions": [
            "Which work can launch, wait, or roll back",
            "Which owner or dependency blocks the next action",
        ],
        "qa": [
            "Every dependency has an owner and failure fallback.",
            "Launch and rollback criteria are visible before execution.",
        ],
        "failures": ["Shipping a workflow with unclear ownership or rollback responsibility."],
        "metrics": ["cycle time", "handoff completion and rollback readiness"],
    },
    "synthetic-audience-simulation": {
        "label": "Synthetic audience simulation",
        "inspect": "persona assumptions, prompt framing, scenarios, synthetic responses, validation needs, and confidence limits",
        "inputs": [
            "Audience definition, assumptions, scenario, question set, and intended decision",
            "Validation plan, confidence threshold, known evidence, and excluded claims",
        ],
        "artifact_fields": ["persona", "assumption", "scenario", "prompt", "response", "confidence", "validation need"],
        "decisions": [
            "Which hypotheses are worth testing with real evidence",
            "Which simulated output must not be treated as proof",
        ],
        "qa": [
            "Synthetic output is labeled separately from observed evidence.",
            "The artifact includes a validation step before launch use.",
        ],
        "failures": ["Treating simulated reactions as proof instead of hypothesis generation."],
        "metrics": ["assumption shortlist quality", "validation hit rate"],
    },
    "inbound-chat-qualification": {
        "label": "Inbound chat qualification",
        "inspect": "questions, answer branches, qualification rules, fallback copy, handoff notes, and booking path",
        "inputs": [
            "Target visitor, qualification criteria, required fields, and disqualifiers",
            "Chat questions, routing rules, handoff owner, fallback message, and booking path",
        ],
        "artifact_fields": ["question", "answer branch", "qualification rule", "score", "route", "fallback", "handoff note"],
        "decisions": [
            "Which visitors book, route to a human, nurture, or exit",
            "Which questions are necessary versus conversion friction",
        ],
        "qa": [
            "Each question changes routing or qualification.",
            "Fallback and handoff messages preserve context for the next owner.",
        ],
        "failures": ["Asking chat questions that do not change route or handoff quality."],
        "metrics": ["qualified handoff rate", "booking completion and fallback rate"],
    },
    "ugc-creator-workflow": {
        "label": "UGC creator workflow",
        "inspect": "creator fit, deliverables, asset intake, rights, approvals, revisions, tagging, and reuse",
        "inputs": [
            "Creator criteria, offer, deliverables, asset examples, and usage rights",
            "Approval path, revision rule, tagging taxonomy, and paid reuse constraints",
        ],
        "artifact_fields": ["creator", "deliverable", "hook", "proof", "rights", "revision", "approval", "reuse state"],
        "decisions": [
            "Which creators or assets are approved, revised, renewed, or reused",
            "Which rights or approvals block paid amplification",
        ],
        "qa": [
            "Rights, usage windows, and edit permissions are explicit.",
            "Creator fit is scored beyond follower count.",
        ],
        "failures": ["Collecting creator assets without rights, tagging, and reuse rules."],
        "metrics": ["approved asset rate", "creator renewal or reuse rate"],
    },
    "website-visitor-identification": {
        "label": "Website visitor identification",
        "inspect": "visit pattern, account match, intent level, page path, evidence, owner route, and follow-up timing",
        "inputs": [
            "Visitor or account matching method, page events, intent threshold, and freshness window",
            "Routing owner, CRM fields, follow-up rule, and confidence fallback",
        ],
        "artifact_fields": ["visit", "matched account", "intent level", "evidence", "confidence", "owner", "follow-up"],
        "decisions": [
            "Which visits trigger sales, nurture, retargeting, or no action",
            "Which matches are too uncertain for direct outreach",
        ],
        "qa": [
            "Confidence level and evidence are visible before routing.",
            "Follow-up timing matches observed intent, not just page view volume.",
        ],
        "failures": ["Routing anonymous visits without confidence and intent thresholds."],
        "metrics": ["match rate", "signal-to-action latency"],
    },
    "message-testing": {
        "label": "Message testing",
        "inspect": "audience, claim, proof, clarity, differentiation, objection handling, risk, and next action",
        "inputs": [
            "Messages to compare, target audience, channel, decision criteria, and scoring scale",
            "Proof points, objections, alternatives, risk constraints, and intended next action",
        ],
        "artifact_fields": ["message", "audience", "claim", "proof", "score", "risk", "objection", "next test"],
        "decisions": [
            "Which message advances, changes, or gets rejected",
            "Which weakness requires research, proof, or creative iteration",
        ],
        "qa": [
            "Scores use explicit criteria instead of preference alone.",
            "The winning message includes a next test or launch boundary.",
        ],
        "failures": ["Choosing a message without separating clarity, proof, differentiation, and risk."],
        "metrics": ["message score movement", "conversion or reply lift"],
    },
    "local-storefront-growth": {
        "label": "Local storefront growth",
        "inspect": "locations, radius, local offer, route plan, reviews, community proof, and owner follow-up",
        "inputs": [
            "Target location set, radius, category, offer, local proof, and field owner",
            "Route constraints, review signals, storefront data, and follow-up channel",
        ],
        "artifact_fields": ["location", "radius", "offer", "local proof", "route", "owner", "follow-up"],
        "decisions": [
            "Which local targets get field action versus digital follow-up",
            "Which local proof or listing gap blocks trust",
        ],
        "qa": [
            "Routes are prioritized by fit, proximity, and actionability.",
            "Local proof is tied to the offer and outreach path.",
        ],
        "failures": ["Treating local prospecting as a generic list without route and proof context."],
        "metrics": ["route completion", "local response or conversion rate"],
    },
    "campaign-analytics-qa": {
        "label": "Campaign analytics QA",
        "inspect": "UTMs, events, conversion paths, dashboards, attribution fields, expected values, and readout decisions",
        "inputs": [
            "Campaign plan, channels, events, conversion definition, dashboard, and owner",
            "Expected values, test records, attribution rules, data freshness, and decision cadence",
        ],
        "artifact_fields": ["event", "parameter", "expected value", "observed value", "owner", "status", "decision impact"],
        "decisions": [
            "Which metrics are trustworthy enough for a decision",
            "Which tracking gaps block launch or interpretation",
        ],
        "qa": [
            "Tracking is tested before performance interpretation.",
            "Each metric states the decision it can change.",
        ],
        "failures": ["Reading campaign performance before verifying event and attribution integrity."],
        "metrics": ["QA pass rate", "attribution coverage and data freshness"],
    },
    "product-image-generation": {
        "label": "Product image generation",
        "inspect": "shot type, product fidelity, merchandising context, prompts, negative constraints, and visual QA",
        "inputs": [
            "Product details, required shot types, usage context, dimensions, and brand rules",
            "Prompt constraints, unacceptable artifacts, approval owner, and retouching path",
        ],
        "artifact_fields": ["product", "shot type", "context", "prompt", "negative constraint", "QA note", "approval"],
        "decisions": [
            "Which image prompts are ready for generation or retouching",
            "Which visual defects block commerce or ad use",
        ],
        "qa": [
            "Product details, scale, text, and prohibited artifacts are checked.",
            "Each asset has a usage context and approval state.",
        ],
        "failures": ["Generating appealing images that fail product fidelity or merchandising needs."],
        "metrics": ["asset acceptance rate", "visual defect rate"],
    },
}


SKILL_SPECS = [
    SkillSpec("agent-discovery-question-map", "agent discovery question map", "AI Search / Agent Discovery", "map buyer questions to the answer engines, agents, and proof assets that can influence discovery", "Turn buyer questions into a prioritized answer-engine inspection map.", "question map, prompt set, and proof inventory", ("ai-search-visibility-monitoring", "answer-source-remediation")),
    SkillSpec("ai-answer-visibility-scorecard", "AI answer visibility scorecard", "AI Search / Agent Discovery", "score brand visibility, answer accuracy, citation quality, and next-action usefulness across answer surfaces", "Audit how a brand, product, or category appears in AI answers.", "visibility scorecard with remediation backlog", ("ai-search-visibility-monitoring", "answer-source-remediation")),
    SkillSpec("prompt-rank-monitor", "prompt rank monitor", "AI Search / Agent Discovery", "build a reusable prompt-rank table for answer engines and competitor comparisons", "Track answer-engine rank and mention quality across a repeatable prompt set.", "prompt-rank table and monitoring cadence", ("ai-search-visibility-monitoring",), "build_prompt_rank_table.py"),
    SkillSpec("share-of-answer-benchmark", "share of answer benchmark", "AI Search / Agent Discovery", "compare answer share, entity mentions, claim framing, and competitor displacement opportunities", "Benchmark answer share against competitors and alternatives.", "share-of-answer report", ("ai-search-visibility-monitoring", "customer-research-synthesis")),
    SkillSpec("citation-source-gap-map", "citation source gap map", "AI Search / Agent Discovery", "identify cited and uncited proof assets, pages, listings, and third-party references", "Find the proof assets answer engines cite, miss, or distort.", "citation gap map and proof backlog", ("answer-source-remediation", "seo-content-briefing")),
    SkillSpec("citable-proof-asset-kit", "citable proof asset kit", "AI Search / Agent Discovery", "package claims, proof, press, docs, FAQs, and comparison assets so answers have better evidence to cite", "Create citable proof assets for AI answers and search surfaces.", "proof kit and publishing checklist", ("answer-source-remediation", "brand-governance-review")),
    SkillSpec("answer-ready-content-brief", "answer-ready content brief", "AI Search / Agent Discovery", "write content briefs for missing questions with answer structure, evidence, and schema needs", "Produce briefs for answer-ready pages or docs.", "answer-ready content brief", ("seo-content-briefing", "answer-source-remediation")),
    SkillSpec("page-schema-indexability-audit", "page schema indexability audit", "AI Search / Agent Discovery", "check whether pages, structured data, feeds, and crawl paths expose the proof agents need", "Audit indexability and structured proof for AI discovery.", "indexability audit and implementation tickets", ("seo-content-briefing", "answer-source-remediation")),
    SkillSpec("ai-shopping-feed-optimizer", "AI shopping feed optimizer", "AI Search / Agent Discovery", "optimize product feed, PDP, FAQ, image, and checkout signals for AI shopping inclusion", "Improve product inclusion and ranking in AI shopping answers.", "shopping feed optimization plan", ("ai-search-visibility-monitoring", "product-image-generation", "seo-content-briefing")),
    SkillSpec("agent-action-backlog", "agent action backlog", "AI Search / Agent Discovery", "convert visibility gaps into the smallest on-page, off-page, data, and workflow actions to ship", "Prioritize actions that improve agent discovery and answer inclusion.", "ranked agent-discovery action backlog", ("ai-search-visibility-monitoring", "answer-source-remediation", "marketing-ops-orchestration")),
    SkillSpec("ai-referral-roi-readout", "AI referral ROI readout", "AI Search / Agent Discovery", "read AI referrals, bot traffic, assisted conversion, and revenue signal without over-claiming attribution", "Measure AI-search and answer-surface traffic value with attribution caveats.", "AI referral readout and dashboard spec", ("ai-search-visibility-monitoring", "campaign-analytics-qa")),
    SkillSpec("generative-search-weekly-ops-report", "generative search weekly ops report", "AI Search / Agent Discovery", "turn answer visibility, citation gaps, traffic signal, and shipped fixes into a recurring operator report", "Create a recurring operating report for AI visibility work.", "weekly ops report with actions", ("ai-search-visibility-monitoring", "answer-source-remediation", "campaign-analytics-qa")),
    SkillSpec("answer-claim-risk-review", "answer claim risk review", "AI Search / Agent Discovery", "review AI answers for unsupported claims, stale positioning, missing caveats, and brand-risky phrasing", "Review AI answer text for claim, accuracy, and brand risk.", "answer risk review and correction plan", ("brand-governance-review", "answer-source-remediation")),
    SkillSpec("agent-discovery-content-refresh-plan", "agent discovery content refresh plan", "AI Search / Agent Discovery", "refresh stale pages, FAQs, comparison copy, and proof assets based on answer-surface gaps", "Plan content refreshes that improve AI discovery.", "refresh plan and CMS handoff", ("seo-content-briefing", "ai-search-visibility-monitoring")),
    SkillSpec("agentic-answer-ops-workflow", "agentic answer ops workflow", "AI Search / Agent Discovery", "orchestrate AI answer monitoring, evidence lookup, remediation actions, review gates, and telemetry", "Design agent-assisted operations for AI answer visibility and remediation.", "agentic answer ops workflow", ("ai-marketing-agent-workflow", "ai-search-visibility-monitoring", "answer-source-remediation")),
    SkillSpec("ai-answer-brand-risk-map", "AI answer brand risk map", "AI Search / Agent Discovery", "connect answer visibility observations to brand risk, claim status, proof gaps, and correction owners", "Map AI answer visibility into brand and claim risk actions.", "AI answer brand risk map", ("ai-search-visibility-monitoring", "brand-governance-review", "answer-source-remediation")),
    SkillSpec("seo-brand-proof-governance", "SEO brand proof governance", "AI Search / Agent Discovery", "govern search and answer-ready content by approved proof, schema needs, claim risk, and publish decisions", "Review SEO and AI-search briefs for proof, brand, and claim readiness.", "SEO proof governance brief", ("seo-content-briefing", "brand-governance-review", "answer-source-remediation")),
    SkillSpec("search-creative-message-bridge", "search creative message bridge", "AI Search / Agent Discovery", "translate answer-surface insights into creative angles, proof reuse, channel messages, and next tests", "Turn AI answer insights into testable creative messaging.", "search-to-creative message bridge", ("ai-search-visibility-monitoring", "ad-creative-generation", "customer-research-synthesis")),
    SkillSpec("offer-angle-mining", "offer angle mining", "Creative / Ads / Assets", "mine research, reviews, competitor ads, and sales objections for offer angles worth testing", "Find the strongest campaign angles before writing creative.", "offer angle map", ("ad-creative-generation", "customer-research-synthesis")),
    SkillSpec("creative-brief-from-research", "creative brief from research", "Creative / Ads / Assets", "convert audience insight, proof, and objections into a production-ready creative brief", "Turn research into a brief for ads, landing pages, or assets.", "creative brief with claims, proof, and constraints", ("ad-creative-generation", "customer-research-synthesis")),
    SkillSpec("ad-variant-matrix-builder", "ad variant matrix builder", "Creative / Ads / Assets", "generate a controlled variant matrix across hooks, angles, proof, CTAs, and formats", "Create structured ad variants for controlled creative testing.", "creative variant matrix", ("ad-creative-generation", "message-testing"), "build_variant_matrix.py"),
    SkillSpec("visual-asset-prompt-brief", "visual asset prompt brief", "Creative / Ads / Assets", "write generation prompts and production notes for image, video, and mixed-media ad assets", "Specify AI-generated visual assets for campaign production.", "visual prompt brief and production notes", ("ad-creative-generation", "product-image-generation")),
    SkillSpec("product-image-qa-brief", "product image QA brief", "Creative / Ads / Assets", "define product image generation constraints, shot types, merchandising context, and QA checks", "Create and QA product imagery for commerce or ads.", "product image brief and QA checklist", ("product-image-generation", "ad-creative-generation")),
    SkillSpec("catalog-ad-feed-plan", "catalog ad feed plan", "Creative / Ads / Assets", "turn product attributes, audience segments, and creative rules into a catalog ad feed plan", "Build repeatable catalog creative from product data.", "catalog creative feed plan", ("ad-creative-generation", "product-image-generation", "audience-data-sync")),
    SkillSpec("video-ad-storyboard", "video ad storyboard", "Creative / Ads / Assets", "structure video ads into hook, proof, product moment, objection, CTA, and edit notes", "Storyboard video ads from campaign inputs and production constraints.", "video storyboard and shot list", ("video-ad-production", "ad-creative-generation")),
    SkillSpec("short-form-hook-bank", "short-form hook bank", "Creative / Ads / Assets", "generate platform-specific hooks for short-form video while preserving proof and CTA", "Build a hook bank for short-form creative testing.", "hook bank and test notes", ("video-ad-production", "social-content-automation")),
    SkillSpec("ugc-ad-script-pack", "UGC ad script pack", "Creative / Ads / Assets", "write creator-style ad scripts with believable hooks, proof moments, and usage constraints", "Create UGC-style ad scripts for paid or organic use.", "UGC script pack", ("ugc-creator-workflow", "ad-creative-generation")),
    SkillSpec("landing-page-message-match", "landing page message match", "Creative / Ads / Assets", "align ad angle, page headline, proof, objections, CTA, and tracking for a conversion path", "Design landing-page variants matched to ad angles.", "message-match landing page spec", ("ad-creative-generation", "message-testing", "seo-content-briefing")),
    SkillSpec("competitor-ad-teardown", "competitor ad teardown", "Creative / Ads / Assets", "reverse engineer competitor angles, proof, offers, formats, and gaps without copying execution", "Analyze competitor ads for testable creative opportunities.", "competitor ad teardown", ("ad-creative-generation", "customer-research-synthesis")),
    SkillSpec("creative-fatigue-refresh-plan", "creative fatigue refresh plan", "Creative / Ads / Assets", "diagnose creative fatigue and plan refreshes by angle, asset, audience, and format", "Refresh fatigued creative without resetting the learning loop.", "creative refresh plan", ("ad-creative-generation", "campaign-analytics-qa")),
    SkillSpec("paid-launch-checklist", "paid launch checklist", "Creative / Ads / Assets", "turn creative, targeting, budget, tracking, approvals, and rollback into a launch checklist", "Prepare a paid campaign for launch with QA coverage.", "paid launch checklist", ("ad-creative-generation", "campaign-analytics-qa", "marketing-ops-orchestration")),
    SkillSpec("creative-performance-readout", "creative performance readout", "Creative / Ads / Assets", "separate creative signal from tracking, spend, audience, and conversion-path noise", "Analyze creative results and choose next tests.", "creative readout and next-test backlog", ("ad-creative-generation", "campaign-analytics-qa")),
    SkillSpec("brand-compliance-creative-review", "brand compliance creative review", "Creative / Ads / Assets", "review ads and assets for claim support, brand fit, legal risk, and platform constraints", "Review creative before launch, reuse, or paid amplification.", "creative compliance review", ("brand-governance-review", "ad-creative-generation")),
    SkillSpec("multilingual-creative-localization", "multilingual creative localization", "Creative / Ads / Assets", "localize campaign copy, video, voice, and proof while preserving intent and claim boundaries", "Localize campaign creative without losing meaning or compliance.", "localized creative plan", ("social-content-automation", "brand-governance-review", "video-ad-production")),
    SkillSpec("podcast-audio-ad-read-guide", "podcast audio ad read guide", "Creative / Ads / Assets", "write host-read or produced audio ads with pronunciation, timing, claim, and CTA control", "Create podcast or audio ad copy and read guidance.", "audio ad script and read guide", ("social-content-automation", "ad-creative-generation")),
    SkillSpec("multimodal-asset-assembly-brief", "multimodal asset assembly brief", "Creative / Ads / Assets", "compose image, video, voice, copy, captions, and landing proof into one coherent asset plan", "Plan multimodal ad assets across formats and review states.", "multimodal assembly brief", ("ad-creative-generation", "video-ad-production", "product-image-generation", "brand-governance-review")),
    SkillSpec("creative-lead-capture-loop", "creative lead capture loop", "Creative / Ads / Assets", "connect creative angles to lead signals, capture fields, list rules, follow-up routes, and measurement events", "Turn paid or organic creative into a lead-capture operating loop.", "creative lead-capture loop", ("ad-creative-generation", "lead-list-building")),
    SkillSpec("creative-agent-production-workflow", "creative agent production workflow", "Creative / Ads / Assets", "scope an AI workflow for generating creative variants, applying review gates, and handing off approved assets", "Specify agent-assisted creative production with review and handoff gates.", "creative agent production workflow", ("ad-creative-generation", "ai-marketing-agent-workflow")),
    SkillSpec("agentic-video-production-workflow", "agentic video production workflow", "Creative / Ads / Assets", "scope agent-assisted video production from script inputs through scene generation, edit checks, and delivery state", "Plan AI-assisted video ad production with review gates.", "agentic video production workflow", ("ai-marketing-agent-workflow", "video-ad-production")),
    SkillSpec("creative-outbound-message-bridge", "creative outbound message bridge", "Creative / Ads / Assets", "convert creative angles into outbound hooks, proof points, cadence steps, reply routes, and stop rules", "Adapt winning creative angles into outbound sequences.", "creative-to-outbound message bridge", ("ad-creative-generation", "outbound-cadence-automation")),
    SkillSpec("creative-enrichment-personalization-plan", "creative enrichment personalization plan", "Creative / Ads / Assets", "turn enrichment fields into personalization claims, creative variants, confidence checks, and fallback copy", "Use enrichment fields to personalize creative without overreaching.", "creative personalization plan", ("ad-creative-generation", "lead-enrichment-and-research")),
    SkillSpec("synthetic-creative-test-panel", "synthetic creative test panel", "Creative / Ads / Assets", "use synthetic audience scenarios to pressure-test creative angles, reactions, confidence, and validation needs", "Stress-test creative concepts with synthetic audience assumptions.", "synthetic creative test panel", ("synthetic-audience-simulation", "ad-creative-generation", "message-testing")),
    SkillSpec("video-seo-content-reuse-plan", "video SEO content reuse plan", "Creative / Ads / Assets", "convert video assets into search-answer blocks, social cuts, proof moments, and reuse ownership", "Repurpose video production into SEO and social content assets.", "video SEO reuse plan", ("video-ad-production", "seo-content-briefing", "social-content-automation")),
    SkillSpec("chat-creative-conversion-plan", "chat creative conversion plan", "Creative / Ads / Assets", "align ad angles, landing promises, chat questions, qualification rules, and conversion handoff", "Connect creative promises to inbound chat conversion paths.", "chat creative conversion plan", ("ad-creative-generation", "inbound-chat-qualification", "message-testing")),
    SkillSpec("social-content-calendar-system", "social content calendar system", "Content / Creator / Social", "turn narrative pillars, campaign moments, and channel rules into a reusable content calendar", "Plan social content around repeatable campaign mechanics.", "social calendar and posting system", ("social-content-automation",)),
    SkillSpec("content-repurposing-map", "content repurposing map", "Content / Creator / Social", "map one source asset into ads, social posts, emails, landing copy, and sales enablement", "Repurpose long-form or campaign assets across channels.", "content repurposing map", ("social-content-automation", "seo-content-briefing", "ad-creative-generation")),
    SkillSpec("creator-discovery-scorecard", "creator discovery scorecard", "Content / Creator / Social", "score creators by audience fit, trust, content quality, risk, usage rights, and expected lift", "Find and rank creators or influencers for a campaign.", "creator scorecard", ("ugc-creator-workflow", "social-content-automation", "customer-research-synthesis")),
    SkillSpec("influencer-outreach-offer-brief", "influencer outreach offer brief", "Content / Creator / Social", "draft creator outreach, offer, deliverables, approvals, usage rights, and renewal terms", "Brief creator outreach and partnership offers with usage terms.", "creator outreach brief", ("ugc-creator-workflow", "social-content-automation", "outbound-cadence-automation")),
    SkillSpec("ugc-intake-rights-workflow", "UGC intake rights workflow", "Content / Creator / Social", "manage creator asset intake, rights, tagging, approvals, edits, and paid reuse", "Turn UGC into reusable approved assets with rights tracking.", "UGC intake and rights workflow", ("ugc-creator-workflow", "ad-creative-generation")),
    SkillSpec("creator-performance-reuse-readout", "creator performance reuse readout", "Content / Creator / Social", "evaluate creator assets for performance, learning, renewal, and paid reuse decisions", "Decide which creator assets to reuse or renew.", "creator performance readout", ("ugc-creator-workflow", "social-content-automation", "campaign-analytics-qa")),
    SkillSpec("community-ambassador-loop-design", "community ambassador loop design", "Content / Creator / Social", "design member, customer, or local advocate loops that produce referrals, proof, and content", "Build an ambassador or advocacy loop with proof generation.", "ambassador loop plan", ("ugc-creator-workflow", "social-content-automation", "local-storefront-growth")),
    SkillSpec("social-listening-insight-brief", "social listening insight brief", "Content / Creator / Social", "turn reviews, social posts, comments, and communities into message and campaign insights", "Extract marketing insights from social and community signals.", "social listening brief", ("customer-research-synthesis", "social-content-automation")),
    SkillSpec("seo-social-content-brief", "SEO social content brief", "Content / Creator / Social", "blend search questions, social hooks, proof, and distribution into one content brief", "Create content briefs that work for search and social.", "SEO/social content brief", ("seo-content-briefing", "social-content-automation")),
    SkillSpec("voiceover-localization-workflow", "voiceover localization workflow", "Content / Creator / Social", "plan translated or localized voice assets with tone, timing, proof, and review checks", "Localize voiceover assets for marketing use with review checks.", "voiceover localization workflow", ("video-ad-production", "social-content-automation")),
    SkillSpec("event-content-reuse-system", "event content reuse system", "Content / Creator / Social", "turn event, webinar, or field moments into social, email, ads, and sales follow-up assets", "Repurpose event content into campaign assets and follow-up.", "event content reuse system", ("social-content-automation", "lead-list-building", "outbound-cadence-automation")),
    SkillSpec("community-response-playbook", "community response playbook", "Content / Creator / Social", "draft response patterns for comments, questions, objections, praise, and moderation risk", "Create social or community response guidance for repeat questions.", "community response playbook", ("social-content-automation", "brand-governance-review")),
    SkillSpec("icp-segment-trigger-map", "ICP segment trigger map", "Lead Intelligence / Conversion", "define fit, segment, trigger, disqualifier, pain, proof, and channel logic", "Map ideal segments and buying triggers for campaign action.", "ICP trigger map", ("customer-research-synthesis", "lead-list-building")),
    SkillSpec("account-list-sourcing-brief", "account list sourcing brief", "Lead Intelligence / Conversion", "turn segment rules into source selection, list criteria, exclusions, and evidence fields", "Specify how to build a qualified account list.", "account list sourcing brief", ("lead-list-building",)),
    SkillSpec("lead-list-prioritization-scorecard", "lead list prioritization scorecard", "Lead Intelligence / Conversion", "score leads by fit, trigger, intent, evidence strength, urgency, and route", "Prioritize leads before outreach using fit and intent evidence.", "lead scoring table and routing notes", ("lead-list-building", "lead-enrichment-and-research"), "score_leads.py"),
    SkillSpec("account-research-snapshot", "account research snapshot", "Lead Intelligence / Conversion", "summarize account context, role pain, trigger, proof match, objection, and first message angle", "Create concise account research for personalized outbound outreach.", "account research snapshot", ("lead-enrichment-and-research", "customer-research-synthesis")),
    SkillSpec("enrichment-field-contract", "enrichment field contract", "Lead Intelligence / Conversion", "define enrichment fields, source priority, freshness, usage, and fallback behavior", "Design enrichment that changes routing or messaging.", "enrichment field contract", ("lead-enrichment-and-research", "audience-data-sync")),
    SkillSpec("buying-signal-listener-spec", "buying signal listener spec", "Lead Intelligence / Conversion", "specify web, product, social, hiring, funding, content, and CRM signals that trigger action", "Detect buying intent from observable signals and route actions.", "signal listener spec", ("website-visitor-identification", "lead-enrichment-and-research", "audience-data-sync")),
    SkillSpec("website-visitor-to-account-workflow", "website visitor to account workflow", "Lead Intelligence / Conversion", "map anonymous or known visits into account identity, intent, routing, and follow-up", "Turn website visits into account-level actions and follow-up.", "visitor-to-account workflow", ("website-visitor-identification",)),
    SkillSpec("intent-led-outbound-sequence", "intent-led outbound sequence", "Lead Intelligence / Conversion", "write outbound emails tied to a specific trigger, pain, proof, and reply route", "Create outbound sequences from intent signals and proof points.", "intent-led email sequence", ("outbound-cadence-automation", "lead-enrichment-and-research")),
    SkillSpec("linkedin-prospecting-cadence", "LinkedIn prospecting cadence", "Lead Intelligence / Conversion", "create connection, message, follow-up, and stop rules for LinkedIn prospecting", "Build LinkedIn outreach flows for target accounts.", "LinkedIn cadence", ("outbound-cadence-automation",)),
    SkillSpec("multichannel-prospecting-orchestration", "multichannel prospecting orchestration", "Lead Intelligence / Conversion", "coordinate email, LinkedIn, phone, retargeting, chat, and sales owner handoff", "Coordinate prospecting across channels with owner handoff rules.", "multichannel prospecting map", ("outbound-cadence-automation", "marketing-ops-orchestration")),
    SkillSpec("reply-intent-triage-rules", "reply intent triage rules", "Lead Intelligence / Conversion", "classify replies into interest, objection, referral, timing, unsubscribe, or support paths", "Route replies into the right next action.", "reply triage rules", ("inbound-chat-qualification", "outbound-cadence-automation")),
    SkillSpec("inbound-chat-qualification-flow", "inbound chat qualification flow", "Lead Intelligence / Conversion", "design chat questions, qualification logic, handoff moments, and fallback messages", "Qualify inbound chat without damaging handoff quality.", "chat qualification flow", ("inbound-chat-qualification",)),
    SkillSpec("demo-booking-friction-audit", "demo booking friction audit", "Lead Intelligence / Conversion", "inspect the path from ad, page, chat, form, or outreach to booked meeting", "Improve the conversion path into booked meetings.", "booking friction audit", ("inbound-chat-qualification", "website-visitor-identification")),
    SkillSpec("local-business-prospecting-route", "local business prospecting route", "Lead Intelligence / Conversion", "find local accounts or locations, prioritize routes, and prepare direct outreach", "Prioritize local prospects for direct outreach and route planning.", "local prospecting route", ("local-storefront-growth", "lead-list-building")),
    SkillSpec("event-lead-capture-followup", "event lead capture follow-up", "Lead Intelligence / Conversion", "turn event scans, meetings, booth notes, and field signals into segmented follow-up", "Convert event leads into follow-up and sales actions.", "event follow-up plan", ("lead-list-building", "outbound-cadence-automation", "marketing-ops-orchestration")),
    SkillSpec("referral-partner-lead-loop", "referral partner lead loop", "Lead Intelligence / Conversion", "design partner, affiliate, referral, or ambassador lead flow with tracking and ownership", "Create referral or partner lead loops with tracking ownership.", "referral lead loop plan", ("lead-list-building", "outbound-cadence-automation")),
    SkillSpec("crm-handoff-qa", "CRM handoff QA", "Lead Intelligence / Conversion", "check campaign response, enrichment, owner assignment, next step, and reporting fields", "QA the handoff from marketing signal to CRM action.", "CRM handoff QA checklist", ("marketing-ops-orchestration", "audience-data-sync")),
    SkillSpec("sales-marketing-feedback-loop", "sales marketing feedback loop", "Lead Intelligence / Conversion", "convert sales replies, objections, disqualifiers, and wins into marketing list and message updates", "Use sales feedback to improve targeting and messaging.", "sales feedback loop", ("lead-list-building", "customer-research-synthesis", "outbound-cadence-automation")),
    SkillSpec("agentic-list-building-workflow", "agentic list building workflow", "Lead Intelligence / Conversion", "scope an AI workflow for list criteria, evidence lookup, disqualification, routing actions, and review gates", "Design agent-assisted list building with evidence and routing controls.", "agentic list building workflow", ("ai-marketing-agent-workflow", "lead-list-building")),
    SkillSpec("audience-list-sync-readiness", "audience list sync readiness", "Lead Intelligence / Conversion", "align audience segments, list criteria, join keys, consent status, exclusions, destinations, and count checks", "Check whether a lead list is ready for audience activation.", "audience list sync readiness check", ("audience-data-sync", "lead-list-building")),
    SkillSpec("visitor-list-routing-plan", "visitor list routing plan", "Lead Intelligence / Conversion", "connect visit signals, list membership, intent thresholds, confidence, suppression, and follow-up routing", "Route website visitor signals into list and owner actions.", "visitor list routing plan", ("website-visitor-identification", "lead-list-building")),
    SkillSpec("chat-lead-routing-flow", "chat lead routing flow", "Lead Intelligence / Conversion", "turn chat qualification answers into list membership, owner routing, follow-up timing, and suppression-aware actions", "Move chat-qualified visitors into the right list and follow-up path.", "chat lead routing flow", ("inbound-chat-qualification", "lead-list-building")),
    SkillSpec("answer-led-list-hypothesis-panel", "answer-led list hypothesis panel", "Lead Intelligence / Conversion", "use answer proof gaps and synthetic audience checks to refine list hypotheses, disqualifiers, and follow-up routes", "Use answer gaps to sharpen list hypotheses before outreach.", "answer-led list hypothesis panel", ("lead-list-building", "answer-source-remediation", "synthetic-audience-simulation")),
    SkillSpec("synthetic-audience-panel-builder", "synthetic audience panel builder", "Research / Audience Simulation", "define synthetic panel composition, assumptions, prompts, validation checks, and confidence limits", "Build a synthetic audience panel with validation limits.", "synthetic panel spec", ("synthetic-audience-simulation", "customer-research-synthesis")),
    SkillSpec("stakeholder-simulation-scenario-plan", "stakeholder simulation scenario plan", "Research / Audience Simulation", "simulate stakeholder reactions to launches, messages, pricing, policy, or market events", "Plan stakeholder reaction simulations for launch or message decisions.", "simulation scenario plan", ("synthetic-audience-simulation", "message-testing")),
    SkillSpec("survey-instrument-builder", "survey instrument builder", "Research / Audience Simulation", "write survey questions, screeners, branching, scales, and analysis fields around a decision", "Design surveys that answer a marketing decision.", "survey instrument and analysis plan", ("customer-research-synthesis", "message-testing")),
    SkillSpec("interview-guide-builder", "interview guide builder", "Research / Audience Simulation", "create interview guides tied to buyer questions, objections, alternatives, and decision criteria", "Create customer, buyer, or stakeholder interview guides.", "interview guide", ("customer-research-synthesis",)),
    SkillSpec("interview-synthesis-matrix", "interview synthesis matrix", "Research / Audience Simulation", "synthesize interviews into themes, quotes, objections, segments, confidence, and implications", "Turn interviews into a decision-ready matrix with confidence notes.", "interview synthesis matrix", ("customer-research-synthesis",)),
    SkillSpec("review-forum-mining-brief", "review forum mining brief", "Research / Audience Simulation", "mine reviews, forums, communities, calls, and comments for pain, language, triggers, and objections", "Extract customer language from public or owned feedback.", "review mining brief", ("customer-research-synthesis", "message-testing")),
    SkillSpec("message-test-scorecard", "message test scorecard", "Research / Audience Simulation", "score messages by clarity, relevance, proof, differentiation, risk, and next-action strength", "Evaluate competing messages before launch with explicit scoring.", "message test scorecard", ("message-testing", "customer-research-synthesis")),
    SkillSpec("positioning-claim-map", "positioning claim map", "Research / Audience Simulation", "map competitors, alternatives, claims, proof, objections, and whitespace", "Clarify positioning against alternatives using claims and proof.", "positioning claim map", ("customer-research-synthesis",)),
    SkillSpec("market-segmentation-memo", "market segmentation memo", "Research / Audience Simulation", "break a market into segments, jobs, channels, triggers, and acquisition implications", "Segment a market for marketing decisions and channel choices.", "segmentation memo", ("customer-research-synthesis", "lead-list-building")),
    SkillSpec("customer-journey-evidence-map", "customer journey evidence map", "Research / Audience Simulation", "map stages, questions, objections, proof needs, channels, and conversion gaps", "Map the buyer journey from evidence and conversion gaps.", "journey evidence map", ("customer-research-synthesis", "inbound-chat-qualification")),
    SkillSpec("audience-intelligence-brief", "audience intelligence brief", "Research / Audience Simulation", "turn audience data into motivations, segments, channels, triggers, and risks", "Convert audience data into campaign decisions and channel choices.", "audience intelligence brief", ("customer-research-synthesis", "audience-data-sync")),
    SkillSpec("research-decision-memo", "research decision memo", "Research / Audience Simulation", "convert research findings into a recommendation, confidence level, rejected options, and next evidence", "Turn research into a decision with confidence and tradeoffs.", "research decision memo", ("customer-research-synthesis",)),
    SkillSpec("synthetic-enrichment-panel", "synthetic enrichment panel", "Research / Audience Simulation", "test enrichment assumptions, personalization cues, confidence limits, and validation needs with synthetic panels", "Pressure-test enrichment assumptions before personalization reaches outreach or creative.", "synthetic enrichment panel", ("synthetic-audience-simulation", "lead-enrichment-and-research", "customer-research-synthesis")),
    SkillSpec("local-market-research-brief", "local market research brief", "Research / Audience Simulation", "turn local reviews, storefront signals, route context, and customer language into market insight", "Synthesize local market signals into campaign and route decisions.", "local market research brief", ("customer-research-synthesis", "local-storefront-growth", "lead-list-building")),
    SkillSpec("campaign-tracking-plan", "campaign tracking plan", "Lifecycle / Ops / Analytics", "define UTMs, events, properties, destinations, QA checks, and reporting owner", "Plan campaign tracking before launch with QA ownership.", "campaign tracking plan", ("campaign-analytics-qa", "marketing-ops-orchestration")),
    SkillSpec("attribution-diagnostic", "attribution diagnostic", "Lifecycle / Ops / Analytics", "find attribution gaps across source capture, conversion events, identity, routing, and reporting", "Diagnose attribution before making performance decisions from campaign data.", "attribution diagnostic", ("campaign-analytics-qa",)),
    SkillSpec("audience-sync-contract", "audience sync contract", "Lifecycle / Ops / Analytics", "define audience fields, refresh cadence, destinations, exclusions, and owner checks", "Move audiences between systems reliably with field contracts.", "audience sync contract", ("audience-data-sync",)),
    SkillSpec("warehouse-audience-activation-plan", "warehouse audience activation plan", "Lifecycle / Ops / Analytics", "turn warehouse tables into campaign audiences with joins, QA, consent, and refresh rules", "Activate warehouse data for campaigns with QA rules.", "warehouse activation plan", ("audience-data-sync",)),
    SkillSpec("lifecycle-segmentation-map", "lifecycle segmentation map", "Lifecycle / Ops / Analytics", "define lifecycle states, transitions, triggers, suppressions, and owner actions", "Create lifecycle audience segmentation with transitions and owner actions.", "lifecycle segmentation map", ("audience-data-sync", "marketing-ops-orchestration")),
    SkillSpec("whatsapp-sms-conversation-flow", "WhatsApp SMS conversation flow", "Lifecycle / Ops / Analytics", "design compliant conversational flows for SMS, WhatsApp, or messaging channels", "Build messaging campaign flows with compliance and handoff checks.", "messaging conversation flow", ("marketing-ops-orchestration", "outbound-cadence-automation", "inbound-chat-qualification")),
    SkillSpec("email-template-system", "email template system", "Lifecycle / Ops / Analytics", "create reusable templates, dynamic fields, QA states, and version rules", "Create reusable campaign email templates with QA states.", "email template system", ("marketing-ops-orchestration", "outbound-cadence-automation")),
    SkillSpec("campaign-preflight-qa-checklist", "campaign preflight QA checklist", "Lifecycle / Ops / Analytics", "check assets, audiences, approvals, tracking, consent, owner routing, and rollback before launch", "QA campaigns before they go live with rollback coverage.", "campaign preflight checklist", ("campaign-analytics-qa", "marketing-ops-orchestration"), "build_campaign_qa.py"),
    SkillSpec("experiment-readout", "experiment readout", "Lifecycle / Ops / Analytics", "summarize experiment result, confidence, tradeoffs, decision, and next test", "Turn campaign or message tests into decisions.", "experiment readout", ("campaign-analytics-qa", "message-testing")),
    SkillSpec("retention-reactivation-loop", "retention reactivation loop", "Lifecycle / Ops / Analytics", "design lifecycle campaigns for retention, winback, repeat purchase, or expansion", "Build retention or reactivation loops with lifecycle triggers.", "retention or reactivation loop", ("audience-data-sync", "outbound-cadence-automation", "marketing-ops-orchestration")),
    SkillSpec("marketing-dashboard-spec", "marketing dashboard spec", "Lifecycle / Ops / Analytics", "specify dashboard metrics, dimensions, data checks, thresholds, and operating decisions", "Design dashboards that drive marketing operating decisions.", "dashboard spec", ("campaign-analytics-qa", "marketing-ops-orchestration")),
    SkillSpec("consent-suppression-rollback-plan", "consent suppression rollback plan", "Lifecycle / Ops / Analytics", "define consent checks, suppression rules, privacy review, rollback path, and incident owner", "Protect campaign operations with consent and rollback rules.", "consent and rollback plan", ("marketing-ops-orchestration", "brand-governance-review")),
    SkillSpec("marketing-agent-workflow-spec", "marketing agent workflow spec", "Marketing Agents / Governance", "scope a bounded marketing agent by job, inputs, tools, review gates, and final artifact", "Specify an AI agent workflow for a bounded marketing job.", "agent workflow spec", ("ai-marketing-agent-workflow", "marketing-ops-orchestration")),
    SkillSpec("agentic-seo-briefing-workflow", "agentic SEO briefing workflow", "Marketing Agents / Governance", "scope an AI workflow for target queries, proof lookup, brief drafting, schema actions, review gates, and publish handoff", "Design agent-assisted SEO and answer-ready content briefing.", "agentic SEO briefing workflow", ("ai-marketing-agent-workflow", "seo-content-briefing")),
    SkillSpec("tool-orchestration-map", "tool orchestration map", "Marketing Agents / Governance", "map model calls, tools, data access, human handoffs, and fallback paths", "Plan tool use inside marketing workflows with fallback paths.", "tool orchestration map", ("ai-marketing-agent-workflow",)),
    SkillSpec("human-approval-ladder", "human approval ladder", "Marketing Agents / Governance", "define what AI can draft, decide, route, or escalate based on risk", "Set approval rules for AI-assisted marketing by risk level.", "approval ladder", ("ai-marketing-agent-workflow", "brand-governance-review")),
    SkillSpec("marketing-output-eval-harness", "marketing output eval harness", "Marketing Agents / Governance", "create evals for factuality, claim support, brand fit, usefulness, and operational reliability", "Evaluate AI-generated marketing output with measurable criteria.", "marketing eval harness", ("ai-marketing-agent-workflow", "campaign-analytics-qa")),
    SkillSpec("brand-voice-memory", "brand voice memory", "Marketing Agents / Governance", "distill approved voice, claims, examples, banned patterns, and review notes into reusable memory", "Build reusable brand voice guidance for AI workflows.", "brand voice memory", ("brand-governance-review", "social-content-automation")),
    SkillSpec("prompt-library-maintenance", "prompt library maintenance", "Marketing Agents / Governance", "maintain prompt patterns, examples, failures, variants, owners, and version notes", "Maintain prompt libraries for marketing workflows with version notes.", "prompt library maintenance plan", ("ai-marketing-agent-workflow",)),
    SkillSpec("claims-hallucination-review", "claims hallucination review", "Marketing Agents / Governance", "review AI-generated marketing for unsupported claims, factual drift, missing caveats, and legal risk", "Review AI marketing for unsupported claims and hallucinations.", "claims review checklist", ("brand-governance-review", "answer-source-remediation", "ai-marketing-agent-workflow")),
    SkillSpec("ai-workflow-telemetry-plan", "AI workflow telemetry plan", "Marketing Agents / Governance", "define quality, throughput, review, acceptance, rework, and business-impact telemetry", "Measure AI workflow performance beyond output volume.", "AI workflow telemetry plan", ("ai-marketing-agent-workflow", "campaign-analytics-qa")),
    SkillSpec("internal-knowledge-activation", "internal knowledge activation", "Marketing Agents / Governance", "turn approved docs, calls, data, and research into safe inputs for AI-assisted marketing", "Activate internal knowledge for marketing AI workflows.", "knowledge activation plan", ("ai-marketing-agent-workflow", "customer-research-synthesis")),
    SkillSpec("automation-risk-register", "automation risk register", "Marketing Agents / Governance", "identify automation risks, mitigations, owners, monitoring, escalation, and rollback", "Manage risk in marketing automation and AI workflows.", "automation risk register", ("ai-marketing-agent-workflow", "brand-governance-review", "marketing-ops-orchestration")),
]


SKILL_SPECIFIC_FIELDS = {
    "agent-discovery-question-map": ("buyer question", "persona", "intent stage", "answer surface", "prompt wording", "current answer", "cited proof", "action priority"),
    "ai-answer-visibility-scorecard": ("prompt", "surface", "mention status", "rank", "answer accuracy", "citation quality", "next action", "risk"),
    "prompt-rank-monitor": ("prompt", "surface", "run date", "mention status", "rank", "cited proof", "competitor rank", "trend note"),
    "share-of-answer-benchmark": ("prompt cluster", "entity mention", "competitor alternative", "answer framing", "rank", "proof gap", "opportunity", "benchmark date"),
    "citation-source-gap-map": ("answer claim", "cited asset", "missing proof", "stale proof", "page or listing gap", "owner", "fix priority"),
    "citable-proof-asset-kit": ("claim", "proof asset", "format", "audience question", "citation target", "publishing owner", "review state", "refresh date"),
    "answer-ready-content-brief": ("target question", "intent", "answer block", "proof", "schema need", "internal link", "content owner", "publish check"),
    "page-schema-indexability-audit": ("page", "crawl path", "structured data", "proof exposure", "indexability issue", "fix owner", "test method", "priority"),
    "ai-shopping-feed-optimizer": ("product", "feed field", "PDP proof", "image signal", "FAQ gap", "checkout signal", "answer inclusion risk", "fix"),
    "agent-action-backlog": ("visibility gap", "surface", "smallest action", "asset or system touched", "owner", "effort", "impact", "cycle"),
    "ai-referral-roi-readout": ("referral surface", "traffic type", "session path", "assisted event", "revenue caveat", "bot signal", "dashboard field"),
    "generative-search-weekly-ops-report": ("prompt movement", "citation gap", "shipped fix", "traffic signal", "risk item", "owner", "next week action"),
    "answer-claim-risk-review": ("answer text", "unsupported claim", "stale phrase", "missing caveat", "proof needed", "correction path", "risk owner"),
    "agent-discovery-content-refresh-plan": ("stale page", "target question", "missing proof", "refresh angle", "schema or index need", "CMS owner", "expected answer change"),
    "agentic-answer-ops-workflow": ("monitored prompt", "agent job", "allowed action", "evidence lookup", "remediation task", "review gate", "telemetry", "fallback"),
    "ai-answer-brand-risk-map": ("priority prompt", "observed answer", "brand risk", "claim status", "proof gap", "correction owner", "severity", "monitoring cadence"),
    "seo-brand-proof-governance": ("target query", "claim", "approved proof", "schema need", "page section", "reviewer", "risk state", "publish decision"),
    "search-creative-message-bridge": ("answer insight", "buyer belief", "creative angle", "proof to reuse", "channel", "CTA", "message risk", "next test"),
    "offer-angle-mining": ("audience segment", "pain", "desire", "objection", "competitor angle", "proof point", "offer angle", "test rationale"),
    "creative-brief-from-research": ("insight", "audience", "claim", "proof", "objection", "format", "CTA", "production constraint", "reviewer"),
    "ad-variant-matrix-builder": ("hook", "angle", "proof", "format", "CTA", "variable changed", "hypothesis", "review state"),
    "visual-asset-prompt-brief": ("asset goal", "scene", "product detail", "style constraint", "prompt", "negative constraint", "channel", "QA note"),
    "product-image-qa-brief": ("product attribute", "shot type", "context", "fidelity risk", "prompt constraint", "unacceptable artifact", "approval state"),
    "catalog-ad-feed-plan": ("product field", "audience segment", "creative rule", "image rule", "feed mapping", "exclusion", "destination", "QA check"),
    "video-ad-storyboard": ("scene", "hook", "product moment", "proof line", "objection", "visual cue", "caption", "CTA", "edit note"),
    "short-form-hook-bank": ("platform", "hook type", "opening line", "proof cue", "retention beat", "CTA", "test note"),
    "ugc-ad-script-pack": ("creator persona", "hook", "story beat", "product use", "proof moment", "disclosure", "usage limit", "CTA"),
    "landing-page-message-match": ("ad angle", "page headline", "proof block", "objection block", "CTA", "tracking parameter", "conversion path"),
    "competitor-ad-teardown": ("competitor angle", "format", "claim", "proof", "offer", "audience belief", "gap", "testable response"),
    "creative-fatigue-refresh-plan": ("fatigued asset", "symptom", "retained learning", "variable to refresh", "new angle", "audience", "relaunch check"),
    "paid-launch-checklist": ("asset", "audience", "budget", "conversion event", "tracking", "approvals", "fallback", "rollback trigger"),
    "creative-performance-readout": ("asset", "audience", "spend context", "tracking confidence", "creative signal", "learning", "next test", "stop rule"),
    "brand-compliance-creative-review": ("asset", "claim", "proof", "voice fit", "platform risk", "required edit", "reviewer", "approval state"),
    "multilingual-creative-localization": ("locale", "original intent", "claim", "proof", "idiom risk", "voice note", "reviewer", "localized CTA"),
    "podcast-audio-ad-read-guide": ("host line", "timing", "pronunciation", "claim", "proof", "CTA", "read style", "compliance note"),
    "multimodal-asset-assembly-brief": ("format", "image", "video", "voice", "copy", "caption", "landing proof", "review state", "assembly owner"),
    "creative-lead-capture-loop": ("creative angle", "audience", "lead signal", "capture field", "list rule", "follow-up route", "proof", "measurement event"),
    "creative-agent-production-workflow": ("agent job", "input brief", "variant rule", "generation step", "review gate", "tool boundary", "output handoff"),
    "agentic-video-production-workflow": ("video job", "script input", "scene generation", "voice or caption rule", "edit gate", "brand review", "delivery state"),
    "creative-outbound-message-bridge": ("creative angle", "trigger", "lead segment", "email hook", "proof point", "cadence step", "reply route", "stop rule"),
    "creative-enrichment-personalization-plan": ("enrichment field", "audience cue", "personalization claim", "creative variant", "confidence", "fallback copy", "review flag"),
    "synthetic-creative-test-panel": ("audience assumption", "scenario", "creative angle", "simulated reaction", "validation need", "confidence", "next real test"),
    "video-seo-content-reuse-plan": ("video asset", "transcript moment", "target query", "answer block", "social cut", "proof", "reuse owner", "publish check"),
    "chat-creative-conversion-plan": ("ad angle", "landing promise", "chat question", "qualification rule", "message match", "handoff path", "conversion event", "fix"),
    "social-content-calendar-system": ("pillar", "channel", "format", "hook", "proof", "asset", "publish date", "owner", "response rule"),
    "content-repurposing-map": ("original asset", "extractable claim", "channel adaptation", "format", "CTA", "proof preserved", "owner", "reuse rights"),
    "creator-discovery-scorecard": ("creator", "audience fit", "trust signal", "content quality", "risk", "usage rights", "expected lift", "decision"),
    "influencer-outreach-offer-brief": ("creator segment", "offer", "deliverables", "usage rights", "approval path", "outreach hook", "renewal option"),
    "ugc-intake-rights-workflow": ("asset", "creator", "rights window", "edit permission", "tag", "approval state", "reuse channel", "renewal note"),
    "creator-performance-reuse-readout": ("creator asset", "spend or organic context", "performance signal", "learning", "reuse decision", "renewal decision", "rights check"),
    "community-ambassador-loop-design": ("member segment", "referral trigger", "proof asset", "reward", "content loop", "owner", "tracking", "renewal"),
    "social-listening-insight-brief": ("channel", "post or comment", "pain", "language", "objection", "segment", "implication", "campaign action"),
    "seo-social-content-brief": ("search question", "social hook", "proof", "content angle", "channel cut", "schema need", "distribution step"),
    "voiceover-localization-workflow": ("source script", "locale", "timing", "tone", "pronunciation", "proof", "reviewer", "approval state"),
    "event-content-reuse-system": ("event moment", "captured asset", "lead signal", "follow-up segment", "social cut", "email angle", "owner"),
    "community-response-playbook": ("question type", "response pattern", "proof", "escalation trigger", "moderation risk", "owner", "update rule"),
    "icp-segment-trigger-map": ("segment", "fit rule", "trigger", "disqualifier", "pain", "proof", "channel", "owner"),
    "account-list-sourcing-brief": ("segment rule", "list source", "inclusion criterion", "exclusion", "evidence field", "dedupe key", "owner route"),
    "lead-list-prioritization-scorecard": ("record", "fit score", "intent score", "evidence strength", "urgency", "route", "next action"),
    "account-research-snapshot": ("account context", "role pain", "trigger", "proof match", "objection", "first message angle", "confidence"),
    "enrichment-field-contract": ("field", "source priority", "freshness", "confidence", "usage rule", "fallback", "owner", "QA check"),
    "buying-signal-listener-spec": ("signal type", "event", "threshold", "source", "freshness", "route", "action", "false-positive check"),
    "website-visitor-to-account-workflow": ("visit path", "matched account", "intent score", "confidence", "owner", "follow-up", "fallback"),
    "intent-led-outbound-sequence": ("trigger", "pain", "proof", "opening line", "step", "wait rule", "reply route", "stop rule"),
    "linkedin-prospecting-cadence": ("connection reason", "first note", "follow-up step", "proof", "wait", "stop rule", "handoff"),
    "multichannel-prospecting-orchestration": ("channel", "step", "trigger", "owner", "handoff", "suppression", "fallback", "reporting field"),
    "reply-intent-triage-rules": ("reply text", "intent class", "urgency", "objection", "route", "owner", "response SLA", "stop flag"),
    "inbound-chat-qualification-flow": ("question", "branch", "qualification rule", "score", "route", "fallback", "booking path", "handoff note"),
    "demo-booking-friction-audit": ("entry point", "friction point", "required field", "routing delay", "handoff gap", "test step", "fix"),
    "local-business-prospecting-route": ("location", "category", "fit", "local proof", "route order", "contact path", "owner", "follow-up"),
    "event-lead-capture-followup": ("event note", "lead segment", "booth context", "meeting signal", "follow-up message", "owner", "CRM field"),
    "referral-partner-lead-loop": ("partner type", "referral trigger", "lead handoff", "tracking field", "reward or terms", "owner", "loop metric"),
    "crm-handoff-qa": ("record", "owner", "route", "next step", "enrichment field", "reporting field", "missing data", "fix"),
    "sales-marketing-feedback-loop": ("reply or objection", "segment", "message gap", "list update", "proof need", "owner", "next experiment"),
    "agentic-list-building-workflow": ("agent job", "target segment", "list criteria", "evidence lookup", "disqualifier", "routing action", "review gate", "audit field"),
    "audience-list-sync-readiness": ("audience segment", "list criterion", "join key", "consent status", "exclusion", "destination", "count check", "owner"),
    "visitor-list-routing-plan": ("visit signal", "matched account", "list membership", "intent threshold", "route", "confidence", "follow-up", "suppression"),
    "chat-lead-routing-flow": ("chat answer", "qualification score", "list membership", "fit rule", "owner route", "follow-up timing", "suppression", "handoff note"),
    "answer-led-list-hypothesis-panel": ("answer gap", "proof gap", "list hypothesis", "target segment", "synthetic check", "disqualifier", "confidence", "follow-up route"),
    "synthetic-audience-panel-builder": ("persona", "assumption", "scenario", "prompt", "response", "confidence", "validation plan", "blocked use"),
    "stakeholder-simulation-scenario-plan": ("stakeholder type", "scenario", "expected reaction", "objection", "risk", "decision", "validation step"),
    "survey-instrument-builder": ("decision", "respondent criteria", "screener", "question", "scale", "branch", "analysis field", "bias check"),
    "interview-guide-builder": ("buyer question", "objection", "alternative", "decision criterion", "prompt", "probe", "segment", "evidence label"),
    "interview-synthesis-matrix": ("theme", "quote", "segment", "objection", "alternative", "confidence", "implication", "next evidence"),
    "review-forum-mining-brief": ("review or comment", "evidence type", "pain", "language", "trigger", "objection", "segment", "message implication"),
    "message-test-scorecard": ("message", "audience", "clarity", "relevance", "proof", "differentiation", "risk", "next action"),
    "positioning-claim-map": ("alternative", "claim", "proof", "objection", "whitespace", "segment", "risk", "decision"),
    "market-segmentation-memo": ("segment", "job", "trigger", "channel", "pain", "proof need", "acquisition implication", "priority"),
    "customer-journey-evidence-map": ("stage", "question", "objection", "proof need", "channel", "conversion gap", "owner", "next evidence"),
    "audience-intelligence-brief": ("segment", "motivation", "channel", "trigger", "risk", "data signal", "message implication", "next test"),
    "research-decision-memo": ("decision", "evidence", "finding", "confidence", "option rejected", "recommendation", "next evidence", "owner"),
    "synthetic-enrichment-panel": ("enrichment assumption", "persona", "scenario", "personalization cue", "simulated reaction", "confidence", "validation need", "blocked use"),
    "local-market-research-brief": ("location", "review signal", "storefront gap", "local language", "route context", "segment", "offer implication", "next action"),
    "campaign-tracking-plan": ("channel", "UTM", "event", "property", "conversion", "destination", "owner", "QA step"),
    "attribution-diagnostic": ("touchpoint", "source capture", "identity link", "conversion event", "attribution rule", "gap", "fix owner"),
    "audience-sync-contract": ("audience", "field", "join key", "refresh cadence", "destination", "exclusion", "owner", "check"),
    "warehouse-audience-activation-plan": ("table", "join key", "segment rule", "consent", "exclusion", "destination", "count check", "refresh"),
    "lifecycle-segmentation-map": ("state", "transition", "trigger", "suppression", "owner action", "message", "metric", "rollback"),
    "whatsapp-sms-conversation-flow": ("channel", "consent state", "message step", "branch", "quiet-hour rule", "handoff", "fallback", "opt-out"),
    "email-template-system": ("template", "dynamic field", "segment", "proof block", "QA state", "version", "owner", "fallback"),
    "campaign-preflight-qa-checklist": ("asset", "audience", "tracking", "approval", "consent", "owner route", "fallback", "rollback"),
    "experiment-readout": ("hypothesis", "variant", "result", "confidence", "tradeoff", "decision", "next test", "metric caveat"),
    "retention-reactivation-loop": ("lifecycle state", "trigger", "message", "suppression", "channel", "owner", "reactivation path", "metric"),
    "marketing-dashboard-spec": ("metric", "dimension", "threshold", "data check", "owner", "decision", "cadence", "caveat"),
    "consent-suppression-rollback-plan": ("consent rule", "suppression list", "risky action", "rollback trigger", "incident owner", "test", "approval"),
    "marketing-agent-workflow-spec": ("job", "input", "tool", "allowed action", "review gate", "artifact", "fallback", "telemetry"),
    "agentic-seo-briefing-workflow": ("agent job", "target query", "brief input", "proof lookup", "schema action", "review gate", "publish handoff", "telemetry"),
    "tool-orchestration-map": ("model call", "tool", "input", "output", "owner", "failure mode", "fallback", "handoff"),
    "human-approval-ladder": ("risk level", "action right", "review owner", "escalation trigger", "blocked action", "approval SLA", "evidence needed"),
    "marketing-output-eval-harness": ("criterion", "test case", "expected behavior", "failure mode", "sample output", "score", "threshold", "owner"),
    "brand-voice-memory": ("approved phrase", "banned pattern", "claim", "proof", "example", "reviewer", "update rule", "conflict note"),
    "prompt-library-maintenance": ("prompt pattern", "example", "variant", "failure", "owner", "version", "eval note", "retirement rule"),
    "claims-hallucination-review": ("generated claim", "evidence status", "drift risk", "caveat", "correction", "reviewer", "blocked use"),
    "ai-workflow-telemetry-plan": ("workflow step", "quality metric", "acceptance signal", "rework reason", "throughput", "business impact", "review cadence"),
    "internal-knowledge-activation": ("approved doc", "insight", "access boundary", "allowed use", "claim extraction", "owner", "freshness", "caveat"),
    "automation-risk-register": ("risk", "trigger", "affected workflow", "mitigation", "owner", "monitor", "escalation", "rollback"),
}


HELPER_SCRIPTS = {
    "prompt-rank-monitor": {
        "filename": "build_prompt_rank_table.py",
        "description": "Normalize prompt-rank observations from CSV into a Markdown table.",
        "content": r'''#!/usr/bin/env python3
"""Build a prompt-rank table from answer observations."""

from __future__ import annotations

import argparse
import csv
import sys


FIELDS = ["prompt", "engine", "mentioned", "rank", "citations", "note"]


def clean(value: str | None) -> str:
    return (value or "").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Markdown prompt-rank table from CSV.")
    parser.add_argument("csv_path", help="CSV with prompt, engine, mentioned, rank, citations, note")
    args = parser.parse_args()

    with open(args.csv_path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    missing = [field for field in FIELDS if rows and field not in rows[0]]
    if missing:
        raise SystemExit(f"missing columns: {', '.join(missing)}")

    print("| Prompt | Engine | Mentioned | Rank | Citations | Note |")
    print("| --- | --- | --- | ---: | --- | --- |")
    for row in rows:
        values = [clean(row.get(field)).replace("|", "/") for field in FIELDS]
        values[3] = values[3] or "0"
        print("| " + " | ".join(values) + " |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
''',
        "test_filename": "test_build_prompt_rank_table.py",
        "test_content": r'''from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_prompt_rank_table.py"


class PromptRankTableTest(unittest.TestCase):
    def test_builds_markdown_table(self) -> None:
        with tempfile.NamedTemporaryFile("w", newline="", suffix=".csv") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["prompt", "engine", "mentioned", "rank", "citations", "note"],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "prompt": "best tools",
                    "engine": "answer-engine",
                    "mentioned": "yes",
                    "rank": "2",
                    "citations": "2",
                    "note": "Alpha | Beta",
                }
            )
            handle.flush()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), handle.name],
                text=True,
                capture_output=True,
                check=True,
            )
        self.assertIn("| best tools | answer-engine | yes | 2 | 2 | Alpha / Beta |", result.stdout)


if __name__ == "__main__":
    unittest.main()
''',
    },
    "ad-variant-matrix-builder": {
        "filename": "build_variant_matrix.py",
        "description": "Generate a controlled creative variant CSV from simple option lists.",
        "content": r'''#!/usr/bin/env python3
"""Build a creative variant matrix."""

from __future__ import annotations

import argparse
import csv
import itertools
import sys


def split_options(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate creative variants.")
    parser.add_argument("--hooks", required=True, help="comma-separated hooks")
    parser.add_argument("--proof", required=True, help="comma-separated proof points")
    parser.add_argument("--formats", required=True, help="comma-separated formats")
    parser.add_argument("--ctas", required=True, help="comma-separated CTAs")
    parser.add_argument("--limit", type=int, default=60, help="maximum rows")
    args = parser.parse_args()

    rows = itertools.product(
        split_options(args.hooks),
        split_options(args.proof),
        split_options(args.formats),
        split_options(args.ctas),
    )
    writer = csv.writer(sys.stdout)
    writer.writerow(["variant_id", "hook", "proof", "format", "cta", "hypothesis"])
    for index, (hook, proof, fmt, cta) in enumerate(rows, 1):
        if index > args.limit:
            break
        writer.writerow([f"variant-{index:03d}", hook, proof, fmt, cta, f"{hook} plus {proof} should improve {cta}"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
''',
        "test_filename": "test_build_variant_matrix.py",
        "test_content": r'''from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_variant_matrix.py"


class VariantMatrixTest(unittest.TestCase):
    def test_limits_variant_rows(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--hooks",
                "speed,proof",
                "--proof",
                "case study",
                "--formats",
                "static,video",
                "--ctas",
                "book demo",
                "--limit",
                "3",
            ],
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("variant_id,hook,proof,format,cta,hypothesis", result.stdout)
        self.assertIn("variant-003", result.stdout)
        self.assertNotIn("variant-004", result.stdout)


if __name__ == "__main__":
    unittest.main()
''',
    },
    "lead-list-prioritization-scorecard": {
        "filename": "score_leads.py",
        "description": "Score lead records from CSV using fit, intent, evidence, and urgency fields.",
        "content": r'''#!/usr/bin/env python3
"""Score lead records deterministically."""

from __future__ import annotations

import argparse
import csv
import sys


SCORE_FIELDS = ["fit", "intent", "evidence", "urgency"]


def to_int(value: str | None) -> int:
    try:
        return max(0, min(5, int((value or "0").strip())))
    except ValueError:
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Score lead records from CSV.")
    parser.add_argument("csv_path", help="CSV with account, fit, intent, evidence, urgency, route")
    args = parser.parse_args()

    with open(args.csv_path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    fieldnames = list(rows[0].keys()) if rows else ["account", *SCORE_FIELDS, "route"]
    output_fields = [*fieldnames, "priority_score", "priority_tier"]
    writer = csv.DictWriter(sys.stdout, fieldnames=output_fields)
    writer.writeheader()
    for row in rows:
        score = sum(to_int(row.get(field)) for field in SCORE_FIELDS)
        row["priority_score"] = str(score)
        row["priority_tier"] = "high" if score >= 16 else "medium" if score >= 10 else "low"
        writer.writerow(row)
    return 0


if __name__ == "__main__":
    sys.exit(main())
''',
        "test_filename": "test_score_leads.py",
        "test_content": r'''from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "score_leads.py"


class ScoreLeadsTest(unittest.TestCase):
    def test_scores_priority_tiers(self) -> None:
        with tempfile.NamedTemporaryFile("w", newline="", suffix=".csv") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["account", "fit", "intent", "evidence", "urgency", "route"],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "account": "A",
                    "fit": "5",
                    "intent": "5",
                    "evidence": "4",
                    "urgency": "4",
                    "route": "sales",
                }
            )
            writer.writerow(
                {
                    "account": "B",
                    "fit": "1",
                    "intent": "2",
                    "evidence": "1",
                    "urgency": "0",
                    "route": "nurture",
                }
            )
            handle.flush()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), handle.name],
                text=True,
                capture_output=True,
                check=True,
            )
        self.assertIn("A,5,5,4,4,sales,18,high", result.stdout)
        self.assertIn("B,1,2,1,0,nurture,4,low", result.stdout)


if __name__ == "__main__":
    unittest.main()
''',
    },
    "campaign-preflight-qa-checklist": {
        "filename": "build_campaign_qa.py",
        "description": "Generate a campaign preflight checklist from selected channels.",
        "content": r'''#!/usr/bin/env python3
"""Build a campaign preflight QA checklist."""

from __future__ import annotations

import argparse
import sys


BASE_CHECKS = [
    "Audience/exclusions verified",
    "Tracking parameters/events tested",
    "Claim, brand, channel approvals complete",
    "Owner, route, fallback defined",
    "Suppression, consent, rollback confirmed",
]

CHANNEL_CHECKS = {
    "email": ["Template variables render", "Reply route plus unsubscribe work"],
    "paid": ["Budget, bid, conversion event match plan", "Landing page message match verified"],
    "sms": ["Consent status plus quiet hours checked", "Short links plus replies tested"],
    "chat": ["Qualification questions plus human handoff tested", "Fallback response reviewed"],
    "social": ["Post format, tags, approval state checked", "Comment response owner assigned"],
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown campaign QA checklist.")
    parser.add_argument("--channels", required=True, help="comma-separated channels")
    args = parser.parse_args()

    channels = [item.strip().lower() for item in args.channels.split(",") if item.strip()]
    print("# Campaign Preflight QA")
    print("")
    for check in BASE_CHECKS:
        print(f"- [ ] {check}")
    for channel in channels:
        for check in CHANNEL_CHECKS.get(channel, []):
            print(f"- [ ] {channel}: {check}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
''',
        "test_filename": "test_build_campaign_qa.py",
        "test_content": r'''from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_campaign_qa.py"


class CampaignQaTest(unittest.TestCase):
    def test_builds_channel_checks(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--channels", "email,paid"],
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("# Campaign Preflight QA", result.stdout)
        self.assertIn("- [ ] email: Template variables render", result.stdout)
        self.assertIn("- [ ] paid: Landing page message match verified", result.stdout)


if __name__ == "__main__":
    unittest.main()
''',
    },
}


def wrap_lines(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


def table_cell(value: str) -> str:
    return value.replace("|", "/")


def surface_configs(skill: SkillSpec) -> list[tuple[str, dict]]:
    missing = [surface for surface in skill.surfaces if surface not in SURFACE_CONFIG]
    if missing:
        raise ValueError(f"missing surface config for {skill.name}: {', '.join(missing)}")
    return [(surface, SURFACE_CONFIG[surface]) for surface in skill.surfaces]


def surface_labels(skill: SkillSpec) -> str:
    return ", ".join(config["label"] for _, config in surface_configs(skill))


def surface_items(skill: SkillSpec, key: str) -> list[str]:
    items: list[str] = []
    for _, config in surface_configs(skill):
        for item in config[key]:
            items.append(f"{config['label']}: {item}")
    return unique(items)


def surface_mechanics_table(skill: SkillSpec) -> str:
    rows = ["| Surface | Inspect | Decision It Changes |", "| --- | --- | --- |"]
    for surface, config in surface_configs(skill):
        rows.append(
            "| "
            + " | ".join(
                [
                    f"`{surface}`",
                    table_cell(config["inspect"]),
                    table_cell("; ".join(config["decisions"])),
                ]
            )
            + " |"
        )
    return "\n".join(rows)


def surface_artifact_fields(skill: SkillSpec) -> list[str]:
    return [
        f"{config['label']}: {', '.join(config['artifact_fields'])}"
        for _, config in surface_configs(skill)
    ]


def skill_specific_work_product(skill: SkillSpec) -> list[str]:
    core_fields = SKILL_SPECIFIC_FIELDS.get(skill.name)
    if not core_fields:
        raise ValueError(f"missing skill-specific fields for {skill.name}")
    return [
        f"Final artifact: {skill.output}.",
        f"Organizing mechanic: {skill.mechanic}.",
        f"Core fields or sections: {', '.join(core_fields)}.",
        "Keep the artifact narrow enough that the owner can execute or review the next action today.",
    ]


def required_inputs(skill: SkillSpec) -> list[str]:
    config = CATEGORY_CONFIG[skill.category]
    return unique(
        [
            *config["inputs"],
            *surface_items(skill, "inputs"),
            f"Specific constraints, examples, and existing assets for {skill.display_name}",
        ]
    )


def decision_rules(skill: SkillSpec) -> list[str]:
    config = CATEGORY_CONFIG[skill.category]
    return unique(
        [
            *config["rules"],
            *surface_items(skill, "decisions"),
            "If the user asks for strategy only, still return the smallest artifact this mechanic can produce.",
            "If launch risk is present, mark the item as review-required rather than pretending it is ready.",
        ]
    )


def decision_gates(skill: SkillSpec) -> list[str]:
    return [
        f"{config['label']}: do not mark the artifact ready until {config['qa'][0].rstrip('.').lower()}."
        for _, config in surface_configs(skill)
    ]


def qa_checks(skill: SkillSpec) -> list[str]:
    config = CATEGORY_CONFIG[skill.category]
    return unique([*config["qa"], *surface_items(skill, "qa")])


def failure_modes(skill: SkillSpec) -> list[str]:
    config = CATEGORY_CONFIG[skill.category]
    return unique([*config["failures"], *surface_items(skill, "failures")])


def proof_metrics(skill: SkillSpec) -> list[str]:
    config = CATEGORY_CONFIG[skill.category]
    return unique([*config["metrics"], *surface_items(skill, "metrics")])


def skill_workflow(skill: SkillSpec) -> list[str]:
    return [
        f"Confirm the user needs the `{skill.mechanic}` mechanic and identify the audience, artifact, and review owner.",
        f"Collect only the inputs needed for {surface_labels(skill)}; infer low-risk defaults and mark missing high-risk fields.",
        "Map each surface to the artifact fields before drafting recommendations.",
        "Apply the decision rules in `references/pattern.md` before drafting the artifact.",
        f"Return {skill.output} with QA checks, failure modes, metric, and next action.",
    ]


def artifact_template(skill: SkillSpec) -> list[str]:
    return [
        "Context and decision the artifact supports",
        "Input table with owner, freshness, and gaps",
        f"Mechanic-specific work product for {skill.display_name}",
        "Decision rules applied and tradeoffs",
        "QA checklist, failure modes, metric, and next action",
    ]


def ensure_initialized(skill: SkillSpec) -> None:
    skill_dir = SKILLS_DIR / skill.name
    (skill_dir / "agents").mkdir(parents=True, exist_ok=True)
    (skill_dir / "references").mkdir(parents=True, exist_ok=True)
    if skill.script:
        (skill_dir / "scripts").mkdir(parents=True, exist_ok=True)
    default_prompt = f"Use ${skill.name} to produce {skill.output}."
    short_description = skill.one_line_description.rstrip(".")
    (skill_dir / "agents" / "openai.yaml").write_text(
        "\n".join(
            [
                "interface:",
                f'  display_name: "{skill.display_name}"',
                f'  short_description: "{short_description}"',
                f'  default_prompt: "{default_prompt}"',
                "",
            ]
        ),
        encoding="utf-8",
    )


def skill_description(skill: SkillSpec) -> str:
    return (
        f"Use when a marketer or go-to-market operator needs {skill.output} "
        f"for {skill.category} work involving {surface_labels(skill)}, especially when "
        f"the task must {skill.mechanic}."
    )


def build_skill_md(skill: SkillSpec) -> str:
    script_note = ""
    if skill.script:
        script_note = f"\n- Run `scripts/{skill.script}` when the user provides structured inputs for the repeatable table, scorecard, or checklist."
    description = skill_description(skill)
    return f"""---
name: {skill.name}
description: {description}
---

# {skill.display_name}

## Quick Start

- Produce {skill.output}.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.{script_note}

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return {skill.output}. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
"""


def build_pattern_md(skill: SkillSpec) -> str:
    script = HELPER_SCRIPTS.get(skill.name)
    helper = "No helper script is bundled for this skill."
    if script:
        helper = f"Use `scripts/{script['filename']}` when inputs are structured. {script['description']}"
    example_prompt = (
        f"Use ${skill.name} to create {skill.output} for a marketing task in {skill.category}. "
        f"Apply the {surface_labels(skill)} mechanics and return the QA checks, failure modes, "
        "proof metric, and next action."
    )
    return f"""# {skill.display_name}

- Category: {skill.category}
- Product mechanic: {skill.mechanic}
- Output: {skill.output}
- Evidence surfaces: {", ".join(skill.surfaces)}

## When To Use

{skill.one_line_description}

## Product Mechanics

{surface_mechanics_table(skill)}

## Required Inputs

{wrap_lines(required_inputs(skill))}

## Decision Rules

{wrap_lines(decision_rules(skill))}

## Procedure

{wrap_lines(skill_workflow(skill))}

## Artifact Template

{wrap_lines(artifact_template(skill))}

## Skill-Specific Work Product

{wrap_lines(skill_specific_work_product(skill))}

## Artifact Fields

{wrap_lines(surface_artifact_fields(skill))}

## Decision Gates

{wrap_lines(decision_gates(skill))}

## QA Checks

{wrap_lines(qa_checks(skill))}

## Failure Modes

{wrap_lines(failure_modes(skill))}

## Proof Metrics

{wrap_lines(proof_metrics(skill))}

## Example Prompt

{example_prompt}

## Optional Helper

{helper}

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
"""


def write_helper_script(skill: SkillSpec) -> None:
    if not skill.script:
        return
    spec = HELPER_SCRIPTS[skill.name]
    skill_dir = SKILLS_DIR / skill.name
    script_path = skill_dir / "scripts" / spec["filename"]
    script_path.write_text(spec["content"], encoding="utf-8")
    tests_dir = skill_dir / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)
    test_path = tests_dir / spec["test_filename"]
    test_path.write_text(spec["test_content"], encoding="utf-8")


def write_license(skill: SkillSpec) -> None:
    skill_dir = SKILLS_DIR / skill.name
    (skill_dir / "LICENSE.txt").write_text(LICENSE_TEXT, encoding="utf-8")


def build_skills() -> list[dict]:
    skills = []
    for spec in SKILL_SPECS:
        surface_configs(spec)
        skill_specific_work_product(spec)
        item = asdict(spec)
        item["surfaces"] = list(spec.surfaces)
        skills.append(item)
    return skills


def readme(skills: list[dict]) -> str:
    grouped: dict[str, list[dict]] = {}
    for skill in skills:
        grouped.setdefault(skill["category"], []).append(skill)

    category_sections = []
    for category, category_skills in grouped.items():
        rows = "\n".join(
            "| "
            + " | ".join(
                [
                    f"[{skill['name']}](skills/{skill['name']}/SKILL.md)",
                    skill["one_line_description"],
                ]
            )
            + " |"
            for skill in category_skills
        )
        category_sections.append(f"### {category}\n\n| Skill | Description |\n| --- | --- |\n{rows}")
    catalog_sections = "\n\n".join(category_sections)

    return f"""# Marketing Skills

Marketing Skills are instructions, scripts, and resources that Codex, Claude Code, Gemini, and other AI agents can use for marketing tasks.

Built by Marvin Vista. Need hands-on help? I help teams build AI-ready marketing systems at [2066 Labs](https://2066labs.com).

## Skills

{catalog_sections}

## Install

Clone the repo, then run the installer:

```sh
git clone https://github.com/marvinvista/marketing-skills.git
cd marketing-skills
./install.sh
```

To install one skill:

```sh
./install.sh prompt-rank-monitor
```

Manual install:

```sh
mkdir -p "$HOME/.codex/skills"
ln -s "$PWD/skills/prompt-rank-monitor" "$HOME/.codex/skills/prompt-rank-monitor"
```

After installing or updating skills, restart Codex.

## License

Each skill folder includes `LICENSE.txt`.
"""


def agents_md() -> str:
    return """# Repository Guidance

This is a public Codex skill pack. Keep each skill folder lean, installable, and safe to publish:

- Put only `SKILL.md`, `agents/openai.yaml`, `references/pattern.md`, and justified helper scripts in each skill.
- Treat frontmatter `description` as a routing trigger, not long-form documentation.
- Keep `SKILL.md` concise and operational; put detailed decision rules, artifact templates, QA checks, failure modes, and examples in `references/pattern.md`.
- For helper-backed skills, keep the matching `tests/test_*.py` focused on script behavior only.
- Do not add private research inputs, unpublished links, or identity clues to this repository.
- Keep public wording useful to a marketer or operator who has no background context.
- Do not add per-skill READMEs or process notes.
- Keep the current single `skills/` layout; do not introduce `.system` or `.curated` splits.
- Validate with `python3 scripts/validate_skills.py` before committing.
"""


def contributing_md() -> str:
    return """# Contributing

## Values

- Keep contributions practical, respectful, and focused on repeatable marketing work.
- Improve the skill pack by making skills easier to trigger, run, validate, and review.
- Prefer small, reviewable changes over broad rewrites.

## Skill Rules

- Keep each skill self-contained and installable.
- Put routing context in the `description` frontmatter.
- Keep `SKILL.md` concise; put detailed rules, templates, checks, and examples in `references/pattern.md`.
- Add scripts only when deterministic execution is meaningfully better than instructions.
- Do not add private research inputs, unpublished links, or identity clues.
- Do not add per-skill README files or process notes.
- Keep the single `skills/` layout.

## Validation

Before opening a pull request, run:

```sh
python3 scripts/validate_skills.py
python3 scripts/smoke_install_skill.py
```

For helper-backed skills, also run the matching tests in `skills/*/tests/`.
"""


def gitignore() -> str:
    return """# Local retrieval snapshots
retrieval_*.html
retrieval_*.js

# Python
__pycache__/
.DS_Store
"""


def build(clean: bool) -> None:
    if clean and SKILLS_DIR.exists():
        shutil.rmtree(SKILLS_DIR)
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for path in DATA_DIR.glob("*.json"):
        path.unlink()

    skills = build_skills()
    specs_by_name = {spec.name: spec for spec in SKILL_SPECS}
    for skill in skills:
        spec = specs_by_name[skill["name"]]
        ensure_initialized(spec)
        skill_dir = SKILLS_DIR / spec.name
        (skill_dir / "SKILL.md").write_text(build_skill_md(spec), encoding="utf-8")
        (skill_dir / "references" / "pattern.md").write_text(build_pattern_md(spec), encoding="utf-8")
        write_license(spec)
        write_helper_script(spec)

    DATA_FILE.write_text(
        json.dumps(
            {
                "compiled_on": COMPILED_ON,
                "skill_count": len(skills),
                "evidence_boundary": "Private evidence map is maintained outside this repository.",
                "skills": skills,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (REPO_ROOT / "README.md").write_text(readme(skills), encoding="utf-8")
    (REPO_ROOT / "AGENTS.md").write_text(agents_md(), encoding="utf-8")
    (REPO_ROOT / "contributing.md").write_text(contributing_md(), encoding="utf-8")
    (REPO_ROOT / "LICENSE").write_text(LICENSE_TEXT, encoding="utf-8")
    (REPO_ROOT / ".gitignore").write_text(gitignore(), encoding="utf-8")
    print(f"Generated {len(skills)} anonymized product-mechanic skills.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build anonymized AI marketing product-mechanic skills")
    parser.add_argument("--clean", action="store_true", help="recreate the skills directory")
    args = parser.parse_args()
    build(clean=args.clean)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
