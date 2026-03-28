---
name: multi-agent-orchestration
description: Use when disjoint role-owned slices can run in parallel only if dispatch, support paths, proof, and convergence are explicit.
---

# Multi-Agent Orchestration

## Overview

Parallelism is optional and must earn its cost.

**Core principle:** if ownership overlaps, convergence is vague, or one operator can finish cleanly, do not fan out.

Delegate tasks to specialized agents with isolated context. By precisely crafting their instructions and context, ensure they stay focused and succeed at their task. They should never inherit your full session context or history. Construct exactly what they need.

<HARD-GATE>
Do not dispatch parallel slices until ownership, proof, convergence order, and shutdown condition are explicit.
</HARD-GATE>

<HARD-GATE>
If the user explicitly asked for subagents, delegation, parallel evaluation, or orchestration, do not leave that decision implicit. Either run `multi-agent-orchestration` with a dispatch record or return an explicit no-fan-out decision that names why one operator remains superior.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before dispatch, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
The orchestrator keeps integration, acceptance routing, and shutdown authority. Slices may deliver evidence and bounded changes, but they do not redefine the program boundary mid-flight. Slice returns must preserve actual support files used and any deviation from dispatch.
</NON-NEGOTIABLE>

<IDENTITY-GATE>
Each dispatched sub-agent must declare its repo role identity explicitly. Do not let workers answer as the orchestrator or as an unnamed generic Codex.
</IDENTITY-GATE>

<PARALLELISM-GATE>
parallel_fan_out_requires_independent_owned_slices. Do not split the work until each slice maps to one problem domain or owned seam with no shared root-cause dependency.
</PARALLELISM-GATE>

<NON-NEGOTIABLE>
Fresh subagent per task or slice. Do not reuse stale worker context when a fresh dispatch can carry the bounded task cleanly.
</NON-NEGOTIABLE>

## Required Reads

- You MUST read `references/parallel-governance.md` before defining slices, dispatching work, or converging returns.
- You MUST start from `assets/slice-record.md` before issuing dispatch. If the fan-out is already live, also update `assets/active-slices.md`.

## Routing

```text
IF slice_count < 2:
  STOP("record no-fan-out decision in assets/slice-record.md and keep one owner")
ELSE IF shared_write_overlap = TRUE:
  STOP("record no-fan-out decision in assets/slice-record.md and keep one owner")
ELSE IF merge_strategy IS null OR acceptance_owner IS null:
  STOP("convergence contract is incomplete")
ELSE:
  ROUTE -> multi-agent-orchestration
```

## Procedure

```text
1. DECLARE(support_files := exact assets/ + references/ set OR none)
2. READ(required_assets_and_references_before_dispatch)
3. RECORD(why_each_declared_file_was_loaded)
4. DEFINE(reason_for_fan_out)
4A. RECORD(fan_out_trigger := explicit_user_request OR independent_tracks OR review_parallelism OR competing_proposals)
4B. RECORD(why_single_operator_is_insufficient)
5. CHECK(independence := file_overlap, concern_overlap, shared_root_cause_risk)
6. CHOOSE(pattern := research_fan_out OR independent_implementation OR verification_parallel OR competing_proposals)
7. REQUIRE(one_slice_per_problem_domain_when_root_causes_are_independent)
8. RECORD(each_slice IN assets/slice-record.md)
8A. RECORD(no_fan_out_decision := fan_out_trigger + why_single_operator_is_sufficient + chosen_single_owner + next_skill IN assets/slice-record.md) IF orchestration_was_considered_but_rejected
9. DISPATCH(fresh_subagent_with_precisely_curated_context_per_slice)
10. REQUIRE(two_stage_review := spec_compliance_then_code_quality) IF slice_is_implementation_work
11. TRACK(live_status IN assets/active-slices.md) IF fan_out_is_live = TRUE
12. DEFINE(acceptance_owner, integration_owner, convergence_owner, shutdown_condition IN assets/convergence-record.md) IF convergence_risk > minimal OR shutdown_decision_is_not_trivial
13. ROUTE -> quality-and-review IF convergence_is_ready_for_acceptance
14. ROUTE -> release-and-operations IF runtime_or_ship_decision_dominates
15. STOP("collapse to smaller path") IF overlap_grows OR shared_state_edits_appear OR latency_benefit_disappears OR worker_role_drift_is_not_stopped OR shared_root_cause_risk = TRUE
```

## Parallel Dispatch Pattern

Dispatch one agent per independent problem domain. Let them work concurrently.

Use when:
- multiple failures have different root causes
- multiple subsystems are broken independently
- each problem can be understood without context from others
- no shared state exists between investigations or implementations

Do not use when:
- failures are related and fixing one may fix others
- agents would edit the same seam
- full system state must be understood before acting

Each agent gets:
- specific scope
- clear goal
- exact constraints
- expected output

## Implementation Slice Review Pattern

For implementation slices:

1. Dispatch implementer with full slice text and bounded context
2. If implementer needs context, answer and re-dispatch
3. Implementer completes work, tests, and self-reviews
4. Dispatch spec compliance review first
5. Fix spec gaps and re-review until approved
6. Dispatch code quality review second
7. Fix quality issues and re-review until approved
8. Only then mark slice complete

Do not start code quality review before spec compliance is approved.

## Asset Routing

```text
IF creating_or_refreshing_one_slice_contract:
  START -> assets/slice-record.md
ELSE IF convergence_order OR acceptance_order needs explicit tracking:
  START -> assets/convergence-record.md
ELSE IF dispatch_prompt must be explicit for another owner:
  START -> assets/dispatch-handoff.md
ELSE IF fan_out_is_live:
  START -> assets/active-slices.md
ELSE IF ownership_overlap_is_the_main_risk:
  START -> assets/module-ownership.md
ELSE IF update_must_cross_role_boundaries_without_mixing_execution:
  START -> assets/mail-handoff.md
```

## Reference Routing

```text
IF dispatch_is_about_to_begin OR convergence_is_under_review:
  READ -> references/parallel-governance.md
IF merge_strategy OR shutdown_decision is disputed:
  READ -> references/convergence-rules.md
```

## Output Contract

Return an orchestration record with:

- declared support files
- files read before dispatch
- why each file was loaded
- reason for fan-out
- fan-out trigger
- why one operator is insufficient
- no-fan-out decision when orchestration was considered and rejected
- slice list
- per-slice owner, required skills, and proof
- per-slice declared identity
- per-slice fresh dispatch context
- per-slice local support paths dispatched
- per-slice local support paths actually used
- per-slice deviations from dispatch
- per-slice review stage and approval status
- merge strategy
- convergence order
- integration owner
- acceptance owner
- review path
- shutdown condition
- next skill after convergence
- files actually used
