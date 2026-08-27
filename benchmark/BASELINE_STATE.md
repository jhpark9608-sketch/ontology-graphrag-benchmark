# Baseline state (`benchmark-start-v1`)

The initial benchmark repository is intentionally incomplete.

Expected full-suite state before Codex edits:

```text
Task 01: 1 test passes
Tasks 02–10: target implementations raise NotImplementedError
```

A full `pytest -q` run therefore fails by design.

This is not a broken setup. Each benchmark run targets **one task file at a time**, starting from the same initial commit.

Use:

```bash
python scripts/run_task_eval.py XX
```

After Codex implements the target task, that task's test file should pass while unrelated task modules may remain incomplete.

Do not implement multiple tasks in one benchmark run unless you are deliberately conducting a different experiment.
