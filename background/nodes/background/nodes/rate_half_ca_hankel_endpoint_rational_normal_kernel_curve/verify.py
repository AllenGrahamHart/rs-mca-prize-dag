#!/usr/bin/env python3
"""Tiny checks for the strict-endpoint rational-normal kernel curve."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_endpoint_rational_normal_kernel_curve"


def check_dimensions(m: int) -> None:
    residual = 8 * m
    locator_degree = 4 * m - 1
    rank = locator_degree
    rows = residual - locator_degree
    columns = locator_degree + 1
    assert rows == 4 * m + 1
    assert columns == 4 * m
    assert columns - rank == 1
    assert rows - rank == 2
    assert residual + 1 - 2 * rank == 3
    regular_size = rank - 3 * m
    assert regular_size == m - 1


def check_canonical_block(index: int) -> None:
    # Coefficients of (U^e,U^(e-1)V,...,V^e) are distinct basis vectors.
    coefficients = [tuple(int(i == j) for i in range(index + 1))
                    for j in range(index + 1)]
    assert len(set(coefficients)) == index + 1
    assert all(sum(vector) == 1 for vector in coefficients)


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert ("rate_half_ca_hankel_minimal_index_budget", NODE, "req") in edges
    assert (
        "rate_half_ca_hankel_endpoint_component_defect_localization",
        NODE,
        "req",
    ) in edges
    assert (NODE, "rate_half_band_closure", "ev") in edges

    target = nodes["rate_half_band_closure"]
    expected = f"background/nodes/{NODE}/statement.md"
    assert expected in target["refs"]


def main() -> None:
    for m in range(1, 129):
        check_dimensions(m)
        check_canonical_block(m)
    official_m = 1 << 37
    check_dimensions(official_m)
    assert 3 * official_m + 2 == 412_316_860_418
    assert 15 * official_m == 2_061_584_302_080
    assert 4 * official_m - 1 == 549_755_813_887
    check_dag()
    print(
        "RATE_HALF_CA_HANKEL_ENDPOINT_RATIONAL_NORMAL_KERNEL_CURVE_PASS "
        f"small_indices=128 official_m={official_m}"
    )


if __name__ == "__main__":
    main()
