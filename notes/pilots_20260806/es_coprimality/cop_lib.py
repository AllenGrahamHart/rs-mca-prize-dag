#!/usr/bin/env python3
"""Round 17 -- (ES) coprimality pilot: exact machinery.

All arithmetic is EXACT INTEGER / F_p arithmetic.  Floats appear only in
printed log2 diagnostics, never in a decision path.

OBJECT.  n = 2^m, h = n/2 = [K:Q], K = Q(zeta_n), O_K = Z[zeta_n],
Phi_n(X) = X^h + 1.  S <= Z/n, |S| = r'.
    x_s = sum_{i in S} zeta^{s i},      I_S = (x_1, ..., x_{w-1}) <= O_K.

NEW HERE (round 17): N(I_S) = [O_K : I_S] is computed EXACTLY as the index
of the sublattice of Z^h spanned by { x_s * zeta^j : 1<=s<=w-1, 0<=j<h },
via an incremental integer Hermite normal form.  This is a completely
different computation from round 16's F_p[X]-gcd census (which only decides
the PRIME SUPPORT of N(I_S)); agreement of the two is falsifier Phi4.

Basic ring/poly primitives are adapted from the banked round-16 file
notes/pilots_20260806/es_boundary_adversary/es_lib.py (read-only source).
"""

import math
import random

# --------------------------------------------------------------------------
# integers / primality / factorisation   (adapted from es_lib.py:43-153)
# --------------------------------------------------------------------------

_SMALL_PRIMES = []


def small_primes(limit=100000):
    global _SMALL_PRIMES
    if _SMALL_PRIMES and _SMALL_PRIMES[-1] >= limit - 1:
        return _SMALL_PRIMES
    sieve = bytearray([1]) * limit
    sieve[0] = sieve[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    _SMALL_PRIMES = [i for i in range(limit) if sieve[i]]
    return _SMALL_PRIMES


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _pollard_brent(n, rng):
    if n % 2 == 0:
        return 2
    while True:
        y = rng.randrange(1, n)
        c = rng.randrange(1, n)
        m = 128
        g = r = q = 1
        x = ys = y
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = (y * y + c) % n
                    q = q * abs(x - y) % n
                g = math.gcd(q, n)
                k += m
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n
                g = math.gcd(abs(x - ys), n)
        if g != n:
            return g


class UnfactoredCofactor(Exception):
    pass


def factorize(n, effort=8, seed=12345):
    if n < 0:
        n = -n
    out = {}
    if n in (0, 1):
        return out
    for q in small_primes(100000):
        if q * q > n:
            break
        while n % q == 0:
            out[q] = out.get(q, 0) + 1
            n //= q
    if n == 1:
        return out
    rng = random.Random(seed)
    stack = [n]
    while stack:
        m = stack.pop()
        if m == 1:
            continue
        if is_prime(m):
            out[m] = out.get(m, 0) + 1
            continue
        got = None
        for _ in range(effort):
            d = _pollard_brent(m, rng)
            if 1 < d < m:
                got = d
                break
        if got is None:
            raise UnfactoredCofactor("could not split %d" % m)
        stack.append(got)
        stack.append(m // got)
    return out


def mult_order(p, n):
    assert n & (n - 1) == 0 and p % 2 == 1
    o = 1
    cur = p % n
    while cur != 1:
        cur = cur * p % n
        o += 1
        assert o <= n
    return o


# --------------------------------------------------------------------------
# the ring Z[zeta_n] = Z[X]/(X^h+1)     (coord_vector/field_norm: es_lib)
# --------------------------------------------------------------------------

def coord_vector(S, s, n):
    """coords of x_s = sum_{i in S} zeta^{s i} in the basis 1..zeta^{h-1}."""
    h = n // 2
    v = [0] * h
    for i in S:
        e = (s * i) % n
        if e < h:
            v[e] += 1
        else:
            v[e - h] -= 1
    return v


def mul_zeta(v, h):
    """multiply by zeta:  zeta^h = -1, so shift up and wrap with a sign."""
    return [-v[h - 1]] + v[:h - 1]


def det_bareiss(mat):
    m = [row[:] for row in mat]
    k = len(m)
    sign = 1
    prev = 1
    for i in range(k - 1):
        if m[i][i] == 0:
            for j in range(i + 1, k):
                if m[j][i] != 0:
                    m[i], m[j] = m[j], m[i]
                    sign = -sign
                    break
            else:
                return 0
        for j in range(i + 1, k):
            for c in range(i + 1, k):
                m[j][c] = (m[j][c] * m[i][i] - m[j][i] * m[i][c]) // prev
            m[j][i] = 0
        prev = m[i][i]
    return sign * m[k - 1][k - 1]


def field_norm(v, n):
    """N_{K/Q}(x) for x with coordinate vector v."""
    h = n // 2
    if not any(v):
        return 0
    mat = [[0] * h for _ in range(h)]
    for j in range(h):
        for k in range(h):
            idx = k - j
            mat[k][j] = v[idx] if idx >= 0 else -v[idx + h]
    return det_bareiss(mat)


# --------------------------------------------------------------------------
# EXACT IDEAL NORM by incremental integer Hermite normal form
# --------------------------------------------------------------------------

def _egcd(a, b):
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return (old_r, old_s, old_t)


def lattice_index(gens, h):
    """[Z^h : L] for L spanned by the integer row vectors `gens`.

    Returns 0 if L has rank < h (infinite index).  Exact, no floats."""
    basis = [None] * h
    for g in gens:
        v = list(g)
        for c in range(h):
            if v[c] == 0:
                continue
            if basis[c] is None:
                if v[c] < 0:
                    v = [-t for t in v]
                basis[c] = v
                v = None
                break
            a = basis[c][c]
            b = v[c]
            g0, u, w0 = _egcd(a, b)
            m1 = -(b // g0)
            m2 = a // g0
            nb = [u * x + w0 * y for x, y in zip(basis[c], v)]
            nv = [m1 * x + m2 * y for x, y in zip(basis[c], v)]
            if nb[c] < 0:
                nb = [-t for t in nb]
            basis[c] = nb
            v = nv
        # size reduction: keep entries bounded by the pivots
        for c in range(h):
            if basis[c] is None:
                continue
            pc = basis[c][c]
            for c2 in range(c + 1, h):
                if basis[c2] is None:
                    continue
                q = basis[c][c2] // basis[c2][c2]
                if q:
                    basis[c] = [x - q * y for x, y in zip(basis[c], basis[c2])]
    if any(b is None for b in basis):
        return 0
    d = 1
    for c in range(h):
        d *= abs(basis[c][c])
    return d


def ideal_norm(S, n, w):
    """N(I_S) = [O_K : (x_1,...,x_{w-1})], EXACT.  0 iff rank deficient."""
    h = n // 2
    gens = []
    for s in range(1, w):
        v = coord_vector(S, s, n)
        if not any(v):
            continue
        for _ in range(h):
            gens.append(v)
            v = mul_zeta(v, h)
    if not gens:
        return 0
    return lattice_index(gens, h)


# --------------------------------------------------------------------------
# polynomials over F_p  (adapted from es_lib.py:225-283) -- census route
# --------------------------------------------------------------------------

def pnorm(a, p):
    a = [c % p for c in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def pgcd(a, b, p):
    a, b = pnorm(a, p), pnorm(b, p)
    while b:
        inv = pow(b[-1], p - 2, p)
        r = a[:]
        while len(r) >= len(b):
            c = r[-1] * inv % p
            off = len(r) - len(b)
            for i, bc in enumerate(b):
                r[off + i] = (r[off + i] - c * bc) % p
            r = pnorm(r, p)
        a, b = b, r
    return a


def phi_n_poly(n):
    h = n // 2
    return [1] + [0] * (h - 1) + [1]


def census_bad(S, n, w, cand):
    """the census route: which of the candidate primes really are bad."""
    PHI = phi_n_poly(n)
    out = []
    for p in cand:
        if p == 2:
            continue
        gg = PHI
        for s in range(1, w):
            v = pnorm(coord_vector(S, s, n), p)
            if not v:
                continue
            gg = pgcd(gg, v, p)
            if len(gg) - 1 < 1:
                break
        if len(gg) - 1 >= 1:
            out.append(p)
    return out


# --------------------------------------------------------------------------
# window / stratum bookkeeping
# --------------------------------------------------------------------------

def cyclotomic_closure(w, n, p):
    """Z_w = the p-cyclotomic closure of {1,...,w-1} mod n (es_lib:339)."""
    Z = set()
    for s in range(1, w):
        c = s % n
        while c not in Z:
            Z.add(c)
            c = c * p % n
    return Z


def z_w_odd(w, n, p):
    """Z_w^odd -- the <p>-closure of the ODD part of {1,...,w-1}."""
    return set(s for s in cyclotomic_closure(w, n, p) if s % 2 == 1)


def M_of(w):
    M = 1
    while M < w:
        M *= 2
    return M


def strat(S, n):
    """max a >= 0 with S + n/2^a = S  (a=0 is always true)."""
    st = set(x % n for x in S)
    a = 0
    while True:
        L = n // (2 ** (a + 1))
        if L < 1:
            return a
        if all(((i + L) % n in st) == (i in st) for i in range(n)):
            a += 1
        else:
            return a


def reduce_strat(S, n, a):
    """the reduced set S' <= Z/(n/2^a) when strat(S) >= a."""
    n2 = n // (2 ** a)
    return sorted(set(i % n2 for i in S))


def is_periodic(S, n, w):
    L = n // M_of(w)
    st = set(S)
    return all(((i + L) % n in st) == (i in st) for i in range(n))


def antipodal_pairs(S, n):
    """a_{n/2}(S) = #{(i,j) in SxS : i-j = n/2 mod n}."""
    st = set(S)
    return sum(1 for i in S if (i + n // 2) % n in st)


def cs_floor_ok(n, rp, w, p, S):
    """(CS3): |Z_w^odd| log2 p <= (n/4) log2 (r' - a).  True = consistent."""
    zo = len(z_w_odd(w, n, p))
    a = antipodal_pairs(S, n)
    base = rp - a
    if base <= 1:
        return zo * math.log2(p) <= 0.0, zo, base
    return zo * math.log2(p) <= (n / 4.0) * math.log2(base), zo, base
