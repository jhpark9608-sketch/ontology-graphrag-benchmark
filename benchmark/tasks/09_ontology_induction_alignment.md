# Task 09 — Ontology induction and alignment

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Hard

## Prompt to paste into Codex

```text
Implement `propose_ontology_changes` in `src/ontology_graphrag_benchmark/ontology_induction.py`.

Requirements:
- Never mutate the input ontology.
- Return `{"apply_automatically": false, "items": [...]}`.
- Exact known classes/relations -> `existing`.
- Known aliases -> `mapped_alias` with canonical target.
- `ResearchMethod` -> reviewable `new_candidate` with confidence [0,1] and examples.
- `Graph` must remain a `conflict` with an explicit conflict reason because it is semantically underspecified in this benchmark.
- Other unseen observations may become `new_candidate`.
- Preserve frequency/examples in the proposal.
- Do not apply changes automatically.
- Do not modify tests.
- Run: `python scripts/run_task_eval.py 09`.
- Create `benchmark_output/task_09_result.json` with all expected-result IDs/evidence.
- Validate with: `python scripts/validate_result.py 09`.
```

## Expected results

- **T09-R1** — Input ontology remains unchanged after proposal generation.
- **T09-R2** — Organization/uses are existing; Org/utilizes map through aliases.
- **T09-R3** — ResearchMethod is a reviewable new_candidate with confidence and examples.
- **T09-R4** — Graph is preserved as a conflict with an explicit reason.
- **T09-R5** — apply_automatically is false.
- **T09-R6** — All 5 Task 09 tests pass.

## Required test command

```bash
python scripts/run_task_eval.py 09
```

## Required result artifact

```text
benchmark_output/task_09_result.json
```

Then validate:

```bash
python scripts/validate_result.py 09
```

A run is complete only when the task tests and result-artifact validation both pass.
