# karpathy-auto-research-apply-for-codex

A concept repository for running purpose-driven auto-research loops with Codex.

Korean README: [README.ko.md](README.ko.md)

The core idea is simple:

- write a clear `purpose.txt`
- let the agent generate a fit-for-purpose `rubric.txt`
- freeze the rubric
- run repeated improve -> execute -> score -> keep/discard loops against `project/`

This repo is not a finished product. It is a clean starting point for building and testing that workflow in a way that is inspectable, reproducible, and easy to fork.

## What Is In This Repo

- `research-scaffold/`: reusable starter layout for a single auto-research run
- `purpose.txt`: the purpose of this repository itself
- `rubric.txt`: quality rubric for this repository as a concept scaffold
- `docs/plans/`: design and implementation planning records for this repo

## Why This Shape

Most "auto-research" prompts mix three different concerns:

1. what the project is trying to achieve
2. how success is evaluated
3. how the agent iterates

This repo separates them on purpose.

- `purpose.txt` defines the objective.
- `rubric.txt` defines the scoring contract.
- `AGENTS.md` defines the operating loop.

The important constraint is that the rubric can be generated once from purpose, but it cannot be edited during the run to make the score easier to win.

## Scaffold Model

`research-scaffold/` is designed for copy-and-run usage.

Expected flow:

1. Put your target code or assets inside `research-scaffold/project/`.
2. Replace `research-scaffold/purpose.txt` with your actual goal.
3. If `research-scaffold/rubric.txt` does not exist, the agent generates it using `research-scaffold/rubric-generation-prompt.md`.
4. From that point on, `research-scaffold/rubric.txt` is treated as immutable.
5. The agent iterates on `research-scaffold/project/`, logs runs, scores outcomes, and keeps only validated improvements.

## Repository Status

This repository currently provides:

- a concept-level README
- root operating guidance
- a reusable scaffold directory
- a rubric-generation prompt
- logging templates
- a scaffold-level `AGENTS.md` for downstream experiment runs

It does not yet provide a dedicated bootstrap script or scoring engine. The current version favors explicit text contracts over opaque automation.

## Next Improvements Worth Considering

- add a small bootstrap script that creates `rubric.txt` from `purpose.txt` using the prompt contract
- add domain-specific rubric generation variants for frontend, CLI, and research workflows
- add example projects that demonstrate one full baseline-to-improvement run
- add a machine-readable results summary format next to `results.tsv`
