from __future__ import annotations

import json
from pathlib import Path


def load_ontology(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_triple(
    *,
    subject_type: str,
    relation: str,
    object_type: str,
    ontology: dict,
) -> dict:
    """Classify a triple as valid, repairable, or rejected.

    Return:
        {"status": "valid|repairable|rejected", "reason": "...", "relation": "..."}
    """
    raise NotImplementedError("Task 03: implement ontology triple validation")
