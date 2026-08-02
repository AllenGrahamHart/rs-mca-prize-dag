#!/usr/bin/env python3
"""tslib -- the TWO-SLOPE condition/rank engine for the band occupancy lemma.

Setting.  RS code C = RS_k on a domain X = (x_1..x_n) in F_q, A = k+h the
selected support size, band depths d in [1, h-2].  A received pair is
(u,v) in F_q^n x F_q^n.  A band pair P = (f,g) in C x C has joint agreement
Z_P = {i : f(x_i)=u_i and g(x_i)=v_i} of size k+d.  A live slope for P is
z in P^1(F_q) with agr(u+zv, f+zg) >= A; its support S_z contains Z_P.

The conditions imposed on (u,v) by a two-live-slope datum

        (Z ; z_1, S_1 ; z_2, S_2),    |Z| = k+d, |S_j| = A, S_1 ^ S_2 = Z

are LINEAR in (u,v) once the slopes are prescribed:

  (C0)  <c,u> = <c,v> = 0    for all c in C_Z          [P exists on core Z]
  (Cj)  <c,u> + z_j <c,v> = 0 for all c in C_{S_j}     [ray j is live]

where C_S = {c : supp(c) in S, c _|_ RS_k} has dim |S|-k (MDS shortening;
this is lemma L1 of the pb_h4_hunt pilot).  Row space

  R(P) = (C_Z x C_Z) + {(c, z_1 c)} + {(c, z_2 c)}   inside C^perp x C^perp.

THEOREM A (this pilot): dim R(P) = 2h exactly, for EVERY admissible datum,
independent of the depth d.  With the two slopes free the locus has
codimension 2h-2.  Since RS_k x RS_k lies in every kernel, a family is
realisable by a NON-degenerate received pair only if its total rank is
<= 2(n-k)-1.

Everything is exact arithmetic over a prime field.  Run under tools/ramguard.
"""
from __future__ import annotations

import itertools
import sys

sys.dont_write_bytecode = True


# ------------------------------------------------------------------ field
def is_prime(m):
    if m < 2:
        return False
    if m % 2 == 0:
        return m == 2
    d = 3
    while d * d <= m:
        if m % d == 0:
            return False
        d += 2
    return True


def primitive_root(q):
    m = q - 1
    fac, t, d = [], q - 1, 2
    while d * d <= t:
        if t % d == 0:
            fac.append(d)
            while t % d == 0:
                t //= d
        d += 1
    if t > 1:
        fac.append(t)
    for g in range(2, q):
        if all(pow(g, m // p, q) != 1 for p in fac):
            return g
    raise RuntimeError("no primitive root")


def primes_with(nn, lo=3, hi=200000, count=8, cond=None):
    out, q = [], lo
    while len(out) < count and q < hi:
        q += 1
        if not is_prime(q):
            continue
        if cond is not None and not cond(q):
            continue
        out.append(q)
    return out


# ------------------------------------------------------------------- row
class Row2:
    """Duck-compatible with xr_graded_band_ledger.bandlib.Row, but the
    evaluation domain may be prescribed (needed for multiplicative-coset
    domains: the MC calibration adversary)."""

    def __init__(self, n, k, t, q, xs=None):
        self.n, self.k, self.t, self.q = n, k, t, q
        self.A = k + t
        self.h = t
        self.R = n - k
        self.r = n - self.A
        if xs is None:
            xs = [(i + 1) % q for i in range(n)]
        self.xs = list(xs)
        assert len(set(self.xs)) == n, "domain must be distinct"
        self.INV = [0] * q
        for a in range(1, q):
            self.INV[a] = pow(a, q - 2, q)
        self.DIFF = [[(self.xs[i] - self.xs[m]) % q for m in range(n)]
                     for i in range(n)]
        self.INVDIFF = [[self.INV[self.DIFF[i][m]] if i != m else 0
                         for m in range(n)] for i in range(n)]

    def interp(self, W, vals):
        q, k = self.q, self.k
        coeff = [0] * k
        for idx, j in enumerate(W):
            num, den = [1], 1
            for m in W:
                if m == j:
                    continue
                new = [0] * (len(num) + 1)
                for e, ce in enumerate(num):
                    if ce:
                        new[e] = (new[e] - ce * self.xs[m]) % q
                        new[e + 1] = (new[e + 1] + ce) % q
                num = new
                den = den * self.DIFF[j][m] % q
            w = vals[idx] * self.INV[den] % q
            for e in range(len(num)):
                coeff[e] = (coeff[e] + w * num[e]) % q
        return tuple(coeff)

    def ev(self, c, x):
        q, acc = self.q, 0
        for co in reversed(c):
            acc = (acc * x + co) % q
        return acc


def poly_ev(coeffs, x, q):
    acc = 0
    for c in reversed(coeffs):
        acc = (acc * x + c) % q
    return acc


def mult_domain(q, n, x0exp=0):
    """H = x0 * mu_n inside F_q^*  (requires n | q-1)."""
    assert (q - 1) % n == 0
    g = primitive_root(q)
    om = pow(g, (q - 1) // n, q)
    x0 = pow(g, x0exp, q)
    return [x0 * pow(om, i, q) % q for i in range(n)], om


# ------------------------------------------------------- shortened duals
def lam(S, xs, q):
    out = []
    for i in S:
        p = 1
        for j in S:
            if j != i:
                p = p * (xs[i] - xs[j]) % q
        out.append(pow(p, q - 2, q))
    return out


def dual_basis(S, row):
    """Basis of C_S = {c : supp(c) in S, c _|_ RS_k}; dim = |S|-k.

    c^(t)_i = lam^S_i * x_i^t for i in S, t = 0 .. |S|-k-1.
    (sum_{i in S} lam_i x_i^e = 0 for e <= |S|-2, so orthogonality to
    X^0..X^{k-1} holds exactly when t+k-1 <= |S|-2.)
    """
    q, n, k = row.q, row.n, row.k
    S = tuple(sorted(S))
    m = len(S)
    assert m >= k, (m, k)
    L = lam(S, row.xs, q)
    rows = []
    for t in range(m - k):
        c = [0] * n
        for e, i in enumerate(S):
            c[i] = L[e] * pow(row.xs[i], t, q) % q
        rows.append(c)
    return rows


# ------------------------------------------------------- linear algebra
def rref(rows, q):
    rows = [list(r) for r in rows]
    if not rows:
        return [], []
    ncol = len(rows[0])
    piv, pivcol = 0, []
    for col in range(ncol):
        sel = None
        for i in range(piv, len(rows)):
            if rows[i][col] % q:
                sel = i
                break
        if sel is None:
            continue
        rows[piv], rows[sel] = rows[sel], rows[piv]
        inv = pow(rows[piv][col], q - 2, q)
        rows[piv] = [x * inv % q for x in rows[piv]]
        for i in range(len(rows)):
            if i != piv and rows[i][col] % q:
                f = rows[i][col]
                rows[i] = [(rows[i][c] - f * rows[piv][c]) % q
                           for c in range(ncol)]
        pivcol.append(col)
        piv += 1
        if piv == len(rows):
            break
    return rows[:piv], pivcol


def rank_mod(rows, q):
    r, _ = rref(rows, q)
    return len(r)


def nullspace_mod(rows, ncol, q):
    if not rows:
        return [[1 if i == j else 0 for i in range(ncol)] for j in range(ncol)]
    red, pivcol = rref(rows, q)
    free = [c for c in range(ncol) if c not in pivcol]
    basis = []
    for fc in free:
        vv = [0] * ncol
        vv[fc] = 1
        for r, pc in enumerate(pivcol):
            vv[pc] = (-red[r][fc]) % q
        basis.append(vv)
    return basis


# --------------------------------------------------- the two-slope datum
INF = "inf"


def ray_rows(row, S, z):
    """rows {(c, z c) : c in C_S} in F_q^{2n};  z = 'inf' means (0,c)."""
    n = row.n
    out = []
    for c in dual_basis(S, row):
        if z == INF:
            out.append([0] * n + list(c))
        else:
            out.append(list(c) + [z * x % row.q for x in c])
    return out


def core_rows(row, Z):
    """rows (c,0) and (0,c) for c in C_Z."""
    n = row.n
    out = []
    for c in dual_basis(Z, row):
        out.append(list(c) + [0] * n)
        out.append([0] * n + list(c))
    return out


def datum_rows(row, Z, S1, z1, S2, z2):
    return core_rows(row, Z) + ray_rows(row, S1, z1) + ray_rows(row, S2, z2)


def family_rows(row, fam):
    """fam: list of (Z, [(z,S), (z,S), ...]) -- >= 2 rays each."""
    rows = []
    for Z, rays in fam:
        rows += core_rows(row, Z)
        for z, S in rays:
            rows += ray_rows(row, S, z)
    return rows


def realise(row, rows, seed=0, tries=200, require_v_nonzero=True):
    """Draw a solution (u,v) of the linear system that is NOT in C x C.

    Returns (u, v) or None.
    """
    import random
    rnd = random.Random(seed)
    q, n, k = row.q, row.n, row.k
    ns = nullspace_mod(rows, 2 * n, q)
    if not ns:
        return None
    for _ in range(tries):
        w = [0] * (2 * n)
        for b in ns:
            cf = rnd.randrange(q)
            if cf:
                for i in range(2 * n):
                    w[i] = (w[i] + cf * b[i]) % q
        u, v = w[:n], w[n:]
        if require_v_nonzero and any(x == 0 for x in v):
            continue
        if is_codeword(row, u) and is_codeword(row, v):
            continue
        return u, v
    return None


def is_codeword(row, w):
    k, n = row.k, row.n
    if n <= k:
        return True
    f = row.interp(tuple(range(k)), w[:k])
    return all(row.ev(f, row.xs[i]) == w[i] for i in range(n))


# -------------------------------------------------------------- builders
def sunflower(row, d, m, start=0):
    """Generalised sunflower at depth d: m cores through a common (k-1)-set,
    petals of size d+1, plus (for d < (h-1)/2) a top-up block of size
    h-2d-1 for each edge of the m-cycle so that the FORCED ray of the edge
    reaches agreement exactly A.

    Returns (cores, edges, used) with edges = [(i,j,topup_block)].
    Point budget: (k-1) + m(d+1) + m(h-2d-1) = (k-1) + m(h-d) <= n.
    """
    k, h, n = row.k, row.h, row.n
    assert 2 * d + 1 <= h, "sunflower mechanism needs 2d+1 <= h"
    need = (k - 1) + m * (h - d)
    if need > n:
        return None
    pts = list(range(start, start + n))
    Y = [p % n for p in pts[:k - 1]]
    cur = k - 1
    cores, petals = [], []
    for i in range(m):
        P = [p % n for p in pts[cur:cur + d + 1]]
        cur += d + 1
        petals.append(P)
        cores.append(tuple(sorted(Y + P)))
    edges = []
    tw = h - 2 * d - 1
    for i in range(m):
        j = (i + 1) % m
        B = [p % n for p in pts[cur:cur + tw]]
        cur += tw
        edges.append((i, j, tuple(sorted(B))))
    return cores, edges, cur


def spread_two_slope_family(row, d, M, rng, tries=400000):
    """Random DESIGNED family: M depth-d two-slope data whose 2M supports
    pairwise meet in <= k points across distinct members (k-spread)."""
    n, k, h, A = row.n, row.k, row.h, row.A
    fam, supp = [], []
    for _ in range(tries):
        pool = rng.sample(range(n), k + d + 2 * (h - d))
        Z = tuple(sorted(pool[:k + d]))
        B1 = tuple(sorted(pool[k + d:k + d + h - d]))
        B2 = tuple(sorted(pool[k + d + h - d:]))
        S1 = tuple(sorted(set(Z) | set(B1)))
        S2 = tuple(sorted(set(Z) | set(B2)))
        ok = True
        for T in supp:
            if len(set(S1) & set(T)) > k or len(set(S2) & set(T)) > k:
                ok = False
                break
        if not ok:
            continue
        z1 = rng.randrange(1, row.q)
        z2 = rng.randrange(1, row.q)
        while z2 == z1:
            z2 = rng.randrange(1, row.q)
        fam.append((Z, [(z1, S1), (z2, S2)]))
        supp += [S1, S2]
        if len(fam) == M:
            return fam
    return fam
