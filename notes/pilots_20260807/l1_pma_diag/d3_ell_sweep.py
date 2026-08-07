#!/usr/bin/env python3
"""D3: the ell-sweep -- the census growth parameter is PETAL SIZE, not n.

The banked N10 census only ever ran ell = 2 (two-point petals).  Here the
SAME object is measured at fixed n with ell = 2,3,4 on the maximal-source
chart of pma_arbitrary_petal_source_realizability (statement.md:9-28):
core |C| = k-1, petals T_1..T_t of size ell, background b < ell,
U = 0 on C u B and U = c_i L_C on T_i.

Prediction under the law established at ell=2 (retained ~ BOX/q):
the retained count at fixed n should scale like BOX(ell), i.e. jump by
orders of magnitude from ell=2 to ell=3 with n held FIXED.
"""
from __future__ import annotations

import itertools
from math import comb
import numpy as np


def domain(p, n):
    for g in range(2, p):
        z = pow(g, (p - 1) // n, p)
        if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
            xs = [1] * n
            for j in range(1, n):
                xs[j] = xs[j - 1] * z % p
            return xs
    raise RuntimeError("no generator")


def chart(n, ell):
    """Maximal-source layout: |C| = k-1, t petals of size ell, b = rest."""
    k = n // 2
    t = (n - k + 1) // ell
    b = (n - k + 1) - t * ell
    core = list(range(k - 1))
    bgs = list(range(k - 1, k - 1 + b))
    petals = [tuple(range(k - 1 + b + i * ell, k - 1 + b + (i + 1) * ell))
              for i in range(t)]
    assert len(core) + len(bgs) + t * ell == n
    return k, core, bgs, petals


def run(n, p, ell, scalars_mode="consec", verbose=True):
    k, core, bgs, petals = chart(n, ell)
    t = len(petals)
    if t < 3:
        return None
    xs = domain(p, n)
    pidx = {pt: i for i, pr in enumerate(petals) for pt in pr}
    ppts = sorted(pidx)
    LC = {}
    for pt in range(n):
        v = 1
        for r in core:
            v = v * ((xs[pt] - xs[r]) % p) % p
        LC[pt] = v
    band = ell * (t - 2)
    A_max = len(core) - band
    if A_max < 0:
        return None
    scal = ([(i + 1) % p for i in range(t)] if scalars_mode == "consec"
            else [pow(5, i, p) for i in range(t)])
    U = [0] * n
    for pt, i in pidx.items():
        U[pt] = scal[i] * LC[pt] % p

    alpha = {pt: xs[pt] * LC[pt] % p * LC[pt] % p for pt in ppts}
    box = 0
    survivors = []
    for a in range(0, A_max + 1):
        for K in itertools.combinations(core, a):
            for nb in range(0, len(bgs) + 1):
                for B in itertools.combinations(bgs, nb):
                    om_max = a + nb + t * ell - k - 1
                    for om in range(1, min(len(ppts), om_max) + 1):
                        for O in itertools.combinations(ppts, om):
                            # mixed: some petal partially met
                            if not any(0 < sum(x not in O for x in pr) < ell
                                       for pr in petals):
                                continue
                            box += 1
                            m = a + nb - om
                            drop = list(K) + list(B)
                            R = set(drop[:m - 1])
                            Kp = [x for x in K if x not in R]
                            Bp = [x for x in B if x not in R]
                            acc = 0
                            for pt in ppts:
                                if pt in O:
                                    continue
                                v = alpha[pt]
                                for y in O:
                                    v = v * ((xs[pt] - xs[y]) % p) % p
                                for y in bgs:
                                    if y not in Bp:
                                        v = v * ((xs[pt] - xs[y]) % p) % p
                                den = 1
                                for y in Kp:
                                    den = den * ((xs[pt] - xs[y]) % p) % p
                                acc = (acc + scal[pidx[pt]] * v
                                       * pow(den, p - 2, p)) % p
                            if acc % p == 0:
                                S = sorted(set(ppts) - set(O)
                                           | set(K) | set(Bp) | set(R))
                                S = sorted((set(ppts) - set(O)) | set(K)
                                           | set(B))
                                survivors.append(tuple(S))
    kept, hist = 0, {}
    for S in survivors:
        pts = list(S[:k])
        agree = []
        for target in range(n):
            acc = 0
            for j, pj in enumerate(pts):
                num, den = 1, 1
                for l, pl in enumerate(pts):
                    if l == j:
                        continue
                    num = num * ((xs[target] - xs[pl]) % p) % p
                    den = den * ((xs[pj] - xs[pl]) % p) % p
                acc = (acc + U[pj] * num % p * pow(den, p - 2, p)) % p
            if acc == U[target]:
                agree.append(target)
        if tuple(agree) == S:
            kept += 1
            hist[len(agree)] = hist.get(len(agree), 0) + 1
    lam = 2 * ell + len(bgs) - 2
    if verbose:
        print(f"  n={n} ell={ell} t={t} b={len(bgs)} |C|={len(core)} "
              f"band d>={band} A_max={A_max} Lambda(pred)={lam}")
        print(f"     mixed floor-band BOX = {box:,}   filter survivors "
              f"{len(survivors):,}   EXACT retained = {kept:,}  {hist}")
        print(f"     BOX/q = {box/p:.1f}   (the ell=2 law predicts retained "
              f"~ BOX/q)")
    return box, len(survivors), kept, lam


print("=" * 78)
print("D3 ell-SWEEP at FIXED n -- is the growth parameter n, or petal size?")
print("=" * 78)
print()
print("n=16, q=97:")
r16 = {}
for ell in (2, 3):
    out = run(16, 97, ell)
    if out:
        r16[ell] = out
print()
print("n=24, q=97:")
r24 = {}
for ell in (2, 3, 4):
    out = run(24, 97, ell)
    if out:
        r24[ell] = out
print()
print("=" * 78)
print("SUMMARY: retained count at FIXED n as ell increases")
print("=" * 78)
for n, r in (("16", r16), ("24", r24)):
    if not r:
        continue
    base = r[2][2]
    print(f"  n={n}: " + "   ".join(
        f"ell={e}: box {v[0]:,} retained {v[2]:,} "
        f"({v[2]/base:.1f}x the ell=2 count)" for e, v in sorted(r.items())))
print()
print("Reference: the banked N10 census raised n from 16 to 64 at ell=2 and")
print("got 43 -> 109,391 (a 2544x rise across THREE doublings of n).")
