# Canon-Owned Packages

This directory keeps Canon-owned reusable package surfaces that may later be materialized elsewhere in the repository or copied into downstream projects.

Rules:

- treat files under `CANON/skillsmith/packages/**` as editable package sources when working on reusable package behavior
- keep package-internal docs topology-agnostic enough that the same package can be copied outward without becoming misleading
- put repository-specific source-of-truth explanations in parent Canon docs rather than inside the copied package body whenever the package may also appear as a derived copy

## Materialization Contract

When materializing a downstream shell from this repository:

1. create the downstream root directory
2. copy `CANON/skillsmith/packages/research-scaffold/**` into that downstream root
3. copy the root `CANON/**` tree into `<downstream-root>/CANON/`
4. treat the materialized root as the control plane and `project/` as the product work surface
5. do not depend on any sibling root `research-scaffold/` directory in this repository

Required downstream layout:

- `<downstream-root>/purpose.txt`
- `<downstream-root>/rubric-generation-prompt.md`
- `<downstream-root>/plan.md`
- `<downstream-root>/loop-status.md`
- `<downstream-root>/iterations/**`
- `<downstream-root>/results.tsv`
- `<downstream-root>/run.log`
- `<downstream-root>/score.log`
- `<downstream-root>/notes.md`
- `<downstream-root>/project/**`
- `<downstream-root>/CANON/**`
