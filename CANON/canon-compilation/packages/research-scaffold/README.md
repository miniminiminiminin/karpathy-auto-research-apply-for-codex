# research-scaffold

Reusable downstream shell for a single purpose-driven project.

Treat the local `CANON/` tree as the operating law and keep the loop purpose-first, regardless of where this scaffold is materialized.

## Operating Model

The scaffold separates:

- scaffold root: control-plane state, evidence, and loop records
- `project/`: the only product change surface
- `CANON/`: local routing and execution law

Every iteration should improve the project in service of `purpose.txt`.

## Intended Flow

1. Put the actual project code, assets, or materials in `project/`.
2. Replace `purpose.txt` with the project goal.
3. If `rubric.txt` is missing, generate it once from `CANON/autonomous-app-loop/assets/rubric-generation-prompt.md`.
4. Lock `rubric.txt` for the rest of the continuous run.
5. Run `node CANON/canon-compilation/packages/research-scaffold/scripts/validate-scaffold.mjs <downstream-root>` and fix every reported gate failure before execution.
6. Use `plan.md` and `loop-status.md` to define the active slice and role boundaries.
7. If the active slice is UI-facing and `design-system/` exists, record which master file and page override the slice should consult.
8. Run planner -> executor -> evaluator -> memory loops.
9. Record each iteration in `iterations/` and summarize it in `results.tsv`.
10. Route to release only when the project is ready enough to stop iterating.

## Control-Plane Files

- `purpose.txt`: downstream project objective
- `rubric.txt`: immutable run rubric once created
- `plan.md`: current approved execution plan
- `loop-status.md`: stage, active iteration, next owner, and current blocker
- `design-system/MASTER.md`: optional global design-rule record for UI-facing projects
- `design-system/pages/<page>.md`: optional page-specific overrides that record only deviations from the master file
- `iterations/`: one file per iteration
- `results.tsv`: compact iteration history
- `run.log`: execution evidence
- `score.log`: scoring evidence
- `notes.md`: cross-iteration notes, ideas, and failure memory candidates

## Optional Design-System Persistence Contract

Use this surface only when the downstream project has a meaningful UI or UX seam that benefits from stable design guidance across iterations.

- `design-system/MASTER.md` holds cross-page defaults such as design principles, tokens, component rules, and other global decisions.
- `design-system/pages/<page>.md` holds page-level deviations from the master file and should not restate unchanged global rules.
- page overrides should explain why the page deviates, what evidence justified the deviation, and what fallback to use if the evidence is weak or later invalidated.
- retrieval order is: page override first, then `design-system/MASTER.md`, then the normal Canon routing flow for anything still undecided.
- this is a control-plane artifact, not product code and not a replacement for local `CANON/` authority.
- if the project does not need persistent design guidance, leave this surface unused and continue the normal loop.

## Validation Gate

The scaffold now ships with an executable minimum gate:

```bash
node CANON/canon-compilation/packages/research-scaffold/scripts/validate-scaffold.mjs .
```

Run it:

- after bootstrap creates `rubric.txt`
- before editing `project/` for an execution slice
- before evaluator or review claims an iteration is promotable
- before copying the scaffold into another downstream root if you changed the package templates

The validator is intentionally narrow. It checks that Canon's minimum control-plane requirements are visible:

- `rubric.txt` exists
- `loop-status.md` is not still blocked on rubric generation
- `plan.md` names the active slice, proof path, and planner/executor/evaluator owners
- iteration evidence exists once execution has started
- `run.log`, `score.log`, and `results.tsv` contain actual evidence after execution starts
- if `design-system/` exists, the optional persistence contract is structurally complete enough to use safely

## Evaluation Tools

Use the tools that already exist in the downstream project whenever possible. The scaffold does not require one fixed stack.

Common evaluation tool categories:

- unit, integration, end-to-end, contract, or regression tests
- linters, type checkers, build checks, packaging checks, and static analysis
- browser-based QA, accessibility audits, screenshots, visual diffs, and responsive checks
- API probes, smoke tests, service health checks, and load or latency measurements
- logs, traces, metrics dashboards, profiling, and crash reports
- benchmark runs, simulation runs, replay tests, or scenario scripts
- dataset-backed evaluation, offline scoring, model benchmarks, and experiment comparisons
- deployment verification, rollback drills, and post-change operational checks
- human review artifacts such as checklists, task walkthroughs, scored demos, or expert inspection notes

Pick the proof path that best reflects whether the project performs `purpose.txt` better. Different projects should use different evidence.

## Proof Path Templates

Use these as minimum viable proof bundles. Add more only when the active slice needs it.

- website, blog, or homepage:
  baseline: current screenshot or flow capture, current performance or accessibility snapshot
  candidate checks: changed-page screenshots, broken-link or content checks, responsive or accessibility pass
  promotion gate: the target flow works, no obvious visual regression, no major accessibility regression
  rollback trigger: key page breaks, content integrity drops, severe layout or navigation regression
- service, SaaS, or API-backed workflow:
  baseline: current contract behavior, critical path smoke result, relevant logs or metrics snapshot
  candidate checks: unit or integration checks, contract probes, critical user-flow or API smoke
  promotion gate: changed contract still holds, critical flow passes, no new reliability or observability blind spot
  rollback trigger: contract break, failed smoke, elevated error rate, missing telemetry on changed path
- local or desktop app:
  baseline: current install or launch result, core task walkthrough, startup or latency snapshot
  candidate checks: launch test, core flow walkthrough, packaging or file-safety verification
  promotion gate: installs or launches reliably, changed task completes, no new local data or device risk
  rollback trigger: install failure, startup regression, file corruption risk, severe local performance drop
- game or interactive system:
  baseline: current playtest notes, frame or interaction snapshot, scenario replay if available
  candidate checks: targeted playtest, deterministic scenario or replay, input or progression sanity checks
  promotion gate: changed loop feels correct, progression still works, no severe stability or control regression
  rollback trigger: core interaction breaks, progression dead-end, repeatable crash, unacceptable frame regression
- ML workflow or model evaluation:
  baseline: locked dataset split, current metrics table, current inference examples
  candidate checks: offline eval on unchanged split, regression comparison, representative output review
  promotion gate: target metric improves or holds by rule, no important regression, outputs remain usable
  rollback trigger: split drift, unexplainable metric drop, harmful output regression, irreproducible result
- MLOps, data pipeline, or deployment workflow:
  baseline: current job success rate, freshness or latency snapshot, current deployment safety checks
  candidate checks: staging run, pipeline replay, data-quality checks, rollout or rollback drill
  promotion gate: pipeline is reproducible, checks pass in staging or equivalent, rollback path is clear
  rollback trigger: data corruption risk, failed staging check, freshness regression, no safe rollback path

## Loop Adjustment Heuristics

Adjust the loop based on evidence quality, not preference.

- If the proof is weak or ambiguous, strengthen evaluation before expanding implementation scope.
- If iterations fail for unrelated reasons, reduce slice size until proof and causality are clear.
- If local metrics improve but `purpose.txt` is not better served, treat that as a slice-selection problem, not a reason to weaken the rubric.
- If the project is visual or user-facing, require proof from real flows, screens, or interactions rather than code checks alone.
- If the project is service, platform, or operations-heavy, require contract, reliability, and observability proof before keeping changes.
- If the project is ML, data, or MLOps-heavy, require stable datasets, reproducible comparisons, and regression guards before promotion.
- If evidence confidence is low, do not promote the iteration. Tighten the proof path or shrink the slice first.
- If the same blocker survives two iterations, reroute to planning, architecture, or product instead of repeating execution.
- If rollback conditions are unclear, the slice is not ready for promotion yet.
- If a slice keeps producing noise, switch the next owner from execution back to routing, product, planning, or architecture until the next bounded slice is clearer.
- If the project is ready enough to stop iterating, move to release deliberately instead of continuing the loop by habit.

Evidence confidence guide:

- low: evidence is incomplete, not reproducible, or not tied to promotion gate
- medium: evidence is mostly complete, but one major check is still weak
- high: evidence is complete, reproducible, and directly satisfies promotion gate

Promotion rule:

- do not promote with `Evidence confidence: low`
- require explicit waiver note in iteration record if promoting with `Evidence confidence: medium`
- promote with `Evidence confidence: high` by default when score and gate both pass

## Bootstrap Minimum

Before iteration 1 starts:

1. write or confirm `purpose.txt`
2. generate `rubric.txt` once from `rubric-generation-prompt.md`
3. verify the rubric has a fixed scoring shape and project-fit evidence dimensions
4. choose one bounded slice and record it in `plan.md`
5. record planner, executor, and evaluator ownership in `plan.md`
6. record a baseline proof path before changing `project/`
7. run `validate-scaffold.mjs` and resolve every bootstrap error

If rubric quality is poor at bootstrap, regenerate it before execution begins. After execution begins, do not rewrite it to rescue a weak result.

## Results Table Discipline

Keep `results.tsv` compact and comparable across iterations.

- `iteration`: zero-padded iteration id such as `000`, `001`, `002`
- `stage`: the loop stage where the decision was made
- `total_score`: the score produced by the fixed rubric formula
- `delta`: the signed change versus the previous kept baseline or previous iteration, whichever your run uses consistently
- `status`: one of `baseline`, `keep`, `discard`, `escalate`, `ship`, `crash`
- `description`: one short sentence describing the slice or decision

Choose one `delta` convention at bootstrap and do not change it mid-run.

## First Iteration Snippets

Use these snippets if you need a concrete starting point.

`plan.md` proof path snippet:

```md
- Proof path baseline: capture current state from the active flow
- Proof path candidate checks: run checks tied to the changed seam only
- Promotion gate: require gate checks plus rubric threshold
- Rollback trigger: define one clear revert condition
- Design system master: design-system/MASTER.md or not used
- Design system page override: design-system/pages/<page>.md or not used
- Page override evidence or fallback note: named or not used
- Planner owner: planner
- Executor owner: executor
- Evaluator owner: evaluator
```

`loop-status.md` update snippet:

```md
- Stage: autonomous-loop
- Active iteration: 1
- Next owner: evaluator
- Current blocker: none
- Evidence confidence: medium
- Last decision: waiting on final gate check
- Ship readiness: not assessed
```

## Important Constraint

`rubric.txt` may be created once from `purpose.txt`, but it must not be rewritten during the run to make success easier to claim.

Bootstrap authority:

- generate the rubric from the local `CANON/autonomous-app-loop/assets/rubric-generation-prompt.md`
- follow the local `CANON/autonomous-app-loop/references/bootstrap-and-rubric-lock-rules.md` when deciding whether bootstrap is complete

## What This Scaffold Does Not Promise

- It does not promise a hidden orchestrator or scoring engine.
- It does provide an executable validator for minimum Canon control-plane gates.
- It does not replace fresh review, verification, or release judgment.
- It does not allow planner, executor, and evaluator roles to collapse into untracked intuition.
