#!/usr/bin/env python3
"""Light GAP-1/TR telescope stress checks.

The check models functions on a small cyclic evaluation subgroup H.  For
K_M-stability, the r-th isotypic character space is spanned by

    x^r F(x^M).

For an active set R, the joint telescope claim says that all characters in R
sit inside the single K_D-isotypic space where

    D = gcd(M, {r-r0 : r in R}).

Equality should hold exactly when R is the full congruence class r0 mod D.
"""

from __future__ import annotations

import json
import math
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "gap1_telescope_results.json"


def factor_int(n: int) -> list[int]:
    factors: list[int] = []
    d = 2
    value = n
    while d * d <= value:
        if value % d == 0:
            factors.append(d)
            while value % d == 0:
                value //= d
        d += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(p: int) -> int:
    factors = factor_int(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in factors):
            return g
    raise ValueError(f"no primitive root for {p}")


def subgroup(p: int, n: int) -> list[int]:
    g = pow(primitive_root(p), (p - 1) // n, p)
    H = [pow(g, i, p) for i in range(n)]
    if len(set(H)) != n:
        raise AssertionError("wrong subgroup order")
    return H


def rank_mod(rows: list[list[int]], p: int) -> int:
    if not rows:
        return 0
    A = [row[:] for row in rows]
    m = len(A)
    n = len(A[0])
    r = 0
    for c in range(n):
        pivot = None
        for i in range(r, m):
            if A[i][c] % p:
                pivot = i
                break
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c] % p, -1, p)
        A[r] = [(v * inv) % p for v in A[r]]
        for i in range(m):
            if i != r and A[i][c] % p:
                factor = A[i][c] % p
                A[i] = [(A[i][j] - factor * A[r][j]) % p for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def char_space_basis(H: list[int], p: int, M: int, r: int) -> list[list[int]]:
    quotient_size = len(H) // M
    return [
        [(pow(x, r, p) * pow(pow(x, M, p), a, p)) % p for x in H]
        for a in range(quotient_size)
    ]


def span_rank_for_chars(H: list[int], p: int, M: int, chars: list[int]) -> int:
    rows: list[list[int]] = []
    for r in chars:
        rows.extend(char_space_basis(H, p, M, r))
    return rank_mod(rows, p)


def in_span_rank(H: list[int], p: int, M: int, subset: list[int], full: list[int]) -> tuple[int, int]:
    rows_subset: list[list[int]] = []
    rows_full: list[list[int]] = []
    for r in subset:
        rows_subset.extend(char_space_basis(H, p, M, r))
    for r in full:
        rows_full.extend(char_space_basis(H, p, M, r))
    return rank_mod(rows_subset, p), rank_mod(rows_full + rows_subset, p)


def check_case(p: int, n: int, M: int, R: list[int]) -> dict:
    H = subgroup(p, n)
    r0 = R[0]
    D = M
    for r in R[1:]:
        D = math.gcd(D, (r - r0) % M)
    if D == 0:
        D = M
    full_class = [r for r in range(M) if (r - r0) % D == 0]

    rank_R = span_rank_for_chars(H, p, M, R)
    expected_rank_R = len(set(R)) * (n // M)
    if rank_R != expected_rank_R:
        raise AssertionError((p, n, M, R, rank_R, expected_rank_R))

    rank_full = span_rank_for_chars(H, p, M, full_class)
    expected_full = n // D
    if rank_full != expected_full:
        raise AssertionError((p, n, M, R, D, rank_full, expected_full))

    rank_R, rank_full_plus_R = in_span_rank(H, p, M, R, full_class)
    contained = rank_full_plus_R == rank_full
    equality = rank_R == rank_full
    expected_equality = set(R) == set(full_class)
    if not contained or equality != expected_equality:
        raise AssertionError(
            {
                "p": p,
                "n": n,
                "M": M,
                "R": R,
                "D": D,
                "full_class": full_class,
                "rank_R": rank_R,
                "rank_full": rank_full,
                "contained": contained,
                "equality": equality,
                "expected_equality": expected_equality,
            }
        )

    # Negative control: using a strictly larger divisor as if it were the
    # joint stabilizer should fail containment whenever possible.
    bad_divisor_detected = False
    for D_bad in sorted(d for d in range(D + 1, M + 1) if M % d == 0):
        bad_class = [r for r in range(M) if (r - r0) % D_bad == 0]
        if not set(R).issubset(bad_class):
            _, rank_bad_plus_R = in_span_rank(H, p, M, R, bad_class)
            rank_bad = span_rank_for_chars(H, p, M, bad_class)
            if rank_bad_plus_R > rank_bad:
                bad_divisor_detected = True
                break

    return {
        "p": p,
        "n": n,
        "M": M,
        "R": R,
        "D": D,
        "full_class_size": len(full_class),
        "rank_R": rank_R,
        "rank_telescoped": rank_full,
        "contained": contained,
        "equality": equality,
        "negative_bad_divisor_detected": bad_divisor_detected,
    }


def main() -> int:
    started = time.time()
    cases = [
        (97, 24, 6, [1, 3, 5]),
        (97, 24, 6, [1, 4]),
        (97, 24, 8, [2, 6]),
        (97, 24, 8, [1, 3]),
        (193, 32, 8, [1, 3, 5, 7]),
        (193, 32, 8, [1, 5]),
        (193, 32, 8, [1, 3]),
        (193, 32, 16, [3, 7, 11, 15]),
        (193, 32, 16, [2, 10]),
        (193, 32, 16, [3, 7]),
    ]
    results = {
        "started_at_unix": started,
        "node": "gap1_product_model / tr_joint_telescope",
        "cases": [],
    }
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    for case in cases:
        results["cases"].append(check_case(*case))
        OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    results["status"] = "PASS"
    results["wall_seconds"] = round(time.time() - started, 6)
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
