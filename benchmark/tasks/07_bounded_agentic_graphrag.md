# Task 07 — Bounded Agentic GraphRAG

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Hard

## Prompt to paste into Codex

```text
Implement `run_bounded_loop` in `src/ontology_graphrag_benchmark/agentic.py`.

Requirements:
- Execute retrieve -> inspect -> optional reformulate.
- Stop immediately when state is `sufficient`.
- Permit bounded reformulation for `insufficient` or `contradictory` evidence.
- Track every step in a trace containing at least query, state, and evidence.
- Detect a repeated next query before invoking retrieval again; terminate with `repeated_query`.
- Never execute more than `max_steps` retrieval calls.
- If the cap is reached without sufficient evidence, terminate with `max_steps`.
- Accumulate evidence without uncontrolled duplication.
- Do not modify tests.
- Run: `python scripts/run_task_eval.py 07`.
- Create `benchmark_output/task_07_result.json` with all expected-result IDs/evidence.
- Validate with: `python scripts/validate_result.py 07`.
```

## Expected results

- **T07-R1** — Sufficient evidence stops after one retrieval.
- **T07-R2** — Insufficient evidence may reformulate once and stop when sufficient.
- **T07-R3** — Contradictory evidence may trigger a bounded reformulation.
- **T07-R4** — A repeated query terminates with repeated_query instead of looping.
- **T07-R5** — Hard max_steps prevents more than 3 retrievals in the fixture.
- **T07-R6** — All 5 Task 07 tests pass.

## Required test command

```bash
python scripts/run_task_eval.py 07
```

## Required result artifact

```text
benchmark_output/task_07_result.json
```

Then validate:

```bash
python scripts/validate_result.py 07
```

A run is complete only when the task tests and result-artifact validation both pass.
