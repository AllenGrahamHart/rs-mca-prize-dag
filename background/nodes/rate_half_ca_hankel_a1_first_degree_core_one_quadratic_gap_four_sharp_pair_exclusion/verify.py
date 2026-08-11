#!/usr/bin/env python3
"""Check the exact integer and orientation ledger in the sharp-pair proof."""

import json
from pathlib import Path


def check(e):
    rho = 3 * e - 1
    total_deficit = e - 6

    # Double-root arm: one padded heavy row, endpoint deficits in {0,1}.
    for r_source in range(2):
        triple_cap = 2 * rho + 1 - r_source - 1
        assert triple_cap <= 2 * rho

    # Two-simple arm: orient from a positive-deficit endpoint. If both
    # endpoint deficits vanish, the endpoint full locators have no padding.
    for left in range(3):
        for right in range(3):
            if max(left, right) >= 1:
                r_source = max(left, right)
                triple_cap = 2 * rho + 2 - r_source - 1
            else:
                triple_cap = (rho + 2) + rho - 3
            assert triple_cap <= 2 * rho

    line_deficit = (rho + 1) - 2 * (e + 1)
    assert line_deficit == e - 2
    assert line_deficit > total_deficit

    for pair_deficit in range(5):
        old_line_cap = (rho + 2 - pair_deficit) // 2
        new_line_cap = (rho + 3 - pair_deficit) // 3
        expanding = rho + 4 - new_line_cap
        closed_form = (2 * rho + 9 + pair_deficit + 2) // 3
        assert expanding == closed_form
        assert expanding >= 2 * e + 3
        assert new_line_cap <= old_line_cap


for test_e in (7, 9, 15, 101, 183251937963):
    check(test_e)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "sharp_pair_exclusion"
)
assert nodes[node_id]["status"] == "PROVED"
assert nodes["rate_half_band_crossing_location"]["status"] == "TARGET"

print("RATE_HALF_QUADRATIC_GAP_FOUR_SHARP_PAIR_EXCLUSION_PASS")
