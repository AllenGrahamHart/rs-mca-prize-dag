#!/usr/bin/env python3
"""Classify the h=6 n=64 p4993 witnesses as square-lifted h=3 trades."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"
EXTRA = NOTES / "f3_h6_n64_extra_primes_certificate.json"


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
    g = primitive_root(p)
    z = pow(g, (p - 1) // n, p)
    if pow(z, n, p) != 1 or pow(z, n // 2, p) == 1:
        raise AssertionError((p, n, z))
    return [pow(z, i, p) for i in range(n)]


def decode_mask(mask: int, n: int) -> tuple[int, ...]:
    return tuple(i for i in range(n) if (mask >> i) & 1)


def elementary_signature(exponents: tuple[int, ...], vals: list[int], p: int) -> tuple[int, ...]:
    coeffs = [1]
    for exponent in exponents:
        x = vals[exponent]
        coeffs.append(0)
        for i in range(len(coeffs) - 1, 0, -1):
            coeffs[i] = (coeffs[i] + coeffs[i - 1] * x) % p
    return tuple(coeffs[1:])


def antipodal_quotient(exponents: tuple[int, ...], n: int = 64) -> tuple[int, ...]:
    half = n // 2
    q = sorted({e % half for e in exponents})
    if len(q) * 2 != len(exponents):
        raise AssertionError(("not paired", exponents, q))
    if tuple(sorted(q + [e + half for e in q])) != tuple(sorted(exponents)):
        raise AssertionError(("not antipodal", exponents, q))
    return tuple(q)


def h3_anchored_trades(p: int = 4993, n: int = 32) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    vals = root_table(p, n)
    by_prefix: dict[tuple[int, int], list[tuple[tuple[int, ...], int]]] = {}
    for a, b in combinations(range(1, n), 2):
        left = (0, a, b)
        sig = elementary_signature(left, vals, p)
        by_prefix.setdefault(sig[:2], []).append((left, sig[2]))

    trades = set()
    for right in combinations(range(1, n), 3):
        sig = elementary_signature(right, vals, p)
        for left, last in by_prefix.get(sig[:2], []):
            if set(left) & set(right):
                continue
            if last == sig[2]:
                continue
            trades.add((tuple(left), tuple(right)))
    return trades


def lift_h3_trade(trade: tuple[tuple[int, ...], tuple[int, ...]]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return tuple(tuple(sorted(side + tuple(e + 32 for e in side))) for side in trade)  # type: ignore[return-value]


def main() -> None:
    rows = json.loads(EXTRA.read_text())
    row = next(row for row in rows if row["p"] == 4993)
    witnesses = row["witnesses"]
    vals64 = root_table(4993, 64)
    vals32 = root_table(4993, 32)

    descended = set()
    lifted = set()
    for witness in witnesses:
        left = decode_mask(witness["left_mask"], 64)
        right = decode_mask(witness["right_mask"], 64)
        sig_left = elementary_signature(left, vals64, 4993)
        sig_right = elementary_signature(right, vals64, 4993)
        if sig_left[:5] != sig_right[:5] or sig_left[5] == sig_right[5]:
            raise AssertionError(("bad h6 signature", left, right, sig_left, sig_right))
        qleft = antipodal_quotient(left)
        qright = antipodal_quotient(right)
        qsig_left = elementary_signature(qleft, vals32, 4993)
        qsig_right = elementary_signature(qright, vals32, 4993)
        if qsig_left[:2] != qsig_right[:2] or qsig_left[2] == qsig_right[2]:
            raise AssertionError(("bad h3 descent", qleft, qright, qsig_left, qsig_right))
        descended.add((qleft, qright))
        lifted.add((left, right))

    all_h3 = h3_anchored_trades()
    all_lifts = {lift_h3_trade(trade) for trade in all_h3}
    if descended != all_h3:
        raise AssertionError(("descended mismatch", descended, all_h3))
    if lifted != all_lifts:
        raise AssertionError(("lift mismatch", lifted, all_lifts))

    print("h=3 n32 p4993 anchored trades:", len(all_h3))
    print("h=6 n64 p4993 witnesses:", len(witnesses))
    print("all h=6 p4993 witnesses are antipodal square-lifts of h=3 quotient trades")
    print("H6_P4993_SQUARE_LIFT_ANALYSIS_PASS")


if __name__ == "__main__":
    main()
