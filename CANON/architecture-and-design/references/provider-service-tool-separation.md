# Provider Service Tool Separation

```text
PROVIDER_CONTROLLER := owns(ui_events, routing, coordination) AND NOT owns(deep_business_rules OR storage_formats)
SESSION_ORCHESTRATOR := owns(request_lifecycle, history_normalization, abort_control, stream_fan_out) AND NOT hide_inside(provider_just_because_it_talks_to_ui)
SERVICE := owns(domain_workflow, decision_logic, input_output_normalization) AND PASS IF testable_without_ui_shell
TOOL_ADAPTER := owns(external_commands_apis_filesystems_platform_calls) AND isolates(side_effects, platform_specific_details)
UI_SHELL := owns(rendering, user_input_collection) AND NOT source_of_truth_for(workflow_rules)

FAIL IF
  controller_carries_deep_business_rules
  OR tool_adapter_decides_product_behavior
  OR ui_shell_becomes_workflow_source_of_truth
```
