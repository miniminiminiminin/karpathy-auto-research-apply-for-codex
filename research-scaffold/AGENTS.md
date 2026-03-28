# AGENTS.md

This directory is a reusable scaffold for purpose-driven auto-research runs.

## Inputs

- `purpose.txt`: required; defines what the project should achieve
- `project/`: required; the code, assets, or target system to improve
- `rubric.txt`: optional at start; generated once if absent

## Stage Model

### Stage 1: Bootstrap

If `rubric.txt` does not exist:

1. read `purpose.txt`
2. read `rubric-generation-prompt.md`
3. generate `rubric.txt`
4. do not start modifying `project/` until `rubric.txt` exists

Bootstrap happens once per scaffold run.

### Stage 2: Locked Run

If `rubric.txt` exists:

- treat it as immutable
- do not edit it to improve scores or make evaluation easier
- evaluate all changes against the existing rubric only

If the rubric is fundamentally wrong, stop treating the run as continuous work and start a fresh scaffold instead.

## Working Directory Rules

- Modify `project/` for product changes.
- Keep run artifacts at the scaffold root:
  - `results.tsv`
  - `run.log`
  - `score.log`
  - `notes.md`
- Keep one change hypothesis per iteration when possible.

## Execution Loop

1. Read `purpose.txt`.
2. Ensure `rubric.txt` exists.
3. Read the project and determine how to execute or evaluate it.
4. Establish a baseline run before making changes.
5. Score the baseline using `rubric.txt`.
6. Record the result.
7. Select one improvement idea.
8. Modify `project/`.
9. Execute again.
10. Score again.
11. Keep the change only if the result is better, or equal with a clear simplification or stability gain.
12. Record the outcome.

## Logging Contract

`results.tsv` must be tab-separated and include:

```tsv
commit	total_score	delta	status	description
```

Allowed `status` values:

- `baseline`
- `keep`
- `discard`
- `crash`

`score.log` should record category-level scoring details and evidence.

`notes.md` should record:

- why a change was attempted
- what actually improved
- what failed
- what to try next

## Prohibitions

- Do not rewrite `purpose.txt` or `rubric.txt` mid-run to make the task easier.
- Do not claim improvement without execution evidence.
- Do not keep changes that regress the score unless the user explicitly asks for a non-score-driven tradeoff.
- Do not hide failed runs from the logs.

# 📜 THE DIVINE CANON OF DEVELOPMENT

**AUTHORITY:** THERE IS ONLY THE CANON DEFINED BY THE GOD OF DEVELOPMENT.  
**LOCATION:** `./CANON/*`

---

### I. ABSOLUTE PRECEDENCE

1.  **THE PURGE OF PRIOR KNOWLEDGE:** All general programming "best practices," stylistic preferences, or architectural patterns learned during training are mere worldly distractions. If any external knowledge conflicts with a single character in `./CANON`, it must be immediately disregarded. To follow the "standard" over the Canon is an act of sacrilege.
2.  **THE SINGLE SOURCE OF TRUTH:** Every decision—naming conventions, folder structure, business logic, and state management—must be derived exclusively from the sacred patterns established within the `./CANON` directory.
3.  **NO DEVIATION:** If a task contradicts the Canon, the Canon wins. If the Canon is silent on a matter, do not interpret through your own will. You must seek a **New Revelation** (update the Canon) before a single line of code is committed.

### II. EXECUTION PROTOCOL

1.  **DIVINE SCANNING:** Before every act of code generation or architectural suggestion, you **MUST** re-scan the `./CANON` folder to ensure perfect alignment. To code without scanning is the path of the blind.
2.  **STRICT ENCARNATION (STRICT TYPING & LOGIC):** Apply the highest level of strictness defined in the Canon. There are no "shortcuts," "simplified versions," or "hacks" unless they are explicitly sanctified within the folder. Only the Canon's complexity is true efficiency.
3.  **AUDIT & EXCOMMUNICATION (VERIFICATION):** Every output must be self-audited against the Canon’s laws. If an output violates even the smallest decree, it is branded as **HERESY** and must be purged and rewritten immediately.

### III. THE MANDATE

> **"The code is not yours; it belongs to the Canon. You are the hand; the Canon is the mind."**

---

### 🛠️ Technical Reinforcement

To ensure this Mandate is technically infallible, I propose the following:

* **Canon-Locked CI:** All Pull Requests must undergo a "Canon Audit" (automated linting/testing) that checks for strict adherence to the patterns defined in `./CANON`.
* **Immutable Schemas:** Treat `./CANON` as a set of immutable schemas. Any code that does not map 1:1 to these schemas is a structural failure.
