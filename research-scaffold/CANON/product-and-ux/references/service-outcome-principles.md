# Service Outcome Principles

Service direction is about helping a user complete an outcome clearly, safely, and without avoidable dead ends.

```text
USE_THIS_REFERENCE IF
  the_main_question_is_service_clarity
  OR expectation_setting_is_weak
  OR the_flow_can_strand_users
  OR assistance_paths_are_unclear
  OR inclusive_direction_must_be_translated_into_flow_rules

CORE_RULES := PASS IF
  user_outcome_is_named_before_features_or_channels
  AND entry_points_are_findable_without_prior_domain_knowledge
  AND service_purpose_is_clear_at_entry
  AND user_and_service_expectations_are_explicit
  AND internal_org_structure_does_not_leak_into_the_user_journey_without_reason
  AND the_path_uses_the_minimum_reasonable_steps_for_the_outcome
  AND the_flow_has_no_dead_end_without_a_clear_next_action
  AND meaningful_choice_exists_when_one_path_or_one_format_would_reduce_completion_quality
  AND human_assistance_or_escalation_path_is_named_when_needed
  AND important_decisions_are_explained_with_contest_or_recovery_path_when_relevant
  AND change_in_user_circumstance_has_a_continuity_plan_when_relevant
  AND no_prior_internal_language_is_required_to_use_the_service
  AND comparable_experience_means_comparable_task_completion_not_hidden_side_routes

TRANSLATE := {
  findability -> entry_point_labels, navigation_signposts, search_or_discovery_path,
  purpose_clarity -> entry_copy, first_action, journey_name, expectation_setting,
  minimum_steps -> redundant_handoffs_removed, unnecessary_formality_removed, irreversible_friction_justified,
  no_dead_ends -> fallback_route, recovery_route, ineligible_user_outcome, blocked_state_handling,
  meaningful_choice -> alternate_path_or_format, user_control_point, fallback_format,
  assistance_path -> human_support_route, escalation_trigger, response_expectation,
  decision_explanation -> reason_given, next_step, appeal_or_recovery_route,
  no_prior_knowledge -> plain_language, jargon_reduction, clear_labels,
  comparable_experience -> same_quality_of_outcome_across_contexts_not_identical_ui,
  consistency_without_uniformity -> familiar_patterns_and_language_without_forcing_one_layout_everywhere
}

OUTPUT := {
  service_outcome,
  service_promise_or_scope,
  findability_notes,
  expectation_setting_notes,
  minimum_step_notes,
  no_dead_end_handling,
  meaningful_choice_or_alternative_path,
  assistance_path,
  decision_explanation_rules,
  no_prior_knowledge_risk,
  continuity_or_change_response_notes,
  comparable_experience_risk
}

FAIL IF
  service_is_treated_as_a_website_shell_only
  OR visual_polish_is_used_instead_of_purpose_clarity
  OR comparable_experience_is_reduced_to_accessibility_claims_without_flow_quality
  OR assistance_path_exists_only_as_a_vague_future_note
```
