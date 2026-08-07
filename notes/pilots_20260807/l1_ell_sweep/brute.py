#!/usr/bin/env python3
"""E0c: a THIRD, fully independent code path for small cells.

No dual conditions, no barycentric identity: for every candidate support S
it solves the Vandermonde system for P of degree < k directly by Gaussian
elimination over F_p, then evaluates P at all n points and compares the
complete agreement set to S.  This adjudicates the one gate mismatch
(n=16 ell=3 LAYOUT-A: engine 100 vs d3_ell_sweep.py 0).
"""
import itertools
import sys

import numpy as np

sys.path.insert(0, "notes/pilots_20260807/l1_ell_sweep")
from sweep_engine import build, consec, geom5, word_U           # noqa: E402

P = 97


def solve(A, y, p):
    """Least ... exact solve of A z = y over F_p; returns z or None."""
    m, k = A.shape
    M = np.concatenate([A % p, (y % p).reshape(-1, 1)], axis=1)
    piv, where = 0, []
    for col in range(k):
        sel = None
        for r in range(piv, m):
            if M[r, col] % p:
                sel = r
                break
        if sel is None:
            continue
        M[[piv, sel]] = M[[sel, piv]]
        M[piv] = M[piv] * pow(int(M[piv, col]), p - 2, p) % p
        for r in range(m):
            if r != piv and M[r, col] % p:
                M[r] = (M[r] - M[r, col] * M[piv]) % p
        where.append(col)
        piv += 1
    for r in range(piv, m):
        if M[r, k] % p:
            return None                       # inconsistent
    z = np.zeros(k, dtype=np.int64)
    for i, col in enumerate(where):
        z[col] = M[i, k] % p
    return z


def brute(n, ell, lay, mode):
    c = build(n, P, ell, lay)
    cv = consec(c.t, P) if mode == "consec" else geom5(c.t, P)
    U = word_U(c, cv)
    k, tl, t, b = c.k, c.tl, c.t, c.b
    V = np.array([[pow(int(x), j, P) for j in range(k)] for x in c.xs],
                 dtype=np.int64)
    box = ret = 0
    hist_a, hist_agr = {}, {}
    for a in range(0, c.Lam + 1):
        for K in itertools.combinations(c.core, a):
            for nb in range(0, b + 1):
                for Bp in itertools.combinations(c.bgs, nb):
                    hi = min(tl, a + nb - b)
                    for om in range(1, hi + 1):
                        for Oi in itertools.combinations(range(tl), om):
                            cnt = [0] * t
                            for z in Oi:
                                cnt[z // ell] += 1
                            if not any(0 < v < ell for v in cnt):
                                continue
                            box += 1
                            O = set(int(c.P[z]) for z in Oi)
                            S = sorted(set(int(z) for z in c.P) - O
                                       | set(K) | set(Bp))
                            z = solve(V[S], U[S], P)
                            if z is None:
                                continue
                            vals = V @ z % P
                            agr = tuple(np.flatnonzero(vals == U).tolist())
                            if agr == tuple(S):
                                ret += 1
                                hist_a[a] = hist_a.get(a, 0) + 1
                                hist_agr[len(S)] = hist_agr.get(len(S), 0) + 1
    return box, ret, hist_a, hist_agr


for n, ell, lay, mode in ((16, 2, "B", "consec"), (16, 2, "B", "geom5"),
                          (16, 2, "A", "consec"), (16, 3, "A", "consec"),
                          (24, 2, "A", "consec")):
    box, ret, ha, hg = brute(n, ell, lay, mode)
    print(f"  BRUTE n={n} ell={ell} LAYOUT-{lay} {mode:6s}: BOX={box:,} "
          f"RET={ret:,}  a={ha} agr={hg}", flush=True)
