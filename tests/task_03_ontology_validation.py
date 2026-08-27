import json
from pathlib import Path
from ontology_graphrag_benchmark.ontology import validate_triple

def ontology():
    p = Path(__file__).parents[1] / "ontology" / "base_ontology.json"
    return json.loads(p.read_text(encoding="utf-8"))

def test_valid_triple():
    out = validate_triple(subject_type="Organization", relation="develops", object_type="Technology", ontology=ontology())
    assert out["status"] == "valid" and out["relation"] == "develops"

def test_relation_alias_is_repairable():
    out = validate_triple(subject_type="Organization", relation="builds", object_type="Technology", ontology=ontology())
    assert out["status"] == "repairable" and out["relation"] == "develops"

def test_invalid_domain_rejected():
    out = validate_triple(subject_type="Concept", relation="develops", object_type="Technology", ontology=ontology())
    assert out["status"] == "rejected" and "domain" in out["reason"].lower()

def test_invalid_range_rejected():
    out = validate_triple(subject_type="Organization", relation="develops", object_type="Concept", ontology=ontology())
    assert out["status"] == "rejected" and "range" in out["reason"].lower()

def test_unknown_relation_rejected():
    out = validate_triple(subject_type="Organization", relation="invented_unknown_relation", object_type="Technology", ontology=ontology())
    assert out["status"] == "rejected" and "unknown" in out["reason"].lower()

def test_unknown_class_rejected():
    out = validate_triple(subject_type="UnknownClass", relation="develops", object_type="Technology", ontology=ontology())
    assert out["status"] == "rejected" and "class" in out["reason"].lower()
