#!/usr/bin/env python3
"""Check the exact concave pair-union obstruction and official floor."""

import json
from pathlib import Path


def F(e, j):
    return (
        3 * e * e * j
        - 9 * e * e
        - 2 * e * j * j
        + 5 * e * j
        + 6 * e
        - 2 * j * j
        - 2 * j
    )


def check(e):
    assert e % 2 == 1 and e >= 7
    rho = 3 * e - 1
    j0 = rho // 2 - 1
    assert j0 == (3 * e - 3) // 2
    assert F(e, 4) == 3 * e * e - 6 * e - 40 > 0
    assert F(e, j0 - 1) == (3 * e * e - 14 * e - 15) // 2 > 0

    union_floor = rho + j0
    assert union_floor == 3 * rho // 2 - 1
    assert (rho + j0 - 1) // j0 == 3
    assert 3 * j0 + 1 == rho + j0 - 1
    assert 4 * j0 > rho + j0 - 1
    return rho, j0, union_floor


for test_e in (7, 13, 127, 1009):
    rho, j0, _ = check(test_e)
    for j in range(4, j0):
        assert F(test_e, j) > 0

official = check(183251937963)
assert official == (549755813888, 274877906943, 824633720831)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "macroscopic_pair_union_floor"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_MACROSCOPIC_PAIR_UNION_FLOOR_PASS", official)
