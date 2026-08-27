from __future__ import annotations

from .models import Entity


def resolve_entity(
    surface_form: str,
    entities: list[Entity],
    *,
    min_candidate_score: float = 0.55,
    ambiguity_margin: float = 0.05,
) -> dict:
    """Resolve an entity without fabricating a graph id.

    Expected statuses:
    resolved_exact, resolved_alias, resolved_candidate, ambiguous, unresolved.
    """
    raise NotImplementedError("Task 04: implement open-world entity resolution")
