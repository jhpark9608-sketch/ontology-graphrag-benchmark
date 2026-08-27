from __future__ import annotations


def _minmax(values: dict[str, float]) -> dict[str, float]:
    if not values:
        return {}
    lo = min(values.values())
    hi = max(values.values())
    if hi == lo:
        return {k: 1.0 for k in values}
    return {k: (v - lo) / (hi - lo) for k, v in values.items()}


def hybrid_retrieve(
    *,
    vector_candidates: list[dict],
    graph_candidates: list[dict],
    vector_weight: float = 0.5,
    graph_weight: float = 0.5,
    limit: int = 5,
) -> list[dict]:
    """Fuse vector and graph evidence.

    Candidate fields: evidence_id, text, source_document_id, score.
    """
    raise NotImplementedError("Task 05: implement hybrid retrieval")
