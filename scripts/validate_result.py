#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PATH = ROOT / "benchmark" / "expected_results.json"


def fail(msg: str) -> int:
    print(f"FAIL: {msg}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task_id", help="01..10")
    args = parser.parse_args()
    task_id = args.task_id.zfill(2)

    expected_all = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))
    if task_id not in expected_all:
        return fail(f"unknown task id {task_id}")

    result_path = ROOT / "benchmark_output" / f"task_{task_id}_result.json"
    metrics_path = ROOT / "benchmark_output" / f"task_{task_id}_test_metrics.json"

    if not result_path.exists():
        return fail(f"missing {result_path.relative_to(ROOT)}")
    if not metrics_path.exists():
        return fail("run scripts/run_task_eval.py before validating the result artifact")

    try:
        result = json.loads(result_path.read_text(encoding="utf-8"))
        metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return fail(f"invalid JSON: {exc}")

    if result.get("task_id") != task_id:
        return fail("task_id mismatch")
    if result.get("status") not in {"pass", "fail"}:
        return fail("status must be pass or fail")
    if not isinstance(result.get("summary"), str) or not result["summary"].strip():
        return fail("summary is required")
    if not isinstance(result.get("files_changed"), list):
        return fail("files_changed must be a list")

    tests = result.get("tests")
    if not isinstance(tests, dict):
        return fail("tests object is required")
    if any(k not in tests for k in ("command", "passed", "failed")):
        return fail("tests must include command, passed, failed")
    if tests["passed"] != metrics["passed"] or tests["failed"] != metrics["failed"]:
        return fail(
            f"reported test counts do not match runner metrics "
            f"(reported {tests['passed']}/{tests['failed']}, "
            f"actual {metrics['passed']}/{metrics['failed']})"
        )

    expected_ids = {x["id"] for x in expected_all[task_id]["expected"]}
    observed_rows = result.get("expected_results")
    if not isinstance(observed_rows, list):
        return fail("expected_results must be a list")
    rows_by_id = {x.get("id"): x for x in observed_rows if isinstance(x, dict)}

    missing = sorted(expected_ids - set(rows_by_id))
    if missing:
        return fail(f"missing expected-result ids: {missing}")

    no_evidence = [rid for rid in expected_ids if not str(rows_by_id[rid].get("evidence", "")).strip()]
    if no_evidence:
        return fail(f"missing evidence for: {no_evidence}")

    if result["status"] == "pass":
        if metrics["pytest_exit_code"] != 0:
            return fail("status=pass but task tests failed")
        false_rows = [rid for rid in expected_ids if rows_by_id[rid].get("observed") is not True]
        if false_rows:
            return fail(f"pass status requires observed=true for: {false_rows}")

    print(f"PASS: task {task_id} result artifact matches test metrics and expected-result schema")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
