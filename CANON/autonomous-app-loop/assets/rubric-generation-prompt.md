# Rubric Generation Prompt

Canonical source for downstream scaffold bootstrap.

Use this file only when `rubric.txt` does not already exist.

Generate a `rubric.txt` from `purpose.txt` using the following contract.

## Objective

Produce a rubric that helps the loop choose changes that perform `purpose.txt` better over repeated iterations.

Assume the downstream project may be any of the following:

- a website, homepage, blog, or content product
- a web app, SaaS product, internal tool, or API-backed service
- a local or desktop application
- a game or other interactive visual software
- an automation workflow or agentic tool
- an ML project, model workflow, data product, or MLOps system
- a mixed system that spans product, operations, data, and deployment concerns

The rubric must make it hard for the planner, executor, or evaluator to game the process.

## Requirements

- The rubric must directly reflect the goal in `purpose.txt`.
- The rubric must stay stable across repeated iterations.
- The rubric must remain readable enough to consult before every iteration.
- The rubric must reward actual progress toward purpose, not only local code churn.
- The rubric must avoid vague vanity criteria that cannot be scored consistently.
- The rubric must evaluate observable outcomes that fit the project, not force the same criteria onto every project type.

## Stable Core Sections

Always include sections for:

1. Purpose fit
2. Execution clarity and reproducibility
3. Stability and error handling
4. Quality and completeness
5. Evidence, scoring, and iteration traceability

## Extension Slots

Add purpose-specific sections only when the project clearly demands them.

Examples:

- visual website, blog, or homepage: information clarity, UX, accessibility, responsiveness, visual quality, content accuracy, performance
- web app or SaaS workflow: task completion, state clarity, trust signals, responsiveness, operational reliability
- local or desktop app: installability, startup reliability, offline behavior, latency, file or device safety
- backend, API, or service: contracts, observability, reliability, operational safety, failure recovery
- game or interactive system: core loop quality, control feel, frame or interaction stability, progression clarity
- automation or agentic tooling: task completion rate, guardrails, fallback behavior, auditability, operator control
- ML model or evaluation workflow: metric quality, regression protection, dataset handling, experiment traceability, inference behavior
- MLOps or data pipeline: reproducibility, deployment safety, monitoring, rollback clarity, data freshness, cost control
- research workflow: experiment traceability, comparison quality, leverage, decision usefulness

## Measurement Guidance

Prefer dimensions that can be checked with fresh evidence from the current project.

Examples of project-fit signals:

- user or operator task success
- artifact quality or output usefulness
- correctness against examples, contracts, or datasets
- latency, throughput, stability, or crash rate
- deployability, rollback safety, or observability
- accessibility, readability, navigation clarity, or interaction quality
- cost, resource efficiency, or maintenance burden

Do not require every project to use every signal. Choose only the ones that materially reflect whether the project performs `purpose.txt` better.

## Required Scoring Contract

The rubric must define a fixed scoring structure before execution begins.

Always include:

- the score range for each section
- the weight of each section, or an explicit statement that all sections are equally weighted
- the total score formula
- the minimum promotion threshold or decision rule for keep, discard, escalate, or ship
- any hard gates that override the total score, such as failed safety, failed rollback readiness, failed critical flow, or failed reproducibility
- a consistent logging shape, including whether section weights sum to 100 and how many decimal places to use for totals

Do not leave the evaluator to invent weights or reinterpret the total score mid-run.

## Recommended Rubric Shape

Prefer a short plain-text structure like this:

```text
Section: Purpose fit
Range: 0-5
Weight: 3
Checks:
- ...

Section: Stability and error handling
Range: 0-5
Weight: 2
Checks:
- ...

Total score formula:
sum(section_score * section_weight)

Decision rule:
- keep: total score improves and no hard gate fails
- discard: total score drops or a rollback trigger fires
- escalate: score is ambiguous or a required proof path is missing
- ship: release threshold is met and ship-specific gates pass
```

The exact section names may vary, but the scoring shape must stay fixed once the run starts.

## Output Style

- Use a simple plain-text rubric.
- Make scoring dimensions explicit.
- Prefer yes/no checks or bounded score ranges over vague prose.
- Include brief guidance on how to total or summarize scores.
- Do not include any instruction that permits editing the rubric during a continuous run.

## Output Goal

Produce a rubric that is strict enough to guide convergence toward the purpose and stable enough to prevent score gaming.
