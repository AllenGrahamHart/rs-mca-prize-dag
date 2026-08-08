#!/usr/bin/env python3
"""Round-24 kernel_window_hunt library.  STDLIB ONLY, EXACT INTEGER ARITHMETIC.

REUSES the coordinator-replayed exact tower norm from
notes/pilots_20260807/ge_floor_falsifier/gelib.py (tower_norm, lines 41-56).
Nothing here re-derives it.

Registered in PREREG.md sections P3, P4, P5, P8.
"""
import os
import random
import sys
from math import gcd

_HERE = os.path.dirname(os.path.abspath(__file__))
_GE = os.path.abspath(os.path.join(_HERE, "..", "..", "pilots_20260807",
                                   "ge_floor_falsifier"))
if _GE not in sys.path:
    sys.path.insert(0, _GE)

from gelib import tower_norm  # noqa: E402  (the reused exact norm)

# --------------------------------------------------------------- constants
B_TD = 1 << 17                      # registered trial-division bound (P4)
CEIL253 = 253 ** 32                 # PROVED ceiling (high_field_folded_box)
W_TOP_LO = 1 << 244
W_DEP_LO = 1 << 166
W_ADM_LO = 1 << 128


def _sieve(limit):
    bs = bytearray([1]) * limit
    bs[0:2] = b"\x00\x00"
    i = 2
    while i * i < limit:
        if bs[i]:
            bs[i * i::i] = bytearray(len(bs[i * i::i]))
        i += 1
    return [i for i in range(limit) if bs[i]]


SMALL_PRIMES = _sieve(B_TD)


def _prodprimes(ps):
    cur = [p for p in ps]
    while len(cur) > 1:
        nxt = []
        for i in range(0, len(cur) - 1, 2):
            nxt.append(cur[i] * cur[i + 1])
        if len(cur) % 2:
            nxt.append(cur[-1])
        cur = nxt
    return cur[0]


PPROD = _prodprimes(SMALL_PRIMES[1:])       # product of odd primes < B_TD

# --------------------------------------------------------------- primality


def _mr(n, a):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1:
            return True
    return False


def _jacobi(a, n):
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def _is_square(n):
    if n < 0:
        return False
    r = int(n ** 0.5) if n.bit_length() < 52 else 1 << ((n.bit_length() + 1) // 2)
    if n.bit_length() >= 52:                  # integer Newton
        while True:
            r2 = (r + n // r) // 2
            if r2 >= r:
                break
            r = r2
    for c in range(max(0, r - 2), r + 3):
        if c * c == n:
            return True
    return False


def _strong_lucas(n):
    """Strong Lucas PRP with Selfridge (method A) parameters."""
    if _is_square(n):
        return False
    D = 5
    while True:
        j = _jacobi(D, n)
        if j == -1:
            break
        if j == 0 and abs(D) != n:
            return False
        D = -(D + 2) if D > 0 else -(D - 2)
    P, Q = 1, (1 - D) // 4
    d = n + 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    U, V, Qk = 1, P % n, Q % n                 # (U_1, V_1, Q^1)
    for b in bin(d)[3:]:
        U, V = U * V % n, (V * V - 2 * Qk) % n  # index doubling
        Qk = Qk * Qk % n
        if b == "1":
            U, V = (P * U + V), (D * U + P * V)
            if U % 2:
                U += n
            if V % 2:
                V += n
            U = (U >> 1) % n
            V = (V >> 1) % n
            Qk = Qk * Q % n
    if U == 0 or V == 0:
        return True
    for _ in range(s - 1):
        V = (V * V - 2 * Qk) % n
        if V == 0:
            return True
        Qk = Qk * Qk % n
    return False


def is_probable_prime(n, mr_rounds=0, rng=None):
    """BPSW (strong base-2 MR + strong Lucas) plus optional random-base MR."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    if not _mr(n, 2):
        return False
    if not _strong_lucas(n):
        return False
    if mr_rounds:
        rr = rng or random.Random(12345)
        for _ in range(mr_rounds):
            if not _mr(n, rr.randrange(2, n - 1)):
                return False
    return True


# --------------------------------------------------------- factor stripping
def strip_small(n):
    """Remove EVERY prime factor < B_TD.  Returns (rough, {p: e})."""
    fac = {}
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    if e:
        fac[2] = e
    if n == 1:
        return 1, fac
    g = gcd(n, PPROD)
    if g > 1:
        gg = g
        for p in SMALL_PRIMES:
            if gg == 1:
                break
            if p * p > gg:
                break
            if gg % p == 0:
                gg //= p
                e = 0
                while n % p == 0:
                    n //= p
                    e += 1
                fac[p] = e
        if gg > 1:
            e = 0
            while n % gg == 0:
                n //= gg
                e += 1
            fac[gg] = e
    return n, fac


def pollard_brent(n, budget, rng):
    """Brent's rho; a nontrivial factor of composite n, or None within budget."""
    if n % 2 == 0:
        return 2
    y = rng.randrange(1, n)
    c = rng.randrange(1, n)
    m = 128
    g = r = q = 1
    x = ys = y
    steps = 0
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
                steps += 1
            g = gcd(q, n)
            k += m
            if steps > budget:
                return None
        r *= 2
    if g == n:
        g = 1
        while g == 1:
            ys = (ys * ys + c) % n
            g = gcd(abs(x - ys), n)
            steps += 1
            if steps > budget:
                return None
    return None if g == n else g


# ---------------------------------------------------------------- families
def fam_A(h, rng):
    return [rng.choice((-2, -1, 0, 1, 2)) for _ in range(h)]


def fam_B(h, rng):
    w = [rng.choice((-2, 2)) for _ in range(h)]
    w[rng.randrange(h)] = rng.choice((-1, 1))
    return w


def fam_C(h, rng, k=3):
    w = [rng.choice((-2, 2)) for _ in range(h)]
    for j in rng.sample(range(h), k):
        w[j] = rng.choice((-1, 1))
    return w


def fam_S(h, rng, s):
    w = [0] * h
    for j in rng.sample(range(h), s):
        w[j] = rng.choice((-1, 1))
    return w


def nodd(w):
    return sum(1 for t in w if t % 2)


def sq(w):
    return sum(t * t for t in w)


def l1(w):
    return sum(abs(t) for t in w)


# ------------------------------------------------------------ climb (FAM-D)
def climb(w, rng, target_bits, max_evals=20000):
    """Single-coordinate hill climb on |Norm|; keeps nodd(w) odd (norm odd)."""
    h = len(w)
    w = list(w)
    cur = abs(tower_norm(w))
    start = cur
    evals = 0
    while evals < max_evals and cur.bit_length() < target_bits:
        improved = False
        order = list(range(h))
        rng.shuffle(order)
        for j in order:
            old = w[j]
            w[j] = -old                        # sign flip: parity preserved
            n2 = abs(tower_norm(w))
            evals += 1
            if n2 > cur:
                cur = n2
                improved = True
                break
            w[j] = old
            if evals >= max_evals:
                break
        if not improved:
            break
    return w, cur, start, evals


# --------------------------------------------------- independent verifier
def kernel_membership(w, p, order):
    """Independent of tower_norm.  Find rho of exact order `order` mod p and an
    odd s with sum_i w_i rho^{s i} = 0 mod p.  Returns (rho, s) or None."""
    if (p - 1) % order:
        return None
    e = (p - 1) // order
    rho = None
    for g in range(2, 500):
        r = pow(g, e, p)
        if pow(r, order // 2, p) == p - 1:
            rho = r
            break
    if rho is None:
        return None
    h = len(w)
    for s in range(1, order, 2):
        rs = pow(rho, s, p)
        acc = 0
        cur = 1
        for j in range(h):
            if w[j]:
                acc = (acc + w[j] * cur) % p
            cur = cur * rs % p
        if acc % p == 0:
            return (rho, s)
    return None
