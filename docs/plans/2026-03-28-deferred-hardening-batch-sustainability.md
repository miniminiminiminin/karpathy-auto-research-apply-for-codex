# Deferred Hardening Batch: Sustainability Decision Hooks

## Goal

Turn sustainability from note-level recording into an actual release decision hook.

## Problem

Current release and review artifacts require `sustainability materiality` and a `decision or mitigation`, but they still allow weak handling:

- materiality can be recorded without naming what changed operationally
- mitigation can be vague
- ship can proceed without making clear whether the sustainability effect is accepted, measured-first, mitigated, or blocking

## Planned Changes

1. add a release-side sustainability decision matrix asset
2. require explicit materiality class, impact vector, horizon, and decision class
3. make `measure_before_ship` and `hold` first-class outcomes when sustainability risk is material and unproven
4. require review/release artifacts to check sustainability-decision quality, not just presence

## Acceptance Criteria

- release artifacts fail if sustainability is “material” without a named decision class
- sustainability mitigation cannot stay generic
- review can reject release posture if sustainability decision quality is weak
