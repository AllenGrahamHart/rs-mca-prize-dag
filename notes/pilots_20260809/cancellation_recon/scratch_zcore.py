#!/usr/bin/env python3
"""z_ceiling_assault -- round 24 core library.  Stdlib only.
Run ONLY via  tools/ramguard tiny|local -- python3 ...  from repo root.

Functionals are the ones named in PREREG.md section R0.
The round-23 machinery (cw.py) is REUSED VERBATIM: the two weight-
enumerator functions are exec'd straight out of that file (see REF_*).
"""
import math, os, sys
from fractions import Fraction
from math import comb

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CW = os.path.join(REPO, "notes", "pilots_20260807", "cw_shared_target", "cw.py")

# ---------------------------------------------------------------- verbatim reuse
_src = open(CW).read()
_a = _src.index("def ternary_enum(")
_b = _src.index("# ================================================================ SECTION 1")
_ns = {"comb": comb, "math": math}
exec(compile(_src[_a:_b], CW, "exec"), _ns)          # noqa: S102 -- verbatim round-23 code
REF_wenum = _ns["weight_enum_kernel"]                # kappa = 1
REF_wenum_multi = _ns["weight_enum_kernel_multi"]    # kappa >= 1

PASS = 0
FAIL = 0
FAILED = []


def check(name, cond, extra=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("PASS  %-62s %s" % (name, extra))
    else:
        FAIL += 1
        FAILED.append(name)
        print("FAIL  %-62s %s" % (name, extra))


def summary():
    print("=" * 104)
    print("TOTAL: %d PASS / %d FAIL" % (PASS, FAIL))
    if FAILED:
        for f in FAILED:
            print("   FAILED: %s" % f)
    print("=" * 104)
    return 1 if FAIL else 0


# ---------------------------------------------------------------- arithmetic
def primes_upto(N):
    s = bytearray([1]) * (N + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(N ** .5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(2, N + 1) if s[i]]


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primitive_root(p):
    f = []
    n = p - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        f.append(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in f):
            return g
    raise RuntimeError


def elt_of_order(p, m):
    assert (p - 1) % m == 0
    t = pow(primitive_root(p), (p - 1) // m, p)
    assert pow(t, m, p) == 1
    return t


def all_elts_of_order(p, m):
    """every element of exact order m in F_p^*"""
    t = elt_of_order(p, m)
    out = []
    for j in range(1, m):
        if math.gcd(j, m) == 1:
            out.append(pow(t, j, p))
    return sorted(set(out))


def log2big(x):
    n = int(x)
    if n == 0:
        return float("-inf")
    b = n.bit_length()
    if b <= 900:
        return math.log2(n)
    return b - 900 + math.log2(n >> (b - 900))


# ---------------------------------------------------------------- the families
def rows_M2(S, R, p, w=None):
    """negacyclic GRS of record; Lambda = {1,3,...,2R-1} (CATCH-19B: 0 not in Lambda)."""
    lam = [2 * j - 1 for j in range(1, R + 1)]
    assert 0 not in lam, "CATCH-19B"
    if w is None:
        w = elt_of_order(p, 2 * S)
    return [[pow(w, l * e, p) for e in range(S)] for l in lam]


def rows_M4(L, p, th=None):
    """RSET / crossing deep stratum; Lambda = {1} (CATCH-19B: 0 not in Lambda)."""
    if th is None:
        th = elt_of_order(p, 2 * L)
    return [[pow(th, j, p) for j in range(L)]]


def assert_2power_grid(N):
    """CATCH-Z6: 2N must be a power of 2 for a non-probe cell."""
    n = 2 * N
    assert n & (n - 1) == 0, "CATCH-Z6 violation: 2N = %d is not a 2-power" % n


# ---------------------------------------------------------------- exact TMASS
def _half_k1(cols, p):
    cur = {0: 1}
    for c in cols:
        nxt = {}
        g = nxt.get
        for s, wv in cur.items():
            nxt[s] = g(s, 0) + 2 * wv
            a = s + c
            if a >= p:
                a -= p
            nxt[a] = g(a, 0) + wv
            b = s - c
            if b < 0:
                b += p
            nxt[b] = g(b, 0) + wv
        cur = nxt
    return cur


def _half_kk(cols, p, k):
    cur = {(0,) * k: 1}
    for col in cols:
        nxt = {}
        g = nxt.get
        for s, wv in cur.items():
            nxt[s] = g(s, 0) + 2 * wv
            a = tuple((s[i] + col[i]) % p for i in range(k))
            nxt[a] = g(a, 0) + wv
            b = tuple((s[i] - col[i]) % p for i in range(k))
            nxt[b] = g(b, 0) + wv
        cur = nxt
    return cur


def tmass_exact(rows, p):
    """EXACT Fraction  TMASS = sum_{eps in ker, ternary} 2^{-wt(eps)}.

    Meet in the middle on the 2^{-wt} weights directly (one integer per
    residue state instead of a whole weight array): state count is
    bounded by min(3^h, p^kappa), cost O(N * states)."""
    k = len(rows)
    N = len(rows[0])
    h = N // 2
    if k == 1:
        A = _half_k1(rows[0][:h], p)
        B = _half_k1(rows[0][h:], p)
        tot = 0
        for s, av in A.items():
            bv = B.get((p - s) % p)
            if bv:
                tot += av * bv
    else:
        cols = [tuple(r[j] for r in rows) for j in range(N)]
        A = _half_kk(cols[:h], p, k)
        B = _half_kk(cols[h:], p, k)
        tot = 0
        for s, av in A.items():
            bv = B.get(tuple((-x) % p for x in s))
            if bv:
                tot += av * bv
    return Fraction(tot, 1 << N)


def cell(rows, p, want_AU=False):
    """the full record for one cell; every key is a functional named in R0."""
    k = len(rows)
    N = len(rows[0])
    tm = tmass_exact(rows, p)
    H = Fraction((1 << N) - 1, p ** k)
    d = dict(N=N, kappa=k, p=p,
             TMASS=tm, TMASSf=float(tm),
             H=float(H), HEUR=float(1 + H),
             CRATIO=float(tm / (1 + H)),
             EXCESS=float((tm - 1) / H),
             SIGMA=N - k * math.log2(p),
             ZFRATIO=float(tm * p ** k / (1 << N)))
    if want_AU:
        AU = REF_wenum(rows[0], p) if k == 1 else REF_wenum_multi(rows, p)
        d["AU"] = AU
        d["UMIN"] = next((U for U in range(1, N + 1) if AU[U]), None)
        d["NKER"] = sum(AU)
    return d


# ---------------------------------------------------------------- p-free (char 0)
def cyclotomic(n):
    """Phi_n(x) as a coefficient list, integer arithmetic only."""
    # x^n - 1 divided by all Phi_d, d | n, d < n
    poly = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            q = cyclotomic(d)
            poly = _polydiv(poly, q)
    return poly


def _polydiv(a, b):
    a = a[:]
    db = len(b) - 1
    out = [0] * (len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i] // b[db]
        out[i - db] = c
        if c:
            for j in range(db + 1):
                a[i - db + j] -= c * b[j]
    assert all(x == 0 for x in a[:db]), "not divisible"
    return out


def pfree_mass(n, cap=3 ** 15):
    """PFMASS(n) and |PFREE(n)| by exhaustive search over the relation lattice
    spanned by x^i * Phi_n(x), deg < n/2.  Exact Fraction."""
    h = n // 2
    ph = cyclotomic(n)
    dph = len(ph) - 1
    shifts = h - dph
    if shifts <= 0:
        return Fraction(1), 1, 0
    if 3 ** shifts > cap:
        return None, None, shifts
    mass = Fraction(0)
    cnt = 0
    coefs = [0] * shifts
    def rec(i):
        nonlocal mass, cnt
        if i == shifts:
            v = [0] * h
            for s in range(shifts):
                if coefs[s]:
                    for j in range(dph + 1):
                        v[s + j] += coefs[s] * ph[j]
            if all(abs(x) <= 1 for x in v):
                cnt += 1
                mass += Fraction(1, 1 << sum(1 for x in v if x))
            return
        for c in (0, 1, -1):
            coefs[i] = c
            rec(i + 1)
        coefs[i] = 0
    rec(0)
    return mass, cnt, shifts
