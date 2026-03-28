---
name: autonomous-app-loop
description: Use when one bounded slice is execution-ready and the next move is a planner -> executor -> evaluator iteration that should improve how well the project performs `purpose.txt`.
---

# Autonomous App Loop

## Overview

Run one purpose-first delivery iteration without letting planning, implementation, and evaluation collapse into wishful narration.

**Core principle:** if the active slice, proof path, or promotion rule is vague, the loop is not ready.

<HARD-GATE>
Do not start an iteration until the project objective, locked rubric, active slice, and fresh proof path are all visible.

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

- the purpose is already defined
- `rubric.txt` already exists and is locked
- one bounded slice is ready for execution
- the next move is a planner -> executor -> evaluator loop rather than new product direction or release approval

## Do Not Use

- if the request is still unclear -> route to `intake-and-routing`
- if the next move still needs design -> route to `product-and-ux`
- if the active slice is not yet operable -> route to `planning-and-scoping`
- if seams or contracts are still unstable -> route to `architecture-and-design`
- if the next decision is ship/no-ship -> route to `release-and-operations`

## Required Reads

- You MUST start from `assets/project-state.md` before the iteration.
- You MUST read `assets/iteration-brief.md` before defining the active slice.
- You MUST read `assets/evaluation-report.md` before making the promotion decision.
- You MUST read `references/planner-executor-evaluator-contract.md` before assigning responsibilities.
- Read `references/control-plane-and-worktree-separation.md` when the work surface is drifting.
- Read `references/loop-convergence-rules.md` when the loop is repeating without useful progress.
- Read `references/autonomous-delivery-guardrails.md` when the slice touches risky runtime, permissions, or expensive operations.

## Procedure

```text
1. DECLARE(support_files := exact assets/ + references/ set OR none)
2. READ(required_assets_and_references_before_iteration)
3. RECORD(why_each_declared_file_was_loaded)
4. LOAD(purpose, locked_rubric, active_plan, current_project_state, last_iteration)
5. STOP("bootstrap is incomplete") IF purpose_missing OR rubric_missing
6. STOP("slice is not ready") IF active_slice OR proof_path OR promotion_rule IS implicit
7. RECORD(project_state := current_stage + active_iteration + open_risks + next_owner)
8. DEFINE(iteration_brief := purpose_link + active_slice + non_goals + exact_proof + expected_score_change)
9. ASSIGN(planner, executor, evaluator) WITH explicit boundaries
10. EXECUTOR_CHANGES_ONLY(project_surface)
11. RUN(fresh_execution_proof)
12. EVALUATE(result := rubric_score + regression_check + purpose_fit_delta)
13. DECIDE(promotion := keep OR discard OR escalate OR ship_candidate)
14. RECORD(loop_record := what_changed + proof + score_delta + promotion + next_slice_candidate)
15. ROUTE ->
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
- `IF defining_the_active_slice THEN START -> assets/iteration-brief.md`
- `IF deciding_keep_discard_or_escalate THEN START -> assets/evaluation-report.md`
- `IF writing_the_promotion_decision THEN START -> assets/promotion-decision.md`
- `IF recording_iteration_history THEN START -> assets/loop-record.md`

## Choose References

- `IF planner_executor_evaluator_boundaries_need_clarity THEN READ -> references/planner-executor-evaluator-contract.md`
- `IF control_plane_and_project_surface_are_blurring THEN READ -> references/control-plane-and-worktree-separation.md`
- `IF repeated_iterations_show_weak_progress THEN READ -> references/loop-convergence-rules.md`
- `IF autonomy_or_runtime_risk_is_increasing THEN READ -> references/autonomous-delivery-guardrails.md`

## Output Contract

Return an autonomous loop record with:

- declared support files
- files read before the iteration
- why each file was loaded
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
