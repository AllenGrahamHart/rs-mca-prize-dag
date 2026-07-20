#!/usr/bin/env python3
"""Replay the distance-three dual row product and power-residue gate."""

from __future__ import annotations

from math import gcd, isqrt


def inv(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def poly_mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return out


def locator_coefficients(roots: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = poly_mul(out, [(-root) % prime, 1], prime)
    return out


def poly_eval(coefficients: list[int], x: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % prime
    return value


def locator(roots: tuple[int, ...], x: int, prime: int) -> int:
    return poly_eval(locator_coefficients(roots, prime), x, prime)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def positive_fixture() -> tuple[int, int]:
    prime = 17
    roots_a = (2, 5)
    triple = (3, 13, 15)
    active = (4, 9, 11, 6, 7, 10, 8, 12, 16)
    external = (15, 2, 4)
    internal = 1
    rank_degree = 3

    a_poly = locator_coefficients(roots_a, prime) + [0]
    b_poly = locator_coefficients(triple, prime)
    q_1 = [(right - left) % prime for left, right in zip(a_poly, b_poly, strict=True)]
    p_z = locator_coefficients(external, prime)

    leading_product = 1
    for x in active:
        leading_product = leading_product * poly_eval(q_1, x, prime) % prime

    for z in range(prime):
        row_product = 1
        for x in active:
            q_x = (poly_eval(a_poly, x, prime) + z * poly_eval(q_1, x, prime)) % prime
            row_product = row_product * q_x % prime
        expected = leading_product * pow(poly_eval(p_z, z, prime), rank_degree, prime) % prime
        assert row_product == expected

    residue = 1
    for x in active:
        residue = residue * locator(triple, x, prime) % prime
        residue = residue * inv(locator(roots_a, x, prime), prime) % prime
    witness = poly_eval(p_z, internal, prime) * inv(poly_eval(p_z, 0, prime), prime) % prime
    assert residue == pow(witness, rank_degree, prime)
    return residue, leading_product


def negative_prefilter_fixture() -> tuple[int, int]:
    prime = 241
    exponent = 5
    omega = 113
    assert pow(omega, 24, prime) == 1
    assert pow(omega, 12, prime) != 1
    assert pow(omega, 8, prime) != 1

    domain = []
    value = 1
    for _ in range(24):
        domain.append(value)
        value = value * omega % prime
    assert len(set(domain)) == 24

    roots_a = (113, 237, 30, 16)
    triple = (121, 177, 239)
    omitted = 15
    active = tuple(
        x for x in domain[1:] if x not in roots_a + triple + (omitted,)
    )
    pair = roots_a[:2]
    assert len(active) == 15

    residue = 1
    for x in active:
        residue = residue * locator(triple, x, prime) % prime
        residue = residue * inv(locator(pair, x, prime), prime) % prime
    gate_value = pow(residue, (prime - 1) // gcd(exponent, prime - 1), prime)
    assert residue == 174
    assert gate_value == 91 != 1
    return residue, gate_value


def main() -> None:
    e = 2**38 - 1
    rank_degree = 2**39 - 1
    e_factors = (3, 174763, 524287)
    r_factors = (7, 79, 8191, 121369)
    assert all(is_prime(value) for value in e_factors + r_factors)
    assert e == 3 * 174763 * 524287
    assert rank_degree == 7 * 79 * 8191 * 121369
    assert gcd(e, rank_degree) == 1

    residue, leading_product = positive_fixture()
    mutation, gate_value = negative_prefilter_fixture()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "DISTANCE_THREE_DUAL_ROW_PRODUCT_POWER_ROUTER_PASS "
        f"positive_residue={residue} leading_product={leading_product} "
        f"negative_residue={mutation} negative_gate={gate_value}"
    )


if __name__ == "__main__":
    main()
