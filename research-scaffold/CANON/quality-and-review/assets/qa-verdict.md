# QA Verdict

## Summary

- summary:
- next:

## Scope

- seam:
- qa owner:
- claimed behavior:
- regression surface:
- verification target chosen and why:
- reproduction status:
- confidence:

## Evidence

- verification command:
- full verification command:
- exact output:
- screenshots or artifacts:
- stale evidence:
- proof freshness or evidence gaps:
- independent rerun:
- behavior covered:
- comparable experience covered:
- responsive survival covered:
- user control covered:
- implementation-detail dependence:
- coverage blind spots:
- flaky evidence handling:
- performance regression evidence:
- docs reviewed:
- examples exercised or inspected:
- remaining operator or user-facing risk:
- impact:
- workaround:
- environment checked:
- static validation proof:
- runtime verification proof:
- migration or reprocessing proof:
- threshold trigger reviewed:
- threshold action reviewed:
- sustainability decision reviewed when material:

## Findings

- findings:
- risks:
- open questions:

## Verdict

- pass:
- fail:
- completion claim allowed:
- failure type:
- last known good:
- root cause:
- prevention:
- blockers:
- follow-up:
- regression handoff:
- regression prevention:

PASS IF
  pass = true IMPLIES completion_claim_allowed = true
  AND pass = true IMPLIES stale_evidence IS none_or_no
  AND pass = true IMPLIES comparable_experience_covered IS explicit_or_not_applicable
  AND pass = true IMPLIES threshold_trigger_reviewed IS explicit_or_not_applicable
  AND pass = true IMPLIES threshold_action_reviewed IS explicit_or_not_applicable
  AND pass = true IMPLIES sustainability_decision_reviewed_when_material IS explicit_or_not_applicable

FAIL IF
  pass = true AND proof_freshness_or_evidence_gaps IS unresolved
  OR pass = true AND comparable_experience_covered IS missing
  OR pass = true AND threshold_trigger_reviewed IS missing
  OR pass = true AND threshold_action_reviewed IS missing
  OR pass = true AND sustainability_decision_reviewed_when_material IS missing
