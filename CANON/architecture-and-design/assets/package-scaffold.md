# Package Scaffold

```text
USE_IF new_package_or_module_root IS part_of_the_design

PACKAGE := {
  name,
  purpose,
  impact_scope,
  upstream_dependencies,
  downstream_consumers,
  extension_points,
  owned_subseams,
  split_trigger_for_large_or_multi_responsibility_units,
  split_trigger_waiver_id,
  split_trigger_waiver_owner,
  split_trigger_waiver_expiry_or_recheck_trigger,
  decision_owner,
  verification_owner,
  security_privacy_review,
  release_approval,
  rollback_owner
}

SHAPE :=
<module-root>/
├─ <manifest-or-build-file>
├─ <public-entrypoint>
└─ <implementation-root>/
   ├─ <owned-feature-a>/
   ├─ <owned-feature-b>/
   └─ <shared-leaf>

RULES := PASS IF
  public_entrypoint IS explicit
  AND split_only_when_seam_is_easier_to_own_or_replace
  AND owned_subseams_are_named_before_shared_utility_space_is_added
  AND extension_points_are_named_when_growth_is_expected
  AND a_single_file_or_class_is_not_expected_to_hold_unrelated_policy_state_and_io
  AND split_trigger_for_large_or_multi_responsibility_units IS explicit
  AND split_trigger_waiver_has_owner_and_expiry_when_present
  AND vague_filenames_are_avoided
  AND tests_mirror_the_owned_seam

FAIL IF
  public_entrypoint IS implicit
  OR split_exists_only_for_style
  OR extension_points_are_handwaved_as_future_work_without_named_surface
  OR a_god_object_is_the_default_shape
  OR split_trigger_for_large_or_multi_responsibility_units IS missing
  OR split_trigger_waiver_exists_without_owner_or_expiry
  OR filenames_hide_responsibility

split_trigger_waiver_has_owner_and_expiry_when_present := PASS IF
  split_trigger_waiver_id IS missing IMPLIES true
  AND split_trigger_waiver_id IS present IMPLIES
    split_trigger_waiver_owner
    AND split_trigger_waiver_expiry_or_recheck_trigger

NAMING := { package, folders, files }
```
