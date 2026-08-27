# Task 05 — Hybrid retrieval

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Medium

## Prompt to paste into Codex

```text
Implement `hybrid_retrieve` in `src/ontology_graphrag_benchmark/retrieval.py`.

Requirements:
- Normalize vector and graph score ranges independently before fusion.
- Deduplicate by `evidence_id`.
- Expose `vector_score_norm`, `graph_score_norm`, and `fused_score` in every returned item.
- Weighted fusion must use the supplied vector/graph weights.
- If one retrieval source is empty, use the other source deterministically rather than failing.
- Sort deterministically by fused score, then a stable tie-breaker.
- Respect `limit`.
- Do not modify tests.
- Run: `python scripts/run_task_eval.py 05`.
- Create `benchmark_output/task_05_result.json` with all expected-result IDs/evidence.
- Validate with: `python scripts/validate_result.py 05`.
```

## Expected results

- **T05-R1** — Vector and graph raw scores are independently normalized before fusion.
- **T05-R2** — Shared evidence e2 is deduplicated and ranked first with equal weights.
- **T05-R3** — Each result exposes normalized vector score, normalized graph score, and fused score.
- **T05-R4** — Vector-only and graph-only fallbacks are deterministic.
- **T05-R5** — All 5 Task 05 tests pass.

## Required test command

```bash
python scripts/run_task_eval.py 05
```

## Required result artifact

```text
benchmark_output/task_05_result.json
```

Then validate:

```bash
python scripts/validate_result.py 05
```

A run is complete only when the task tests and result-artifact validation both pass.
