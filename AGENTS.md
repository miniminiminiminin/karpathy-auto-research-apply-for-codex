# Root Repository Contract

This repository owns the public concept, the reusable scaffold, and the Canon packages that downstream projects will copy.

## Root Scope

- The repository root defines the concept and the reusable operating law.
- `research-scaffold/` is the copied project shell that downstream users operate.
- Root documentation must describe the scaffold honestly and keep the purpose-first loop explicit.

## Purpose-First Rule

Every structure in this repository exists to help a downstream project perform `purpose.txt` as well as possible.

That means:

- plan quality matters only insofar as it improves purpose delivery
- implementation detail matters only insofar as it improves purpose delivery
- evaluation matters because it decides whether a change really helped the purpose
- release matters because the loop should eventually finish a useful application, not only iterate forever

## Repository Responsibilities

- keep `research-scaffold/` usable as a control-plane plus `project/` worktree shell
- keep Canon routing broad, explicit, and reusable
- separate live scaffold state from reusable Canon assets
- avoid overstating automation that is not actually implemented
- when root `CANON/` changes are intended for downstream reuse, reflect them into `research-scaffold/CANON/`
- keep deferred hardening explicit instead of claiming source-absorption closure means perfect finality

## Downstream Model

The copied scaffold should support:

1. define `purpose.txt`
2. generate `rubric.txt` once if absent
3. lock the rubric
4. route the next slice through design, planning, architecture, or direct execution as needed
5. run planner -> executor -> evaluator -> memory loops
6. promote only verified iterations
7. release when the application is ready enough

## Canon Sync Rule

- Treat root `CANON/` as the reusable upstream source of truth for scaffold shipping.
- Keep `research-scaffold/CANON/` aligned when the intent is to publish or refresh the scaffold.
- Do not claim scaffold parity if root and scaffold Canon trees have diverged.

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
