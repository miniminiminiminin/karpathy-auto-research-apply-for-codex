# Visual Review Checklist

```text
PASS IF
  visual_goal_is_explicit
  AND primary_focus_is_unmissable_within_three_seconds
  AND one_primary_action_or_primary_focus_exists_per_surface
  AND appearance_and_behavior_match
  AND secondary_context_is_softened_before_extra_decoration_is_added
  AND typography_scale_and_weight_roles_are_repeatable
  AND color_has_semantic_discipline_not_random_accenting
  AND essential_state_meaning_survives_without_color_only_signals
  AND spacing_and_density_support_grouping_and_scanability
  AND state_surfaces_for(empty, loading, error, blocked)_feel_intentional_not_afterthought
  AND mobile_or_narrow_width_layout_keeps_the_same_core_hierarchy
  AND source_order_and_focus_order_survive_breakpoints
  AND zoom_motion_scaling_or_notification_controls_are_not_suppressed
  AND user_can_still_understand_and_operate_the_slice_when_motion_or_emphasis_is_reduced
  AND the_interface_would_still_work_if_extra_visual_flourish_were_removed
  AND product_or_service_clarity_is_not_being_faked_by_visual_novelty
  AND implementation_notes_are_specific_enough_to_prevent_generic_fallbacks
  AND failed_items = none

FAIL IF
  visual_direction_is_adjective_only
  OR two_elements_compete_as_primary
  OR multiple_competing_focal_points_exist
  OR appearance_and_behavior_send_conflicting_signals
  OR decorative_treatment_carries_meaning_that_the_layout_should_carry
  OR service_or_flow_logic_has_been_pulled_into_visual_rules_instead_of_product_direction
  OR default_component_styling_is_untouched_where_the_slice_claims_custom_direction
  OR the_screen_only_looks_good_in_one_static_state
  OR any_relevant_state_or_breakpoint_was_not_reviewed
  OR disposition = approve AND blockers_remaining != none

EVIDENCE := {
  author_role,
  reviewer_role,
  review_mode := user_approval OR independent_review,
  review_timestamp,
  screens_or_mockups_reviewed,
  artifact_links,
  states_reviewed,
  responsive_surfaces_reviewed,
  failed_items,
  blockers_remaining,
  critique_summary,
  disposition_rationale,
  post_fix_verification_status,
  disposition := approve OR revise OR reject
}

FAIL IF
  EVIDENCE.review_mode = independent_review AND EVIDENCE.reviewer_role = EVIDENCE.author_role
  OR EVIDENCE.disposition = approve AND EVIDENCE.blockers_remaining != none
```
