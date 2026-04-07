# Design System Page Overrides

Create one file per page only when that page needs rules that differ from `design-system/MASTER.md`.

- keep each file limited to the deviations for that page
- prefer reusing the master file over creating override files
- record why the page deviates, what evidence justified the deviation, and what to fall back to if that evidence is weak, stale, or later contradicted
- prefer evidence-derived recommendations over style adjectives or page-type folklore
- do not use page override files to bypass local `CANON/` routing, proof, or review rules

Suggested shape:

```md
# <Page Name>

- page purpose:
- why this page deviates from `design-system/MASTER.md`:
- evidence source:
- confidence or freshness:
- fallback if evidence is weak:

## Override Rules

- <rule that differs from the master>
```
