# UX Review

## Flow

- task flow:
- entry state:
- exit state:
- service purpose clarity:
- entry-point findability:
- expectation-setting clarity:
- minimum-step discipline:
- no-dead-end or blocked-user outcome:
- meaningful choice or alternative path:
- assistance or escalation path:
- decision explanation points:
- no-prior-knowledge language risk:
- continuity across channel or changed circumstance:
- critical decision points:
- primary objects and destinations:
- information architecture model:
- information hierarchy:
- navigation or wayfinding model:
- collection or drilldown pattern:
- layout or disclosure pattern:
- responsive breakpoints or surfaces:
- responsive priority:
- navigation behavior across widths:
- state behavior on narrow screens:
- edge states:

## Review

- current evidence basis:
- evidence strength:
- limitations:
- segment scope:
- friction points:
- clarity risks:
- comparable experience risks:
- signposts and current-location cues:
- recognition versus recall support:
- safe exploration and reversibility:
- interruption or resume support:
- accessibility risks:
- accessibility text implications:
- translation readiness risks:
- design-system consistency risks:
- mobile-first behavior risks:
- keyboard or focus behavior:
- screen-reader or announcement behavior:
- spacing or density risks:
- actionability or affordance risks:
- list, data, or form pattern fit:
- smart-surface or system implications:
- option comparison:
- assistive tech notes:
- evidence gaps:
- stale or weak signals:
- unresolved uncertainty:
- feasibility notes:

## Decision

- approved:
- changes required:
- rationale:
- measurable approval criteria:
- approval criteria:
- success criteria at risk:
- next owner:

PASS IF
  approved = true IMPLIES changes_required IS none_or_empty
  AND approved = true IMPLIES evidence_gaps IS none_or_empty
  AND approved = true IMPLIES stale_or_weak_signals IS none_or_empty
  AND approved = true IMPLIES unresolved_uncertainty IS none_or_empty

FAIL IF
  approved = true AND no-dead-end_or_blocked-user_outcome IS missing
  OR approved = true AND assistance_or_escalation_path IS missing_when_needed
  OR approved = true AND comparable_experience_risks IS unresolved
