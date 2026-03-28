---
name: failure-memory
description: Use when a failure, repeated workaround, or environment quirk should become a repo-local lesson and possibly a promoted rule, asset, or skill update.
---

# Failure Memory

## Overview

This is a self-contained execution skill for repo-local failure capture.

The package owns:

- the trigger boundary
- the lesson record shape
- the promotion checklist
- the executable commands

<HARD-GATE>
Do not leave a reusable lesson trapped only in `.codex/lessons/`.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before logging or promotion, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Use the scripts in this skill directory as the authoritative execution path. Do not rely on root-level helper scripts for normal operation.
</NON-NEGOTIABLE>

<PROMOTION-GATE>
debugging_or_verification_rule_repeated_twice_routes_to_same_session_promotion.
</PROMOTION-GATE>

## When To Use

- a command failed in a non-trivial way
- the same difficulty appeared more than once
- a tool or environment quirk changed how work had to be done
- a workaround or debugging result is likely to matter again
- a release or deployment surprise exposed a reusable operating rule

Trigger this skill immediately when:

- you are about to rely on memory for a workaround that changed future behavior
- the same failure or environment quirk appeared twice in one session
- the same debugging or verification workaround appeared twice in one session
- a fix is known, but the reusable lesson has not been recorded yet
- a review, release, or operations issue should change future operator behavior
- the same debugging workaround appeared twice and should become a rule

## Do Not Use

- routine progress updates
- product requirements or plans
- status-only notes with no lesson
- hidden rule changes that should be promoted directly into `.codex/skills/**` or `.codex/AGENTS.md`

## Hard Rules

```text
STEP_1 := record(event -> .codex/lessons/)
STEP_2 := classify(event_type := failure OR difficulty OR error)
STEP_3 := decide(reusable_lesson := TRUE OR FALSE)
STEP_4 := IF reusable_lesson = TRUE THEN name(promotion_target := skill OR asset OR reference OR rule OR none)
STEP_5 := IF lesson_changes_future_behavior THEN promote_deliberately() AND update_record()
STEP_6 := FAIL IF promotion_target_path NOT_IN .codex/lessons/records/
```

## Procedure

```text
STEP_0 := declare(support_files := exact assets/ + references/ set OR none)
STEP_0A := read(required_assets_and_references_before_logging)
STEP_0B := record(why_each_declared_file_was_loaded)
STEP_1 := summarize(event_in_one_sentence)
STEP_2 := capture(context, observed_problem, root_cause_or_hypothesis, workaround_or_fix, reusable_lesson)
STEP_3 := RUN -> scripts/log_lesson.py

IF reusable_lesson = TRUE THEN
  ROUTE -> .codex/skills/**
  OR ROUTE -> skill_local_assets_or_references
  OR ROUTE -> .codex/AGENTS.md
  OR ROUTE -> .codex/README.md

STEP_4 := RUN -> scripts/promote_lesson.py
IF reusable_lesson = FALSE THEN STOP("record complete without promotion")
```

## Activation Signals

Do not wait for a perfect postmortem. Activate the skill as soon as one of these becomes true:

- you repeated a command because the first workaround was not captured
- the same operational quirk blocked you twice in one session
- you are about to rely on memory for a workaround that changed future behavior
- review or release findings exposed a durable control or verification gap

## Role By Phase Coverage

- operator: captures the event and runs the logging command
- reviewer or lead: decides whether the lesson is reusable and where it should be promoted
- maintainer: updates the target rule, asset, or skill when promotion is warranted

## Choose Assets

- use `assets/activation-checklist.md` when deciding whether the event is strong enough to log now
- use `assets/lesson-record-template.md` when shaping the lesson fields before running the script
- use `assets/promotion-checklist.md` when the lesson likely changes future repo behavior
- use `assets/quickstart.md` when the command path or compatibility path is the main blocker

## Choose References

- use `references/lesson-routing.md` when deciding whether the lesson belongs in `SKILL.md`, `assets/`, `references/`, or `.codex/AGENTS.md`

## Choose Scripts

- use `scripts/log_lesson.py` for the initial record
- use `scripts/promote_lesson.py` only after the reusable decision and target path are explicit

## Quick Commands

```bash
python3 .codex/skills/failure-memory/scripts/log_lesson.py \
  --type error \
  --summary "codex exec panicked under sandboxed network path" \
  --context "multi-stage prompt juggling in vendored sdk" \
  --problem "codex exec disconnected after the first successful stage" \
  --cause "sandboxed network path triggered an unstable subprocess path" \
  --fix "rerun the failing command outside the sandbox" \
  --lesson "when codex exec shows a network disconnect symptom, re-run outside the sandbox and record the constraint" \
  --reusable yes \
  --promotion-target skill
```

```bash
python3 .codex/skills/failure-memory/scripts/promote_lesson.py \
  --record .codex/lessons/records/2026-03-10-example.md \
  --status promoted \
  --target-path .codex/skills/failure-memory/SKILL.md
```

If the repo root is not inferable from the script path, pass `--repo-root /path/to/repo`.

## Output Contract

Return:

- declared support files
- files read before logging or promotion
- why each file was loaded
- lesson record path
- event type
- summary
- reusable decision
- promotion target
- files actually used

## Supporting Files

- record template: `assets/lesson-record-template.md`
- promotion checklist: `assets/promotion-checklist.md`
- quickstart: `assets/quickstart.md`
- activation checklist: `assets/activation-checklist.md`
- routing notes: `references/lesson-routing.md`
- executable helpers:
  - `scripts/log_lesson.py`
  - `scripts/promote_lesson.py`

## Common Mistakes

- logging the failure but skipping the reusable decision
- reusing the same summary and assuming the new record can overwrite the old one
- promoting a lesson without updating the record
- passing a non-lesson file to `promote_lesson.py`
- keeping the lesson only in `.codex/lessons/` when it should change a skill or rule
- documenting commands that point outside the skill package
