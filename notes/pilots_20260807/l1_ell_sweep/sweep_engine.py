#!/usr/bin/env python3
"""E1: the ell-sweep engine (PREREG R1 existence test, exact).

Replaces the round-21 "drop m-1 points" filter (d3_ell_sweep.py:84-86),
which is only valid at b<=1, by the exact top-r-coefficient test

    sum_{j in S} U_j x_j^{s+1} prod_{l in D\\S}(x_j - x_l) = 0,  s = 0..r-1

(necessary AND sufficient for a degree-<k interpolant on S, |S| = k+r).
Weights use prod_{l in D, l!=j}(x_j - x_l) = n x_j^{-1} on mu_n.

Factorisation used for speed (this is the whole trick):

    sum_i c_i g^{(s)}_i = sum_{j in petals} RK[K,j] * Vs[B',O,j] * c_{i(j)}

with RK[K,j] = 1/L_K(x_j) depending only on K, and
Vs[B',O,j] = x_j^{s+1} L_C(x_j)^2 L_B(x_j) L_O(x_j) / L_{B'}(x_j) * 1{j notin O}
depending only on (B',O,s).  The filter over a whole (K,O) stratum is then
one float64 matmul (entries < 16*96*96 = 147456, exact in float64) followed
by a mod-97 zero test.

Exactness guard (complete agreement = S) is done by the barycentric
identity, for every y in W = D\\S:

    U_y x_y prod_{l in W, l!=y}(x_y-x_l)  ==  sum_{j in S} num_j/(x_y-x_j),
    num_j = U_j x_j prod_{l in W}(x_j - x_l).

No node/dag/tool is touched.  Draft-only.
"""
from __future__ import annotations

import itertools
import json
import sys
from math import comb

import numpy as np


# ------------------------------------------------------------------ charts --
def domain(p, n):
    for g in range(2, p):
        z = pow(g, (p - 1) // n, p)
        if pow(z, n, p) == 1 and pow(z, n // 2, p) != 1:
            xs = [1] * n
            for j in range(1, n):
                xs[j] = xs[j - 1] * z % p
            return xs
    raise RuntimeError("no generator")


def layout_contig(n, ell):
    """LAYOUT-A -- verbatim d3_ell_sweep.py:32-42."""
    k = n // 2
    t = (n - k + 1) // ell
    b = (n - k + 1) - t * ell
    core = list(range(k - 1))
    bgs = list(range(k - 1, k - 1 + b))
    petals = [tuple(range(k - 1 + b + i * ell, k - 1 + b + (i + 1) * ell))
              for i in range(t)]
    assert len(core) + len(bgs) + t * ell == n
    return k, core, bgs, petals


def layout_coset(n, ell):
    """LAYOUT-B -- petals are cosets of mu_ell.  At ell=2 this is exactly
    a5_scale32.py:24-31 (checked in the gate)."""
    assert n % ell == 0, (n, ell)
    k = n // 2
    t = (n - k + 1) // ell
    b = (n - k + 1) - t * ell
    step = n // ell
    assert t <= step
    cosets = [tuple((j + step * m) % n for m in range(ell)) for j in range(step)]
    petals = cosets[step - t:]
    used = {pt for pr in petals for pt in pr}
    rest = [i for i in range(n) if i not in used]
    assert len(rest) == k - 1 + b
    return k, rest[:k - 1], rest[k - 1:], petals


LAYOUTS = {"A": layout_contig, "B": layout_coset}


# ------------------------------------------------------------------ tables --
class Ctx:
    pass


def build(n, p, ell, lay):
    c = Ctx()
    c.n, c.p, c.ell, c.lay = n, p, ell, lay
    k, core, bgs, petals = LAYOUTS[lay](n, ell)
    c.k, c.core, c.bgs, c.petals = k, core, bgs, petals
    c.t, c.b, c.C = len(petals), len(bgs), len(core)
    c.Lam = 2 * ell + c.b - 2
    c.xs = np.array(domain(p, n), dtype=np.int64)
    c.P = np.array([pt for pr in petals for pt in pr], dtype=np.int64)
    c.tl = len(c.P)
    c.P32 = c.P.astype(np.int32)
    c.pid = np.zeros(n, dtype=np.int64)
    for i, pr in enumerate(petals):
        for pt in pr:
            c.pid[pt] = i
    # L_C on every domain point
    LC = np.ones(n, dtype=np.int64)
    for r in core:
        LC = LC * ((c.xs - c.xs[r]) % p) % p
    c.LC = LC
    LB = np.ones(n, dtype=np.int64)
    for y in bgs:
        LB = LB * ((c.xs - c.xs[y]) % p) % p
    c.LB = LB
    c.DIFF = ((c.xs[:, None] - c.xs[None, :]) % p).astype(np.int32)
    inv = np.array([0] + [pow(i, p - 2, p) for i in range(1, p)], dtype=np.int64)
    c.INV = inv
    c.DINV = inv[c.DIFF].astype(np.int32)     # DINV[u,u] = 0, never used
    # A0[j] = x_j * L_C(x_j)^2   on petal points
    c.A0 = (c.xs[c.P] * c.LC[c.P] % p * c.LC[c.P] % p).astype(np.int32)
    c.xP = c.xs[c.P].astype(np.int32)
    c.xs32 = c.xs.astype(np.int32)
    return c


def word_U(c, cv):
    """The received word as a length-n vector: 0 on C u B, c_i L_C on T_i."""
    U = np.zeros(c.n, dtype=np.int64)
    U[c.P] = np.asarray(cv, dtype=np.int64)[c.pid[c.P]] * c.LC[c.P] % c.p
    return U.astype(np.int32)


def mindeg_word(c):
    """PREREG R0.5(3): kill as many TOP coefficients of the interpolant of U
    over mu_n as possible.  coeff_s ~ sum_i c_i D_s(i),
    D_s(i) = sum_{pt in T_i} L_C(x_pt) x_pt^{-s}."""
    p, n, t = c.p, c.n, c.t
    xinv = c.INV[c.xs]
    rows = []
    for s in range(n - 1, -1, -1):
        v = np.zeros(t, dtype=np.int64)
        w = np.array([pow(int(xinv[pt]), s, p) for pt in c.P], dtype=np.int64)
        contrib = c.LC[c.P] * w % p
        for i in range(t):
            v[i] = int(contrib[c.pid[c.P] == i].sum() % p)
        rows.append(v)
    # add rows until rank = t; the previous kernel is the answer
    M, best, jbest = [], None, 0
    for j, v in enumerate(rows):
        M.append(v)
        ker = nullspace(np.array(M, dtype=np.int64), p)
        if ker is None:
            break
        best, jbest = ker, j + 1
    if best is None:
        raise RuntimeError("no kernel even at j=1")
    return best, n - 1 - jbest        # jbest top coefficients killed


def nullspace(M, p):
    """One nonzero kernel vector of M over F_p, or None."""
    A = M % p
    rows, cols = A.shape
    piv, where = 0, []
    for col in range(cols):
        sel = None
        for r in range(piv, rows):
            if A[r, col] % p:
                sel = r
                break
        if sel is None:
            continue
        A[[piv, sel]] = A[[sel, piv]]
        A[piv] = A[piv] * pow(int(A[piv, col]), p - 2, p) % p
        for r in range(rows):
            if r != piv and A[r, col] % p:
                A[r] = (A[r] - A[r, col] * A[piv]) % p
        where.append(col)
        piv += 1
        if piv == rows:
            break
    free = [cc for cc in range(cols) if cc not in where]
    if not free:
        return None
    v = np.zeros(cols, dtype=np.int64)
    v[free[0]] = 1
    for i, col in enumerate(where):
        v[col] = (-A[i, free[0]]) % p
    return v % p


# ------------------------------------------------------------------- strata --
def subsets(items, r):
    if r == 0:
        return np.zeros((1, 0), dtype=np.int64)
    return np.array(list(itertools.combinations(items, r)), dtype=np.int64)


def mixed_mask(O, t, ell, tl):
    """O (NO, om) indices into 0..tl-1.  Mixed = some petal partially met."""
    NO, om = O.shape
    if om == 0:
        return np.zeros(NO, dtype=bool)
    cnt = np.zeros((NO, t), dtype=np.int64)
    pet = O // ell                      # petal index of each omitted point
    np.add.at(cnt, (np.arange(NO)[:, None], pet), 1)
    return np.any((cnt > 0) & (cnt < ell), axis=1)


def complement(sub, universe_size):
    """Row-wise complement of sub (Ns, m) inside range(universe_size)."""
    Ns, m = sub.shape
    mask = np.ones((Ns, universe_size), dtype=bool)
    if m:
        mask[np.arange(Ns)[:, None], sub] = False
    idx = np.tile(np.arange(universe_size), (Ns, 1))
    return idx[mask].reshape(Ns, universe_size - m)


# --------------------------------------------------------------------- run --
def run(c, words, band=True, mixed=True, a_cap=None, chunk=2_000_000,
        exact_chunk=40_000, verbose=False, collect_gamma=0, rng=None):
    """Returns per-word dicts with BOX/FILT/RET and histograms."""
    p, n, k, ell, t, b, C, tl = c.p, c.n, c.k, c.ell, c.t, c.b, c.C, c.tl
    cap = C if a_cap is None else min(a_cap, C)
    if band:
        cap = min(cap, c.Lam)
    W = len(words)
    Us = [word_U(c, cv) for cv in words]
    ctil = np.stack([np.asarray(cv, dtype=np.int64)[c.pid[c.P]] for cv in words]).astype(np.int32)
    res = [{"BOX": 0, "FILT": 0, "RET": 0, "hist_agr": {}, "hist_a": {},
            "hist_r": {}} for _ in range(W)]
    box_total = 0
    gam_rows, gam_meta = [], []
    for a in range(0, cap + 1):
        Karr = subsets(c.core, a)
        NK = Karr.shape[0]
        RK = np.ones((NK, tl), dtype=np.int32)
        for i in range(a):
            RK = RK * c.DINV[c.P[:, None], Karr[:, i][None, :]].T % p
        Kcomp = complement(
            np.searchsorted(np.array(c.core), Karr) if a else Karr, C)
        Kcomp_dom = np.array(c.core, dtype=np.int32)[Kcomp]
        for nb in range(0, b + 1):
            for Bp in itertools.combinations(c.bgs, nb):
                Brest = [y for y in c.bgs if y not in Bp]
                prodbg = np.ones(tl, dtype=np.int32)
                for y in Brest:
                    prodbg = prodbg * c.DIFF[c.P, y] % p
                hi = min(tl, a + nb - b)
                for om in range(0 if not mixed else 1, hi + 1):
                    r = a + nb - b - om + 1
                    if r < 1:
                        continue
                    Oall = subsets(range(tl), om)
                    if mixed:
                        Oall = Oall[mixed_mask(Oall, t, ell, tl)]
                    NO = Oall.shape[0]
                    if NO == 0 or NK == 0:
                        continue
                    box_total += NK * NO
                    V0 = np.broadcast_to(c.A0 * prodbg % p, (NO, tl)).copy()
                    for i in range(om):
                        V0 = V0 * c.DIFF[c.P[:, None],
                                         c.P[Oall[:, i]][None, :]].T % p
                    Ocomp = complement(Oall, tl)
                    if collect_gamma and r == 1 and len(gam_rows) < collect_gamma:
                        _sample_gamma(c, RK, V0, Oall, gam_rows, gam_meta,
                                      collect_gamma, a, nb, tuple(Bp), om, rng)
                    for wi in range(W):
                        _do_word(c, wi, res, RK, V0, Oall, Ocomp, Karr,
                                 Kcomp_dom, Bp, Brest, a, nb, om, r,
                                 Us[wi], ctil[wi], chunk, exact_chunk)
            if verbose:
                print(f"    a={a} nb={nb} done, box so far {box_total:,}",
                      flush=True)
    for d in res:
        d["BOX"] = box_total
    return res, (np.array(gam_rows, dtype=np.int64) if gam_rows else None,
                 gam_meta)


def _sample_gamma(c, RK, V0, Oall, gam_rows, gam_meta, cap, a, nb, Bp, om, rng):
    p, tl, t = c.p, c.tl, c.t
    NK, NO = RK.shape[0], V0.shape[0]
    take = min(cap - len(gam_rows), 400)
    if take <= 0 or rng is None:
        return
    ki = rng.integers(0, NK, size=take)
    oi = rng.integers(0, NO, size=take)
    prod = RK[ki] * V0[oi] % p                       # (take, tl)
    g = np.zeros((take, t), dtype=np.int64)
    np.add.at(g, (np.arange(take)[:, None],
                  np.broadcast_to(c.pid[c.P], (take, tl))), prod)
    gam_rows.extend((g % p).tolist())
    gam_meta.extend([(a, nb, Bp, om)] * take)


def _do_word(c, wi, res, RK, V0, Oall, Ocomp, Karr, Kcomp_dom, Bp, Brest,
             a, nb, om, r, U, ct, chunk, exact_chunk):
    p, tl, k = c.p, c.tl, c.k
    NK, NO = RK.shape[0], V0.shape[0]
    Vc = V0 * ct % p
    RKf = RK.astype(np.float64)
    Vcf = Vc.astype(np.float64)
    step = max(1, min(NK, int(chunk // max(NO, 1))))
    pws = []
    pw = np.ones(tl, dtype=np.int32)
    for _ in range(1, r):
        pw = pw * c.xP % p
        pws.append(pw.copy())
    nW = (c.C - a) + (c.b - nb) + om
    Brest_arr = np.array(Brest, dtype=np.int32)
    kept = 0
    nfilt = 0
    # STREAMING: each matmul chunk is carried all the way through the deep
    # conditions and the exactness guard before the next one is formed, so
    # peak memory is O(chunk) even for degenerate words with huge FILT.
    for t0 in range(0, NK, step):
        M = RKf[t0:t0 + step] @ Vcf.T
        Z = (M.astype(np.int32) % p) == 0
        del M
        ii, jj = np.nonzero(Z)
        del Z
        if not len(ii):
            continue
        ki = (ii + t0).astype(np.int32)
        oi = jj.astype(np.int32)
        del ii, jj
        if r > 1:
            kk_, oo_ = [], []
            for s1 in range(0, len(ki), 100_000):
                kc, oc = ki[s1:s1 + 100_000], oi[s1:s1 + 100_000]
                T = RK[kc] * Vc[oc] % p
                keep = np.ones(len(kc), dtype=bool)
                for pwv in pws:
                    keep &= ((T * pwv).sum(axis=1) % p) == 0
                    if not keep.any():
                        break
                del T
                if keep.any():
                    kk_.append(kc[keep])
                    oo_.append(oc[keep])
            if not kk_:
                continue
            ki, oi = np.concatenate(kk_), np.concatenate(oo_)
        nfilt += len(ki)
        kept += _exact_pass(c, ki, oi, Oall, Ocomp, Kcomp_dom, Brest_arr,
                            nW, U, exact_chunk)
    res[wi]["FILT"] += nfilt
    if kept:
        d = res[wi]
        d["RET"] += kept
        d["hist_agr"][k + r] = d["hist_agr"].get(k + r, 0) + kept
        d["hist_a"][a] = d["hist_a"].get(a, 0) + kept
        d["hist_r"][r] = d["hist_r"].get(r, 0) + kept


def _exact_pass(c, ki, oi, Oall, Ocomp, Kcomp_dom, Brest_arr, nW, U,
                exact_chunk):
    p = c.p
    kept = 0
    for s0 in range(0, len(ki), exact_chunk):
        kk = ki[s0:s0 + exact_chunk]
        oo = oi[s0:s0 + exact_chunk]
        Ns = len(kk)
        Odom = c.P32[Oall[oo]]                          # (Ns, om)
        Wm = np.concatenate(
            [Kcomp_dom[kk],
             np.broadcast_to(Brest_arr, (Ns, len(Brest_arr))),
             Odom], axis=1)                             # (Ns, nW)
        Sp = c.P32[Ocomp[oo]]                           # (Ns, tl-om)
        prodW = np.ones_like(Sp)
        for w in range(nW):
            prodW = prodW * c.DIFF[Sp, Wm[:, w:w + 1]] % p
        num = U[Sp] * c.xs32[Sp] % p * prodW % p
        prodWy = np.ones_like(Wm)
        for w in range(nW):
            d = c.DIFF[Wm, Wm[:, w:w + 1]].copy()
            d[:, w] = 1
            prodWy = prodWy * d % p
        lhs = U[Wm] * c.xs32[Wm] % p * prodWy % p
        rhs = np.zeros_like(Wm)
        for j in range(Sp.shape[1]):
            rhs = (rhs + num[:, j:j + 1] * c.DINV[Wm, Sp[:, j:j + 1]]) % p
        ok = np.all(((lhs - rhs) % p) != 0, axis=1)
        kept += int(ok.sum())
    return kept


def consec(t, p):
    return [(i + 1) % p for i in range(t)]


def geom5(t, p):
    out, g = [], 1
    for _ in range(t):
        out.append(g)
        g = g * 5 % p
    return out
