#!/usr/bin/env python3
"""Verify the admissible F2 Newton-distance transport and DAG contract."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f2_admissible_newton_signed_distance"
PARENTS = {
    "dli_wcl_newton_short_window_exclusion",
    "f2_admissible_direct_sum_grs_reduction",
}
CONSUMER = "f2_conditional_close"


def element_of_order(p: int, order: int) -> int:
    assert (p - 1) % order == 0
    for candidate in range(2, p):
        omega = pow(candidate, (p - 1) // order, p)
        if pow(omega, order, p) == 1 and pow(omega, order // 2, p) != 1:
            return omega
    raise AssertionError("no element of requested dyadic order")


def check_small_row(p: int, s: int, r: int) -> int:
    omega = element_of_order(p, 2 * s)
    checked = 0
    columns = [
        [pow(omega, exponent * (2 * j - 1), p) for j in range(1, r + 1)]
        for exponent in range(s)
    ]
    for weight in range(1, min(2 * r, s) + 1):
        for support in itertools.combinations(range(s), weight):
            # Overall negation is redundant, so fix the first sign positive.
            for tail in itertools.product((-1, 1), repeat=weight - 1):
                signs = (1,) + tail
                checked += 1
                sums = [
                    sum(sign * columns[index][j] for sign, index in zip(signs, support)) % p
                    for j in range(r)
                ]
                assert any(sums), (p, s, r, support, signs)
    return checked


def main() -> None:
    counts = [
        check_small_row(17, 8, 3),
        check_small_row(97, 16, 2),
        check_small_row(193, 32, 2),
    ]

    s = 1 << 38
    r = 4_294_967_340
    assert 2 * r + 1 == s // 32 + 89

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    print(
        "F2_ADMISSIBLE_NEWTON_SIGNED_DISTANCE_PASS "
        f"small_checks={sum(counts)} floor={2 * r + 1} dag=3/3"
    )


if __name__ == "__main__":
    main()
