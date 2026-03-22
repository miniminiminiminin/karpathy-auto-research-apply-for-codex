# Rubric Generation Prompt

Use this file only when `rubric.txt` does not already exist.

Generate a `rubric.txt` from `purpose.txt` using the following contract.

## Requirements

- The rubric must reflect the goal in `purpose.txt`.
- The rubric must stay evaluable through repeated runs.
- The rubric must avoid vague vanity criteria that are hard to score consistently.
- The rubric must preserve a stable core shared across most projects.
- The rubric must be concise enough to read before every run.

## Stable Core Sections

Always include sections for:

1. Purpose fit
2. Reproducibility and execution clarity
3. Stability and error handling
4. Quality and completeness
5. Logging and documentation of results

## Extension Slots

Add purpose-specific sections only when the goal clearly demands them.

Examples:

- frontend: UX, accessibility, visual consistency, performance
- CLI/tooling: flags, output clarity, recovery from bad input
- research workflow: experiment traceability, comparison quality, automation leverage
- content system: factual structure, consistency, editability

## Output Style

- Use a simple plain-text rubric.
- Make scoring dimensions explicit.
- Prefer yes/no checks or bounded score ranges over vague prose.
- Include brief guidance on how to total or summarize scores.
- Do not include instructions that permit editing the rubric during the run.

## Output Goal

Produce a rubric that is strict enough to guide improvement and stable enough to prevent score gaming.
