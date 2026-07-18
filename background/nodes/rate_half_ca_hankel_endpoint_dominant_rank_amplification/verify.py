#!/usr/bin/env python3
"""Tiny checks for strict-endpoint component rank amplification."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_endpoint_dominant_rank_amplification"


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def check_m(m: int) -> None:
    assert m % 4 == 0
    worst_b = m // 4 - 1
    assert ceil_div(m + 1, worst_b + 1) == 5
    assert ceil_div(m + 1, 1) == m + 1
    midpoint = worst_b // 2
    assert ceil_div(m + 1, midpoint + 1) >= 5
    for b in (0, midpoint, worst_b):
        exact = ceil_div(m + 1, b + 1)
        assert exact >= 5


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert (
        "rate_half_ca_hankel_endpoint_rational_normal_kernel_curve",
        NODE,
        "req",
    ) in edges
    assert (
        "rate_half_ca_hankel_endpoint_component_defect_localization",
        NODE,
        "req",
    ) in edges
    assert (NODE, "rate_half_band_closure", "ev") in edges
    expected = f"background/nodes/{NODE}/statement.md"
    assert expected in nodes["rate_half_band_closure"]["refs"]


def main() -> None:
    for power in range(3, 18):
        check_m(1 << power)
    official_m = 1 << 37
    check_m(official_m)
    assert official_m // 4 - 1 == 34_359_738_367
    check_dag()
    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_DOMINANT_RANK_AMPLIFICATION_PASS "
        f"official_m={official_m} worst_residual={official_m // 4 - 1}"
    )


if __name__ == "__main__":
    main()
