from pathlib import Path

def test_expected_query_path_symbols_exist():
    root = Path(__file__).parents[1] / "src" / "ontology_graphrag_benchmark"
    expected = {
        "pipeline.py": "def answer_question",
        "planner.py": "def plan_query",
        "retrieval.py": "def hybrid_retrieve",
        "agentic.py": "def run_bounded_loop",
        "provenance.py": "def verify_claims",
    }
    for filename, symbol in expected.items():
        text = (root / filename).read_text(encoding="utf-8")
        assert symbol in text
