#!/usr/bin/env python3
"""Tiny arithmetic checks for strict-endpoint component-profile rigidity."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def check_formula(m: int) -> None:
    assert m > 1
    rho = 4 * m - 1
    n = 16 * m
    slopes = 4 * m + 1
    budget = m - 1

    for e in range(1, m + 1):
        assert slopes * (4 * e + 1) - n * e == 4 * e + slopes > budget
        assert slopes * (4 * e) - n * e == 4 * e

    assert 4 * m - rho == 1
    residual_parameter_degree = (m - 1) // 4
    dominant_parameter_degree = m - residual_parameter_degree
    assert dominant_parameter_degree == (3 * m + 4) // 4
    assert dominant_parameter_degree >= 2


def check_small_profiles() -> int:
    checked = 0
    for m in range(2, 11):
        budget = m - 1
        for parts in range(1, m + 1):
            for parameter_degrees in compositions(m, parts):
                for special in range(parts):
                    binary_degrees = tuple(
                        4 * e - (index == special)
                        for index, e in enumerate(parameter_degrees)
                    )
                    assert sum(binary_degrees) == 4 * m - 1
                    balanced_parameter_degree = m - parameter_degrees[special]
                    minimum_shortfall = 4 * balanced_parameter_degree
                    if minimum_shortfall <= budget:
                        assert parameter_degrees[special] >= (3 * m + 4) // 4
                    checked += 1
        check_formula(m)
    return checked


def check_official_profile() -> int:
    m = 1 << 37
    rho = 4 * m - 1
    residual = (m - 1) // 4
    dominant = m - residual
    assert rho == (1 << 39) - 1
    assert 16 * m == 1 << 41
    assert residual == (1 << 35) - 1
    assert dominant == 3 * (1 << 35) + 1
    assert 4 * dominant - 1 == 3 * (1 << 37) + 3
    return m


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node_id = "rate_half_ca_hankel_endpoint_rational_branch_exclusion"
    assert nodes[node_id]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_ca_hankel_endpoint_norm_factorization",
        node_id,
        "req",
    ) in edges
    assert (node_id, "rate_half_band_closure", "ev") in edges


def main() -> None:
    checked = check_small_profiles()
    official = check_official_profile()
    check_dag()
    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_COMPONENT_PROFILE_PASS "
        f"profiles={checked} official_m={official}"
    )


if __name__ == "__main__":
    main()
