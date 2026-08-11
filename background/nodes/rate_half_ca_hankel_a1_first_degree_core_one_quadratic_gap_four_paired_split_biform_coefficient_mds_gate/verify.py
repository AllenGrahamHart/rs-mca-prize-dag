#!/usr/bin/env python3
"""Check the paired coefficient-MDS matrix dimensions."""

import json
from pathlib import Path


def check(e, extremal_deficit, strict_deficit):
    assert e % 2 == 1 and e >= 7
    assert extremal_deficit in (0, 1)
    assert 0 <= strict_deficit <= e - 6
    rho = 3 * e - 1
    p = rho // 2

    ext_m = e - 2
    ext_n = p - 3
    ext_columns = 3 * p - 3 + extremal_deficit
    ext_checks = ext_columns - (ext_n + 1)
    ext_rows = (ext_m + 1) * ext_checks
    assert ext_checks == 2 * p - 1 + extremal_deficit

    strict_m = e - 1
    strict_n = p - 2
    strict_columns = 2 * p + strict_deficit
    strict_checks = strict_columns - (strict_n + 1)
    strict_rows = (strict_m + 1) * strict_checks
    assert strict_checks == p + 1 + strict_deficit

    return (
        rho,
        p,
        ext_columns,
        ext_rows,
        strict_columns,
        strict_rows,
    )


for test_e in (7, 13, 1009, 183251937963):
    for ext_d in (0, 1):
        for strict_d in range(min(test_e - 6, 3) + 1):
            check(test_e, ext_d, strict_d)

official = check(183251937963, 0, 0)
assert official == (
    549755813888,
    274877906944,
    824633720829,
    100743818300669342078294,
    549755813888,
    50371909150884426853035,
)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "paired_split_biform_coefficient_mds_gate"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_PAIRED_COEFFICIENT_MDS_GATE_PASS", official)
