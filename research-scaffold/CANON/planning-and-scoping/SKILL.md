---
name: planning-and-scoping
description: Use when an approved direction must become an execution-ready plan with one owned active step, explicit non-goals, exact proof, exact ownership, and a clean stop condition before implementation begins.
---

# Planning And Scoping

## Overview

Turn direction into a bounded execution plan.

**Core principle:** if ownership, verification, or stop conditions are vague, the plan is not ready, and implementation does not start.

Write comprehensive implementation plans assuming the engineer has zero context for our codebase and questionable taste. Document everything they need to know: which files to touch for each task, code, testing, docs they might need to check, how to test it. Give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.

Assume they are a skilled developer, but know almost nothing about our toolset or problem domain. Assume they don't know good test design very well.

Use isolated workspace setup before executing implementation plans that should not pollute the current branch or working tree.

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance the work is not yet execution-ready, you ABSOLUTELY MUST finish scoping before implementation begins.

IF PLANNING APPLIES TO THE REQUEST, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

<HARD-GATE>
Do not route work to implementation until the active step has an exact owned seam, exact owner, exact proof path, and clean stop point.

Do not let the first worker discover ownership.
Do not let proof stay implied.
Do not let multiple active steps compete for attention.
Do not start planning until the design has been presented and approved.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before scoping, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Quote the approved requirement, name the seam, name the owned files or surface, and state the non-goals. Planning is boundary control, not wishlist expansion.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
After the design, the next move is implementation planning. Do NOT invoke any other implementation skill until the direction package has been reviewed and explicitly approved.
</NON-NEGOTIABLE>

<WORKTREE-GATE>
Execution that needs isolation must use a verified isolated workspace or worktree before implementation begins.
</WORKTREE-GATE>

## Red Flags

These thoughts mean STOP: you're rationalizing.

| Thought | Reality |
|---------|---------|
| "The worker can choose exact files later" | That is missing ownership, not planning. |
| "The proof path is obvious" | If it is not written down, it is not controlled. |
| "I'll sketch several tasks now and tighten them later" | Multiple active steps hide drift and re-planning. |
| "I know the seam conceptually" | Conceptual seams without owned files or surface invite spillover. |
| "We can split while implementing" | Mid-execution decomposition is scope drift. |
| "This next step is small enough, even without a stop point" | No stop point means the step is not bounded. |
| "I can keep future-proofing in scope since we're already here" | That is wishlist expansion. Remove it. |
| "The next owner can figure out the rest from context" | Handoffs without exact proof and ownership are incomplete. |
| "The design is obvious enough to skip approval" | Planning starts only after the design is presented and approved. |

## Required Reads

- You MUST start from `assets/plan-record.md` before sequencing work. Add `assets/owned-slice.md` only when the plan hands off one bounded slice.
- You MUST read `assets/task-breakdown-stub.md` before writing bite-sized execution steps or chunked plan sections.
- You MUST read `references/step-control-rules.md` before finalizing the active step, handoff package, or cut point.
- Read `references/scope-control-rules.md` when the plan is widening, when hidden refactors appear, or when the active step feels vague.
- Read `references/dependency-risk-review.md` when blockers, approvals, or blast radius may reorder the plan.

## Workspace Isolation

Follow this priority order for isolated execution:

1. Check existing worktree directories
2. Use project preference if already established
3. Verify project-local worktree directories are ignored before use
4. Run project setup in the isolated workspace
5. Verify a clean baseline before execution

Do not proceed with execution in a dirty or unverified isolation path when the plan depends on clean separation.

## Scope Check

If the spec covers multiple independent subsystems, it should have been broken into sub-project specs during direction-setting. If it wasn't, suggest breaking this into separate plans one per subsystem. Each plan should produce working, testable software on its own.

## File Structure

Before defining tasks, map out which files will be created or modified and what each one is responsible for. This is where decomposition decisions get locked in.

- Design units with clear boundaries and well-defined interfaces. Each file should have one clear responsibility.
- You reason best about code you can hold in context at once, and your edits are more reliable when files are focused. Prefer smaller, focused files over large ones that do too much.
- Files that change together should live together. Split by responsibility, not by technical layer.
- In existing codebases, follow established patterns. If the codebase uses large files, don't unilaterally restructure, but if a file you're modifying has grown unwieldy, including a split in the plan is reasonable.

This structure informs the task decomposition. Each task should produce self-contained changes that make sense independently.

## Bite-Sized Task Granularity

**Each step is one action (2-5 minutes):**
- "Write the failing test" step
- "Run it to make sure it fails" step
- "Implement the minimal code to make the test pass" step
- "Run the tests and make sure they pass" step
- "Commit" step

## Plan Document Header

Every plan MUST start with this header:

```markdown
# [Feature Name] Implementation Plan

> **For agentic workers:** REQUIRED: Use the repo-local orchestration or execution path that owns this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## Routing

```text
IF target_outcome IS unclear:
  ROUTE -> intake-and-routing
ELSE IF design_is_not_presented_or_not_approved:
  ROUTE -> product-and-ux
ELSE IF major_technical_decision_is_still_open:
  ROUTE -> architecture-and-design
ELSE IF implementation_can_start_without_guesswork AND exact_proof_and_exact_ownership_are_visible:
  STOP("planning is complete")
ELSE:
  ROUTE -> planning-and-scoping
```

## Procedure

```text
1. DECLARE(support_files := exact assets/ + references/ set OR none)
2. READ(required_assets_and_references_before_scoping)
3. RECORD(why_each_declared_file_was_loaded)
4. LOAD(approved_requirement, source_inputs, existing_constraints)
5. REQUIRE(design_presented_and_user_approved)
6. QUOTE(source_requirement_or_decision, freshness, approval_owner)
7. DEFINE(decision_to_unlock, owned_seam, owned_files_or_surface, non_goals)
8. MAP(file_structure := created_files + modified_files + tests + responsibilities)
9. WRITE(acceptance := observable_behavior + exact_proof_path + approval_owner)
10. CHECK(blockers, dependency_risks, producer_or_consumer_blast_radius)
11. REDUCE(work) UNTIL active_step_is_one_owned_action_with_one_proof_path_and_one_clean_stop_point
12. WRITE(bite_sized_steps := one_action_per_step_with_exact_commands_and_expected_signals)
13. NAME(exact_executor, exact_verifier, exact_receiver)
14. RECORD(active_step, parked_follow_ups, handoff_target, next_skill IN assets/plan-record.md)
15. REVIEW(plan_chunks) UNTIL approved OR loop_exceeds_five_iterations
16. ROUTE -> multi-agent-orchestration IF a later parked step becomes_parallel_safe
17. STOP("re-scope the plan") IF the active step expands, loses ownership, or loses its proof path
```

## Plan Review Loop

After completing each chunk of the plan:

1. Dispatch a bounded plan reviewer with precisely crafted review context, never your full session history
2. If issues are found, fix the issues in the chunk and review it again
3. If approved, proceed to the next chunk or to execution handoff if it was the last chunk

If the loop exceeds 5 iterations, surface to the human for guidance.

## Execution Handoff

After saving the plan, route execution through the repo-local owner that matches the actual seam and execution mode. Do not jump straight from approved direction to code without this planning handoff.

If execution stays in the current session with bounded parallel slices, route to `multi-agent-orchestration`.

If execution is sequential or single-operator, follow the plan exactly:
- review the plan critically before starting
- stop when blocked instead of guessing
- follow plan steps exactly
- do not skip verifications

If isolated execution is required, set up the isolated workspace first and confirm baseline status before starting.

## Asset Routing

```text
IF writing_the_default_execution_plan:
  START -> assets/plan-record.md
ELSE IF one_slice_needs_tighter_ownership:
  START -> assets/owned-slice.md
ELSE IF acceptance_wording_is_weak:
  START -> assets/acceptance-criteria-checklist.md
ELSE IF drift_risk_is_high:
  START -> assets/scope-boundary-checklist.md
ELSE IF the_next_step_still_needs_decomposition:
  START -> assets/task-breakdown-stub.md
ELSE IF ordering_is_the_main_decision:
  START -> assets/prioritization-scorecard.md
ELSE IF work_is_experimental:
  START -> assets/experiment-brief.md
ELSE IF multiple_owners_must_see_the_current_plan_state:
  START -> assets/active-slices.md
```

## Output Contract

Return a plan record with:

- support files declared before execution
- files read before scoping
- why each file was loaded
- quoted source requirement or decision
- plan header fields
- seam, owned files or surface, and non-goals
- exact file structure and responsibilities
- exact acceptance and exact proof path
- one active step only
- bite-sized task steps with exact commands and expected signals
- parked follow-up steps or cut point
- blockers, dependencies, and clean stop point
- exact implementation owner, verification owner, and receiving owner
- next owner or next skill
- support files actually used
