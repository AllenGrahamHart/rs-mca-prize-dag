#!/usr/bin/env python3
"""Verify the extremal marked constant-shift kernel normal form."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_marked_constant_shift_extremal_kernel_normal_form"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(out)


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % prime
    return trim(out)


def divmod_poly(
    numerator: list[int], denominator: list[int], prime: int
) -> tuple[list[int], list[int]]:
    remainder = trim(numerator[:])
    denominator = trim(denominator[:])
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, prime)
    while len(remainder) >= len(denominator) and remainder != [0]:
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse % prime
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + shift] = (
                remainder[index + shift] - coefficient * value
            ) % prime
        trim(remainder)
    return trim(quotient), trim(remainder)


def gcd_poly(left: list[int], right: list[int], prime: int) -> list[int]:
    left, right = trim(left[:]), trim(right[:])
    while right != [0]:
        _, remainder = divmod_poly(left, right, prime)
        left, right = right, remainder
    inverse = pow(left[-1], -1, prime)
    return [(value * inverse) % prime for value in left]


def rref_nullspace(rows: list[list[int]], prime: int) -> tuple[int, list[list[int]]]:
    matrix = [[entry % prime for entry in row] for row in rows]
    pivot_columns: list[int] = []
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = [(entry * inverse) % prime for entry in matrix[rank]]
        for index, row in enumerate(matrix):
            if index == rank or not row[column]:
                continue
            factor = row[column]
            matrix[index] = [
                (left - factor * right) % prime
                for left, right in zip(row, matrix[rank])
            ]
        pivot_columns.append(column)
        rank += 1
    free_columns = [
        column for column in range(len(matrix[0])) if column not in pivot_columns
    ]
    basis = []
    for free in free_columns:
        vector = [0] * len(matrix[0])
        vector[free] = 1
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = (-matrix[row][free]) % prime
        basis.append(vector)
    return rank, basis


def locator(labels: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for label in labels:
        out = mul(out, [(-label) % prime, 1], prime)
    return out


def compose_xell(poly: list[int], ell: int) -> list[int]:
    out = [0] * ((len(poly) - 1) * ell + 1)
    for index, value in enumerate(poly):
        out[index * ell] = value
    return trim(out)


def main() -> None:
    checks = 0
    matrix_cases = 0
    sharp_cases = 0

    # Every two-dimensional full-row-rank kernel determinant is either zero
    # or a scalar multiple of the complete label locator. Saturation rules out
    # the zero case in the theorem.
    for m, prime in ((1, 5), (2, 5)):
        labels = tuple(range(2 * m))
        q_poly = locator(labels, prime)
        for values in itertools.product(range(prime), repeat=2 * m):
            rows = []
            for label, value in zip(labels, values):
                powers = [pow(label, exponent, prime) for exponent in range(m + 1)]
                rows.append(
                    [(-value * power) % prime for power in powers] + powers
                )
            rank, basis = rref_nullspace(rows, prime)
            if rank != 2 * m:
                continue
            assert len(basis) == 2
            a0, b0 = basis[0][: m + 1], basis[0][m + 1 :]
            a1, b1 = basis[1][: m + 1], basis[1][m + 1 :]
            delta = add(mul(a0, b1, prime), [(-x) % prime for x in mul(a1, b0, prime)], prime)
            if delta != [0]:
                kappa = delta[-1]
                assert delta == [(kappa * value) % prime for value in q_poly]
                checks += 1
            matrix_cases += 1
            checks += 2
    assert matrix_cases > 100

    # Replay finite specializations of the sharp family.
    prime = 29
    for m in range(1, 4):
        labels = tuple(range(1, 2 * m + 1))
        u = locator(labels[:m], prime)
        v_poly = locator(labels[m:], prime)
        for ell in range(2, 6):
            for cofactor in range(1, ell):
                w = compose_xell(u, ell)
                v_of_p = compose_xell(v_poly, ell)
                chosen = None
                for lam in range(1, prime):
                    twist = [0] * cofactor + [lam]
                    f = add([1], mul(twist, v_of_p, prime), prime)
                    if len(gcd_poly(f, w, prime)) == 1:
                        chosen = (lam, f)
                        break
                assert chosen is not None
                _, f = chosen
                assert len(f) - 1 == m * ell + cofactor
                assert len(w) - 1 == m * ell
                for index, label in enumerate(labels):
                    divisor = [(-label) % prime] + [0] * (ell - 1) + [1]
                    value = 0 if index < m else sum(
                        coefficient * pow(label, exponent, prime)
                        for exponent, coefficient in enumerate(u)
                    ) % prime
                    difference = add(w, [(-value * x) % prime for x in f], prime)
                    _, remainder = divmod_poly(difference, divisor, prime)
                    assert remainder == [0]
                    checks += 1
                sharp_cases += 1
                checks += 3
    assert sharp_cases == 30

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge["kind"])
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_marked_constant_shift_multistrip_exclusion",
        "pma_saturated_mixed_support_kernel",
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

    statement = (
        ROOT / "background" / "nodes" / NODE / "statement.md"
    ).read_text()
    for anchor in (
        "rank exactly `2m`",
        "A_0B_1-A_1B_0=kappa Q",
        "F=1+lambda X^cV(P)",
    ):
        assert anchor in statement
        checks += 1

    print(
        "L1_EXTREMAL_KERNEL_PASS "
        f"checks={checks} matrices={matrix_cases} sharp={sharp_cases}"
    )


if __name__ == "__main__":
    main()
