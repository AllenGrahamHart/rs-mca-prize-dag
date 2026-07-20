#!/usr/bin/env python3
"""Verify the quotient-chart bounded core-boundary closure."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_quotient_chart_bounded_core_boundary_closure"


def support_encoding_check(petal_count: int, ell: int, cap: int) -> int:
    points = tuple(range(petal_count * ell))
    petals = tuple(
        frozenset(range(index * ell, (index + 1) * ell))
        for index in range(petal_count)
    )
    encodings: set[tuple[tuple[bool, ...], tuple[int, ...]]] = set()
    accepted = 0

    for mask in range(1 << len(points)):
        support = {point for point in points if mask >> point & 1}
        dense = tuple(len(support & petal) > ell / 2 for petal in petals)
        baseline = set().union(
            *(petal for bit, petal in zip(dense, petals) if bit)
        ) if any(dense) else set()
        exceptions = tuple(sorted(support ^ baseline))
        polarity = sum(min(len(support & petal), ell - len(support & petal)) for petal in petals)
        assert len(exceptions) == polarity
        if polarity <= cap:
            key = (dense, exceptions)
            assert key not in encodings
            encodings.add(key)
            reconstructed = set(baseline) ^ set(exceptions)
            assert reconstructed == support
            accepted += 1

    bound = 2**petal_count * sum(math.comb(len(points), e) for e in range(cap + 1))
    assert accepted <= bound
    return accepted


def defect_encoding_check(core_fibers: int, ell: int, cap: int) -> int:
    fibers = tuple(
        frozenset(range(index * ell, (index + 1) * ell))
        for index in range(core_fibers)
    )
    points = tuple(range(core_fibers * ell))
    encodings: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    accepted = 0

    for mask in range(1 << len(points)):
        defect = {point for point in points if mask >> point & 1}
        full = tuple(index for index, fiber in enumerate(fibers) if fiber <= defect)
        full_points = set().union(*(fibers[index] for index in full)) if full else set()
        boundary = tuple(sorted(defect - full_points))
        if len(boundary) <= cap:
            key = (boundary, full)
            assert key not in encodings
            encodings.add(key)
            reconstructed = set(boundary) | full_points
            assert reconstructed == defect
            accepted += 1

    bound = 2**core_fibers * sum(math.comb(len(points), beta) for beta in range(cap + 1))
    assert accepted <= bound
    return accepted


def main() -> None:
    checks = 0
    profiles = 0
    for petal_count, ell, cap in ((2, 2, 1), (3, 2, 2), (2, 3, 2)):
        assert support_encoding_check(petal_count, ell, cap) > 0
        profiles += 1
        checks += 1
    for core_fibers, ell, cap in ((2, 2, 1), (3, 2, 2), (2, 3, 2)):
        assert defect_encoding_check(core_fibers, ell, cap) > 0
        profiles += 1
        checks += 1

    # Exact arithmetic for the displayed cutoff exponent.
    for log_n in range(8, 81):
        n = 1 << log_n
        for cutoff_denominator in (1, 2, 4, 8):
            fiber_cap = cutoff_denominator * log_n
            for total_fibers in (0, fiber_cap // 2, fiber_cap):
                assert 2**total_fibers <= n**cutoff_denominator
                checks += 1
        for polarity_cap, boundary_cap, gamma in itertools.product(range(4), repeat=3):
            q = n**gamma
            left = n ** (polarity_cap + boundary_cap) * q ** (2 * polarity_cap)
            right = n ** (polarity_cap + boundary_cap + 2 * gamma * polarity_cap)
            assert left == right
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_marked_common_pencil_quotient_boundary_router",
        "l1_marked_common_pencil_next_strip_boundary_fiber_bound",
        "l1_polarized_petal_entropy_ledger",
        "petal_reserve_rich_fiber_reduction",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in (
        "l1_mixed_residual_intersection_pin",
        "l1_mixed_petal_amplification",
        "petal_mixed_amplification",
    ):
        assert (NODE, consumer, "ev") in edges
        checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "2^(M+N) n^(P_0+B_0) q^(2P_0)",
        "n^(1/c_0+P_0+B_0+2 gamma P_0)",
        "per-source-chart closure",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_BOUNDED_BOUNDARY_PASS checks={checks} profiles={profiles}")


if __name__ == "__main__":
    main()
