#!/usr/bin/env python3
"""Check the h=7 cubic two-triple exclusion identities."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_two_triple_exclusion"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_two_triple_reduction"
CONSUMER = "l1_mixed_petal_amplification"

Poly = list[Fraction]


def trim(poly: Poly) -> Poly:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def scale(poly: Poly, scalar: Fraction) -> Poly:
    return trim([scalar * value for value in poly])


def sub(left: Poly, right: Poly) -> Poly:
    return add(left, scale(right, Fraction(-1)))


def mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def main() -> None:
    d = [0, 1]
    d2 = mul(d, d)
    s = [3, 3, 1]
    S = [9, 9, 2]

    # Check 16d^4 times the W^2 coefficient difference. Its r and r^2
    # coefficients are respectively 4ds and d^2.
    l4_r = scale(mul(d, [23, 7, 1]), Fraction(1, 4))
    factorization_r = mul(d, [5, 1])
    assert scale(sub(l4_r, factorization_r), 16) == scale(mul(d, s), 4)
    assert scale(
        sub(scale(d2, Fraction(1, 8)), scale(d2, Fraction(1, 16))), 16
    ) == d2

    # Substitute r=-4s/d into the conic; its d factors cancel exactly.
    conic_substitution = add(
        add(scale(mul(s, s), 560), scale(mul([27, 27, 11], s), -56)),
        scale([3, 6, 7, 4, 1], 120),
    )
    assert conic_substitution == scale(mul(s, S), 32)

    # Substitute into q_2 r^2+q_1 r+q_0 from the dependency.
    hnf_substitution = add(
        add(
            scale(mul([7, 5], mul(s, s)), 80),
            scale(mul([480, 845, 540, 130], s), -4),
        ),
        [720, 2076, 2724, 1956, 744, 120],
    )
    assert hnf_substitution == scale(mul(mul(d, [2, 1]), S), -8)
    assert mul([3, 2], [3, 1]) == S

    official_primes = (8191, 131071, 524287, 2147483647)
    assert all(prime % 8 == 7 for prime in official_primes)
    assert all(prime not in {2, 5, 13} for prime in official_primes)

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(CTE1)", "(CTE2)", "9/4"):
        assert anchor in statement
    for anchor in ("32sS", "-8d(d+2)S", "2,5,13"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_TWO_TRIPLE_EXCLUSION_PASS rows=4")


if __name__ == "__main__":
    main()
