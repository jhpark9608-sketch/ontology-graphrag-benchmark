# Task 08 — Provenance verification

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Hard

## Prompt to paste into Codex

```text
Implement `verify_claims` in `src/ontology_graphrag_benchmark/provenance.py`.

Requirements:
- Match explicit `required_facts` in each Claim against evidence `supports_facts` and `contradicts_facts`.
- Classify each claim as exactly one of: `supported`, `partially_supported`, `contradicted`, `unsupported`.
- Contradiction takes precedence if any required fact is explicitly contradicted.
- Supported requires every required fact to be supported.
- Partial requires at least one but not all required facts supported and no contradiction.
- Unsupported has neither supporting nor contradicting evidence.
- Include evidence ids and non-empty graph paths used as provenance.
- Do not attach irrelevant evidence to an unsupported claim.
- Do not modify tests.
- Run: `python scripts/run_task_eval.py 08`.
- Create `benchmark_output/task_08_result.json` with all expected-result IDs/evidence.
- Validate with: `python scripts/validate_result.py 08`.
```

## Expected results

- **T08-R1** — c1 is supported and includes evidence e1 plus graph path provenance.
- **T08-R2** — c2 is partially_supported.
- **T08-R3** — c3 is contradicted.
- **T08-R4** — c4 is unsupported and has no evidence ids.
- **T08-R5** — All 4 Task 08 tests pass.

## Required test command

```bash
python scripts/run_task_eval.py 08
```

## Required result artifact

```text
benchmark_output/task_08_result.json
```

Then validate:

```bash
python scripts/validate_result.py 08
```

A run is complete only when the task tests and result-artifact validation both pass.
