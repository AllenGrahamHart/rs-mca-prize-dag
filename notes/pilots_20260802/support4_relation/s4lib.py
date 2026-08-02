#!/usr/bin/env python3
"""s4lib -- the SUPPORT-4 RELATION engine (the band lane's last heart).

THE OBJECT.  A ray system is a list of pairs (z_a, S_a), a = 1..V, with
z_a in P^1(F_q) pairwise distinct and S_a a subset of the domain of size
A = k+h.  Its condition row space is

    Row  =  sum_a G_{z_a}(C_{S_a}),      G_z(W) = {(c, zc) : c in W},

where C_S = {c : supp(c) in S, c _|_ RS_k} (dim |S|-k = h).  By the banked
per-RAY cost theorem (adv_sublinear_rank T1) rank(Row) = Vh - dim Rel with

    Rel  =  {(c_a) in (+)_a C_{S_a} : sum_a c_a = 0, sum_a z_a c_a = 0}
         =  {(c_a) : sum_a e(z_a) (x) c_a = 0},      e(z) := (1, z) in F^2.

Support <= 2 and support 3 relations are PROVED zero (banked).  This file
attacks support 4 and above.

THE STRUCTURE THEOREMS PROVED HERE (see stage1_structure.py for the checks):

  S4-1 (localization)  supp(c_a) is contained in the set of points lying in
        S_a AND in at least two of the other supports of the relation.
        [group {a,b} against the rest, for every b != a.]
  S4-2 (general position kills)  hence c_a = 0 whenever
        |T_abc u T_abd u T_acd| <= k  (T = triple intersection), because a
        nonzero dual word has weight >= k+1.
  S4-3 (rank-2 rigidity)  for support exactly 4 all four c_a lie in ONE
        2-dimensional L <= C^perp, and no two are proportional -- if two
        were, all four would be, forcing |S_1^S_2^S_3^S_4| >= k+1 and
        breaking k-packing.
  S4-4 (Mobius / cross-ratio criterion)  with zeta_a := [c_a] in P(L) = P^1,
        a support-4 relation exists iff the four points ([1:z_a], zeta_a) of
        P^1 x P^1 lie on a (1,1)-divisor, i.e. iff
              CR(z_1,z_2,z_3,z_4) = CR(zeta_1,zeta_2,zeta_3,zeta_4).
        The relation is then unique up to scalar.
  S4-5 (pencil picture)  U := supp of a generic element of L satisfies
        |U| >= k+2; L = lambda^U . <pencil of polys of degree <= |U|-k-1>;
        zeta_a is the pencil parameter of c_a.
  S4-6 (minimal case |U| = k+2)  L = C_U, the weight-(k+1) words of C_U are
        exactly e_y = lambda^U (x - x_y)|_U for y in U, zeta_y = x_y, and the
        criterion reads  CR(z_1..z_4) = CR(x_{y_1}..x_{y_4}).

Run everything under tools/ramguard.  Exact arithmetic over a prime field.
Imports of other pilots are READ-ONLY.
"""
from __future__ import annotations

import os
import sys

sys.dont_write_bytecode = True

_ROOT = "/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260802"
for _p in (os.path.join(_ROOT, "xr_occupancy_v2"),
           os.path.join(_ROOT, "xr_band_occupancy"),
           os.path.join(_ROOT, "adv_sublinear_rank")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import tslib as T                                              # noqa: E402
import occlib                                                  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
INF = T.INF


# --------------------------------------------------------------- helpers
def inv(a, q):
    return pow(a % q, q - 2, q)


def det_mod(M, q):
    """Determinant of a square matrix mod prime q (fraction-free-ish)."""
    M = [[x % q for x in r] for r in M]
    nn = len(M)
    det = 1
    for c in range(nn):
        piv = None
        for r in range(c, nn):
            if M[r][c]:
                piv = r
                break
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = (-det) % q
        det = det * M[c][c] % q
        ic = inv(M[c][c], q)
        M[c] = [x * ic % q for x in M[c]]
        for r in range(c + 1, nn):
            f = M[r][c]
            if f:
                M[r] = [(M[r][j] - f * M[c][j]) % q for j in range(nn)]
    return det % q


def cross_ratio(a, b, c, d, q):
    """CR = ((a-c)(b-d)) / ((a-d)(b-c)); entries in F_q (no 'inf' here)."""
    num = (a - c) * (b - d) % q
    den = (a - d) * (b - c) % q
    if den == 0:
        return None
    return num * inv(den, q) % q


def segre_matrix(zs, ws, q):
    """rows indexed by (1(x)1, 1(x)x, z(x)1, z(x)x); column a is
    e(z_a) (x) (x - w_a)  =  (-w_a, 1, -z_a w_a, z_a)."""
    return [[(-w) % q for w in ws],
            [1] * len(zs),
            [(-z * w) % q for z, w in zip(zs, ws)],
            [z % q for z in zs]]


def mobius_curve_through(pts, q):
    """(1,1)-curve alpha + beta z + gamma w + delta z w = 0 through the given
    (z,w) points.  Returns a basis of the coefficient nullspace."""
    rows = [[1, z % q, w % q, z * w % q] for z, w in pts]
    return T.nullspace_mod(rows, 4, q)


def mobius_image(coef, w, q):
    """z with alpha + beta z + gamma w + delta z w = 0 for given w."""
    al, be, ga, de = [x % q for x in coef]
    num = (-(al + ga * w)) % q
    den = (be + de * w) % q
    if den == 0:
        return None
    return num * inv(den, q) % q


# ------------------------------------------------------- relation spaces
def ray_columns(row, supports, slopes):
    q, n = row.q, row.n
    blocks = [T.dual_basis(tuple(sorted(S)), row) for S in supports]
    cols = []
    for a, B in enumerate(blocks):
        z = slopes[a]
        for c in B:
            if z == INF:
                cols.append([0] * n + [x % q for x in c])
            else:
                cols.append([x % q for x in c] + [z * x % q for x in c])
    return blocks, cols


def relation_space(row, supports, slopes):
    """Return (dim, relations, blocks).  Each relation is the list of the V
    vectors c_a in F_q^n."""
    q, n = row.q, row.n
    blocks, cols = ray_columns(row, supports, slopes)
    widths = [len(b) for b in blocks]
    tot = sum(widths)
    if tot == 0:
        return 0, [], blocks
    Mrows = [[cols[j][i] for j in range(tot)] for i in range(2 * n)]
    ker = T.nullspace_mod(Mrows, tot, q)
    rels = []
    for kv in ker:
        cs, off = [], 0
        for a, B in enumerate(blocks):
            c = [0] * n
            for j in range(widths[a]):
                t = kv[off + j]
                if t:
                    Bj = B[j]
                    for i in range(n):
                        if Bj[i]:
                            c[i] = (c[i] + t * Bj[i]) % q
            off += widths[a]
            cs.append(c)
        rels.append(cs)
    return len(ker), rels, blocks


def family_rank(row, supports, slopes):
    _, cols = ray_columns(row, supports, slopes)
    return T.rank_mod(cols, row.q)


def support_of(c):
    return frozenset(i for i, x in enumerate(c) if x)


def multiplicity(supports, n):
    m = [0] * n
    for S in supports:
        for i in S:
            m[i] += 1
    return m


def triple_locus(supports, n):
    m = multiplicity(supports, n)
    return frozenset(i for i in range(n) if m[i] >= 3)


# ------------------------------------------------------------- builders
def build_mobius_family(row, d, V, seed=0, extra_free=0, mob=None):
    """The U-mechanism family.

    U = {0..k+1} (size k+2, so dim C_U = 2);  y_a = U[a] for a = 0..V-1;
    S_a = (U \\ {y_a}) u (pair blocks B_ab, |B_ab| = d) u (private block).
    |S_a| = k+h,  |S_a^S_b| = k+d,  |S_a^S_b^S_c| = k-1 (k-packing TIGHT),
    slopes z_a = nu(x_{y_a}) for a fixed nu in PGL_2  ==>  every 4-subset of
    the rays is Mobius-matched and carries a support-4 relation.

    Returns dict(supports, slopes, U, ys, blocks, n_used) or None.
    """
    import random
    rnd = random.Random(seed)
    k, h, q, n = row.k, row.h, row.q, row.n
    if V < 3 or V > k + 2:
        return None
    if d < 1 or d > h - 2:
        return None
    priv = (h - 1) - (V - 1) * d
    if priv < 0:
        return None
    need = (k + 2) + (V * (V - 1) // 2) * d + V * priv + extra_free
    if need > n:
        return None
    U = list(range(k + 2))
    ys = U[:V]
    cur = k + 2
    B = {}
    for a in range(V):
        for b in range(a + 1, V):
            B[(a, b)] = list(range(cur, cur + d))
            cur += d
    P = {}
    for a in range(V):
        P[a] = list(range(cur, cur + priv))
        cur += priv
    supports = []
    for a in range(V):
        S = set(U) - {ys[a]}
        for b in range(V):
            if b == a:
                continue
            S |= set(B[(min(a, b), max(a, b))])
        S |= set(P[a])
        supports.append(tuple(sorted(S)))
        assert len(S) == k + h, (len(S), k + h)
    ws = [row.xs[y] for y in ys]
    for _ in range(400):
        if mob is None:
            p, r, s, t = (rnd.randrange(q), rnd.randrange(q),
                          rnd.randrange(q), rnd.randrange(q))
        else:
            p, r, s, t = mob
        if (p * t - r * s) % q == 0:
            continue
        zs, ok = [], True
        for w in ws:
            den = (s * w + t) % q
            if den == 0:
                ok = False
                break
            zs.append((p * w + r) % q * inv(den, q) % q)
        if not ok or len(set(zs)) != V or 0 in zs:
            if mob is not None:
                return None
            continue
        return dict(supports=supports, slopes=zs, U=U, ys=ys,
                    pair_blocks={str(kk): vv for kk, vv in B.items()},
                    priv={str(a): P[a] for a in P}, n_used=cur,
                    mobius=(p, r, s, t), ws=ws, d=d, V=V)
    return None


def realise_family(row, supports, slopes, seed=0, tries=400):
    """Solve the linear system for (u,v) realising the ray system."""
    _, cols = ray_columns(row, supports, slopes)
    return T.realise(row, cols, seed=seed, tries=tries)


def gate_report(row, u, v, name=""):
    rec, pairs, band = occlib.measure(row, u, v, name=name, want_checks=True)
    rec["FULL_GATE"] = bool(rec["below_cascade"] and rec["globally_generic"]
                            and rec["tangent_free_finite_slopes"]
                            and rec["tangent_free_v_direction"]
                            and rec["v_nonvanishing"] and rec["kpacking_ok"])
    return rec, pairs, band


def combinatorial_gates(row, supports):
    """Gates that depend on the support pattern alone."""
    k, h = row.k, row.h
    V = len(supports)
    Ss = [set(S) for S in supports]
    pair = {}
    for a in range(V):
        for b in range(a + 1, V):
            pair[(a, b)] = len(Ss[a] & Ss[b])
    trip = {}
    for a in range(V):
        for b in range(a + 1, V):
            for c in range(b + 1, V):
                trip[(a, b, c)] = len(Ss[a] & Ss[b] & Ss[c])
    return dict(
        sizes=[len(S) for S in Ss],
        size_ok=all(len(S) == k + h for S in Ss),
        pair=pair, triple=trip,
        pairwise_intersecting=all(x >= k + 1 for x in pair.values()),
        depth_ok=all(x <= k + h - 2 for x in pair.values()),
        kpacking_ok=all(x <= k - 1 for x in trip.values()),
        max_pair=max(pair.values(), default=0),
        max_triple=max(trip.values(), default=0),
    )
