# Frontend Performance Guardrails

```text
DEFAULT_CHECKS := PASS IF
  layout_shift_from_late_loading_media_or_fonts_is_avoided
  AND progressive_enhancement_is_preferred_over_large_blocking_bundles
  AND non_critical_assets_are_lazy_loaded
  AND interaction_latency_stays_acceptable_on_slower_devices
  AND motion_choices_do_not_create_repaint_heavy_regressions
  AND changed_seam_has_a_bounded_no_regression_expectation

BOUNDED_EXPECTATIONS := PASS IF
  existing_baseline_is_not_regressed_without_explicit_tradeoff
  AND no_regression_claim_is_exact_when_no_numeric_baseline_exists
  AND performance_note_is_tied_to_one_user_visible_surface
  AND proof_is_narrow_not_global

PROOF := {
  performance_sensitive_surfaces_changed,
  evidence_checked,
  tradeoff_if_regression_is_accepted
}
```
