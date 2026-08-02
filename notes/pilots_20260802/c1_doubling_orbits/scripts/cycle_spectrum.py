#!/usr/bin/env python3
"""Per-doubling-cycle mode spectrum for the order-2N C1 analogue.

For a sampled prime q = 1 (mod 2N):
  * build Q = F_q^*/H explicitly as {g^j H : j < M}, M = (q-1)/(2N), g a primitive root;
  * the doubling permutation is sigma(j) = j + t (mod M) with t = dlog_{g^{2N}}(2^{2N}),
    so every cycle has the SAME length r = M/gcd(t,M) -- verified here against an
    explicit cycle walk;
  * evaluate, per coset,
        L(C)      = log D(C) = sum_{i<N} log( 4 sin^2(pi c omega^i / q) )
        log A(C)  =            sum_{i<N} log( 4 cos^2(pi c omega^i / q) )
    using the EXACT half-angle reformulations
        4 cos^2(pi m/q) = 4 sin^2(pi (q-2m) / (2q)),
        4 sin^2(pi m/q) = 4 sin^2(pi min(m,q-m)/q),
    which move every evaluation away from the cancellation region, so IEEE-754
    binary64 delivers ~1e-15 relative accuracy per factor (~1e-14 absolute on the
    16-term log sums).  DIAGNOSTIC ONLY -- every verdict number in this pilot
    (X, Z, weight profiles, sum_C A(C)) is computed exactly elsewhere.
  * cross-checks: coboundary log A(C) = L(sigma C) - L(C); cycle sums of log A = 0;
    sum_C L(C) = log q; sum_C A(C) against the exact integer (q*SS - 2^{2N})/(2N).

Usage: tools/ramguard local -- python3 <this> --qs 257,641,... --out results/....json
"""

from __future__ import annotations

import argparse
import json
import math
import time

import numpy as np

import orbit_spectrum as osp


def primitive_root(q: int) -> int:
    fac = osp.factorize(q - 1)
    g = 2
    while True:
        if all(pow(g, (q - 1) // p, q) != 1 for p in fac):
            return g
        g += 1


def log4sin2(m: np.ndarray, q: int) -> np.ndarray:
    """log(4 sin^2(pi m / q)) for integer m in [1, q-1], well conditioned."""
    mm = np.minimum(m % q, q - (m % q))
    return 2.0 * np.log(2.0 * np.sin(np.pi * mm.astype(np.float64) / q))


def log4cos2(m: np.ndarray, q: int) -> np.ndarray:
    """log(4 cos^2(pi m / q)) via 4cos^2(pi m/q) = 4 sin^2(pi (q-2m)/(2q))."""
    mm = m % q
    u = np.abs(q - 2 * mm).astype(np.float64)      # odd, 0 < u <= q
    return 2.0 * np.log(2.0 * np.sin(np.pi * u / (2.0 * q)))


def analyse(q: int, twoN: int, top_k: int = 10) -> dict:
    N = twoN // 2
    M = (q - 1) // twoN
    g = primitive_root(q)
    omega = pow(g, M, q)                      # exact order twoN
    assert pow(omega, twoN, q) == 1 and pow(omega, twoN // 2, q) != 1

    # coset representatives g^j, j = 0..M-1
    reps = np.empty(M, dtype=np.int64)
    x = 1
    for j in range(M):
        reps[j] = x
        x = (x * g) % q

    # t with 2 * g^j H = g^{j+t} H  <=>  G^t = 2^{2N} where G = g^{2N} (order M)
    G = pow(g, twoN, q)
    y = pow(2, twoN, q)
    t, cur = None, 1
    for j in range(M):
        if cur == y:
            t = j
            break
        cur = (cur * G) % q
    assert t is not None
    # verify the translation law on a sample of cosets
    for j in (0, 1, M // 3, M // 2, M - 1):
        c1 = (2 * int(reps[j])) % q
        c2 = int(reps[(j + t) % M])
        ratio = (c1 * pow(c2, q - 2, q)) % q
        assert pow(ratio, twoN, q) == 1, (q, j)

    gcd_tM = math.gcd(t, M)
    r_theory = M // gcd_tM
    # explicit cycle walk
    seen = np.zeros(M, dtype=bool)
    cycles = []
    for j in range(M):
        if not seen[j]:
            cyc = []
            k = j
            while not seen[k]:
                seen[k] = True
                cyc.append(k)
                k = (k + t) % M
            cycles.append(cyc)
    cyc_lens = sorted({len(c) for c in cycles})

    # potentials
    logD = np.zeros(M)
    logA = np.zeros(M)
    for i in range(N):
        wi = pow(omega, i, q)
        m = (reps * wi) % q
        logD += log4sin2(m, q)
        logA += log4cos2(m, q)

    sigma = (np.arange(M) + t) % M
    cob_resid = float(np.max(np.abs(logA - (logD[sigma] - logD))))
    sumL = float(np.sum(logD))
    A = np.exp(logA)
    sumA = float(math.fsum(A.tolist()))

    # exact reference for sum_C A(C)
    coeffs = [pow(omega, i, q) for i in range(N)]
    SS = osp.subset_sum_SS(coeffs, q)
    num = q * SS - (1 << (2 * N))
    assert num % twoN == 0
    sumA_exact = num // twoN

    per_cycle = []
    for ci, cyc in enumerate(cycles):
        idx = np.array(cyc, dtype=np.int64)
        la = logA[idx]
        a = A[idx]
        per_cycle.append({
            "cycle": ci,
            "length": len(cyc),
            "sum_logA": float(math.fsum(la.tolist())),
            "max_abs_logA": float(np.max(np.abs(la))),
            "max_logA": float(np.max(la)),
            "min_logA": float(np.min(la)),
            "sumA": float(math.fsum(a.tolist())),
            "maxA": float(np.max(a)),
            "share_of_sumA": float(math.fsum(a.tolist()) / sumA) if sumA > 0 else None,
        })
    per_cycle.sort(key=lambda d: -d["share_of_sumA"] if d["share_of_sumA"] else 0.0)

    order = np.argsort(-A)
    topk = [{"j": int(j), "rep": int(reps[j]), "A": float(A[j]),
             "logA": float(logA[j]), "share": float(A[j] / sumA)}
            for j in order[:top_k]]
    cum = np.cumsum(A[order]) / sumA

    row = {
        "q": q, "twoN": twoN, "M": M, "t": t, "gcd_t_M": gcd_tM,
        "r_theory": r_theory, "n_cycles": len(cycles),
        "cycle_lengths_explicit": cyc_lens,
        "all_cycles_equal_length": len(cyc_lens) == 1,
        "r_matches_explicit": cyc_lens == [r_theory],
        "coboundary_max_residual": cob_resid,
        "sum_logD": sumL, "log_q": math.log(q),
        "sum_logD_minus_log_q": sumL - math.log(q),
        "max_abs_cycle_sum_logA": max(abs(c["sum_logA"]) for c in per_cycle),
        "sumA_float": sumA, "sumA_exact": str(sumA_exact),
        "sumA_rel_error": abs(sumA - sumA_exact) / max(1.0, abs(sumA_exact)),
        "max_logA": float(np.max(logA)), "min_logA": float(np.min(logA)),
        "max_A": float(np.max(A)),
        "logA_std": float(np.std(logA)),
        "top1_share": float(cum[0]), "top10_share": float(cum[min(9, M - 1)]),
        "top1pct_share": float(cum[max(0, int(0.01 * M) - 1)]),
        "n_cosets_for_half_mass": int(np.searchsorted(cum, 0.5) + 1),
        "top_cosets": topk,
        "per_cycle": per_cycle[: min(len(per_cycle), 40)],
        "n_cycles_reported": min(len(per_cycle), 40),
        "cycle_share_max": max(c["share_of_sumA"] for c in per_cycle),
        "cycle_share_min": min(c["share_of_sumA"] for c in per_cycle),
        "X_float": float((q * SS - (1 << (2 * N))) / (q * (1 << N))),
        "avgA": sumA / M,
    }
    return row


def mp_spotcheck(q: int, twoN: int, n_probe: int = 8, dps: int = 60) -> dict:
    """Independent mpmath (60 dps) recomputation of logA on a few cosets."""
    from mpmath import mp, mpf, cos, log, pi

    mp.dps = dps
    N = twoN // 2
    M = (q - 1) // twoN
    g = primitive_root(q)
    omega = pow(g, M, q)
    out = []
    rng = np.random.default_rng(12345)
    js = sorted(set(int(v) for v in rng.integers(0, M, size=n_probe)))
    for j in js:
        c = pow(g, j, q)
        s = mpf(0)
        for i in range(N):
            m = (c * pow(omega, i, q)) % q
            s += log(4 * cos(pi * mpf(m) / q) ** 2)
        # float64 route
        reps = np.array([c], dtype=np.int64)
        f = 0.0
        for i in range(N):
            f += float(log4cos2((reps * pow(omega, i, q)) % q, q)[0])
        out.append({"j": j, "logA_mp": float(s), "logA_f64": f, "abs_diff": abs(float(s) - f)})
    return {"q": q, "dps": dps, "probes": out,
            "max_abs_diff": max(p["abs_diff"] for p in out)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--twoN", type=int, default=32)
    ap.add_argument("--qs", required=True, help="comma-separated primes")
    ap.add_argument("--spotcheck", default="")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    t0 = time.time()
    rows = [analyse(int(q), args.twoN) for q in args.qs.split(",") if q]
    spot = [mp_spotcheck(int(q), args.twoN) for q in args.spotcheck.split(",") if q]
    with open(args.out, "w") as f:
        json.dump({"meta": {"twoN": args.twoN, "seconds": round(time.time() - t0, 2),
                            "precision": "IEEE-754 binary64 with exact half-angle "
                                         "reformulation; mpmath 60-dps spot checks",
                            "n_rows": len(rows)},
                   "rows": rows, "spotchecks": spot}, f)
    print(json.dumps({"n_rows": len(rows), "seconds": round(time.time() - t0, 2),
                      "max_coboundary_residual": max(r["coboundary_max_residual"] for r in rows),
                      "max_cycle_sum_logA": max(r["max_abs_cycle_sum_logA"] for r in rows),
                      "max_sumA_rel_error": max(r["sumA_rel_error"] for r in rows),
                      "max_sumlogD_dev": max(abs(r["sum_logD_minus_log_q"]) for r in rows),
                      "mp_max_diff": max((s["max_abs_diff"] for s in spot), default=None)}))


if __name__ == "__main__":
    main()
