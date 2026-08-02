#!/usr/bin/env python3
r"""dzlib -- the d = 0 (EXACT-K) stratum engine for P-A1.

THE OBJECT.  RS_k on domain D, |D| = n; A = k + h the selected-support size.
A live ray is (z, S) with |S| = A and agr(u + z v, codeword) = A.  P-A1
counts DISTINCT live slopes z whose selected support S_z meets another live
support in >= k points.  The d >= 1 band was settled by xr_occupancy_v2 /
adv_sublinear_rank; this file is the d = 0 base stratum: pairs of live rays
with |S ^ S'| EXACTLY k.

WHY d = 0 IS DIFFERENT.  The core condition space C_Z = {c : supp c in Z,
c _|_ RS_k} has dim |Z| - k = 0.  So (i) the core imposes NO equations --
every k-set is the joint-agreement core of a unique codeword pair
(P_W, Q_W) = (interp u|_W, interp v|_W), so there are C(n,k) candidate cores
with no arithmetic filter; and (ii) the exclusivity that protects the
cascade tier fails: |Z ^ Z'| >= 2k - A = k - h is far below k, so one live
support of size A carries C(A,k) k-subsets and can serve many pairs.

THE RANK MODULE (the engine).  For a family of live rays (z_a, S_a),
    Phi : (+)_a C_{S_a} -> F_q^n x F_q^n,   (c_a) |-> (sum c_a, sum z_a c_a).
rank(family) = dim im Phi = V h - nullity.  The LOCATOR NORMAL FORM
    C_S = { nu . (Lam_{D\S} . r) : deg r < h },  nu_i = 1/prod_{j!=i}(x_i-x_j)
turns a relation into a pair of polynomial syzygies
    sum_a m_a r_a = 0,   sum_a z_a m_a r_a = 0,   m_a := Lam_{D\S_a},
with deg m_a = n - A = R - h and deg r_a < h.  This is exactly the F5-OS
live-syzygy object (a_{S_i}, z_i a_{S_i}); L3a covering rigidity is its
pointwise shadow.

Read-only imports of the banked engines.  Exact arithmetic.  ramguard only.
"""
from __future__ import annotations

import itertools
import os
import random
import sys

sys.dont_write_bytecode = True

_V2 = ("/home/u2470931/smooth-read-solomin/prize/notes/"
       "pilots_20260802/xr_occupancy_v2")
_BO = ("/home/u2470931/smooth-read-solomin/prize/notes/"
       "pilots_20260802/xr_band_occupancy")
_GB = ("/home/u2470931/smooth-read-solomin/prize/notes/"
       "pilots_20260802/xr_graded_band_ledger")
for _p in (_V2, _BO, _GB):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import tslib as T                                              # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

INF = T.INF

# ------------------------------------------------------------- six rows
ROWS = []
for _name, _n, _rate, _scale in [("RowC 1/4", 1024, 4, 256),
                                 ("RowC 1/8", 1024, 8, 256),
                                 ("RowC 1/16", 1024, 16, 512),
                                 ("prize 1/4", 2 ** 41, 4, 256),
                                 ("prize 1/8", 2 ** 41, 8, 256),
                                 ("prize 1/16", 2 ** 41, 16, 512)]:
    _k = _n // _rate
    _A = _k + _n // _scale + 1
    ROWS.append(dict(name=_name, n=_n, k=_k, A=_A, h=_A - _k,
                     R=_n - _k, r=_n - _A))
BANKED_A = [261, 133, 67, 558345748481, 283467841537, 141733920769]
assert [r["A"] for r in ROWS] == BANKED_A


# --------------------------------------------------------- polynomials
def polymul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        if ca:
            for j, cb in enumerate(b):
                if cb:
                    out[i + j] = (out[i + j] + ca * cb) % q
    return out


def locator(row, T_pts):
    """coefficients of prod_{i in T}(X - x_i)."""
    P = [1]
    for i in T_pts:
        P = polymul(P, [(-row.xs[i]) % row.q, 1], row.q)
    return P


def dual_from_locator(row, S, r):
    """nu_i * Lam_{D\\S}(x_i) * r(x_i), i in D.  Should equal an element of
    C_S (zero off S automatically since Lam_{D\\S} kills D\\S)."""
    q, n = row.q, row.n
    comp = [i for i in range(n) if i not in set(S)]
    m = locator(row, comp)
    out = []
    for i in range(n):
        nu = 1
        for j in range(n):
            if j != i:
                nu = nu * (row.xs[i] - row.xs[j]) % q
        nu = pow(nu, q - 2, q)
        out.append(nu * T.poly_ev(m, row.xs[i], q) % q
                   * T.poly_ev(r, row.xs[i], q) % q)
    return out


# ------------------------------------------------------------ rank core
def ray_block(row, S, z):
    return T.ray_rows(row, S, z)


def family_rank(row, rays):
    """rays: list of (z, S).  Returns (rank, V*h)."""
    rows = []
    for z, S in rays:
        rows += ray_block(row, S, z)
    return T.rank_mod(rows, row.q), len(rays) * row.h


def relation_space(row, rays):
    """Basis of {(c_a) in (+) C_{S_a} : sum c_a = 0, sum z_a c_a = 0},
    expressed in the concatenated dual-basis coordinates (V*h coords)."""
    q, n = row.q, row.n
    blocks = [T.dual_basis(S, row) for z, S in rays]
    ncol = sum(len(b) for b in blocks)
    M = [[0] * ncol for _ in range(2 * n)]
    col = 0
    for (z, S), B in zip(rays, blocks):
        for c in B:
            for i in range(n):
                M[i][col] = c[i] % q
                if z == INF:
                    M[n + i][col] = 0
                else:
                    M[n + i][col] = z * c[i] % q
            if z == INF:
                for i in range(n):
                    M[i][col] = 0
                    M[n + i][col] = c[i] % q
            col += 1
    return T.nullspace_mod(M, ncol, q), ncol


def datum_rank_d0(row, Z, S1, z1, S2, z2):
    """rank of a d=0 two-slope datum.  Core rows are EMPTY (dim C_Z = 0)."""
    assert len(Z) == row.k
    assert set(S1) & set(S2) == set(Z)
    rows = T.core_rows(row, Z) + T.ray_rows(row, S1, z1) + \
        T.ray_rows(row, S2, z2)
    return T.rank_mod(rows, row.q), len(T.core_rows(row, Z))


# -------------------------------------------------------------- builders
def sunflower0(row, m, start=0):
    """d = 0 sunflower: common (k-1)-set Y, m petals of ONE point each,
    m cycle edges each with a top-up block of h-1 points.
    Ray a = the forced slope of edge a = (a, a+1); its support is
    Y u {p_a, p_{a+1}} u B_a, size (k-1)+2+(h-1) = k+h = A.  Two rays
    adjacent in the cycle meet in Y u {shared petal} = k points -> d = 0.
    Point budget (k-1) + m + m(h-1) = (k-1) + m h <= n."""
    k, h, n = row.k, row.h, row.n
    need = (k - 1) + m * h
    if need > n:
        return None
    pts = [(start + i) % n for i in range(n)]
    Y = pts[:k - 1]
    cur = k - 1
    petal = []
    for _ in range(m):
        petal.append(pts[cur])
        cur += 1
    edges = []
    for a in range(m):
        b = (a + 1) % m
        B = pts[cur:cur + h - 1]
        cur += h - 1
        edges.append((a, b, tuple(B)))
    return Y, petal, edges, cur


def kv0(row, V, rng, tries=4000):
    """d = 0 K_V: V lines in general position in the (alpha,beta) plane,
    data at the C(V,2) intersection points; petal of a datum = ONE point.
    Ray a = line a: support Y u {petals of the V-1 data on line a} u topup_a,
    |topup_a| = h + 1 - (V - 1)  ->  needs V <= h + 2.
    Two rays meet in Y u {their common datum's petal} = k points."""
    k, h, n = row.k, row.h, row.n
    if V - 1 > h + 1:
        return None
    top = h + 1 - (V - 1)
    need = (k - 1) + (V * (V - 1)) // 2 + V * top
    if need > n:
        return None
    lg = T.__dict__.get("lines_general_position")
    if lg is None:
        import advlib_stub  # pragma: no cover
    pts = [i % n for i in range(n)]
    Y = pts[:k - 1]
    cur = k - 1
    petal = {}
    for a in range(V):
        for b in range(a + 1, V):
            petal[(a, b)] = pts[cur]
            cur += 1
    tops = []
    for a in range(V):
        tops.append(tuple(pts[cur:cur + top]))
        cur += top
    return Y, petal, tops, cur


def kv0_rays(row, V, zs, Y, petal, tops):
    rays = []
    for a in range(V):
        S = set(Y) | set(tops[a])
        for b in range(V):
            if b == a:
                continue
            S.add(petal[(min(a, b), max(a, b))])
        S = tuple(sorted(S))
        assert len(S) == row.A, (len(S), row.A)
        rays.append((zs[a], S))
    return rays


def sunflower0_rays(row, Y, petal, edges, zs):
    rays = []
    for idx, (a, b, B) in enumerate(edges):
        S = tuple(sorted(set(Y) | {petal[a], petal[b]} | set(B)))
        assert len(S) == row.A, (len(S), row.A)
        rays.append((zs[idx], S))
    return rays


# --------------------------------------------------------- pair measures
def pair_stats(rays):
    """Return (#exact-k pairs, #pairs by |S ^ S'|)."""
    from collections import Counter
    cnt = Counter()
    for a in range(len(rays)):
        for b in range(a + 1, len(rays)):
            cnt[len(set(rays[a][1]) & set(rays[b][1]))] += 1
    return cnt


def kpacked(rays, k):
    return all(len(set(rays[a][1]) & set(rays[b][1])) <= k
               for a in range(len(rays)) for b in range(a + 1, len(rays)))


def rand_slopes(q, V, rng):
    return rng.sample(range(1, q), V)


def make_row(n, k, h, q, xs=None):
    return T.Row2(n, k, h, q, xs=xs)
