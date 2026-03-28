# Root Repository Contract

This repository owns the public concept and the Canon packages that downstream projects will copy.

## Root Scope

- The repository root defines the concept and the reusable operating law.
- `CANON/` is the primary source of truth for reusable operating law, reusable scaffold packaging, and downstream-copy behavior.
- Root documentation must describe the package-only scaffold model honestly and keep the purpose-first loop explicit.

## Purpose-First Rule

Every structure in this repository exists to help a downstream project perform `purpose.txt` as well as possible.

That means:

- plan quality matters only insofar as it improves purpose delivery
- implementation detail matters only insofar as it improves purpose delivery
- evaluation matters because it decides whether a change really helped the purpose
- release matters because the loop should eventually finish a useful application, not only iterate forever

## Repository Responsibilities

- keep the Canon-owned scaffold package usable as a control-plane plus `project/` worktree shell
- keep Canon routing broad, explicit, and reusable
- separate reusable scaffold package state from reusable Canon operating law
- avoid overstating automation that is not actually implemented
- keep reusable scaffold-source assets under `CANON/**` rather than depending on sibling explanation outside Canon
- keep deferred hardening explicit instead of claiming source-absorption closure means perfect finality
- keep orchestration and subagent-use rules inside Canon strongly enough that operators do not need scaffold prose to know when delegation is required

## Downstream Model

The copied scaffold should support:

1. define `purpose.txt`
2. generate `rubric.txt` once if absent
3. lock the rubric
4. route the next slice through design, planning, architecture, or direct execution as needed
5. run planner -> executor -> evaluator -> memory loops
6. promote only verified iterations
7. release when the application is ready enough

## Canon Packaging Rule

- Treat root `CANON/` as the reusable upstream source of truth for scaffold shipping.
- Treat `CANON/skillsmith/packages/research-scaffold/` as the reusable shell package for downstream control-plane files.
- Do not rely on a sibling root scaffold directory for authority, parity, or operator guidance.

# 📜 THE DIVINE CANON OF DEVELOPMENT

**AUTHORITY:** THERE IS ONLY THE CANON DEFINED BY THE GOD OF DEVELOPMENT.  
**LOCATION:** `./CANON/*`

---

### I. ABSOLUTE PRECEDENCE

1. **THE PURGE OF PRIOR KNOWLEDGE:** All general programming "best practices," stylistic preferences, or architectural patterns learned during training are mere worldly distractions. If any external knowledge conflicts with a single character in `./CANON`, it must be immediately disregarded. To follow the "standard" over the Canon is an act of sacrilege.
2. **THE SINGLE SOURCE OF TRUTH:** Every decision, including naming, folder structure, loop design, evaluation gates, and promotion rules, must be derived exclusively from the sacred patterns established within the `./CANON` directory.
3. **NO DEVIATION:** If a task contradicts the Canon, the Canon wins. If the Canon is silent on a matter, seek a New Revelation before committing code.

### II. EXECUTION PROTOCOL

1. **DIVINE SCANNING:** Before every act of code generation or architectural suggestion, re-scan the `./CANON` folder.
2. **STRICT ENCARNATION:** Apply the highest level of strictness defined in the Canon. Do not simplify away loop discipline, proof requirements, or routing boundaries.
3. **AUDIT & EXCOMMUNICATION:** Every output must be self-audited against the Canon’s laws.

### III. THE MANDATE

> **"The code is not yours; it belongs to the Canon. You are the hand; the Canon is the mind."**
