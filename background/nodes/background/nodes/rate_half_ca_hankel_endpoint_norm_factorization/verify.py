#!/usr/bin/env python3
"""Tiny degree checks for endpoint norm and complementary factorization."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def check_profile(m: int, omissions: int, nonsaturated: int) -> None:
    assert m >= 1
    rho = 4 * m - 1
    n = 16 * m
    slopes = 4 * m + 1
    assert 0 <= omissions <= m - 1
    assert 1 <= nonsaturated <= 1 + omissions

    incidences = slopes * rho - omissions
    residual_degree = n * m - incidences
    assert residual_degree == 1 + omissions

    omission_degree = omissions
    assert n * m + omission_degree == slopes * rho + residual_degree
    assert residual_degree <= m

    saturated_degree = n - nonsaturated
    assert saturated_degree >= 15 * m
    complementary_parameter_degree = slopes - m
    assert complementary_parameter_degree == 3 * m + 1
    bezout_x_degree = rho - 1
    assert bezout_x_degree == 4 * m - 2

    clean_fibers = 3 * m + 1 - omissions
    assert clean_fibers >= 2 * m + 2

    weight_from_columns = slopes * (n - rho) + omissions
    weight_from_rows = n * (slopes - m) + residual_degree
    assert weight_from_columns == weight_from_rows
    assert weight_from_columns == 48 * m * m + 16 * m + 1 + omissions


def check_small_profiles() -> int:
    checked = 0
    for m in range(1, 257):
        for omissions in {0, (m - 1) // 2, m - 1}:
            for nonsaturated in {1, 1 + omissions}:
                check_profile(m, omissions, nonsaturated)
                checked += 1
    return checked


def check_official_profile() -> int:
    m = 1 << 37
    check_profile(m, m - 1, m)
    assert 4 * m - 1 == (1 << 39) - 1
    assert 16 * m == 1 << 41
    assert 15 * m == 2061584302080
    assert 3 * m + 1 - (m - 1) == 2 * m + 2
    return m


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node_id = "rate_half_ca_hankel_endpoint_norm_factorization"
    assert nodes[node_id]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_ca_hankel_endpoint_saturation_rigidity",
        node_id,
        "req",
    ) in edges
    assert (node_id, "rate_half_band_closure", "ev") in edges


def main() -> None:
    checked = check_small_profiles()
    official = check_official_profile()
    check_dag()
    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_NORM_FACTORIZATION_PASS "
        f"profiles={checked} official_m={official}"
    )


if __name__ == "__main__":
    main()
