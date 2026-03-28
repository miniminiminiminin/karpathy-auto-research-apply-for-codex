# CANON Self-Sufficiency And Scaffold Internalization Plan

> **For agentic workers:** REQUIRED: Use the repo-local owner that matches each bounded seam. Treat `CANON/**` as the source of truth and only mirror outward after the owning Canon change is accepted.

**Goal:** Make `CANON` self-sufficient as the primary operating law, internalize the reusable downstream scaffold under Canon ownership, and remove the need for a sibling root `research-scaffold/` tree.

**Architecture:** Move scaffold-source authority under `CANON`, strengthen root and Canon AGENTS contracts so the skill system can route, orchestrate, and bootstrap without depending on an external scaffold explanation, and absorb rubric bootstrap rules into Canon-owned assets. Downstream consumers should materialize the shell from `CANON/skillsmith/packages/research-scaffold/` together with the root `CANON/` tree instead of relying on a sibling root scaffold directory.

**Tech Stack:** Markdown contracts, Canon skill packages, repo documentation, file-tree synchronization.

---

## Problem Statement

The repository currently has strong owner packages, but the reusable downstream shell still exists as a sibling source tree outside Canon. That leaves three weaknesses:

1. `CANON` is not yet the sole place an operator can read to understand bootstrap, rubric locking, and scaffold-copy logic.
2. the repository still carries legacy assumptions that a sibling root scaffold directory is part of the source model.
3. Orchestration and subagent use are documented, but not yet framed as part of a Canon-owned self-sufficient operating system that can stand without scaffold-side explanation.

## Desired End State

- `CANON/**` alone is sufficient to explain routing, bootstrap, rubric locking, orchestration, execution, evaluation, and release.
- The reusable downstream scaffold lives under Canon-owned paths and can be copied outward when a downstream consumer wants a materialized tree.
- Root docs and AGENTS state clearly that the Canon-owned package is the only source model required in-repo.
- Rubric bootstrap rules and scaffold bootstrap assets are owned inside Canon rather than depending on root-only explanation.

## Design Decisions

### 1. Canon-Owns-The-Scaffold Rule

The reusable scaffold package should live under `CANON/skillsmith/` as a Canon-owned package artifact rather than as a sibling conceptual source tree. `skillsmith` already owns repo-wide Canon maintenance, packaging, and owner-boundary work.

### 2. Package-Only Rule

The repository does not need a sibling root scaffold directory once the Canon-owned package is established. Materialized copies may exist outside the repository or be generated on demand.

### 3. Rubric Bootstrap Internalization

Rubric generation and rubric lock rules should be rooted in `CANON/autonomous-app-loop/**` and related Canon documentation so that bootstrap is part of the operating law rather than an external scaffold instruction.

### 4. Orchestration Self-Sufficiency

`intake-and-routing`, `multi-agent-orchestration`, and `autonomous-app-loop` should be described in the repository and AGENTS contracts as sufficient to decide when subagents are required, not merely available.

## Bounded Execution Seams

### Seam A: Contract And Documentation Shift

Owned files:
- `AGENTS.md`
- `CANON/AGENTS.md`
- `README.md`
- `CANON/README.md`

Purpose:
- state that Canon is the primary operating source
- state that the Canon-owned scaffold package is the reusable shell source and that no sibling root scaffold tree is required
- state that rubric/bootstrap/orchestration rules must be legible from Canon without scaffold-side explanation

### Seam B: Canon-Owned Scaffold Package

Owned files or surfaces:
- `CANON/skillsmith/**` for package-location and packaging rules
- new Canon-owned scaffold package path containing the reusable scaffold source

Purpose:
- internalize the scaffold package under Canon ownership
- keep a bounded copy source for downstream shell materialization

### Seam C: Rubric Bootstrap Internalization

Owned files or surfaces:
- `CANON/autonomous-app-loop/**`
- Canon-owned scaffold package bootstrap files

Purpose:
- make rubric bootstrap, lock, and baseline-proof rules Canon-owned

## Non-Goals

- Do not build a hidden automation daemon.
- Do not invent a new top-level Canon owner unless an existing owner cannot absorb the rule.
- Do not silently change downstream semantics of the scaffold without documenting the source-of-truth shift.
- Do not rewrite product-direction or implementation rules unrelated to Canon self-sufficiency.

## Acceptance

The work is acceptable when:

1. Root and Canon AGENTS state that Canon is self-sufficient and package-first.
2. The reusable scaffold source exists under a Canon-owned path.
3. Rubric bootstrap and lock rules are described in Canon-owned files.
4. The repository no longer depends on a sibling root scaffold directory for any operator-facing authority.
5. Parallel subagent review confirms the source-of-truth model, owner boundaries, and bootstrap/orchestration story are coherent.

## Proof Path

- Read-path proof: verify all changed docs agree on source-of-truth and bootstrap ownership.
- File-path proof: verify the Canon-owned scaffold package exists and that no root sibling scaffold directory is required for operator guidance.
- Review proof: run parallel subagent reviews focused on owner boundaries, bootstrap coherence, and orchestration self-sufficiency.

## Active Step

Create the Canon-first contract and package path, then remove the need for a sibling root scaffold copy.

## Parked Follow-Ups

- harden `intake-and-routing`, `multi-agent-orchestration`, and `autonomous-app-loop` further if review still finds orchestration ambiguity
- decide later whether a small copy script belongs inside `CANON/skillsmith/scripts/`
