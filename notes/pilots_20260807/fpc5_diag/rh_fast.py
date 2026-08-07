#!/usr/bin/env python3
"""Fast fixed-source guarded split census for FPC5 rate-half M=4,t=2.

Same object as rh_m4t2_census.py (which holds the A1 gate and the slow
reference implementation); this version adds a DFS with an incremental
locator product and a single-functional prefilter, then verifies every
survivor against the full (ell-1)-row syndrome.

Measured functionals (CATCH-19C):
  N_split  #{D subset C, |D|=d : L_D in the guarded flat V_F}
  N_prim   ... additionally gcd(L_D, W)=1
  N_exact  ... additionally (W - c_u L_D)(x) != 0 on both untouched petals
  mu_t2    binom(5ell-5, 2ell-3) / q^(ell-1)      (first-moment prediction)
"""
from __future__ import annotations

import json
import random
import sys
from itertools import combinations
from math import comb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from rh_m4t2_census import (  # noqa: E402
    build_flat, domain, flat_dim, locator, peval, pmul, prem,
)


def census_fast(core, bg, petals, labels, pair, ell, q, rng):
    T, P, G, d, L0, L1, L2, c1, c2 = build_flat(
        core, bg, petals, labels, pair, ell, q)
    rows = ell - 1
    # single random functional u = sum_r a_r T[r]
    coef = [rng.randrange(q) for _ in range(rows)]
    u = [0] * (d + 1)
    for r in range(rows):
        ar = coef[r]
        if ar:
            Tr = T[r]
            for m in range(d + 1):
                u[m] = (u[m] + ar * Tr[m]) % q
    ushift = [u[m + 1] for m in range(d)]        # pairs with p[m]
    ulow = u[:d]                                  # pairs with p[m]
    N = len(core)
    survivors = []

    def rec(start, depth, p):
        if depth == d - 1:
            s0 = 0
            s1 = 0
            for m in range(d):
                pm = p[m]
                if pm:
                    s0 += ushift[m] * pm
                    s1 += ulow[m] * pm
            s0 %= q
            s1 %= q
            for i in range(start, N):
                x = core[i]
                if (s0 - x * s1) % q == 0:
                    survivors.append((depth_stack[:depth], p, x, i))
            return
        need = d - depth
        for i in range(start, N - need + 1):
            x = core[i]
            np_ = [0] * (len(p) + 1)
            for m, c in enumerate(p):
                if c:
                    np_[m + 1] = (np_[m + 1] + c) % q
                    np_[m] = (np_[m] - c * x) % q
            depth_stack[depth] = i
            rec(i + 1, depth + 1, np_)

    depth_stack = [0] * d
    rec(0, 0, [1])

    untouched = [i for i in range(4) if i not in pair]
    n_split = n_prim = n_exact = 0
    witness = None
    for idxs, p, x, i in survivors:
        F = [0] * (len(p) + 1)
        for m, c in enumerate(p):
            if c:
                F[m + 1] = (F[m + 1] + c) % q
                F[m] = (F[m] - c * x) % q
        ok = True
        for r in range(rows):
            Tr = T[r]
            acc = 0
            for m in range(d + 1):
                if F[m]:
                    acc += Tr[m] * F[m]
            if acc % q:
                ok = False
                break
        if not ok:
            continue
        n_split += 1
        D = [core[j] for j in idxs] + [x]
        W = prem(pmul(F, G, q), P, q)
        if any(peval(W, xx, q) == 0 for xx in D):
            continue
        n_prim += 1
        bad = False
        for un in untouched:
            cu = labels[un]
            for xx in petals[un]:
                if (peval(W, xx, q) - cu * peval(F, xx, q)) % q == 0:
                    bad = True
                    break
            if bad:
                break
        if bad:
            continue
        n_exact += 1
        if witness is None:
            witness = {"D": sorted(D), "F": F, "W": W,
                       "labels": [labels[pair[0]], labels[pair[1]]]}
    return n_split, n_prim, n_exact, witness, len(survivors)


def make_source(pts, ell, q, rng):
    pool = pts[:]
    rng.shuffle(pool)
    nc = 5 * ell - 5
    b = ell - 3
    core = sorted(pool[:nc])
    bg = pool[nc:nc + b]
    petals = []
    off = nc + b
    for i in range(4):
        petals.append(pool[off:off + ell])
        off += ell
    labels = rng.sample(range(1, q), 4)
    return core, bg, petals, labels


def main():
    ell = int(sys.argv[1])
    q = int(sys.argv[2])
    nsrc = int(sys.argv[3])
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 20260807
    npair = int(sys.argv[5]) if len(sys.argv) > 5 else 6
    n = 10 * ell - 8
    k = 5 * ell - 4
    d = 2 * ell - 3
    nc = 5 * ell - 5
    assert q > n
    pts, cyc = domain(n, q)
    rng = random.Random(seed)
    tot = [0, 0, 0]
    mx = [0, 0, 0]
    cells = 0
    surv_tot = 0
    hits = []
    dimset = set()
    pairs = list(combinations(range(4), 2))[:npair]
    for si in range(nsrc):
        core, bg, petals, labels = make_source(pts, ell, q, rng)
        for pair in pairs:
            T, _, _, dd, *_ = build_flat(core, bg, petals, labels, pair, ell, q)
            kd, rk = flat_dim(T, dd, q)
            dimset.add(kd)
            ns, npm, nex, w, nsurv = census_fast(
                core, bg, petals, labels, pair, ell, q, rng)
            cells += 1
            surv_tot += nsurv
            tot[0] += ns
            tot[1] += npm
            tot[2] += nex
            mx[0] = max(mx[0], ns)
            mx[1] = max(mx[1], npm)
            mx[2] = max(mx[2], nex)
            if nex:
                hits.append({"src": si, "pair": list(pair), "split": ns,
                             "prim": npm, "exact": nex,
                             "D": w["D"] if w else None})
    mu = comb(nc, d) / q ** (ell - 1)
    print(json.dumps({
        "ell": ell, "q": q, "n": n, "k": k, "d": d, "core": nc,
        "b": ell - 3, "s": ell - 3,
        "two_power_n": (n & (n - 1)) == 0, "mu_n_domain": cyc,
        "dim_V_F_observed": sorted(dimset),
        "sources": nsrc, "cells": cells,
        "subsets_per_cell": comb(nc, d),
        "prefilter_survivors_per_cell": surv_tot / cells,
        "prefilter_expected": comb(nc, d) / q,
        "mu_t2": mu,
        "mean_split": tot[0] / cells,
        "mean_prim": tot[1] / cells,
        "mean_exact": tot[2] / cells,
        "ratio_mean_split_over_mu": (tot[0] / cells) / mu,
        "ratio_mean_split_over_q_mu": (tot[0] / cells) / (q * mu),
        "max_split": mx[0], "max_prim": mx[1], "max_exact": mx[2],
        "tot_split": tot[0], "tot_prim": tot[1], "tot_exact": tot[2],
        "hits": hits[:25],
    }))


if __name__ == "__main__":
    main()
