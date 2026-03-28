# Autonomous App Loop Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reframe the repository and scaffold around an autonomous planner -> executor -> evaluator delivery loop with explicit control-plane state and Canon support.

**Architecture:** Keep the repository root as the concept and Canon owner, then make `research-scaffold/` the copied project control plane. Add one new broad Canon skill for the autonomous delivery loop, update the root and scaffold documentation to route work into it, and add scaffold live-state records that make each iteration inspectable.

**Tech Stack:** Markdown, plain text templates, repo-local AGENTS contracts, Canon skill packages

---

### Task 1: Reframe root repository docs

**Files:**
- Modify: `README.md`
- Modify: `README.ko.md`
- Modify: `purpose.txt`
- Modify: `rubric.txt`
- Modify: `AGENTS.md`

**Step 1: Rewrite root purpose and rubric**

Describe the repository as a reusable autonomous application delivery scaffold and update the rubric to score control-plane clarity, loop rigor, and scaffold reusability.

**Step 2: Rewrite the root READMEs**

Explain:
- the control-plane plus worktree model
- the planner/executor/evaluator loop
- how `research-scaffold/` is copied and used
- current honesty limits

**Step 3: Update root AGENTS contract**

Make the root repo rules explicit about:
- root versus scaffold scope
- Canon precedence
- no hidden automation claims
- control-plane ownership

### Task 2: Rebuild the scaffold as a downstream project shell

**Files:**
- Modify: `research-scaffold/README.md`
- Modify: `research-scaffold/AGENTS.md`
- Modify: `research-scaffold/project/README.md`
- Modify: `research-scaffold/purpose.txt`
- Create: `research-scaffold/plan.md`
- Create: `research-scaffold/loop-status.md`
- Create: `research-scaffold/iterations/README.md`
- Modify: `research-scaffold/notes.md`
- Modify: `research-scaffold/results.tsv`
- Modify: `research-scaffold/run.log`
- Modify: `research-scaffold/score.log`

**Step 1: Define scaffold operating stages**

Describe bootstrap, design and planning, autonomous delivery loop, and release completion.

**Step 2: Add live control-plane files**

Create `plan.md`, `loop-status.md`, and an `iterations/` area for per-iteration evidence.

**Step 3: Tighten project boundary wording**

Make clear that product edits belong in `project/` and the scaffold root is for loop state and evidence only.

### Task 3: Add a new Canon owner for the autonomous loop

**Files:**
- Create: `CANON/autonomous-app-loop/SKILL.md`
- Create: `CANON/autonomous-app-loop/agents/orchestrator.md`
- Create: `CANON/autonomous-app-loop/agents/planner.md`
- Create: `CANON/autonomous-app-loop/agents/executor.md`
- Create: `CANON/autonomous-app-loop/agents/evaluator.md`
- Create: `CANON/autonomous-app-loop/agents/openai.yaml`
- Create: `CANON/autonomous-app-loop/assets/project-state.md`
- Create: `CANON/autonomous-app-loop/assets/iteration-brief.md`
- Create: `CANON/autonomous-app-loop/assets/evaluation-report.md`
- Create: `CANON/autonomous-app-loop/assets/promotion-decision.md`
- Create: `CANON/autonomous-app-loop/assets/loop-record.md`
- Create: `CANON/autonomous-app-loop/references/control-plane-and-worktree-separation.md`
- Create: `CANON/autonomous-app-loop/references/planner-executor-evaluator-contract.md`
- Create: `CANON/autonomous-app-loop/references/loop-convergence-rules.md`
- Create: `CANON/autonomous-app-loop/references/autonomous-delivery-guardrails.md`

**Step 1: Write the new skill**

Define when the loop starts, how one iteration is bounded, when to route back out to existing Canon owners, and what proof is required before promotion.

**Step 2: Add role prompts**

Separate orchestrator, planner, executor, and evaluator responsibilities.

**Step 3: Add reusable assets and references**

Give the new skill templates and guardrails for loop state, iteration brief, evaluation, and promotion.

### Task 4: Mirror the new Canon owner into the scaffold and update the catalog

**Files:**
- Modify: `CANON/README.md`
- Create: `research-scaffold/CANON/autonomous-app-loop/...`
- Modify: `research-scaffold/CANON/README.md`

**Step 1: Update both Canon catalogs**

Add the new skill to the catalog and insert it into the operating order between planning and implementation/release where appropriate.

**Step 2: Mirror the new skill package into the scaffold Canon**

Ensure copied downstream projects carry the same loop owner locally.

### Task 5: Verify the reshaped repository

**Files:**
- Review only

**Step 1: Read the updated docs**

Confirm terminology is consistent across root docs, scaffold docs, and the new Canon package.

**Step 2: List the new files**

Confirm all expected control-plane and Canon files exist.

**Step 3: Check git status**

Verify the repo only contains the intended changes.
