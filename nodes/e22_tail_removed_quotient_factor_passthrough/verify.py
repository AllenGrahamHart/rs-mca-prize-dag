#!/usr/bin/env python3
"""Small polynomial check for tail-removal factor passthrough."""

from __future__ import annotations


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] += av * bv
    return trim(out)


def div_exact(num: list[int], den: list[int]) -> list[int]:
    num = num[:]
    den = trim(den[:])
    if len(num) < len(den):
        raise AssertionError("degree too small")
    quot = [0] * (len(num) - len(den) + 1)
    while len(num) >= len(den):
        shift = len(num) - len(den)
        lead = num[-1]
        assert lead % den[-1] == 0
        coeff = lead // den[-1]
        quot[shift] = coeff
        for i, dv in enumerate(den):
            num[shift + i] -= coeff * dv
        trim(num)
    assert num == [0]
    return trim(quot)


def linear(root: int) -> list[int]:
    return [-root, 1]


def quotient_factor(M: int, z: int) -> list[int]:
    return [-z] + [0] * (M - 1) + [1]


def prod(polys: list[list[int]]) -> list[int]:
    out = [1]
    for poly in polys:
        out = mul(out, poly)
    return out


def main() -> None:
    tail_locator = linear(3)
    q_factors = [quotient_factor(2, 1), quotient_factor(2, 4)]
    non_tail_locator = prod(q_factors)
    touched_locator = mul(tail_locator, non_tail_locator)
    cofactor_rest = mul(linear(-5), [2, 0, 1])
    H = mul(touched_locator, cofactor_rest)

    tail_removed = div_exact(H, tail_locator)
    assert div_exact(tail_removed, non_tail_locator) == cofactor_rest
    for factor in q_factors:
        div_exact(tail_removed, factor)

    print("PASS: tail removal preserves quotient factors")


if __name__ == "__main__":
    main()
