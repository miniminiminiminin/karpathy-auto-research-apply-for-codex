# research-scaffold

Reusable starter for a single purpose-driven auto-research run.

## Intended Flow

1. Put your target code or materials inside `project/`.
2. Replace `purpose.txt` with a real objective.
3. If `rubric.txt` is missing, let the agent generate it from `rubric-generation-prompt.md`.
4. Lock the rubric.
5. Iterate on `project/` while logging runs and scores.

## Important Constraint

`rubric.txt` may be created once from `purpose.txt`, but it must not be edited during the run to manipulate the evaluation.

## Files

- `purpose.txt`: objective for this specific run
- `rubric-generation-prompt.md`: how to derive the initial rubric
- `project/`: target work area
- `results.tsv`: run summary table
- `run.log`: raw execution output
- `score.log`: scoring evidence
- `notes.md`: experiment notes
