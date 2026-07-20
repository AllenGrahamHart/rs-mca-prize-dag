#!/usr/bin/env python3
"""Verify the optimized one-fiber affine coset-pair bound."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_affine_coset_pair_optimized_stepanov"
DEPENDENCY = "f3_h2_stepanov_inhouse"
CONSUMER = "f3_h3_dsp8_nodal_trace_parameter_router"


def floor_rational_cuberoot(numerator: int, denominator: int) -> int:
    low, high = 0, 1
    while denominator * high**3 <= numerator:
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if denominator * middle**3 <= numerator:
            low = middle
        else:
            high = middle
    return low


def parameter_check() -> int:
    minimum_slack = 0
    for exponent in range(13, 42):
        n = 1 << exponent
        a = floor_rational_cuberoot(27 * n * n, 64)
        b = floor_rational_cuberoot(125 * n, 64) + 1
        d = a
        linear_slack = a * b * b - d * (a + d)
        assert linear_slack > 0
        assert a * b <= n
        assert a + n * b < n * n + 1
        degree_slack = 64 * d**3 * n * n - (a + 2 * n * b) ** 3
        assert degree_slack > 0
        row_slack = min(linear_slack, degree_slack)
        minimum_slack = row_slack if not minimum_slack else min(minimum_slack, row_slack)
    return minimum_slack


def finite_field_check(prime: int, order: int) -> int:
    root = next(
        pow(base, (prime - 1) // order, prime)
        for base in range(2, prime)
        if pow(pow(base, (prime - 1) // order, prime), order // 2, prime)
        == prime - 1
    )
    subgroup = [pow(root, exponent, prime) for exponent in range(order)]
    subgroup_set = set(subgroup)
    maximum = 0
    for alpha in range(1, prime):
        for beta in range(1, prime):
            count = sum((alpha * value + beta) % prime in subgroup_set for value in subgroup)
            maximum = max(maximum, count)
    assert maximum**3 < 64 * order * order
    return maximum


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "req") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md").read_text().split()
    )
    for marker in (
        "<4n^(2/3)",
        "nonconstant,nonproportionalaffineforms",
        "optimized`T=1`specialization",
        "doesnotimprovethemulti-fiberrich-cosetconstant",
    ):
        assert marker in statement


def main() -> None:
    slack = parameter_check()
    maximum = finite_field_check(97, 16)
    packet_check()
    print(
        "F3_AFFINE_COSET_PAIR_OPTIMIZED_STEPANOV_PASS "
        f"official_rows=29 minimum_slack={slack} control_max={maximum}"
    )


if __name__ == "__main__":
    main()
