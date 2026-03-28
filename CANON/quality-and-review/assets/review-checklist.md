# Review Checklist

## Slice

- declared assets:
- declared references:
- files read before review:
- why each file was loaded:
- files actually used:
- name:
- commit:
- owner:
- decision owner:
- verification owner:
- impact scope:
- upstream dependencies:
- downstream dependencies:
- seam summary:
- receiver:

## Reviews

- spec review complete:
- code-quality review complete:
- security/privacy review complete:

## Findings

- blocking:
- non-blocking:
- remaining uncertainty:

## Verification

- command:
- fresh_command_run_in_this_session:
- result:
- feedback_item_verified_against_codebase_reality:
- proof freshness or evidence gaps:
- stale evidence:
- actual behavior checked:
- comparable experience checked:
- responsive survival checked when relevant:
- user control checked when relevant:
- threshold trigger checked when release_or_monitoring_claim_exists:
- sustainability decision checked when material:
- docs or examples checked:
- examples exercised or only inspected:
- approvals verified:
- rollback owner named:
- release approval required:

## Decision

- approved:
- approved with follow-up:
- rejected:
- release escalation:
- required fixes:
- follow-up cleanup:
- next owner:

PASS IF
  declared_assets ARE named_or_none
  AND declared_references ARE named_or_none
  AND files_read_before_review ARE explicit
  AND why_each_file_was_loaded IS explicit
  AND fresh_command_run_in_this_session = yes
  AND stale_evidence IS none_or_no
  AND comparable_experience_checked IS explicit_or_not_applicable
  AND responsive_survival_checked_when_relevant IS explicit_or_not_applicable
  AND user_control_checked_when_relevant IS explicit_or_not_applicable
  AND threshold_trigger_checked_when_release_or_monitoring_claim_exists IS explicit_or_not_applicable
  AND sustainability_decision_checked_when_material IS explicit_or_not_applicable
  AND next_owner IS explicit

FAIL IF
  files_actually_used ARE missing
  OR stale_evidence IS yes_or_unknown
  OR comparable_experience_checked IS missing
  OR responsive_survival_checked_when_relevant IS missing
  OR user_control_checked_when_relevant IS missing
  OR threshold_trigger_checked_when_release_or_monitoring_claim_exists IS missing
  OR sustainability_decision_checked_when_material IS missing
  OR fresh_command_run_in_this_session IS not_yes
