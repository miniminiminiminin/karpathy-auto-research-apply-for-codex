# AGENTS.md

This repository is a concept and scaffold repo for purpose-driven auto-research loops inspired by Karpathy-style iterative improvement.

## Scope

- The repository root defines the concept, rationale, and reusable scaffold.
- `research-scaffold/` is the executable template that downstream users copy or adapt.
- Do not treat the repository root itself as an experiment target unless the user explicitly asks for that.

## Operating Priorities

1. Preserve the repository's role as a reusable starter, not a one-off run directory.
2. Keep the contract between `purpose.txt`, rubric generation, and execution explicit.
3. Prefer simple, inspectable text files over hidden automation.
4. Document stage boundaries clearly: bootstrap, lock, run.

## Root Expectations

- `README.md` must explain the concept, why the scaffold exists, and how to use it.
- Root `purpose.txt` describes the goal of this repository itself.
- Root `rubric.txt` evaluates this repository as a concept scaffold, not a downstream experiment.
- Design and implementation planning docs belong in `docs/plans/`.

## Scaffold Expectations

- `research-scaffold/AGENTS.md` is the authority for actual experiment runs.
- The scaffold must support this path:
  1. user writes `purpose.txt`
  2. agent generates `rubric.txt` once
  3. agent treats `rubric.txt` as immutable
  4. agent improves `project/` through repeated execution and scoring
- If the scaffold contract changes, update the scaffold docs and examples together.

## Safety Rules

- Do not silently blur bootstrap-time rubric creation with run-time rubric editing.
- Do not claim a fully automated system exists unless the files present actually support the claim.
- Prefer templates, prompts, and contracts over fake implementation promises.
