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
- actual behavior checked:
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
  AND next_owner IS explicit

FAIL IF
  files_actually_used ARE missing
  OR fresh_command_run_in_this_session IS not_yes
