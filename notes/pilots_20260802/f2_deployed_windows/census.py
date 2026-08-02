#!/usr/bin/env python3
"""Census of DEPLOYED F2 windows: exact Delta multisets, defect D, flatness.

Stages:
  orders   -- every admissible subgroup order n_ord, every frequency c
              (exhaustive for small p, sampled above): the flatness
              distribution of the windows the tower actually processes.
  degen    -- the exact degeneracy law  n_ord / gcd(n_ord, p-1) == 2
              tested over a wide prime range, all frequencies.
  scaling  -- deployed flatness vs p and vs n_ord (the "rung index" axis).
  compare  -- deployed vs random-multiset windows vs the banked killer classes.

Everything about the Delta multiset is EXACT integer arithmetic (counts, the
defect D, beta_min).  max_k |R_k| and Lambda_k are float diagnostics, labelled
`_float` wherever banked.
"""
from __future__ import annotations

import collections
import json
import math
import os
import sys
import time
from fractions import Fraction

sys.dont_write_bytecode = True
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import numpy as np  # noqa: E402
import deployed as DP  # noqa: E402
from slicecore import Fp2, admissible_orders, pair_reps  # noqa: E402


# --------------------------------------------------------------- fast core ---


def reps_arrays(p: int, n_ord: int):
    """(a_y, b_y) arrays for the genuine conjugate pairs of mu_{n_ord}."""
    F = Fp2.make(p)
    reps = pair_reps(F, F.subgroup(n_ord))
    if not reps:
        return None
    ay = np.array([y[0] for y in reps], dtype=np.int64)
    by = np.array([y[1] for y in reps], dtype=np.int64)
    return F, ay, by


def delta_counts(p: int, F, ay, by, c):
    """bincount of the Delta multiset over Z/2p.  EXACT integers."""
    two_p = 2 * p
    A = (2 * c[0]) % p
    B = (2 * F.N * c[1]) % p
    u = (A * ay) % p
    v = (B * by) % p
    sp = (u + v) % p
    sm = (u - v) % p
    sig_p = sp + p * (2 * sp > p)
    sig_m = sm + p * (2 * sm > p)
    D = (sig_p - sig_m) % two_p
    return np.bincount(D, minlength=two_p)


def defect_from_counts(p: int, cnt) -> int:
    """D = sum_{d in Z/p} |c_d|, c_d = (even-parity count) - (odd).  EXACT."""
    tot = 0
    for d in range(p):
        x0, x1 = d, d + p
        e0 = int(cnt[x0]) if x0 % 2 == 0 else 0
        o0 = int(cnt[x0]) if x0 % 2 == 1 else 0
        e1 = int(cnt[x1]) if x1 % 2 == 0 else 0
        o1 = int(cnt[x1]) if x1 % 2 == 1 else 0
        tot += abs((e0 + e1) - (o0 + o1))
    return tot


def _emat(p: int):
    two_p = 2 * p
    ks = np.arange(1, two_p, 2)
    vs = np.arange(two_p)
    return np.exp(1j * math.pi * np.outer(ks, vs) / p), ks


_EMAT: dict = {}


def Rabs(p: int, cnt, m: int):
    """|R_k| for k = 1,3,...,2p-1 via FFT.  O(p log p).  FLOAT diagnostic."""
    F = np.fft.fft(np.asarray(cnt, dtype=float))
    return np.abs(F[1::2]) / m           # index 2j+1 <-> k = 2j+1


ODD_K = {}


def odd_ks(p: int):
    if p not in ODD_K:
        ODD_K[p] = np.arange(1, 2 * p, 2)
    return ODD_K[p]


def maxR(p: int, cnt, m: int):
    """(max_k |R_k|, argmax k).  FLOAT diagnostic."""
    R = Rabs(p, cnt, m)
    j = int(np.argmax(R))
    return float(R[j]), int(odd_ks(p)[j])


def maxR_excluding_p(p: int, cnt, m: int):
    """(max_{k odd, k != p} |R_k|, argmax).  FLOAT diagnostic."""
    R = Rabs(p, cnt, m)
    ks = odd_ks(p)
    keep = ks != p
    Rk = R[keep]
    j = int(np.argmax(Rk))
    return float(Rk[j]), int(ks[keep][j])


def beta_min_from_counts(p: int, cnt, m: int) -> Fraction:
    odd = int(sum(int(cnt[v]) for v in range(1, 2 * p, 2)))
    return Fraction(min(odd, m - odd), m)


def window_row(p: int, F, ay, by, c):
    cnt = delta_counts(p, F, ay, by, c)
    m = int(cnt.sum())
    Dd = defect_from_counts(p, cnt)
    mr, kr = maxR(p, cnt, m)
    return {
        "c": list(c), "m": m,
        "n_values": int((cnt > 0).sum()),
        "defect_D": Dd,
        "flat_bound": Fraction(m - Dd, m),          # EXACT
        "max_absR_float": mr, "argmax_k": kr,
        "flat_float": 1.0 - mr,
        "beta_min": beta_min_from_counts(p, cnt, m),  # EXACT
    }


def frequencies(p: int, limit: int | None = None, seed: int = 12345):
    """All c in F_{p^2}^* with c not in F_p^* (the non-vacuous class, F2A.2)."""
    allc = [(a, b) for a in range(p) for b in range(1, p)]  # b != 0 <=> c not in F_p
    if limit is None or len(allc) <= limit:
        return allc, True
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(allc), size=limit, replace=False)
    return [allc[i] for i in sorted(idx)], False


# ---------------------------------------------------------------- stages ----

FLAT_43 = 0.0860        # (H-flat) threshold for eta = 1/43 (F2A.5b, sharp)
FLAT_THIRD_HALF = 1.0 / 3.0 * math.log(2) / 0.25   # eta=1/3 at beta=1/2
FLAT_THIRD_QUART = 1.0 / 3.0 * math.log(2) / 0.1875  # eta=1/3 at beta=1/4 (>1)


def stage_orders(primes, cmax=None):
    for p in primes:
        t0 = time.time()
        out = {"p": p, "N_nonresidue": Fp2.make(p).N, "p2m1": p * p - 1,
               "orders": []}
        cs, exhaustive = frequencies(p, cmax)
        for n_ord in admissible_orders(p):
            ra = reps_arrays(p, n_ord)
            if ra is None:
                continue
            F, ay, by = ra
            m = len(ay)
            if m == 0:
                continue
            rows = [window_row(p, F, ay, by, c) for c in cs]
            fl = [r["flat_float"] for r in rows]
            fb = [float(r["flat_bound"]) for r in rows]
            bm = [float(r["beta_min"]) for r in rows]
            dead = [r for r in rows if r["flat_float"] < 1e-9]
            worst = min(rows, key=lambda r: r["flat_float"])
            out["orders"].append({
                "n_ord": n_ord, "m": m,
                "gcd_n_pm1": math.gcd(n_ord, p - 1),
                "quot": n_ord // math.gcd(n_ord, p - 1),
                "degenerate_law": (n_ord // math.gcd(n_ord, p - 1)) == 2,
                "n_c": len(cs), "exhaustive_c": exhaustive,
                "flat_min": min(fl), "flat_med": float(np.median(fl)),
                "flat_max": max(fl),
                "flat_bound_min": min(fb), "flat_bound_med": float(np.median(fb)),
                "beta_min_min": min(bm), "beta_min_med": float(np.median(bm)),
                "n_dead": len(dead),
                "frac_clear_43": float(np.mean([x >= FLAT_43 for x in fl])),
                "frac_bound_clears_43": float(np.mean([x >= FLAT_43 for x in fb])),
                "worst_c": worst["c"], "worst_flat": worst["flat_float"],
                "worst_argmax_k": worst["argmax_k"],
                "worst_beta_min": float(worst["beta_min"]),
                "worst_n_values": worst["n_values"],
                "worst_defect_D": worst["defect_D"],
            })
        DP.dump(f"orders_p{p}.json", out)
        print(f"p={p}: {len(out['orders'])} orders x {len(cs)} freqs "
              f"in {time.time()-t0:.1f}s (exhaustive_c={exhaustive})")


def stage_degen(primes):
    """Test the exact degeneracy law over many primes, all frequencies."""
    rows = []
    for p in primes:
        for n_ord in admissible_orders(p):
            ra = reps_arrays(p, n_ord)
            if ra is None:
                continue
            F, ay, by = ra
            m = len(ay)
            if m == 0:
                continue
            law = (n_ord // math.gcd(n_ord, p - 1)) == 2
            cs, exh = frequencies(p, 400)
            allev, anydead, minflat = True, False, 1.0
            for c in cs:
                cnt = delta_counts(p, F, ay, by, c)
                odd = int(sum(int(cnt[v]) for v in range(1, 2 * p, 2)))
                if odd != 0:
                    allev = False
                mr, _ = maxR(p, cnt, m)
                minflat = min(minflat, 1.0 - mr)
                if 1.0 - mr < 1e-9:
                    anydead = True
            rows.append({"p": p, "n_ord": n_ord, "m": m, "law_predicts_dead": law,
                         "all_delta_even_every_c": allev,
                         "some_c_dead": anydead, "min_flat_float": minflat,
                         "exhaustive_c": exh})
    viol = [r for r in rows
            if r["law_predicts_dead"] != r["all_delta_even_every_c"]]
    DP.dump("degeneracy_law.json",
            {"rows": rows, "violations": viol, "n_rows": len(rows)})
    print(f"degeneracy law: {len(rows)} (p,n_ord) rows, "
          f"{len(viol)} violations of "
          f"[n_ord/gcd(n_ord,p-1)==2  <=>  all Delta even at every c]")
    for v in viol:
        print("  VIOLATION:", v)
    extra = [r for r in rows if r["some_c_dead"] and not r["law_predicts_dead"]]
    print(f"  windows dead at SOME c but not predicted by the law: {len(extra)}")
    for r in extra:
        print(f"    p={r['p']} n_ord={r['n_ord']} m={r['m']} "
              f"min_flat={r['min_flat_float']:.2e}")


def stage_scaling(primes, cmax=200):
    """Deployed flatness vs p at the full group and at the largest few orders."""
    rows = []
    for p in primes:
        orders = admissible_orders(p)
        # the top few orders (the 'deep rungs') plus the smallest non-degenerate
        pick = orders[-4:] + [o for o in orders
                              if (o // math.gcd(o, p - 1)) != 2][:2]
        for n_ord in sorted(set(pick)):
            ra = reps_arrays(p, n_ord)
            if ra is None:
                continue
            F, ay, by = ra
            m = len(ay)
            if m < 2:
                continue
            cs, exh = frequencies(p, cmax)
            fl, fb, bmv = [], [], []
            for c in cs:
                cnt = delta_counts(p, F, ay, by, c)
                mr, _ = maxR(p, cnt, m)
                fl.append(1.0 - mr)
                fb.append(float(Fraction(m - defect_from_counts(p, cnt), m)))
                bmv.append(float(beta_min_from_counts(p, cnt, m)))
            rows.append({"p": p, "n_ord": n_ord, "m": m,
                         "quot": n_ord // math.gcd(n_ord, p - 1),
                         "n_c": len(cs), "exhaustive_c": exh,
                         "flat_min": min(fl), "flat_med": float(np.median(fl)),
                         "flat_max": max(fl),
                         "flat_bound_min": min(fb),
                         "flat_bound_med": float(np.median(fb)),
                         "beta_min_med": float(np.median(bmv))})
            print(f"p={p:4d} n_ord={n_ord:7d} m={m:6d} quot={rows[-1]['quot']:3d} "
                  f"flat min/med/max = {min(fl):.4f}/{np.median(fl):.4f}/{max(fl):.4f} "
                  f"bound med={np.median(fb):.4f}")
    DP.dump("scaling.json", {"rows": rows})


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "orders"
    if stage == "orders":
        primes = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 \
            else [11, 13, 19, 23, 31]
        cmax = int(sys.argv[3]) if len(sys.argv) > 3 else None
        stage_orders(primes, cmax)
    elif stage == "degen":
        primes = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 \
            else [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
        stage_degen(primes)
    elif stage == "scaling":
        primes = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 \
            else [23, 41, 67, 101, 151, 199]
        cmax = int(sys.argv[3]) if len(sys.argv) > 3 else 200
        stage_scaling(primes, cmax)
    else:
        raise SystemExit(f"unknown stage {stage}")


if __name__ == "__main__":
    main()
