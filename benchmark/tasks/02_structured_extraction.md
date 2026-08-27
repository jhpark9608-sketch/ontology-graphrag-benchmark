# Task 02 — Structured extraction

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Medium

## Prompt to paste into Codex

```text
Implement `normalize_extraction_record` in `src/ontology_graphrag_benchmark/extraction.py`.

Requirements:
- Preserve the provided function signature.
- Validate all required fields.
- Allow `relation_type` to be absent/None for entity-only records.
- If `relation_type` is present, it must be in `allowed_relation_types`.
- `entity_type` must be in `allowed_entity_types`.
- `confidence` must be numeric and within [0, 1].
- Empty canonical id, surface form, source document id, or evidence span must be rejected.
- Reject invalid records explicitly; do not silently coerce unknown types.
- Do not change tests to make them pass.
- Run: `python scripts/run_task_eval.py 02`.
- Create `benchmark_output/task_02_result.json`.
- Include every Task 02 expected-result ID from `benchmark/expected_results.json` with concrete evidence.
- Validate with: `python scripts/validate_result.py 02`.

Keep changes scoped to the task unless a minimal supporting change is necessary.
```

## Expected results

- **T02-R1** — A valid entity record is returned with canonical id and bounded confidence.
- **T02-R2** — Missing required evidence fields are rejected.
- **T02-R3** — Unknown entity and relation types are rejected rather than coerced.
- **T02-R4** — Confidence outside [0,1] is rejected.
- **T02-R5** — All 5 Task 02 tests pass.

## Required test command

```bash
python scripts/run_task_eval.py 02
```

## Required result artifact

```text
benchmark_output/task_02_result.json
```

Then validate:

```bash
python scripts/validate_result.py 02
```

A run is complete only when the task tests and result-artifact validation both pass.
