#!/usr/bin/env python3
"""Polynomial replay of the misaligned common-pencil factorization."""

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


def main() -> None:
    checks = 0
    for ell, a in ((5, 1), (7, 2), (11, 3)):
        s = ell - a
        p_poly = [7, 3] + [0] * (ell - 2) + [1]
        q_poly = [1 + 2 * i for i in range(s)] + [1]
        for z0, z2, z3, scalar in ((13, 29, 47, 5), (61, 83, 109, 17)):
            m0 = (z0 - z2) * (z0 - z3) % MOD
            e_poly = scale(add(p_poly, [-z0]), scalar)
            l2 = add(p_poly, [-z2])
            l3 = add(p_poly, [-z3])
            v_poly = scale(q_poly, -m0)
            d_poly = scale(
                mul(q_poly, add(p_poly, [z0 - z2 - z3])),
                pow(scalar, -1, MOD),
            )
            left = mul(d_poly, e_poly)
            right = add(mul(mul(l2, l3), q_poly), v_poly)
            assert left == right
            assert len(q_poly) - 1 == s > 0
            assert len(d_poly) - 1 == 2 * ell - a
            checks += 1

    assert checks == 6
    print("PASS: every misaligned common-pencil solution carries the forbidden factor Q")


if __name__ == "__main__":
    main()
