#!/usr/bin/env python3
"""
verify.py -- the t/q pin (round 16, pilot f2_tq_pin).

Self-contained, stdlib only, FAIL-CLOSED: every check appends to a global
ledger; any FAIL (or any uncaught exception) exits nonzero.

Run from repo root:
    tools/ramguard tiny -- python3 notes/pilots_20260806/f2_tq_pin/verify.py

Sources for every pinned input are quoted verbatim in PROOFS.md with
file:line.  Nothing here reads the repo; all inputs are literals so the
script is replayable in isolation.
"""

import sys
from math import lgamma, log2, log

LOG2E = 1.0 / log(2.0)
LEDGER = []


def check(tag, ok, msg):
    LEDGER.append((tag, bool(ok), msg))
    print(("  [PASS] " if ok else "  [FAIL] ") + tag + " " + msg)
    return bool(ok)


def log2binom(n, j):
    """log2 C(n, j) via lgamma.  n ~ 2^41: lgamma ~ 6e13, double relative
    error 1e-16 => absolute error ~ 0.03 bits, negligible against the
    L ~ 256-bit step of the corridor function (see xr_radius_arithmetic
    proof.md:49-51)."""
    if j < 0 or j > n:
        return float("-inf")
    return (lgamma(n + 1.0) - lgamma(j + 1.0) - lgamma(n - j + 1.0)) * LOG2E


# ---------------------------------------------------------------------------
# RULES-LEVEL CONSTANTS (critical/nodes/rules_freeze/statement.md:9,
#                        critical/nodes/field_cap_check/statement.md:13)
# ---------------------------------------------------------------------------
K_CAP = 1 << 40          # k <= 2^40
FIELD_CAP_BITS = 256     # |F| < 2^256
EPS_BITS = 128           # eps* = 2^-128
RATES = [(1, 2), (1, 4), (1, 8), (1, 16)]

# KoalaBear tower constants (notes/pilots_20260802/f2_deployed_windows/
# tower.py:11-18; REPORT.md:17)
P_KB = 2**31 - 2**24 + 1
LOG2P_BANKED = 30.988685   # f2_sl1_powersums/PROOFS.md:384


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def is_prime(n):
    """Deterministic Miller-Rabin for n < 3.3e24 (covers n < 2^64)."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
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


def t_star(L, n, num, den):
    """Corridor edge, xr_radius_arithmetic/proof.md:41-43:
       t* = min { t : t*L >= log2 C(n, n-k-t) + 128 }."""
    k = n * num // den
    def f(t):
        return t * L - log2binom(n, n - k - t) - EPS_BITS
    lo, hi = 1, n - k
    if f(hi) < 0:
        return None
    while lo < hi:
        mid = (lo + hi) // 2
        if f(mid) >= 0:
            hi = mid
        else:
            lo = mid + 1
    return lo


print("=" * 74)
print("S1  KoalaBear tower constants (the row of record in the F2 lane)")
print("=" * 74)
check("S1.1", P_KB == 2130706433, "p = 2^31-2^24+1 = %d" % P_KB)
check("S1.2", is_prime(P_KB), "p is prime")
check("S1.3", P_KB - 1 == 2**24 * 127,
      "p-1 = 2^24 * 127 exactly (v_2 = %d)" % v2(P_KB - 1))
check("S1.4", abs(log2(P_KB) - LOG2P_BANKED) < 1e-6,
      "log2 p = %.6f reproduces the banked 30.988685" % log2(P_KB))
# ord_{2^40}(p) = 2^16  (F2_CAMPAIGN_LOG.md:2159)
ordp = 1
x = P_KB % (1 << 40)
while x != 1:
    x = x * P_KB % (1 << 40)
    ordp += 1
check("S1.5", ordp == 2**16, "ord_{2^40}(p) = 2^%d (banked: 2^16)" % v2(ordp))

print()
print("=" * 74)
print("S2  (Q1) THE FIELD-CAP TEST -- is the 16-rung tower prize-admissible?")
print("=" * 74)
lp = log2(P_KB)
worst_ok_j = None
for j in range(0, 18):
    Lj = (2**j) * lp
    ok = Lj < FIELD_CAP_BITS
    if ok:
        worst_ok_j = j
print("  rung j : log2 q_j = 2^j * log2 p   vs cap 256")
for j in (1, 2, 3, 4, 8, 16):
    Lj = (2**j) * lp
    print("     j=%2d : log2 q_j = %18.3f   %s" %
          (j, Lj, "ADMISSIBLE" if Lj < FIELD_CAP_BITS else "OVER CAP"))
check("S2.1", worst_ok_j == 3,
      "largest admissible rung is j = 3 (q_3 = p^8, log2 q_3 = %.3f < 256)"
      % (8 * lp))
check("S2.2", (2**4) * lp >= FIELD_CAP_BITS,
      "rung 4 already breaks |F| < 2^256 (log2 q_4 = %.1f)" % (16 * lp))
L16 = (2**16) * lp
check("S2.3", L16 > 2_000_000,
      "rung 16: log2 q_16 = %.0f bits, i.e. %.0fx the cap IN BITS"
      % (L16, L16 / FIELD_CAP_BITS))
check("S2.4", (2**16) * lp > FIELD_CAP_BITS,
      "=> Q1 CONFIRMED: rungs 4..16 are NOT prize-admissible rows")

print()
print("=" * 74)
print("S3  (Q3) admissible (p, e) at the maximal rate-1/2 row n = 2^41")
print("=" * 74)
# n | q-1 with n = 2^41 => v_2(p^e - 1) >= 41.
# LTE: e = 2^s * u, u odd =>
#   s = 0 : v_2(p^e-1) = v_2(p-1)
#   s >= 1: v_2(p^e-1) = v_2(p-1) + v_2(p+1) + s - 1
# and exactly one of v_2(p-1), v_2(p+1) equals 1 (p odd).
NBITS = 41
adm = []
for s in range(0, 12):
    # minimal log2 p forced by the valuation requirement
    if s == 0:
        min_log2p = NBITS               # v_2(p-1) >= 41
    else:
        min_log2p = NBITS - s           # max(v2(p-1),v2(p+1)) >= 41-s
    u = 1
    while True:
        e = (2**s) * u
        if e * min_log2p >= FIELD_CAP_BITS:
            break
        adm.append((s, u, e, min_log2p))
        u += 2
    if s >= 1 and (2**s) * min_log2p >= FIELD_CAP_BITS:
        # no odd multiplier can help either; and larger s is worse
        pass
smax = max(a[0] for a in adm)
emax = max(a[2] for a in adm)
minp = min(a[3] for a in adm)
print("  admissible (s = v_2(e), e, min log2 p):")
for (s, u, e, mp) in sorted(adm, key=lambda z: z[2]):
    print("     e = %d (s=%d)  requires log2 p >= %d, log2 q >= %d"
          % (e, s, mp, e * mp))
check("S3.1", smax == 2, "v_2(extension degree) <= 2 (found max %d)" % smax)
check("S3.2", emax == 6, "extension degree e <= 6 (found max %d)" % emax)
check("S3.3", minp == 39, "log2 p >= 39 at every admissible row (min %d)" % minp)
check("S3.4", minp > 31,
      "=> the KoalaBear log2 p ~ 31 base field is INADMISSIBLE at n = 2^41")
# tower depth = log2 ord_n(p); ord_n(p) is a 2-power dividing e <= 6
check("S3.5", 2**2 <= emax and 2**3 > emax,
      "ord_n(p) in {1,2,4} => tower depth <= 2 rungs, not 16")
# explicit witness that s=3 is impossible
check("S3.6", (2**3) * (NBITS - 3) > FIELD_CAP_BITS,
      "s=3 needs log2 q >= 8*38 = %d > 256 -- excluded" % (8 * 38))

print()
print("=" * 74)
print("S4  An EXPLICIT prize-admissible maximal rate-1/2 row (existence)")
print("=" * 74)
found = None
c = (1 << 25) - 1
while c > 0 and found is None:
    if c % 2 == 1:
        cand = c * (1 << 39) + 1
        if cand < (1 << 64) and is_prime(cand):
            found = cand
    c -= 1
check("S4.1", found is not None, "found p = %s" % found)
p = found
check("S4.2", v2(p - 1) == 39, "v_2(p-1) = %d (exactly 39)" % v2(p - 1))
q_ex = p**4
check("S4.3", (q_ex - 1) % (1 << 41) == 0,
      "n = 2^41 divides q-1 for q = p^4  (v_2(q-1) = %d)" % v2(q_ex - 1))
check("S4.4", q_ex < (1 << FIELD_CAP_BITS),
      "q = p^4 < 2^256: log2 q = %.4f" % log2(q_ex))
check("S4.5", log2(p) >= 39.0, "log2 p = %.4f >= 39" % log2(p))
# ord_{2^41}(p)
o = 1
x = p % (1 << 41)
while x != 1:
    x = x * p % (1 << 41)
    o += 1
check("S4.6", o == 4, "ord_{2^41}(p) = %d => exactly 2 moving rungs" % o)
L_exhibit = log2(q_ex)

print()
print("=" * 74)
print("S5  Reproduce the banked corridor table t*(L=255.9), n=2^41 [xr]")
print("=" * 74)
TARGET = {2: 8592912739, 4: 7014660390, 8: 4722556392, 16: 2943177800}
n41 = 1 << 41
allok = True
for den, want in TARGET.items():
    got = t_star(255.9, n41, 1, den)
    ok = (got == want)
    allok = allok and ok
    print("     rate 1/%-2d : t* = %d  (banked %d) %s"
          % (den, got, want, "OK" if ok else "MISMATCH"))
check("S5.1", allok, "all four t* reproduce xr_radius_arithmetic proof.md:53-58")
TSTAR = TARGET[2]

print()
print("=" * 74)
print("S6  (Q2) the window-bits product, and what it is really equal to")
print("=" * 74)
prod = TSTAR * 255.9
check("S6.1", abs(prod / n41 - 1.0) < 5e-4,
      "t* * log2 q = %.6e equals n = 2^41 = %.6e to %.4f%%"
      % (prod, float(n41), abs(prod / n41 - 1.0) * 100))
check("S6.2", abs(prod - 2.15e12) / 2.15e12 > 0.02,
      "the banked literal 2.15e12 is %.2f%% BELOW the true product"
      % ((prod - 2.15e12) / prod * 100))
lc = log2binom(n41, 2**40 - TSTAR)
check("S6.3", (n41 - lc) / n41 < 1e-3,
      "log2 C(n, n-k-t*) = %.6e is %.4f%% below n -- the counting balance is "
      "tight to 5e-3%%, NOT to '~2%%'" % (lc, (n41 - lc) / n41 * 100))
# t = 7e10 would need log2 q = 31.4  -- but n | q-1 forces q > n
implied_L = n41 / 7e10
check("S6.4", implied_L < 41.0,
      "t = 7e10 implies log2 q = %.3f, but n | q-1 forces log2 q > 41"
      % implied_L)
t_upper = n41 / 41.0
t_lower = n41 / 256.0
check("S6.5", t_lower < TSTAR <= t_upper,
      "t* = %d lies INSIDE the rules-forced interval (%.4e, %.4e]"
      % (TSTAR, t_lower, t_upper))
check("S6.6", 7e10 > t_upper,
      "t = 7e10 lies OUTSIDE it (upper limit %.4e) -- excluded by the rules"
      % t_upper)
# base-field variant of the same bound (falsifier F-Q2b: report it too)
t_upper_base = n41 / 39.0
check("S6.7", 7e10 > t_upper_base,
      "even the BASE-FIELD reading caps t at n/39 = %.4e < 7e10"
      % t_upper_base)
check("S6.8", 7e10 <= n41 / LOG2P_BANKED,
      "7e10 is recovered only by dividing by log2 p = 30.99 (n/log2 p = %.4e)"
      % (n41 / LOG2P_BANKED))

print()
print("=" * 74)
print("S7  (Q5) the [255.9113, 256) sliver")
print("=" * 74)
T33 = 1 << 33
# --- (Q5) AS PRE-REGISTERED: I predicted the sliver = {L : t*(L) <= 2^33},
#     i.e. the FM+gate crossing (T*).  THIS PREDICTION IS FALSIFIED. ---
L_fm = (log2binom(n41, 2**40 - T33) + EPS_BITS) / T33
print("     Q5 as registered: min L with t*(L) <= 2^33 = %.6f" % L_fm)
check("S7.1", abs(L_fm - 255.9113) > 0.01,
      "Q5 FALSIFIED: the FM/gate endpoint is %.4f, NOT the banked 255.9113 "
      "(off by %.4f bits)" % (L_fm, abs(L_fm - 255.9113)))
check("S7.2", t_star(L_fm + 1e-6, n41, 1, 2) <= T33,
      "the FM/gate endpoint IS a genuine crossing of t*(L)=2^33 (sanity)")
check("S7.3", t_star(L_fm - 1e-3, n41, 1, 2) > T33,
      "...and t*(L) > 2^33 just below it -- so 255.9887 is a real quantity, "
      "simply not the one TARGET_3C_EXTRACTION.md:29-30 reports")
# --- THE TRUE FORMULA, identified after the falsification ---
# u2c_giant_tnull_dichotomy/node.json:8 ties the sliver to the aspect guard
# Q^41 < N^256 / the first-moment counting balance, not to (T*).
L_count = n41 / TSTAR
print("     TRUE formula: n / t* = %.6f" % L_count)
check("S7.4", abs(L_count - 255.9113) < 1e-4,
      "the sliver's left endpoint is exactly n/t* = %.4f = the banked 255.9113"
      % L_count)
check("S7.5", abs((FIELD_CAP_BITS - L_count) - 0.0887) < 2e-4,
      "sliver width = 256 - n/t* = %.4f bits (banked 0.089)"
      % (FIELD_CAP_BITS - L_count))
check("S7.6", abs(TSTAR * L_count - n41) / n41 < 1e-9,
      "=> the sliver is the PURE COUNTING/EMPTINESS balance t*.L >= n "
      "(q^t > 2^n), NOT the FM+gate condition (T*)")
# the convention point at which t* was computed fails its own sliver
check("S7.7", TSTAR * 255.9 < n41,
      "CATCH: at the L = 255.9 convention (xr proof.md:33) t*.L = %.6e < n = "
      "%.6e -- the convention point lies BELOW its own sliver's left endpoint"
      % (TSTAR * 255.9, float(n41)))
check("S7.8", L_exhibit > L_count,
      "the explicit admissible row S4 (log2 q = %.4f) lies INSIDE the sliver; "
      "its corridor edge is t* = %d" % (L_exhibit, t_star(L_exhibit, n41, 1, 2)))

print()
print("=" * 74)
print("S8  (Q4) the m_j ladder -- both readings")
print("=" * 74)
# new-part  m_j = (n_j - n_{j-1})/2 = 2^{22+j}   (tower.py:18)
# nested    m_j = n_j / 2       = 2^{23+j}
mnew = {j: 2**(22 + j) for j in range(1, 17)}
mnest = {j: 2**(23 + j) for j in range(1, 17)}
for j in range(1, 17):
    nj, njm1 = 2**(24 + j), 2**(23 + j)
    assert (nj - njm1) // 2 == mnew[j]
    assert nj // 2 == mnest[j]
check("S8.1", mnew[16] == 2**38, "new-part m_16 = (n_16-n_15)/2 = 2^38")
check("S8.2", mnest[16] == 2**39, "nested   m_16 = n_16/2      = 2^39")
check("S8.3", mnest[16] == 2 * mnew[16],
      "the 2^38-vs-2^39 conflict is EXACTLY the 2x nested/new-part ambiguity "
      "of f2_deployed_windows/REPORT.md:69 -- not an arithmetic error")
check("S8.4", 2**(24 + 16) == 2**40 and 2**40 // 2 == 2**39,
      "PREREG.json:58's m = 2^39 = n_16/2, consistent with its own "
      "'dim L >= n/(2 log2 p)' wording (:57)")

print()
print("=" * 74)
print("S9  (P5) LEMMA 3  t >= m_j / log2 p  at EVERY rung, every reading")
print("=" * 74)
CANDS = [("7e10  (verify.py:958,1038 literal)", 7e10),
         ("2^36  (F2_CAMPAIGN_LOG)", float(2**36)),
         ("t* = 8,592,912,739 (xr)", float(TSTAR)),
         ("2^33  (official_scale.json / I6)", float(2**33))]
print("     margins t / (m_j/log2 p);  < 1 = VIOLATED.  log2 p = %.6f" % lp)
hdr = "     rung |" + "".join(" %26s |" % c[0][:26] for c in CANDS)
print(hdr)
bands = {}
for label, mm in (("new-part", mnew), ("nested", mnest)):
    print("   --- %s window ---" % label)
    for cname, tv in CANDS:
        band = [j for j in range(1, 17) if tv >= mm[j] / lp]
        bands[(label, cname)] = band
    for j in range(1, 17):
        row = "     %4d |" % j
        for cname, tv in CANDS:
            r = tv / (mm[j] / lp)
            row += " %26s |" % ("%10.4f %s" % (r, "OK " if r >= 1 else "VIO"))
        print(row)
    for cname, tv in CANDS:
        b = bands[(label, cname)]
        print("       LEMMA 3 holds at rungs: %s   [t = %s]"
              % (("1-%d" % max(b)) if b else "NONE", cname))

r16_new_7e10 = 7e10 / (mnew[16] / lp)
check("S9.1", abs(r16_new_7e10 - 7.892) < 0.002,
      "rung16/new-part/7e10 margin = %.4fx reproduces PROOFS.md:233-234's 7.89x"
      % r16_new_7e10)
r16_new_tstar = TSTAR / (mnew[16] / lp)
check("S9.2", abs(r16_new_tstar - 0.9687) < 0.0005,
      "rung16/new-part/t* margin = %.4fx reproduces the banked 0.9687x SIGN FLIP"
      % r16_new_tstar)
check("S9.3", TSTAR / (mnest[16] / lp) < 1 and TSTAR / (mnest[15] / lp) < 1,
      "under t* AND nested, LEMMA 3 fails at rungs 15 AND 16 (banked claim)")
check("S9.4", bands[("new-part", CANDS[2][0])] == list(range(1, 16)),
      "under t*/new-part LEMMA 3 holds exactly at rungs 1-15")
check("S9.5", bands[("nested", CANDS[2][0])] == list(range(1, 15)),
      "under t*/nested   LEMMA 3 holds exactly at rungs 1-14")

print()
print("=" * 74)
print("S10 (P5) LEMMA 2 / THEOREM A cutoff  Lambda contains {1,3,..,2m-1}")
print("=" * 74)
print("     requires t >= 2*m_j - 1")
for label, mm in (("new-part", mnew), ("nested", mnest)):
    for cname, tv in CANDS:
        b = [j for j in range(1, 17) if tv >= 2 * mm[j] - 1]
        print("     %-9s t=%-34s -> rungs %s"
              % (label, cname, ("1-%d" % max(b)) if b else "NONE"))
b_7e10 = [j for j in range(1, 17) if 7e10 >= 2 * mnew[j] - 1]
check("S10.1", max(b_7e10) == 13,
      "t=7e10/new-part reproduces the banked 'rungs 1..13' (PROOFS.md:328)")
b_ts = [j for j in range(1, 17) if TSTAR >= 2 * mnew[j] - 1]
check("S10.2", max(b_ts) == 10,
      "t=t*/new-part reproduces the banked 'rungs 1-10' (sl1 PROOFS.md:391)")
b_ts_nest = [j for j in range(1, 17) if TSTAR >= 2 * mnest[j] - 1]
check("S10.3", max(b_ts_nest) == 9,
      "t=t*/nested shortens it further, to rungs 1-9")

print()
print("=" * 74)
print("S11 THE BAND UNDER THE RULES-FORCED t-INTERVAL (worst case, per Q6)")
print("=" * 74)
# rules force t in (n/256, n/41]; the WORST admissible t is the smallest.
t_worst = t_lower
for label, mm in (("new-part", mnew), ("nested", mnest)):
    b3 = [j for j in range(1, 17) if t_worst >= mm[j] / lp]
    b2 = [j for j in range(1, 17) if t_worst >= 2 * mm[j] - 1]
    print("     %-9s worst-t=%.4e : LEMMA3 rungs 1-%s ; LEMMA2 rungs 1-%s"
          % (label, t_worst, max(b3) if b3 else "NONE",
             max(b2) if b2 else "NONE"))
b2_worst = [j for j in range(1, 17) if t_worst >= 2 * mnew[j] - 1]
check("S11.1", max(b2_worst) <= 10,
      "worst-case admissible t gives a THEOREM A band no longer than rungs 1-10")
check("S11.2", t_worst < 7e10,
      "the published rungs-1-13 headline assumed a t (7e10) that no admissible "
      "field can realise")

print()
print("=" * 74)
print("S12 the (R+1)/m_j corollary table (sl1 PROOFS.md:134-138)")
print("=" * 74)
for j in (14, 15, 16):
    a = ((7e10 + 1) // 2 + 1) / mnew[j]
    b = ((TSTAR + 1) // 2 + 1) / mnew[j]
    print("     rung %d  m=2^%d : 7e10 -> %.5f ; t* -> %.5f"
          % (j, 22 + j, a, b))
check("S12.1", abs(((TSTAR + 1) // 2 + 1) / mnew[16] - 0.01563) < 1e-4,
      "reproduces 0.01563 at rung 16 under t* (SL-1 immunity intact)")

print()
print("=" * 74)
print("S13 rate rows: does the field cap even admit n = 2^41 at every rate?")
print("=" * 74)
for num, den in RATES:
    s = 41 if den == 2 else (41 if den == 2 else None)
for den, nbits in ((2, 41), (4, 42), (8, 43), (16, 44)):
    kk = (1 << nbits) // den
    ok = kk <= K_CAP
    print("     rate 1/%-2d : n = 2^%d, k = 2^%d  k<=2^40 ? %s"
          % (den, nbits, nbits - int(log2(den)), "yes" if ok else "no"))
    if not check("S13.%d" % den, ok, "row admissible on the k-cap"):
        pass

print()
print("=" * 74)
print("S14 (P6) the |K1| average-vs-sum seam, PRICED")
print("=" * 74)
# K1 = {c : f_even = 0} (f2_deployed_windows/REPORT.md:41), i.e. the frequency
# vectors supported on ODD indices l <= t.  So dim_F K1 = ceil(t/2) over the
# coefficient field F.  (O1) is stated as an AVERAGE over K1
# (f2_fixed_sector/REPORT.md:33); the consumer SUMS (f2_opening/PROOFS.md:341).
dimK1 = (TSTAR + 1) // 2
half_n = n41 // 2
log2K1_ext = dimK1 * 255.9          # coefficients in F_q  (extension reading)
log2K1_base = dimK1 * lp            # coefficients in F_p  (base reading)
print("     dim K1 = ceil(t*/2) = %d" % dimK1)
print("     log2|K1| (F_q coeffs) = %.6e   vs  n/2 = %.6e"
      % (log2K1_ext, float(half_n)))
print("     log2|K1| (F_p coeffs) = %.6e   (KoalaBear log2 p)" % log2K1_base)
check("S14.1", abs(log2K1_ext / half_n - 1.0) < 1e-3,
      "EXTENSION reading: log2|K1| = %.4f * (n/2) -- the seam is EXACTLY the "
      "whole (O1) budget 2^{n/2}" % (log2K1_ext / half_n))
check("S14.2", log2K1_base / half_n > 0.05,
      "BASE reading: log2|K1| = %.4f * (n/2) -- still Theta(n)"
      % (log2K1_base / half_n))
check("S14.3", log2K1_ext > 0.5 * half_n and log2K1_base > 0.05 * half_n,
      "=> under BOTH readings the seam is Theta(n), so it CANNOT be absorbed "
      "into the '+ o(n)' of (O1)'s target 2^{n/2 + o(n)}")
# why it is exactly n/2 in the extension reading: t*.L = n and dim = t*/2
check("S14.4", abs((TSTAR / 2.0 * 255.9) / half_n - 1.0) < 1e-3,
      "the identity is structural: dim K1 . L = (t*/2).L = (t*.L)/2 = n/2")

print()
print("=" * 74)
print("S15 robustness of the t-interval to the I1 ambiguity (n = 2^40 vs 2^41)")
print("=" * 74)


def admissible(nbits):
    out = []
    for s in range(0, 12):
        minp = nbits if s == 0 else nbits - s
        u = 1
        while (2**s) * u * minp < FIELD_CAP_BITS:
            out.append((s, (2**s) * u, minp))
            u += 2
    return out


for nbits in (40, 41):
    ad = admissible(nbits)
    smx = max(a[0] for a in ad)
    emx = max(a[1] for a in ad)
    mnp = min(a[2] for a in ad)
    nn = 1 << nbits
    hi_ext = nn / float(nbits)      # n | q-1 forces log2 q > nbits
    hi_base = nn / float(mnp)       # base-field reading
    lo = nn / 256.0
    print("     n = 2^%d : v_2(e)<=%d, e<=%d, log2 p >= %d" %
          (nbits, smx, emx, mnp))
    print("        t in (%.4e, %.4e]  (ext) ;  upper %.4e (base)"
          % (lo, hi_ext, hi_base))
    check("S15.%d" % nbits, 7e10 > hi_ext and 7e10 > hi_base,
          "t = 7e10 is EXCLUDED at n = 2^%d under BOTH field readings" % nbits)
check("S15.3", min(a[2] for a in admissible(40)) == 38,
      "at n = 2^40 the characteristic still satisfies log2 p >= 38 > 31")

print()
print("=" * 74)
nf = sum(1 for _, ok, _ in LEDGER if not ok)
print("TOTAL %d checks, %d FAIL" % (len(LEDGER), nf))
if nf:
    print("F2_TQ_PIN_VERIFY_FAIL")
    sys.exit(1)
print("F2_TQ_PIN_VERIFY_ALL_PASS")
sys.exit(0)
