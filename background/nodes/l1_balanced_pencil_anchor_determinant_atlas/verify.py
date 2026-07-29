#!/usr/bin/env python3
"""Tiny exact checks for the balanced-pencil determinant atlas."""

from itertools import combinations, product
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def rank_f2(rows: tuple[int, ...], width: int) -> int:
    work = list(rows)
    rank = 0
    for bit in reversed(range(width)):
        pivot = next((i for i in range(rank, len(work)) if work[i] >> bit & 1), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for i in range(len(work)):
            if i != rank and (work[i] >> bit) & 1:
                work[i] ^= work[rank]
        rank += 1
    return rank


def check_loopless_matroid_floor() -> None:
    for r in range(1, 4):
        nonzero_rows = range(1, 1 << r)
        for h in range(r, 6):
            for rows in product(nonzero_rows, repeat=h):
                if rank_f2(rows, r) != r:
                    continue
                bases = sum(
                    rank_f2(tuple(rows[i] for i in idx), r) == r
                    for idx in combinations(range(h), r)
                )
                assert bases >= h - r + 1


def check_parameter_identities() -> int:
    checks = 0
    for n in range(8, 33):
        for k in range(1, n):
            for m in range(k + 1, n + 1):
                s = n - 2 * m + k
                if s < 1:
                    continue
                w = m - k
                omega = n - m
                for d1 in range(w + 1, (omega + w + 1) // 2 + 1):
                    d2 = omega + w + 1 - d1
                    if d2 > omega:
                        continue
                    alpha = omega - d1
                    beta = omega - d2
                    assert alpha + beta == s - 1
                    checks += 1
                for j in range(min(k - 1, s - 1) + 1):
                    g = k - 1 - j
                    d = s - 1 - j
                    h = w + 1 + j
                    assert d == n - 2 * m + g
                    assert h == m - g == omega - d
                    for r in range(1, j + 2):
                        assert h - r + 1 == w + j - r + 2 > 0
                        assert comb(m, r) >= 1
                    checks += 1
    return checks


def main() -> None:
    check_loopless_matroid_floor()
    checks = check_parameter_identities()

    statement = (ROOT / "statement.md").read_text()
    proof = (ROOT / "proof.md").read_text()
    assert "gcd(Delta_0,W_0)=D" in statement
    assert "|C_D| <= floor( binom(m,r_D)/(h-r_D+1) )" in statement
    assert "may be exponential" in statement
    assert "A loopless rank-`r` matroid" in proof

    print(f"L1_BALANCED_PENCIL_ANCHOR_DETERMINANT_ATLAS_PASS checks={checks}")


if __name__ == "__main__":
    main()
