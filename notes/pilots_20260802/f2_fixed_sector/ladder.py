#!/usr/bin/env python3
"""C6/C7: the 1/p ceiling ladder FOR THE FIXED SECTOR, and its base-invariance.

C6 -- the deployed-windows pilot proved (REPORT.md:39) that a parity-homogeneous
      window's b-resolved cancellation saturates at log2 p, uniformly in the
      window size m.  Here the SAME exact ladder is run on the FIXED sector
      mu_{2^r} <= F_p^* (antipodally closed because -1 in mu_{2^r}, r >= 1) at
      parity-pure frequencies: if the fixed sector saturates too, it is inside
      the degenerate class, not a bigger hammer.

C7 -- the only channel by which the fixed sector can touch a moving rung's slice
      statistic is the scalar offset `base` in Z/2p (the fixed elements are
      always present, so they shift the carry argument and nothing else).  This
      stage sweeps ALL 2p values of base on a deployed rung window and reports
      the best achievable cancellation: if it stays <= log2 p, the fixed sector
      cannot pay any part of a rung's budget through that channel.
"""
from __future__ import annotations

import math
import os
import sys

sys.dont_write_bytecode = True
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import core as C  # noqa: E402


def dp_counts(p: int, deltas):
    """dp[b][r] = #{ b-subsets T : sum_{i in T} Delta_i = r mod 2p }.  EXACT."""
    two_p = 2 * p
    n = len(deltas)
    dp = [[0] * two_p for _ in range(n + 1)]
    dp[0][0] = 1
    for i, d in enumerate(deltas):
        nd = [[0] * two_p for _ in range(n + 1)]
        for b in range(i + 1):
            row = dp[b]
            ndb, ndb1 = nd[b], nd[b + 1]
            for r in range(two_p):
                v = row[r]
                if v:
                    ndb[r] += v
                    ndb1[(r + d) % two_p] += v
        dp = nd
    return dp


def V_from_counts(p, dp, b, base):
    two_p = 2 * p
    row = dp[b]
    return sum(row[r] * (1 if (base + r) % two_p < p else -1)
               for r in range(two_p) if row[r])


def bits_profile(p, dp, m, base):
    lo, hi = math.ceil(0.25 * m), math.floor(0.75 * m)
    best, worst = None, None
    for b in range(lo, hi + 1):
        v = V_from_counts(p, dp, b, base)
        if v == 0:
            continue
        x = math.log2(math.comb(m, b)) - math.log2(abs(v))
        best = x if best is None or x > best else best
        worst = x if worst is None or x < worst else worst
    return best, worst


# --------------------------------------------------------------------- C6 ----


def fixed_sector_window(p: int, r: int, coeffs: dict):
    """(Delta, base) for the fixed sector mu_{2^r} <= F_p^* with its antipodal
    pairing, at the F_p-frequency polynomial chi(x) = sum_l a_l x^l."""
    two_p = 2 * p
    n0 = 1 << r
    # generator of mu_{2^r} inside F_p^*
    g = 2
    while pow(g, (p - 1) // 2, p) != p - 1:
        g += 1
    h = pow(g, (p - 1) // n0, p)
    elts, cur = [], 1
    for _ in range(n0):
        elts.append(cur)
        cur = cur * h % p
    assert len(set(elts)) == n0
    reps, seen = [], set()
    for x in elts:
        if x in seen:
            continue
        reps.append(x)
        seen.add(x)
        seen.add((-x) % p)
    D, base = [], 0
    for x in reps:
        sp = sum(a * pow(x, l, p) for l, a in coeffs.items()) % p
        sm = sum(a * pow((-x) % p, l, p) for l, a in coeffs.items()) % p
        a1, a2 = C.sigma_of(p, sp), C.sigma_of(p, sm)
        D.append((a1 - a2) % two_p)
        base += a2
    return D, base % two_p, len(reps)


def stage_c6():
    rows = []
    cases = [(97, 5), (193, 6), (257, 8), (641, 7), (769, 8), (12289, 6),
             (12289, 7), (7681, 7)]
    for p, r in cases:
        if (p - 1) % (1 << r):
            print(f"skip p={p} r={r}")
            continue
        for tag, co in (("odd_monomial_l1", {1: 3}),
                        ("odd_multi_l1_l3", {1: 3, 3: 5}),
                        ("odd_multi_l1_l3_l5", {1: 1, 3: 2, 5: 7})):
            D, base, m = fixed_sector_window(p, r, co)
            if m > 128:
                continue
            allev = C.all_even(D)
            mr, kk = C.maxR_float(p, D)
            dp = dp_counts(p, D)
            best, worst = bits_profile(p, dp, m, base)
            rows.append({"p": p, "r": r, "n0": 1 << r, "m_pairs": m,
                         "case": tag, "all_delta_even": allev,
                         "flat_float": 1.0 - mr, "argmax_k": kk,
                         "log2_p": math.log2(p),
                         "best_central_bits": best, "worst_central_bits": worst,
                         "best_over_log2p": (best / math.log2(p)) if best else None,
                         "eta_if_worst": (worst / m) if worst else None})
            print(f"p={p:6d} r={r} m={m:4d} {tag:20s} allEven={allev} "
                  f"flat={1-mr:.4f} best={_f(best)} worst={_f(worst)} "
                  f"log2p={math.log2(p):.3f} best/log2p="
                  f"{_f(best/math.log2(p) if best else None)}")
    C.dump("C6_fixed_sector_ceiling.json", {"rows": rows})


# --------------------------------------------------------------------- C7 ----


def stage_c7():
    """Sweep every base in Z/2p on a deployed rung-1 window: the fixed sector's
    only channel into the rung's slice statistic."""
    rows = []
    for e in (4, 5, 6):
        p = C.official_shaped_prime(e)
        F = C.Fp2(p)
        fixed, mreps, freps = C.sectors(F, e)
        n_ord = 1 << (e + 1)
        for tag, co in (("K1_linear", {1: (1, 1)}),
                        ("K1_multi", {1: (2, 3), 3: (1, 5)}),
                        ("G_multi", {1: (1, 1), 2: (2, 3)})):
            D, base0 = C.window_of(F, co, mreps, n_ord)
            m = len(D)
            dp = dp_counts(p, D)
            best_all, worst_all = [], []
            for base in range(2 * p):
                b, w = bits_profile(p, dp, m, base)
                if b is not None:
                    best_all.append(b)
                    worst_all.append(w)
            rows.append({
                "e": e, "p": p, "m_pairs": m, "case": tag,
                "class": C.parity_class(co), "all_delta_even": C.all_even(D),
                "log2_p": math.log2(p),
                "actual_base": base0,
                "max_over_base_of_best_central_bits": max(best_all),
                "max_over_base_of_worst_central_bits": max(worst_all),
                "min_over_base_of_worst_central_bits": min(worst_all),
                "ratio_max_worst_to_log2p": max(worst_all) / math.log2(p),
                "eta_best_achievable_over_base": max(worst_all) / m,
            })
            print(f"e={e} p={p:4d} m={m:3d} {tag:10s} "
                  f"allEven={C.all_even(D)} "
                  f"max_base(worst-central bits)={max(worst_all):.4f} "
                  f"(log2 p={math.log2(p):.4f}, ratio="
                  f"{max(worst_all)/math.log2(p):.4f}) "
                  f"best-achievable eta={max(worst_all)/m:.5f}")
    C.dump("C7_base_sweep.json", {"rows": rows})


def _f(x):
    return "None" if x is None else f"{x:.4f}"


if __name__ == "__main__":
    st = sys.argv[1] if len(sys.argv) > 1 else "c6"
    {"c6": stage_c6, "c7": stage_c7}[st]()
