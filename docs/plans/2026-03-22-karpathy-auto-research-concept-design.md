# Karpathy Auto-Research Concept Design

## Goal

Turn this repository into a publishable concept repo that explains and packages a reusable "purpose -> generated rubric -> locked evaluation -> iterative improvement" workflow for Codex.

## Design Summary

The repository is split into two layers:

- root layer: explains the concept and governs maintenance of the scaffold itself
- `research-scaffold/` layer: provides a reusable run template for downstream experiments

The scaffold uses a two-stage model:

1. bootstrap stage
   - read `purpose.txt`
   - generate `rubric.txt` once
2. run stage
   - treat `rubric.txt` as immutable
   - modify only `project/`
   - execute, score, log, and keep only validated improvements

## Key Decision

Use a minimum-core plus extension-slot rubric model.

The generated rubric should always include shared evaluation dimensions such as:

- purpose fit
- reproducibility
- stability
- quality/completeness
- documentation and experiment logging

Then it can append purpose-specific sections for domains like frontend, CLI, or research workflows.

## Why This Design

- It keeps the core contract stable across projects.
- It avoids the main failure mode of self-serving rubric drift during execution.
- It is lightweight enough for a public concept repo.
- It keeps the system inspectable by relying on plain text instead of hidden orchestration.

## Planned Outputs

- root `README.md`
- updated root `AGENTS.md`
- root `purpose.txt`
- root `rubric.txt`
- `research-scaffold/AGENTS.md`
- `research-scaffold/README.md`
- `research-scaffold/purpose.txt`
- `research-scaffold/rubric-generation-prompt.md`
- `research-scaffold/project/README.md`
- logging templates for results and notes

## Risks

- If `rubric.txt` ships inside the scaffold by default, the bootstrap step becomes ambiguous.
- If the repo claims full automation without scripts, it will over-promise.
- If the root and scaffold rules differ, users will not know which operating contract matters.

## Guardrails

- Do not include a pre-generated `research-scaffold/rubric.txt`.
- State plainly that rubric generation is contract-defined but not yet script-backed.
- Keep stage boundaries explicit in both README and scaffold `AGENTS.md`.
