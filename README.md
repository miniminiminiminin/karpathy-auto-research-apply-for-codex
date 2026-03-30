# karpathy-auto-research-apply-for-codex

A Codex-oriented scaffold repository for building applications through repeated planner -> executor -> evaluator loops guided by a locked purpose and rubric.

Korean README: [README.ko.md](README.ko.md)

## Credit

This repository is inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch), but it is not a port of that project. The idea here is to keep the useful loop discipline and expand it into an autonomous application-delivery scaffold.

## Core Idea

Every downstream project should optimize for one thing: perform `purpose.txt` as well as possible.

To make that operational, the scaffold separates:

- `purpose.txt`: what the project should achieve
- `rubric.txt`: how success is evaluated once the run starts
- control-plane state: the current plan, loop status, iteration history, and promotion decisions
- `project/`: the application code or assets being changed

The loop is explicit:

1. define or refine the next bounded slice in service of `purpose.txt`
2. plan that slice
3. execute only inside `project/`
4. evaluate with fresh evidence against the locked rubric
5. promote or discard the iteration
6. record memory and repeat until the release gate says the application is ready

## Repository Shape

- `CANON/`: repo-local skill system and operating law
- `CANON/skillsmith/packages/research-scaffold/`: Canon-owned reusable downstream operating shell source
- `purpose.txt`: the goal of this repository itself
- `rubric.txt`: quality rubric for this repository as a scaffold
- `docs/plans/`: design and implementation records for this repository

## Control Plane + Worktree Model

The scaffold is designed to be copied for each real project. Inside the copied scaffold:

- the scaffold root is the control plane
- `project/` is the only product change surface
- `CANON/` routes the work through intake, design, planning, autonomous delivery, review, and release

This separation matters because planner, executor, and evaluator should not disappear into one untracked blob. The loop has to be inspectable if it is going to converge on the purpose rather than merely produce activity.

## Autonomous Delivery Loop

Once the purpose is defined and the rubric is locked, the downstream project should use the loop like this:

1. `planner` chooses the next smallest valuable slice that improves `purpose.txt`
2. `executor` implements only that slice in `project/`
3. `evaluator` runs fresh proof, scores the result, and checks regressions
4. `memory` records what to repeat, avoid, or escalate
5. `release` decides whether to keep iterating or ship

The repository now adds a dedicated Canon owner for that operating lane: `autonomous-app-loop`.

## What The Canon-Owned Scaffold Package Contains

The reusable scaffold source now lives under `CANON/skillsmith/packages/research-scaffold/`.

That Canon-owned package contains:

- `purpose.txt`: downstream project objective
- `rubric-generation-prompt.md`: contract for generating `rubric.txt` once
- `plan.md`: currently approved execution plan
- `loop-status.md`: current stage, active iteration, and next owner
- `iterations/`: one record per iteration
- `results.tsv`: summary table for baseline and later iterations
- `run.log`: execution evidence
- `score.log`: scoring evidence
- `notes.md`: cross-iteration notes and ideas
- `project/`: target application

Downstream packaging should materialize this shell package together with the root `CANON/` tree. The repository no longer needs a sibling root `research-scaffold/` directory.

## Honesty Limits

This repository does not claim that a hidden runtime engine already exists.

What it provides today is:

- a clear operating contract
- a reusable scaffold layout
- Canon skills and assets for routing and loop control
- explicit state files for planning, execution, evaluation, and release

What it does not yet provide is:

- a dedicated script or daemon that runs the loop unattended
- an automatic scoring engine
- a guaranteed self-driving build pipeline

The current version favors explicit operating law over opaque automation.

## Why This Direction

The original research-loop shape was useful but incomplete for application delivery. It optimized for experimentation, not for finishing software. The new structure keeps the good discipline from purpose/rubric locking while adding:

- explicit planning and architecture gates
- separate planner/executor/evaluator roles
- promotion decisions backed by fresh evidence
- release readiness as a real terminal lane

## Next Improvements Worth Considering

- add a small bootstrap tool that generates `rubric.txt` and initializes the control-plane files
- add domain-specific rubric generation variants for frontend, backend, and agentic tool projects
- add example downstream projects that show multiple full planner/executor/evaluator iterations
- add machine-readable iteration summaries next to `results.tsv`

## UX Library CLI

This repository now includes a small CLI for collecting rendered web content or GitHub README content into Markdown under `resources/`.

### Install

```bash
npm install
```

If you want rendered page capture through Playwright, install the browser once:

```bash
npx playwright install chromium
```

### Commands

Capture a rendered page into the default `resources/` root:

```bash
ux-library capture-url https://example.com --collection smoke-test
```

Capture a GitHub repository or a local clone and split top-level sections into separate Markdown files:

```bash
ux-library capture-github https://github.com/batoreh/awesome-ux.git --collection ux/awesome-ux --split-sections
ux-library capture-github /tmp/awesome-ux --collection ux/awesome-ux --split-sections
```

### Output Shape

- default root: `resources/`
- override root: `--out <absolute-or-relative-path>`
- collection path: `resources/<collection>/`
- per-capture files:
  - `index.md`
  - `meta.json`
  - `sections/*.md` when `--split-sections` is enabled

### Initial UX Library Slice

The first curated library import lives under `resources/ux/awesome-ux/`. It was produced from the `awesome-ux` repository README after removing the table of contents and normalizing broken markdown so the remaining files are closer to a usable reference shelf than a raw repository mirror.
