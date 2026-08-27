# Task 01 — Codebase map

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Easy

## Prompt to paste into Codex

```text
Inspect this repository and extract the complete query-side execution path from a user question to retrieval, bounded graph/agentic reasoning, and claim verification.

Do not modify source code.

Requirements:
- Read only the files needed to establish the path.
- Identify exact file/function names.
- Distinguish planning, retrieval, agentic loop, and provenance verification.
- State whether this benchmark invokes an external LLM API at runtime.
- Do not summarize unrelated files.
- Run: `python scripts/run_task_eval.py 01`.
- Create `benchmark_output/task_01_result.json`.
- Include every expected-result ID defined for Task 01 in `benchmark/expected_results.json`, with `observed` and concrete `evidence`.
- Validate with: `python scripts/validate_result.py 01`.

Finish only when the result artifact validates.
```

## Expected results

- **T01-R1** — Extract the ordered query path pipeline.answer_question -> planner.plan_query -> retrieval.hybrid_retrieve -> agentic.run_bounded_loop -> provenance.verify_claims.
- **T01-R2** — Identify planning/retrieval/agentic/provenance as separate stages and state that the benchmark has no external LLM API runtime dependency.
- **T01-R3** — Do not modify source files; only benchmark_output/task_01_result.json may be created.

## Required test command

```bash
python scripts/run_task_eval.py 01
```

## Required result artifact

```text
benchmark_output/task_01_result.json
```

Then validate:

```bash
python scripts/validate_result.py 01
```

A run is complete only when the task tests and result-artifact validation both pass.
