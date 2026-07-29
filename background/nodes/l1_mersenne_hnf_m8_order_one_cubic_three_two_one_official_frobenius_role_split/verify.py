#!/usr/bin/env python3
"""Check the official quadratic Frobenius-role packet compiler."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_official_frobenius_role_split"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_galois_role_weld",
    "l1_mersenne_next_to_maximal_exceptional_reduction",
}
CONSUMER = "l1_mixed_petal_amplification"
PRIMES = (8191, 131071, 524287, 2147483647)


def ext_add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def ext_mul(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def poly_mul(
    left: tuple[tuple[int, int], ...], right: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, int], ...]:
    out = [(0, 0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = ext_add(out[i + j], ext_mul(a, b))
    return tuple(out)


SIGNED_QUADRATICS = (
    (((1, 0), (0, 1), (1, 0)), (1, 0, 0, 0, 1), 1),
    (((2, -1), (0, 1), (1, 0)), (2, 4, 2, 0, 1), 1),
    (((3, 2), (0, 0), (1, 0)), (1, 0, 6, 0, 1), 1),
    (((4, 2), (2, 0), (1, 0)), (8, 16, 12, 4, 1), 1),
    (((3, 2), (2, 1), (1, 0)), (1, 4, 8, 4, 1), 1),
    (((2, 1), (2, 1), (1, 0)), (2, 4, 6, 4, 1), 1),
    (((2, 1), (2, 0), (2, 0)), (1, 4, 6, 4, 2), 2),
    (((2, 1), (2, 2), (2, 0)), (1, 0, 2, 4, 2), 2),
    (((2, 1), (4, 2), (4, 0)), (1, 4, 12, 16, 8), 2),
)


def conjugate(poly: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    return tuple((a, -b) for a, b in poly)


def main() -> None:
    for plus, expected, scalar in SIGNED_QUADRATICS:
        product = poly_mul(plus, conjugate(plus))
        assert product == tuple((scalar * value, 0) for value in expected)

    base_quadratics = ((2, 2, 1), (1, 0, 1), (1, 2, 2))
    assert 2 * (len(base_quadratics) + 2 * len(SIGNED_QUADRATICS)) == 42

    for prime in PRIMES:
        assert prime % 8 == 7
        square_root = pow(2, (prime + 1) // 4, prime)
        assert square_root * square_root % prime == 2
        for coefficients in base_quadratics:
            discriminant = (coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]) % prime
            assert pow(discriminant, (prime - 1) // 2, prime) == prime - 1
        for plus, _, _ in SIGNED_QUADRATICS:
            for sign in (1, -1):
                values = [(a + sign * b * square_root) % prime for a, b in plus]
                discriminant = (values[1] ** 2 - 4 * values[0] * values[2]) % prime
                assert pow(discriminant, (prime - 1) // 2, prime) == prime - 1

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(FRS1)", "(FRS2)", "(FRS3)", "(FRS4)"):
        assert anchor in statement
    for anchor in ("3*2+18*2=42", "lambda^p", "beta=gamma"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_OFFICIAL_FROBENIUS_ROLE_SPLIT_PASS")


if __name__ == "__main__":
    main()
