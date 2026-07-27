#!/usr/bin/env python3
"""Exact route probe for the m=128, h=10, Haar-mask 011 residue."""

from __future__ import annotations

from math import comb, gcd


M = 128
PLUS = (13, 16, 17, 19, 26, 27, 36, 66, 86, 87)
MINUS = (23, 29, 38, 42, 50, 68, 81, 94, 102, 112)


def reduce_at_order(coefficients: list[int], order: int) -> list[int]:
    degree = order // 2
    out = [0] * degree
    for exponent, coefficient in enumerate(coefficients):
        quotient, residue = divmod(exponent, degree)
        out[residue] += coefficient if quotient % 2 == 0 else -coefficient
    return out


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def dyadic_norm(coefficients: list[int], order: int) -> int:
    """Compute Res(F, Phi_order) by the exact even/odd norm recursion."""
    current = reduce_at_order(coefficients, order)
    while order > 2:
        even = current[::2]
        odd = current[1::2]
        even_square = multiply(even, even)
        shifted_odd_square = [0] + multiply(odd, odd)
        length = max(len(even_square), len(shifted_odd_square))
        current = [
            (even_square[i] if i < len(even_square) else 0)
            - (shifted_odd_square[i] if i < len(shifted_odd_square) else 0)
            for i in range(length)
        ]
        order //= 2
        current = reduce_at_order(current, order)
    return current[0] - (current[1] if len(current) > 1 else 0)


def taylor_multiplicity_mod_two(occupied: tuple[int, ...]) -> int:
    degree = 0
    while sum(comb(exponent, degree) for exponent in occupied) % 2 == 0:
        degree += 1
    return degree


def main() -> None:
    assert len(PLUS) == len(MINUS) == 10
    assert set(PLUS).isdisjoint(MINUS)
    coefficients = [0] * M
    for exponent in PLUS:
        coefficients[exponent] = 1
    for exponent in MINUS:
        coefficients[exponent] = -1

    half = M // 2
    odd_energy = sum(
        (coefficients[index] - coefficients[index + half]) ** 2
        for index in range(half)
    )
    folded = [
        coefficients[index] + coefficients[index + half]
        for index in range(half)
    ]
    haar = []
    for _ in range(3):
        midpoint = len(folded) // 2
        haar.append(
            sum(
                (folded[index] - folded[index + midpoint]) ** 2
                for index in range(midpoint)
            )
        )
        folded = [
            folded[index] + folded[index + midpoint]
            for index in range(midpoint)
        ]
    assert (odd_energy, *haar) == (22, 22, 24, 0)

    occupied = tuple(sorted(PLUS + MINUS))
    nu = taylor_multiplicity_mod_two(occupied)
    assert nu == 9

    ratio_gcd = M
    for exponent in occupied:
        ratio_gcd = gcd(ratio_gcd, exponent - PLUS[0])
    assert ratio_gcd == 1
    assert all(
        ({(x + shift) % M for x in PLUS}, {(x + shift) % M for x in MINUS})
        != (set(PLUS), set(MINUS))
        for shift in range(1, M)
    )

    # Structural Phi_16 divisibility plus balance contributes 27 powers of two.
    energy_product = odd_energy**32 * haar[0] ** 16 * haar[1] ** 8
    assert energy_product > 1 << 235

    norms = tuple(abs(dyadic_norm(coefficients, order)) for order in (128, 64, 32))
    assert norms == (
        163860267515501318513702842715385299456,
        1601217110606336,
        65637581312,
    )
    joint_product = norms[0] * norms[1] * norms[2]
    assert joint_product < 1 << 235

    print(
        "F3_M128_JOINT_NORM_ROUTE_PROBE_PASS "
        f"energies={odd_energy},{haar[0]},{haar[1]} nu={nu} "
        f"energy_bits={energy_product.bit_length()} "
        f"joint_bits={joint_product.bit_length()}"
    )


if __name__ == "__main__":
    main()
