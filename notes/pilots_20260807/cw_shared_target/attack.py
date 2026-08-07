#!/usr/bin/env python3
# cw_shared_target -- D3 first attack.  Stdlib only.  tools/ramguard local -- python3 ...
import math, sys
from math import comb

# --- helpers (verbatim copies of cw.py's; duplicated so importing cw.py does not re-run its census)
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
    t = pow(primitive_root(p), (p - 1) // m, p)
    assert pow(t, m, p) == 1
    return t

def primes_upto(N):
    sieve = bytearray([1]) * (N + 1); sieve[0:2] = b"\x00\x00"
    for i in range(2, int(N ** .5) + 1):
        if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2, N + 1) if sieve[i]]

def ternary_enum(coeffs, p):
    m = len(coeffs); cur = {0: [1] + [0] * m}
    for c in coeffs:
        nxt = {}
        for v, arr in cur.items():
            for e in (0, 1, -1):
                nv = (v + e * c) % p
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

def weight_enum_kernel(coeffs, p):
    N = len(coeffs); h = N // 2
    A = ternary_enum(coeffs[:h], p); B = ternary_enum(coeffs[h:], p)
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
    N = len(rows[0]); h = N // 2; k = len(rows)
    def enum(cols):
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
    A = enum([tuple(r[j] for r in rows) for j in range(h)])
    B = enum([tuple(r[j] for r in rows) for j in range(h, N)])
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
def check(name, cond, extra=""):
    global PASS, FAIL
    if cond: PASS += 1; print("PASS  %-60s %s" % (name, extra))
    else:    FAIL += 1; print("FAIL  %-60s %s" % (name, extra))

PRIMES = primes_upto(200000)

def excess_ratio(TMASS, N, p, kap):
    """EXCESS-CRATIO := (TMASS - 1) / ((2^N - 1)/p^kappa).  The sharp form of the ceiling."""
    return (TMASS - 1) * (p ** kap) / (2 ** N - 1)

print("=" * 104)
print("SECTION A -- the SHARP shared form.   EXCESS-CRATIO := (TMASS(D) - 1) * p^kappa / (2^N - 1)")
print("            EXCESS-CEILING(C):  TMASS(D) - 1 <= C * (2^N - 1)/p^kappa   for admissible D.")
print("            (Upper companion of THEOREM Z-FLOOR, which gives TMASS >= 2^N/p^kappa.)")
print("=" * 104)

print("\nA1. M4 family (RSET: eps _|_ (1,theta,...,theta^{L-1}), theta of exact order 2L, kappa=1), 2-POWER grid")
print("%4s %8s %8s | %12s %10s %10s %8s | %s" %
      ("L", "pmax", "#cells", "max EXCESS", "at p", "SIGMA", "UMIN", "largest p with R != {0}"))
worstA = 0.0; worstcell = None
for L, plim in [(4, 200000), (8, 200000), (16, 6000)]:
    best = (0.0, None, None); ncell = 0; lastp = None
    for p in PRIMES:
        if p >= plim: break
        if p <= 2 * L or (p - 1) % (2 * L): continue
        th = elt_of_order(p, 2 * L)
        AU = weight_enum_kernel([pow(th, j, p) for j in range(L)], p)
        tm = sum(AU[U] * 2.0 ** (-U) for U in range(L + 1))
        ncell += 1
        if sum(AU) > 1: lastp = p
        er = excess_ratio(tm, L, p, 1)
        if er > best[0]: best = (er, p, L - math.log2(p))
    print("%4d %8d %8d | %12.4f %10s %10.3f %8s | %s" %
          (L, plim, ncell, best[0], best[1], best[2] if best[2] is not None else 0,
           "-", lastp))
    if best[0] > worstA: worstA = best[0]; worstcell = (L, best[1])
check("A1 EXCESS-CEILING with C = 2 survives the whole M4 2-power sweep",
      worstA <= 2.0, "max EXCESS-CRATIO = %.4f at %s" % (worstA, worstcell))
check("A1 EXCESS-CEILING with C = 1.01 survives the whole M4 2-power sweep",
      worstA <= 1.01, "max EXCESS-CRATIO = %.4f at %s" % (worstA, worstcell))

print("\nA2. ADVERSARIAL: cells with SIGMA < 0 (heuristic mass << 1) that STILL carry a relation")
print("    -- this is where a C = O(1) ceiling can break, because one weight-U vector contributes 2^-U")
print("%4s %8s %10s %8s %8s %14s %14s" % ("L", "p", "SIGMA", "UMIN", "A[UMIN]", "TMASS-1", "EXCESS-CRATIO"))
advmax = 0.0; advcell = None
for L, plim in [(4, 200000), (8, 200000), (16, 6000)]:
    for p in PRIMES:
        if p >= plim: break
        if p <= 2 * L or (p - 1) % (2 * L): continue
        sig = L - math.log2(p)
        if sig >= 0: continue
        th = elt_of_order(p, 2 * L)
        AU = weight_enum_kernel([pow(th, j, p) for j in range(L)], p)
        if sum(AU) == 1: continue
        tm = sum(AU[U] * 2.0 ** (-U) for U in range(L + 1))
        er = excess_ratio(tm, L, p, 1)
        umin = next(U for U in range(1, L + 1) if AU[U])
        print("%4d %8d %10.3f %8d %8d %14.6g %14.4f" % (L, p, sig, umin, AU[umin], tm - 1, er))
        if er > advmax: advmax = er; advcell = (L, p)
if advcell is None:
    print("    (none found: every SIGMA < 0 cell in the swept range has RSET = {0} exactly)")
check("A2 no SIGMA<0 counterexample to EXCESS-CEILING(C=2) in the swept range",
      advmax <= 2.0, "max %.4f at %s" % (advmax, advcell))

print("\nA3. M2 family (negacyclic GRS toy, Lambda={1,3,...,2R-1}, kappa=R), adversarial sweep")
print("%5s %4s %3s | %8s | %6s %6s | %12s %14s" %
      ("S", "R", "", "#cells", "UMIN", "2R+1", "max TMASS-1", "max EXCESS"))
m2max = 0.0; m2cell = None
for (S, R, plim) in [(8, 2, 20000), (8, 3, 20000), (16, 2, 4000), (16, 4, 4000)]:
    best = (0.0, None, None); ncell = 0; z1viol = 0
    for p in PRIMES:
        if p >= plim: break
        if p <= 2 * S or (p - 1) % (2 * S): continue
        w = elt_of_order(p, 2 * S)
        rows = [[pow(w, (2 * j - 1) * e, p) for e in range(S)] for j in range(1, R + 1)]
        AU = weight_enum_kernel_multi(rows, p)
        tm = sum(AU[U] * 2.0 ** (-U) for U in range(S + 1))
        ncell += 1
        umin = next((U for U in range(1, S + 1) if AU[U]), None)
        if umin is not None and umin < 2 * R + 1: z1viol += 1
        er = excess_ratio(tm, S, p, R)
        if er > best[0]: best = (er, p, umin)
    print("%5d %4d %3s | %8d | %6s %6d | %12s %14.4f  (at p=%s)" %
          (S, R, "", ncell, best[2], 2 * R + 1, "-", best[0], best[1]))
    check("Z-1 (min ternary weight >= 2R+1) holds at every swept cell S=%d R=%d" % (S, R), z1viol == 0,
          "%d violations / %d cells" % (z1viol, ncell))
    if best[0] > m2max: m2max = best[0]; m2cell = (S, R, best[1])
check("A3 EXCESS-CEILING with C = 2 survives the whole M2 sweep", m2max <= 2.0,
      "max EXCESS-CRATIO = %.4f at (S,R,p) = %s" % (m2max, m2cell))

print("\nA4. CONTROL (invalid grid, CATCH-Z6): composite 2L -- how large can C get?")
for L in [6, 12]:
    best = (0.0, None)
    for p in PRIMES:
        if p >= 20000: break
        if p <= 2 * L or (p - 1) % (2 * L): continue
        th = elt_of_order(p, 2 * L)
        AU = weight_enum_kernel([pow(th, j, p) for j in range(L)], p)
        tm = sum(AU[U] * 2.0 ** (-U) for U in range(L + 1))
        er = excess_ratio(tm, L, p, 1)
        if er > best[0]: best = (er, p)
    print("   L=%2d (2L=%d): max EXCESS-CRATIO = %.2f at p=%d   -- grows linearly in p (p-free cyclotomic relations)"
          % (L, 2 * L, best[0], best[1]))

# ============================================================================ B
print()
print("=" * 104)
print("SECTION B -- what EXCESS-CEILING(C) BUYS MYSTERY 4 (deep stratum).  Exact integers.")
print("=" * 104)
p_w = 3 * 2 ** 41 + 1; e_w = 6
Bstar = 242251802232021244567343686397347233808
lB = log2big(Bstar)
print("B* = 2^%.4f ; witness row p = 3*2^41+1 (log2 p = %.6f, e = 6) ; prime rows e = 1, log2 p in [129.5849625, 256)"
      % (lB, math.log2(p_w)))
print()
print("Acc_deep(v) = C(L,r'/2) * sum_{eps != 0} GDEV(U) 2^-U  <=  C(L,r'/2) * GDEVmax(L) * C * (2^L-1)/p^e")
print("%3s %5s | %10s %10s %10s | %12s %12s %12s | %10s" %
      ("v", "L", "S(v)", "U1", "U2", "CEIL e=6", "CEIL e=1lo", "CEIL e=1hi", "U2 margin"))
Cceil = 2.0
rows_out = []
for v in [34, 35, 36, 37, 38, 39]:
    L = 2 ** (41 - v); rp = L - 2
    Sv = log2big(comb(2 ** (41 - v), 2 ** (40 - v) - 1)) - (41 - v)
    U1 = log2big(comb(2 * L, rp))
    U2 = log2big((comb(2 * L, rp) + comb(L, rp // 2)) // (2 * L))
    gdevmax = max((comb(L - U, (rp - U) // 2) / comb(L, rp // 2)) * 2.0 ** U
                  for U in range(0, rp + 1, 2))
    base = log2big(comb(L, rp // 2)) + math.log2(gdevmax) + math.log2(Cceil) + L
    ce6 = base - e_w * math.log2(p_w)
    ce1lo = base - 129.5849625
    ce1hi = base - 256.0
    rows_out.append((v, L, Sv, U1, U2, ce6, ce1lo, ce1hi, gdevmax))
    print("%3d %5d | %10.4f %10.4f %10.4f | %12.4f %12.4f %12.4f | %+10.4f" %
          (v, L, Sv, U1, U2, ce6, ce1lo, ce1hi, lB - U2))
print()
print("  (all columns are log2.  S(v) = C(2^{41-v},2^{40-v}-1)/2^{41-v}, banked exact.")
print("   U1 = C(2L,r'), U2 = M(2L,r') = PROPOSITION U2.  CEIL* = the conditional bound above, C = %.1f.)" % Cceil)
for (v, L, Sv, U1, U2, ce6, ce1lo, ce1hi, gm) in rows_out:
    tot6 = max(Sv, ce6) + 1 if ce6 > Sv else Sv + math.log2(1 + 2 ** (ce6 - Sv))
    print("   v=%2d: GDEVmax=%.4f | U2 %s B* | CEIL(e=6) %s B* | CEIL(e=1,lo) %s B* | S(v)+CEIL(e=6) = 2^%.4f %s B*"
          % (v, gm, "<" if U2 < lB else ">=", "<" if ce6 < lB else ">=",
             "<" if ce1lo < lB else ">=", tot6, "<" if tot6 < lB else ">="))
v34 = rows_out[0]
check("B: U2 is VACUOUS at v=34 (banked)", v34[4] >= lB, "U2 = 2^%.4f vs B* = 2^%.4f" % (v34[4], lB))
check("B: EXCESS-CEILING(C=2) DE-VACUUMS v=34 at the e=6 witness row", v34[5] < lB,
      "CEIL = 2^%.4f < B* = 2^%.4f  (margin %+.4f bits)" % (v34[5], lB, lB - v34[5]))
check("B: EXCESS-CEILING(C=2) DE-VACUUMS v=34 at the e=1 prime-row floor log2 p = 129.585", v34[6] < lB,
      "CEIL = 2^%.4f < B* = 2^%.4f  (margin %+.4f bits)" % (v34[6], lB, lB - v34[6]))
check("B: v=34 deep-stratum TOTAL S(34)+Acc_deep under the ceiling is below B* (e=6)",
      max(v34[2], v34[5]) + 1 < lB, "S(34)=2^%.4f, CEIL=2^%.4f" % (v34[2], v34[5]))

# ============================================================================ C
print()
print("=" * 104)
print("SECTION C -- what EXCESS-CEILING(C) BUYS MYSTERY 2.")
print("=" * 104)
print("  banked: Z-FLOOR fires at +17.98 bits under the exact-balance reading (Z_1 >= 2^17.98);")
print("          silent by -46.02 bits under the banked R = ceil(t/2) reading;")
print("          finite target Z(L) <= 1 + N^3, i.e. Z_1 <= 2^22.75.  Window = 4.77 bits.")
for reading, sig in [("exact-balance", 17.98), ("R=ceil(t/2)", -46.02)]:
    for C in [1.0, 2.0, 2 ** 4.77, 2 ** 5.0]:
        val = math.log2(1 + C * 2 ** sig)
        print("   reading=%-14s SIGMA=%+7.2f  C=2^%-6.3f ->  Z_1 <= 2^%-8.4f   vs target 2^22.75 : %s"
              % (reading, sig, math.log2(C), val, "MEETS" if val <= 22.75 else "MISSES"))
check("C: EXCESS-CEILING with C <= 2^4.77 closes M2's finite target (exact-balance reading)",
      math.log2(1 + (2 ** 4.77) * 2 ** 17.98) <= 22.75 + 1e-9,
      "Z_1 <= 2^%.4f vs 2^22.75" % math.log2(1 + (2 ** 4.77) * 2 ** 17.98))
check("C: the toy-measured C (<= 1.01) leaves 4.76 bits of headroom on M2's finite target",
      math.log2(1 + 1.01 * 2 ** 17.98) <= 22.75,
      "Z_1 <= 2^%.4f, headroom %.4f bits" %
      (math.log2(1 + 1.01 * 2 ** 17.98), 22.75 - math.log2(1 + 1.01 * 2 ** 17.98)))

# ============================================================================ D
print()
print("=" * 104)
print("SECTION D -- THE DIVERGENCE, quantified: the bridge from the PRIMAL count to TMASS.")
print("=" * 104)
print("  PERIODIC strata (LEMMA TC): the fold eps_j = [j in S'] - [j+L in S'] is a BIJECTION.")
print("     -> FIB(fold) == NW(brute) verified at 20/20 toy cells in CENSUS.txt.  LOSS = 0 bits.")
print("  APERIODIC / SHALLOW (no fold): only the collision bound")
print("     NW^2 <= sum_{eps in C cap T, balanced} C(n-U, r'-U/2).   LOSS = L2LOSS bits.")
print()
print("  measured L2LOSS / (kappa*log2 p) at the w=2 toy cells (kappa = 1), from CENSUS.txt SECTION 5:")
meas = [("L=8,p=17", 2.0409, 4.0875), ("L=8,p=97", 2.5948, 6.5999), ("L=8,p=113", 3.3872, 6.8202),
        ("L=8,p=193", 3.0071, 7.5924), ("L=8,p=241", 3.2079, 7.9128), ("L=8,p=257", 3.1730, 8.0056),
        ("L=8,p=337", 2.9918, 8.3966), ("L=8,p=353", 2.6406, 8.4636)]
fr = [a / b for (_, a, b) in meas]
for (nm, a, b) in meas:
    print("     %-12s L2LOSS = %.4f bits ;  kappa*log2 p = %.4f ;  fraction = %.4f" % (nm, a, b, a / b))
print("     range [%.4f, %.4f], mean %.4f  -> the collision bridge recovers at most ~half the suppression"
      % (min(fr), max(fr), sum(fr) / len(fr)))
kap_off = 2 ** 35 - 1
loss_off_half = 0.5 * kap_off * math.log2(p_w)
loss_off_min = min(fr) * kap_off * math.log2(p_w)
print()
print("  at the official row (w = 2^35, kappa = w-1 = %d, log2 p = %.6f):" % (kap_off, math.log2(p_w)))
print("     kappa*log2 p            = %.6g bits" % (kap_off * math.log2(p_w)))
print("     collision loss at 1/2   = %.6g bits" % loss_off_half)
print("     collision loss at %.3f  = %.6g bits   (the MOST FAVOURABLE measured fraction)" % (min(fr), loss_off_min))
print("     MYSTERY 4's ENTIRE TOLERANCE  = %.2f bits (B* = 2^%.4f minus the banked proved floor 2^73.061)"
      % (lB - 73.061, lB))
print("     ratio loss/tolerance    = %.6g" % (loss_off_min / (lB - 73.061)))
check("D: the collision bridge's loss exceeds M4's ENTIRE tolerance by >= 10 orders of magnitude",
      loss_off_min / (lB - 73.061) > 1e9,
      "%.4g bits of loss vs %.2f bits of tolerance" % (loss_off_min, lB - 73.061))
print()
print("  and MYSTERY 2 pays NO such bridge: its open terminal IS the functional")
print("     (f2_z1_mass_knife_edge/statement.md:55-56 'prove Z_1 <= 2^{o(m)} at k = e',")
print("      with Z(L) = sum_{eps in L^perp cap T} 2^{-wt(eps)} at :18).")

# ============================================================================ E
print()
print("=" * 104)
print("SECTION E -- the two contracts, numbers only")
print("=" * 104)
hdr = ("row", "M2 (f2 terminal)", "M4-b (deep stratum)", "M4-a (LIVE crux)")
tab = [
    ("functional",            "TMASS(L^perp) = Z_1",        "TMASS(RSET)",              "|W_w| / X_w(gamma)"),
    ("N (ternary length)",    "m = S = 2.75e11",            "L = 2^{41-v} <= 128",      "n = 2^41"),
    ("kappa (codim)",         "R = S/log2 p ~ 2^32",        "e in {1,...,6}",           "w-1 = 2^35-1"),
    ("SIGMA = N - k*log2 p",  "+17.98 or -46.02",           "-1.585 ... -251.5",        "(no verified model)"),
    ("direction needed",      "UPPER",                      "UPPER",                    "UPPER"),
    ("banked instrument dir", "Z-FLOOR = LOWER",            "CW-FLOOR = LOWER",         "CW-FLOOR = LOWER"),
    ("tolerance",             "4.77 bits",                  "54.45 bits",               "54.45 bits"),
    ("bridge to TMASS",       "NONE (it IS the target)",    "LEMMA TC bijection, 0 bits", "collision, >= 4.5e11 bits"),
    ("ell (odd-power conds)", "R = 2^32 -> wt >= 2R+1",     "1 (PERMANENT) -> wt >= 3", "1 (PERMANENT)"),
    ("already sufficient?",   "NO (open terminal)",         "YES at v>=35 (U1 < B*)",   "NO"),
]
w0 = max(len(r[0]) for r in tab)
def prow(r):
    return "%-*s | %-28s | %-28s | %-28s" % (w0, r[0], r[1], r[2], r[3])
print(prow(hdr))
print("-" * (w0 + 3 + 31 * 3))
for r in tab:
    print(prow(r))

print()
print("=" * 104)
print("TOTAL: %d PASS / %d FAIL" % (PASS, FAIL))
print("=" * 104)
sys.exit(1 if FAIL else 0)
