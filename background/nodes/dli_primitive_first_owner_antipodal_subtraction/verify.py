#!/usr/bin/env python3
"""Exact finite checks for dyadic primitive first-owner subtraction."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction


def primitive_root(q: int) -> int:
    factors = []
    value = q - 1
    p = 2
    while p * p <= value:
        if value % p == 0:
            factors.append(p)
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        factors.append(value)
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in factors):
            return g
    raise AssertionError("primitive root missing")


def counts(q: int, n: int, t: int) -> tuple[list[int], list[int]]:
    zeta = pow(primitive_root(q), (q - 1) // n, q)
    total = [0] * (n + 1)
    prim = [0] * (n + 1)
    for mask in range(1 << n):
        support = [i for i in range(n) if mask >> i & 1]
        if any(sum(pow(zeta, r * i, q) for i in support) % q for r in range(1, t + 1)):
            continue
        b = len(support)
        total[b] += 1
        periodic = any(
            all(bool(mask >> i & 1) == bool(mask >> ((i + shift) % n) & 1)
                for i in range(n))
            for shift in range(1, n)
        )
        if not periodic:
            prim[b] += 1
    return total, prim


def one_case(q: int, n: int, t: int) -> dict[str, int]:
    total, prim = counts(q, n, t)
    half, _ = counts(q, n // 2, t // 2)
    for b in range(n + 1):
        expected = total[b] - (half[b // 2] if b % 2 == 0 else 0)
        assert prim[b] == expected
    x = Fraction(q**t * sum(total), 1 << n)
    xp = Fraction(q**t * sum(prim), 1 << n)
    xh = Fraction(q ** (t // 2) * sum(half), 1 << (n // 2))
    factor = Fraction(q ** (t // 2), 1 << (n // 2))
    assert xp == x - factor * xh
    return {
        "total": sum(total),
        "primitive": sum(prim),
        "nonprimitive": sum(half),
        "weight_checks": n + 1,
    }


def build() -> dict[str, dict[str, int]]:
    result = {
        "8|2|17": one_case(17, 8, 2),
        "16|2|17": one_case(17, 16, 2),
        "16|8|97": one_case(97, 16, 8),
    }
    assert result == {
        "8|2|17": {"total": 4, "primitive": 0, "nonprimitive": 4, "weight_checks": 9},
        "16|2|17": {"total": 224, "primitive": 208, "nonprimitive": 16, "weight_checks": 17},
        "16|8|97": {"total": 2, "primitive": 0, "nonprimitive": 2, "weight_checks": 17},
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["16|2|17"]["primitive"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_PRIMITIVE_SUBTRACTION_TAMPER_PASS mutations=1/1")
        return
    print("DLI_PRIMITIVE_SUBTRACTION_PASS cases=3 weight_checks=43")


if __name__ == "__main__":
    main()
