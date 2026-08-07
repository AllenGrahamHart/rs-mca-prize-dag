#!/usr/bin/env python3
"""E4: the constant-scalar word c = lambda*(1,...,1), exactly.

This is the ONLY word whose UB exceeds 10*BOX/q at n=24 ell=4/6 and at
n=32 ell=5 (ub_scan), and at n=32 ell=5 its FILT (~2.6e8) does not fit the
ramguard local wall.  It has exact structure, derived here and CHECKED
against the full engine wherever the full engine fits.

DERIVATION.  For c = lambda*1 the received word is U = lambda*L_C on the
petals, 0 on C u B; since L_C vanishes on C, U agrees with the CODEWORD
Plam := lambda*L_C on all of D\\B and disagrees on every point of B.
Let P' be a contributor with exact agreement set S.
 * P' = Plam is impossible in the mixed family: its agreement set is D\\B,
   which meets every petal fully, hence is not mixed.
 * So V := P' - Plam is a nonzero polynomial of degree < k, therefore has
   at most k-1 roots.  S n (D\\B) is contained in the root set of V, so

        |S n (D\\B)| <= k-1   =>   |S| <= k-1+nb   =>   r <= nb-1 <= b-1.

   COROLLARY (b <= 1):  RET(lambda*1) = 0 exactly.
 * For b = 2 this forces r = 1, nb = b = 2, |S'| = k-1 with
   S' = S n (D\\B) = K u (Petals\\O), and V = mu*L_{S'} with mu != 0
   (deg V <= k-1 = |S'|).  Since |C| = k-1 = t*ell here, a = om.
   The two conditions V(x_y) = -lambda L_C(x_y), y in B = {y1,y2}, are
   consistent iff

        L_C(y1) L_{S'}(y2) = L_C(y2) L_{S'}(y1),

   i.e.  f(K) * h(O) = rho  with
        f(K) = L_K(y2)/L_K(y1),  h(O) = L_O(y1)/L_O(y2),
        rho  = L_C(y2) L_P(y1) / (L_C(y1) L_P(y2)).
   Exactness is then automatic: L_{S'} has degree k-1 and vanishes exactly
   on S', so the agreement set is exactly S' u B = S.
   Hence RET(lambda*1) = #{(K,O): |K|=|O|=a in [1,Lambda], O mixed,
                            f(K) h(O) = rho}, computable by histogram.
"""
import itertools
import os
import sys
from math import comb

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sweep_engine import build, subsets, mixed_mask       # noqa: E402

P = 97


def degen_ret(n, ell, lay):
    c = build(n, P, ell, lay)
    if c.b <= 1:
        return 0, f"b={c.b} <= 1: theorem gives RET = 0 with no computation"
    if c.b != 2:
        return None, f"b={c.b}: only b<=2 is derived here"
    assert c.C == c.tl, (c.C, c.tl)          # a = om needs |C| = t*ell
    y1, y2 = c.bgs
    inv = c.INV
    LP = np.ones(c.n, dtype=np.int64)
    for j in c.P:
        LP = LP * ((c.xs - c.xs[j]) % P) % P
    rho = (int(c.LC[y2]) * int(LP[y1]) % P
           * int(inv[int(c.LC[y1])]) % P * int(inv[int(LP[y2])]) % P)
    total = 0
    per_a = {}
    for a in range(1, c.Lam + 1):
        K = subsets(c.core, a)
        f = np.ones(len(K), dtype=np.int64)
        for i in range(a):
            f = f * c.DIFF[y2, K[:, i]] % P * inv[c.DIFF[y1, K[:, i]]] % P
        O = subsets(range(c.tl), a)
        O = O[mixed_mask(O, c.t, ell, c.tl)]
        if len(O) == 0:
            continue
        h = np.ones(len(O), dtype=np.int64)
        for i in range(a):
            h = (h * c.DIFF[y1, c.P[O[:, i]]] % P
                 * inv[c.DIFF[y2, c.P[O[:, i]]]] % P)
        hf = np.bincount(f, minlength=P)
        hh = np.bincount(h, minlength=P)
        cnt = 0
        for v in range(1, P):
            w = rho * int(inv[v]) % P
            cnt += int(hf[v]) * int(hh[w])
        per_a[a] = cnt
        total += cnt
    return total, f"rho={rho}, per-a {per_a}"


if __name__ == "__main__":
    for n, ell, lay in ((24, 4, "A"), (24, 6, "A"), (32, 3, "A"),
                        (32, 5, "A")):
        v, msg = degen_ret(n, ell, lay)
        cc = build(n, P, ell, lay)
        print(f"n={n} ell={ell} L{lay} t={cc.t} b={cc.b} Lam={cc.Lam}: "
              f"RET(1,...,1) = {v}   [{msg}]")
