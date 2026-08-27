from __future__ import annotations


def plan_query(query: str) -> dict:
    """Return a bounded structured retrieval plan.

    strategy: local_semantic | local_graph | global_community | multi_hop
    """
    raise NotImplementedError("Task 06: implement query routing and planning")
