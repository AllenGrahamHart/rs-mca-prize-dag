#!/usr/bin/env python3
"""Polynomial replay of the low-multiplier prefix-ladder coordinates."""

from __future__ import annotations


MOD = 257


def trim(poly: list[int]) -> list[int]:
    out = [value % MOD for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * value for value in poly])


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % MOD
    return trim(out)


def divmod_poly(numerator: list[int], denominator: list[int]) -> tuple[list[int], list[int]]:
    remainder = trim(numerator)
    denominator = trim(denominator)
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, MOD)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse % MOD
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + shift] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def main() -> None:
    checks = 0
    for ell, a, e in ((7, 2, 2), (9, 2, 4), (11, 3, 7)):
        s = ell - a
        assert a <= e <= s
        l2 = [3, 1] + [0] * (ell - 2) + [1]
        l3 = [11, 2] + [0] * (ell - 2) + [1]
        m_poly = mul(l2, l3)
        e_poly = [5 + i for i in range(e)] + [7]
        leading = e_poly[-1]
        q_poly = [13 + 2 * i for i in range(e - a)] + [leading]
        tail = [17 + 3 * i for i in range(s - e + 1)]

        t_poly, remainder = divmod_poly(mul(m_poly, q_poly), e_poly)
        d_poly = add(t_poly, tail)
        v_poly = add(scale(remainder, -1), mul(e_poly, tail))
        assert mul(d_poly, e_poly) == add(mul(m_poly, q_poly), v_poly)
        assert len(d_poly) - 1 == 2 * ell - a
        assert d_poly[-1] == 1
        assert len(v_poly) - 1 <= s
        depth = (2 * ell - a) - (s - e) - 1
        assert depth == ell + e - 1
        assert depth - (e - a) == ell + a - 1
        checks += 1

    assert checks == 3
    print("PASS: exact low-multiplier prefix cells and ladder cancellation")


if __name__ == "__main__":
    main()
