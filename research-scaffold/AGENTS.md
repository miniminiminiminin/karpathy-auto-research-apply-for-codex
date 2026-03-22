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
