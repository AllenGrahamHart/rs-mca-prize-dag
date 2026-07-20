#!/usr/bin/env python3
"""Verify the even-Jacobi norm reduction for deleted-pair gcds."""

from __future__ import annotations

from fractions import Fraction
import json
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = (
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_"
    "even_jacobi_norm_router"
)
DEPENDENCY = (
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_trace_gcd_router"
)
CONSUMER = "rate_half_list_adjacent_crossing"


def generalized_binomial(value: Fraction, count: int) -> Fraction:
    numerator = Fraction(1)
    for index in range(count):
        numerator *= value - index
    return numerator / factorial(count)


def pochhammer(value: Fraction, count: int) -> Fraction:
    result = Fraction(1)
    for index in range(count):
        result *= value + index
    return result


def jacobi_value(
    degree: int, alpha: Fraction, beta: Fraction, value: Fraction
) -> Fraction:
    left = (value - 1) / 2
    right = (value + 1) / 2
    return sum(
        generalized_binomial(degree + alpha, index)
        * generalized_binomial(degree + beta, degree - index)
        * left ** (degree - index)
        * right**index
        for index in range(degree + 1)
    )


def gegenbauer_value(degree: int, lam: Fraction, value: Fraction) -> Fraction:
    if degree == 0:
        return Fraction(1)
    previous = Fraction(1)
    current = 2 * lam * value
    for index in range(1, degree):
        following = (
            2 * (index + lam) * value * current
            - (index + 2 * lam - 1) * previous
        ) / (index + 1)
        previous, current = current, following
    return current


def chebyshev_t(degree: int, value: Fraction) -> Fraction:
    if degree == 0:
        return Fraction(1)
    previous, current = Fraction(1), value
    for _ in range(1, degree):
        previous, current = current, 2 * value * current - previous
    return current


def chebyshev_u(degree: int, value: Fraction) -> Fraction:
    if degree == 0:
        return Fraction(1)
    previous, current = Fraction(1), 2 * value
    for _ in range(1, degree):
        previous, current = current, 2 * value * current - previous
    return current


def quadratic_transform_checks() -> None:
    x = Fraction(2, 3)
    w = 2 * x * x - 1
    lam = Fraction(1, 4)
    checked = 0
    for m in range(1, 8):
        ell = 2 * m
        scalar = pochhammer(lam, m) / pochhammer(Fraction(1, 2), m)
        assert gegenbauer_value(2 * m, lam, x) == scalar * jacobi_value(
            m, Fraction(-1, 4), Fraction(-1, 2), w
        )
        assert jacobi_value(
            2 * ell - 1, Fraction(0), Fraction(0), x
        ) == x * jacobi_value(
            ell - 1, Fraction(0), Fraction(1, 2), w
        )
        assert chebyshev_t(2 * ell, x) == chebyshev_t(ell, w)
        assert chebyshev_u(2 * ell - 1, x) == 2 * x * chebyshev_u(
            ell - 1, w
        )
        checked += 1
    assert checked == 7


def branch_norm_checks() -> None:
    p = 101
    checked = 0
    mutation_tripped = False
    for x in (2, 3, 7, 11, 19):
        z = x * x % p
        for q in (4, 9, 23):
            for sign in (1, 10):
                r_value = x * q % p
                original = [
                    (r_value + sign) ** 2 - 2 * sign**2 * (x + 1),
                    2 * (r_value + sign) ** 2
                    - (x + 1) * (r_value - sign) ** 2,
                    (x + 1) * (r_value - sign) ** 2 - 8 * sign**2,
                ]
                a = [
                    z * q * q - sign**2,
                    z * q * q + 2 * sign * z * q + sign**2,
                    z * q * q - 2 * sign * z * q - 7 * sign**2,
                ]
                b = [
                    2 * sign * (q - sign),
                    6 * sign * q - z * q * q - sign**2,
                    z * q * q - 2 * sign * q + sign**2,
                ]
                for index in range(3):
                    assert original[index] % p == (a[index] + x * b[index]) % p
                    conjugate = (a[index] - x * b[index]) % p
                    norm = (a[index] * a[index] - z * b[index] * b[index]) % p
                    assert original[index] % p * conjugate % p == norm
                broken_a2 = z * q * q - 2 * sign * z * q - 6 * sign**2
                if original[2] % p != (broken_a2 + x * b[2]) % p:
                    mutation_tripped = True
                checked += 1
    assert checked == 30
    assert mutation_tripped


def official_degree_check() -> None:
    m = 1 << 35
    ell = 1 << 36
    assert ell == 2 * m
    assert (2 * ell - 1) == (1 << 37) - 1
    assert m < ell


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "w=2x^2-1",
        "Q(w)=J_(L-1)^(0,1/2)(w) mod J(w)",
        "F_(j,s)=A_j^2-zB_j^2",
        "M=L/2=2^35",
        "does not prove any gcd",
    ):
        assert marker in statement
    for marker in (
        "E_(j,s)(x)=A_j(w)+xB_j(w)",
        "E_(j,s)(x)E_(j,s)(-x)",
        "harmless factor `2x`",
        "official values are `M=2^35`, `L=2^36`",
    ):
        assert marker in proof


def main() -> None:
    official_degree_check()
    quadratic_transform_checks()
    branch_norm_checks()
    packet_check()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_ANTIPODAL_GENERIC_DELETED_PAIR_EVEN_JACOBI_NORM_ROUTER_PASS "
        "official=1 transforms=7 norm_cells=30 degree_halving=1 mutation=1"
    )


if __name__ == "__main__":
    main()
