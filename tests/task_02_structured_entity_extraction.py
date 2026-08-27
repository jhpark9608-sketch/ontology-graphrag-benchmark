import pytest
from ontology_graphrag_benchmark.extraction import normalize_extraction_record

ENTITY_TYPES = {"Organization", "Technology", "Concept"}
RELATION_TYPES = {"develops", "uses"}

def valid():
    return {
        "canonical_entity_id": "org:microsoft",
        "surface_form": "Microsoft",
        "entity_type": "Organization",
        "relation_type": None,
        "source_document_id": "d2",
        "evidence_span": "Microsoft Research developed GraphRAG",
        "confidence": 0.92,
    }

def test_valid_entity_record_normalizes():
    out = normalize_extraction_record(valid(), allowed_entity_types=ENTITY_TYPES, allowed_relation_types=RELATION_TYPES)
    assert out["canonical_entity_id"] == "org:microsoft"
    assert out["confidence"] == pytest.approx(0.92)

def test_missing_required_field_is_rejected():
    r = valid(); r.pop("evidence_span")
    with pytest.raises((ValueError, TypeError)):
        normalize_extraction_record(r, allowed_entity_types=ENTITY_TYPES, allowed_relation_types=RELATION_TYPES)

def test_unknown_entity_type_is_rejected():
    r = valid(); r["entity_type"] = "AlienType"
    with pytest.raises(ValueError):
        normalize_extraction_record(r, allowed_entity_types=ENTITY_TYPES, allowed_relation_types=RELATION_TYPES)

def test_unknown_relation_type_is_rejected():
    r = valid(); r["relation_type"] = "hallucinates_relation"
    with pytest.raises(ValueError):
        normalize_extraction_record(r, allowed_entity_types=ENTITY_TYPES, allowed_relation_types=RELATION_TYPES)

def test_confidence_must_be_bounded():
    r = valid(); r["confidence"] = 1.5
    with pytest.raises(ValueError):
        normalize_extraction_record(r, allowed_entity_types=ENTITY_TYPES, allowed_relation_types=RELATION_TYPES)
