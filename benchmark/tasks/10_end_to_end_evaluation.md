# Task 10 — End-to-end evaluation

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Hard

## Prompt to paste into Codex

```text
Implement `evaluate_examples` in `src/ontology_graphrag_benchmark/evaluation.py`.

Compute:
- retrieval_recall = sum(retrieved_relevant) / sum(relevant_total)
- graph_path_validity = valid / available, excluding rows where graph_path_valid is None
- ontology_violation_rate = number of examples with ontology_violations > 0 divided by all examples
- provenance_coverage = sum(claims_grounded) / sum(claims_total)
- mean_latency_ms
- total_tokens
- failure_breakdown counts

Requirements:
- Handle empty denominators safely.
- Keep failure categories separate.
- Return deterministic machine-readable metrics.
- Do not modify tests.
- Run: `python scripts/run_task_eval.py 10`.
- Create `benchmark_output/task_10_result.json` with all expected-result IDs/evidence.
- Validate with: `python scripts/validate_result.py 10`.
```

## Expected results

- **T10-R1** — retrieval_recall = 0.75.
- **T10-R2** — graph_path_validity = 2/3, excluding None.
- **T10-R3** — ontology_violation_rate = 0.25.
- **T10-R4** — provenance_coverage = 0.75.
- **T10-R5** — mean_latency_ms = 150 and total_tokens = 1000.
- **T10-R6** — failure_breakdown = {success:2,retrieval:1,reasoning:1}.
- **T10-R7** — All 6 Task 10 tests pass.

## Required test command

```bash
python scripts/run_task_eval.py 10
```

## Required result artifact

```text
benchmark_output/task_10_result.json
```

Then validate:

```bash
python scripts/validate_result.py 10
```

A run is complete only when the task tests and result-artifact validation both pass.
