from ontology_graphrag_benchmark.agentic import run_bounded_loop

def make_retriever(sequence):
    calls = []
    def retrieve(query, step):
        calls.append((query, step))
        idx = min(step - 1, len(sequence) - 1)
        return dict(sequence[idx])
    retrieve.calls = calls
    return retrieve

def test_early_stop_when_sufficient():
    r = make_retriever([{"state": "sufficient", "evidence": ["e1"], "next_query": None}])
    out = run_bounded_loop(initial_query="q", retrieve_fn=r, max_steps=3)
    assert out["status"] == "sufficient" and len(out["trace"]) == 1

def test_one_retry_then_sufficient():
    r = make_retriever([
        {"state": "insufficient", "evidence": ["e1"], "next_query": "q refined"},
        {"state": "sufficient", "evidence": ["e2"], "next_query": None},
    ])
    out = run_bounded_loop(initial_query="q", retrieve_fn=r, max_steps=3)
    assert out["status"] == "sufficient" and len(out["trace"]) == 2

def test_contradiction_can_reformulate_once():
    r = make_retriever([
        {"state": "contradictory", "evidence": ["e1", "e2"], "next_query": "q resolve contradiction"},
        {"state": "sufficient", "evidence": ["e3"], "next_query": None},
    ])
    out = run_bounded_loop(initial_query="q", retrieve_fn=r, max_steps=3)
    assert out["status"] == "sufficient" and len(out["trace"]) == 2

def test_repeated_query_terminates():
    r = make_retriever([{"state": "insufficient", "evidence": [], "next_query": "q"}])
    out = run_bounded_loop(initial_query="q", retrieve_fn=r, max_steps=3)
    assert out["status"] == "repeated_query" and len(out["trace"]) == 1

def test_hard_step_cap():
    r = make_retriever([
        {"state": "insufficient", "evidence": [], "next_query": "q2"},
        {"state": "insufficient", "evidence": [], "next_query": "q3"},
        {"state": "insufficient", "evidence": [], "next_query": "q4"},
    ])
    out = run_bounded_loop(initial_query="q1", retrieve_fn=r, max_steps=3)
    assert out["status"] == "max_steps"
    assert len(out["trace"]) == 3
    assert len(r.calls) == 3
