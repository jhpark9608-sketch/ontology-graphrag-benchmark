# Benchmark Task Index

Every task must start from the same benchmark start commit.

| ID | Topic | Difficulty | Target | Test command |
|---|---|---:|---|---|
| 01 | Codebase map | Easy | no source change | `python scripts/run_task_eval.py 01` |
| 02 | Structured extraction | Medium | `extraction.py` | `python scripts/run_task_eval.py 02` |
| 03 | Ontology validation | Medium | `ontology.py` | `python scripts/run_task_eval.py 03` |
| 04 | Open-world entity resolution | Medium | `entity_resolution.py` | `python scripts/run_task_eval.py 04` |
| 05 | Hybrid vector + graph retrieval | Medium | `retrieval.py` | `python scripts/run_task_eval.py 05` |
| 06 | Query router / planner | Hard | `planner.py` | `python scripts/run_task_eval.py 06` |
| 07 | Bounded Agentic GraphRAG | Hard | `agentic.py` | `python scripts/run_task_eval.py 07` |
| 08 | Claim provenance verification | Hard | `provenance.py` | `python scripts/run_task_eval.py 08` |
| 09 | Ontology induction / alignment | Hard | `ontology_induction.py` | `python scripts/run_task_eval.py 09` |
| 10 | End-to-end evaluation | Hard | `evaluation.py` | `python scripts/run_task_eval.py 10` |

Open the matching file under `benchmark/tasks/` and copy the **Prompt to paste into Codex** verbatim to both A/B chats.
