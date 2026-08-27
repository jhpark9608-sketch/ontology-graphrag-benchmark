from __future__ import annotations

REQUIRED_FIELDS = {
    "canonical_entity_id",
    "surface_form",
    "entity_type",
    "source_document_id",
    "evidence_span",
    "confidence",
}


def normalize_extraction_record(
    record: dict,
    *,
    allowed_entity_types: set[str],
    allowed_relation_types: set[str],
) -> dict:
    """Validate and normalize a structured entity/relation extraction record.

    Task 02 target. The initial implementation is intentionally incomplete.
    """
    raise NotImplementedError("Task 02: implement structured extraction validation")
