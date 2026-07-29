#!/usr/bin/env python3
"""Verify the finite-field and DAG parts of the J_65 Harbater proof."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_qzeta128_p257_j65_harbater_nonprincipality"
JOIN = "e1_qzeta128_p257_two_involution_nonprincipality_certificate"
P = 257

# Low-to-high coefficients of the Elkies polynomial in Dembele, Remark 6.2.
H = [
    68,
    -2,
    -128,
    16,
    80,
    40,
    32,
    -80,
    -32,
    64,
    0,
    -16,
    16,
    8,
    0,
    0,
    -2,
    1,
]


def trim(poly: list[int]) -> list[int]:
    poly = [value % P for value in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def divmod_poly(left: list[int], right: list[int]) -> tuple[list[int], list[int]]:
    left = trim(left)
    right = trim(right)
    assert right != [0]
    quotient = [0] * max(1, len(left) - len(right) + 1)
    inverse = pow(right[-1], -1, P)
    while left != [0] and len(left) >= len(right):
        shift = len(left) - len(right)
        scale = left[-1] * inverse % P
        quotient[shift] = scale
        for index, value in enumerate(right):
            left[index + shift] = (left[index + shift] - scale * value) % P
        left = trim(left)
    return trim(quotient), left


def gcd_poly(left: list[int], right: list[int]) -> list[int]:
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = divmod_poly(left, right)
        left, right = right, remainder
    scale = pow(left[-1], -1, P)
    return trim([scale * value for value in left])


def mul_mod(left: list[int], right: list[int], modulus: list[int]) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % P
    return divmod_poly(product, modulus)[1]


def pow_mod(base: list[int], exponent: int, modulus: list[int]) -> list[int]:
    result = [1]
    base = divmod_poly(base, modulus)[1]
    while exponent:
        if exponent & 1:
            result = mul_mod(result, base, modulus)
        base = mul_mod(base, base, modulus)
        exponent >>= 1
    return result


def sub(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[index] if index < len(left) else 0)
            - (right[index] if index < len(right) else 0)
            for index in range(size)
        ]
    )


def main() -> None:
    modulus = trim(H)
    assert len(modulus) - 1 == 17
    x = [0, 1]

    # Rabin's criterion. Since 17 is prime, only the proper divisor 1 occurs.
    x_to_p = pow_mod(x, P, modulus)
    assert gcd_poly(modulus, sub(x_to_p, x)) == [1]
    frobenius = x
    for _ in range(17):
        frobenius = pow_mod(frobenius, P, modulus)
    assert frobenius == x

    assert P % 64 == 1
    assert 248 == P - 9
    assert 9 * 9 % P == 248 * 248 % P == 81

    node_dir = ROOT / "background/nodes" / NODE
    proof = (node_dir / "proof.md").read_text()
    source = (node_dir / "source_evidence.md").read_text()
    for text in ("Remark 6.2", "Artin", "N_(L/E)(J_65)=p^2"):
        assert text in proof
    for text in ("10.2140/ant.2020.14.2807", "Section 5.2", "Theorem 6.4"):
        assert text in source

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[JOIN]["status"] == "PROVED"
    assert (NODE, JOIN, "req") in edges

    print(
        "E1_QZETA128_P257_J65_HARBATER_NONPRINCIPALITY_PASS "
        "degree=17 modulus=257 factorization=irreducible"
    )


if __name__ == "__main__":
    main()
