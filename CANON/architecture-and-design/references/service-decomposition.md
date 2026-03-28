# Service Decomposition

```text
PASS IF split_reduces_hidden_coupling
  AND contract_is_clear_between_producer_and_consumer
  AND lifecycle_failure_mode_or_scaling_needs_are_meaningfully_different
  AND current_state_evidence_shows_the_split_improves_replaceability

FAIL IF split_only_renames_layers
  OR shared_state_chatter_remains_constant
  OR ownership_boundary_is_not_meaningful
  OR complexity_is_added_only_for_style

IF runtime_is_interactive THEN CHECK(
  workspace_event_entrypoint,
  provider_or_controller,
  session_orchestration_service,
  domain_service,
  tool_adapter_wrappers,
  webview_or_client_shell,
  workspace_local_artifact_storage,
  workflow_nodes_and_typed_edges
)
```
