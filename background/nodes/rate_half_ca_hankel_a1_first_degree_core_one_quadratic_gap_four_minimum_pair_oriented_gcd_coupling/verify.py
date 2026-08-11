#!/usr/bin/env python3
"""Check all exact oriented-gcd lower bounds."""

import json
from pathlib import Path


def ceil_div(a, b):
    return -((-a) // b)


def check(e):
    zero = ceil_div(3 * e - 2, 5)
    one = ceil_div(e - 2, 3)
    two = ceil_div(e - 1, 2)

    assert zero + 1 + 6 * (e - zero) <= 3 * e + 3
    assert (zero - 1) + 1 + 6 * (e - zero + 1) > 3 * e + 3

    for r, g in ((1, one), (2, two)):
        m = r + 3
        assert g + m * (e - g) <= 3 * e + 2
        if g > 1:
            assert (g - 1) + m * (e - g + 1) > 3 * e + 2
    return zero, one, two


for test_e in (7, 11, 101):
    check(test_e)

official = check(183251937963)
assert official == (109951162778, 61083979321, 91625968981)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "minimum_pair_oriented_gcd_coupling"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_MINIMUM_PAIR_ORIENTED_GCD_COUPLING_PASS", official)
