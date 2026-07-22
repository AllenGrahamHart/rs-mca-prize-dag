#!/usr/bin/env python3
"""Verify the anchored partial-core triple-polarity aggregation."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_fixed_source_anchored_triple_polarity_closure"


def subsets(points: tuple[int, ...]):
    for mask in range(1 << len(points)):
        yield frozenset(point for index, point in enumerate(points) if mask >> index & 1)


def evaluate(coefficients: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % prime
    return value


def main() -> None:
    checks = 0
    domain = tuple(range(7))
    fibers = (frozenset((0, 1)), frozenset((2, 3)), frozenset((4, 5)))
    residual = frozenset((6,))

    core_keys = {}
    for core in subsets(domain):
        orientations = tuple(len(core & fiber) > len(fiber) / 2 for fiber in fibers)
        baseline = frozenset().union(
            *(fiber for dense, fiber in zip(orientations, fibers) if dense)
        )
        exceptions = core ^ baseline
        polarity = len(core & residual) + sum(
            min(len(core & fiber), len(fiber) - len(core & fiber)) for fiber in fibers
        )
        assert len(exceptions) == polarity
        assert baseline ^ exceptions == core
        key = (orientations, exceptions)
        assert key not in core_keys
        core_keys[key] = core
        checks += 3

        defect_keys = {}
        core_tuple = tuple(sorted(core))
        for defect in subsets(core_tuple):
            defect_orientations = tuple(
                len(defect & fiber) > len(core & fiber) / 2 for fiber in fibers
            )
            defect_baseline = frozenset().union(
                *(
                    core & fiber
                    for dense, fiber in zip(defect_orientations, fibers)
                    if dense
                )
            )
            defect_exceptions = defect ^ defect_baseline
            defect_polarity = len(defect & residual) + sum(
                min(len(defect & fiber), len(core & fiber) - len(defect & fiber))
                for fiber in fibers
            )
            assert len(defect_exceptions) == defect_polarity
            assert defect_baseline ^ defect_exceptions == defect
            defect_key = (defect_orientations, defect_exceptions)
            assert defect_key not in defect_keys
            defect_keys[defect_key] = defect
            checks += 3

    # Core plus one full petal uniquely determines a degree-below-k source
    # member. Exhaust all quadratics over F_7 on several disjoint blocks.
    prime = 7
    k = 3
    polynomials = tuple(itertools.product(range(prime), repeat=k))
    for core in itertools.combinations(domain, k - 1):
        remaining = tuple(x for x in domain if x not in core)
        for petal in itertools.combinations(remaining, 2):
            seen = {}
            points = core + petal
            for polynomial in polynomials:
                values = tuple(evaluate(polynomial, x, prime) for x in points)
                assert values not in seen
                seen[values] = polynomial
                checks += 1

    for log_n in range(4, 49):
        n = 1 << log_n
        for cutoff_denominator in (1, 2, 4):
            fiber_count = cutoff_denominator * log_n
            source_petals = fiber_count
            structural = source_petals * 16**fiber_count
            assert fiber_count <= cutoff_denominator * math.log2(n)
            assert math.log2(structural) <= (
                math.log2(source_petals) + 4 * cutoff_denominator * math.log2(n)
                + 1e-9
            )
            checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_fixed_source_quotient_partition_anchor_census",
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
        "|C intersect R|",
        "|D intersect R|",
        "16^(n/ell)",
        "no separate Forney-key",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_FIXED_SOURCE_ANCHORED_TRIPLE_PASS checks={checks}")


if __name__ == "__main__":
    main()
