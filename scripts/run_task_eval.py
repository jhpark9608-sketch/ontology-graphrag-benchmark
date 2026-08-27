#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PATH = ROOT / "benchmark" / "expected_results.json"
OUTPUT_DIR = ROOT / "benchmark_output"


def parse_count(text: str, label: str) -> int:
    matches = re.findall(rf"(\d+)\s+{label}\b", text)
    return int(matches[-1]) if matches else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task_id", help="01..10")
    args = parser.parse_args()
    task_id = args.task_id.zfill(2)

    expected = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))
    if task_id not in expected:
        print(f"Unknown task: {task_id}", file=sys.stderr)
        return 2

    test_file = expected[task_id]["test_file"]
    cmd = [sys.executable, "-m", "pytest", "-q", test_file]
    print("+", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout, end="")

    passed = parse_count(proc.stdout, "passed")
    failed = parse_count(proc.stdout, "failed")
    errors = parse_count(proc.stdout, "error") + parse_count(proc.stdout, "errors")
    skipped = parse_count(proc.stdout, "skipped")

    OUTPUT_DIR.mkdir(exist_ok=True)
    metrics = {
        "task_id": task_id,
        "test_file": test_file,
        "command": " ".join(cmd),
        "pytest_exit_code": proc.returncode,
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "skipped": skipped,
        "expected_result_ids": [x["id"] for x in expected[task_id]["expected"]],
    }
    metrics_path = OUTPUT_DIR / f"task_{task_id}_test_metrics.json"
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(f"Wrote {metrics_path.relative_to(ROOT)}")
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
