#!/usr/bin/env python3
"""pb_h4_hunt / core: exact primitives for the residual (H4) hunt.

FORMALIZATION (word model, matching critical/nodes/xr_lowcore_spread_heart,
"received pair (u,v)"):

  D = mu_n < F_q^*,  RS_K = {P(x) : deg P < K} evaluated on D,  A = K + h.
  S subset D, |S| = A is an exact-A witness of w at slope z iff
      (u + z v)|_S  in  RS_K|_S.
  Equivalently sigma_S(u) + z sigma_S(v) = 0 where the syndrome map is
      sigma_S(w)_t = sum_{i in S} lam^S_i x_i^t w_i,  t = 0..h-1,
      lam^S_i = prod_{j in S, j != i} (x_i - x_j)^{-1}.
  So S is a witness of the PAIR iff the 2 x h matrix [sigma_S(u); sigma_S(v)]
  has rank <= 1 -- exactly h-1 conditions -- and then z is the ratio.

DEGREE-A PENCIL MODEL (the model of the banked pilots): u = U|_D, v = V|_D
with U monic of degree A, deg V < A.  Then u + zv is monic of degree A and
the witness condition reads

      e_j(S) = alpha_j + z beta_j,   j = 1..h,          (STAR)
      alpha_j = (-1)^j U_{A-j},  beta_j = (-1)^j V_{A-j}.

i.e. the MOMENT VECTOR E(S) = (e_1(S),...,e_h(S)) in F_q^h must lie on the
affine line  L = {alpha + z beta}.  Only the top h coefficients of (U,V)
matter; everything of degree < K is invisible.  Hence:

  *** the entire design space of degree-A pencils IS the space of affine
      lines in AG(h,q) ***

and the planted family of a pencil is exactly E^{-1}(L).  By Newton, E is
equivalent to the power-sum map P(S) = sum_{x in S} (x, x^2, ..., x^h),
i.e. the subset-sum map of the moment curve: an ADDITIVE map.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

from itertools import combinations


# ---------------------------------------------------------------- field
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def prime_factors(x: int) -> list[int]:
    out, d = [], 2
    while d * d <= x:
        if x % d == 0:
            out.append(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        out.append(x)
    return out


def primitive_root(q: int) -> int:
    fs = prime_factors(q - 1)
    for c in range(2, q):
        if all(pow(c, (q - 1) // f, q) != 1 for f in fs):
            return c
    raise AssertionError("no primitive root")


def root_of_unity(q: int, n: int) -> int:
    assert (q - 1) % n == 0
    w = pow(primitive_root(q), (q - 1) // n, q)
    for d in range(1, n):
        if n % d == 0 and pow(w, d, q) == 1:
            raise AssertionError("order < n")
    return w


def domain(q: int, n: int) -> list[int]:
    w = root_of_unity(q, n)
    D = [pow(w, i, q) for i in range(n)]
    assert len(set(D)) == n
    return D


# ------------------------------------------------------- polynomials
def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b, q):
    r = [0] * max(len(a), len(b))
    for i in range(len(r)):
        r[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % q
    return ptrim(r)


def pneg(a, q):
    return ptrim([(-c) % q for c in a])


def pscal(a, s, q):
    return ptrim([(c * s) % q for c in a])


def pmul(a, b, q):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    r[i + j] = (r[i + j] + x * y) % q
    return ptrim(r)


def peval(a, x, q):
    acc = 0
    for c in reversed(a):
        acc = (acc * x + c) % q
    return acc


def deg(a):
    return len(ptrim(a)) - 1


def locator(roots, q):
    p = [1]
    for r in roots:
        p = pmul(p, [(-r) % q, 1], q)
    return p


# ------------------------------------------------- moment vector E(S)
def moment_vector(S_vals, h, q):
    """E(S) = (e_1,...,e_h) of the multiset S_vals, exact mod q."""
    e = [1] + [0] * h
    for x in S_vals:
        for j in range(min(h, len(S_vals)), 0, -1):
            e[j] = (e[j] + x * e[j - 1]) % q
    return tuple(e[1:h + 1])


def all_moment_vectors(D, A, h, q):
    """Yield (index-tuple, E) for every A-subset of D.  Exact."""
    n = len(D)
    for S in combinations(range(n), A):
        yield S, moment_vector([D[i] for i in S], h, q)


# ------------------------------------------------------ combinatorics
def mask_of(idx):
    r = 0
    for i in idx:
        r |= 1 << i
    return r


def popcount(x):
    return bin(x).count("1")


def gamma_lo(masks, K):
    """indices i whose mask meets every other mask in <= K-1 coordinates."""
    M = len(masks)
    out = []
    for i in range(M):
        ok = True
        for j in range(M):
            if i != j and popcount(masks[i] & masks[j]) >= K:
                ok = False
                break
        if ok:
            out.append(i)
    return out


def max_pair_core(masks):
    M, mx = len(masks), 0
    for i in range(M):
        for j in range(i + 1, M):
            t = popcount(masks[i] & masks[j])
            if t > mx:
                mx = t
    return mx


def greedy_spread(masks, K):
    """greedy maximum pairwise-<=K-1 subfamily (lower bound)."""
    order = sorted(range(len(masks)),
                   key=lambda i: sum(1 for j in range(len(masks))
                                     if j != i and
                                     popcount(masks[i] & masks[j]) >= K))
    chosen = []
    for i in order:
        if all(popcount(masks[i] & masks[j]) <= K - 1 for j in chosen):
            chosen.append(i)
    return chosen


# ------------------------------------------- syndrome / dual (word model)
def lam(S, D, q):
    """lam^S_i for i in S (S = index tuple)."""
    out = []
    for i in S:
        p = 1
        for j in S:
            if j != i:
                p = p * (D[i] - D[j]) % q
        out.append(pow(p, q - 2, q))
    return out


def dual_basis(S, D, h, q):
    """basis of C_S = {c in F_q^n : supp(c) in S, c perp RS_K}, dim h.

    c^(t)_i = lam^S_i x_i^t for i in S, t = 0..h-1.
    """
    n = len(D)
    L = lam(S, D, q)
    rows = []
    for t in range(h):
        c = [0] * n
        for k, i in enumerate(S):
            c[i] = L[k] * pow(D[i], t, q) % q
        rows.append(c)
    return rows


def syndrome(S, D, h, q, w):
    L = lam(S, D, q)
    return tuple(sum(L[k] * pow(D[i], t, q) % q * w[i] for k, i in enumerate(S)) % q
                 for t in range(h))


def rank_mod(rows, q):
    """exact rank over F_q (rows: list of lists)."""
    rows = [list(r) for r in rows]
    ncol = len(rows[0]) if rows else 0
    piv = 0
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
                rows[i] = [(rows[i][c] - f * rows[piv][c]) % q for c in range(ncol)]
        piv += 1
        if piv == len(rows):
            break
    return piv


def nullspace_mod(rows, ncol, q):
    """basis of the right null space of the given rows over F_q."""
    rows = [list(r) for r in rows]
    piv_col = []
    piv = 0
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
                rows[i] = [(rows[i][c] - f * rows[piv][c]) % q for c in range(ncol)]
        piv_col.append(col)
        piv += 1
        if piv == len(rows):
            break
    free = [c for c in range(ncol) if c not in piv_col]
    basis = []
    for fc in free:
        v = [0] * ncol
        v[fc] = 1
        for r, pc in enumerate(piv_col):
            v[pc] = (-rows[r][fc]) % q
        basis.append(v)
    return basis
