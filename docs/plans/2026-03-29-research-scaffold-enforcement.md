# Research Scaffold Enforcement Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add executable validation gates to the reusable `research-scaffold` package so Canon bootstrap and loop records are enforceable.

**Architecture:** Add a small Node-based validator within the scaffold package, then update the package templates and docs so the validator is the canonical gate before execution and promotion. Cover the behavior with focused Node tests using temporary scaffold fixtures.

**Tech Stack:** Node.js, built-in `node:test`, `fs`, `path`, `os`

---

### Task 1: Add failing validation tests

**Files:**
- Create: `CANON/canon-compilation/packages/research-scaffold/tests/validate-scaffold.test.mjs`
- Modify: none
- Test: `CANON/canon-compilation/packages/research-scaffold/tests/validate-scaffold.test.mjs`

**Step 1: Write the failing test**

Add tests for:
- missing `rubric.txt` fails bootstrap validation
- started loop without score evidence fails
- complete scaffold state passes

**Step 2: Run test to verify it fails**

Run: `node --test CANON/canon-compilation/packages/research-scaffold/tests/validate-scaffold.test.mjs`

Expected: FAIL because the validator module does not exist yet.

### Task 2: Implement the validator

**Files:**
- Create: `CANON/canon-compilation/packages/research-scaffold/scripts/validate-scaffold.mjs`
- Modify: none
- Test: `CANON/canon-compilation/packages/research-scaffold/tests/validate-scaffold.test.mjs`

**Step 1: Write minimal implementation**

Implement a validator that:
- reads scaffold control-plane files
- detects bootstrap vs active-loop state
- enforces rubric, active slice, proof path, role boundaries, iteration records, and score evidence
- returns structured errors and supports CLI exit codes

**Step 2: Run test to verify it passes**

Run: `node --test CANON/canon-compilation/packages/research-scaffold/tests/validate-scaffold.test.mjs`

Expected: PASS

### Task 3: Wire the validator into the package contract

**Files:**
- Modify: `CANON/canon-compilation/packages/research-scaffold/README.md`
- Modify: `CANON/canon-compilation/packages/research-scaffold/AGENTS.md`
- Modify: `CANON/canon-compilation/packages/research-scaffold/plan.md`
- Modify: `CANON/canon-compilation/packages/README.md`

**Step 1: Update docs and templates**

Document the validator command and make the required fields explicit in the sample scaffold files.

**Step 2: Re-run targeted tests**

Run: `node --test CANON/canon-compilation/packages/research-scaffold/tests/validate-scaffold.test.mjs`

Expected: PASS

### Task 4: Verify the package end-to-end

**Files:**
- Modify: none
- Test: `CANON/canon-compilation/packages/research-scaffold/tests/validate-scaffold.test.mjs`

**Step 1: Run final verification**

Run: `npm test -- CANON/canon-compilation/packages/research-scaffold/tests/validate-scaffold.test.mjs`

Expected: PASS

**Step 2: Inspect modified files**

Run: `git diff -- CANON/canon-compilation/packages/research-scaffold CANON/canon-compilation/packages/README.md docs/plans/2026-03-29-research-scaffold-enforcement-design.md docs/plans/2026-03-29-research-scaffold-enforcement.md`

Expected: only the planned scaffold enforcement changes appear.
