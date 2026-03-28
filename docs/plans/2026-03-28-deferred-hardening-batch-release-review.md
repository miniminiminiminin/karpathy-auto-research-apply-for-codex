# Deferred Hardening Batch: Release + Review

## Goal

Close the two highest-value deferred items left by the principles absorption program:

1. stricter iterate-with-data thresholds and post-launch trigger rules
2. broader context-for-everyone matrices covering first-time users, non-ideal environments, and alternate-path equivalence

## Why This Batch

These two gaps still allow a weak form of completion language:

- release can name monitoring without turning it into a decision matrix
- review can claim comparable experience without naming which user contexts and fallback paths were actually checked

Both reduce Canon's self-sufficiency because the operator still has to improvise what counts as enough.

## Planned Changes

1. strengthen `CANON/release-and-operations/**`
   - add a signal threshold matrix asset
   - require explicit signal, threshold shape, comparison window, and action owner
   - make iterate-with-data mean measured follow-up triggers, not generic monitoring prose
2. strengthen `CANON/quality-and-review/**`
   - add a context equivalence matrix asset
   - require review to name first-time, interrupted, low-capability, and alternate-path contexts when relevant
   - require explicit equivalence or non-equivalence rationale instead of generic “comparable experience checked”

## Acceptance Criteria

- release artifacts fail if threshold entries are generic or cannot drive a post-launch decision
- review artifacts fail if comparable-experience claims do not name relevant contexts and fallback routes
- root Canon and the Canon-owned scaffold package model stay in sync
- subagent review reports no remaining blocker in these two hardening areas
