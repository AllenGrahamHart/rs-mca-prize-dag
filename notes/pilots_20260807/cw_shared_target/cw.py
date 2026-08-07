#!/usr/bin/env python3
# cw_shared_target -- round 23.  Stdlib only.  Run via tools/ramguard local -- python3 ...
# Every functional measured here is named in PREREG.md section R0.
import math, sys
from math import comb
from itertools import combinations

PASS = 0
FAIL = 0
def check(name, cond, extra=""):
    global PASS, FAIL
    if cond:
        PASS += 1; print("PASS  %-58s %s" % (name, extra))
    else:
        FAIL += 1; print("FAIL  %-58s %s" % (name, extra))

def log2big(x):
    # exact-ish log2 of a positive integer/Fraction-free
    if x == 0: return float('-inf')
    n = int(x)
    b = n.bit_length()
    if b <= 900:
        return math.log2(n)
    return b - 900 + math.log2(n >> (b - 900))

def primitive_root(p):
    if p == 2: return 1
    f = []
    n = p - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: f.append(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in f):
            return g
    raise RuntimeError

def elt_of_order(p, m):
    """element of exact order m in F_p^*; requires m | p-1"""
    assert (p - 1) % m == 0
    g = primitive_root(p)
    t = pow(g, (p - 1) // m, p)
    assert pow(t, m, p) == 1
    for q in range(1, m):
        if m % q == 0 and q < m:
            assert pow(t, q, p) != 1, (p, m, q)
    return t

def primes_upto(N):
    sieve = bytearray([1]) * (N + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(N ** .5) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2, N + 1) if sieve[i]]

PRIMES = primes_upto(20000)

# ---------------------------------------------------------------- MITM ternary
def ternary_enum(coeffs, p):
    """all eps in {0,+-1}^len(coeffs): dict  value -> [count by weight]"""
    m = len(coeffs)
    cur = {0: [1] + [0] * m}
    for c in coeffs:
        nxt = {}
        for v, arr in cur.items():
            for e in (0, 1, -1):
                nv = (v + e * c) % p
                a = nxt.get(nv)
                if a is None:
                    a = [0] * (m + 1); nxt[nv] = a
                if e == 0:
                    for w in range(m + 1):
                        if arr[w]: a[w] += arr[w]
                else:
                    for w in range(m):
                        if arr[w]: a[w + 1] += arr[w]
        cur = nxt
    return cur

def weight_enum_kernel(coeffs, p):
    """AU[U] = #{eps in {0,+-1}^N : sum eps_j coeffs_j = 0 mod p}, by support U."""
    N = len(coeffs)
    h = N // 2
    A = ternary_enum(coeffs[:h], p)
    B = ternary_enum(coeffs[h:], p)
    AU = [0] * (N + 1)
    for s, arr in A.items():
        brr = B.get((-s) % p)
        if brr is None: continue
        for wa in range(h + 1):
            ca = arr[wa]
            if not ca: continue
            for wb in range(N - h + 1):
                cb = brr[wb]
                if cb: AU[wa + wb] += ca * cb
    return AU

def weight_enum_kernel_multi(rows, p):
    """same but with several linear conditions (rows = list of coeff vectors)."""
    N = len(rows[0]); h = N // 2
    def enum(cols):
        cur = {tuple([0]*len(rows)): [1] + [0]*len(cols)}
        m = len(cols)
        for j, col in enumerate(cols):
            nxt = {}
            for v, arr in cur.items():
                for e in (0, 1, -1):
                    nv = tuple((v[i] + e*col[i]) % p for i in range(len(rows)))
                    a = nxt.get(nv)
                    if a is None:
                        a = [0]*(m+1); nxt[nv] = a
                    if e == 0:
                        for w in range(m+1):
                            if arr[w]: a[w] += arr[w]
                    else:
                        for w in range(m):
                            if arr[w]: a[w+1] += arr[w]
            cur = nxt
        return cur
    colsA = [tuple(r[j] for r in rows) for j in range(h)]
    colsB = [tuple(r[j] for r in rows) for j in range(h, N)]
    A = enum(colsA); B = enum(colsB)
    AU = [0]*(N+1)
    for s, arr in A.items():
        key = tuple((-x) % p for x in s)
        brr = B.get(key)
        if brr is None: continue
        for wa in range(h+1):
            ca = arr[wa]
            if not ca: continue
            for wb in range(N-h+1):
                cb = brr[wb]
                if cb: AU[wa+wb] += ca*cb
    return AU

# ================================================================ SECTION 1
print("=" * 100)
print("SECTION 1 -- Q1: GDEV(L,r',U) = [C(L-U,(r'-U)/2)/C(L,r'/2)] * 2^U   (M4 weight vs M2 weight 2^-U)")
print("=" * 100)
print("%6s %6s | %s" % ("L", "r'", "GDEV at U = 0,2,4,6,8,...  (U even; r'=L-2)"))
gdev_all = []
for L in [8, 16, 32, 64, 128]:
    rp = L - 2
    row = []
    for U in range(0, rp + 1, 2):
        g = comb(L - U, (rp - U) // 2) / comb(L, rp // 2)
        row.append(g * 2 ** U)
    gdev_all.append((L, row))
    print("%6d %6d | %s" % (L, rp, " ".join("%.4f" % x for x in row[:9])))
    mono = all(row[i] <= row[i + 1] + 1e-12 for i in range(len(row) - 1))
    check("Q1 GDEV monotone increasing in U, L=%d" % L, mono)
g64 = comb(64 - 2, (62 - 2) // 2) / comb(64, 31) * 4
check("Q1 GDEV(64,62,2) = 1.0149 +- 0.001", abs(g64 - 1.0149) < 1e-3, "measured %.6f" % g64)
for L, row in gdev_all:
    mx = max(row)
    check("Q1 GDEV in [1,1.6], L=%d" % L, 1 - 1e-12 <= min(row) and mx <= 1.6,
          "min %.4f max %.4f (at U=%d)" % (min(row), mx, 2 * row.index(mx)))
# the full-cube identity  sum_all eps GW = C(2L,r')/C(L,r'/2)
for L in [8, 16, 64]:
    rp = L - 2
    tot = sum(comb(L, U) * (2 ** U) * comb(L - U, (rp - U) // 2) for U in range(0, rp + 1, 2))
    check("LEMMA TC total identity at L=%d" % L, tot == comb(2 * L, rp),
          "%d vs C(%d,%d)=%d" % (tot, 2 * L, rp, comb(2 * L, rp)))

# ================================================================ SECTION 2
print()
print("=" * 100)
print("SECTION 2 -- Q2/Q3/Q5: RSET census at bb_nu_transport's cells (CELL-M4a)")
print("=" * 100)
BB_NACC = {(8, 17): 416, (8, 97): 80, (8, 113): 16, (8, 193): 16, (8, 241): 0,
           (16, 97): 4848608, (16, 193): 2432064, (16, 257): 1823616,
           (16, 353): 1332800, (16, 449): 1042272, (16, 577): 808256,
           (16, 641): 744128}
print("%4s %6s | %10s %10s | %12s %12s %8s | %6s %6s | %9s %9s" %
      ("L", "p", "#R", "#R heur", "ACC", "bb N_acc", "match", "UMIN", "USTAR", "TMASS", "HEUR"))
sec2 = {}
for (L, p) in sorted(BB_NACC):
    th = elt_of_order(p, 2 * L)
    coeffs = [pow(th, j, p) for j in range(L)]
    AU = weight_enum_kernel(coeffs, p)
    rp = L - 2
    nR = sum(AU)
    tmass = sum(AU[U] * 2.0 ** (-U) for U in range(L + 1))
    heur = 1 + (2 ** L - 1) / p
    zfl = (2 ** L) / p
    fib = sum(AU[U] * comb(L - U, (rp - U) // 2) for U in range(0, rp + 1, 2) if AU[U])
    acc = fib - comb(L, rp // 2)
    umin = next((U for U in range(1, L + 1) if AU[U]), None)
    ustar = max(range(L + 1), key=lambda U: AU[U] * 2.0 ** (-U))
    sec2[(L, p)] = dict(AU=AU, tmass=tmass, heur=heur, zfl=zfl, fib=fib, acc=acc,
                        umin=umin, ustar=ustar, nR=nR)
    print("%4d %6d | %10d %10.1f | %12d %12d %8s | %6s %6d | %9.4f %9.4f" %
          (L, p, nR, 3 ** L / p, acc, BB_NACC[(L, p)], acc == BB_NACC[(L, p)],
           umin, ustar, tmass, heur))
    check("Q2 ACC == bb N_acc at (L=%d,p=%d)" % (L, p), acc == BB_NACC[(L, p)],
          "%d vs %d" % (acc, BB_NACC[(L, p)]))
    check("Z-FLOOR TMASS >= 2^L/p at (L=%d,p=%d)" % (L, p), tmass >= zfl - 1e-9,
          "TMASS %.4f  floor %.4f  ZFRATIO %.4f" % (tmass, zfl, tmass / zfl))
print()
print("Q5 (M4 clause): USTAR vs UMIN --")
for (L, p) in sorted(sec2):
    d = sec2[(L, p)]
    print("   L=%3d p=%4d  UMIN=%s  USTAR=%d  (bulk = L/2 = %d)  A[UMIN]*2^-UMIN=%.4g  A[USTAR]*2^-USTAR=%.4g"
          % (L, p, d['umin'], d['ustar'], L // 2,
             (d['AU'][d['umin']] * 2.0 ** (-d['umin'])) if d['umin'] else 0,
             d['AU'][d['ustar']] * 2.0 ** (-d['ustar'])))

# ================================================================ SECTION 3
print()
print("=" * 100)
print("SECTION 3 -- Q3 adversarial: max CRATIO over the 2-power grid, p = 1 mod 2L, p < 1200")
print("=" * 100)
worst = []
for L in [4, 8, 16]:
    best = (0.0, None)
    rows = []
    for p in PRIMES:
        if p >= 1200: break
        if p <= 2 * L or (p - 1) % (2 * L): continue
        th = elt_of_order(p, 2 * L)
        coeffs = [pow(th, j, p) for j in range(L)]
        AU = weight_enum_kernel(coeffs, p)
        tmass = sum(AU[U] * 2.0 ** (-U) for U in range(L + 1))
        heur = 1 + (2 ** L - 1) / p
        cr = tmass / heur
        zfr = tmass / ((2 ** L) / p)
        umin = next((U for U in range(1, L + 1) if AU[U]), None)
        rows.append((p, tmass, heur, cr, zfr, umin))
        if cr > best[0]: best = (cr, p)
    worst.append((L, best))
    print("  L=%2d : %3d cells; max CRATIO = %.4f at p=%d; min CRATIO = %.4f" %
          (L, len(rows), best[0], best[1], min(r[3] for r in rows)))
    for r in rows[:4] + rows[-3:]:
        print("        p=%5d TMASS=%12.5f HEUR=%12.5f CRATIO=%.4f ZFRATIO=%.4f UMIN=%s"
              % (r[0], r[1], r[2], r[3], r[4], r[5]))
    check("Q3 CRATIO <= 2 on 2-power grid, L=%d" % L, best[0] <= 2.0,
          "max %.4f at p=%d" % (best[0], best[1]))

# ================================================================ SECTION 4
print()
print("=" * 100)
print("SECTION 4 -- Q4 adversarial (CELL-ADV, INVALID by CATCH-Z6): composite 2L with 3 | 2L")
print("=" * 100)
for L in [6, 12]:
    rows = []
    for p in PRIMES:
        if p >= 2000: break
        if p <= 2 * L or (p - 1) % (2 * L): continue
        th = elt_of_order(p, 2 * L)
        coeffs = [pow(th, j, p) for j in range(L)]
        AU = weight_enum_kernel(coeffs, p)
        tmass = sum(AU[U] * 2.0 ** (-U) for U in range(L + 1))
        heur = 1 + (2 ** L - 1) / p
        umin = next((U for U in range(1, L + 1) if AU[U]), None)
        rows.append((p, tmass, heur, tmass / heur, umin, AU[umin] if umin else 0))
    mx = max(rows, key=lambda r: r[3])
    print("  L=%2d (2L=%d): %d cells; max CRATIO = %.2f at p=%d" % (L, 2 * L, len(rows), mx[3], mx[0]))
    for r in rows[:3] + rows[-3:]:
        print("        p=%5d TMASS=%10.5f HEUR=%10.5f CRATIO=%8.2f UMIN=%s A[UMIN]=%d"
              % (r[0], r[1], r[2], r[3], r[4], r[5]))
    if L == 6:
        check("Q4 CRATIO > 100 at L=6, some p > 500", any(r[3] > 100 and r[0] > 500 for r in rows),
              "max over p>500: %.2f" % max([r[3] for r in rows if r[0] > 500] or [0]))

# ================================================================ SECTION 5
print()
print("=" * 100)
print("SECTION 5 -- Q6: the L2 (collision) loss.  CELL-M4b, w=2 primal object, kappa = 1")
print("=" * 100)
print("  NW  := #{x in {0,1}^n : wt(x)=r', sum_i x_i theta^i = 0},  n = 2L, r' = L-2")
print("  COLL:= sum over BALANCED ternary eps in the same code of C(n-U, r'-U/2)   (>= NW^2)")
print("%4s %6s | %10s %10s %10s | %12s | %9s %9s" %
      ("L", "p", "NW brute", "FIB(fold)", "C(n,r')/p", "COLL", "L2LOSS", "0.5log2p"))
for L in [4, 8]:
    n = 2 * L; rp = L - 2
    for p in PRIMES:
        if p >= 400: break
        if p <= n or (p - 1) % n: continue
        th = elt_of_order(p, n)
        pw = [pow(th, i, p) for i in range(n)]
        # brute-force primal
        NW = 0
        for S in combinations(range(n), rp):
            if sum(pw[i] for i in S) % p == 0: NW += 1
        # fold route
        coeffs = [pow(th, j, p) for j in range(L)]
        AU = weight_enum_kernel(coeffs, p)
        fib = sum(AU[U] * comb(L - U, (rp - U) // 2) for U in range(0, rp + 1, 2) if AU[U])
        # collision bound: balanced ternary in the LENGTH-n code
        h = n // 2
        def enum2(cols):
            cur = {0: {(0, 0): 1}}
            for c in cols:
                nxt = {}
                for v, dd in cur.items():
                    for e in (0, 1, -1):
                        nv = (v + e * c) % p
                        t = nxt.setdefault(nv, {})
                        for (npl, nmi), ct in dd.items():
                            k = (npl + (e == 1), nmi + (e == -1))
                            t[k] = t.get(k, 0) + ct
                cur = nxt
            return cur
        A2 = enum2(pw[:h]); B2 = enum2(pw[h:])
        COLL = 0
        for s, da in A2.items():
            db = B2.get((-s) % p)
            if db is None: continue
            for (pa, ma), ca in da.items():
                for (pb, mb), cb in db.items():
                    if pa + pb != ma + mb: continue
                    U = 2 * (pa + pb)
                    if rp - U // 2 < 0 or n - U < rp - U // 2: continue
                    COLL += ca * cb * comb(n - U, rp - U // 2)
        check("FIB(fold) == NW(brute) at (L=%d,p=%d)" % (L, p), fib == NW, "%d vs %d" % (fib, NW))
        check("COLL >= NW^2 at (L=%d,p=%d)" % (L, p), COLL >= NW * NW, "%d vs %d" % (COLL, NW * NW))
        l2loss = 0.5 * log2big(COLL) - log2big(NW) if NW > 0 else float('nan')
        print("%4d %6d | %10d %10d %10.2f | %12d | %9.4f %9.4f" %
              (L, p, NW, fib, comb(n, rp) / p, COLL, l2loss, 0.5 * math.log2(p)))
        if NW > 0:
            check("Q6 L2LOSS >= 0.40*log2 p at (L=%d,p=%d)" % (L, p), l2loss >= 0.40 * math.log2(p),
                  "L2LOSS %.4f  vs 0.40*log2p = %.4f  (0.5*log2p = %.4f)"
                  % (l2loss, 0.40 * math.log2(p), 0.5 * math.log2(p)))

# ================================================================ SECTION 6
print()
print("=" * 100)
print("SECTION 6 -- CELL-M2: the negacyclic GRS toy.  ZTOY = TMASS(ker),  Lambda={1,3,..,2R-1}")
print("=" * 100)
print("%5s %4s %3s | %10s %10s %8s | %6s %6s %6s | %s" %
      ("p", "S", "R", "ZTOY", "2^S/p^R", "ZFRATIO", "UMIN", "2R+1", "USTAR", "AU (U: count)"))
for (p, S, R) in [(17, 8, 2), (41, 8, 2), (97, 16, 2), (97, 16, 4), (193, 16, 2), (193, 16, 4)]:
    if (p - 1) % (2 * S): continue
    w = elt_of_order(p, 2 * S)
    rows = [[pow(w, (2 * j - 1) * e, p) for e in range(S)] for j in range(1, R + 1)]
    AU = weight_enum_kernel_multi(rows, p)
    ztoy = sum(AU[U] * 2.0 ** (-U) for U in range(S + 1))
    zfl = (2 ** S) / p ** R
    umin = next((U for U in range(1, S + 1) if AU[U]), None)
    ustar = max(range(S + 1), key=lambda U: AU[U] * 2.0 ** (-U))
    nz = ",".join("%d:%d" % (U, AU[U]) for U in range(S + 1) if AU[U])
    print("%5d %4d %3d | %10.5f %10.5f %8.4f | %6s %6d %6d | %s" %
          (p, S, R, ztoy, zfl, ztoy / zfl, umin, 2 * R + 1, ustar, nz))
    check("Z-FLOOR holds at M2 toy (p=%d,S=%d,R=%d)" % (p, S, R), ztoy >= zfl - 1e-9,
          "ZTOY %.5f >= %.5f" % (ztoy, zfl))
    check("Z-1 min ternary weight >= 2R+1 at (p=%d,S=%d,R=%d)" % (p, S, R),
          umin is None or umin >= 2 * R + 1, "UMIN=%s vs 2R+1=%d" % (umin, 2 * R + 1))
    heur = 1 + (2 ** S - 1) / p ** R
    check("CRATIO <= 2 at M2 toy (p=%d,S=%d,R=%d)" % (p, S, R), ztoy / heur <= 2.0,
          "CRATIO %.4f" % (ztoy / heur))

# ================================================================ SECTION 7
print()
print("=" * 100)
print("SECTION 7 -- Q7/Q8: exact official-row arithmetic")
print("=" * 100)
p_w = 3 * 2 ** 41 + 1
e_w = 6
Bstar = 242251802232021244567343686397347233808
print("witness row p = 3*2^41+1 = %d,  log2 p = %.6f,  e = %d,  log2 Q = %.6f" %
      (p_w, math.log2(p_w), e_w, e_w * math.log2(p_w)))
print("B* = %d = 2^%.4f" % (Bstar, log2big(Bstar)))
print()
print("SIGMA(N=L, kappa, p) := L - kappa*log2 p   (log2 of the heuristic ternary theta mass above 1)")
print("%4s %6s | %14s %14s %14s" % ("v", "L", "e=6 witness", "e=1 p=2^128", "e=1 p=2^129.585"))
for v in [34, 35, 36, 37, 38, 39]:
    L = 2 ** (41 - v)
    print("%4d %6d | %14.3f %14.3f %14.3f" %
          (v, L, L - e_w * math.log2(p_w), L - 128.0, L - 129.5849625))
check("Q7 SIGMA(v=35, e=6 witness) = -191.5 +- 0.2",
      abs((64 - e_w * math.log2(p_w)) - (-191.5)) < 0.2,
      "%.4f" % (64 - e_w * math.log2(p_w)))
check("Q7 SIGMA < 0 at every official row (v in 34..39, log2 p >= 128)",
      all(2 ** (41 - v) - 128.0 < 0 for v in range(34, 40)),
      "max = %.4f at v=34" % max(2 ** (41 - v) - 128.0 for v in range(34, 40)))
print()
print("U1/U2 vs B* at v=35 (L=64, 2L=128, r'=62):")
U1 = comb(128, 62); U2 = (comb(128, 62) + comb(64, 31)) // 128
print("  C(128,62) = %d = 2^%.4f      (margin vs B*: %+.4f bits)" % (U1, log2big(U1), log2big(Bstar) - log2big(U1)))
print("  M(128,62) = %d = 2^%.4f      (margin vs B*: %+.4f bits)" % (U2, log2big(U2), log2big(Bstar) - log2big(U2)))
print("  C(64,31)  = %d = 2^%.4f   (= |X^struct|, the eps=0 fibre)" % (comb(64, 31), log2big(comb(64, 31))))
check("H4: the TRIVIAL ternary bound TMASS<=2^L already puts U1 = C(2L,r') below B*",
      U1 < Bstar, "C(128,62)=2^%.4f < B*=2^%.4f, margin %+.4f bits" %
      (log2big(U1), log2big(Bstar), log2big(Bstar) - log2big(U1)))
print()
print("THEOREM CW-FLOOR: |X_r'| >= C(L,r'/2)^2 / p^delta_a  (r' even) -- a LOWER bound")
for v, dl in [(34, 1), (35, 1)]:
    L = 2 ** (41 - v); rp = L - 2
    cw = log2big(comb(L, rp // 2)) * 2 - dl * math.log2(p_w)
    print("  v=%d L=%3d: C(L,r'/2)=2^%.4f  ->  CW-FLOOR = 2^%.4f  (witness row, delta_a=%d)" %
          (v, L, log2big(comb(L, rp // 2)), cw, dl))
c128 = log2big(comb(128, 63))
print("  banked 'PROVED 2^205.71' reconstruction, v=34: 2*log2 C(128,63) - log2 p = %.4f" %
      (2 * c128 - math.log2(p_w)))
check("CW-FLOOR witness-row value 2^205.71 reproduced", abs((2 * c128 - math.log2(p_w)) - 205.71) < 0.02,
      "%.4f" % (2 * c128 - math.log2(p_w)))
print("  banked 'vacuous at every prime row by 3.85 bits' reconstruction:")
print("     log2 C(128,63) = %.4f ; 128 - that = %.4f ; 129.5849625 - that = %.4f" %
      (c128, 128 - c128, 129.5849625 - c128))
check("Q8 3.85 reconstructed as log2 p = 128 minus log2 C(128,63)", abs((128 - c128) - 3.85) < 0.02,
      "%.4f (my PREREG guessed v=35 / witness p -- MIS-REGISTERED, see report)" % (128 - c128))
print()
print("Precision tolerances, side by side:")
print("  M2 : proved floor 2^17.98 ; finite target Z(L) <= 1+N^3 = 2^22.75 ; tolerance = %.2f bits" % (22.75 - 17.98))
print("  M4 : proved floor 2^73.061 ; budget B* = 2^%.4f ; tolerance = %.2f bits" %
      (log2big(Bstar), log2big(Bstar) - 73.061))
print()
print("=" * 100)
print("TOTAL: %d PASS / %d FAIL" % (PASS, FAIL))
print("=" * 100)
sys.exit(1 if FAIL else 0)
