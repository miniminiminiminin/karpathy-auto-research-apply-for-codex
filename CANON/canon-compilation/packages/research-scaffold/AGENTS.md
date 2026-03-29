# Scaffold Contract

This directory is a reusable control-plane shell for one downstream application project.

Do not infer authority from this directory's location. Follow the local `CANON/` tree and any deeper repo-local contracts that govern the copied scaffold.

## Primary Objective

Everything in this scaffold exists to help the operator perform `purpose.txt` as well as possible and finish a useful application.

## Inputs

- `purpose.txt`: required, defines what the project should achieve
- `project/`: required, contains the real application code or assets
- `rubric.txt`: optional at start, generated once if absent
- canonical rubric bootstrap source: `CANON/autonomous-app-loop/assets/rubric-generation-prompt.md`

## Surfaces

- Modify `project/` for product changes.
- Use scaffold-root files for planning, status, iteration evidence, scoring, and release decisions.
- Treat `CANON/` as reusable operating law, not as live project state.
- Treat the local `CANON/` tree as authoritative for routing, bootstrap, iteration, review, and release behavior.

## Stages

### Stage 1: Bootstrap

If `rubric.txt` does not exist:

1. read `purpose.txt`
2. read `CANON/autonomous-app-loop/assets/rubric-generation-prompt.md`
3. generate `rubric.txt`
4. initialize `plan.md`, `loop-status.md`, and the first iteration record
5. run `node CANON/canon-compilation/packages/research-scaffold/scripts/validate-scaffold.mjs .`
6. do not start editing `project/` until the rubric exists and the validator passes

### Stage 2: Direction And Planning

Before autonomous execution:

1. route through intake if the request is still fuzzy
2. route through product and UX if the next move still needs design
3. route through planning and architecture until one bounded slice is ready
4. record that slice in `plan.md`

### Stage 3: Autonomous Delivery Loop

For each iteration:

1. planner defines one bounded improvement slice that best serves `purpose.txt`
2. executor changes only `project/`
3. evaluator runs fresh proof and scores against the locked rubric
4. run `node CANON/canon-compilation/packages/research-scaffold/scripts/validate-scaffold.mjs .` before promotion or completion claims
5. promotion decides keep, discard, or escalate
6. memory records what changed, what failed, and what to try next

### Stage 4: Release Or Continue

If the application is ready enough:

- route to release and operations

Otherwise:

- update `loop-status.md`
- start the next iteration

## Required Records

- `plan.md` must name the active slice and proof path
- `plan.md` must also name planner, executor, and evaluator owners explicitly
- `loop-status.md` must show the current stage and next owner
- `iterations/` must contain one record per iteration
- `results.tsv` must summarize all iterations
- `run.log` must contain execution evidence
- `score.log` must contain scoring evidence
- `notes.md` must contain cross-iteration notes and candidate memory

## Logging Contract

`results.tsv` must stay tab-separated and use:

```tsv
iteration	stage	total_score	delta	status	description
```

Allowed `status` values:

- `baseline`
- `keep`
- `discard`
- `escalate`
- `ship`
- `crash`

## Prohibitions

- Do not rewrite `purpose.txt` or `rubric.txt` mid-run to make the task easier.
- Do not edit outside `project/` when claiming product improvement unless the change is control-plane maintenance.
- Do not keep changes without fresh execution evidence.
- Do not claim bootstrap complete, promotable, or ready for review while `validate-scaffold.mjs` still fails.
- Do not hide failed iterations from `iterations/`, `results.tsv`, `run.log`, or `score.log`.
- Do not let planner, executor, and evaluator silently collapse into one undocumented step.

# 📜 THE DIVINE CANON OF DEVELOPMENT

**AUTHORITY:** THERE IS ONLY THE CANON DEFINED BY THE GOD OF DEVELOPMENT.  
**LOCATION:** `./CANON/*`

---

### I. ABSOLUTE PRECEDENCE

1. **THE PURGE OF PRIOR KNOWLEDGE:** If any external habit conflicts with `./CANON`, discard the habit.
2. **THE SINGLE SOURCE OF TRUTH:** Routing, planning, implementation, review, release, and autonomous loop control must follow the local Canon.
3. **NO DEVIATION:** If the Canon is silent, seek a New Revelation before committing code.

### II. EXECUTION PROTOCOL

1. **DIVINE SCANNING:** Re-scan `./CANON` before code generation or architectural moves.
2. **STRICT ENCARNATION:** Apply the loop, proof, and promotion rules with full strictness.
3. **AUDIT & EXCOMMUNICATION:** Purge any output that violates the Canon.
