# Research Scaffold Generalization Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make `research-scaffold` more broadly usable without changing the current control-plane model.

**Architecture:** Keep the scaffold structure unchanged and widen its guidance at the documentation layer. Expand rubric-generation guidance so project-specific rubrics can cover visual apps, local tools, games, services, automation, ML, and MLOps. Add a practical operator-facing section that lists evaluation tool categories and loop-adjustment heuristics.

**Tech Stack:** Markdown documentation, plain-text scaffold prompts

---

### Task 1: Broaden Rubric Prompt

**Files:**
- Modify: `research-scaffold/rubric-generation-prompt.md`

**Step 1: Update the scope language**

Rewrite the prompt so it clearly supports many project types, not only application categories already named in the file.

**Step 2: Add broader extension slots**

Add examples for websites, blogs, local apps, games, services, automation, ML systems, and MLOps workflows.

**Step 3: Add observable evaluation guidance**

Clarify that rubric categories should reflect measurable project outcomes such as task success, artifact quality, reliability, latency, cost, or deployment readiness depending on the project.

### Task 2: Add Operator Guidance

**Files:**
- Modify: `research-scaffold/README.md`

**Step 1: Add evaluation tool categories**

Add a section that lists the kinds of tools an operator can use for evaluation without forcing one stack.

**Step 2: Add loop-adjustment heuristics**

Add a short section explaining how to tighten, widen, or redirect the loop based on evidence quality, failure modes, and project type.

### Task 3: Verify The Wording

**Files:**
- Modify: `research-scaffold/README.md`
- Modify: `research-scaffold/rubric-generation-prompt.md`

**Step 1: Re-read both files**

Check that the scaffold still describes the same control-plane model and does not imply hidden automation.

**Step 2: Keep the wording honest**

Make sure the new guidance is framed as operator options and heuristics, not as guaranteed built-in tooling.

### Task 4: Make Proof Paths Operational

**Files:**
- Modify: `research-scaffold/README.md`
- Modify: `research-scaffold/plan.md`
- Modify: `research-scaffold/loop-status.md`
- Modify: `research-scaffold/iterations/README.md`
- Modify: `research-scaffold/project/README.md`

**Step 1: Add proof path templates**

Add small project-type examples that show what a minimum viable proof bundle looks like.

**Step 2: Structure plan and loop metadata**

Add fields for baseline, candidate checks, promotion gate, rollback trigger, and evidence confidence.

**Step 3: Strengthen iteration records**

Require reproducibility-relevant fields so future reviewers can understand what was run and under what conditions.

**Step 4: Clarify project surface wording**

Make it explicit that `project/` can hold code, assets, models, content, or other project artifacts.
