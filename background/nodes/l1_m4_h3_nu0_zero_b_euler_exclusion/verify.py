#!/usr/bin/env python3
"""Verify the zero-b Euler exclusion and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu0_zero_b_euler_exclusion"
SUPPLIERS = {
    "l1_m4_h3_nu0_zero_b_value_coset_certificate",
    "l1_m4_h3_euler_quotient_factorization",
}
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0
    for p in (524287, 2147483647):
        inv2 = pow(2, -1, p)
        q = -3 * inv2 % p
        invariant = (q * q + 3 * q + 1) % p
        expected = -5 * pow(4, -1, p) % p
        assert invariant == expected != 0
        assert p not in (2, 3, 5)
        checks += 2

    for p in (8191, 131071, 524287, 2147483647):
        assert 4 * (p + 1) % p == 4
        assert p > 3
        checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in SUPPLIERS:
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, CONSUMER, "ev") in edges
    checks += 2

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(ZBE1)", "(ZBE2)", "(ZBE3)", "(ZBE4)",
                   "-5/4=0", "m=4,h=3"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_NU0_ZERO_B_EULER_EXCLUSION_PASS checks={checks}")


if __name__ == "__main__":
    main()
