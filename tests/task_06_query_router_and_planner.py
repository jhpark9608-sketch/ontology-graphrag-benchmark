import pytest
from ontology_graphrag_benchmark.planner import plan_query

@pytest.mark.parametrize(
    ("query", "strategy"),
    [
        ("Define ontology.", "local_semantic"),
        ("Which organization developed GraphRAG?", "local_graph"),
        ("What are the main themes across the corpus?", "global_community"),
        ("Which organization developed a technology that uses knowledge graphs?", "multi_hop"),
    ],
)
def test_expected_strategy(query, strategy):
    out = plan_query(query)
    assert out["strategy"] == strategy
    assert isinstance(out["subqueries"], list) and out["subqueries"]
    assert out["expected_evidence_type"]
    assert out["stopping_condition"]
    assert 1 <= out["max_steps"] <= 4

def test_plan_is_deterministic():
    q = "Which organization developed GraphRAG?"
    assert plan_query(q) == plan_query(q)
