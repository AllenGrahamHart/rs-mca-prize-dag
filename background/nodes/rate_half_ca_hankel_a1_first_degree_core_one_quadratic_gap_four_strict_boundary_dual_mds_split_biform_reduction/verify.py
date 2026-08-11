#!/usr/bin/env python3
"""Check strict-boundary dual-MDS dimensions and split counts."""

import json
from pathlib import Path


def check(e, line_deficit):
    assert e % 2 == 1 and e >= 7
    assert 0 <= line_deficit <= e - 6
    rho = 3 * e - 1
    p = rho // 2
    n0 = 3 * p - 1
    d = rho - 1
    dual_dimension = n0 - (d + 1)
    assert dual_dimension == p - 1
    assert (p - 2) + d == n0 - 2
    parameter_degree = e - 1
    domain_degree = p - 2
    split_rows = 2 * p + line_deficit
    clean_fibers = (e + 15) // 2 + line_deficit
    assert split_rows <= n0
    return (
        rho,
        p,
        parameter_degree,
        domain_degree,
        split_rows,
        clean_fibers,
    )


for test_e in (7, 13, 1009, 183251937963):
    for line_deficit in range(min(test_e - 6, 4) + 1):
        check(test_e, line_deficit)

official = check(183251937963, 0)
assert official == (
    549755813888,
    274877906944,
    183251937962,
    274877906942,
    549755813888,
    91625968989,
)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "strict_boundary_dual_mds_split_biform_reduction"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_STRICT_BOUNDARY_DUAL_MDS_BIFORM_PASS", official)
