#!/usr/bin/env python3
"""Check the parity-reduced evaluation identity on formal basis terms."""

from __future__ import annotations


Monomial = tuple[int, int, int]
Polynomial = dict[Monomial, int]


def add(*values: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for value in values:
        for monomial, coefficient in value.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def scale(value: Polynomial, coefficient: int) -> Polynomial:
    return {monomial: coefficient * current for monomial, current in value.items() if coefficient * current}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for (ul, vl, zl), cl in left.items():
        for (ur, vr, zr), cr in right.items():
            monomial = (ul + ur, vl + vr, zl + zr)
            result[monomial] = result.get(monomial, 0) + cl * cr
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def term(u: int, v: int, z: int, coefficient: int = 1) -> Polynomial:
    return {} if coefficient == 0 else {(u, v, z): coefficient}


R = add(term(2, 0, 0), term(0, 1, 1, -1))


def quotient_term(degree: int, index: int, odd_sign: int = -1) -> Polynomial:
    half = index // 2
    if half == 0:
        return {}
    geometric = add(*(
        term(2 * (half - 1 - power), power, power)
        for power in range(half)
    ))
    if index % 2 == 0:
        return multiply(term(0, degree - index, 0), geometric)
    return scale(
        multiply(term(1, degree - index, 0), geometric),
        odd_sign,
    )


def identity_holds(degree: int, index: int, odd_sign: int = -1) -> bool:
    direct_sign = -1 if index % 2 else 1
    direct = term(index, degree - index, 0, direct_sign)
    half = index // 2
    if index % 2 == 0:
        reduced = term(0, degree - half, half)
    else:
        reduced = term(1, degree - half - 1, half, odd_sign)
    difference = add(direct, scale(reduced, -1))
    return difference == multiply(R, quotient_term(degree, index, odd_sign))


def main() -> None:
    cases = [(degree, index) for degree in range(13) for index in range(degree + 1)]
    assert all(identity_holds(degree, index) for degree, index in cases)
    assert any(not identity_holds(degree, index, 1) for degree, index in cases if index % 2)
    print(f"KB_C2_112_PARITY_REDUCED_EVALUATION_PASS cases={len(cases)} mutations=1/1")


if __name__ == "__main__":
    main()
