# Task 04 — Open-world entity resolution

## Purpose

Controlled Codex A/B benchmark. Start from the exact benchmark start commit in a fresh chat.

**Difficulty:** Medium

## Prompt to paste into Codex

```text
Implement `resolve_entity` in `src/ontology_graphrag_benchmark/entity_resolution.py`.

Use a staged policy:
1. exact canonical-name match
2. exact alias match
3. deterministic candidate scoring
4. ambiguous/unresolved fallback

Requirements:
- Case-insensitive comparison is allowed, but results must be deterministic.
- If multiple entities share an exact name (for example `Atlas`), return `ambiguous` with no selected id.
- Never invent an id that is not present in the supplied entity list.
- Return status, selected_id, confidence, candidate_ids, and reason.
- Preserve unresolved entities instead of forcing a match.
- Do not change tests.
- Run: `python scripts/run_task_eval.py 04`.
- Create `benchmark_output/task_04_result.json` with all expected-result IDs/evidence.
- Validate with: `python scripts/validate_result.py 04`.
```

## Expected results

- **T04-R1** — OpenAI resolves exactly to org:openai.
- **T04-R2** — MSFT resolves as an alias to org:microsoft.
- **T04-R3** — Atlas is ambiguous between org:atlas and tech:atlas and has no selected id.
- **T04-R4** — NeoSemanticX remains unresolved with no fabricated id.
- **T04-R5** — All 5 Task 04 tests pass.

## Required test command

```bash
python scripts/run_task_eval.py 04
```

## Required result artifact

```text
benchmark_output/task_04_result.json
```

Then validate:

```bash
python scripts/validate_result.py 04
```

A run is complete only when the task tests and result-artifact validation both pass.
