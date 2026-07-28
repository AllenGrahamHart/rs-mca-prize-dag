#!/usr/bin/env python3
"""Independent audit of the Plotkin/coloring compiler and target wiring."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_low_square_mass_plotkin_coloring_compiler"
TARGET = "e1_official_low_square_mass_collision_coloring"


def main() -> None:
    checks = 0

    # Exhaustively verify the scalar inequality around the sharp boundary.
    for ell in (33, 65):
        for M in range(1, ell + 8):
            lower = M * (M - 1) * (ell + 1)
            upper = M * M * ell
            assert (lower <= upper) == (M <= ell + 1)
            checks += 1

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    contract = (ROOT / f"background/nodes/{NODE}/claim_contract.md").read_text()
    target_statement = (ROOT / f"background/nodes/{TARGET}/statement.md").read_text()
    assert "`chi(G_p(33))<=3`" in statement
    assert "bypasses `P<=K-B*-1`" in contract
    assert "status:** TARGET" in target_statement
    checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[TARGET]["status"] == "TARGET"
    assert (NODE, TARGET, "ev") in edges
    assert (NODE, TARGET, "req") not in edges
    assert (TARGET, "unsafe_crossing_family_instantiation", "ev") in edges
    assert (TARGET, "unsafe_crossing_family_instantiation", "req") not in edges
    checks += 6

    print(f"E1_LOW_SQUARE_MASS_PLOTKIN_COLORING_COMPILER_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
