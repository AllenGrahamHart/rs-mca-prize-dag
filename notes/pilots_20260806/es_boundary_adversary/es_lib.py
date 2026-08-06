#!/usr/bin/env python3
"""Round 16 -- (ES) boundary adversary: shared exact machinery.

All arithmetic is EXACT INTEGER / F_p arithmetic.  No floats anywhere in a
decision path (floats appear only in printed log2 diagnostics).

THE OBJECT.  n = 2^m, S <= Z/n with |S| = r', zeta a primitive n-th root of
unity in F_{p^delta} (delta = ord_n(p)), window condition

    p_s(S) := sum_{i in S} zeta^{s i} = 0   for s = 1 .. w-1.

Periodic (= "structural") solutions: S is (n/M)-periodic, M = least power of
two >= w  (LEMMA Z, banked; notes/pilots_20260804/mun_anticoncentration/
verify_lemmaz.py:4-14).  An ACCIDENT is a solution that is not periodic.

THE CENSUS IDENTITY (this pilot's method M1).  Work in O_K = Z[zeta_n],
K = Q(zeta_n), Phi_n(X) = X^h + 1 with h = n/2 = [K:Q].  Put
x_s = sum_{i in S} zeta^{s i} in O_K and let V_s in Z^h be its coordinate
vector in the power basis.  For odd p (unramified in K) every prime P | p has
residue degree exactly delta = ord_n(p), and the primes above p correspond
bijectively to the irreducible factors of Phi_n mod p, all of degree delta.
Hence

    S is a solution in characteristic p for SOME choice of primitive n-th
    root of unity in F_{p^delta}
      <=>  some prime P | p contains every x_s
      <=>  gcd( Phi_n, V_1, ..., V_{w-1} )  has degree >= 1  in F_p[X]
      <=>  p | N(I_S),   I_S = (x_1, ..., x_{w-1}) <= O_K.

Because N(I_S) divides N(x_s) for every s, the candidate primes are exactly
the prime divisors of gcd_s |N(x_s)| (over the s with x_s != 0), each then
CONFIRMED by the exact F_p[X] gcd.  This decides ALL characteristics at once
instead of sweeping p.
"""

import math
import random

# --------------------------------------------------------------------------
# integer / primality
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
    """deterministic Miller-Rabin for n < 3.3e24, strong-probable beyond."""
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
    """raised when a cofactor could not be split within the effort cap."""


def factorize(n, effort=6, seed=12345):
    """full factorisation as {prime: exponent}; raises UnfactoredCofactor if
    a composite cofactor survives the effort cap (never silently dropped)."""
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
    """ord_n(p); n a power of two, p odd."""
    assert n & (n - 1) == 0 and p % 2 == 1
    o = 1
    cur = p % n
    while cur != 1:
        cur = cur * p % n
        o += 1
        assert o <= n
    return o


# --------------------------------------------------------------------------
# the cyclotomic ring Z[zeta_n] = Z[X]/(X^h + 1),  h = n/2
# --------------------------------------------------------------------------

def coord_vector(S, s, n):
    """coordinates of x_s = sum_{i in S} zeta^{s i} in the basis 1..zeta^{h-1}."""
    h = n // 2
    v = [0] * h
    for i in S:
        e = (s * i) % n
        if e < h:
            v[e] += 1
        else:
            v[e - h] -= 1
    return v


def det_bareiss(mat):
    """exact determinant, fraction-free Gaussian elimination."""
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
    """N_{K/Q}(x) for x with coordinate vector v; = det of multiplication."""
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
# polynomials over F_p
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


def pmulmod(a, b, mod, p):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % p
    return prem(r, mod, p)


def prem(a, mod, p):
    a = pnorm(a, p)
    dm = len(mod) - 1
    inv = pow(mod[-1], p - 2, p)
    while len(a) - 1 >= dm and a:
        c = a[-1] * inv % p
        off = len(a) - 1 - dm
        for i, mc in enumerate(mod):
            a[off + i] = (a[off + i] - c * mc) % p
        a = pnorm(a, p)
    return a


def ppowmod(base, e, mod, p):
    r = [1]
    b = prem(base[:], mod, p)
    while e:
        if e & 1:
            r = pmulmod(r, b, mod, p)
        b = pmulmod(b, b, mod, p)
        e >>= 1
    return r


def phi_n_poly(n):
    """Phi_n(X) = X^{n/2} + 1 for n a power of two >= 2."""
    h = n // 2
    return [1] + [0] * (h - 1) + [1]


def equal_degree_split(f, d, p, rng):
    """split f (all irreducible factors of degree d) into its factors."""
    if len(f) - 1 == d:
        return [f]
    while True:
        r = [rng.randrange(p) for _ in range(len(f) - 1)]
        r = pnorm(r, p)
        if not r:
            continue
        g = pgcd(r, f, p)
        if 1 <= len(g) - 1 < len(f) - 1:
            return (equal_degree_split(g, d, p, rng)
                    + equal_degree_split(pdiv(f, g, p), d, p, rng))
        h = ppowmod(r, (p ** d - 1) // 2, f, p)
        h = pnorm([h[0] - 1] + h[1:] if h else [-1], p)
        g = pgcd(h, f, p)
        if 1 <= len(g) - 1 < len(f) - 1:
            return (equal_degree_split(g, d, p, rng)
                    + equal_degree_split(pdiv(f, g, p), d, p, rng))


def pdiv(a, b, p):
    a = pnorm(a[:], p)
    b = pnorm(b, p)
    dm = len(b) - 1
    inv = pow(b[-1], p - 2, p)
    q = [0] * max(1, len(a) - dm)
    while len(a) - 1 >= dm and a:
        c = a[-1] * inv % p
        off = len(a) - 1 - dm
        q[off] = c
        for i, bc in enumerate(b):
            a[off + i] = (a[off + i] - c * bc) % p
        a = pnorm(a, p)
    return pnorm(q, p)


def one_irreducible_factor(n, p, seed=7):
    """an irreducible factor of Phi_n mod p; its root is a primitive n-th
    root of unity in F_{p^delta}."""
    d = mult_order(p, n)
    f = phi_n_poly(n)
    rng = random.Random(seed)
    facs = equal_degree_split(f, d, p, rng)
    facs.sort()
    assert all(len(g) - 1 == d for g in facs), "Phi_n factors are not equidegree"
    return facs[0]


# --------------------------------------------------------------------------
# the window / balance bookkeeping
# --------------------------------------------------------------------------

def cyclotomic_closure(w, n, p):
    """Z_w = the p-cyclotomic closure of {1,...,w-1} mod n."""
    Z = set()
    for s in range(1, w):
        c = s % n
        while c not in Z:
            Z.add(c)
            c = c * p % n
    return Z


def M_of(w):
    """least power of two >= w."""
    M = 1
    while M < w:
        M *= 2
    return M


def is_periodic(S, n, w):
    """S is (n/M)-periodic, M = least power of two >= w  (LEMMA Z form)."""
    L = n // M_of(w)
    st = set(S)
    return all(((i + L) % n in st) == (i in st) for i in range(n))


def lam_bits(n, rp, w, p):
    """Lam = log2 C(n,r') - |Z_w| * log2 p.   Lam < 0  <=>  SUB-BALANCE."""
    zw = len(cyclotomic_closure(w, n, p))
    return math.log2(math.comb(n, rp)) - zw * math.log2(p), zw


def struct_count(n, rp, w):
    M = M_of(w)
    return math.comb(n // M, rp // M) if rp % M == 0 else 0
