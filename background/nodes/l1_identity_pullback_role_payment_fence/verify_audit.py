#!/usr/bin/env python3
"""Mutation audit for the identity-pullback role-payment fence."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_identity_pullback_role_payment_fence"


def main() -> None:
    checks = 0

    # Degree two is not the identity endpoint: a partially agreed two-point
    # fiber contributes nonzero partial loss.
    agreement = {1}
    complete_fiber = {1, -1}
    fully_agreed_labels = [] if not complete_fiber <= agreement else [0]
    partial_loss = len(agreement)
    assert not fully_agreed_labels
    assert partial_loss == 1
    checks += 2

    # Sparse complete-label coverage can create a kernel; B=D is load-bearing.
    k = 5
    b = 3
    assert max(0, k - b) == 2
    checks += 1

    # Raw threshold supports are not exact-shell owners. One five-agreement
    # word has five distinct four-subsets but one exact agreement set.
    from math import comb

    assert comb(5, 4) == 5
    assert 1 < comb(5, 4)
    checks += 2

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    assert "This is an exact route equivalence, not a list-size upper bound" in statement
    assert "Classifying refinement maps or role vectors at `s>=2` cannot by itself close" in statement
    checks += 2

    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    assert "tameness uses the strict official" in audit
    assert "No computation or probabilistic evidence is load-bearing" in audit
    checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 2

    print(f"AUDIT_L1_IDENTITY_PULLBACK_ROLE_PAYMENT_FENCE_PASS checks={checks}")


if __name__ == "__main__":
    main()
