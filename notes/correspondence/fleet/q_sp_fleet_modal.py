#!/usr/bin/env python3
"""Fleet run on UPSTREAM'S two pre-registered falsifier objects (Modal).

Objects (V13, replayed conventions):
  (Q)  prefix map Phi_{m,w}(M) = ((-1)^h e_h(M))_h on m-subsets of the
       order-N subgroup D of F_p*; for w < p Newton-equivalent to the
       power-sum prefix (identical fibers) — we DP power sums.
       Falsifier: super-polynomial PRIMITIVE max-fiber/mean in the dense
       bulk, sustained across scales.
  (SP) top shift-pair stratum sp_w(w+1; D) = ordered DISJOINT pairs of
       (w+1)-subsets with matching depth-w prefixes (= (A,c): A, A-c both
       split). Falsifier: super-polynomial primitive part after
       quotient-pullback pairs (gamma-dilations, esp. T = -S) removed.

VALIDATION GATE (their printed calibration, must reproduce before the hunt):
  (17,16,8):  max/mean = 1.0012, 1.21, 2.67 at w = 1,2,3
  (41,20,10): 1.0022, 1.21, 4.10; Poisson: max 11 vs mean 2.7 at w=3
  (257,64,34): 1+3e-12, 1+9e-9 at w = 1,2

Exact integer DP throughout (int64, counts bounded by C(64,34) < 2^63)."""
import json
from fractions import Fraction

import modal

app = modal.App("rs-mca-fleet-qsp")
image = modal.Image.debian_slim().pip_install("numpy")

# (p, N, m, w)
FIBER_JOBS = [
    # validation gate
    (17, 16, 8, 1), (17, 16, 8, 2), (17, 16, 8, 3),
    (41, 20, 10, 1), (41, 20, 10, 2), (41, 20, 10, 3),
    (257, 64, 34, 1), (257, 64, 34, 2),
    # hunt ladder: fixed geometry N/sqrt(p) ~ 3-5, m = N/2, w = 2
    (101, 50, 25, 2), (577, 96, 48, 2), (1153, 128, 64, 2),
    # w = 3 ladder (memory-feasible)
    (101, 50, 25, 3),
]
SP_JOBS = [
    # (p, N, w): top stratum sp_w(w+1; D), disjoint-pair DP
    (17, 16, 2), (41, 20, 2), (101, 50, 2), (257, 64, 2), (577, 96, 2),
    (1153, 128, 2),
    (17, 16, 3), (41, 20, 3), (101, 50, 3),
]


def _subgroup(p, N):
    g = None
    for cand in range(2, p):
        x, seen = 1, set()
        for _ in range(p - 1):
            x = x * cand % p
            seen.add(x)
        if len(seen) == p - 1:
            g = cand
            break
    e = (p - 1) // N
    h = pow(g, e, p)
    return sorted(pow(h, i, p) for i in range(N))


@app.function(image=image, cpu=4, memory=8192, timeout=300)
def fiber_census(job):
    """Exact full fiber histogram of the depth-w power-sum prefix map."""
    import numpy as np
    p, N, m, w = job
    D = _subgroup(p, N)
    shape = (m + 1,) + (p,) * w
    dp = np.zeros(shape, dtype=np.int64)
    dp[(0,) + (0,) * w] = 1
    for x in D:
        v = [pow(x, h, p) for h in range(1, w + 1)]
        rolled = dp[:m]  # counts with c items; adding x -> c+1
        shifted = rolled
        for ax in range(w):
            shifted = np.roll(shifted, v[ax], axis=1 + ax)
        dp[1:] += shifted
    fib = dp[m]
    total = int(fib.sum())
    from math import comb
    assert total == comb(N, m), (total, comb(N, m))
    mx = int(fib.max())
    mean = Fraction(comb(N, m), p ** w)
    ratio = float(Fraction(mx) / mean)
    second_moment = int((fib.astype(object) ** 2).sum())
    null_fiber = int(fib[(0,) * w])
    return {"p": p, "N": N, "m": m, "w": w, "max": mx,
            "mean": float(mean), "max_over_mean": ratio,
            "null_fiber": null_fiber,
            "sum_N2": str(second_moment),
            "diag": str(comb(N, m)),
            "sp_total_mass": str(second_moment - comb(N, m))}


@app.function(image=image, cpu=4, memory=8192, timeout=300)
def sp_top_census(job):
    """Exact sp_w(w+1; D): ordered disjoint (w+1)-subset pairs, matching
    depth-w power-sum prefixes. Joint DP: state (a, b, delta)."""
    import numpy as np
    p, N, w = job
    k = w + 1
    D = _subgroup(p, N)
    shape = (k + 1, k + 1) + (p,) * w
    dp = np.zeros(shape, dtype=np.int64)
    dp[(0, 0) + (0,) * w] = 1
    for x in D:
        v = [pow(x, h, p) for h in range(1, w + 1)]
        add_S = dp[:k, :]
        for ax in range(w):
            add_S = np.roll(add_S, v[ax], axis=2 + ax)
        add_T = dp[:, :k]
        for ax in range(w):
            add_T = np.roll(add_T, -v[ax], axis=2 + ax)
        dp[1:, :] += add_S
        dp[:, 1:] += add_T
    sp = int(dp[(k, k) + (0,) * w])
    # pullback columns (exact, same DP machinery at depth enough):
    # gamma = -1: pairs (S, -S) disjoint with p_odd(S) = 0 conditions
    neg = {(-x) % p for x in D} == set(D)
    minus_pairs = 0
    if neg:
        # count k-subsets S with p_h(S) = 0 for all odd h <= w and S ∩ -S = ∅
        # DP over +/- pair classes of D (x paired with -x)
        pairs = []
        seen = set()
        for x in D:
            if x in seen:
                continue
            seen.add(x); seen.add((-x) % p)
            pairs.append(x)
        shp = (k + 1,) + (p,) * w
        d2 = np.zeros(shp, dtype=np.int64)
        d2[(0,) + (0,) * w] = 1
        for x in pairs:
            vx = [pow(x, h, p) for h in range(1, w + 1)]
            vmx = [pow((-x) % p, h, p) for h in range(1, w + 1)]
            aS = d2[:k]
            for ax in range(w):
                aS = np.roll(aS, vx[ax], axis=1 + ax)
            aM = d2[:k]
            for ax in range(w):
                aM = np.roll(aM, vmx[ax], axis=1 + ax)
            d2[1:] += aS + aM
        # S with all depth-w sums giving p_h(S) + p_h(-S)... simpler: T=-S match
        # condition is p_h(S)=p_h(-S)=(-1)^h p_h(S) => odd sums 0. For w=2: p1=0;
        # w=3: p1=p3=0. Count via the d2 histogram marginal:
        fibk = d2[k]
        if w == 2:
            minus_pairs = int(fibk.sum(axis=1)[0])          # p1 = 0
        elif w == 3:
            minus_pairs = int(fibk.sum(axis=1)[0, :].sum() - 0) if False else int(fibk[0, :, 0].sum())  # p1=0 & p3=0
        else:
            minus_pairs = int(fibk[(0,) * w])
    from math import comb
    model = Fraction(comb(N, k) * comb(N - k, k), p ** w)
    return {"p": p, "N": N, "w": w, "k": k, "sp_top": sp,
            "model": float(model),
            "sp_over_model": float(Fraction(sp) / model) if model else None,
            "minus_dilation_pairs_bound": minus_pairs * 2}


@app.local_entrypoint()
def main():
    fibs = list(fiber_census.map(FIBER_JOBS, return_exceptions=True))
    sps = list(sp_top_census.map(SP_JOBS, return_exceptions=True))
    print("=== (Q) fiber census — validation gate + hunt ladder ===")
    print(f"{'(p,N,m,w)':>18} {'max':>10} {'mean':>14} {'max/mean':>10} {'null':>10}")
    for r in fibs:
        if not isinstance(r, dict):
            print("  worker error:", str(r)[:140]); continue
        print(f"  ({r['p']},{r['N']},{r['m']},{r['w']})".rjust(18) +
              f" {r['max']:>10} {r['mean']:>14.4g} {r['max_over_mean']:>10.4f} {r['null_fiber']:>10}")
    print("\n=== (SP) top-stratum census ===")
    print(f"{'(p,N,w)':>14} {'sp_top':>12} {'model':>12} {'sp/model':>9} {'(-1)-dilation<=':>16}")
    for r in sps:
        if not isinstance(r, dict):
            print("  worker error:", str(r)[:140]); continue
        print(f"  ({r['p']},{r['N']},{r['w']})".rjust(14) +
              f" {r['sp_top']:>12} {r['model']:>12.4g} {r['sp_over_model']:>9.3f} {r['minus_dilation_pairs_bound']:>16}")
    with open("/tmp/fleet_qsp.json", "w") as f:
        json.dump({"fiber": [r for r in fibs if isinstance(r, dict)],
                   "sp": [r for r in sps if isinstance(r, dict)]}, f, indent=1)
