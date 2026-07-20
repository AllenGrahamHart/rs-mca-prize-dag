#!/usr/bin/env python3
"""Verify the quotient-chart bipolar entropy closure."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_quotient_chart_bipolar_entropy_closure"


def encode_subsets(block_count: int, ell: int, cap: int) -> tuple[int, int]:
    blocks = tuple(
        frozenset(range(index * ell, (index + 1) * ell))
        for index in range(block_count)
    )
    point_count = block_count * ell
    encodings: set[tuple[tuple[bool, ...], tuple[int, ...]]] = set()
    accepted = 0
    checks = 0

    for mask in range(1 << point_count):
        subset = {point for point in range(point_count) if mask >> point & 1}
        dense = tuple(len(subset & block) > ell / 2 for block in blocks)
        baseline = set().union(
            *(block for bit, block in zip(dense, blocks) if bit)
        ) if any(dense) else set()
        exceptions = tuple(sorted(subset ^ baseline))
        polarity = sum(min(len(subset & block), ell - len(subset & block)) for block in blocks)
        assert len(exceptions) == polarity
        checks += 1

        if polarity <= cap:
            key = (dense, exceptions)
            assert key not in encodings
            encodings.add(key)
            assert baseline ^ set(exceptions) == subset
            accepted += 1
            checks += 2

    bound = 2**block_count * sum(math.comb(point_count, size) for size in range(cap + 1))
    assert accepted <= bound
    checks += 1
    return checks, accepted


def main() -> None:
    checks = 0
    profiles = 0
    for block_count, ell, cap in ((2, 2, 1), (3, 2, 2), (2, 3, 2), (2, 4, 2)):
        profile_checks, accepted = encode_subsets(block_count, ell, cap)
        assert accepted > 0
        checks += profile_checks + 1
        profiles += 1

    for log_n in range(8, 65):
        n = 1 << log_n
        for cutoff_denominator in (1, 2, 4):
            total_fibers = cutoff_denominator * log_n
            assert 2**total_fibers == n**cutoff_denominator
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_polarized_petal_entropy_ledger",
        "l1_marked_common_pencil_crt_fiber_bound",
        "l1_marked_common_pencil_next_strip_boundary_fiber_bound",
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
        "p_core=sum_(core fibers T_a)",
        "2^(M+N) n^(P_0+B_0) q^(2P_0)",
        "strictly sharpens",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_BIPOLAR_ENTROPY_PASS checks={checks} profiles={profiles}")


if __name__ == "__main__":
    main()

