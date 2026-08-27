from __future__ import annotations

from collections.abc import Callable


def run_bounded_loop(
    *,
    initial_query: str,
    retrieve_fn: Callable[[str, int], dict],
    max_steps: int = 3,
) -> dict:
    """Run a bounded retrieve -> inspect -> reformulate loop.

    retrieve_fn(query, step) returns:
        {
          "state": "sufficient|insufficient|contradictory",
          "evidence": [...],
          "next_query": "..." | None
        }
    """
    raise NotImplementedError("Task 07: implement bounded agentic retrieval")
