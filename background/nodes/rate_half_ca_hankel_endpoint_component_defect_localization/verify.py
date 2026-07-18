#!/usr/bin/env python3
"""Tiny arithmetic checks for strict-endpoint component-defect localization."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def check_profile(m: int, omission: int, overlap: int) -> int:
    assert m > 1
    assert 0 <= overlap <= omission <= m - 1
    rho = 4 * m - 1
    n = 16 * m
    slopes = 4 * m + 1
    row_budget = omission - overlap
    column_budget = 1 + row_budget

    assert slopes * rho == 16 * m * m - 1
    assert slopes - (m - 1) == 3 * m + 2
    assert n - (1 + omission) >= 15 * m
    assert 3 * m + 1 - omission >= 2 * m + 2

    maximum_residual = row_budget // 4
    checked = 0
    for residual in range(maximum_residual + 1):
        dominant_e = m - residual
        dominant_r = 4 * dominant_e - 1
        assert n * dominant_e - slopes * dominant_r == 4 * residual + 1
        assert 4 * residual <= row_budget
        assert dominant_e >= m - row_budget // 4
        assert column_budget - row_budget == 1
        checked += 1
    return checked


def check_small_profiles() -> int:
    checked = 0
    for m in range(2, 65):
        for omission in range(m):
            for overlap in range(omission + 1):
                checked += check_profile(m, omission, overlap)
    return checked


def check_official() -> int:
    m = 1 << 37
    omission = m - 1
    overlap = 0
    residual = (omission - overlap) // 4
    dominant = m - residual
    assert residual == (1 << 35) - 1
    assert dominant == 3 * (1 << 35) + 1
    assert 4 * dominant - 1 == 3 * (1 << 37) + 3
    assert 3 * m + 2 == 3 * (1 << 37) + 2
    assert 15 * m == 15 * (1 << 37)
    return m


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node_id = "rate_half_ca_hankel_endpoint_component_defect_localization"
    assert nodes[node_id]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_ca_hankel_endpoint_rational_branch_exclusion",
        node_id,
        "req",
    ) in edges
    assert (
        "rate_half_ca_hankel_endpoint_norm_factorization",
        node_id,
        "req",
    ) in edges
    assert (node_id, "rate_half_band_closure", "ev") in edges


def main() -> None:
    checked = check_small_profiles()
    official = check_official()
    check_dag()
    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_COMPONENT_DEFECT_PASS "
        f"profiles={checked} official_m={official}"
    )


if __name__ == "__main__":
    main()
