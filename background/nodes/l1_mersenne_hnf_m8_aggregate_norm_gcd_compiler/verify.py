#!/usr/bin/env python3
"""Check the m=8 aggregate norm-gcd product identity and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_aggregate_norm_gcd_compiler"
DEPENDENCY = "l1_mersenne_hnf_order_one_frobenius_gate"
CONSUMER = "l1_mixed_petal_amplification"


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def main() -> None:
    # (T-1)(T+1)(T^2+1)(T^4+1)=T^8-1.
    product = [1]
    for factor in ([-1, 1], [1, 1], [1, 0, 1], [1, 0, 0, 0, 1]):
        product = multiply(product, factor)
    assert product == [-1] + [0] * 7 + [1]
    assert multiply([-1, 1], [1, 1]) != [1, 0, 1]

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(ANG1)", "(ANG2)", "(ANG3)", "four aggregate"):
        assert anchor in statement
    for anchor in ("Bezout", "base extension", "UFD"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_AGGREGATE_NORM_GCD_COMPILER_PASS")


if __name__ == "__main__":
    main()
