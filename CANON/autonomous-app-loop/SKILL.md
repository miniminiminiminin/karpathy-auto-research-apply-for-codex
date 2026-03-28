---
name: autonomous-app-loop
description: Use when bootstrap or one bounded slice in a purpose-first loop needs Canon-owned planner -> executor -> evaluator control, rubric lock, and promotion rules.
---

# Autonomous App Loop

## Overview

Run rubric bootstrap or one purpose-first delivery iteration without letting planning, implementation, and evaluation collapse into wishful narration.

**Core principle:** if the active slice, proof path, or promotion rule is vague, the loop is not ready.

<HARD-GATE>
Do not start a post-bootstrap iteration until the project objective, locked rubric, active slice, and fresh proof path are all visible.

Do not let the executor choose the goal.
Do not let the evaluator invent the rubric.
Do not promote a slice without fresh execution evidence.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before starting the iteration, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
The loop exists to improve performance against `purpose.txt`, not to maximize local code churn, story quality, or self-reported momentum.
</NON-NEGOTIABLE>

## When To Use

- the purpose is already defined and the next move is rubric bootstrap, rubric lock, baseline-proof initialization, or one bounded slice
- `rubric.txt` either needs one-time generation and lock or already exists and is locked
- bootstrap work may still be active even when no execution slice is ready yet
- one bounded slice is ready for execution when the loop is past bootstrap
- the next move is a planner -> executor -> evaluator loop rather than new product direction or release approval

## Do Not Use

- if the request is still unclear or the purpose is not yet defined -> route to `intake-and-routing`
- if the next move still needs design -> route to `product-and-ux`
- if rubric bootstrap is complete but the active slice is not yet operable -> route to `planning-and-scoping`
- if seams or contracts are still unstable -> route to `architecture-and-design`
- if planner, executor, evaluator, or required reviews can progress as independent owned slices -> stop and route to `multi-agent-orchestration`
- if the next decision is ship/no-ship -> route to `release-and-operations`

## Required Reads

- You MUST start from `assets/bootstrap-record.md` when rubric bootstrap, rubric lock, or baseline-proof initialization is the active question.
- You MUST read `assets/rubric-generation-prompt.md` and `references/bootstrap-and-rubric-lock-rules.md` when rubric generation, rubric lock, or scaffold bootstrap packaging is the active question.
- You MUST start from `assets/project-state.md` when the loop is past bootstrap and an execution slice is active.
- You MUST read `assets/iteration-brief.md` before defining the active slice once bootstrap is complete.
- You MUST read `assets/evaluation-report.md` before making the promotion decision once fresh execution proof exists.
- You MUST read `references/planner-executor-evaluator-contract.md` before assigning planner, executor, and evaluator responsibilities.
- Read `references/control-plane-and-worktree-separation.md` when the work surface is drifting.
- Read `references/loop-convergence-rules.md` when the loop is repeating without useful progress.
- Read `references/autonomous-delivery-guardrails.md` when the slice touches risky runtime, permissions, or expensive operations.

## Procedure

```text
1. DECLARE(support_files := exact assets/ + references/ set OR none)
2. READ(required_assets_and_references_before_iteration)
3. RECORD(why_each_declared_file_was_loaded)
4. LOAD(purpose, active_plan, current_project_state, last_iteration)
5. STOP("bootstrap cannot start without purpose") IF purpose_missing
6. IF rubric_missing THEN
  READ(assets/rubric-generation-prompt.md, references/bootstrap-and-rubric-lock-rules.md)
  GENERATE_AND_LOCK(rubric := one_time_bootstrap_from_purpose)
  RECORD(bootstrap_state := purpose + rubric_generation_source + rubric_lock_status + baseline_proof_path + next_owner IN assets/bootstrap-record.md)
  STOP("bootstrap still incomplete") IF rubric_not_locked OR baseline_proof_path_not_named
6A. VERIFY(locked_rubric_is_visible) IF rubric_missing = FALSE
7. STOP("slice is not ready") IF active_slice OR proof_path OR promotion_rule IS implicit
8. RECORD(project_state := current_stage + active_iteration + open_risks + next_owner)
9. DEFINE(iteration_brief := purpose_link + active_slice + non_goals + exact_proof + expected_score_change)
9A. STOP("route to multi-agent-orchestration") IF planner_executor_evaluator_or_review_work_decomposes_into_independent_owned_slices
10. ASSIGN(planner, executor, evaluator) WITH explicit boundaries
11. EXECUTOR_CHANGES_ONLY(project_surface)
12. RUN(fresh_execution_proof)
13. EVALUATE(result := rubric_score + regression_check + purpose_fit_delta)
14. DECIDE(promotion := keep OR discard OR escalate OR ship_candidate)
15. RECORD(loop_record := what_changed + proof + score_delta + promotion + next_slice_candidate)
16. ROUTE ->
  quality-and-review IF evidence_or_acceptance_is_weak
  release-and-operations IF the app looks ready to stop iterating
  planning-and-scoping IF the next slice is no longer bounded
  autonomous-app-loop IF another bounded slice is ready
```

## Choose Roles

- use `agents/orchestrator.md` when the main question is how to run and judge the current iteration
- use `agents/planner.md` when the weak point is slice selection and proof design
- use `agents/executor.md` when the implementation seam is already explicit
- use `agents/evaluator.md` when the weak point is scoring, regressions, or promotion decisions

## Choose Assets

- `IF default_iteration_state THEN START -> assets/project-state.md`
- `IF rubric_bootstrap_or_rubric_lock_is_active THEN START -> assets/bootstrap-record.md`
- `IF defining_the_active_slice THEN START -> assets/iteration-brief.md`
- `IF deciding_keep_discard_or_escalate THEN START -> assets/evaluation-report.md`
- `IF writing_the_promotion_decision THEN START -> assets/promotion-decision.md`
- `IF recording_iteration_history THEN START -> assets/loop-record.md`
- `IF bootstrap_or_rubric_generation_contract_is_under_review THEN START -> assets/rubric-generation-prompt.md`

## Choose References

- `IF planner_executor_evaluator_boundaries_need_clarity THEN READ -> references/planner-executor-evaluator-contract.md`
- `IF control_plane_and_project_surface_are_blurring THEN READ -> references/control-plane-and-worktree-separation.md`
- `IF repeated_iterations_show_weak_progress THEN READ -> references/loop-convergence-rules.md`
- `IF autonomy_or_runtime_risk_is_increasing THEN READ -> references/autonomous-delivery-guardrails.md`
- `IF rubric_generation_or_rubric_lock_is_the_question THEN READ -> references/bootstrap-and-rubric-lock-rules.md`

## Output Contract

Return an autonomous loop record with:

- declared support files
- files read before the iteration
- why each file was loaded
- bootstrap record when rubric generation or lock was the active question
- purpose link
- locked rubric assumption
- project state
- active slice and non-goals
- planner, executor, evaluator boundaries
- fresh proof run
- score and regression result
- promotion decision
- next owner or next skill
- files actually used
