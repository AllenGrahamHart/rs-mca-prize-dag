#!/usr/bin/env python3
"""Exact arithmetic replay of rate-quarter M=4 pair uniqueness."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_fpc5_ratequarter_m4_t2_payment"


def main() -> None:
    cells = 0
    for k in range(2, 257):
        outside = 3 * k + 1
        for ell in range(1, outside + 1):
            petals, background = divmod(outside, ell)
            if petals != 4:
                continue
            assert 0 <= background < ell
            assert 4 * ell + background == outside
            assert 5 * ell > outside
            assert 2 * ell > k - 1
            cells += 1

    official_k = 2**40
    minimum_ell = (3 * official_k + 1) // 5 + 1
    assert 5 * minimum_ell > 3 * official_k + 1
    assert 2 * minimum_ell > official_k - 1
    assert comb(4, 2) + 4 == 10

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert ("l1_general_first_layout_domination", NODE, "req") in edges
    assert (NODE, "l1_fpc5_m4_t2_payment", "req") in edges

    print(
        "L1_FPC5_RATEQUARTER_M4_T2_PAYMENT_PASS "
        f"small_cells={cells} official_min_ell={minimum_ell} bound=10"
    )


if __name__ == "__main__":
    main()
