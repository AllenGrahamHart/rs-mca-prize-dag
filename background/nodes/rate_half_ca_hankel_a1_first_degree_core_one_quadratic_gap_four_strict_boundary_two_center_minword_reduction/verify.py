#!/usr/bin/env python3
"""Check the strict-boundary excess and clean-slope arithmetic."""

import json
from pathlib import Path


def check(e, line_deficit):
    assert e % 2 == 1 and e >= 7
    assert 0 <= line_deficit <= e - 6
    rho = 3 * e - 1
    p = rho // 2
    u0 = 3 * p - 1
    off_slopes = 3 * e + 1
    off_deficit = e - 6 - line_deficit
    line_incidence = 4 * p - 2 - line_deficit
    actual = e * u0 - line_incidence
    capacity = (p - 2) * off_slopes - off_deficit
    excess = capacity - actual
    assert excess == p
    zero_excess = off_slopes - excess
    assert zero_excess == p + 2
    clean = zero_excess - off_deficit
    assert clean == (e + 15) // 2 + line_deficit
    return rho, p, u0, off_slopes, zero_excess, clean


for test_e in (7, 13, 1009, 183251937963):
    for line_deficit in range(min(test_e - 6, 4) + 1):
        check(test_e, line_deficit)

official = check(183251937963, 0)
assert official == (
    549755813888,
    274877906944,
    824633720831,
    549755813890,
    274877906946,
    91625968989,
)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "strict_boundary_two_center_minword_reduction"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_STRICT_BOUNDARY_MINWORD_PASS", official)
