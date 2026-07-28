#!/usr/bin/env python3
"""Independent contract and wiring audit for the square-mass node."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = ROOT / "background/nodes/e1_collision_square_mass_reparametrization"
NODE_ID = NODE.name


def main() -> None:
    checks = 0

    # Rebuild the profile arithmetic independently over a finite box.
    for a in range(9):
        for b in range(0, 18, 2):
            for c in range(7):
                coeffs = [2] * a + [1] * b + [0] * c
                assert sum(v * v for v in coeffs) == 4 * a + b
                assert (2 * a + b + 2 * c) // 2 == a + b // 2 + c
                checks += 2

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert '"unbounded"' in statement and "is not used" in statement
    assert "does not mean that a finite-field collision exists" in contract
    assert "S<=260" in statement and "S<=132" in statement
    checks += 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE_ID]["status"] == "PROVED"
    assert "unbounded" not in nodes[NODE_ID]["statement"]
    assert ("acl_count", NODE_ID, "req") in edges
    assert ("e1_prime_field_l2_norm_collision_radius", NODE_ID, "req") in edges
    assert (NODE_ID, "e1_official_prime_exception_control", "ev") in edges
    assert (NODE_ID, "unsafe_crossing_family_instantiation", "ev") in edges
    checks += 6

    print(f"E1_COLLISION_SQUARE_MASS_REPARAMETRIZATION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
