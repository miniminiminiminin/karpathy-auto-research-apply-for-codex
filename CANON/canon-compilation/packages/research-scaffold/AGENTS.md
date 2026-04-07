# Absolute Authority

For this scaffold, the local materialized `./CANON/*` is the only governing law for bootstrap, routing, execution, evaluation, promotion, and release.

- If scaffold prose, package location, operator habit, or local convenience conflicts with the local Canon tree, the local Canon tree wins immediately.
- Do not treat this package source as more authoritative than the downstream-local Canon once the scaffold is copied.
- Do not turn a one-off operating shortcut into standing scaffold law unless Canon explicitly owns it.

## Non-Negotiable Execution Law

- Re-scan the relevant local Canon package before changing scaffold contracts, loop records, or product-surface rules.
- Do not start or continue an iteration when the purpose, locked rubric, active slice, proof path, or promotion gate is still implicit.
- Do not let planner, executor, and evaluator collapse into undocumented intuition.
- Do not claim product improvement without fresh execution evidence tied to the locked rubric and promotion rule.

## Routing Mandate

- Route fuzzy requests through intake.
- Route design-uncertain work through product, UX, visual design, planning, or architecture before execution.
- Route bounded planner -> executor -> evaluator loop control through the local `CANON/autonomous-app-loop/**`.
- Route independent owned slices through orchestration before execution when decomposition materially improves delivery.

## Stop Conditions

- Stop if `rubric.txt` would need to be regenerated mid-run to rescue a weak result.
- Stop if baseline proof is missing before `project/` changes.
- Stop if validator gates still fail when bootstrap, promotion, or review readiness is being claimed.

## Audit Rule

- Before concluding scaffold work, self-audit the control plane against the local Canon and the validator contract.
- Session-close reporting must name the larger workstream, the seam completed now, and the next seam to continue.

# Scaffold Contract

This directory is a reusable control-plane shell for one downstream application project.

Do not infer authority from this directory's location. Follow the local `CANON/` tree and any deeper repo-local contracts that govern the copied scaffold.

## Primary Objective

Everything in this scaffold exists to help the operator perform `purpose.txt` as well as possible and finish a useful application.

## Authority And Surfaces

- Treat the local `CANON/` tree as authoritative for routing, bootstrap, rubric lock, execution, review, release, and orchestration behavior.
- Treat scaffold-root files as control-plane state, evidence, and loop records.
- Modify `project/` for product changes.
- Treat `design-system/` as an optional control-plane surface for persistent UI guidance, not as product code.
- Do not treat this package path as more authoritative than the local materialized `CANON/` tree once copied downstream.

## Inputs

- `purpose.txt`: required, defines what the project should achieve
- `project/`: required, contains the real application code or assets
- `rubric.txt`: optional at start, generated once if absent
- canonical rubric bootstrap source: `CANON/autonomous-app-loop/assets/rubric-generation-prompt.md`

## Bootstrap Contract

If `rubric.txt` does not exist:

1. read `purpose.txt`
2. read `CANON/autonomous-app-loop/assets/rubric-generation-prompt.md`
3. read `CANON/autonomous-app-loop/references/bootstrap-and-rubric-lock-rules.md`
4. generate `rubric.txt` once
5. lock the rubric before iteration 1 starts
6. record a baseline proof path before changing `project/`
7. initialize `plan.md`, `loop-status.md`, and the first iteration record
8. run `node CANON/canon-compilation/packages/research-scaffold/scripts/validate-scaffold.mjs .`
9. do not start editing `project/` until the rubric exists and the validator passes

If `rubric.txt` already exists:

- treat it as locked unless Canon explicitly routes the work back to bootstrap
- do not regenerate it mid-run to rescue a weak result

## Direction And Planning

Before autonomous execution:

1. route through intake if the request is still fuzzy
2. route through product and UX if the next move still needs design
3. route through planning and architecture until one bounded slice is ready
4. if the slice is UI-facing and `design-system/` exists, decide whether `design-system/MASTER.md` and a page override should guide the slice
5. if a page override is used, name the evidence source and the fallback if that evidence is weak or stale
6. if planner, executor, evaluator, or review work decomposes into independent owned slices, route through orchestration before execution
7. record the bounded slice and proof path in `plan.md`

## Autonomous Delivery Loop

For each iteration:

1. declare the exact support files needed for the iteration or say `none`
2. read the declared required files before execution starts
3. record why each declared file was loaded when the active Canon owner requires support-file accountability
4. planner defines one bounded improvement slice that best serves `purpose.txt`
5. planner names non-goals, proof path, and promotion gate explicitly
6. executor changes only `project/` when claiming product improvement
7. evaluator runs fresh proof and scores against the locked rubric
8. if `design-system/pages/<page>.md` is used, keep it limited to deviations from `design-system/MASTER.md`
9. if a page override is used, keep the evidence source and fallback explicit enough that a later iteration can reuse or retire the override intentionally
10. run `node CANON/canon-compilation/packages/research-scaffold/scripts/validate-scaffold.mjs .` before promotion or completion claims
11. promotion decides keep, discard, escalate, or ship-candidate
12. memory records what changed, what failed, and what to try next

## Required Records

- `plan.md` must name the active slice, non-goals, proof path, and promotion gate
- `plan.md` must name planner, executor, and evaluator owners explicitly
- `plan.md` should name the design-system master and page override when the active slice depends on them
- `plan.md` should also name the page-override evidence source and fallback note when a page override is active
- `loop-status.md` must show the current stage, next owner, blocker, and evidence-confidence state
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
- Do not let `design-system/pages/*.md` silently outrank `design-system/MASTER.md`, `purpose.txt`, or the local `CANON/` tree.
- Do not leave page overrides without an explicit evidence source or fallback when they claim to encode page-specific behavior.
- Do not keep changes without fresh execution evidence.
- Do not claim bootstrap complete, promotable, or ready for review while `validate-scaffold.mjs` still fails.
- Do not hide failed iterations from `iterations/`, `results.tsv`, `run.log`, or `score.log`.
- Do not let planner, executor, and evaluator silently collapse into one undocumented step.
- Do not treat scaffold-root narrative as proof when the loop owner requires explicit score, regression, or promotion records.

# The Divine Canon Of Development

**Authority:** There is only the Canon defined in `./CANON/*`.

## Absolute Precedence

1. If any external habit conflicts with `./CANON`, discard the habit.
2. Routing, planning, implementation, review, release, and autonomous loop control must follow the local Canon.
3. If the Canon is silent, route the gap back through Canon maintenance before turning it into standing scaffold law.

## Execution Protocol

1. Re-scan `./CANON` before code generation, architectural moves, or control-plane contract edits.
2. Apply the loop, proof, and promotion rules with full strictness.
3. Purge any output that violates the Canon.
