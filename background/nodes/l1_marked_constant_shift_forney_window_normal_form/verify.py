#!/usr/bin/env python3
"""Verify the marked common-pencil Forney-window normal form."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_marked_constant_shift_forney_window_normal_form"


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


def rank_mod(rows: list[list[int]], prime: int) -> int:
    matrix = [[entry % prime for entry in row] for row in rows]
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
        rank += 1
    return rank


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
    prime = 101
    checks = 0
    strata = 0
    sharp_cases = 0

    for m in range(1, 6):
        for t in range(1, 2 * m + 1):
            labels = tuple(range(1, t + 1))
            q_poly = locator(labels, prime)
            for mu in range(max(0, t - m), t // 2 + 1):
                nu = t - mu
                assert mu <= nu <= m
                assert (m - mu + 1) + (m - nu + 1) == 2 * m - t + 2

                u = locator(labels[:mu], prime)
                v_poly = locator(labels[mu:], prime)
                determinant = [(-value) % prime for value in mul(u, v_poly, prime)]
                assert determinant == [(-value) % prime for value in q_poly]

                values = [0] * mu + [
                    sum(
                        coefficient * pow(label, exponent, prime)
                        for exponent, coefficient in enumerate(u)
                    )
                    % prime
                    for label in labels[mu:]
                ]
                rows = []
                for label, value in zip(labels, values):
                    powers = [pow(label, exponent, prime) for exponent in range(m + 1)]
                    rows.append(
                        [(-value * power) % prime for power in powers] + powers
                    )
                assert rank_mod(rows, prime) == t
                checks += 4

                for ell in (2, 3, 5):
                    for cofactor in range(1, ell):
                        residual_degree = m - nu
                        r_poly = [2] + [0] * (residual_degree - 1) + [1]
                        if residual_degree == 0:
                            r_poly = [1]
                        w = compose_xell(u, ell)
                        rv = mul(r_poly, v_poly, prime)
                        rv_of_p = compose_xell(rv, ell)
                        chosen = None
                        for lam in range(1, prime):
                            twist = [0] * cofactor + [lam]
                            f = add([1], mul(twist, rv_of_p, prime), prime)
                            if len(gcd_poly(f, w, prime)) == 1:
                                chosen = f
                                break
                        assert chosen is not None
                        f = chosen
                        assert len(f) - 1 == m * ell + cofactor
                        for index, label in enumerate(labels):
                            divisor = [(-label) % prime] + [0] * (ell - 1) + [1]
                            value = values[index]
                            difference = add(
                                w, [(-value * coefficient) % prime for coefficient in f], prime
                            )
                            _, remainder = divmod_poly(difference, divisor, prime)
                            assert remainder == [0]
                            checks += 1
                        sharp_cases += 1
                        checks += 2
                strata += 1
    assert strata == 50
    assert sharp_cases == 350

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
        "mu<=nu<=m,       mu+nu=t",
        "2m-t+2",
        "F=1+lambda X^cR(P)V(P)",
    ):
        assert anchor in statement
        checks += 1

    print(
        "L1_FORNEY_WINDOW_PASS "
        f"checks={checks} strata={strata} sharp={sharp_cases}"
    )


if __name__ == "__main__":
    main()
