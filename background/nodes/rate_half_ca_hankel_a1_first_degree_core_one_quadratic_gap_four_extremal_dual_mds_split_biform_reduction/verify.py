#!/usr/bin/env python3
"""Check the dual-MDS biform dimensions and split-fiber counts."""

import json
from pathlib import Path


def check(e, line_deficit):
    assert e % 2 == 1 and e >= 7
    assert line_deficit in (0, 1)
    rho = 3 * e - 1
    p = rho // 2
    n0 = 3 * p - 2
    d = rho - 1
    dual_dimension = n0 - (d + 1)
    assert dual_dimension == p - 2
    assert (p - 3) + d == n0 - 2
    parameter_degree = e - 2
    domain_degree = p - 3
    split_rows = 3 * p - 3 + line_deficit
    clean_fibers = e + 6 + line_deficit
    assert split_rows == n0 - (1 - line_deficit)
    return (
        rho,
        p,
        parameter_degree,
        domain_degree,
        split_rows,
        clean_fibers,
    )


for test_e in (7, 13, 1009, 183251937963):
    check(test_e, 0)
    check(test_e, 1)

official = check(183251937963, 0)
assert official == (
    549755813888,
    274877906944,
    183251937961,
    274877906941,
    824633720829,
    183251937969,
)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "extremal_dual_mds_split_biform_reduction"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_EXTREMAL_DUAL_MDS_BIFORM_PASS", official)
