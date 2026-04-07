# Scaffold Design System Persistence Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a reusable design-system persistence contract to the `research-scaffold` package so downstream projects can store global design rules in `design-system/MASTER.md` and optional page-specific overrides in `design-system/pages/`.

**Architecture:** Keep the first absorption seam narrow. Document the persistence surface in the scaffold package, ship the empty package structure so downstream copies have a stable location, and enforce only the minimum validator rule needed to prevent orphaned page overrides without a master file.

**Tech Stack:** Markdown package docs, Node.js validator script, Node.js test runner

---

### Task 1: Record the package contract

**Files:**
- Modify: `CANON/canon-compilation/packages/research-scaffold/README.md`
- Modify: `CANON/canon-compilation/packages/research-scaffold/AGENTS.md`
- Create: `CANON/canon-compilation/packages/research-scaffold/design-system/MASTER.md`
- Create: `CANON/canon-compilation/packages/research-scaffold/design-system/pages/README.md`

**Step 1: Add the new scaffold surface to package docs**

- Describe `design-system/MASTER.md` as the global design rule source of truth.
- Describe `design-system/pages/<page>.md` as optional overrides that only record deviations from the master file.
- State that this surface is control-plane guidance for product work, not a replacement for Canon routing or proof.

**Step 2: Add package templates**

- Ship a starter `design-system/MASTER.md` file with placeholder guidance.
- Ship a `design-system/pages/README.md` file that explains when page override files should and should not exist.

**Step 3: Tighten operator guidance**

- Update `AGENTS.md` so operators know to consult the master file and page overrides when they exist, but not to treat them as authority above local `CANON/`.

### Task 2: Add the minimum validator gate

**Files:**
- Modify: `CANON/canon-compilation/packages/research-scaffold/scripts/validate-scaffold.mjs`
- Test: `CANON/canon-compilation/packages/research-scaffold/tests/validate-scaffold.test.mjs`

**Step 1: Write the failing tests**

- Add a test that fails when `design-system/pages/*.md` exists without `design-system/MASTER.md`.
- Add a test that passes when both the master file and an override file exist.

**Step 2: Implement the validator rule**

- Keep the rule narrow: only enforce `MASTER.md` when page override files are present.
- Do not require the design-system surface for every scaffold yet.

**Step 3: Re-run the package tests**

- Use the scaffold validator test file as the proof path for this seam.

### Task 3: Verify and capture the Canon absorption result

**Files:**
- Modify: `docs/plans/2026-03-29-ui-ux-pro-max-skill-transfer-brief.md`

**Step 1: Update the transfer brief**

- Record that the first promoted seam is the scaffold persistence contract.
- Note what was intentionally not imported from the upstream source.

**Step 2: Run focused verification**

- Run the validator package tests.
- Optionally run the validator against the scaffold package root to confirm the new files do not create regressions.

**Step 3: Summarize completion**

- Report the exact package surface added, the validator behavior added, and the remaining deferred seams.
