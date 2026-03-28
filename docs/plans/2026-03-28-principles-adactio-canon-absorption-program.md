# principles.adactio.com CANON Absorption Program

> **For agentic workers:** REQUIRED: Route all execution through `CANON/skillsmith/SKILL.md` first, then the owning repo-local skill for each seam batch. Do not treat this as one giant edit pass.

**Goal:** Absorb the usable principles from `resources/principles.adactio.com-markdown/**` into the existing CANON without creating overlap, owner confusion, or a fake completion claim.

**Architecture:** Treat this as a long-form source compilation program, not a prompt rewrite. `skillsmith` owns source coverage, ownership split, and deferred backlog. Each batch then lands in exactly one owning CANON package or one tightly bounded pair when the rule naturally spans direction and review. The sequence is `inventory -> family map -> ownership split -> batch ledger -> owner-specific absorption -> cross-owner audit`.

**Tech Stack:** Markdown, repo-local skill packages under `CANON/**`, source library under `resources/principles.adactio.com-markdown/**`

## Closure Status

- program status: coverage-complete for owner-batch absorption
- completion date: `2026-03-28`
- batch closure:
  - batch 1 complete: `visual-design` + `product-and-ux`
  - batch 2 complete: `architecture-and-design` + `planning-and-scoping`
  - batch 3 complete: `implementation-frontend` + `quality-and-review`
  - batch 4 complete: `implementation-backend` + `release-and-operations`
  - batch 5 complete: `intake-and-routing` + `CANON/README.md`
- verification model:
  - each batch had a dedicated evaluation rubric
    - `docs/plans/2026-03-28-principles-batch-1-evaluation.md`
    - `docs/plans/2026-03-28-principles-batch-2-evaluation.md`
    - `docs/plans/2026-03-28-principles-batch-3-evaluation.md`
    - `docs/plans/2026-03-28-principles-batch-4-evaluation.md`
    - `docs/plans/2026-03-28-principles-batch-5-evaluation.md`
  - each batch was reviewed with parallel subagents including Codex Spark
  - findings were integrated before closure
- deferred hardening left explicit:
  - stronger release-side sustainability decision gates
  - stricter iterate-with-data thresholds and post-launch trigger rules
  - broader context-for-everyone and cross-owner hardening discovered by later audits
- non-goal:
  - this closure does not claim every source sentence was copied verbatim; it claims durable families were translated into owner-facing rules with explicit deferrals for the rest

---

## Program Rules

- Do not claim “the book/site is absorbed” until every named source band has a disposition: `absorbed_now`, `deferred`, `excluded_as_non_durable`, or `needs_visual_review`.
- Do not let `visual-design` become the dumping ground for principles that actually belong to product framing, architecture, planning, implementation, review, or release.
- Do not widen the top-level skill catalog unless an existing owner provably cannot absorb the rule without losing trigger clarity.
- Prefer compiling principle families into existing `references/*.md`, `assets/*.md`, and sharp `SKILL.md` gates over scattering many tiny new files.
- Keep one active batch at a time. Everything else stays in the ledger as parked follow-up work.

## Initial Ownership Hypothesis

- `CANON/skillsmith/**`: source inventory, ownership split, coverage ledger, absorption audit, deferred backlog.
- `CANON/visual-design/**`: hierarchy, composition, typography, density, color, state expression, responsive visual adaptability.
- `CANON/product-and-ux/**`: user-needs-first, service clarity, comparable experience, content priority, wayfinding, no-dead-end flows, choice and control at the UX layer.
- `CANON/architecture-and-design/**`: modularity, maintainability, robustness, interoperability, extensibility, openness, platform reuse, explicit seam ownership.
- `CANON/planning-and-scoping/**`: irreducible core, do-less, bounded slices, exact ownership, dependency-aware sequencing, active-step discipline.
- `CANON/implementation-frontend/**`: interface translation rules, adaptable layouts, keyboard and ARIA baseline, state coverage, progressive enhancement shaped as implementation constraints.
- `CANON/implementation-backend/**`: maintainability, robustness, workflow reliability, schema clarity, compatibility and simplicity at service/backend seam level.
- `CANON/quality-and-review/**`: inclusive QA bar, criterion discipline, root-cause rigor, evidence-before-claims, docs-as-product-quality.
- `CANON/release-and-operations/**`: operational robustness, clear rollback, runtime evidence, environmental or cost-impact notes when they materially affect ship/hold decisions.
- `CANON/intake-and-routing/**`: route large principle-absorption requests into the correct owner without accidental implementation or accidental orchestration.

## Principle Family Map

The source library should be reduced into these reusable family buckets before owner-level edits begin:

1. User need and service outcome
2. Comparable and inclusive experience
3. Context and adaptability
4. Simplicity, clarity, and “do the hard work”
5. Consistency without rigidity
6. Choice, control, and humane defaults
7. Content priority and wayfinding
8. Modularity, extensibility, and reuse
9. Maintainability, longevity, and interoperability
10. Robustness, compatibility, and graceful failure
11. Openness, transparency, and explanation
12. Iteration, data, and evidence loops
13. Minimum viable scope and irreducible core
14. Cross-channel and service continuity
15. Operational sustainability and environmental impact

## Batch Order

1. Foundation ledger and ownership split
2. Visual direction and critique layer
3. Product and UX direction layer
4. Architecture and seam-control layer
5. Planning and bounded execution layer
6. Frontend and backend implementation translation layer
7. Review, QA, and release layer
8. Intake, routing, and catalog audit

## Final Outcome

- no new top-level CANON owner was added
- durable principle families were absorbed into existing owners rather than scattered into tiny packages
- owner boundaries were clarified rather than flattened
- deferred items remain named in `CANON/skillsmith/assets/absorption-decision-record.md`
- the root catalog in `CANON/README.md` now reflects the current owner map and the explicit deferral model

---

### Task 1: Build The Source Coverage Ledger

**Files:**
- Create: `docs/plans/2026-03-28-principles-adactio-canon-absorption-program.md`
- Modify: `CANON/skillsmith/assets/absorption-decision-record.md`

**Step 1: Record the source inventory**

Summarize the captured library using `resources/principles.adactio.com/README.md` and the markdown tree under `resources/principles.adactio.com-markdown/**`.

**Step 2: Name source bands**

Group entries into reusable bands such as `responsive_and_context`, `inclusive_design`, `service_design`, `web_format_and_open_web`, `modularity_and_robustness`, `consistency_and_design_systems`, and `operations_and_sustainability`.

**Step 3: Add disposition fields**

Expand the absorption record so each source band can be marked `absorbed_now`, `deferred`, `excluded_as_non_durable`, or `needs_visual_review`.

**Step 4: Add owner mapping**

For each source band, record the owning CANON package and the expected target files.

**Step 5: Add backlog visibility**

Make deferred rules and visual-review backlog explicit so “not yet absorbed” work cannot disappear into memory.

### Task 2: Build The Family Distillation Matrix

**Files:**
- Modify: `CANON/skillsmith/assets/absorption-decision-record.md`
- Create: `docs/plans/2026-03-28-principles-family-map.md`

**Step 1: Convert source bands into principle families**

Translate author/site-specific prose into repo-local rule families that survive source change.

**Step 2: Strip non-durable material**

Remove biography, vendor-specific examples, platform nostalgia, and low-signal historical detail.

**Step 3: Mark cross-owner families**

Identify families that naturally split across two layers, such as `inclusive experience` across product, visual, implementation, and review.

**Step 4: Name primary owner and secondary consumers**

Keep one owner per family, even when other skills must reference the result.

**Step 5: Freeze the first absorption order**

Choose the family order that minimizes rework in downstream packages.

### Task 3: Create The Program Dispatch Contract

**Files:**
- Modify: `CANON/skillsmith/assets/parallel-maintenance-dispatch.md`

**Step 1: Replace placeholder root paths**

Point the dispatch asset at this repository’s live `CANON/skillsmith/**` paths.

**Step 2: Add owner-batch dispatch fields**

Record `work_area`, `owned_paths`, `required_reads`, `return_contract`, and `stop_conditions` for each seam batch.

**Step 3: Add overlap guardrails**

Require batch workers to stop when they are about to create a neighboring skill concern or duplicate an adjacent reference.

**Step 4: Add completion proof**

Require the worker to return `declared_files`, `files_read`, `files_used`, and the source bands consumed.

**Step 5: Define blocked-state behavior**

Specify that ambiguous rules go back into the ledger as deferred items rather than being forced into the wrong owner.

### Task 4: Normalize Visual Sources Before Editing Visual Design

**Files:**
- Modify: `CANON/visual-design/references/visual-principles-sources.md`
- Possibly create: `CANON/visual-design/references/responsive-visual-rules.md`

**Step 1: Re-evaluate source quality**

Keep responsive and inclusive visual sources, and replace any weak or noisy source references that are not durable enough for CANON use.

**Step 2: Separate source list from working rules**

Keep provenance in `visual-principles-sources.md`, but move stable screen-level rules into a dedicated reference if the file is becoming mixed-purpose.

**Step 3: Translate rules into visual constraints**

Express principles as hierarchy, composition, density, type, color, state, and responsive-survival constraints.

**Step 4: Add anti-misuse language**

Prevent “minimalism”, “taste”, or “brand vibe” from being used as a substitute for usable visual rules.

**Step 5: Verify routing clarity**

Check that visual-only principles do not leak product, architecture, or implementation ownership.

### Task 5: Absorb Visual Adaptability Into Visual Direction

**Files:**
- Modify: `CANON/visual-design/SKILL.md`
- Modify: `CANON/visual-design/assets/visual-direction-brief.md`
- Modify: `CANON/visual-design/assets/visual-review-checklist.md`
- Modify: `CANON/visual-design/assets/design-critique-record.md`

**Step 1: Add “content and task first” framing**

Make visual direction start from task and content priority before layout polish.

**Step 2: Add responsive survival checks**

Require direction to survive unknown widths, density shifts, and degraded surface conditions.

**Step 3: Add comparable visual experience checks**

Make the critique and approval bar reject visual systems that only work for ideal users or ideal conditions.

**Step 4: Add control and motion rules**

Make motion, emphasis, and interaction cues user-controllable and subordinate to comprehension.

**Step 5: Add no-competing-signals review points**

Translate “less but better” into a concrete review bar for removing visual noise.

### Task 6: Absorb User-Need And Service Principles Into Product And UX

**Files:**
- Modify: `CANON/product-and-ux/SKILL.md`
- Modify: `CANON/product-and-ux/assets/product-brief.md`
- Modify: `CANON/product-and-ux/assets/ux-review.md`
- Modify: `CANON/product-and-ux/assets/inclusive-visual-checklist.md`

**Step 1: Tighten user-needs-first language**

Make it explicit that product direction starts from user outcomes, not feature requests or interface ideas.

**Step 2: Add service clarity constraints**

Require purpose, expectations, eligibility, next steps, and assistance paths to be explicit in UX direction.

**Step 3: Add no-dead-end and human-assistance rules**

Push service continuity into the brief and review bar.

**Step 4: Add choice and control at the flow layer**

Require alternative paths and user control where one rigid path harms usability.

**Step 5: Add comparable experience language**

Make “inclusive” mean comparable task completion quality, not a bolt-on checklist.

### Task 7: Expand Product References For Principle Coverage

**Files:**
- Modify: `CANON/product-and-ux/references/signal-translation-rules.md`
- Modify: `CANON/product-and-ux/references/mobile-first-experience-principles.md`
- Modify: `CANON/product-and-ux/references/interaction-accessibility-principles.md`
- Possibly create: `CANON/product-and-ux/references/service-outcome-principles.md`

**Step 1: Add principle-family summaries**

Compile service-design, inclusive-design, and context principles into reusable product decision rules.

**Step 2: Clarify mobile-first meaning**

Frame mobile/context principles as adaptability and task focus, not device worship.

**Step 3: Add expectation-setting and decision-explanation rules**

Make purpose clarity and explainability durable references rather than one-off brief notes.

**Step 4: Add continuity rules**

Cover cross-channel consistency, status continuity, and change response as product/system expectations.

**Step 5: Audit overlap with visual design**

Keep low-fidelity direction here and push presentation-only rules back to `visual-design`.

### Task 8: Absorb Modularity And Robustness Into Architecture

**Files:**
- Modify: `CANON/architecture-and-design/SKILL.md`
- Modify: `CANON/architecture-and-design/assets/design-note.md`
- Modify: `CANON/architecture-and-design/assets/architecture-review-checklist.md`
- Modify: `CANON/architecture-and-design/assets/module-ownership.md`

**Step 1: Add modularity and reuse criteria**

Require seams to justify why a module exists and how it can be reused or replaced without excess redundancy.

**Step 2: Add maintainability and longevity checks**

Make long-lived comprehensibility and low-coupling explicit design requirements.

**Step 3: Add robustness rules**

Require graceful behavior under missing dependencies, partial failure, and degraded environments.

**Step 4: Add interoperability and openness checks**

Favor explicit contracts and reusable platforms over private one-off coupling.

**Step 5: Add do-less pressure**

Require architecture notes to justify the irreducible core and remove non-essential moving parts.

### Task 9: Expand Architecture References For Open-Web Principles

**Files:**
- Modify: `CANON/architecture-and-design/references/platform-contracts.md`
- Modify: `CANON/architecture-and-design/references/service-decomposition.md`
- Modify: `CANON/architecture-and-design/references/observability-and-reliability-baseline.md`
- Possibly create: `CANON/architecture-and-design/references/modularity-and-robustness.md`

**Step 1: Compile maintainability and modularity rules**

Distill Bert Bos style principles into architecture-level decision criteria.

**Step 2: Add compatibility and interoperability language**

Clarify when a seam should prefer durable, open, or composable interfaces.

**Step 3: Add graceful-failure and partial-system rules**

Make robustness more concrete than generic observability wording.

**Step 4: Add documentability and readability pressure**

Keep architecture outputs understandable enough for future operators.

**Step 5: Check for duplication**

Avoid re-stating implementation-specific guardrails in architecture references.

### Task 10: Absorb “Do Less” And Scope Discipline Into Planning

**Files:**
- Modify: `CANON/planning-and-scoping/SKILL.md`
- Modify: `CANON/planning-and-scoping/assets/plan-record.md`
- Modify: `CANON/planning-and-scoping/assets/scope-boundary-checklist.md`
- Modify: `CANON/planning-and-scoping/assets/task-breakdown-stub.md`

**Step 1: Add irreducible-core wording**

Force plans to identify the minimum valuable slice before decomposing steps.

**Step 2: Add anti-redundancy checks**

Prevent duplicate workstreams, duplicated assets, or overlapping active steps.

**Step 3: Add adaptability pressure**

Require step design to preserve room for later iteration without speculative widening now.

**Step 4: Add dead-end prevention**

Make handoff and stop conditions reject slices that strand the next owner without a clear outcome.

**Step 5: Add evidence-shaped iteration**

Tie replanning to fresh evidence rather than planner preference.

### Task 11: Expand Planning References For Bounded Delivery

**Files:**
- Modify: `CANON/planning-and-scoping/references/scope-control-rules.md`
- Modify: `CANON/planning-and-scoping/references/step-control-rules.md`
- Modify: `CANON/planning-and-scoping/references/workflow-delivery-lifecycle.md`
- Possibly create: `CANON/planning-and-scoping/references/minimum-viable-slice-rules.md`

**Step 1: Add “do less” heuristics**

Translate the principle into slice selection and work-sequencing rules.

**Step 2: Add continuity rules**

Make plans account for cross-step consistency and no-orphan outcomes.

**Step 3: Add data-and-iteration hooks**

Make plan review ask what evidence will advance the next iteration.

**Step 4: Add adaptability and context rules**

Allow plans to respond to current constraints without inventing new scope.

**Step 5: Reconcile with autonomous loop**

Ensure planning references stay compatible with planner -> executor -> evaluator operation.

### Task 12: Translate Principle Families Into Frontend Implementation

**Files:**
- Modify: `CANON/implementation-frontend/SKILL.md`
- Modify: `CANON/implementation-frontend/assets/frontend-implementation-brief.md`
- Modify: `CANON/implementation-frontend/assets/component-state-checklist.md`
- Modify: `CANON/implementation-frontend/assets/ui-review-checklist.md`
- Modify: `CANON/implementation-frontend/references/responsive-layout-patterns.md`
- Modify: `CANON/implementation-frontend/references/interface-pattern-translation.md`

**Step 1: Add responsive-from-content rules**

Make layout implementation start from content/task adaptability, not breakpoint theater.

**Step 2: Add comparable-experience implementation checks**

Require keyboard, source order, state messaging, and fallback behavior to preserve task completion.

**Step 3: Add user control constraints**

Forbid suppressing zoom, hidden controls, or unavoidable motion patterns.

**Step 4: Add consistency-without-uniformity translation**

Make frontend implementation preserve learned patterns while allowing justified local variation.

**Step 5: Add graceful state degradation**

Cover loading, error, empty, and offline-like conditions as first-class implementation states.

### Task 13: Translate Principle Families Into Backend Implementation

**Files:**
- Modify: `CANON/implementation-backend/SKILL.md`
- Modify: `CANON/implementation-backend/assets/contract-checklist.md`
- Modify: `CANON/implementation-backend/assets/backend-handoff.md`
- Modify: `CANON/implementation-backend/references/data-pipeline-reliability.md`
- Modify: `CANON/implementation-backend/references/schema-and-lineage-rules.md`

**Step 1: Add maintainability and readability constraints**

Make backend seams understandable and auditable for future operators.

**Step 2: Add robustness under partial failure**

Require retries, fallback shape, and corruption resistance to be explicit when relevant.

**Step 3: Add interoperability and compatibility checks**

Encourage durable contracts and migration-safe change notes.

**Step 4: Add minimum-complexity pressure**

Reject unnecessary indirection or abstraction that does not serve the owned seam.

**Step 5: Add operator-facing explanation requirements**

Make contract and workflow docs explain purpose, inputs, outputs, and failure modes clearly.

### Task 14: Absorb Inclusive And Evidence Principles Into Quality And Review

**Files:**
- Modify: `CANON/quality-and-review/SKILL.md`
- Modify: `CANON/quality-and-review/assets/review-checklist.md`
- Modify: `CANON/quality-and-review/assets/qa-verdict.md`
- Modify: `CANON/quality-and-review/assets/spec-review.md`
- Modify: `CANON/quality-and-review/assets/support-case-review.md`
- Modify: `CANON/quality-and-review/references/inclusive-visual-qa.md`
- Modify: `CANON/quality-and-review/references/criterion-discipline.md`

**Step 1: Add comparable-experience review language**

Make review reject solutions that technically function but degrade the experience for some users.

**Step 2: Add clarity and explanation checks**

Verify that services explain purpose, status, decisions, and next steps well enough to be usable.

**Step 3: Add no-dead-end QA checks**

Require review to catch stranded states, silent failures, and unusable exits.

**Step 4: Add evidence-loop hooks**

Make verification and support evidence feed the next iteration rather than only block completion.

**Step 5: Keep review order intact**

Absorb the new principles without weakening the existing spec-fit -> code-quality -> QA-evidence sequence.

### Task 15: Absorb Runtime Robustness Into Release And Operations

**Files:**
- Modify: `CANON/release-and-operations/SKILL.md`
- Modify: `CANON/release-and-operations/assets/release-gate.md`
- Modify: `CANON/release-and-operations/assets/operational-readiness.md`
- Modify: `CANON/release-and-operations/assets/rollback-record.md`
- Modify: `CANON/release-and-operations/references/release-evidence.md`
- Modify: `CANON/release-and-operations/references/launch-and-operate-cadence.md`

**Step 1: Add graceful-degradation language**

Make operational decisions account for degraded-but-usable states, not just binary up/down.

**Step 2: Add continuity and expectation-setting checks**

Require current user impact, next update time, and recovery expectations to be explicit.

**Step 3: Add adaptability and change-response rules**

Make the release owner consider changing user circumstances and cross-channel continuity.

**Step 4: Add sustainability or cost-impact note**

Include environmental or heavy-runtime impact only when it materially changes rollout or hold decisions.

**Step 5: Keep incident/release distinction sharp**

Do not let broad principle language blur operating-mode boundaries.

### Task 16: Tighten Intake And Routing For Principle-Heavy Requests

**Files:**
- Modify: `CANON/intake-and-routing/SKILL.md`
- Modify: `CANON/intake-and-routing/assets/intake-record.md`
- Modify: `CANON/intake-and-routing/assets/routing-decision.md`
- Modify: `CANON/intake-and-routing/references/signal-driven-routing.md`

**Step 1: Add long-form absorption routing**

Teach intake to route book/site absorption work to `skillsmith` before owner-specific editing begins.

**Step 2: Add mixed-request rules**

Clarify how to route requests that bundle product, visual, architecture, and implementation concerns.

**Step 3: Add minimum-next-owner logic**

Prevent orchestration when one owner can absorb the next principle family directly.

**Step 4: Add clarification discipline**

When principle intent is unclear, ask for the smallest missing boundary rather than broad discovery.

**Step 5: Add completion stop**

Make intake stop once the next owner is explicit and the request is bounded.

### Task 17: Run The Cross-Owner Overlap Audit

**Files:**
- Modify: `CANON/README.md`
- Modify: `CANON/skillsmith/assets/skill-audit.md`
- Modify: `CANON/skillsmith/assets/change-impact-record.md`

**Step 1: Check trigger boundaries**

Ensure no batch made neighboring skills harder to distinguish.

**Step 2: Check duplicate references**

Merge or trim any references that now restate the same family without sharper ownership.

**Step 3: Check asset sprawl**

Promote repeatable checklists, but remove any one-off or weakly justified new files.

**Step 4: Check catalog language**

Update `CANON/README.md` only if public routing or owner descriptions materially changed.

**Step 5: Reconcile owner map**

Update the master ledger with final ownership decisions and remaining deferred items.

### Task 18: Create The Deferred Backlog And Next-Batch Queue

**Files:**
- Modify: `CANON/skillsmith/assets/absorption-decision-record.md`
- Modify: `CANON/skillsmith/assets/change-impact-record.md`

**Step 1: Record what was intentionally deferred**

List source bands or examples that were not durable enough for this batch.

**Step 2: Record what needs visual review**

Capture layout-sensitive or source-ambiguity items that need screenshot or original-page comparison.

**Step 3: Record what was excluded**

Make exclusion explicit so it is not mistaken for forgotten work.

**Step 4: Queue the next owner batch**

Name the next smallest valuable seam to absorb after the current active batch completes.

**Step 5: Prevent false completion**

End with a program status of `partial`, `batched`, or `coverage-complete`; never use “done” until the ledger proves it.

---

## Recommended First Execution Slice

Start with the foundation batch, not `visual-design`.

1. Tighten `CANON/skillsmith/assets/absorption-decision-record.md` into a real coverage ledger.
2. Update `CANON/skillsmith/assets/parallel-maintenance-dispatch.md` to use this repo’s live paths and return contract.
3. Create `docs/plans/2026-03-28-principles-family-map.md` with source bands, principle families, and owner mapping.
4. Only then begin the first owner-facing absorption batch, with `visual-design` and `product-and-ux` as the most likely early winners.

## Stop Conditions

- Stop the active batch if the owning skill is no longer clear.
- Stop if a principle family starts touching three or more owners at once without a primary owner.
- Stop if the batch needs new top-level catalog surface area.
- Stop if source quality is too weak to distill into durable repo-local rules.
- Stop if the coverage ledger is not keeping up with actual edits.
