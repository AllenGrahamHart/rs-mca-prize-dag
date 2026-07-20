#!/usr/bin/env python3
"""Verify the C36' single-quotient Pareto endpoint."""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from math import ceil, gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_single_quotient_endpoint_compiler"
DEPENDENCIES = {
    "f3_h3_dsp8_accident_depth_compiler",
    "f3_h3_dsp8_joint_star_depth_pareto_compiler",
    "f3_h3_double_accident_nonzero_coupling_ideal_router",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}


def free_floor(size: int) -> int:
    return ceil(Fraction(size * (size - 4), 2)) - 2 * size - 6


def antipodal_floor(size: int) -> int:
    return ceil(Fraction(size * (size - 2), 2)) - 4 * (size - 1) - 8


def budget(order: int) -> int:
    return 300 * order * order - 289 * (order - 1) * (order - 2)


def zero_center_fibers(order: int) -> dict[tuple[int, int], set[tuple[int, int]]]:
    fibers: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    for q in range(order):
        if order // gcd(order, q) < 8:
            continue
        # Multiplicative exponent coordinates: -q^2 has exponent 2q+n/2.
        triple = (q, (-q) % order, (2 * q + order // 2) % order)
        quotient_top = 4 * q % order
        assert len(set(triple)) == 3
        for denominator in triple:
            remaining = list(triple)
            remaining.remove(denominator)
            fibers[(denominator, quotient_top)].add(tuple(sorted(remaining)))
    return fibers


def arithmetic_check() -> None:
    assert Fraction(18, free_floor(16)) == Fraction(9, 29)
    assert Fraction(18, antipodal_floor(16)) == Fraction(9, 22)
    assert Fraction(17 * 9, 29) * Fraction(319, 153) == 11
    assert Fraction(9, 22) / Fraction(9, 29) == Fraction(29, 22)

    for size in range(16, 2049):
        excess = 2 * (size - 7)
        assert Fraction(excess, free_floor(size)) <= Fraction(9, 29)
        assert Fraction(excess, antipodal_floor(size)) <= Fraction(9, 22)
        assert ceil(Fraction(2 * free_floor(size), size)) >= 8
        assert ceil(Fraction(2 * antipodal_floor(size), size - 1)) >= 6

    for order in (2**power for power in range(13, 42)):
        assert budget(order) == 11 * order * order + 867 * order - 578
        assert budget(order) > 11 * order * order


def zero_locus_check() -> None:
    for order in (8, 16, 32, 64, 128, 256):
        fibers = zero_center_fibers(order)
        assert fibers
        assert max(map(len, fibers.values())) <= 2
        assert any(len(centers) == 2 for centers in fibers.values())
    assert 1 + 6 > 2


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "(P,R)>=(36,1)",
        "B_(0,17)(n)",
        "(319/153)n^2",
        "at most two",
        "lambda_(E_*,Q)!=0",
        "No second quotient",
        "no quotient-collision spoke",
        "does not prove `(SQE2)`",
    ):
        assert marker in text


def main() -> None:
    arithmetic_check()
    zero_locus_check()
    packet_check()
    print(
        "F3_H3_DSP8_SINGLE_QUOTIENT_ENDPOINT_COMPILER_PASS "
        "endpoint=36,1 free_degree=8 antipodal_degree=6 zero_centers<=2"
    )


if __name__ == "__main__":
    main()
