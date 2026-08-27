import copy, json
from pathlib import Path
from ontology_graphrag_benchmark.ontology_induction import propose_ontology_changes

OBSERVATIONS = [
    {"kind": "class", "name": "Organization", "frequency": 8, "examples": ["Microsoft", "OpenAI"]},
    {"kind": "class", "name": "Org", "frequency": 5, "examples": ["MSFT"]},
    {"kind": "class", "name": "ResearchMethod", "frequency": 6, "examples": ["Agentic RAG"]},
    {"kind": "class", "name": "Graph", "frequency": 4, "examples": ["knowledge graph", "entity graph"]},
    {"kind": "relation", "name": "uses", "frequency": 9, "examples": ["GraphRAG uses KG"]},
    {"kind": "relation", "name": "utilizes", "frequency": 4, "examples": ["method utilizes graph"]},
    {"kind": "relation", "name": "synthesizes", "frequency": 3, "examples": ["system synthesizes reports"]},
]

def load_ontology():
    p = Path(__file__).parents[1] / "ontology" / "base_ontology.json"
    return json.loads(p.read_text(encoding="utf-8"))

def test_input_ontology_not_mutated():
    ont = load_ontology(); before = copy.deepcopy(ont)
    propose_ontology_changes(OBSERVATIONS, ont)
    assert ont == before

def test_existing_and_alias_mappings_are_preserved():
    out = propose_ontology_changes(OBSERVATIONS, load_ontology())
    items = {(x["kind"], x["name"]): x for x in out["items"]}
    assert items[("class", "Organization")]["status"] == "existing"
    assert items[("class", "Org")]["status"] == "mapped_alias"
    assert items[("class", "Org")]["target"] == "Organization"
    assert items[("relation", "utilizes")]["status"] == "mapped_alias"
    assert items[("relation", "utilizes")]["target"] == "uses"

def test_new_candidate_is_reviewable():
    out = propose_ontology_changes(OBSERVATIONS, load_ontology())
    item = {(x["kind"], x["name"]): x for x in out["items"]}[("class","ResearchMethod")]
    assert item["status"] == "new_candidate"
    assert 0.0 <= item["confidence"] <= 1.0 and item["examples"]

def test_graph_candidate_is_marked_conflict():
    out = propose_ontology_changes(OBSERVATIONS, load_ontology())
    item = {(x["kind"], x["name"]): x for x in out["items"]}[("class","Graph")]
    assert item["status"] == "conflict" and item["conflict_reason"]

def test_proposal_requires_review():
    assert propose_ontology_changes(OBSERVATIONS, load_ontology())["apply_automatically"] is False
