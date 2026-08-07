#!/usr/bin/env python3
"""Round-22 MYSTERY-5 falsifier library.  STDLIB ONLY, EXACT INTEGER ARITHMETIC.

Ring  R = Z[zeta_{N'}] = Z[x]/(x^h + 1),  h = N'/2,  N' a 2-power (CATCH-Z6).

Everything a decision depends on is exact:
  * Norm_{R/Q} by the 2-adic tower recursion
        v(x) v(-x) = a(y)^2 - y b(y)^2   (y = x^2,  a = even part, b = odd part)
    so Norm_h(v) = Norm_{h/2}(a^2 - y b^2 mod y^{h/2}+1).   No floating point.
  * prime-ideal support by gcd(d mod p, x^h + 1) in F_p[x]; since p is odd,
    x^h+1 is squarefree mod p, so that gcd is the squarefree product of exactly
    the primes above p dividing (d).  Ideal COUNT = deg(gcd)/f_p with
    f_p = ord of p in (Z/N')^*.  No polynomial factorization is ever needed:
    unions of ideal sets are lcm's of squarefree divisors.
"""
import itertools
from array import array


# --------------------------------------------------------------- exact norm
def negasq(a):
    """Square of a in Z[y]/(y^m+1), m = len(a).  c_k = sum_{i+j=k} - sum_{i+j=k+m}."""
    m = len(a)
    c = [0] * m
    for i in range(m):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(m):
            aj = a[j]
            if aj == 0:
                continue
            s = i + j
            if s < m:
                c[s] += ai * aj
            else:
                c[s - m] -= ai * aj
    return c


def tower_norm(w):
    """Norm_{R/Q} of w in Z[x]/(x^h+1), h = len(w) a power of two.  Exact."""
    n = len(w)
    while n > 1:
        m = n >> 1
        a = w[0::2]
        b = w[1::2]
        A = negasq(a)
        B = negasq(b)
        # u = A - y*B  in Z[y]/(y^m+1);  y*B = (-B[m-1], B[0], ..., B[m-2])
        u = [A[0] + B[m - 1]]
        for i in range(1, m):
            u.append(A[i] - B[i - 1])
        w = u
        n = m
    return w[0]


def is_pow2(x):
    x = abs(int(x))
    return x != 0 and (x & (x - 1)) == 0


def odd_part(x):
    x = abs(int(x))
    while x and x % 2 == 0:
        x >>= 1
    return x


# ------------------------------------------------------------------ centers
def centers(h):
    """C(N') = { v in {-1,0,1}^h : #zeros(v) even } -- the e_1 values."""
    out = []
    for v in itertools.product((-1, 0, 1), repeat=h):
        z = 0
        for t in v:
            if t == 0:
                z += 1
        if z % 2 == 0:
            out.append(v)
    return out


def box(h):
    """{-2,...,2}^h."""
    return itertools.product((-2, -1, 0, 1, 2), repeat=h)


# ------------------------------------------------------------- factorization
def spf_sieve(limit):
    """Smallest-prime-factor table up to `limit` (inclusive)."""
    spf = array('i', [0]) * (limit + 1)
    spf = array('i', bytes(4 * (limit + 1)))
    i = 2
    while i * i <= limit:
        if spf[i] == 0:
            for j in range(i * i, limit + 1, i):
                if spf[j] == 0:
                    spf[j] = i
        i += 1
    return spf


def factor_with(spf, x):
    """{p: e} for x >= 1 using an spf table covering x."""
    out = {}
    while x > 1:
        p = spf[x]
        if p == 0:
            p = x
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        out[p] = e
    return out


# ------------------------------------------------------------ F_p[x] helpers
def ptrim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def pmod(a, p):
    return ptrim([c % p for c in a])


def pgcd(a, b, p):
    """Monic gcd in F_p[x]; a, b given low-to-high, already reduced."""
    a = list(a)
    b = list(b)
    ptrim(a)
    ptrim(b)
    while b:
        # a mod b
        db = len(b) - 1
        inv = pow(b[db], p - 2, p)
        while len(a) - 1 >= db and a:
            da = len(a) - 1
            f = a[da] * inv % p
            sh = da - db
            for i in range(db + 1):
                a[sh + i] = (a[sh + i] - f * b[i]) % p
            ptrim(a)
        a, b = b, a
    if not a:
        return []
    inv = pow(a[-1], p - 2, p)
    return [c * inv % p for c in a]


def mult_order(p, n):
    """ord of p in (Z/n)^*."""
    p %= n
    f = 1
    cur = p
    while cur != 1:
        cur = cur * p % n
        f += 1
    return f


def sigma(dvec, p, h):
    """gcd(d mod p, x^h + 1) in F_p[x], monic.  Encodes exactly the primes
    above p that divide the ideal (d).  Returned as a tuple (hashable)."""
    xh1 = [0] * (h + 1)
    xh1[0] = 1
    xh1[h] = 1
    g = pgcd(pmod(list(dvec), p), xh1, p)
    return tuple(g)


def plcm(a, b, p):
    """lcm of two squarefree monic divisors of x^h+1 mod p."""
    if not a:
        return tuple(b)
    if not b:
        return tuple(a)
    g = pgcd(list(a), list(b), p)
    # a*b/g
    prod = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                prod[i + j] = (prod[i + j] + ai * bj) % p
    ptrim(prod)
    # divide by g
    dg = len(g) - 1
    inv = pow(g[dg], p - 2, p)
    q = [0] * (len(prod) - dg)
    r = list(prod)
    while len(r) - 1 >= dg and r:
        dr = len(r) - 1
        f = r[dr] * inv % p
        q[dr - dg] = f
        for i in range(dg + 1):
            r[dr - dg + i] = (r[dr - dg + i] - f * g[i]) % p
        ptrim(r)
    assert not r, "lcm division not exact"
    inv2 = pow(q[-1], p - 2, p)
    return tuple(c * inv2 % p for c in q)


def pdivides(a, b, p):
    """a | b in F_p[x] for monic a, b."""
    if not a:
        return True
    if len(a) > len(b):
        return False
    da = len(a) - 1
    inv = pow(a[da], p - 2, p)
    r = list(b)
    while len(r) - 1 >= da and r:
        dr = len(r) - 1
        f = r[dr] * inv % p
        for i in range(da + 1):
            r[dr - da + i] = (r[dr - da + i] - f * a[i]) % p
        ptrim(r)
    return not r


# --------------------------------------------------------------- max clique
class Budget(Exception):
    pass


def max_clique(adj, nodes, node_budget=4_000_000, lb=0):
    """Exact max clique (greedy-coloured branch and bound).
    `lb` seeds the incumbent: the search then only certifies "no clique > lb"
    (returned size stays lb if none exists), which prunes hard.
    Returns (size, witness, complete) -- complete=False if the budget ran out."""
    best = [lb]
    best_set = [[]]
    seen = [0]

    def expand(R, P):
        seen[0] += 1
        if seen[0] > node_budget:
            raise Budget()
        if not P:
            if len(R) > best[0]:
                best[0] = len(R)
                best_set[0] = list(R)
            return
        if len(R) + len(P) <= best[0]:
            return
        classes = []
        colours = {}
        for v in sorted(P, key=lambda t: -len(adj[t] & P)):
            for ci, cl in enumerate(classes):
                if not (adj[v] & cl):
                    cl.add(v)
                    colours[v] = ci + 1
                    break
            else:
                classes.append({v})
                colours[v] = len(classes)
        cand = sorted(P, key=lambda t: colours[t])
        for i in range(len(cand) - 1, -1, -1):
            v = cand[i]
            if len(R) + colours[v] <= best[0]:
                return
            expand(R + [v], P & adj[v])
            P = P - {v}

    try:
        expand([], set(nodes))
        return best[0], best_set[0], True
    except Budget:
        return best[0], best_set[0], False
