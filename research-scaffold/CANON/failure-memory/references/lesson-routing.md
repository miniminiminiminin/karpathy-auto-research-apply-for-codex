# Lesson Routing

```text
START -> .codex/lessons/

IF lesson_changes_workflow THEN ROUTE -> `SKILL.md`
ELSE IF lesson_creates_repeatable_record OR lesson_creates_checklist THEN ROUTE -> `assets/`
ELSE IF lesson_needs_durable_explanation THEN ROUTE -> `references/`
ELSE IF lesson_changes_repo_wide_operating_rule THEN ROUTE -> `.codex/AGENTS.md`
ELSE STOP("keep the lesson as local capture only")

PASS IF reusable_command_path_lives_in_the_owning_skill_package
FAIL IF root_level_helper_becomes_the_authoritative_skill_contract
```
