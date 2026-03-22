# Karpathy Auto-Research Concept Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a publishable concept repository with a reusable `research-scaffold/` template for purpose-driven auto-research runs.

**Architecture:** Keep the root layer focused on concept and repo maintenance, then place the executable experiment contract in `research-scaffold/`. Use text-first contracts for rubric generation, locking, logging, and execution so the repository remains understandable without custom tooling.

**Tech Stack:** Markdown, plain text templates, repository-level AGENTS contracts

---

### Task 1: Write root concept docs

**Files:**
- Create: `README.md`
- Modify: `AGENTS.md`
- Modify: `purpose.txt`
- Modify: `rubric.txt`

**Step 1: Replace the placeholder root operating guidance**

Write a root `AGENTS.md` that describes:
- root repo purpose
- root vs scaffold scope
- no run-time rubric editing
- preference for explicit templates over fake automation

**Step 2: Replace placeholder root purpose**

Write `purpose.txt` as a one-line statement of the repository's goal.

**Step 3: Replace placeholder root rubric**

Write `rubric.txt` so it evaluates the quality of the repository as a concept scaffold rather than a downstream experiment.

**Step 4: Write root README**

Document:
- repository concept
- expected scaffold flow
- current limitations
- likely future improvements

**Step 5: Review for internal consistency**

Confirm the README and root AGENTS use the same terminology for bootstrap, lock, and run.

### Task 2: Build the reusable scaffold layout

**Files:**
- Create: `research-scaffold/AGENTS.md`
- Create: `research-scaffold/README.md`
- Create: `research-scaffold/purpose.txt`
- Create: `research-scaffold/rubric-generation-prompt.md`
- Create: `research-scaffold/project/README.md`
- Create: `research-scaffold/results.tsv`
- Create: `research-scaffold/run.log`
- Create: `research-scaffold/score.log`
- Create: `research-scaffold/notes.md`

**Step 1: Write scaffold AGENTS contract**

Define:
- `purpose.txt` as required input
- one-shot `rubric.txt` generation if absent
- `rubric.txt` immutable once present
- iteration only inside `project/`
- logging requirements and keep/discard rules

**Step 2: Add scaffold README**

Explain how a downstream user should copy the scaffold, fill purpose, and start a run.

**Step 3: Add rubric generation prompt**

Specify:
- stable core rubric dimensions
- purpose-specific extension slots
- scoring style
- output shape for generated `rubric.txt`

**Step 4: Add run placeholders**

Create initial logging files and a `project/README.md` so the scaffold is self-describing before a real project is dropped in.

### Task 3: Verify tree and prepare repository for publishing

**Files:**
- Review only

**Step 1: List repository tree**

Run a file listing to confirm all expected files exist.

**Step 2: Review file contents**

Read root docs plus scaffold docs to catch terminology drift.

**Step 3: Initialize git and inspect status**

Create a new repository if needed and confirm staged/untracked files are reasonable.

**Step 4: Prepare for push**

If the user still wants publishing, add the requested GitHub remote and push after approval/escalation as needed.
