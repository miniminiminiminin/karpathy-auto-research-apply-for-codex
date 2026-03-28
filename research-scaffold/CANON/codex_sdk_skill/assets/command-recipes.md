# Command Recipes

```text
SUPPORT := {
  declared_assets,
  declared_references,
  files_read_before_runtime_setup,
  why_each_file_was_loaded,
  files_actually_used
}

ASSUME engine_source = .codex/skills/codex_sdk_skill
ASSUME job_runtime = external_workspace

STEP_1 := initialize_workspace
COMMAND := python .codex/skills/codex_sdk_skill/scripts/init_workspace.py --workspace ./exports/investing-book --preset book-chapter

STEP_2 := inspect_workspace
COMMAND := find ./exports/investing-book -maxdepth 2 -type f | sort

STEP_3 := run_pipeline_direct
COMMAND := cd ./exports/investing-book && PYTHONPATH=sdk/src python scripts/run_pipeline.py --pipeline pipelines/book-chapter.json --manifest manifests/chapters.jsonl --output-dir outputs --runtime-dir runtime

STEP_4 := dry_run_pipeline
COMMAND := cd ./exports/investing-book && PYTHONPATH=sdk/src python scripts/run_pipeline.py --pipeline pipelines/book-chapter.json --manifest manifests/chapters.jsonl --dry-run

STEP_5 := use_vendored_cli
COMMAND := cd ./exports/investing-book && PYTHONPATH=sdk/src python -m codex_writer.cli.main pipeline run --pipeline pipelines/book-chapter.json --manifest manifests/chapters.jsonl

STEP_6 := start_daemon_mode
COMMAND := cd ./exports/investing-book && PYTHONPATH=sdk/src python -m codex_writer.cli.main daemon --runtime-dir runtime --socket-path runtime/daemon.sock start

STEP_7 := submit_pipeline_job_to_daemon
COMMAND := use_small_python_wrapper_when_inline_payload_is_required

STEP_8 := verify_representative_outputs
COMMAND := find outputs -maxdepth 2 -type f | sort

PASS IF
  SUPPORT.declared_assets IS named_or_none
  AND SUPPORT.declared_references IS named_or_none
  AND SUPPORT.files_read_before_runtime_setup
  AND SUPPORT.why_each_file_was_loaded

FAIL IF
  SUPPORT.files_actually_used IS missing
```
