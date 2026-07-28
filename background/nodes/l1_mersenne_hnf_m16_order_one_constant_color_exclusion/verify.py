#!/usr/bin/env python3
"""Check the h=15 constant-color unit-gcd certificates."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m16_order_one_constant_color_exclusion"
DEPENDENCY = "l1_mersenne_hnf_m16_order_one_constant_color_reduction"
CONSUMER = "l1_mixed_petal_amplification"
P = 8191


def primitive_certificate(a: int, b: int, c: int) -> tuple[int, int, int]:
    L = -b * (b * b - 2 * a * c - 4 * a * a)
    M = -c * b * b + a * c * c + 4 * a * a * c + 2 * a**3
    obstruction = a * M * M - b * M * L + c * L * L
    return L % P, M % P, obstruction % P


def main() -> None:
    assert [28 * s * s + 29 * s + 370 for s in (0, 2, -2)] == [370, 540, 424]
    assert [28 * s * s + 27 * s - 1202 for s in (0, 2, -2)] == [-1202, -1036, -1144]
    assert (426**2 - 2 * 29**2) % P == 7783
    assert (1146**2 - 2 * 27**2) % P == 1298
    assert primitive_certificate(28, 29, 370) == (3964, 47, 4509)
    assert primitive_certificate(28, 27, -1202) == (439, 321, 4947)

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    assert "(CCE15)" in statement
    for anchor in ("7783", "1298", "4509", "4947"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M16_ORDER_ONE_CONSTANT_COLOR_EXCLUSION_PASS gcds=2")


if __name__ == "__main__":
    main()
