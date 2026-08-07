#!/usr/bin/env python3
# cw_shared_target -- adversarial round: is EXCESS-CEILING(C) with an ABSOLUTE C true?
# and what does the WEAKER ratio form (CRATIO) buy mystery 4?   tools/ramguard local -- python3 ...
import math, sys
from math import comb
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import importlib.util
spec = importlib.util.spec_from_file_location("atk", __file__.rsplit('/', 1)[0] + "/attack.py")
# do NOT execute attack.py; re-declare the helpers instead.

def log2big(x):
    n = int(x)
    if n == 0: return float('-inf')
    b = n.bit_length()
    if b <= 900: return math.log2(n)
    return b - 900 + math.log2(n >> (b - 900))

def primitive_root(p):
    f = []; n = p - 1; d = 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: f.append(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in f): return g
    raise RuntimeError

def elt_of_order(p, m):
    assert (p - 1) % m == 0
    return pow(primitive_root(p), (p - 1) // m, p)

def primes_upto(N):
    s = bytearray([1]) * (N + 1); s[0:2] = b"\x00\x00"
    for i in range(2, int(N ** .5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(2, N + 1) if s[i]]

def enum_half(cols, p, k):
    m = len(cols); cur = {tuple([0] * k): [1] + [0] * m}
    for col in cols:
        nxt = {}
        for v, arr in cur.items():
            for e in (0, 1, -1):
                nv = tuple((v[i] + e * col[i]) % p for i in range(k))
                a = nxt.get(nv)
                if a is None: a = [0] * (m + 1); nxt[nv] = a
                if e == 0:
                    for w in range(m + 1):
                        if arr[w]: a[w] += arr[w]
                else:
                    for w in range(m):
                        if arr[w]: a[w + 1] += arr[w]
        cur = nxt
    return cur

def wenum(rows, p):
    N = len(rows[0]); h = N // 2; k = len(rows)
    A = enum_half([tuple(r[j] for r in rows) for j in range(h)], p, k)
    B = enum_half([tuple(r[j] for r in rows) for j in range(h, N)], p, k)
    AU = [0] * (N + 1)
    for s, arr in A.items():
        brr = B.get(tuple((-x) % p for x in s))
        if brr is None: continue
        for wa in range(h + 1):
            ca = arr[wa]
            if not ca: continue
            for wb in range(N - h + 1):
                cb = brr[wb]
                if cb: AU[wa + wb] += ca * cb
    return AU

PASS = 0; FAIL = 0
def check(nm, c, ex=""):
    global PASS, FAIL
    if c: PASS += 1; print("PASS  %-60s %s" % (nm, ex))
    else: FAIL += 1; print("FAIL  %-60s %s" % (nm, ex))

PR = primes_upto(30000)

print("=" * 104)
print("ADV-1 -- is EXCESS-CRATIO := (TMASS-1)*p^kappa/(2^N-1) BOUNDED as p grows at fixed (N,kappa)?")
print("=" * 104)
print("M2 family (negacyclic GRS, Lambda={1,3,...,2R-1}); every cell with a NONZERO ternary kernel:")
print("%4s %3s %8s %9s %6s %8s %14s %14s" % ("S", "R", "p", "SIGMA", "UMIN", "A[UMIN]", "TMASS-1", "EXCESS"))
grow = {}
for (S, R, plim) in [(8, 2, 30000), (16, 2, 20000)]:
    rows_seen = []
    for p in PR:
        if p >= plim: break
        if p <= 2 * S or (p - 1) % (2 * S): continue
        w = elt_of_order(p, 2 * S)
        rws = [[pow(w, (2 * j - 1) * e, p) for e in range(S)] for j in range(1, R + 1)]
        AU = wenum(rws, p)
        if sum(AU) == 1: continue
        tm = sum(AU[U] * 2.0 ** (-U) for U in range(S + 1))
        umin = next(U for U in range(1, S + 1) if AU[U])
        ex = (tm - 1) * p ** R / (2 ** S - 1)
        rows_seen.append((p, tm - 1, ex, umin, AU[umin]))
    grow[(S, R)] = rows_seen
    for (p, d, ex, um, au) in rows_seen:
        print("%4d %3d %8d %9.3f %6d %8d %14.6g %14.4f" % (S, R, p, S - R * math.log2(p), um, au, d, ex))
    if rows_seen:
        mx = max(rows_seen, key=lambda r: r[2])
        print("   -> S=%d R=%d : %d cells with a nonzero kernel out of the sweep; MAX EXCESS = %.4f at p=%d"
              % (S, R, len(rows_seen), mx[2], mx[0]))
    else:
        print("   -> S=%d R=%d : NO cell in the sweep has a nonzero ternary kernel" % (S, R))
allm2 = [r for v in grow.values() for r in v]
mx = max(allm2, key=lambda r: r[2]) if allm2 else None
check("ADV-1 EXCESS-CEILING(C=2) survives the extended M2 sweep", mx is None or mx[2] <= 2.0,
      "max EXCESS = %.4f at p=%d" % (mx[2], mx[0]) if mx else "no cells")
check("ADV-1 EXCESS-CEILING(C=4) survives the extended M2 sweep", mx is None or mx[2] <= 4.0,
      "max EXCESS = %.4f at p=%d" % (mx[2], mx[0]) if mx else "no cells")

print()
print("M4 family (RSET, kappa = 1), extended sweep -- where do relations die?")
print("%4s %8s %9s %6s %8s %14s %14s" % ("L", "p", "SIGMA", "UMIN", "A[UMIN]", "TMASS-1", "EXCESS"))
m4rows = {}
for (L, plim) in [(8, 30000), (16, 20000)]:
    seen = []
    for p in PR:
        if p >= plim: break
        if p <= 2 * L or (p - 1) % (2 * L): continue
        th = elt_of_order(p, 2 * L)
        AU = wenum([[pow(th, j, p) for j in range(L)]], p)
        if sum(AU) == 1: continue
        tm = sum(AU[U] * 2.0 ** (-U) for U in range(L + 1))
        umin = next(U for U in range(1, L + 1) if AU[U])
        ex = (tm - 1) * p / (2 ** L - 1)
        seen.append((p, tm - 1, ex, umin, AU[umin]))
    m4rows[L] = seen
    for (p, d, ex, um, au) in seen[-6:]:
        print("%4d %8d %9.3f %6d %8d %14.6g %14.4f" % (L, p, L - math.log2(p), um, au, d, ex))
    if seen:
        mx4 = max(seen, key=lambda r: r[2])
        print("   -> L=%d : last p with a relation = %d (sweep limit %d); MAX EXCESS = %.4f at p=%d"
              % (L, seen[-1][0], plim, mx4[2], mx4[0]))
all4 = [r for v in m4rows.values() for r in v]
mx4 = max(all4, key=lambda r: r[2])
check("ADV-1 EXCESS-CEILING(C=2) survives the extended M4 sweep", mx4[2] <= 2.0,
      "max EXCESS = %.4f at p=%d" % (mx4[2], mx4[0]))

print()
print("=" * 104)
print("ADV-2 -- the WEAKER ratio form.  CRATIO-CEILING(C): TMASS(D) <= C * (1 + (2^N-1)/p^kappa).")
print("=" * 104)
mxc = 0.0; mxcell = None
for (S, R, plim) in [(8, 2, 30000), (16, 2, 20000)]:
    for (p, d, ex, um, au) in grow[(S, R)]:
        cr = (1 + d) / (1 + (2 ** S - 1) / p ** R)
        if cr > mxc: mxc = cr; mxcell = ("M2", S, R, p)
for L in m4rows:
    for (p, d, ex, um, au) in m4rows[L]:
        cr = (1 + d) / (1 + (2 ** L - 1) / p)
        if cr > mxc: mxc = cr; mxcell = ("M4", L, 1, p)
print("   max CRATIO over every swept cell of BOTH families (2-power grids only) = %.4f at %s" % (mxc, mxcell))
check("ADV-2 CRATIO-CEILING(C=2) survives every swept cell of both families", mxc <= 2.0,
      "max CRATIO = %.4f at %s" % (mxc, mxcell))

print()
print("What CRATIO-CEILING(C) buys mystery 4 (weaker form; C enters as (C-1) when SIGMA < 0):")
p_w = 3 * 2 ** 41 + 1; e_w = 6
Bstar = 242251802232021244567343686397347233808; lB = log2big(Bstar)
print("%3s %5s | %9s %9s | %12s %12s %12s %12s" %
      ("v", "L", "S(v)", "U2", "C=1.1 e=6", "C=1.1 e=1lo", "C=2 e=6", "C=2 e=1lo"))
for v in [34, 35]:
    L = 2 ** (41 - v); rp = L - 2
    Sv = log2big(comb(2 ** (41 - v), 2 ** (40 - v) - 1)) - (41 - v)
    U2 = log2big((comb(2 * L, rp) + comb(L, rp // 2)) // (2 * L))
    gm = max((comb(L - U, (rp - U) // 2) / comb(L, rp // 2)) * 2.0 ** U for U in range(0, rp + 1, 2))
    base = log2big(comb(L, rp // 2)) + math.log2(gm)
    out = []
    for C in (1.1, 2.0):
        for lp, kap in ((math.log2(p_w), e_w), (129.5849625, 1)):
            heur = 1 + 2 ** (L - kap * lp)
            out.append(base + math.log2(C * heur - 1))
    print("%3d %5d | %9.4f %9.4f | %12.4f %12.4f %12.4f %12.4f" % (v, L, Sv, U2, out[0], out[1], out[2], out[3]))
    if v == 34:
        check("ADV-2 CRATIO-CEILING(C=1.1) de-vacuums v=34 at e=6", out[0] < lB,
              "2^%.4f < B*=2^%.4f (margin %+.4f bits)" % (out[0], lB, lB - out[0]))
        check("ADV-2 CRATIO-CEILING(C=1.1) de-vacuums v=34 at the e=1 prime floor", out[1] < lB,
              "2^%.4f < B*=2^%.4f (margin %+.4f bits)" % (out[1], lB, lB - out[1]))
        check("ADV-2 CRATIO-CEILING(C=2) de-vacuums v=34 at e=6", out[2] < lB,
              "2^%.4f < B*=2^%.4f (margin %+.4f bits)" % (out[2], lB, lB - out[2]))
        check("ADV-2 CRATIO-CEILING(C=2) de-vacuums v=34 at the e=1 prime floor", out[3] < lB,
              "2^%.4f < B*=2^%.4f (margin %+.4f bits)" % (out[3], lB, lB - out[3]))

print()
print("=" * 104)
print("TOTAL: %d PASS / %d FAIL" % (PASS, FAIL))
print("=" * 104)
sys.exit(1 if FAIL else 0)
