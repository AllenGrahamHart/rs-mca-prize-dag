#!/usr/bin/env python3
"""C1 doubling-orbit spectrum compiler (order-2N analogue of the official L=1 C1 shape).

Setup (background/nodes/dli_c1_doubling_coboundary_identity):
  q prime, q = 1 mod 2N; H = <omega> the unique subgroup of order 2N of F_q^*;
  Q = F_q^*/H (cyclic of order M = (q-1)/(2N)); sigma(C) = 2C the doubling permutation.
  Boolean subset-sum over the half-section 1, omega, ..., omega^(N-1):
      m_s = #{xi in {0,1}^N : sum xi_i omega^i = s mod q},
      Z   = sum_s m_s^2 / 2^N   (= sum over ternary kernel of 2^-wt),
      X   = Z - 2^N/q          (the C1 excess; L=1 target is X <= 4).
  (DB-3): X = (q-1)/(q 2^N) * avg_C A(C), so sum_C A(C) = (q*SS - 2^(2N))/(2N)
  must be a non-negative integer -- an exact structural check performed on every row.

ALL VERDICT ARITHMETIC IS EXACT (Python ints / Fractions). Floats are display only.

Usage:  tools/ramguard local -- python3 <this> --qmax 100000 --twoN 32 --out results/...json
"""

from __future__ import annotations

import argparse
import json
import math
import time
from fractions import Fraction

import numpy as np


# ----------------------------------------------------------------- primes ---
def primes_up_to(n: int) -> np.ndarray:
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p :: p] = False
    return np.flatnonzero(sieve)


def factorize(n: int) -> dict[int, int]:
    f: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def mult_order(a: int, q: int, fac_qm1: dict[int, int]) -> int:
    """Order of a in F_q^*, given the factorisation of q-1."""
    o = q - 1
    for p in fac_qm1:
        while o % p == 0 and pow(a, o // p, q) == 1:
            o //= p
    return o


def root_of_order(q: int, order: int) -> int:
    """An element of exact multiplicative order `order` (order | q-1)."""
    e = (q - 1) // order
    a = 2
    while True:
        w = pow(a, e, q)
        # order(w) divides `order`; it equals `order` iff w^(order/p) != 1 for all p | order
        ok = True
        for p in factorize(order):
            if pow(w, order // p, q) == 1:
                ok = False
                break
        if ok:
            return w
        a += 1


# ------------------------------------------------------- exact kernel MITM ---
def ternary_table(coeffs: list[int], q: int) -> tuple[np.ndarray, np.ndarray]:
    """All 3^k signed combinations of `coeffs`: (values mod q, hamming weights)."""
    vals = np.zeros(1, dtype=np.int64)
    wts = np.zeros(1, dtype=np.int64)
    for a in coeffs:
        vals = np.concatenate([vals, (vals + a) % q, (vals - a) % q])
        wts = np.concatenate([wts, wts + 1, wts + 1])
    return vals, wts


def kernel_weight_profile(coeffs: list[int], q: int) -> np.ndarray:
    """Exact counts N_w of d in {-1,0,1}^N with sum d_i coeffs_i = 0 mod q, by weight w."""
    n = len(coeffs)
    half = n // 2
    lv, lw = ternary_table(coeffs[:half], q)
    rv, rw = ternary_table(coeffs[half:], q)
    order = np.argsort(lv, kind="stable")
    lvs, lws = lv[order], lw[order]
    wmaxL = half + 1
    cum = np.zeros((lvs.size + 1, wmaxL), dtype=np.int64)
    cum[np.arange(1, lvs.size + 1), lws] = 1
    cum = np.cumsum(cum, axis=0)
    targets = (-rv) % q
    lo = np.searchsorted(lvs, targets, side="left")
    hi = np.searchsorted(lvs, targets, side="right")
    hist = cum[hi] - cum[lo]                      # (3^(n-half), wmaxL)
    idx = rw[:, None] + np.arange(wmaxL)[None, :]  # total weights
    N = np.zeros(n + 1, dtype=np.int64)
    np.add.at(N, idx.ravel(), hist.ravel())
    return N


def subset_sum_SS(coeffs: list[int], q: int) -> int:
    """sum_s m_s^2 by direct enumeration of all 2^N Boolean subset sums."""
    s = np.zeros(1, dtype=np.int64)
    for a in coeffs:
        s = np.concatenate([s, (s + a) % q])
    _, counts = np.unique(s, return_counts=True)
    c = counts.astype(object)
    return int(sum(c * c))


# ------------------------------------------------- explicit coset machinery ---
def explicit_cycle_structure(q: int, H: list[int]) -> dict:
    """Build Q = F_q^*/H and the doubling permutation explicitly; return cycle lengths."""
    coset_of = [-1] * q
    reps = []
    for x in range(1, q):
        if coset_of[x] == -1:
            cid = len(reps)
            reps.append(x)
            for h in H:
                coset_of[(x * h) % q] = cid
    sigma = [coset_of[(2 * r) % q] for r in reps]
    seen = [False] * len(reps)
    lens = []
    for i in range(len(reps)):
        if not seen[i]:
            ln = 0
            j = i
            while not seen[j]:
                seen[j] = True
                j = sigma[j]
                ln += 1
            lens.append(ln)
    return {"n_cosets": len(reps), "cycle_lengths": sorted(set(lens)),
            "n_cycles": len(lens), "max_cycle": max(lens), "min_cycle": min(lens)}


# ------------------------------------------------------------------- row ----
def process_q(q: int, twoN: int, explicit: bool, want_profile: bool = True) -> dict:
    N = twoN // 2
    omega = root_of_order(q, twoN)
    coeffs = [pow(omega, i, q) for i in range(N)]
    fac = factorize(q - 1)
    ord2 = mult_order(2, q, fac)
    g = math.gcd(ord2, twoN)
    r = ord2 // g                       # order of the class of 2 in Q
    M = (q - 1) // twoN
    n_cycles = M // r
    v2 = fac.get(2, 0)

    SS = subset_sum_SS(coeffs, q)
    row: dict = {
        "q": q, "twoN": twoN, "N": N, "omega": omega,
        "v2_qm1": v2, "ord2": ord2, "r": r, "M": M,
        "n_cycles": n_cycles, "max_cycle": r, "cycle_lengths_theory": [r],
        "SS": str(SS),
    }

    if want_profile:
        Nw = kernel_weight_profile(coeffs, q)
        SS_from_profile = int(sum(int(Nw[w]) * (1 << (N - w)) for w in range(N + 1)))
        row["weight_profile"] = [int(x) for x in Nw]
        row["profile_matches_SS"] = (SS_from_profile == SS)
        nz = [w for w in range(1, N + 1) if Nw[w] > 0]
        row["min_relation_weight"] = int(nz[0]) if nz else None
        row["n_kernel_nonzero"] = int(sum(int(Nw[w]) for w in range(1, N + 1)))

    # exact excess
    num = q * SS - (1 << (2 * N))
    den = q << N
    X = Fraction(num, den)
    row["X_num"], row["X_den"] = X.numerator, X.denominator
    row["X_float"] = float(X)
    Z = Fraction(SS, 1 << N)
    row["Z_num"], row["Z_den"] = Z.numerator, Z.denominator
    row["Z_float"] = float(Z)
    # relation mass = sum over NONZERO ternary kernel of 2^-wt = Z - 1 exactly.
    # X = (1 - 2^N/q) + relation_mass, so in the hard regime q >> 2^N, X ~ 1 + mass.
    rm = Z - 1
    row["relmass_num"], row["relmass_den"] = rm.numerator, rm.denominator
    row["relmass_float"] = float(rm)

    # (DB-3): sum_C A(C) = (q*SS - 2^(2N))/(2N) must be a non-negative integer
    row["sumA_is_integer"] = (num % twoN == 0)
    row["sumA"] = str(num // twoN) if num % twoN == 0 else None
    row["sumA_nonneg"] = num >= 0

    # exact-flatness reference value (r=1 theorem): X = (q-1)/(q 2^N)
    flat = Fraction(q - 1, q << N)
    row["X_flat_num"], row["X_flat_den"] = flat.numerator, flat.denominator
    row["is_exactly_flat"] = (X == flat)
    row["X_over_flat"] = float(X / flat)          # = avg_C A(C)
    row["avgA_float"] = float(X / flat)
    row["hard_regime"] = q > (1 << N)

    if explicit:
        H = [pow(omega, i, q) for i in range(twoN)]
        row["explicit"] = explicit_cycle_structure(q, H)
    return row


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--twoN", type=int, default=32)
    ap.add_argument("--qmin", type=int, default=0)
    ap.add_argument("--qmax", type=int, default=100000)
    ap.add_argument("--explicit-below", type=int, default=20000)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    t0 = time.time()
    ps = primes_up_to(args.qmax)
    qs = [int(p) for p in ps if p % args.twoN == 1 and p > args.qmin]
    rows = []
    for q in qs:
        rows.append(process_q(q, args.twoN, explicit=(q <= args.explicit_below)))
    meta = {
        "twoN": args.twoN, "N": args.twoN // 2,
        "qmin": args.qmin, "qmax": args.qmax,
        "n_rows": len(rows), "seconds": round(time.time() - t0, 2),
        "arithmetic": "exact integers/Fractions for X, Z, weight profile, sumA",
    }
    with open(args.out, "w") as f:
        json.dump({"meta": meta, "rows": rows}, f)
    print(json.dumps(meta))


if __name__ == "__main__":
    main()
