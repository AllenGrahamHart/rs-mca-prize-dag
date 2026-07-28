#!/usr/bin/env python3
"""Check the constant color-pair and two-adic root bound."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_basefield_branch_exclusion"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_basefield_conic_router"
CONSUMER = "l1_mixed_petal_amplification"


def v2(value: int) -> int:
    out = 0
    while value % 2 == 0:
        value //= 2
        out += 1
    return out


def imaginary_part(exponent: int) -> int:
    return {0: 0, 1: 1, 2: 0, 3: -1}[exponent]


def main() -> None:
    for exponent in (19, 31):
        p = 2**exponent - 1
        assert v2(p - 1) == 1
        assert v2(p + 1) == exponent
        assert v2(p * p + 1) == 1
        assert v2(p**4 - 1) == exponent + 2

    pairs = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if imaginary_part(a) == imaginary_part(b)
    ]
    assert pairs == [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2), (3, 3)]
    real_pairs = [pair for pair in pairs if pair[0] % 2 == pair[1] % 2 == 0]
    assert real_pairs == [(0, 0), (0, 2), (2, 0), (2, 2)]
    residual_pairs = [pair for pair in real_pairs if pair != (0, 0)]
    assert residual_pairs == [(0, 2), (2, 0), (2, 2)]
    assert 2 * len(residual_pairs) == 6 < 7

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(BBE1)", "(BBE2)", "at most six", "seven"):
        assert anchor in statement
    for anchor in ("v_2(p^4-1)", "a-a^(-1)=b-b^(-1)", "order six"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_BASEFIELD_BRANCH_EXCLUSION_PASS roots<=6<7")


if __name__ == "__main__":
    main()
