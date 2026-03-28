# Skill Audit

## Audit Scope

```text
SCOPE.skill_path :=
SCOPE.reviewer :=
SCOPE.package_version :=
```

## Checks

```text
CHECK.trigger_is_sharp := TRUE AND evidence_present
CHECK.procedure_is_pseudocode := TRUE AND uses(IF OR ROUTE OR STOP)
CHECK.output_contract_is_explicit := TRUE
CHECK.local_assets_are_justified := TRUE
CHECK.hidden_dependencies_removed := TRUE
CHECK.delegated_skills_named_when_needed := TRUE
CHECK.support_file_selection_is_explicit := TRUE
CHECK.dispatch_vs_actual_usage_traceability_preserved := TRUE
CHECK.external_materials_distilled := TRUE
CHECK.logic_symbols_used_in_checklists := TRUE
CHECK.examples_or_best_code_correctly_placed := TRUE
```

## Decision

```text
DECISION.pass := ALL(CHECK.* = TRUE)
DECISION.revise := ANY(CHECK.* = FALSE)
DECISION.blockers :=
```
