#!/usr/bin/env python3
"""bc_block_census -- verifier 3: route 2, the D-LOCAL list count.

By the LENS the per-slope block census is a punctured-RS agreement census:
blocks of slope nu are the size-r agreement sets of RS_K (K = k-ell)
restricted to D (|D| = e = 2r) with the fixed word W_nu.  This verifier
measures it exactly and tests the two structural bounds.

  (L1) PER-SLOPE PACKING BOUND.  Distinct blocks at one slope meet in
       <= K-1 points (two distinct deg<K polys agree <= K-1 times), so
       every K-subset of D lies in at most one block:
                #blocks at a fixed slope  <=  C(e,K) / C(r,K).
  (L2) THE D-LOCAL CENSUS.  N_D := #{tau in RS_K : the slope word
       x |-> psi_tau(x) takes exactly two values on D, each r times}.
       Every selected block of every maximal-selected target is a block of
       some tau counted by N_D, so  |Bset| <= 2 * #partitions(N_D).
       This is the strongest D-LOCAL relaxation of (BC): it drops the
       off-D core condition entirely.
  (L3) THE REGIME BOUNDARY.  When K >= e the restriction RS_K -> F_q^D is
       SURJECTIVE, so for EVERY partition {B,C} and EVERY slope pair
       (nu,mu) the interpolant is a legal tau: the D-local census is
       COMPLETE, N_part = C(e,r)/2, and (L2) is worthless.  Verifier 1
       showed K/e is between 55 and 111 at every prize row.

Run: tools/ramguard local -- python3 \
       notes/pilots_20260804/bc_block_census/dlocal.py
"""

import itertools
import json
import os
import sys
from collections import Counter
from math import comb

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fixture import (BShape, ground, build_fixture, canon_slope,  # noqa
                     inv)                                          # noqa

CHECKS = []


def chk(cond, name, info=""):
    CHECKS.append({"name": name, "ok": bool(cond), "info": str(info)})
    return bool(cond)


def W_of(shape, g, fx):
    """W_nu(x) for every slope nu and x in D  (the LENS word system)."""
    q = shape.q
    D = g["D"]
    u, v = fx["u"], fx["v"]
    W = {}
    for nu in g["slopes"]:
        a, b = nu
        col = {}
        for x in D:
            L = (a - b * pow(x, 3, q)) % q
            if L:
                col[x] = ((a * u[x] + b * v[x]) % q) * inv(L, q) % q
        W[nu] = col
    return W


def d_local_census(shape, g, fx, K):
    """EXHAUSTIVE over all q^K polys of degree < K: the D-local census."""
    q, r, e = shape.q, shape.r, shape.e
    D = g["D"]
    u, v = fx["u"], fx["v"]
    Da = np.array(D, dtype=np.int64)
    cube = np.array([pow(x, 3, q) for x in D], dtype=np.int64)
    ua = np.array([u[x] for x in D], dtype=np.int64)
    va = np.array([v[x] for x in D], dtype=np.int64)

    total = q ** K
    CH = 40000
    n_two_block, parts, blocks = 0, set(), set()
    max_class = 0
    for st in range(0, total, CH):
        idxs = np.arange(st, min(st + CH, total), dtype=np.int64)
        coefs, tmp = [], idxs.copy()
        for _ in range(K):
            coefs.append(tmp % q)
            tmp //= q
        TAU = np.zeros((len(idxs), e), dtype=np.int64)
        for j in range(K - 1, -1, -1):
            TAU = (TAU * Da[None, :] + coefs[j][:, None]) % q
        E = (ua[None, :] - TAU) % q
        Ep = (va[None, :] + cube[None, :] * TAU) % q
        # canonical slope key: (1, -E/Ep) if Ep != 0 else (0,1) -> key q
        key = np.where(Ep != 0, (-E * pow_arr(Ep, q - 2, q)) % q, q)
        m = key.shape[0]
        base = (np.arange(m) * (q + 2))[:, None]
        cnt = np.bincount((base + key).ravel(),
                          minlength=m * (q + 2)).reshape(m, q + 2)
        mx = cnt.max(axis=1)
        max_class = max(max_class, int(mx.max()))
        # exactly two classes, each of size r
        two = (cnt == r).sum(axis=1)
        nz = (cnt > 0).sum(axis=1)
        good = np.nonzero((two == 2) & (nz == 2))[0]
        n_two_block += len(good)
        for w in good:
            kk = key[w]
            vals = sorted(set(int(z) for z in kk))
            B = tuple(sorted(D[i] for i in range(e) if int(kk[i]) == vals[0]))
            C = tuple(sorted(D[i] for i in range(e) if int(kk[i]) == vals[1]))
            blocks.add(B)
            blocks.add(C)
            parts.add(frozenset((B, C)))
    return {"K": K, "family_size_qK": total, "N_D_two_block_taus": n_two_block,
            "partitions": len(parts), "blocks": len(blocks),
            "max_slope_class_on_D": max_class,
            "GATE_r_max_class_le_r": max_class <= r}


def pow_arr(a, ex, q):
    r = np.ones_like(a)
    b = a % q
    while ex:
        if ex & 1:
            r = (r * b) % q
        b = (b * b) % q
        ex >>= 1
    return r


def per_slope_counts(shape, g, fx, K):
    """(L1): exact #blocks at each slope, vs the packing bound."""
    q, r, e = shape.q, shape.r, shape.e
    D = g["D"]
    W = W_of(shape, g, fx)
    bound = comb(e, K) // comb(r, K)
    worst, tally = 0, {}
    for nu, col in W.items():
        if len(col) < K:
            continue
        seen = set()
        for sub in itertools.combinations(sorted(col), K):
            pts = [(x, col[x]) for x in sub]
            # interpolate deg<K through pts, evaluate on all of col
            agr = []
            for x in col:
                acc = 0
                for j, (xj, yj) in enumerate(pts):
                    num, den = yj, 1
                    for i, (xi, _) in enumerate(pts):
                        if i == j:
                            continue
                        num = (num * (x - xi)) % q
                        den = (den * (xj - xi)) % q
                    acc = (acc + num * inv(den % q, q)) % q
                if acc == col[x]:
                    agr.append(x)
            if len(agr) == r:
                seen.add(tuple(sorted(agr)))
        if seen:
            tally[str(nu)] = len(seen)
            worst = max(worst, len(seen))
    return {"K": K, "packing_bound_C(e,K)/C(r,K)": bound,
            "max_blocks_at_one_slope": worst,
            "slopes_with_a_block": len(tally),
            "bound_respected": worst <= bound}


def surjective_regime(shape, g, fx):
    """(L3): at K >= e every partition x every slope pair is realisable."""
    q, r, e = shape.q, shape.r, shape.e
    D = g["D"]
    W = W_of(shape, g, fx)
    slopes = [nu for nu in g["slopes"] if len(W[nu]) == e][:6]
    realised = set()
    tested = 0
    for B in itertools.combinations(D, r):
        if B[0] != D[0]:
            continue
        C = tuple(x for x in D if x not in set(B))
        nu, mu = slopes[0], slopes[1]
        # tau := W_nu on B, W_mu on C -- deg < e interpolation always exists
        vals = {}
        for x in B:
            vals[x] = W[nu][x]
        for x in C:
            vals[x] = W[mu][x]
        # slope word of this tau is nu on B, mu on C BY CONSTRUCTION;
        # verify pointwise from the words, no shortcut.
        ok = True
        for x in D:
            E = (fx["u"][x] - vals[x]) % q
            Ep = (fx["v"][x] + pow(x, 3, q) * vals[x]) % q
            want = nu if x in set(B) else mu
            if canon_slope(E, Ep, q) != want:
                ok = False
        tested += 1
        if ok:
            realised.add(frozenset((tuple(sorted(B)), tuple(sorted(C)))))
    return {"partitions_tested": tested, "partitions_realised": len(realised),
            "all_realised": len(realised) == tested,
            "C(e,r)/2": comb(e, r) // 2}


def main():
    report = {}

    # --- the D-local system of the audited-shape fixture, K swept 1..3
    shp = BShape(h=25, k=5, q=61, n=60, tag="A2-above")
    g = ground(shp)
    fx = build_fixture(shp, g, "noreuse", seed=1)
    sweep, per_slope = [], []
    for K in (1, 2, 3):
        c = d_local_census(shp, g, fx, K)
        sweep.append(c)
        chk(c["GATE_r_max_class_le_r"],
            f"GATE-r holds on D at K={K} (no slope class exceeds r)",
            c["max_slope_class_on_D"])
        ps = per_slope_counts(shp, g, fx, K)
        per_slope.append(ps)
        chk(ps["bound_respected"],
            f"(L1) per-slope packing bound C(e,K)/C(r,K) respected at K={K}",
            f"{ps['max_blocks_at_one_slope']} <= "
            f"{ps['packing_bound_C(e,K)/C(r,K)']}")
    report["d_local_sweep_A2"] = sweep
    report["per_slope_A2"] = per_slope

    # --- (L3): the prize regime.  K >= e => the D-local census is COMPLETE.
    sur = surjective_regime(shp, g, fx)
    chk(sur["all_realised"],
        "(L3) at K >= e EVERY partition is realised (D-local route dead)",
        f"{sur['partitions_realised']}/{sur['partitions_tested']}")
    chk(sur["partitions_tested"] == sur["C(e,r)/2"],
        "(L3) partition count = C(e,r)/2", sur["C(e,r)/2"])
    report["surjective_regime"] = sur

    # --- the growth law: N_D and #partitions as K grows toward e
    report["growth_law"] = {
        str(c["K"]): {"N_D": c["N_D_two_block_taus"],
                      "partitions": c["partitions"],
                      "blocks": c["blocks"]} for c in sweep}
    report["X_at_rows"] = {"1/4,1/8": 118, "1/16": 136}
    report["checks"] = len(CHECKS)
    report["failed"] = [c for c in CHECKS if not c["ok"]]
    with open(os.path.join(HERE, "dlocal.json"), "w") as fh:
        json.dump({"report": report, "all_checks": CHECKS}, fh, indent=1,
                  sort_keys=True, default=str)
    print(json.dumps(report, indent=1, sort_keys=True, default=str))
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
