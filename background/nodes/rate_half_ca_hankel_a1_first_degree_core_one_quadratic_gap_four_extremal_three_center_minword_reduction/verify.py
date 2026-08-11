#!/usr/bin/env python3
"""Check the extremal-line excess ledger and minimum-word arithmetic."""

import json
from pathlib import Path


def check(e):
    assert e % 2 == 1 and e >= 7
    rho = 3 * e - 1
    p = rho // 2
    j = p - 1
    T = rho + 4
    u = rho + j - 1
    assert u == 3 * p - 2
    assert T - 3 == rho + 1 == 3 * e

    for d_line in (0, 1):
        line_missing = 3 * j + d_line
        assert line_missing == u - (1 - d_line)
        line_incidence = 3 * u - line_missing

        off_deficit = (e - 6) - d_line
        off_capacity = (p - 3) * (T - 3) - off_deficit
        off_actual = e * u - line_incidence
        assert off_capacity - off_actual == e

    N = 4 * rho
    k = 2 * rho
    d_min = N - k + 1
    assert d_min == 2 * rho + 1
    assert N - d_min == k - 1

    alpha, beta, delta = 2, 5, 11
    coefficients = (beta - delta, delta - alpha, alpha - beta)
    assert sum(coefficients) == 0
    assert sum(c * x for c, x in zip(coefficients, (alpha, beta, delta))) == 0
    return rho, p, 2 * e, d_min


for test_e in (7, 13, 127, 1009):
    check(test_e)

official = check(183251937963)
assert official == (
    549755813888,
    274877906944,
    366503875926,
    1099511627777,
)

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
node_id = (
    "rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_"
    "extremal_three_center_minword_reduction"
)
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes[node_id]["status"] == "PROVED"

print("RATE_HALF_QUADRATIC_EXTREMAL_THREE_CENTER_MINWORD_PASS", official)
