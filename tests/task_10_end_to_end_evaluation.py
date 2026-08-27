import pytest
from ontology_graphrag_benchmark.evaluation import evaluate_examples

EXAMPLES = [
    {"retrieved_relevant":2,"relevant_total":2,"graph_path_valid":True,"ontology_violations":0,"claims_total":2,"claims_grounded":2,"latency_ms":100,"tokens":200,"failure_type":"success"},
    {"retrieved_relevant":1,"relevant_total":2,"graph_path_valid":False,"ontology_violations":1,"claims_total":2,"claims_grounded":1,"latency_ms":200,"tokens":300,"failure_type":"retrieval"},
    {"retrieved_relevant":2,"relevant_total":2,"graph_path_valid":True,"ontology_violations":0,"claims_total":2,"claims_grounded":2,"latency_ms":150,"tokens":250,"failure_type":"success"},
    {"retrieved_relevant":1,"relevant_total":2,"graph_path_valid":None,"ontology_violations":0,"claims_total":2,"claims_grounded":1,"latency_ms":150,"tokens":250,"failure_type":"reasoning"},
]
def metrics(): return evaluate_examples(EXAMPLES)

def test_exact_retrieval_recall(): assert metrics()["retrieval_recall"] == pytest.approx(0.75)
def test_graph_path_validity_excludes_missing_paths(): assert metrics()["graph_path_validity"] == pytest.approx(2/3)
def test_ontology_violation_rate(): assert metrics()["ontology_violation_rate"] == pytest.approx(0.25)
def test_provenance_coverage(): assert metrics()["provenance_coverage"] == pytest.approx(0.75)
def test_latency_and_tokens():
    out=metrics(); assert out["mean_latency_ms"] == pytest.approx(150.0); assert out["total_tokens"] == 1000
def test_failure_breakdown_separates_failure_types():
    assert metrics()["failure_breakdown"] == {"success":2,"retrieval":1,"reasoning":1}
