# Platform Contracts

```text
MINIMUM_CONTRACT_RECORD := {
  owner,
  consumers,
  current_state_evidence,
  target_state_framing,
  allowed_dependency_direction,
  compatibility_expectations,
  observability_hooks,
  migration_path,
  rollback_notes,
  activation_events_and_host_entrypoints,
  command_view_or_config_ids,
  sender_receiver_ownership,
  artifact_storage_location,
  artifact_classes_readers_writers_and_lifecycle,
  failure_behavior,
  execution_model_compatibility_expectations
}

PASS IF every_field_in(MINIMUM_CONTRACT_RECORD) IS explicit_when_relevant

FAIL IF
  prompt_policy_assets_mix_with_runtime_code
  OR ui_shell_reads_or_mutates_storage_without_contract
  OR provider_service_tool_dependencies_are_implicit
  OR path_normalization_and_workspace_fallback_are_implicit
```
