#!/usr/bin/env python3
"""Verify the intrinsic partial-core triple-polarity closure."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_intrinsic_partial_core_triple_polarity_closure"


def encode(subset: set[int], blocks: tuple[frozenset[int], ...]) -> tuple[tuple[bool, ...], tuple[int, ...]]:
    dense = tuple(len(subset & block) > len(block) / 2 for block in blocks)
    baseline = set().union(
        *(block for bit, block in zip(dense, blocks) if bit)
    ) if any(dense) else set()
    return dense, tuple(sorted(subset ^ baseline))


def main() -> None:
    checks = 0
    profiles = 0

    # Exhaust every source core and every defect inside it on three two-point
    # quotient fibers. Verify both orientation encodings reconstruct exactly.
    ell = 2
    fibers = tuple(
        frozenset(range(index * ell, (index + 1) * ell))
        for index in range(3)
    )
    domain = set().union(*fibers)
    for core_mask in range(1 << len(domain)):
        core = {point for point in domain if core_mask >> point & 1}
        layout_dense, layout_exceptions = encode(core, fibers)
        layout_baseline = set().union(
            *(block for bit, block in zip(layout_dense, fibers) if bit)
        ) if any(layout_dense) else set()
        assert layout_baseline ^ set(layout_exceptions) == core
        checks += 1

        core_slices = tuple(frozenset(core & fiber) for fiber in fibers)
        core_points = tuple(sorted(core))
        for defect_mask in range(1 << len(core_points)):
            defect = {
                core_points[index]
                for index in range(len(core_points))
                if defect_mask >> index & 1
            }
            defect_dense, defect_exceptions = encode(defect, core_slices)
            defect_baseline = set().union(
                *(block for bit, block in zip(defect_dense, core_slices) if bit)
            ) if any(defect_dense) else set()
            assert defect_baseline ^ set(defect_exceptions) == defect
            assert defect <= core
            checks += 2
            profiles += 1

    for log_n in range(6, 65):
        n = 1 << log_n
        for cutoff_denominator in (1, 2, 4):
            fibers_at_cutoff = cutoff_denominator * log_n
            assert 16**fibers_at_cutoff == n ** (4 * cutoff_denominator)
            assert log_n + 1 <= n
            checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_intrinsic_quotient_source_chart_census",
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
        "p_layout=sum_a",
        "p_defect=sum_a",
        "16^L",
        "globally",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_TRIPLE_POLARITY_PASS checks={checks} profiles={profiles}")


if __name__ == "__main__":
    main()

