#!/usr/bin/env python3
"""Verify the universal h=0 packet exclusion and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu0_h0_universal_packet_exclusion"
SUPPLIER = "l1_m4_h3_nu0_h0_projective_quarter_certificate"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    y, r = sp.symbols("y r", nonzero=True)
    g = y**3 + 6 * r**2 * y + 20 * r**3
    assert sp.expand((y + 2 * r) * (y**2 - 2 * r * y + 10 * r**2)) == g
    assert sp.expand((y - r) * (y - 4 * r) * (y + 5 * r)) == \
        y**3 - 21 * r**2 * y + 20 * r**3
    logarithmic = sp.together(
        1 / (y - 4 * r) + sp.diff(g, y) / g - 4 / (y - r)
        - 324 * r**4 / ((y - r) * (y - 4 * r) * g)
    )
    assert sp.factor(logarithmic) == 0
    checks = 3

    for p in (8191, 131071, 524287, 2147483647):
        assert p % 4 == 3
        multiplicity = (3 * p - 1) // 4
        assert 4 * multiplicity + 1 == 3 * p
        assert multiplicity < p - 1 < 2 * multiplicity
        for m in range(1, min(p, 20)):
            if (4 * (p + 1 - m)) % p == 0:
                assert m == 1
        checks += 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(UPE2)", "(UPE3)", "(UPE4)", "F(X)^p",
                   "only the exceptional", "does not exclude"):
        assert anchor in statement
        checks += 1
    print(f"L1_M4_H3_NU0_H0_UNIVERSAL_PACKET_EXCLUSION_PASS checks={checks}")


if __name__ == "__main__":
    main()
