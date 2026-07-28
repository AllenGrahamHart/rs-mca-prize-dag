#!/usr/bin/env python3
"""Independent audit of the Plotkin/coloring compiler and target wiring."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_low_square_mass_plotkin_coloring_compiler"
TARGET = "e1_official_low_square_mass_collision_coloring"
PAIR_TARGET = "e1_official_low_square_mass_pair_budget"


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
    pair_statement = (ROOT / f"background/nodes/{PAIR_TARGET}/statement.md").read_text()
    assert "`chi(G_p(33))<=3`" in statement
    assert "bypasses `P<=K-B*-1`" in contract
    assert "status:** TARGET" in target_statement
    assert "65127585921474870475467050631501738502567" in pair_statement
    checks += 4

    # Independent tight-row boundary replay.
    ell = 33
    K = 38001322036274275320505631960233903602944
    budget = 317494674775468773183020924238786383963
    C = 50
    edge_cap = 65127585921474870475467050631501738502567
    assert budget * ((ell + 1) * K + C * edge_cap) < K * K
    assert budget * ((ell + 1) * K + C * (edge_cap + 1)) >= K * K
    assert 3 * K // 2 <= edge_cap
    checks += 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[TARGET]["status"] == "TARGET"
    assert nodes[PAIR_TARGET]["status"] == "TARGET"
    assert (NODE, TARGET, "ev") in edges
    assert (NODE, TARGET, "req") not in edges
    assert (TARGET, "unsafe_crossing_family_instantiation", "ev") in edges
    assert (TARGET, "unsafe_crossing_family_instantiation", "req") not in edges
    assert (NODE, PAIR_TARGET, "ev") in edges
    assert (NODE, PAIR_TARGET, "req") not in edges
    assert (PAIR_TARGET, "unsafe_crossing_family_instantiation", "ev") in edges
    checks += 10

    print(f"E1_LOW_SQUARE_MASS_PLOTKIN_COLORING_COMPILER_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
