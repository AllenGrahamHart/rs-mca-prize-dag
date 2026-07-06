#!/usr/bin/env python3
"""Small PMA auxiliary-list falsification probe.

This probes the toy window recorded in the PMA ledger:

    F_109, ell = 3, d = 5.

For fixed defect locator L_D and scalar-per-petal targets c_i L_D(x), enumerate
degree <= d auxiliary polynomials by interpolation from d+1 agreement points.
Small M rows are exact; the M=12 wide row is sampled with checkpoints so a
timeout still leaves evidence.
"""

from __future__ import annotations

import itertools
import json
import random
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "pma_aux_list_results.json"

P = 109
ELL = 3
D_DEG = 5
SIGMA = ELL - 1
AGREE_THRESHOLD = D_DEG + 1 + SIGMA


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
    if (p - 1) % n:
        raise ValueError(f"{n=} does not divide {p - 1=}")
    z = pow(primitive_root(p), (p - 1) // n, p)
    H = [pow(z, i, p) for i in range(n)]
    if len(set(H)) != n:
        raise AssertionError("wrong subgroup order")
    return H


def eval_poly(coeffs: tuple[int, ...], x: int) -> int:
    value = 0
    for c in reversed(coeffs):
        value = (value * x + c) % P
    return value


def solve_interpolation(xs: list[int], ys: list[int]) -> tuple[int, ...] | None:
    n = D_DEG + 1
    A = [[pow(xs[i], j, P) for j in range(n)] + [ys[i] % P] for i in range(n)]
    r = 0
    for c in range(n):
        pivot = None
        for i in range(r, n):
            if A[i][c] % P:
                pivot = i
                break
        if pivot is None:
            return None
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c], -1, P)
        A[r] = [(v * inv) % P for v in A[r]]
        for i in range(n):
            if i != r and A[i][c] % P:
                factor = A[i][c] % P
                A[i] = [(A[i][j] - factor * A[r][j]) % P for j in range(n + 1)]
        r += 1
    return tuple(A[i][n] % P for i in range(n))


def make_aux_word(M: int) -> tuple[list[int], dict[int, int], list[int]]:
    H = subgroup(P, ELL * M)
    image = sorted({pow(x, ELL, P) for x in H})
    if len(image) != M:
        raise AssertionError("wrong petal quotient")
    outside = [x for x in range(1, P) if x not in set(H)]
    D = outside[:D_DEG]

    def locator(x: int) -> int:
        value = 1
        for root in D:
            value = (value * (x - root)) % P
        return value

    word: dict[int, int] = {}
    for i, alpha in enumerate(image):
        scalar = i + 1
        fiber = [x for x in H if pow(x, ELL, P) == alpha]
        if len(fiber) != ELL:
            raise AssertionError("wrong fiber size")
        for x in fiber:
            word[x] = scalar * locator(x) % P
    return sorted(word), word, D


def probe_row(M: int, sample_limit: int | None, rng: random.Random) -> dict:
    points, word, D = make_aux_word(M)
    values = [word[x] for x in points]
    total_combos = 1
    for a in range(len(points) - D_DEG, len(points) + 1):
        total_combos *= a
    for a in range(1, D_DEG + 2):
        total_combos //= a

    exact = sample_limit is None or total_combos <= sample_limit
    if exact:
        combos = itertools.combinations(range(len(points)), D_DEG + 1)
        checked_budget = total_combos
    else:
        seen_combos: set[tuple[int, ...]] = set()

        def sampled():
            while len(seen_combos) < sample_limit:
                combo = tuple(sorted(rng.sample(range(len(points)), D_DEG + 1)))
                if combo not in seen_combos:
                    seen_combos.add(combo)
                    yield combo

        combos = sampled()
        checked_budget = sample_limit

    candidates: dict[tuple[int, ...], int] = {}
    checked = 0
    start = time.time()
    for combo in combos:
        coeffs = solve_interpolation([points[i] for i in combo], [values[i] for i in combo])
        checked += 1
        if coeffs is None or coeffs in candidates:
            continue
        agreement = sum(eval_poly(coeffs, x) == word[x] for x in points)
        if agreement >= AGREE_THRESHOLD:
            candidates[coeffs] = agreement
    max_agreement = max(candidates.values(), default=0)
    johnson_safe = AGREE_THRESHOLD * AGREE_THRESHOLD > D_DEG * len(points)
    return {
        "M": M,
        "field": P,
        "ell": ELL,
        "d": D_DEG,
        "D": D,
        "points": len(points),
        "agreement_threshold": AGREE_THRESHOLD,
        "johnson_safe": johnson_safe,
        "total_interpolation_subsets": total_combos,
        "checked_interpolation_subsets": checked,
        "checked_budget": checked_budget,
        "exact": exact,
        "list_count_at_threshold": len(candidates),
        "max_agreement": max_agreement,
        "wall_seconds": round(time.time() - start, 6),
    }


def checkpoint(results: dict) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def main() -> int:
    rng = random.Random(20260706)
    results = {
        "started_at_unix": time.time(),
        "node": "petal_mixed_amplification / pma_wide_residual",
        "rows": [],
    }
    checkpoint(results)
    for M, sample_limit in [(4, None), (6, None), (9, None), (12, 200_000)]:
        results["rows"].append(probe_row(M, sample_limit, rng))
        checkpoint(results)
    results["status"] = "PASS"
    results["wall_seconds"] = round(time.time() - results["started_at_unix"], 6)
    checkpoint(results)
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
