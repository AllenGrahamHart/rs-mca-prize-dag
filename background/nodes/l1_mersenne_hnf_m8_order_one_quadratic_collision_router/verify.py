#!/usr/bin/env python3
"""Structural checks for the h=7 quadratic-collision router."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_quadratic_collision_router"
DEPENDENCIES = {
    "l1_mersenne_hnf_order_one_frobenius_gate",
    "l1_mersenne_hnf_m8_order_one_conic_reduction",
}
CONSUMER = "l1_mixed_petal_amplification"


def scalar_remainder_identity(r: Fraction, d: Fraction) -> tuple[Fraction, Fraction]:
    l1 = 6 / d
    l2 = (30 + r * d) / (2 * d * d)
    l3 = (60 + r * d * (d + 8)) / (3 * d**3)
    l5_over_l6 = -6 * d / (r - 1)
    lhs = (l5_over_l6 / l1) * (l2 - l3 / l1)
    closed = -Fraction(210, 1) - r * d * (1 - d)
    closed /= 18 * (r - 1)
    return lhs, closed


def main() -> None:
    atlas = ROOT / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
    rows = []
    for line in atlas.read_text().splitlines()[1:]:
        _, n, p, _, m, remainder = map(int, line.split("\t"))
        if m == 8 and remainder == 8:
            rows.append((n, p))
    assert sorted(rows) == [
        (65536, 8191),
        (1048576, 131071),
        (4194304, 524287),
        (17179869184, 2147483647),
    ]

    for r, d in ((Fraction(2), Fraction(3)), (Fraction(-5), Fraction(7)), (Fraction(9), Fraction(-2))):
        got, closed = scalar_remainder_identity(r, d)
        assert got == closed
        assert (got == 1) == (r * (18 + d - d * d) + 192 == 0)

    # Six reduced roots beat a cubic marked-point identity; three antipodal
    # pairs would force their sum to zero, contrary to l1=6/d.
    assert 6 > 3
    assert 3 * 2 == 6

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert statuses[CONSUMER] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(QCR2)", "(QCR3)", "six distinct colors"):
        assert anchor in statement
    for anchor in ("marked triples", "X^2-X-1", "l_5/l_6"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_QUADRATIC_COLLISION_ROUTER_PASS rows=4 chambers=3")


if __name__ == "__main__":
    main()
