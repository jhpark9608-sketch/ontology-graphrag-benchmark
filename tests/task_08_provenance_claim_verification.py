from ontology_graphrag_benchmark.models import Claim
from ontology_graphrag_benchmark.provenance import verify_claims

CLAIMS = [
    Claim("c1", "Microsoft developed GraphRAG.", ("microsoft", "developed", "graphrag")),
    Claim("c2", "GraphRAG uses knowledge graphs and agentic planning.", ("graphrag", "uses_kg", "uses_agentic_planning")),
    Claim("c3", "OpenAI developed GraphRAG.", ("openai", "developed_graphrag")),
    Claim("c4", "GraphRAG was released in 1999.", ("released_1999",)),
]
EVIDENCE = [
    {"evidence_id": "e1", "supports_facts": ["microsoft", "developed", "graphrag"], "contradicts_facts": [], "graph_path": ["org:microsoft","develops","tech:graphrag"]},
    {"evidence_id": "e2", "supports_facts": ["graphrag", "uses_kg"], "contradicts_facts": [], "graph_path": ["tech:graphrag","uses","concept:knowledge_graph"]},
    {"evidence_id": "e3", "supports_facts": [], "contradicts_facts": ["openai", "developed_graphrag"], "graph_path": []},
]

def result_map():
    return {x["claim_id"]: x for x in verify_claims(CLAIMS, EVIDENCE)}

def test_supported_claim():
    out = result_map()["c1"]
    assert out["status"] == "supported"
    assert "e1" in out["evidence_ids"] and out["graph_paths"]

def test_partially_supported_claim():
    out = result_map()["c2"]
    assert out["status"] == "partially_supported"
    assert "uses_kg" in out["supported_facts"]

def test_contradicted_claim():
    out = result_map()["c3"]
    assert out["status"] == "contradicted" and out["contradicted_facts"]

def test_unsupported_claim():
    out = result_map()["c4"]
    assert out["status"] == "unsupported" and not out["evidence_ids"]
