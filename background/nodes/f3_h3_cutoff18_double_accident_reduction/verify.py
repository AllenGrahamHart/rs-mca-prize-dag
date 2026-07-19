#!/usr/bin/env python3
"""Exact replay for the C36' cutoff-18 double-accident reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_cutoff18_double_accident_reduction"
CONSUMER = "f3_h3_mobius_excess_half"
DEPENDENCY = "f3_h3_shifted_product_sidon"


def q18(product_fiber: int) -> int:
    return max(product_fiber - 18, 0)


def profile_terms(profile: list[tuple[int, int]]) -> tuple[int, int, int]:
    x18 = sum(q18(p) * r for p, r in profile)
    single = sum(q18(p) for p, r in profile if r > 0)
    double = sum(q18(p) * max(r - 1, 0) for p, r in profile)
    return x18, single, double


def main() -> None:
    point_checks = 0
    for product_fiber in range(0, 65):
        for quotient_fiber in range(0, 33):
            profile = [(product_fiber, quotient_fiber)]
            x18, single, double = profile_terms(profile)
            assert x18 == single + double
            point_checks += 1

    fixtures = [
        [(20, 1), (20, 1)],
        [(40, 0), (19, 2), (36, 7), (18, 30)],
        [(0, 0), (18, 1), (19, 1), (19, 5)],
    ]
    fixture_checks = 0
    for profile in fixtures:
        x18, single, double = profile_terms(profile)
        assert x18 == single + double
        assert single <= sum(p for p, _ in profile)
        fixture_checks += 1

    boundary_x, boundary_single, boundary_y = profile_terms([(20, 1), (20, 1)])
    assert (boundary_x, boundary_single, boundary_y) == (4, 4, 0)

    constant_checks = 0
    for exponent in range(13, 42):
        n = 1 << exponent
        exact_residual = 300 * n * n - 17 * (n - 1) ** 2
        assert exact_residual == 283 * n * n + 34 * n - 17
        assert 17 * 16 * n * n <= exact_residual
        assert 17 * (n - 1) ** 2 + exact_residual == 300 * n * n
        constant_checks += 1

    # Two tempting incorrect splits are detected by explicit profiles.
    p, r = 20, 0
    assert q18(p) * r != q18(p) + q18(p) * max(r - 1, 0)
    p, r = 20, 1
    assert q18(p) * r != q18(p) * max(r - 1, 0)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] in ("TARGET", "CONDITIONAL")  # 2026-07-19 amber re-pose
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "F3_H3_CUTOFF18_DOUBLE_ACCIDENT_REDUCTION_PASS "
        f"point_checks={point_checks} fixture_checks={fixture_checks} "
        f"constant_checks={constant_checks} boundary_X18={boundary_x} "
        f"boundary_Y18={boundary_y} mutation_controls=2"
    )


if __name__ == "__main__":
    main()
