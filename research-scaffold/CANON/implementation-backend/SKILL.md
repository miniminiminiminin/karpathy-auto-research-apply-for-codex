---
name: implementation-backend
description: Use when a chosen backend seam such as an API, job, adapter, or data contract needs implementation and contract-safe verification.
---

# Implementation Backend

## Overview

Ship the backend seam without smuggling in architectural drift.

**Core principle:** if the contract, dependency boundary, edge handling, or verification seam is vague, the backend change is not ready.

Write the test first. Watch it fail. Write minimal code to pass.

**Violating the letter of the rules is violating the spirit of the rules.**

<HARD-GATE>
Do not implement a backend change until the public seam, allowed dependencies, data assumptions, and verification path are explicit.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before coding, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
If runtime behavior matters, record baseline evidence, consumer impact, idempotency expectations, and bounded runtime behavior before calling the seam complete.
</NON-NEGOTIABLE>

<DISCIPLINE-GATE>
root_cause_or_failure_mode_is_named_before_fix.
red_green_proof_is_required_when_behavior_changes.
NO_PRODUCTION_CODE_WITHOUT_A_FAILING_TEST_FIRST.
</DISCIPLINE-GATE>

<ANTI-PATTERN>
Do not hide schema drift, null handling, compatibility risk, or undocumented contract changes behind passing tests.
</ANTI-PATTERN>

## Required Reads

- You MUST read `references/implementation-guardrails.md` before coding when this skill triggers.
- You MUST start from `assets/contract-checklist.md` before implementation.
- IF data_movement_or_lineage_risk_dominates THEN SWITCH -> `assets/pipeline-review-checklist.md`

## When to Use

- IF public_api OR job OR adapter OR persistence_seam IS chosen AND needs_building THEN USE
- IF data_shape OR compatibility OR null_handling IS now implementation_work THEN USE
- IF architecture_is_settled AND remaining_risk_is_contract_safe_delivery THEN USE
- IF new_feature OR bug_fix OR refactor OR behavior_change THEN USE

## Do Not Use

- IF seam_is_not_chosen THEN ROUTE -> architecture-and-design OR planning-and-scoping
- IF work_is_frontend_behavior THEN ROUTE -> implementation-frontend
- IF work_is_release_approval THEN ROUTE -> quality-and-review OR release-and-operations

## The Iron Law

```text
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

## Procedure

```text
STEP_0 := DECLARE(support_files := exact assets/ + references/ set OR none)
STEP_0A := READ(required_assets_and_references_before_coding)
STEP_0B := RECORD(why_each_declared_file_was_loaded)
INPUT := { seam, dependencies, consumers, rollback_sensitivity, runtime_expectations }

IF seam_is_not_explicit OR verification_path_is_missing THEN STOP("clarify the backend seam first")
IF behavior_change_or_bug_fix AND root_cause_or_failure_mode_is_implicit THEN STOP("name the failure mode before fixing")

BOUNDARY := DEFINE(
  validation,
  error_shape,
  side_effects,
  data_assumptions,
  compatibility_risk
)

IF runtime_behavior_matters THEN
  RECORD(latency, retries, batching, duplicates, idempotency, baseline_evidence)

IF behavior_change_or_bug_fix THEN
  RECORD(failing_or_blocked_case_before_fix, expected_red_signal)
  WRITE(minimal_failing_test_showing_one_behavior)
  VERIFY_RED(test_fails_for_expected_reason_not_typo_or_harness_error)

IMPLEMENT minimum_change_that_satisfies(seam)

IF change_widens_into_architecture OR cross_consumer_redesign THEN ROUTE -> planning-and-scoping

VERIFY FROM owned_seam USING(targeted_tests, contract_checks, runtime_or_compatibility_proof)
VERIFY(red_green_proof) IF behavior_change_or_bug_fix
REFACTOR_ONLY_AFTER_GREEN()

HANDOFF := RECORD(changed_contract, changed_files, consumers, remaining_risk)

STOP("backend delivery note is ready")
```

## Choose Roles

- `IF default_backend_build THEN use agents/software-engineer-backend.md`
- `IF shared_infrastructure_or_cross_service_contract THEN use agents/platform.md`
- `IF contract_proof_is_the_weak_point THEN use agents/qa.md`
- `IF ETL_lineage_ingestion_or_schema_drift_sensitive THEN use agents/data-pipeline-reviewer.md`

## Choose Assets

- `IF default_delivery_note THEN START -> assets/backend-handoff.md`
- `IF contract_safe_completion_gate THEN START -> assets/contract-checklist.md`
- `IF data_movement_or_pipeline_behavior_dominates THEN START -> assets/pipeline-review-checklist.md`
- `IF endpoint_or_public_interface_changed THEN START -> assets/api-change-note.md`

## Choose References

- `IF coding_guardrail_needed THEN READ -> references/implementation-guardrails.md`
- `IF dependency_direction_or_seam_shape_needs_contract_check THEN READ -> references/backend-architecture-review.md`
- `IF seam_is_job_workflow_or_producer_consumer_chain THEN READ -> references/workflow-job-delivery.md`
- `IF reliability_idempotency_or_data_freshness_matter THEN READ -> references/data-pipeline-reliability.md`
- `IF fields_provenance_or_schema_evolution_changed THEN READ -> references/schema-and-lineage-rules.md`
- `IF docs_or_handoff_are_vague_after_code THEN READ -> references/backend-docs-gates.md`

## Output Contract

Return a backend delivery note with:

- declared support files
- files read before coding
- why each file was loaded
- seam implemented
- contracts and edge cases covered
- proof run
- watched failing test before implementation
- wrote minimal code to pass
- compatibility or consumer risk
- docs or release implications
- next owner or next skill
- files actually used

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Already manually tested" | Ad-hoc is not systematic. No record, can't re-run. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "TDD will slow me down" | TDD is faster than debugging regressions later. |

## Red Flags - STOP and Start Over

- Code before test
- Test after implementation
- Test passes immediately
- Can't explain why test failed
- Tests added later
- Rationalizing just this once
- Keep as reference or adapt existing code
- Already spent X hours, deleting is wasteful

All of these mean: Delete code. Start over with TDD.
