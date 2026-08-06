#!/usr/bin/env python3
"""Probe the h=8 n=64 antipodal square-lift branch via h=4 on mu_32."""

from __future__ import annotations

from itertools import combinations


def prime_factors(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    g = 2
    while any(pow(g, (p - 1) // r, p) == 1 for r in factors):
        g += 1
    return g


def root_table(p: int, n: int) -> list[int]:
    z = pow(primitive_root(p), (p - 1) // n, p)
    if pow(z, n, p) != 1 or pow(z, n // 2, p) == 1:
        raise AssertionError((p, n, z))
    return [pow(z, i, p) for i in range(n)]


def signature(exponents: tuple[int, ...], vals: list[int], p: int) -> tuple[int, ...]:
    coeffs = [1]
    for exponent in exponents:
        x = vals[exponent]
        coeffs.append(0)
        for i in range(len(coeffs) - 1, 0, -1):
            coeffs[i] = (coeffs[i] + coeffs[i - 1] * x) % p
    return tuple(coeffs[1:])


def is_toral(exponents: tuple[int, ...], n: int, h: int) -> bool:
    if n % h:
        return False
    step = n // h
    residue = exponents[0] % step
    seen = set()
    for exponent in exponents:
        if exponent % step != residue:
            return False
        seen.add((exponent - residue) // step)
    return len(seen) == h


def h4_anchored_trade_counts(p: int, n: int = 32) -> dict:
    vals = root_table(p, n)
    lefts: dict[tuple[int, int, int], list[tuple[tuple[int, ...], int, bool]]] = {}
    for tail in combinations(range(1, n), 3):
        left = (0,) + tail
        sig = signature(left, vals, p)
        lefts.setdefault(sig[:3], []).append((left, sig[3], is_toral(left, n, 4)))

    total = 0
    toral = 0
    nontoral = 0
    for right in combinations(range(1, n), 4):
        sig = signature(right, vals, p)
        right_toral = is_toral(right, n, 4)
        for left, last, left_toral in lefts.get(sig[:3], []):
            if set(left) & set(right):
                continue
            if last == sig[3]:
                continue
            total += 1
            if left_toral and right_toral:
                toral += 1
            else:
                nontoral += 1
    return {"p": p, "total": total, "toral": toral, "nontoral": nontoral}


def main() -> None:
    rows = [h4_anchored_trade_counts(p) for p in (193, 262337, 4289)]
    expected = {
        193: {"total": 15, "toral": 7, "nontoral": 8},
        262337: {"total": 7, "toral": 7, "nontoral": 0},
        4289: {"total": 7, "toral": 7, "nontoral": 0},
    }
    for row in rows:
        for key, value in expected[row["p"]].items():
            if row[key] != value:
                raise AssertionError((row, key, value))
        print(
            f"p={row['p']} h4 quotient anchored trades: "
            f"total={row['total']} toral={row['toral']} nontoral={row['nontoral']}"
        )
    print("H8_N64_SQUARE_LIFT_PROBE_PASS")


if __name__ == "__main__":
    main()
