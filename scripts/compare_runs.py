#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

BASELINE = "baseline_sol_medium"
ROUTING = "agent_routing_gpt"

def num(v):
    s = str(v or "").strip()
    try:
        return float(s) if s else None
    except ValueError:
        return None

def truth(v):
    s = str(v or "").strip().lower()
    if s in {"1","true","yes","pass","passed"}: return True
    if s in {"0","false","no","fail","failed"}: return False
    return None

def avg(rows, key):
    vals = [num(r.get(key)) for r in rows]
    vals = [v for v in vals if v is not None]
    return mean(vals) if vals else None

def total_tokens_avg(rows):
    vals=[]
    for r in rows:
        parts=[num(r.get(k)) for k in ("uncached_input_tokens","cached_input_tokens","output_tokens")]
        if all(v is None for v in parts): continue
        vals.append(sum(v or 0 for v in parts))
    return mean(vals) if vals else None

def success(rows):
    vals=[truth(r.get("task_success")) for r in rows]
    vals=[v for v in vals if v is not None]
    return 100*sum(vals)/len(vals) if vals else None

def test_rate(rows):
    p=t=0.0
    for r in rows:
        a,b=num(r.get("tests_passed")),num(r.get("tests_total"))
        if a is not None and b is not None and b>0:
            p+=a;t+=b
    return 100*p/t if t else None

def fmt(x, d=1):
    return "—" if x is None else f"{x:,.{d}f}"

def reduction(b, r):
    return None if b in (None,0) or r is None else (b-r)/b*100

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv_path", nargs="?", default="benchmark/run_results.csv")
    ap.add_argument("--output", default="benchmark/BENCHMARK_RESULTS.md")
    args=ap.parse_args()

    with open(args.csv_path, encoding="utf-8-sig", newline="") as f:
        rows=list(csv.DictReader(f))
    groups=defaultdict(list)
    for r in rows: groups[r.get("condition","")].append(r)
    b=groups[BASELINE]; g=groups[ROUTING]

    metrics=[
        ("Total tokens / run", total_tokens_avg(b), total_tokens_avg(g)),
        ("Uncached input / run", avg(b,"uncached_input_tokens"), avg(g,"uncached_input_tokens")),
        ("Cached input / run", avg(b,"cached_input_tokens"), avg(g,"cached_input_tokens")),
        ("Output tokens / run", avg(b,"output_tokens"), avg(g,"output_tokens")),
        ("Credits / run", avg(b,"credits"), avg(g,"credits")),
        ("Wall time (s) / run", avg(b,"wall_time_s"), avg(g,"wall_time_s")),
        ("Sol calls / run", avg(b,"sol_calls"), avg(g,"sol_calls")),
    ]
    lines=[
        "# Benchmark Results","",
        "> Generated from `benchmark/run_results.csv`. Incomplete rows are ignored per metric.","",
        "## Efficiency","",
        "| Metric | Sol Medium baseline | agent-routing-gpt | Reduction |",
        "|---|---:|---:|---:|",
    ]
    for label,x,y in metrics:
        red=reduction(x,y)
        lines.append(f"| {label} | {fmt(x)} | {fmt(y)} | {'—' if red is None else f'{red:.1f}%'} |")
    bs,gs=success(b),success(g)
    bt,gt=test_rate(b),test_rate(g)
    lines += [
        "","## Quality","",
        "| Metric | Sol Medium baseline | agent-routing-gpt | Difference |",
        "|---|---:|---:|---:|",
        f"| Task success | {fmt(bs)}% | {fmt(gs)}% | {'—' if bs is None or gs is None else f'{gs-bs:+.1f} pp'} |",
        f"| Test pass rate | {fmt(bt)}% | {fmt(gt)}% | {'—' if bt is None or gt is None else f'{gt-bt:+.1f} pp'} |",
        "","## Interpretation","",
    ]
    cr = reduction(avg(b,"credits"), avg(g,"credits"))
    if cr is None:
        lines.append("- Credit data are not complete enough for a cost claim.")
    else:
        lines.append(f"- Mean credit reduction: **{cr:.1f}%**.")
    if bs is not None and gs is not None:
        lines.append(f"- Task-success difference: **{gs-bs:+.1f} percentage points**.")
    if bt is not None and gt is not None:
        lines.append(f"- Test-pass difference: **{gt-bt:+.1f} percentage points**.")
    lines += ["","Only claim an efficiency improvement when the quality gate remains acceptable.",""]
    out=Path(args.output)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
