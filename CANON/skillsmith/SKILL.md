---
name: skillsmith
description: Use when creating or revising a repo-local skill package or Canon-owned reusable package so its triggers, support files, and output contract are explicit and reusable.
---

# Skillsmith

## Required Reads

- You MUST read `references/pseudocode-style-rules.md` before revising routing, process, checklist, asset, or reference wording.
- You MUST read `references/overlap-and-audit-guardrails.md` before widening a package, creating neighboring support files, or cloning adjacent skill behavior.
- You MUST read `references/book-absorption-rules.md` before distilling a PDF, book, or other long-form source into repo-local skills.
- You MUST start from `assets/skill-authoring-record.md` before revising package boundaries. Add `assets/asset-promotion-record.md` when moving detail out of `SKILL.md`.
- You MUST start from `assets/absorption-decision-record.md` when importing external material or long-form source material.
- You MUST use `assets/parallel-maintenance-dispatch.md` when the change will be fanned out across multiple owned packages.

## Overview

Build the skill package, not just the wording.

**Core principle:** if the trigger, output contract, or failure defenses are implicit, the skill is still a draft.

<HARD-GATE>
Do not ship a new or revised skill while its local ownership, output contract, and anti-failure structure are still implicit.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before revising the package, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<COVERAGE-GATE>
Do not claim long-form absorption is complete until coverage_proof exists for the source inventory, ownership split, absorbed rules, deferred rules, and visual-review backlog.
</COVERAGE-GATE>

<ANTI-PATTERN>
Do not treat skill writing as prompt filing. Copying persona-heavy source text into a skill package without distilling procedure, assets, and guardrails is a failed compilation.
</ANTI-PATTERN>

<CATALOG-GATE>
Do not ship a parallel top-level namespace when an existing repo-local skill can absorb the behavior without losing trigger clarity.
</CATALOG-GATE>

## When to Use

- adding or revising a repo-local skill package under `.codex/skills/**`
- adding or revising a Canon-owned reusable package under `CANON/skillsmith/packages/**`
- reducing a prompt dump, note, or repeated workflow into a deterministic skill package
- moving detail out of `SKILL.md` into durable local assets or references
- tightening trigger boundaries, support-file selection, or output contract clarity

## Do Not Use

- executing the target task directly when no skill change is needed
- broad prompt refactors outside the skill package
- one-off task notes that do not deserve reusable packaging

## Procedure

```text
INPUT := { recurring_job, raw_materials, failure_modes, output_contract, coverage_proof }
SUPPORT := { declared_files, files_read_before_revision, why_each_file_was_loaded }
STYLE_RULES := LOAD(references/pseudocode-style-rules.md)
OVERLAP_RULES := LOAD(references/overlap-and-audit-guardrails.md)

IF INPUT.recurring_job IS null OR INPUT.output_contract IS implicit:
  STOP("refine inputs before revising the package")
IF raw_materials_include(long_form_source) AND coverage_proof IS implicit:
  STOP("record source coverage before claiming absorption")
IF imported_behavior_map_is_incomplete THEN STOP("finish the convergence audit before changing catalog surface area")
IF new_top_level_skill_is_proposed AND admission_gate_justification IS implicit:
  STOP("justify the new top-level skill before revising the catalog")

CORE := {
  trigger,
  success_condition,
  non_goals,
  hard_gates,
  anti_patterns
}

SKILL_MD := KEEP({ routing, required_reads, hard_gates, process, output_contract })
DETAIL.reference := MOVE(long_form_rules AND stable decision logic)
DETAIL.asset := MOVE(repeatable worksheets OR dispatch stubs OR checklists)

IF raw_materials_include(long_form_source):
  REQUIRE(source_inventory, ownership_split, absorbed_vs_deferred_record, visual_review_backlog)

IF new_top_level_skill_is_proposed THEN REQUIRE(admission_gate_justification)
IF existing_repo_local_skill_can_absorb_behavior_without_losing(trigger_clarity OR output_contract_force):
  KEEP(absorption_inside_existing_owner)
ELSE:
  ALLOW(new_top_level_skill)

IF support_file DOES_NOT materially_reduce_guesswork:
  DROP(support_file)

AUDIT := PASS IF
  trigger_is_sharp
  AND support_file_selection_is_explicit
  AND hidden_dependencies_are_removed
  AND style_matches(STYLE_RULES)
  AND overlap_risk_matches(OVERLAP_RULES)
  AND coverage_proof_exists_before_completion_claims

IF AUDIT = FAIL:
  REVISE()

IF routing_surface_changed = TRUE:
  UPDATE(.codex/skills/README.md)
```

## Choose Roles

- `IF compiling_or_distilling THEN use agents/skill-author.md`
- `IF auditing_trigger_or_package_shape THEN use agents/skill-reviewer.md`

## Choose Assets

- `IF default_revision THEN use assets/skill-authoring-record.md`
- `IF auditing_trigger OR auditing_bloat THEN use assets/skill-audit.md`
- `IF moving_detail_out_of_SKILL THEN use assets/asset-promotion-record.md`
- `IF routing_surface_changed THEN use assets/change-impact-record.md`
- `IF deciding_durability THEN use assets/skill-pattern-checklist.md`
- `IF absorbing_external_material THEN use assets/absorption-decision-record.md`
- `IF long_form_absorption_needs_coverage_tracking THEN use assets/absorption-decision-record.md`
- `IF parallel_maintenance = TRUE THEN use assets/parallel-maintenance-dispatch.md`

## Choose References

- `IF deciding_what_leaves_SKILL THEN use references/asset-promotion.md`
- `IF package_shape OR support_scope IS disputed THEN use references/skill-packaging-rules.md`
- `IF importing_external_material THEN use references/external-material-distillation.md`
- `IF deciding_examples OR scripts THEN use references/example-and-best-code-usage.md`
- `IF revising_style THEN use references/pseudocode-style-rules.md`
- `IF source_is_pdf OR source_is_book OR source_is_long_form_document THEN use references/book-absorption-rules.md`
- `IF guarding_against_sprawl THEN use references/overlap-and-audit-guardrails.md`

## Output Contract

Return a skill authoring record with:

- declared support files
- files read before revision
- why each file was loaded
- target skill path
- operating concern
- admission gate justification
- source behavior map
- pseudocode style changes applied
- support files added or removed
- Canon-owned package surfaces added or revised
- failure modes addressed
- multi-agent dispatch or reporting contract changed
- traceability fields added or tightened
- coverage proof added or tightened
- shared docs updated
- files actually used
