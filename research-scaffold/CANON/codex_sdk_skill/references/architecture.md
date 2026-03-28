# Batch Patterns

Use this reference to keep execution assets separated cleanly.

```text
FOUR_LAYERS := {
  skill_engine := { vendored_sdk, initializer, preset_source_files },
  workspace_prompts := { editable_role_files, editable_stage_prompt_files },
  pipeline_contract := { ordered_stage_list, final_output_name, stage_artifact_names },
  manifest_rows := { one_row_per_output_unit }
}

LAYER_DISCIPLINE := PASS IF
  skill_engine_workspace_prompts_pipeline_contract_and_manifest_rows_stay_separate
  AND retryability_remains_clear
  AND inspection_remains_possible
  AND reuse_across_folders_remains_possible

GOOD_SHAPES := {
  one_book_chapter_pipeline + one_chapters_manifest,
  one_blog_post_pipeline + one_topics_manifest,
  one_rewrite_pipeline + one_filename_manifest
}

SPLIT_THE_JOB IF
  outputs_need_different_stage_orders
  OR outputs_need_different_shared_files
  OR outputs_need_different_acceptance_rules

NEXT_ACTION := create_another_pipeline_file_instead_of_stuffing_everything_into_one_job
```
