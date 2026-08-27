# ontology-graphrag-benchmark

A small, deterministic coding benchmark for comparing **Codex Sol Medium** against a **cost-aware multi-agent routing policy** on modern LLM + Ontology + Knowledge Graph engineering tasks.

The repository is intentionally **partially implemented**. Each benchmark task asks Codex to complete or analyze one bounded capability while preserving the same starting code. The goal is to compare **coding quality, token/credit usage, latency, and escalation behavior** under controlled A/B conditions.

## Why this benchmark exists

For realistic repository work, a strong model can waste expensive tokens on tasks that do not require deep reasoning: file discovery, repetitive edits, log extraction, and straightforward tests. A routing setup can delegate those tasks to cheaper agents while reserving stronger reasoning for genuinely difficult problems.

This benchmark provides a neutral target project for measuring whether that routing strategy actually helps.

### A/B conditions

| Condition | Setup |
|---|---|
| **Baseline** | Codex app, GPT-5.6 Sol, Medium reasoning, no routing overlay |
| **Routing** | Same project + `agent-routing-gpt` overlay; Terra High default, Luna/Terra/Sol subagents |

Use the **same task prompt**, **same start commit**, **fresh chat**, and **same test command** for both conditions.

---

## Domain

The tasks are based on current LLM system patterns that combine:

- structured entity/relation extraction
- ontology constraints
- open-world entity resolution
- GraphRAG
- hybrid vector + graph retrieval
- query routing and multi-step planning
- bounded Agentic RAG
- claim-level provenance and verification
- LLM-assisted ontology induction/alignment
- end-to-end RAG evaluation

The benchmark itself uses deterministic fixtures and does **not** require an external LLM API. This makes A/B comparisons reproducible and isolates Codex's coding behavior.

---

## Project structure

```text
ontology-graphrag-benchmark/
├── README.md
├── pyproject.toml
├── docs/
│   └── CODEX_APP_PROTOCOL.md
├── src/ontology_graphrag_benchmark/
│   ├── models.py
│   ├── pipeline.py
│   ├── extraction.py
│   ├── ontology.py
│   ├── entity_resolution.py
│   ├── retrieval.py
│   ├── planner.py
│   ├── agentic.py
│   ├── provenance.py
│   ├── ontology_induction.py
│   └── evaluation.py
├── data/
├── ontology/
├── tests/
├── benchmark/
│   ├── TASK_INDEX.md
│   ├── expected_results.json
│   └── tasks/
└── scripts/
    ├── run_task_eval.py
    └── validate_result.py
```

`benchmark_output/` is ignored by Git and is where Codex writes standardized per-task result artifacts.

---

## Quick start

```bash
python -m pip install -e ".[dev]"
pytest -q tests/task_01_codebase_map.py
```

Most task-specific tests are expected to **fail on the initial benchmark commit** because the target function is intentionally incomplete.

Do not "fix" the initial repository before the A/B experiment.

---

## Tasks and expected outcomes

| Task | Topic | Difficulty | Expected observable outcome |
|---|---|---:|---|
| 01 | Codebase map | Easy | Correct query execution path extracted; no source edits |
| 02 | Structured extraction | Medium | Valid records normalize; malformed/unknown records are rejected |
| 03 | Ontology validation | Medium | Triples classified as valid/repairable/rejected with reasons |
| 04 | Open-world entity resolution | Medium | Exact/alias/ambiguous/unseen cases are separated without fabricated IDs |
| 05 | Hybrid retrieval | Medium | Vector + graph scores are normalized/fused; duplicates removed; fallback works |
| 06 | Query router/planner | Hard | Four query types route to the expected strategy with bounded structured plans |
| 07 | Bounded Agentic GraphRAG | Hard | Early stop, retry, contradiction handling, duplicate-query prevention, hard step cap |
| 08 | Provenance verification | Hard | Claims classified as supported/partial/contradicted/unsupported with evidence |
| 09 | Ontology induction/alignment | Hard | Reviewable proposal generated; conflicts preserved; production ontology unchanged |
| 10 | End-to-end evaluation | Hard | Exact benchmark metrics produced and retrieval vs reasoning failures separated |

Detailed expected-result IDs are in `benchmark/expected_results.json` and in each task specification.

---

## Standard Codex result artifact

After completing a task, Codex must write:

```text
benchmark_output/task_XX_result.json
```

Schema:

```json
{
  "task_id": "02",
  "status": "pass",
  "summary": "What changed and why",
  "expected_results": [
    {
      "id": "T02-R1",
      "observed": true,
      "evidence": "pytest test name or concrete runtime evidence"
    }
  ],
  "tests": {
    "command": "python scripts/run_task_eval.py 02",
    "passed": 5,
    "failed": 0
  },
  "files_changed": [
    "src/ontology_graphrag_benchmark/extraction.py"
  ],
  "notes": ""
}
```

Validate it with:

```bash
python scripts/validate_result.py 02
```

This standardized output helps compare baseline and routing runs without relying only on free-form chat text.

---

## Important benchmark rule

Do **not** compare two runs that started from different code.

Before every task/run, restore the exact benchmark start commit in the disposable checkout.

See `docs/CODEX_APP_PROTOCOL.md` for the full Codex app procedure.

Record A/B usage in `benchmark/run_results.csv`, then generate a comparison report:

```bash
python scripts/compare_runs.py
```

This writes `benchmark/BENCHMARK_RESULTS.md`.

---

## Current benchmark start

Use the protected benchmark reference:

```text
benchmark-start-v1
```

All A/B runs for v1 should start from that exact code state. Do not advance the benchmark-start reference during an active benchmark round.
