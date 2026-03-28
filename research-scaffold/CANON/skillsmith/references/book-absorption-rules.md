# Book Absorption Rules

```text
SOURCE_INVENTORY := PASS IF
  long_form_source_has(chapter_map OR topic_map OR section_inventory)
  AND source_inventory_is_recorded_before_slice_dispatch
  AND no_named_source_band_is_left_without_a_disposition

TEXT_EXTRACTION := PASS IF
  source_pdf_or_book_is_converted_into_working_text_before_distillation
  AND extracted_text_path_is_recorded
  AND extraction_quality_is_checked_on(table_of_contents OR representative_pages)

PAGE_IMAGE_REVIEW := USE IF
  layout_or_figure_meaning_is_lost_in_text
  OR OCR_or_text_extraction_is_ambiguous
  OR visual_examples_carry_the_actual_rule

CHAPTER_SLICING := PASS IF
  long_form_source_is_split_by_chapter_or_topic_band
  AND each_slice_has_a_named_target_skill_or_reference_seam
  AND workers_return(page_ranges_or_topic_ranges_used, target_paths, ambiguities)

OWNERSHIP_SPLIT := PASS IF
  each_slice_names(target_skill_or_reference_owner)
  AND direction_layer_and_implementation_layer_work_are_not_mixed_without_justification
  AND convergence_owner_is_named_before_target_files_change

DISTILLATION := PASS IF
  prose_is_compiled_into_rules_heuristics_and_decision_criteria
  AND chapter_examples_are_generalized_before_entering_repo_local_skills
  AND framework_specific_examples_are_kept_only_when_the_rule_survives_framework_change

COVERAGE_LEDGER := PASS IF
  each_named_source_band_is_marked_as(absorbed_now OR deferred OR excluded_as_non_durable OR needs_visual_review)
  AND absorbed_rules_name(target_paths)
  AND deferred_rules_name(next_owner_or_next_batch)
  AND visual_review_backlog_names(page_ranges_and_reason)

CONVERGENCE_CHECK := PASS IF
  declared_target_paths_do_not_cover_the_source_inventory = FALSE
  AND every_deferred_or_visual_review_item_is_visible
  AND source_wide_gap_check_runs_before_completion_claim

FAIL IF
  verbatim_book_prose_is_copied_instead_of_distilled_rules
  OR page_images_are_rendered_for_the_whole_book_without_need
  OR slicing_is_done_by_arbitrary_page_count_when_chapter_boundaries_are_available
  OR target_skill_mapping_is_left_implicit
  OR declared_target_paths_do_not_cover_the_source_inventory
  OR deferred_or_visual_review_backlog_is_hidden
```
