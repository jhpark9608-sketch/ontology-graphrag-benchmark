from __future__ import annotations

from .models import Claim


def verify_claims(claims: list[Claim], evidence_records: list[dict]) -> list[dict]:
    """Verify claim facts against explicit evidence metadata.

    Statuses: supported, partially_supported, contradicted, unsupported.
    """
    raise NotImplementedError("Task 08: implement claim-level provenance verification")
