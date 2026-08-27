from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Entity:
    entity_id: str
    name: str
    entity_type: str
    aliases: tuple[str, ...] = ()


@dataclass(frozen=True)
class Triple:
    subject_id: str
    subject_type: str
    relation: str
    object_id: str
    object_type: str
    source_document_id: str
    evidence_span: str
    confidence: float = 1.0


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    source_document_id: str
    text: str
    vector_score: float = 0.0
    graph_score: float = 0.0
    graph_path: tuple[str, ...] = ()


@dataclass(frozen=True)
class Claim:
    claim_id: str
    text: str
    required_facts: tuple[str, ...]


@dataclass
class Verification:
    claim_id: str
    status: str
    evidence_ids: list[str] = field(default_factory=list)
    graph_paths: list[list[str]] = field(default_factory=list)
    supported_facts: list[str] = field(default_factory=list)
    contradicted_facts: list[str] = field(default_factory=list)


JsonDict = dict[str, Any]
