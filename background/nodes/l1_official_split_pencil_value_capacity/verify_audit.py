#!/usr/bin/env python3
"""Mutation audit for the official split-pencil value capacity."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_split_pencil_value_capacity"


def main() -> None:
    checks = 0

    assert 23 * 22 // 2 == 253
    assert 24 * 23 // 2 == 276 > 253
    checks += 2

    # Strictness matters: p=n/24 would permit 24 fibers.
    n = 24 * 5
    assert n // 5 == 24
    assert n // 6 == 20
    checks += 2

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    contract = (ROOT / "background" / "nodes" / NODE / "claim_contract.md").read_text()
    assert "p>n/24" in statement
    assert "ordinary integer cardinalities" in audit
    assert "No bound on perturbations" in contract
    assert "oriented ledger" in audit
    assert "rank test is one-way" in audit
    assert "squarefree" in statement
    assert "not asserted for" in audit
    assert "Equality is retained" in audit
    assert "complement map is injective only for unordered pairs" in audit
    assert "raw `binom(n,n-2p)` cap" in audit
    assert "Frobenius-degenerate branch" in contract
    assert "Squarefreeness of the complement" in audit
    assert "antipodal complements" in audit
    checks += 13

    # Mutating the strict degree boundary would reject the exact F_9 fixture.
    p = 3
    n = 8
    assert 2 * p <= n < 3 * p
    assert 3 * p - n == 1
    assert not (1 < 3 * p - n)
    checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 2

    print(f"AUDIT_L1_OFFICIAL_SPLIT_PENCIL_VALUE_CAPACITY_PASS checks={checks}")


if __name__ == "__main__":
    main()
