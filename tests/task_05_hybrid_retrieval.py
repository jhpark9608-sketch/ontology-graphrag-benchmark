from ontology_graphrag_benchmark.retrieval import hybrid_retrieve

VECTOR = [
    {"evidence_id": "e1", "text": "semantic only", "source_document_id": "d1", "score": 0.95},
    {"evidence_id": "e2", "text": "shared evidence", "source_document_id": "d2", "score": 0.80},
]
GRAPH = [
    {"evidence_id": "e2", "text": "shared evidence", "source_document_id": "d2", "score": 10.0},
    {"evidence_id": "e3", "text": "graph only", "source_document_id": "d3", "score": 9.0},
]

def test_hybrid_deduplicates_and_exposes_contributions():
    out = hybrid_retrieve(vector_candidates=VECTOR, graph_candidates=GRAPH, limit=5)
    ids = [x["evidence_id"] for x in out]
    assert len(ids) == len(set(ids))
    shared = next(x for x in out if x["evidence_id"] == "e2")
    assert {"vector_score_norm","graph_score_norm","fused_score"} <= set(shared)

def test_scores_are_normalized_before_fusion():
    for item in hybrid_retrieve(vector_candidates=VECTOR, graph_candidates=GRAPH):
        assert 0.0 <= item["vector_score_norm"] <= 1.0
        assert 0.0 <= item["graph_score_norm"] <= 1.0
        assert 0.0 <= item["fused_score"] <= 1.0

def test_vector_only_fallback():
    out = hybrid_retrieve(vector_candidates=VECTOR, graph_candidates=[])
    assert [x["evidence_id"] for x in out][:2] == ["e1", "e2"]

def test_graph_only_fallback():
    out = hybrid_retrieve(vector_candidates=[], graph_candidates=GRAPH)
    assert [x["evidence_id"] for x in out][:2] == ["e2", "e3"]

def test_shared_evidence_is_top_with_equal_weights():
    out = hybrid_retrieve(vector_candidates=VECTOR, graph_candidates=GRAPH, vector_weight=0.5, graph_weight=0.5)
    assert out[0]["evidence_id"] == "e2"
