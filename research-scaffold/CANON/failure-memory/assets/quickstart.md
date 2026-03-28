# Failure Memory Quickstart

Preferred path:

1. Run `python3 .codex/skills/failure-memory/scripts/log_lesson.py ...`.
2. Inspect the emitted JSON for the created record path.
3. If the lesson is reusable, promote it with `python3 .codex/skills/failure-memory/scripts/promote_lesson.py ...`.
4. Confirm the record and `.codex/lessons/index.jsonl` show the same promotion status.

Compatibility path:

- `python3 .codex/scripts/log-lesson.py ...`
- `python3 .codex/scripts/promote-lesson.py ...`

The root-level commands are compatibility shims. The skill-local scripts remain the authoritative contract.

Use `--repo-root /path/to/repo` when invoking the scripts from a copied skill package or a non-standard working directory.
If `python` is not available on the host, use `python3`.

Example:

```bash
python3 .codex/skills/failure-memory/scripts/log_lesson.py \
  --type difficulty \
  --summary "lesson logging should stay inside the skill package" \
  --context "skill packaging cleanup" \
  --lesson "execution helpers for a skill should live in that skill directory" \
  --reusable yes \
  --promotion-target skill
```
