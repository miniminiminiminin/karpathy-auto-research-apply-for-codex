# iterations

Store one Markdown file per iteration in this directory.

Suggested filename:

- `000-baseline.md`
- `001-first-improvement.md`
- `002-contract-fix.md`

Each iteration record should capture:

- why this slice was chosen
- what changed in `project/`
- what proof was run
- what the baseline was before the change
- what promotion gate was used
- what rollback trigger would force discard or revert
- how the rubric score moved
- whether the iteration was kept, discarded, escalated, or shipped

Recommended extra fields when reproducibility matters:

- dataset, corpus, or content snapshot identifier
- scenario, replay, or prompt set identifier
- configuration, model, or feature-flag version
- seed, environment, platform, hardware, or runtime details
- build, package, or artifact identifier
- links or paths to logs, screenshots, traces, metrics, or eval tables

Quick record skeleton:

```md
# Iteration NNN: short-title

## Slice Choice
- why this slice was chosen:

## Change Summary
- what changed in `project/`:

## Proof
- baseline:
- candidate checks:
- promotion gate:
- rollback trigger:

## Evidence Metadata
- dataset or content snapshot:
- config or model version:
- seed or environment:
- artifact or build id:
- evidence paths:

## Scoring And Decision
- total score:
- delta from prior iteration:
- status: keep | discard | escalate | ship
- evidence confidence: low | medium | high
```
