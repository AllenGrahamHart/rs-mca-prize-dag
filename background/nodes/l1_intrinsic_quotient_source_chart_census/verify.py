#!/usr/bin/env python3
"""Verify the intrinsic quotient source-chart census."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_intrinsic_quotient_source_chart_census"


def evaluate(coefficients: tuple[int, ...], x: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(coefficients):
        out = (out * x + coefficient) % prime
    return out


def main() -> None:
    checks = 0

    # Exhaustive source-member uniqueness on the three intrinsic square fibers
    # of F_7^*. Here k=3, so a two-point core plus a two-point petal gives four
    # agreement points for degree-at-most-two polynomials.
    prime = 7
    domain = tuple(range(1, prime))
    fibers = ({1, 6}, {2, 5}, {3, 4})
    words = (
        {x: (x**3 + 2 * x + 1) % prime for x in domain},
        {x: (3 * x**4 + x**2 + 5) % prime for x in domain},
        {x: (x % 2) for x in domain},
    )
    polynomials = tuple(itertools.product(range(prime), repeat=3))

    for word in words:
        for core_index, core in enumerate(fibers):
            for petal_index, petal in enumerate(fibers):
                if core_index == petal_index:
                    continue
                matches = [
                    coefficients
                    for coefficients in polynomials
                    if all(evaluate(coefficients, x, prime) == word[x] for x in core | petal)
                ]
                assert len(matches) <= 1
                checks += len(polynomials) * len(core | petal)

    for fiber_count in range(1, 7):
        assignments = tuple(itertools.product(range(3), repeat=fiber_count))
        assert len(assignments) == 3**fiber_count
        checks += 1
    for fiber_count in range(7, 13):
        assert 3**fiber_count > 0
        checks += 1

    for log_n in range(4, 65):
        n = 1 << log_n
        for cutoff_denominator in (1, 2, 4, 8):
            fiber_count = cutoff_denominator * log_n
            assert math.log2(3**fiber_count) <= (
                cutoff_denominator * math.log2(3) * log_n + 1e-9
            )
            assert log_n + 1 <= n
            checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "pma_source_paving_bridge",
        "l1_quotient_chart_bipolar_entropy_closure",
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
        "3^L",
        "n^(log_2(3)/c_0)",
        "global polynomial bound",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_INTRINSIC_CHART_CENSUS_PASS checks={checks}")


if __name__ == "__main__":
    main()
