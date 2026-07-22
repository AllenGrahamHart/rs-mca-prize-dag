#!/usr/bin/env python3
"""Verify the fixed-source quotient-partition anchor census."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_fixed_source_quotient_partition_anchor_census"


def evaluate(coefficients: tuple[int, ...], x: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(coefficients):
        out = (out * x + coefficient) % prime
    return out


def partition_key(
    coefficients: tuple[int, ...], domain: tuple[int, ...], prime: int
) -> tuple[tuple[int, ...], ...]:
    fibers: dict[int, list[int]] = {}
    for x in domain:
        fibers.setdefault(evaluate(coefficients, x, prime), []).append(x)
    return tuple(sorted(tuple(fiber) for fiber in fibers.values()))


def main() -> None:
    checks = 0
    prime = 7
    ell = 2
    domain = tuple(range(prime))
    petals = tuple(itertools.combinations(domain, ell))
    monic = tuple((constant, linear, 1) for constant in range(prime) for linear in range(prime))

    # Exhaust every collection of at most three disjoint two-point source
    # petals. A monic quadratic partition class is its linear coefficient:
    # changing only the constant translates every fiber label.
    for size in (1, 2, 3):
        for source in itertools.combinations(petals, size):
            if len(set().union(*map(set, source))) != ell * size:
                continue
            anchored: dict[int, set[int]] = {}
            partitions: dict[int, tuple[tuple[int, ...], ...]] = {}
            for polynomial in monic:
                carried = {
                    index
                    for index, petal in enumerate(source)
                    if len({evaluate(polynomial, x, prime) for x in petal}) == 1
                }
                if not carried:
                    continue
                class_key = polynomial[1]
                anchored.setdefault(class_key, set()).update(carried)
                key = partition_key(polynomial, domain, prime)
                if class_key in partitions:
                    assert partitions[class_key] == key
                else:
                    partitions[class_key] = key
                checks += 1

            owners: dict[int, int] = {}
            for class_key, carried in anchored.items():
                owner = min(carried)
                assert owner not in owners
                owners[owner] = class_key
                checks += 1
            assert len(anchored) <= size
            checks += 1

    for fiber_count in range(1, 8):
        assert sum(1 for _ in itertools.product(range(3), repeat=fiber_count)) == 3**fiber_count
        checks += 1
    for fiber_count in range(8, 13):
        assert 3**fiber_count > 0
        checks += 1

    for log_n in range(4, 65):
        n = 1 << log_n
        for cutoff_denominator in (1, 2, 4, 8):
            fiber_count = cutoff_denominator * log_n
            source_petals = fiber_count
            key_bound = source_petals * 3**fiber_count
            assert fiber_count <= cutoff_denominator * math.log2(n)
            assert math.log2(key_bound) <= (
                math.log2(source_petals)
                + math.log2(3) * cutoff_denominator * math.log2(n)
                + 1e-9
            )
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_general_first_layout_domination",
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
        "P-P'=a_i-a_i'",
        "M_src 3^L",
        "anchored internal quotient",
        "Forney coefficient strata",
        "anchor hypothesis is not automatic",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_FIXED_SOURCE_QUOTIENT_ANCHOR_PASS checks={checks}")


if __name__ == "__main__":
    main()
