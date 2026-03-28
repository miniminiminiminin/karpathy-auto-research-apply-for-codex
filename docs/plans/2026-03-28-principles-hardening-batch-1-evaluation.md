# principles.adactio Deferred Hardening Batch 1 Evaluation Criteria

## Batch Scope

- owner 1: `CANON/release-and-operations/**`
- owner 2: `CANON/quality-and-review/**`
- goal:
  - turn deferred iterate-with-data rules into explicit threshold and follow-up gates
  - turn sustainability from note-only capture into an operating decision hook when material
  - keep release focused on ship/hold/monitor decisions and keep review focused on evidence and acceptance discipline

## Pass Criteria

### 1. Owner Boundary

PASS IF
- `release-and-operations` owns threshold-triggered rollout, monitoring, mitigation, rollback, and sustainability-decision posture
- `quality-and-review` owns whether threshold evidence and sustainability decision notes are sufficient to support completion claims
- review does not become release management
- release does not become implementation redesign

FAIL IF
- release templates prescribe product or implementation redesign
- review templates start deciding rollout strategy instead of checking its evidence

### 2. Principle Fidelity

PASS IF
- “design with data” becomes explicit threshold, signal review time, and action-trigger recording
- “iterate” becomes a named follow-up loop with measurable trigger or decision threshold
- sustainability becomes a routing or decision consequence when the note is materially risky, not a decorative field
- openness remains explicit through evidence source, uncertainty, and threshold rationale

FAIL IF
- thresholds remain hand-wavy placeholders
- sustainability remains note-only even when marked material

### 3. Operator Usability

PASS IF
- a release operator can tell when monitoring-only is no longer enough and a trigger forces mitigation or rollback
- a reviewer can fail a release claim when thresholds, trigger logic, or material sustainability handling are missing
- assets ask for fields that real release work can fill

FAIL IF
- operators can still pass with only generic “monitor closely” language
- “material sustainability” has no explicit consequence

### 4. Reviewability

PASS IF
- release and review artifacts can reject missing threshold triggers, stale signal loops, and unresolved material sustainability risk
- completion cannot be claimed when follow-up cadence is implicit

FAIL IF
- threshold or sustainability gaps are still narrative-only concerns

## Required Review Outputs

- verdict: `pass`, `pass_with_revisions`, or `block`
- findings ordered by severity
- owner-boundary issues
- operator-ambiguity issues
- deferred coverage still missing after this hardening pass
