#!/usr/bin/env python3
"""Check the extremal three-center source partition arithmetic."""

import json
from pathlib import Path


def check(e, deficits):
    assert e % 2 == 1 and e >= 7
    assert len(deficits) == 3
    assert sum(deficits) in (0, 1)
    rho = 3 * e - 1
    p = rho // 2
    u0 = 3 * p - 2
    class_sizes = [p - 1 + value for value in deficits]
    assert sum(class_sizes) == u0 - (1 - sum(deficits))
    return rho, p, u0, class_sizes


for test_e in (7, 13, 1009, 183251937963):
    check(test_e, (0, 0, 0))
    check(test_e, (1, 0, 0))

official = check(183251937963, (1, 0, 0))
assert official[:3] == (549755813888, 274877906944, 824633720830)
assert sum(official[3]) == official[2]

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "extremal_three_center_source_partition"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_EXTREMAL_SOURCE_PARTITION_PASS", official[:3])
