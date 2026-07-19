#!/usr/bin/env python3
"""Tiny arithmetic checks for strict A=3 endpoint saturation rigidity."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def endpoint_data(m: int, omissions: int) -> tuple[int, int, int, int]:
    assert m >= 1
    rho = 4 * m - 1
    n = 16 * m
    delta = m - 1
    assert 0 <= omissions <= delta

    target_failure = 4 * m + 1
    incidences = target_failure * rho - omissions
    deficit = n * m - incidences
    saturated = n - deficit

    assert deficit == 1 + omissions
    assert saturated == 16 * m - 1 - omissions
    assert saturated >= 15 * m
    return rho, target_failure, deficit, saturated


def check_small_profiles() -> int:
    checked = 0
    for m in range(1, 257):
        rho = 4 * m - 1
        n = 16 * m
        delta = m - 1

        assert (4 * m + 1) * rho <= n * m + delta
        assert (4 * m + 2) * rho > n * m + delta
        for omissions in {0, delta // 2, delta}:
            endpoint_data(m, omissions)
            checked += 1
    return checked


def check_official_profile() -> int:
    m = 1 << 37
    rho, failure, deficit, saturated = endpoint_data(m, m - 1)
    assert rho == (1 << 39) - 1
    assert failure == (1 << 39) + 1
    assert deficit == m
    assert saturated == 15 * m
    assert 16 * m == 1 << 41
    return m


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node_id = "rate_half_ca_hankel_endpoint_saturation_rigidity"
    assert nodes[node_id]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_ca_hankel_exceptional_root_charge",
        node_id,
        "req",
    ) in edges
    assert (node_id, "rate_half_band_closure", "ev") in edges


def main() -> None:
    checked = check_small_profiles()
    official = check_official_profile()
    check_dag()
    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_SATURATION_RIGIDITY_PASS "
        f"profiles={checked} official_m={official}"
    )


if __name__ == "__main__":
    main()
