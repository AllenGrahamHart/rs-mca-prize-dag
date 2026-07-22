#!/usr/bin/env python3
"""Verify the h=0 projective factorization and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu0_h0_projective_branch_exclusion"
SUPPLIER = "l1_m4_h3_nu0_nonzero_b_tangent_exclusion"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0
    for p in (7, 31, 127):
        for a_value in range(1, min(p, 11)):
            for r in range(1, min(p, 11)):
                for b_value in range(1, min(p, 11)):
                    a = a_value * pow(r, -2, p) % p
                    b = b_value * pow(r, -3, p) % p
                    left = (27 * b * b - 12 * a * a * b
                            - 8 * a**3 - 12 * a * a) % p
                    factored = ((3 * b + 2 * a)
                                * (9 * b - 4 * a * a - 6 * a)) % p
                    assert left == factored
                    checks += 1

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
    for anchor in ("(PBE2)", "(PBE3)", "9bR(0)", "first factor is impossible",
                   "does not exclude"):
        assert anchor in statement
        checks += 1
    print(f"L1_M4_H3_NU0_H0_PROJECTIVE_BRANCH_EXCLUSION_PASS checks={checks}")


if __name__ == "__main__":
    main()
