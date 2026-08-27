# Codex App A/B Protocol

This protocol is written for the **Codex desktop app**, not the CLI.

## 1. Create two identical working copies

Start from the same Git commit.

```text
CodexBench/
├── ontology-graphrag-baseline/
└── ontology-graphrag-routing/
```

Both copies must point to the same `benchmark-start-v1` commit.

### Baseline copy

- Do not add the `agent-routing-gpt` overlay.
- In the Codex app choose:
  - GPT-5.6 Sol
  - Medium reasoning

### Routing copy

Apply the `agent-routing-gpt` project overlay:

```text
ontology-graphrag-routing/
├── AGENTS.md
└── .codex/
    ├── config.toml
    └── agents/
        ├── luna_max.toml
        ├── terra_high.toml
        ├── sol_low.toml
        └── sol_medium.toml
```

Use the routing configuration as committed in the `agent-routing-gpt` repository.

## 2. One fresh chat per task per condition

For Task 02:

```text
Task 02
├── Baseline: fresh Codex chat
└── Routing: fresh Codex chat
```

Do not continue Task 03 in the Task 02 chat. Previous context would bias the result.

## 3. Never run the two conditions at the same time

If you plan to record account-level usage/credits, simultaneous runs make attribution difficult.

Run one condition to completion, record usage, then run the paired condition.

## 4. Copy the prompt exactly

Open:

```text
benchmark/tasks/XX_*.md
```

Copy only the text inside **Prompt to paste into Codex**.

Use exactly the same prompt for Baseline and Routing.

## 5. Counterbalance order

To reduce order/cache bias:

```text
replicate 1: A → B
replicate 2: B → A
replicate 3: A → B
```

For the next task, reverse the starting order.

A = Sol Medium baseline  
B = agent-routing-gpt

## 6. Restore the starting commit before every run

Use a disposable checkout.

```bash
git reset --hard <BENCHMARK_START_SHA>
git clean -fd
```

Warning: this deletes uncommitted changes.

For the Routing condition, restore the benchmark start, then re-apply the routing overlay before starting the new chat.

## 7. What Codex must produce

Each task requires:

```text
benchmark_output/task_XX_result.json
```

The file must include:
- task id
- pass/fail status
- concise summary
- each expected-result ID and evidence
- test counts
- files changed

The file is ignored by Git.

## 8. What you record manually after each run

Record these separately in your A/B results sheet:

- condition
- task id
- replicate
- start/end time
- uncached input tokens, if shown
- cached input tokens, if shown
- output tokens, if shown
- credits consumed
- wall-clock time
- Sol calls, if observable
- task success
- test pass count

Prefer account/work Usage & billing data where available. A single chat's visible usage may not represent all delegated/subagent activity.

## 9. Quality gate

A routed run counts as more efficient only if it preserves acceptable quality.

Minimum quality gate:

- required task tests pass
- result artifact validates
- no unrelated regressions
- no unsupported claims about completion

## 10. Pilot before the full benchmark

Run these first:

1. Task 01 — easy discovery
2. Task 05 — medium implementation/retrieval
3. Task 07 — hard agentic reasoning

If the protocol works, expand to all 10 tasks × 3 replicates.
