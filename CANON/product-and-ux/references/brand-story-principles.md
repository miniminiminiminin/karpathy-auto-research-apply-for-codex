# Brand Story Principles

Brand guidance is useful only when it sharpens product comprehension and trust.

```text
CORE_CHECKS := {
  promise := reliable_value_the_product_claims,
  audience_fit := who_should_recognize_themselves_in_the_experience,
  tone := how_the_product_should_sound_in(normal AND stressed)_moments,
  anti_goals := what_the_brand_must_not_feel_like,
  trust_target := what_kind_of_confidence_or_reassurance_the_message_should_create,
  reasons_to_believe_mapping := how_each_claim_becomes_visible_to_users
}

REVIEW_RULES := PASS IF
  concrete_voice_traits_replace_aspirational_adjectives
  AND brand_choices_map_to(onboarding, empty_states, marketing_copy, support_language)
  AND clarity_survives(error, loading, edge_states)
  AND trust_target_and_reasons_to_believe_mapping_stay_consistent_across(product, launch, support)_contexts
  AND delight_arrives_after_orientation_is_clear

FAILURE_MODES := FAIL IF
  brand_pillars_never_change_interface_decisions
  OR tone_is_inconsistent_across_product_and_support
  OR message_trust_relies_on_style_or_polish_instead_of_visible_proof
  OR visual_storytelling_obscures_the_user_task
```
