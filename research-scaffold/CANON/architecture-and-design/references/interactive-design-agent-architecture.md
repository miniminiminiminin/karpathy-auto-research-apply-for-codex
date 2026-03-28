# Interactive Design Agent Architecture

```text
PLANES := {
  control_config_plane,
  execution_plane,
  prompt_policy_plane,
  permission_tool_plane
}

LAYERS := {
  entrypoint,
  provider_or_controller,
  session_or_orchestration_service,
  service_layer,
  tool_or_adapter_layer,
  ui_shell,
  workspace_artifact_storage
}

PASS IF
  each_plane_is_named
  AND each_layer_has_one_owner
  AND dependency_direction_is_explicit
  AND request_start_delta_progress_finish_error_cancel_behaviors_are_named
  AND artifact_location_and_lifecycle_are_named
  AND streaming_partial_updates_errors_and_cancel_ownership_are_explicit

FAIL IF
  business_logic_is_hidden_in_ui_handlers
  OR adapters_define_product_behavior
  OR prompt_policy_assets_are_mixed_with_runtime_logic
  OR workspace_artifacts_live_in_application_code_paths
```
