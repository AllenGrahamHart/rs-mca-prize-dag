#!/usr/bin/env python3
"""Check the official congruences and base-field conic routing identities."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_basefield_conic_router"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_order_one_conic_reduction",
    "l1_mersenne_next_to_maximal_belyi_shifted_value_gate",
}
CONSUMER = "l1_mixed_petal_amplification"
EXPONENTS = (13, 17, 19, 31)


def main() -> None:
    rows = []
    for exponent in EXPONENTS:
        p = 2**exponent - 1
        assert p % 8 == 7
        assert p % 3 == 1
        assert pow(5, (p - 1) // 2, p) == (1 if exponent in (13, 17) else p - 1)
        rows.append((exponent, p, p % 5))
    assert rows == [
        (13, 8191, 1),
        (17, 131071, 1),
        (19, 524287, 2),
        (31, 2147483647, 2),
    ]

    # z=-1 gives w=+/-6; z=3 gives the printed scalar equation.
    assert 247 - 770 + 775 == 7 * 6**2
    assert 247 * 3**2 + 770 * 3 + 775 == 5308
    assert {2 - zeta for zeta in (-1, 1)} == {1, 3}

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(BCR1)", "(BCR2)", "(BCR3)", "(BCR4)", "5308"):
        assert anchor in statement
    for anchor in ("gcd(8,p-1)=2", "discriminant of `c^2-3c+1` is five", "rho^p"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_BASEFIELD_CONIC_ROUTER_PASS rows=4 residual_packets<=4")


if __name__ == "__main__":
    main()
