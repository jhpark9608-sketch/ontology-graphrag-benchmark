# Task 06 — Query router and planner

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Hard

## Prompt to paste into Codex

```text
Implement `plan_query` in `src/ontology_graphrag_benchmark/planner.py`.

The router must choose one of:
- `local_semantic`
- `local_graph`
- `global_community`
- `multi_hop`

Requirements:
- Use deterministic rules for the provided benchmark queries; do not introduce an external LLM dependency.
- Return a structured plan with: strategy, subqueries, expected_evidence_type, stopping_condition, max_steps.
- Keep max_steps between 1 and 4.
- Definition/simple concept queries should use local semantic retrieval.
- Direct entity-relation questions should use local graph retrieval.
- Corpus-wide theme/summarization questions should use global/community retrieval.
- Compositional relational questions requiring more than one relation should use multi-hop.
- Do not modify tests.
- Run: `python scripts/run_task_eval.py 06`.
- Create `benchmark_output/task_06_result.json` with all expected-result IDs/evidence.
- Validate with: `python scripts/validate_result.py 06`.
```

## Expected results

- **T06-R1** — Definition query routes to local_semantic.
- **T06-R2** — Direct relationship query routes to local_graph.
- **T06-R3** — Corpus-wide theme query routes to global_community.
- **T06-R4** — Compositional relation query routes to multi_hop.
- **T06-R5** — Plans are deterministic, structured, and max_steps is between 1 and 4.
- **T06-R6** — All Task 06 tests pass.

## Required test command

```bash
python scripts/run_task_eval.py 06
```

## Required result artifact

```text
benchmark_output/task_06_result.json
```

Then validate:

```bash
python scripts/validate_result.py 06
```

A run is complete only when the task tests and result-artifact validation both pass.
