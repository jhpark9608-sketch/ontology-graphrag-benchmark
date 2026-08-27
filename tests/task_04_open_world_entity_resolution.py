import json
from pathlib import Path
from ontology_graphrag_benchmark.entity_resolution import resolve_entity
from ontology_graphrag_benchmark.models import Entity

def load_entities():
    p = Path(__file__).parents[1] / "data" / "graph_entities.json"
    rows = json.loads(p.read_text(encoding="utf-8"))
    return [Entity(r["entity_id"], r["name"], r["entity_type"], tuple(r.get("aliases", []))) for r in rows]

def test_exact_match():
    out = resolve_entity("OpenAI", load_entities())
    assert out["status"] == "resolved_exact" and out["selected_id"] == "org:openai" and out["confidence"] == 1.0

def test_alias_match():
    out = resolve_entity("MSFT", load_entities())
    assert out["status"] == "resolved_alias" and out["selected_id"] == "org:microsoft"

def test_exact_collision_is_ambiguous():
    out = resolve_entity("Atlas", load_entities())
    assert out["status"] == "ambiguous" and out["selected_id"] is None
    assert set(out["candidate_ids"]) == {"org:atlas", "tech:atlas"}

def test_unseen_entity_is_unresolved():
    out = resolve_entity("NeoSemanticX", load_entities())
    assert out["status"] == "unresolved" and out["selected_id"] is None

def test_resolution_never_fabricates_id():
    entities = load_entities()
    known = {e.entity_id for e in entities}
    out = resolve_entity("Microsoft Research", entities)
    assert out["selected_id"] in known
