# Research Scaffold Enforcement Design

## Goal

Turn the reusable `research-scaffold` package from a documentation-only shell into a scaffold with executable gates for Canon bootstrap and iteration discipline.

## Problem

The current scaffold states that `rubric.txt`, planner/executor/evaluator boundaries, iteration records, and scoring evidence are required, but it does not provide an executable check that blocks invalid state. This leaves Canon compliance dependent on operator memory and narration.

## Recommended Approach

Add a small validator under `CANON/canon-compilation/packages/research-scaffold/` that inspects a scaffold instance and fails when:

- bootstrap is incomplete because `rubric.txt` is missing
- `loop-status.md` still reports a rubric bootstrap blocker
- `plan.md` has no active slice or proof path
- iteration evidence is missing after execution starts
- scoring evidence is missing after execution starts
- planner/executor/evaluator separation is undocumented in the active plan

Keep the validator intentionally narrow. It should enforce Canon’s minimum gates, not invent project-specific scoring rules.

## Chosen Shape

- Add `scripts/validate-scaffold.mjs` inside the package
- Add Node tests under `tests/` for failing and passing states
- Update package README and scaffold templates to make the validator the canonical pre-execution and pre-promotion gate
- Add role-boundary fields to `plan.md`

## Why This Approach

- Stays inside `CANON/**`, which is the owning subtree for reusable scaffold packaging
- Preserves the scaffold’s package-only model
- Makes the existing Canon rules auditable without adding a heavy runtime
- Gives downstream copies a concrete command they can run before claiming progress

## Non-Goals

- Building a hidden orchestrator
- Auto-spawning agents from the scaffold package
- Auto-generating project-specific rubric scores
- Replacing review, release, or human judgment
