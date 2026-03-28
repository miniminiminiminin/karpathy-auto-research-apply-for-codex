# Parallel Maintenance Dispatch

```text
DISPATCH.root_skill := /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/skillsmith/SKILL.md
DISPATCH.root_reference := /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/skillsmith/references/pseudocode-style-rules.md
DISPATCH.work_area := principles.adactio.com owner-batch absorption program
DISPATCH.command := one_active_batch_at_a_time_then_cross_owner_audit
DISPATCH.owned_paths :=
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/skillsmith/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/visual-design/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/product-and-ux/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/architecture-and-design/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/planning-and-scoping/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/implementation-frontend/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/implementation-backend/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/quality-and-review/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/release-and-operations/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/intake-and-routing/**
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/CANON/README.md
  - /Users/gimminseog/Projects/research/karpathy-auto-research-apply-for-codex/docs/plans/2026-03-28-principles-*.md
DISPATCH.required_reads :=
  - docs/plans/2026-03-28-principles-adactio-canon-absorption-program.md
  - docs/plans/2026-03-28-principles-family-map.md
  - owner-local `SKILL.md`, `assets/`, and `references/` for the active batch
  - representative source files for the active principle family
DISPATCH.stop_conditions :=
  - stop if a rule starts duplicating a neighboring owner
  - stop if a batch would add a new top-level owner without proof
  - stop if a principle cannot be translated into an operator-facing hook and park it as deferred
DISPATCH.return_contract :=
  - declared_files
  - files_read
  - files_used
  - source_bands_consumed
  - owner_boundary_notes
  - deferred_items_recorded
  - review_verdict
DISPATCH.source_bands :=
  - responsive_and_context
  - inclusive_and_comparable_experience
  - service_outcome_and_wayfinding
  - simplicity_clarity_and_irreducible_core
  - modularity_maintainability_and_reuse
  - robustness_compatibility_and_graceful_failure
  - consistency_hierarchy_and_visual_restraint
  - data_iteration_and_open_improvement
  - implementation_translation_and_open_web_constraints
  - operations_longevity_and_sustainability
DISPATCH.principle_families :=
  - user-needs-first outcomes
  - comparable experience
  - adaptability to context
  - simplicity through hard work
  - consistency without blind uniformity
  - user control and meaningful choice
  - content priority and wayfinding
  - modularity and replaceable seams
  - maintainability and longevity
  - robustness and graceful degradation
  - interoperability and openness
  - evidence-driven iteration
  - minimal viable scope
  - cross-channel continuity
  - sustainability when operationally material
DISPATCH.primary_owner := skillsmith coordinating owner-specific batches
DISPATCH.secondary_consumers := all repo-local CANON owners listed in the family map

BATCH_RESULTS :=
  batch_1 -> visual-design + product-and-ux coverage-complete_with_review `docs/plans/2026-03-28-principles-batch-1-evaluation.md`
  batch_2 -> architecture-and-design + planning-and-scoping coverage-complete_with_review `docs/plans/2026-03-28-principles-batch-2-evaluation.md`
  batch_3 -> implementation-frontend + quality-and-review coverage-complete_with_review `docs/plans/2026-03-28-principles-batch-3-evaluation.md`
  batch_4 -> implementation-backend + release-and-operations coverage-complete_with_review `docs/plans/2026-03-28-principles-batch-4-evaluation.md`
  batch_5 -> intake-and-routing + README catalog audit coverage-complete_with_review `docs/plans/2026-03-28-principles-batch-5-evaluation.md`

DEFERRED_BACKLOG :=
  - release-side sustainability gates stronger than note-only capture
  - iterate-with-data thresholds and post-launch trigger hardening
  - broader context-for-everyone matrices and cross-owner hardening

RETURN := PASS IF
  actual_work_area = DISPATCH.work_area
  AND edited_paths SUBSET_OF DISPATCH.owned_paths
  AND required_reads_loaded = TRUE
  AND deviations_recorded = TRUE
  AND source_bands_consumed SUBSET_OF DISPATCH.source_bands
  AND primary_owner_respected = TRUE
  AND declared_files_reported = TRUE
  AND files_read_reported = TRUE
  AND files_used_reported = TRUE
```
