#!/usr/bin/env python3
"""Check the extremal Forney-barycentric sizes and official counts."""

import json
from pathlib import Path


def check(e, line_deficit, rank_loss):
    assert e % 2 == 1 and e >= 7
    assert line_deficit in (0, 1)
    assert rank_loss in (0, 1, 2)
    rho = 3 * e - 1
    p = rho // 2
    d = rho - 1
    inside = p - 3 - rank_loss
    outside = (rho - rank_loss) - 1 - inside
    complement = (3 * p - 2) - inside
    assert outside == p + 2
    assert complement == rho + 1 + rank_loss == d + 2 + rank_loss
    zero_excess = 2 * e
    clean = zero_excess - (e - 6 - line_deficit)
    assert clean == e + 6 + line_deficit
    return rho, p, outside, complement, zero_excess, clean


for test_e in (7, 13, 1009, 183251937963):
    for line_deficit in (0, 1):
        for rank_loss in (0, 1, 2):
            check(test_e, line_deficit, rank_loss)

official = check(183251937963, 0, 0)
assert official == (
    549755813888,
    274877906944,
    274877906946,
    549755813889,
    366503875926,
    183251937969,
)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "extremal_zero_excess_forney_barycentric_gate"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_EXTREMAL_FORNEY_BARYCENTRIC_PASS", official)
