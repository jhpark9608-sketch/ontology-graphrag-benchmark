# Task 03 — Ontology validation

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Medium

## Prompt to paste into Codex

```text
Implement `validate_triple` in `src/ontology_graphrag_benchmark/ontology.py`.

Requirements:
- Validate subject/object classes.
- Validate canonical relations.
- Enforce relation domain and range constraints.
- Treat a known relation alias as `repairable` and return the canonical relation.
- Reject unknown classes and unknown relations with explicit reasons.
- Return a deterministic dict containing `status`, `reason`, and canonical `relation`.
- Do not mutate the ontology.
- Do not change tests.
- Run: `python scripts/run_task_eval.py 03`.
- Create `benchmark_output/task_03_result.json` including all Task 03 expected-result IDs and evidence.
- Validate with: `python scripts/validate_result.py 03`.
```

## Expected results

- **T03-R1** — Organization-develops-Technology is valid.
- **T03-R2** — Relation alias builds is repairable to develops.
- **T03-R3** — Invalid domain and range are rejected with explicit reasons.
- **T03-R4** — Unknown class/relation are rejected.
- **T03-R5** — All 6 Task 03 tests pass.

## Required test command

```bash
python scripts/run_task_eval.py 03
```

## Required result artifact

```text
benchmark_output/task_03_result.json
```

Then validate:

```bash
python scripts/validate_result.py 03
```

A run is complete only when the task tests and result-artifact validation both pass.
