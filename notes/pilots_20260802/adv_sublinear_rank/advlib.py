#!/usr/bin/env python3
"""advlib -- adversarial constructions against the two-slope occupancy lemma.

THE TARGET.  xr_occupancy_v2 proved: a depth-d two-slope datum costs exactly
2h condition-rank (THEOREM 1); the sunflower is the unique deficit family and
costs exactly h per datum; the occupancy lemma is closed modulo the named
class "a family whose condition rank grows sublinearly in M".

THE REFORMULATION THIS FILE ATTACKS.  For a family of two-slope data the row
space is

    V  =  sum_i (C_{Z_i} x C_{Z_i})  +  sum_e G_{z_e}(C_{S_e}),
    G_z(W) := {(c, z c) : c in W}.

Because S_a ^ S_b = Z_ab (banked T2) and L1 gives C_{S_a} ^ C_{S_b} = C_{Z_ab},
the CORE rows are already inside the RAY span:  (c, z_a c) - (c, z_b c) =
(0, (z_a - z_b) c).  Hence

    rank(family)  =  dim sum_{a=1..V} G_{z_a}(C_{S_a})   <=  V h,

i.e. **the charge is h per RAY, not per datum**.  A datum is a PAIR of rays
(its core is S_a ^ S_b, which the pair of rays determines), so

    M  <=  C(V, 2).

The sunflower is the CYCLE configuration (V rays, M = V data, cost h).  The
COMPLETE-GRAPH configuration (V rays, M = C(V,2) data) costs 2h/(V-1) and is
what this file builds.

K_V BUILDER (the "dual sunflower").  Y a common (k-1)-set, V_Y its vanishing
polynomial.  Band pairs are indexed by points (alpha,beta) of F_q^2 via
(f + alpha V_Y, g + beta V_Y).  A slope z is live for such a pair with
support Y u (petals of all data on the line {alpha + z beta = c}).  The
sunflower puts the M points in GENERAL POSITION (no 3 collinear) and uses the
C(M,2)... no, m of the lines.  We instead take V LINES in general position and
put the data at their C(V,2) intersection points: each line then carries
V-1 data, each datum lies on exactly 2 lines, and every pair of lines meets in
exactly one datum.

Run under tools/ramguard.  Exact arithmetic.  Imports are read-only.
"""
from __future__ import annotations

import os
import random
import sys

sys.dont_write_bytecode = True

_V2 = ("/home/u2470931/smooth-read-solomin/prize/notes/"
       "pilots_20260802/xr_occupancy_v2")
_BO = ("/home/u2470931/smooth-read-solomin/prize/notes/"
       "pilots_20260802/xr_band_occupancy")
for _p in (_V2, _BO):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import tslib as T                                             # noqa: E402
import occlib                                                 # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- helpers
def vanish_poly(row, Y):
    """Coefficient tuple (length k) of prod_{i in Y}(X - x_i), |Y| = k-1."""
    q = row.q
    P = [1]
    for i in Y:
        new = [0] * (len(P) + 1)
        for e, c in enumerate(P):
            if c:
                new[e] = (new[e] - c * row.xs[i]) % q
                new[e + 1] = (new[e + 1] + c) % q
        P = new
    assert len(P) == len(Y) + 1 <= row.k, (len(P), row.k)
    return tuple((P + [0] * row.k)[:row.k])


def add_poly(a, b, q):
    return tuple((x + y) % q for x, y in zip(a, b))


def scal_poly(a, s, q):
    return tuple(x * s % q for x in a)


def lines_general_position(q, V, rng, tries=4000):
    """V lines  alpha + z_a beta = c_a  in AG(2,q), pairwise distinct slopes,
    no three concurrent.  Returns (zs, cs, pts) with
    pts[(a,b)] = (alpha, beta) the intersection of lines a and b."""
    for _ in range(tries):
        zs = rng.sample(range(q), V)
        cs = [rng.randrange(q) for _ in range(V)]
        pts, ok = {}, True
        for a in range(V):
            for b in range(a + 1, V):
                den = (zs[a] - zs[b]) % q
                beta = (cs[a] - cs[b]) * pow(den, q - 2, q) % q
                alpha = (cs[a] - zs[a] * beta) % q
                pts[(a, b)] = (alpha, beta)
        if len(set(pts.values())) != len(pts):
            continue
        # no three lines concurrent  <=>  all C(V,2) points distinct (above)
        # additionally: no point of the plane on 3 of our lines
        for a in range(V):
            on = [p for (i, j), p in pts.items() if i == a or j == a]
            if len(set(on)) != V - 1:
                ok = False
                break
        if ok:
            return zs, cs, pts
    return None


def extra_rich_lines(q, pts, V, zs):
    """Lines OTHER than the V designed ones that carry >= 3 of the data
    points.  Returns list of (z, c, count)."""
    items = sorted(pts.items())
    P = [p for _, p in items]
    des = set(zip(zs, [None] * V))
    seen = {}
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            (a1, b1), (a2, b2) = P[i], P[j]
            db = (b1 - b2) % q
            if db == 0:
                key = ("inf", a1 % q)      # beta = const line
            else:
                z = (-(a1 - a2)) * pow(db, q - 2, q) % q
                key = (z, (a1 + z * b1) % q)
            seen.setdefault(key, set()).update([i, j])
    out = []
    for (z, c), S in seen.items():
        if len(S) >= 3:
            out.append((z, c, len(S)))
    del des
    return out


# --------------------------------------------------------------- builder
def build_KV(row, d, V, seed=0, topup=True):
    """The K_V (complete-graph-of-rays) family.

    Y : common (k-1)-set.  M = C(V,2) data, petal P_ab of size d+1 each.
    Ray a : S_a = Y u (petals of the V-1 data on line a) u top-up B_a,
            |B_a| = h+1 - (V-1)(d+1)  (>= 0 required).
    |S_a| = k+h,  S_a ^ S_b = Y u P_ab = Z_ab  (size k+d).

    Returns (u, v, info) or None.
    """
    rnd = random.Random(seed)
    n, k, h, q = row.n, row.k, row.h, row.q
    if V < 3 or d < 1 or d > h - 2:
        return None
    tau = (h + 1) - (V - 1) * (d + 1)
    if tau < 0:
        return None
    if not topup and tau != 0:
        return None
    M = V * (V - 1) // 2
    need = (k - 1) + M * (d + 1) + V * tau
    if need > n:
        return None

    pts_all = list(range(n))
    Y = pts_all[:k - 1]
    cur = k - 1
    keys = [(a, b) for a in range(V) for b in range(a + 1, V)]
    petal = {}
    for key in keys:
        petal[key] = pts_all[cur:cur + d + 1]
        cur += d + 1
    block = {}
    for a in range(V):
        block[a] = pts_all[cur:cur + tau]
        cur += tau

    geo = lines_general_position(q, V, rnd)
    if geo is None:
        return None
    zs, cs, pts = geo

    f = tuple(rnd.randrange(q) for _ in range(k))
    g = tuple(rnd.randrange(q) for _ in range(k))
    VY = vanish_poly(row, Y)

    u = [None] * n
    v = [None] * n
    for i in Y:
        u[i] = row.ev(f, row.xs[i])
        v[i] = row.ev(g, row.xs[i])
    cores = {}
    for key in keys:
        al, be = pts[key]
        fab = add_poly(f, scal_poly(VY, al, q), q)
        gab = add_poly(g, scal_poly(VY, be, q), q)
        for i in petal[key]:
            u[i] = row.ev(fab, row.xs[i])
            v[i] = row.ev(gab, row.xs[i])
        cores[key] = tuple(sorted(Y + petal[key]))
    for a in range(V):
        za, ca = zs[a], cs[a]
        psi = add_poly(add_poly(f, scal_poly(g, za, q), q),
                       scal_poly(VY, ca, q), q)
        for x in block[a]:
            vx = rnd.randrange(1, q)
            u[x] = (row.ev(psi, row.xs[x]) - za * vx) % q
            v[x] = vx
    for i in range(n):
        if u[i] is None:
            u[i] = rnd.randrange(q)
            v[i] = rnd.randrange(1, q)

    supports = {}
    for a in range(V):
        S = set(Y) | set(block[a])
        for key in keys:
            if a in key:
                S |= set(petal[key])
        supports[a] = tuple(sorted(S))
    info = dict(Y=Y, petal={str(kk): vv for kk, vv in petal.items()},
                block=block, zs=zs, cs=cs, V=V, d=d, M=M, tau=tau,
                points_used=cur,
                cores={str(kk): vv for kk, vv in cores.items()},
                supports={str(a): supports[a] for a in supports},
                extra_rich=extra_rich_lines(q, pts, V, zs))
    return u, v, info


def designed_rank(row, info):
    """Exact rank of the DESIGNED family rows (cores + the V rays)."""
    q = row.q
    rows = []
    for a_s, S in info["supports"].items():
        rows += T.ray_rows(row, S, info["zs"][int(a_s)])
    for _, Z in info["cores"].items():
        rows += T.core_rows(row, Z)
    return T.rank_mod(rows, q)


def ray_only_rank(row, info):
    q = row.q
    rows = []
    for a_s, S in info["supports"].items():
        rows += T.ray_rows(row, S, info["zs"][int(a_s)])
    return T.rank_mod(rows, q)


def measured_family(row, band, d):
    """Extract the depth-d two-slope family (Z, [(z,S),(z,S)]) from a band."""
    fam = []
    for Zf, p, dd, sl in band:
        if dd == d and len(sl) >= 2:
            fam.append((tuple(sorted(Zf)),
                        [(z, tuple(sorted(p["supports"][z]))) for z in sl]))
    return fam


def family_rank_two_rays(row, fam):
    """rank of the family using only the FIRST TWO live slopes per datum
    (the two-slope datum as formalised in xr_occupancy_v2)."""
    f2 = [(Z, rays[:2]) for Z, rays in fam]
    return T.rank_mod(T.family_rows(row, f2), row.q)


def family_rank_all_rays(row, fam):
    return T.rank_mod(T.family_rows(row, fam), row.q)
