# Autonomous App Loop Design

## Goal

Turn this repository from a purpose-driven auto-research concept into a reusable Codex scaffold for autonomous application delivery, where a copied `research-scaffold/` directory acts as the control plane for repeated planner -> executor -> evaluator -> memory loops over a real `project/`.

## Design Summary

The repository keeps two layers:

- root layer: owns the public concept, Canon, and reusable scaffold contract
- `research-scaffold/` layer: is the downstream operating shell that users copy and run for a specific application

The downstream scaffold separates:

- `project/`: the only product change surface
- scaffold root control-plane files: purpose, rubric, live status, plans, evaluations, and iteration records
- `CANON/`: the local operating law for routing, planning, implementation, review, release, and autonomous loop control

## Core Operating Model

Each downstream project follows this loop:

1. bootstrap the project objective and create `rubric.txt` once if missing
2. use intake, product, planning, and architecture skills to shape the next owned slice
3. run an autonomous delivery loop:
   - planner defines the next bounded iteration
   - executor changes only `project/`
   - evaluator runs fresh proof and scores against the locked rubric
   - memory records what should be retried, promoted, or avoided
4. promote only verified improvements into the next iteration state
5. repeat until the release gate says the application is ready to ship

## Key Decision

Adopt a control-plane plus worktree model instead of a single undifferentiated run directory.

The scaffold should explicitly separate:

- objective and evaluation contract
- planning and architecture records
- iteration-by-iteration delivery evidence
- the actual application under `project/`

This makes the autonomous loop inspectable and prevents planner, executor, and evaluator responsibilities from collapsing into one hidden blob.

## New Canon Responsibility

Add a broad top-level Canon owner for the autonomous delivery loop. This skill should:

- decide when the loop can start
- define the planner, executor, and evaluator contract for one iteration
- require fresh proof before promotion
- write loop state and convergence notes
- route to existing Canon owners when the next problem is really intake, design, planning, implementation, review, or release

The new skill does not replace the existing catalog. It sits above implementation and below planning as the owner of repeated autonomous delivery once the direction is approved and the next slice is operable.

## Scaffold Contract Changes

`research-scaffold/` should become a live project operating shell with explicit state files:

- `purpose.txt`: project objective
- `rubric.txt`: immutable evaluation contract once created
- `plan.md`: currently approved execution plan
- `loop-status.md`: current stage, active iteration, and next owner
- `iterations/`: one file per iteration with plan, proof, score delta, and promotion decision
- `results.tsv`: tab-separated summary for all iterations
- `notes.md`: cross-iteration operator notes and future ideas
- `project/`: actual application source tree

## Why This Design

- It matches the Canon emphasis on explicit ownership, proof, and routing.
- It makes downstream projects easier to manage because the control plane and work surface are separate.
- It supports repeated planner/executor/evaluator loops without pretending a hidden orchestration engine exists.
- It keeps the repo honest: the automation contract is documented, but the human or Codex still runs the loop explicitly.

## Alternatives Considered

### 1. Keep the current research-only loop

Rejected because it is too weak for application delivery and does not give the planner/evaluator enough independent structure.

### 2. Let a single agent own planning, coding, and scoring without state files

Rejected because it collapses auditability and makes promotion decisions hard to inspect or repeat.

### 3. Full script-driven orchestration now

Rejected for now because the repository does not yet provide a trustworthy runtime engine, and claiming one would overstate the current implementation.

## Risks

- If the scaffold adds too many narrow skills, the catalog becomes harder to route.
- If the loop state files overlap with Canon assets, users may not know which files are templates and which are live records.
- If the repo claims autonomous completion without fresh proof gates, the system will drift into self-approval.

## Guardrails

- Keep the new loop owner broad and route to existing skills when a narrower owner exists.
- Distinguish Canon reusable assets from scaffold live records.
- Keep `rubric.txt` immutable during a continuous run.
- Require promotion decisions to cite fresh execution evidence and score movement.

## Planned Outputs

- revised root docs and purpose/rubric
- revised root and scaffold `AGENTS.md`
- revised scaffold README and live-state files
- new `autonomous-app-loop` Canon package in both root and scaffold Canon trees
- Canon catalog updates describing the new operating order
