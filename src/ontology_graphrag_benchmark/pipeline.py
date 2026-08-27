from __future__ import annotations

from .agentic import run_bounded_loop
from .planner import plan_query
from .provenance import verify_claims
from .retrieval import hybrid_retrieve


def answer_question(query: str, *, vector_candidates, graph_candidates, retrieve_fn):
    """Illustrative query-side execution path used by Task 01.

    This benchmark intentionally keeps the path explicit so a coding agent can
    trace the architecture without scanning the whole repository.
    """
    plan = plan_query(query)
    initial_evidence = hybrid_retrieve(
        vector_candidates=vector_candidates,
        graph_candidates=graph_candidates,
    )
    loop_result = run_bounded_loop(
        initial_query=query,
        retrieve_fn=retrieve_fn,
        max_steps=plan["max_steps"],
    )

    claims = loop_result.get("claims", [])
    evidence = loop_result.get("verification_evidence", [])
    verification = verify_claims(claims, evidence)

    return {
        "plan": plan,
        "initial_evidence": initial_evidence,
        "loop": loop_result,
        "verification": verification,
    }
