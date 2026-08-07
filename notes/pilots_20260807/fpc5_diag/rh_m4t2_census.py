#!/usr/bin/env python3
"""FPC5 rate-half M=4,t=2 sharp-cell FIXED-SOURCE guarded split census.

Sharp cell (l1_fpc5_ratehalf_m4_t2_codimtwo_guarded_slice GS1):
    5*ell = k+4,  b = r = s = ell-3,  d = 2*ell-3,
    |C| = k-1 = 5*ell-5,  k = 5*ell-4,  n = 2k = 10*ell-8.

Guarded cell for a fixed source (C,B,T_1..T_4) and labels c_1..c_4:
    deg F, deg W <= d;  L_1 | (W - c_1 F);  L_2 | (W - c_2 F);  L_0 | W
with L_0 = locator of B (deg ell-3), L_i = locator of T_i (deg ell).

CRT form used here (derived, then checked against the kernel rank):
    W = rem_P(F*G),  P = L_0 L_1 L_2 (deg 3*ell-3),
    G = c_1 e_1 + c_2 e_2  (CRT idempotents),
so F lies in the guarded flat V_F  <=>  deg rem_P(F*G) <= d,
i.e. the top (ell-1) coefficients of rem_P(F*G) vanish.  That is exactly
(ell-1) linear conditions on the (2*ell-2)-dim space of deg<=d polys,
giving dim V_F = ell-1 and locator codimension ell-1.

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json
import random
import sys
from itertools import combinations
from math import comb


# ---------------------------------------------------------------- poly ops
def pmulx_sub(p, x, q):
    """p(X)*(X-x) mod q, p given low-to-high."""
    out = [0] * (len(p) + 1)
    for i, c in enumerate(p):
        out[i + 1] = (out[i + 1] + c) % q
        out[i] = (out[i] - c * x) % q
    return out


def pmul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % q
    return out


def pdegree(p):
    d = len(p) - 1
    while d >= 0 and p[d] == 0:
        d -= 1
    return d


def prem(a, m, q):
    """remainder of a mod m (m monic-ish; we normalise by its lead inverse)."""
    a = a[:]
    dm = pdegree(m)
    if dm < 0:
        raise ZeroDivisionError
    inv = pow(m[dm], q - 2, q)
    da = pdegree(a)
    while da >= dm:
        f = a[da] * inv % q
        if f:
            for i in range(dm + 1):
                a[da - dm + i] = (a[da - dm + i] - f * m[i]) % q
        a[da] = 0
        da = pdegree(a)
    return a[: dm] if dm > 0 else []


def pgcd(a, b, q):
    a, b = a[:], b[:]
    while pdegree(b) >= 0:
        a, b = b, prem(a, b, q)
    da = pdegree(a)
    if da < 0:
        return [0]
    inv = pow(a[da], q - 2, q)
    return [c * inv % q for c in a[: da + 1]]


def pinvmod(a, m, q):
    """inverse of a modulo m via extended Euclid."""
    old_r, r = m[:], prem(a, m, q)
    old_s, s = [0], [1]
    while pdegree(r) >= 0:
        # quotient of old_r by r
        dr = pdegree(r)
        inv = pow(r[dr], q - 2, q)
        qq = [0] * max(1, pdegree(old_r) - dr + 1)
        tmp = old_r[:]
        dt = pdegree(tmp)
        while dt >= dr:
            f = tmp[dt] * inv % q
            qq[dt - dr] = f
            if f:
                for i in range(dr + 1):
                    tmp[dt - dr + i] = (tmp[dt - dr + i] - f * r[i]) % q
            tmp[dt] = 0
            dt = pdegree(tmp)
        old_r, r = r, tmp
        prod = pmul(qq, s, q)
        news = [0] * max(len(old_s), len(prod))
        for i, c in enumerate(old_s):
            news[i] = c
        for i, c in enumerate(prod):
            news[i] = (news[i] - c) % q
        old_s, s = s, news
    d = pdegree(old_r)
    if d != 0:
        raise ValueError("not invertible")
    inv = pow(old_r[0], q - 2, q)
    res = prem([c * inv % q for c in old_s], m, q)
    return res


def locator(points, q):
    p = [1]
    for x in points:
        p = pmulx_sub(p, x, q)
    return p


def peval(p, x, q):
    acc = 0
    for c in reversed(p):
        acc = (acc * x + c) % q
    return acc


# --------------------------------------------------------- flat construction
def build_flat(core, bg, petals, labels, pair, ell, q):
    """Return (T, P, G, d) with T the (ell-1) x (d+1) syndrome matrix."""
    d = 2 * ell - 3
    i1, i2 = pair
    L0 = locator(bg, q)
    L1 = locator(petals[i1], q)
    L2 = locator(petals[i2], q)
    c1, c2 = labels[i1], labels[i2]
    P = pmul(pmul(L0, L1, q), L2, q)
    # CRT idempotents e1 (=1 mod L1, 0 mod L0,L2), e2 likewise
    N1 = pmul(L0, L2, q)
    N2 = pmul(L0, L1, q)
    e1 = pmul(N1, pinvmod(N1, L1, q), q)
    e2 = pmul(N2, pinvmod(N2, L2, q), q)
    G = [0] * max(len(e1), len(e2))
    for i, c in enumerate(e1):
        G[i] = (G[i] + c1 * c) % q
    for i, c in enumerate(e2):
        G[i] = (G[i] + c2 * c) % q
    G = prem(G, P, q)
    degP = 3 * ell - 3
    # T[r][m] = coeff of X^{d+1+r} in rem_P(X^m * G)
    rows = ell - 1
    T = [[0] * (d + 1) for _ in range(rows)]
    cur = G[:] + [0] * (degP - len(G))
    for m in range(d + 1):
        for r in range(rows):
            idx = d + 1 + r
            T[r][m] = cur[idx] if idx < len(cur) else 0
        # cur <- rem_P(X*cur)
        nxt = [0] + cur[:-1]
        top = cur[degP - 1]
        if top:
            lead = P[degP]
            f = top * pow(lead, q - 2, q) % q
            for i in range(degP + 1):
                if i < len(nxt):
                    nxt[i] = (nxt[i] - f * P[i]) % q
        cur = nxt[:degP]
    return T, P, G, d, L0, L1, L2, c1, c2


def flat_dim(T, d, q):
    """rank of T -> dim of kernel = (d+1) - rank."""
    rows = [row[:] for row in T]
    m = len(rows)
    ncol = d + 1
    rank = 0
    pivcol = 0
    for col in range(ncol):
        piv = None
        for r in range(rank, m):
            if rows[r][col] % q:
                piv = r
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], q - 2, q)
        rows[rank] = [c * inv % q for c in rows[rank]]
        for r in range(m):
            if r != rank and rows[r][col]:
                f = rows[r][col]
                rows[r] = [(a - f * b) % q for a, b in zip(rows[r], rows[rank])]
        rank += 1
        if rank == m:
            break
    return ncol - rank, rank


# --------------------------------------------------------------- the census
def census(core, bg, petals, labels, pair, ell, q, want_witness=False):
    T, P, G, d, L0, L1, L2, c1, c2 = build_flat(
        core, bg, petals, labels, pair, ell, q
    )
    rows = ell - 1
    n_split = 0
    n_prim = 0
    n_exact = 0
    witness = None
    untouched = [i for i in range(4) if i not in pair]
    for D in combinations(core, d):
        F = locator(D, q)
        ok = True
        for r in range(rows):
            Tr = T[r]
            acc = 0
            for m in range(d + 1):
                acc += Tr[m] * F[m]
            if acc % q:
                ok = False
                break
        if not ok:
            continue
        n_split += 1
        W = prem(pmul(F, G, q), P, q)
        # primitivity: gcd(F,W)=1  <=>  W nonzero on every root of F
        if any(peval(W, x, q) == 0 for x in D):
            continue
        n_prim += 1
        # untouched-petal nonagreement
        bad = False
        for u in untouched:
            cu = labels[u]
            for x in petals[u]:
                if (peval(W, x, q) - cu * peval(F, x, q)) % q == 0:
                    bad = True
                    break
            if bad:
                break
        if bad:
            continue
        n_exact += 1
        if want_witness and witness is None:
            witness = {"D": list(D), "F": F, "W": W}
    return n_split, n_prim, n_exact, witness


def make_source(pts, ell, q, rng):
    pool = pts[:]
    rng.shuffle(pool)
    nc = 5 * ell - 5
    b = ell - 3
    core = pool[:nc]
    bg = pool[nc:nc + b]
    petals = []
    off = nc + b
    for i in range(4):
        petals.append(pool[off:off + ell])
        off += ell
    labels = rng.sample(range(1, q), 4)
    return core, bg, petals, labels


def domain(n, q):
    """n distinct nonzero points; use mu_n when n | q-1, else first n units."""
    if (q - 1) % n == 0:
        g = None
        for cand in range(2, q):
            if pow(cand, (q - 1) // 2, q) != 1:
                ok = True
                for p in set(prime_factors((q - 1))):
                    if pow(cand, (q - 1) // p, q) == 1:
                        ok = False
                        break
                if ok:
                    g = cand
                    break
        if g is not None:
            h = pow(g, (q - 1) // n, q)
            pts = [pow(h, i, q) for i in range(n)]
            if len(set(pts)) == n:
                return pts, True
    return list(range(1, n + 1)), False


def prime_factors(m):
    fs = []
    d = 2
    while d * d <= m:
        while m % d == 0:
            fs.append(d)
            m //= d
        d += 1
    if m > 1:
        fs.append(m)
    return fs


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "gate"
    if mode == "gate":
        # A1 REPLICATION GATE at the banked cell (32,16,4,4,1,1,5), F_97.
        ell, q = 4, 97
        n = 10 * ell - 8
        k = 5 * ell - 4
        assert (n, k) == (32, 16)
        assert 5 * ell == k + 4
        pts, cyc = domain(n, q)
        assert cyc and len(pts) == 32
        rng = random.Random(20260807)
        dims = set()
        ranks = set()
        for _ in range(40):
            core, bg, petals, labels = make_source(pts, ell, q, rng)
            for pair in combinations(range(4), 2):
                T, P, G, d, *_ = build_flat(core, bg, petals, labels,
                                            pair, ell, q)
                kd, rk = flat_dim(T, d, q)
                dims.add(kd)
                ranks.add(rk)
        print(json.dumps({
            "gate": "A1",
            "cell": [n, k, ell, 4, ell - 3, ell - 3, 2 * ell - 3],
            "q": q,
            "mu_n_domain": cyc,
            "dim_V_F_observed": sorted(dims),
            "dim_V_F_expected": ell - 1,
            "syndrome_rank_observed": sorted(ranks),
            "syndrome_rank_expected": ell - 1,
            "affine_monic_chart_dim_expected": ell - 2,
            "locator_codimension_expected": ell - 1,
            "PASS": sorted(dims) == [ell - 1] and sorted(ranks) == [ell - 1],
        }))
        return

    if mode == "sweep":
        ell = int(sys.argv[2])
        q = int(sys.argv[3])
        nsrc = int(sys.argv[4])
        seed = int(sys.argv[5]) if len(sys.argv) > 5 else 20260807
        n = 10 * ell - 8
        k = 5 * ell - 4
        d = 2 * ell - 3
        nc = 5 * ell - 5
        assert q > n
        pts, cyc = domain(n, q)
        rng = random.Random(seed)
        tot_split = tot_prim = tot_exact = 0
        max_split = max_prim = max_exact = 0
        cells = 0
        hits = []
        for si in range(nsrc):
            core, bg, petals, labels = make_source(pts, ell, q, rng)
            for pair in combinations(range(4), 2):
                ns, npm, nex, w = census(core, bg, petals, labels, pair,
                                         ell, q, want_witness=True)
                cells += 1
                tot_split += ns
                tot_prim += npm
                tot_exact += nex
                max_split = max(max_split, ns)
                max_prim = max(max_prim, npm)
                max_exact = max(max_exact, nex)
                if nex:
                    hits.append({"src": si, "pair": list(pair),
                                 "split": ns, "prim": npm, "exact": nex,
                                 "D": w["D"] if w else None})
        mu = comb(nc, d) / q ** (ell - 1)
        print(json.dumps({
            "mode": "sweep", "ell": ell, "q": q, "n": n, "k": k, "d": d,
            "core": nc, "b": ell - 3, "s": ell - 3,
            "two_power_n": (n & (n - 1)) == 0,
            "mu_n_domain": cyc,
            "sources": nsrc, "cells": cells,
            "subsets_per_cell": comb(nc, d),
            "mu_t2": mu,
            "mean_split": tot_split / cells,
            "mean_prim": tot_prim / cells,
            "mean_exact": tot_exact / cells,
            "ratio_mean_split_over_mu": (tot_split / cells) / mu if mu else None,
            "max_split": max_split, "max_prim": max_prim,
            "max_exact": max_exact,
            "tot_split": tot_split, "tot_prim": tot_prim,
            "tot_exact": tot_exact,
            "hits": hits[:20],
        }))
        return


if __name__ == "__main__":
    main()
