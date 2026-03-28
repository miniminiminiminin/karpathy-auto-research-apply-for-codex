# Frontend Performance Guardrails

```text
AUTHORITY := {
  type := external_summary_plus_house_rule,
  primary_sources := [Core_Web_Vitals, MDN, web.dev],
  note := "Do not imply measured success when only qualitative checks were run."
}

DEFAULT_CHECKS := PASS IF
  layout_shift_from_late_loading_media_or_fonts_is_avoided
  AND progressive_enhancement_is_preferred_over_large_blocking_bundles
  AND non_critical_assets_are_lazy_loaded
  AND image_font_and_embed_loading_strategy_is_named_when_they_can_affect_cls_or_lcp
  AND interaction_latency_risk_is_named_for_the_changed_surface
  AND motion_choices_do_not_create_repaint_heavy_regressions
  AND changed_seam_has_a_bounded_no_regression_expectation

BOUNDED_EXPECTATIONS := PASS IF
  existing_baseline_is_not_regressed_without_explicit_tradeoff
  AND no_regression_claim_is_exact_when_no_numeric_baseline_exists
  AND numeric_claims_reference_named_metrics_or_tooling_when_numbers_are_used
  AND performance_note_is_tied_to_one_user_visible_surface
  AND proof_is_narrow_not_global

PROOF := {
  performance_sensitive_surfaces_changed,
  evidence_checked,
  metrics_used_if_any,
  tradeoff_if_regression_is_accepted
}
```
