---
name: batch-production
description: Use when one prompt or transformation must run across many items from a durable workspace with manifests, retries, and resumable batch state.
---

# Batch Production

## Overview

This skill is an execution-first bulk prompt runtime. It does not stop at advice.

Default path:
1. initialize an external workspace
2. edit prompt files, pipeline JSON, manifests, and shared files there
3. run the vendored SDK from that workspace

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before workspace initialization or batch execution, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

## Use This Skill When

- one prompt or prompt pipeline must run across many rows
- chapters, posts, reports, rewrites, or configs should be driven from a manifest
- prompts should live as editable files, not inline shell strings
- stop, resume, retry, and per-item status matter
- work should happen in a folder outside `.codex`

Trigger this skill immediately when:

- the same transformation must run across many items with one shared prompt or pipeline shape
- one failed item should be retryable without rerunning the full batch
- the operator needs a real workspace, not inline ad hoc shell strings
- direct run versus daemon mode is a meaningful operational decision

## Do Not Use

- one-off single-item prompting where a normal skill or direct edit is faster
- ad hoc shell loops that do not need a durable workspace contract
- tasks that should happen inside `.codex` instead of an external workspace
- batch work where retry, manifest ownership, or prompt-file editing do not matter

## Hard Rules

- Do not write mutable job assets back into `.codex/skills/...`.
- Use the vendored SDK under `scripts/codex_writer_sdk/` as the default engine for matching tasks.
- Create or target an external workspace first.
- Treat one manifest row as one unit of work.
- Retry failed units only.

## Workspace Model

The skill package owns the engine.  
The chosen workspace owns the job.

Expected workspace layout:

```text
<workspace>/
  prompts/
  pipelines/
  manifests/
  shared/
  outputs/
  runtime/
  scripts/
  sdk/
  README.md
```

## Default Commands

Initialize:

```bash
python .codex/skills/codex_sdk_skill/scripts/init_workspace.py \
  --workspace /path/to/job-root \
  --preset book-chapter
```

Run direct:

```bash
cd /path/to/job-root
PYTHONPATH=sdk/src python scripts/run_pipeline.py \
  --pipeline pipelines/book-chapter.json \
  --manifest manifests/chapters.jsonl
```

Run daemonized work by using the same workspace and vendored CLI paths when the job is long-running.

## What Ships With The Skill

- `presets/` reusable prompt + pipeline + manifest starters
- `scripts/init_workspace.py` external workspace initializer
- `scripts/templates/run_pipeline.py` workspace runner template
- `scripts/codex_writer_sdk/` vendored runtime engine
- `assets/command-recipes.md` concrete setup and run commands

## Workflow

```text
STEP_0 := declare(support_files := exact assets/ + references/ set OR none)
STEP_0A := read(required_assets_and_references_before_runtime_setup)
STEP_0B := record(why_each_declared_file_was_loaded)
STEP_1 := pick(workspace_path)
STEP_2 := initialize(workspace_path, preset)
STEP_3 := edit(prompts, pipeline_json, manifest_jsonl, shared_context)
STEP_4 := run(pipeline)
STEP_5 := inspect(outputs, runtime_state)

IF job_needs_retryable_units THEN retry(failed_units_only)
ELSE IF interruption_matters THEN ROUTE -> daemon_mode
ELSE STOP("direct batch run is enough")
```

## Role By Phase Coverage

- operator: chooses workspace, preset, and runtime mode
- content or prompt author: edits prompt stages and shared files in the workspace
- reviewer: checks representative outputs and retryability before handoff

## Choose Assets

```text
IF default_operator_entrypoint THEN START -> assets/command-recipes.md
ELSE IF verifying_workspace_or_runtime_contract THEN SWITCH -> assets/delivery-checklist.md
ELSE IF invocation_wording_is_the_blocker THEN SWITCH -> assets/sample-usage.md
ELSE STOP("choose the asset that matches the runtime question")
```

## Choose References

```text
IF deciding(prompt_pipeline_manifest_split) THEN READ -> references/architecture.md
ELSE IF choosing(runtime_mode) THEN READ -> references/operations.md
ELSE STOP("no narrower batch-production reference matches")
```

## Choose Scripts And Presets

- use `scripts/init_workspace.py` first when the workspace does not already exist
- choose the closest preset under `presets/` before inventing a workspace layout from scratch
- treat the initialized workspace scripts and vendored SDK paths as the runtime contract for the batch job

## Output Contract

Return a batch runtime record with:

- declared support files
- files read before runtime setup
- why each file was loaded
- workspace path
- selected preset
- runtime mode chosen
- prompts, pipeline, and manifest paths
- commands executed or ready to run
- retry strategy
- verification or delivery status
- files actually used
