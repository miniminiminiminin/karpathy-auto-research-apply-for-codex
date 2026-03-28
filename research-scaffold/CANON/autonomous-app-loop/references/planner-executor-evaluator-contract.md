# Planner Executor Evaluator Contract

- planner chooses the slice and proof path
- executor implements the slice and does not redefine success
- evaluator judges the result with fresh evidence and does not excuse missing proof
- if any role has to invent missing scope, route back instead of guessing
