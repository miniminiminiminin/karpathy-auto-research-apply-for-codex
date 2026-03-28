# Context Equivalence Matrix

```text
USE_THIS_ASSET IF
  the_review_makes_a_comparable_experience_claim
  OR the_slice_is_user_facing
  OR fallback_paths_or_alternate_flows_exist
  OR first_time_or_non_ideal_use_is_plausible

CONTEXT := {
  user_context,
  entry_path,
  environment_constraint,
  primary_path,
  alternate_or_fallback_path,
  expected_outcome,
  equivalence_expectation,
  verified_evidence,
  unresolved_gap,
  decision
}

DEFAULT_CONTEXTS_TO_CONSIDER := {
  first_time_or_low_context_user,
  interrupted_or_resume_later_user,
  non_ideal_network_or_device_context,
  keyboard_or_assistive_path_when_relevant,
  alternate_or_fallback_path_when_primary_path_is_unavailable
}

PASS IF
  relevant_contexts_are_named
  AND each_named_context_has_an_expected_outcome
  AND each_named_context_has_a_primary_or_alternate_path
  AND each_named_context_has_verified_evidence_or_explicit_gap
  AND equivalence_expectation_is_named_as_equal_outcome_or_degraded_but_acceptable_or_not_applicable_with_reason
  AND review_result_is_use_or_revise_or_block

FAIL IF
  comparable_experience_is_claimed_without_named_contexts
  OR first_time_or_non_ideal_context_is_plausible_but_not_considered
  OR fallback_path_exists_but_expected_outcome_is_unnamed
  OR equivalence_claim_is_generic
  OR unresolved_gap_is_hidden
```
