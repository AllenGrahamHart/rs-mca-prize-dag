#!/usr/bin/env python3
"""Replay the exact common-row and slack contradictions."""

import json
from pathlib import Path


def ceil_div(a, b):
    return -((-a) // b)


def check(e, R):
    J = 3 * e - R - 5
    assert J > 0

    for q in range(2, min(e, 20) + 1):
        g = e - q
        slack = (R + 5) * g - (R + 3) * e + 2
        difference = J * (q - 1) - slack
        assert difference == e * (3 * q - 5) + R + 3
        assert difference > 0

    g = e - 1
    slack = (R + 5) * g - (R + 3) * e + 2
    assert slack == 2 * e - R - 3
    for d_line in (0, 1):
        missing_J = 3 * e - R - 6 + d_line
        zero_deficit_slack = slack - (e - 6 - d_line)
        assert zero_deficit_slack == e - R + 3 + d_line
        assert missing_J - zero_deficit_slack == 2 * e - 9
        assert missing_J > zero_deficit_slack

    rho = 3 * e - 1
    T = rho + 4
    for endpoint_deficit in range(5):
        left = T - ((rho + 4 - endpoint_deficit) // 4)
        right = ceil_div(3 * rho + 12 + endpoint_deficit, 4)
        assert left == right


for test_e in (7, 13, 127, 1009, 183251937963):
    for test_R in range(5):
        check(test_e, test_R)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "minimum_pair_exclusion"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_GAP_FOUR_MINIMUM_PAIR_EXCLUSION_PASS")
