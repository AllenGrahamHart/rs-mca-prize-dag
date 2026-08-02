#!/usr/bin/env python3
"""EXPERIMENT B -- exhaustive (H4) constant over the WHOLE design space.

For every affine line L of AG(h,q) (= every degree-A pencil, core.py header)
compute
    count(L)  = #{A-subsets S : E(S) in L}                (= all witnesses)
    Gamma_lo^full(L) = #{S on L : |S ^ S'| <= K-1 for every other S' on L}
    Gamma_lo^lex(L)  = the same after the support-lex first-match selector
                       keeps one witness per slope
and report the maxima, both raw and after the gauge-invariant admissibility
gate.  (H4) asks whether Gamma_lo <= mu := C(n,A)/q^{h-1}; the measured
  lambda := max_L Gamma_lo(L) / mu
is the exact (H4) constant at that scale.

Enumeration is over the (q^h-1)/(q-1) projective directions; for each, the
image points are reduced modulo the direction and grouped, so every line is
visited exactly once.  Exact integer arithmetic throughout.

Run:  tools/ramguard local -- python3 expB.py CASE...
"""
from __future__ import annotations

import json
import os
import sys
from itertools import combinations, product

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np

import core
from expA import CASES

HERE = os.path.dirname(os.path.abspath(__file__))


def directions(h, q):
    """canonical representatives of P^{h-1}(F_q): first nonzero entry = 1."""
    for t0 in range(h):
        for tail in product(range(q), repeat=h - 1 - t0):
            yield (0,) * t0 + (1,) + tail


def fold_invariant(dv, base, n, q, K, h, w):
    gc = np.gcd(n, K)
    for M in range(2, int(gc) + 1):
        if gc % M:
            continue
        zt = pow(int(w), n // M, q)
        zz = [pow(zt, j + 1, q) for j in range(h)]
        dv2 = tuple(dv[t] * zz[t] % q for t in range(h))
        t0 = next(t for t in range(h) if dv2[t])
        inv = pow(dv2[t0], q - 2, q)
        cd2 = tuple(x * inv % q for x in dv2)
        if cd2 != tuple(dv):
            continue
        b2 = tuple(base[t] * zz[t] % q for t in range(h))
        s0 = next(t for t in range(h) if dv[t])
        b2r = tuple((b2[t] - b2[s0] * dv[t]) % q for t in range(h))
        if b2r == tuple(base):
            return True, M
    return False, 0


def run(name, gl_floor=3):
    prm = CASES[name]
    n, q, K, h = prm["n"], prm["q"], prm["K"], prm["h"]
    A = K + h
    D = core.domain(q, n)
    w = core.root_of_unity(q, n)

    S_all, E_all = [], []
    for S in combinations(range(n), A):
        S_all.append(core.mask_of(S))
        E_all.append(core.moment_vector([D[i] for i in S], h, q))
    NS = len(S_all)
    P = np.array(E_all, dtype=np.int64)
    masks = np.array(S_all, dtype=object)
    mu = NS / q ** (h - 1)

    pw = np.array([q ** j for j in range(h)], dtype=np.int64)
    hist = {}
    best_cnt = (0, None)
    best_lo = (0, None)
    best_lo_adm = (0, None)
    best_lex_adm = (0, None)
    ndir = 0
    for dv in directions(h, q):
        ndir += 1
        t0 = next(t for t in range(h) if dv[t])
        dva = np.array(dv, dtype=np.int64)
        red = (P - P[:, t0:t0 + 1] * dva[None, :]) % q
        key = red @ pw
        order = np.argsort(key, kind="stable")
        ks = key[order]
        starts = np.concatenate(([0], np.flatnonzero(np.diff(ks)) + 1))
        ends = np.concatenate((starts[1:], [NS]))
        sizes = ends - starts
        for c in np.unique(sizes):
            hist[int(c)] = hist.get(int(c), 0) + int((sizes == c).sum())
        thr = max(gl_floor, best_lo[0], best_lo_adm[0], best_lex_adm[0])
        big = np.flatnonzero(sizes >= min(thr, int(sizes.max())))
        for b in big:
            idx = order[starts[b]:ends[b]]
            cnt = int(sizes[b])
            base = tuple(int(x) for x in red[idx[0]])
            if cnt > best_cnt[0]:
                best_cnt = (cnt, (dv, base))
            if cnt < thr:
                continue
            mk = [S_all[i] for i in idx]
            lo = len(core.gamma_lo(mk, K))
            byz = {}
            for i in idx:
                z = int(P[i][t0])
                byz.setdefault(z, []).append(S_all[i])
            sel = [min(v) for v in byz.values()]
            lex = len(core.gamma_lo(sel, K))
            inv, M = fold_invariant(dv, base, n, q, K, h, w)
            if lo > best_lo[0]:
                best_lo = (lo, (dv, base, cnt, inv))
            if not inv:
                if lo > best_lo_adm[0]:
                    best_lo_adm = (lo, (dv, base, cnt))
                if lex > best_lex_adm[0]:
                    best_lex_adm = (lex, (dv, base, cnt))

    nlines = ndir * q ** (h - 1)
    out = dict(case=name, params=dict(n=n, q=q, K=K, h=h, A=A),
               subsets=NS, mu_mean_witnesses_per_line=mu,
               directions=ndir, lines=nlines,
               count_histogram={str(k): v for k, v in sorted(hist.items())},
               max_count=best_cnt[0],
               max_count_line=[list(best_cnt[1][0]), list(best_cnt[1][1])],
               max_gamma_lo_any=best_lo[0],
               max_gamma_lo_any_line=[list(best_lo[1][0]), list(best_lo[1][1]),
                                      best_lo[1][2], best_lo[1][3]]
               if best_lo[1] else None,
               max_gamma_lo_admissible=best_lo_adm[0],
               max_gamma_lo_admissible_line=[list(best_lo_adm[1][0]),
                                             list(best_lo_adm[1][1]),
                                             best_lo_adm[1][2]]
               if best_lo_adm[1] else None,
               max_gamma_lo_lex_admissible=best_lex_adm[0],
               lambda_full=best_lo_adm[0] / mu,
               lambda_lex=best_lex_adm[0] / mu,
               budget_8n3=8 * n ** 3)
    path = os.path.join(HERE, f"EXPB_{name}.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f"[{name}] n={n} q={q} K={K} h={h} A={A} | subsets={NS} "
          f"lines={nlines} mu={mu:.4g}")
    print(f"   max count over ALL lines            = {best_cnt[0]}"
          f"  (x{best_cnt[0]/mu:.3g} mu)")
    print(f"   max Gamma_lo over ALL lines         = {best_lo[0]}"
          f"  (x{best_lo[0]/mu:.3g} mu)")
    print(f"   max Gamma_lo, gate-admissible       = {best_lo_adm[0]}"
          f"  (lambda_full={best_lo_adm[0]/mu:.3g})")
    print(f"   max Gamma_lo after lex first-match  = {best_lex_adm[0]}"
          f"  (lambda_lex={best_lex_adm[0]/mu:.3g})")
    print(f"   -> {path}")
    return out


if __name__ == "__main__":
    for nm in (sys.argv[1:] or ["A5"]):
        run(nm)
