# Plugin Eval All Skills

Run date: 2026-05-17

## Summary

- Skills evaluated individually: 116
- Gate: score >= 93, zero fail/error checks, zero warn/warning checks
- Gate failures: 0
- Low-risk skills: 116
- Minimum score: 100
- Maximum active budget: 532 tokens
- Maximum trigger cost: 52 tokens
- Plugin Eval CLI: resolved locally via PLUGIN_EVAL_CLI or Codex plugin cache

## Method

- Ran Plugin Eval `analyze` against every `skills/*/SKILL.md` target listed in `data/marketing_skills.json`.
- Treated informational coverage-artifact notes as non-blocking because these skills are mostly instruction artifacts; helper-backed scripts are covered by the repo test suite.
- Preserved per-skill score, risk, warning/failure counts, and token budget data in `evals/plugin_eval_all_skills.json`.

## Results

| Skill | Category | Score | Risk | Fail | Warn | Active Tokens | Trigger Tokens |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |
| `agent-action-backlog` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 518 | 44 |
| `agent-discovery-content-refresh-plan` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 513 | 44 |
| `agent-discovery-question-map` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 524 | 48 |
| `agentic-answer-ops-workflow` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 513 | 45 |
| `ai-answer-brand-risk-map` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 505 | 43 |
| `ai-answer-visibility-scorecard` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 528 | 52 |
| `ai-referral-roi-readout` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 518 | 48 |
| `ai-shopping-feed-optimizer` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 504 | 42 |
| `answer-claim-risk-review` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 519 | 47 |
| `answer-ready-content-brief` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 501 | 43 |
| `citable-proof-asset-kit` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 505 | 46 |
| `citation-source-gap-map` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 497 | 42 |
| `generative-search-weekly-ops-report` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 523 | 49 |
| `page-schema-indexability-audit` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 527 | 48 |
| `prompt-rank-monitor` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 528 | 41 |
| `search-creative-message-bridge` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 523 | 48 |
| `seo-brand-proof-governance` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 514 | 46 |
| `share-of-answer-benchmark` | AI Search / Agent Discovery | 100 | low | 0 | 0 | 498 | 42 |
| `community-ambassador-loop-design` | Content / Creator / Social | 100 | low | 0 | 0 | 501 | 42 |
| `community-response-playbook` | Content / Creator / Social | 100 | low | 0 | 0 | 498 | 42 |
| `content-repurposing-map` | Content / Creator / Social | 100 | low | 0 | 0 | 496 | 40 |
| `creator-discovery-scorecard` | Content / Creator / Social | 100 | low | 0 | 0 | 495 | 41 |
| `creator-performance-reuse-readout` | Content / Creator / Social | 100 | low | 0 | 0 | 511 | 43 |
| `event-content-reuse-system` | Content / Creator / Social | 100 | low | 0 | 0 | 504 | 42 |
| `influencer-outreach-offer-brief` | Content / Creator / Social | 100 | low | 0 | 0 | 500 | 41 |
| `seo-social-content-brief` | Content / Creator / Social | 100 | low | 0 | 0 | 493 | 39 |
| `social-content-calendar-system` | Content / Creator / Social | 100 | low | 0 | 0 | 498 | 46 |
| `social-listening-insight-brief` | Content / Creator / Social | 100 | low | 0 | 0 | 494 | 42 |
| `ugc-intake-rights-workflow` | Content / Creator / Social | 100 | low | 0 | 0 | 494 | 40 |
| `voiceover-localization-workflow` | Content / Creator / Social | 100 | low | 0 | 0 | 499 | 43 |
| `ad-variant-matrix-builder` | Creative / Ads / Assets | 100 | low | 0 | 0 | 515 | 40 |
| `agentic-video-production-workflow` | Creative / Ads / Assets | 100 | low | 0 | 0 | 524 | 52 |
| `brand-compliance-creative-review` | Creative / Ads / Assets | 100 | low | 0 | 0 | 496 | 43 |
| `catalog-ad-feed-plan` | Creative / Ads / Assets | 100 | low | 0 | 0 | 499 | 40 |
| `chat-creative-conversion-plan` | Creative / Ads / Assets | 100 | low | 0 | 0 | 513 | 45 |
| `competitor-ad-teardown` | Creative / Ads / Assets | 100 | low | 0 | 0 | 489 | 41 |
| `creative-agent-production-workflow` | Creative / Ads / Assets | 100 | low | 0 | 0 | 524 | 51 |
| `creative-brief-from-research` | Creative / Ads / Assets | 100 | low | 0 | 0 | 522 | 47 |
| `creative-enrichment-personalization-plan` | Creative / Ads / Assets | 100 | low | 0 | 0 | 526 | 50 |
| `creative-fatigue-refresh-plan` | Creative / Ads / Assets | 100 | low | 0 | 0 | 492 | 40 |
| `creative-lead-capture-loop` | Creative / Ads / Assets | 100 | low | 0 | 0 | 506 | 47 |
| `creative-outbound-message-bridge` | Creative / Ads / Assets | 100 | low | 0 | 0 | 519 | 48 |
| `creative-performance-readout` | Creative / Ads / Assets | 100 | low | 0 | 0 | 509 | 43 |
| `landing-page-message-match` | Creative / Ads / Assets | 100 | low | 0 | 0 | 507 | 43 |
| `multilingual-creative-localization` | Creative / Ads / Assets | 100 | low | 0 | 0 | 501 | 44 |
| `multimodal-asset-assembly-brief` | Creative / Ads / Assets | 100 | low | 0 | 0 | 506 | 43 |
| `offer-angle-mining` | Creative / Ads / Assets | 100 | low | 0 | 0 | 477 | 38 |
| `paid-launch-checklist` | Creative / Ads / Assets | 100 | low | 0 | 0 | 492 | 40 |
| `podcast-audio-ad-read-guide` | Creative / Ads / Assets | 100 | low | 0 | 0 | 497 | 43 |
| `product-image-qa-brief` | Creative / Ads / Assets | 100 | low | 0 | 0 | 508 | 44 |
| `short-form-hook-bank` | Creative / Ads / Assets | 100 | low | 0 | 0 | 483 | 38 |
| `synthetic-creative-test-panel` | Creative / Ads / Assets | 100 | low | 0 | 0 | 520 | 49 |
| `ugc-ad-script-pack` | Creative / Ads / Assets | 100 | low | 0 | 0 | 475 | 37 |
| `video-ad-storyboard` | Creative / Ads / Assets | 100 | low | 0 | 0 | 489 | 40 |
| `video-seo-content-reuse-plan` | Creative / Ads / Assets | 100 | low | 0 | 0 | 499 | 42 |
| `visual-asset-prompt-brief` | Creative / Ads / Assets | 100 | low | 0 | 0 | 514 | 45 |
| `account-list-sourcing-brief` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 486 | 42 |
| `account-research-snapshot` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 495 | 43 |
| `agentic-list-building-workflow` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 513 | 49 |
| `answer-led-list-hypothesis-panel` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 522 | 51 |
| `audience-list-sync-readiness` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 511 | 49 |
| `buying-signal-listener-spec` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 494 | 41 |
| `chat-lead-routing-flow` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 499 | 47 |
| `crm-handoff-qa` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 471 | 38 |
| `demo-booking-friction-audit` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 483 | 37 |
| `enrichment-field-contract` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 486 | 40 |
| `event-lead-capture-followup` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 489 | 39 |
| `icp-segment-trigger-map` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 470 | 34 |
| `inbound-chat-qualification-flow` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 480 | 40 |
| `intent-led-outbound-sequence` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 487 | 39 |
| `lead-list-prioritization-scorecard` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 532 | 43 |
| `linkedin-prospecting-cadence` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 473 | 37 |
| `local-business-prospecting-route` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 487 | 40 |
| `multichannel-prospecting-orchestration` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 496 | 42 |
| `referral-partner-lead-loop` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 488 | 41 |
| `reply-intent-triage-rules` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 481 | 40 |
| `sales-marketing-feedback-loop` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 496 | 43 |
| `visitor-list-routing-plan` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 506 | 46 |
| `website-visitor-to-account-workflow` | Lead Intelligence / Conversion | 100 | low | 0 | 0 | 497 | 43 |
| `attribution-diagnostic` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 483 | 42 |
| `audience-sync-contract` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 469 | 38 |
| `campaign-preflight-qa-checklist` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 530 | 45 |
| `campaign-tracking-plan` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 473 | 37 |
| `consent-suppression-rollback-plan` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 498 | 44 |
| `email-template-system` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 470 | 35 |
| `experiment-readout` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 463 | 34 |
| `lifecycle-segmentation-map` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 482 | 39 |
| `marketing-dashboard-spec` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 471 | 37 |
| `retention-reactivation-loop` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 497 | 41 |
| `warehouse-audience-activation-plan` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 483 | 43 |
| `whatsapp-sms-conversation-flow` | Lifecycle / Ops / Analytics | 100 | low | 0 | 0 | 494 | 40 |
| `agentic-seo-briefing-workflow` | Marketing Agents / Governance | 100 | low | 0 | 0 | 515 | 51 |
| `ai-workflow-telemetry-plan` | Marketing Agents / Governance | 100 | low | 0 | 0 | 495 | 41 |
| `automation-risk-register` | Marketing Agents / Governance | 100 | low | 0 | 0 | 493 | 39 |
| `brand-voice-memory` | Marketing Agents / Governance | 100 | low | 0 | 0 | 484 | 40 |
| `claims-hallucination-review` | Marketing Agents / Governance | 100 | low | 0 | 0 | 508 | 44 |
| `human-approval-ladder` | Marketing Agents / Governance | 100 | low | 0 | 0 | 467 | 32 |
| `internal-knowledge-activation` | Marketing Agents / Governance | 100 | low | 0 | 0 | 496 | 42 |
| `marketing-agent-workflow-spec` | Marketing Agents / Governance | 100 | low | 0 | 0 | 484 | 41 |
| `marketing-output-eval-harness` | Marketing Agents / Governance | 100 | low | 0 | 0 | 495 | 43 |
| `prompt-library-maintenance` | Marketing Agents / Governance | 100 | low | 0 | 0 | 488 | 41 |
| `tool-orchestration-map` | Marketing Agents / Governance | 100 | low | 0 | 0 | 466 | 35 |
| `audience-intelligence-brief` | Research / Audience Simulation | 100 | low | 0 | 0 | 489 | 39 |
| `customer-journey-evidence-map` | Research / Audience Simulation | 100 | low | 0 | 0 | 484 | 38 |
| `interview-guide-builder` | Research / Audience Simulation | 100 | low | 0 | 0 | 481 | 40 |
| `interview-synthesis-matrix` | Research / Audience Simulation | 100 | low | 0 | 0 | 489 | 43 |
| `local-market-research-brief` | Research / Audience Simulation | 100 | low | 0 | 0 | 509 | 44 |
| `market-segmentation-memo` | Research / Audience Simulation | 100 | low | 0 | 0 | 475 | 37 |
| `message-test-scorecard` | Research / Audience Simulation | 100 | low | 0 | 0 | 482 | 41 |
| `positioning-claim-map` | Research / Audience Simulation | 100 | low | 0 | 0 | 469 | 35 |
| `research-decision-memo` | Research / Audience Simulation | 100 | low | 0 | 0 | 487 | 43 |
| `review-forum-mining-brief` | Research / Audience Simulation | 100 | low | 0 | 0 | 491 | 43 |
| `stakeholder-simulation-scenario-plan` | Research / Audience Simulation | 100 | low | 0 | 0 | 499 | 43 |
| `survey-instrument-builder` | Research / Audience Simulation | 100 | low | 0 | 0 | 508 | 45 |
| `synthetic-audience-panel-builder` | Research / Audience Simulation | 100 | low | 0 | 0 | 495 | 44 |
| `synthetic-enrichment-panel` | Research / Audience Simulation | 100 | low | 0 | 0 | 519 | 48 |
