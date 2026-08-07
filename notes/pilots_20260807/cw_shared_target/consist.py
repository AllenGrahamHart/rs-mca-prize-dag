#!/usr/bin/env python3
# cw_shared_target -- CORRECTED section B + the THEOREM BB consistency test.
# SELF-CORRECTION: attack.py section B used kappa = e (the extension degree). The deep-stratum
# relation set RSET has ONE F_p-condition when delta_a = 1 (p = 1 mod n_a, theta in F_p), which is
# exactly bb_nu_transport's "the measured U2 loss factor tracks Q = p".  kappa = delta_a = 1.
import math, sys
from math import comb

def log2big(x):
    n = int(x)
    if n == 0: return float('-inf')
    b = n.bit_length()
    if b <= 900: return math.log2(n)
    return b - 900 + math.log2(n >> (b - 900))

PASS = 0; FAIL = 0
def check(nm, c, ex=""):
    global PASS, FAIL
    if c: PASS += 1; print("PASS  %-62s %s" % (nm, ex))
    else: FAIL += 1; print("FAIL  %-62s %s" % (nm, ex))

p_w = 3 * 2 ** 41 + 1
lp_w = math.log2(p_w)
Bstar = 242251802232021244567343686397347233808
lB = log2big(Bstar)
BB_v34 = 199.575          # THEOREM BB, banked lower bound on max-shell X_{2^34} at tower rows

print("=" * 104)
print("CORRECTED SECTION B.  kappa = delta_a = 1 (NOT e).  All rows in the break region have delta_a = 1.")
print("=" * 104)
print("Chain (an IDENTITY + one exact finite bound + the assumed ceiling):")
print("  (i)  LEMMA TC identity, verified 20/20 at toy scale and 12/12 against bb's N_acc:")
print("         Acc_deep_total = C(L,r'/2) * sum_{eps in RSET, eps != 0} GDEV(U) * 2^-U ,  r' = L-2")
print("  (ii) exact finite bound: GDEV(U) <= GDEVmax(L) := max_U GDEV(L,L-2,U) = 2^{L-2}/C(L,L/2-1)")
print("  (iii)assumed EXCESS-CEILING(C):  sum_{eps != 0} 2^-U  <=  C * (2^L - 1)/p^{delta_a}")
print("  =>   Acc_deep_total <= C(L,r'/2) * GDEVmax(L) * C * (2^L - 1)/p")
print()
print("%3s %5s | %9s %9s %9s | %9s | %11s %11s | %11s %11s" %
      ("v", "L", "S(v)", "U1", "U2", "SIGMA_w", "CEIL C=1 w", "CEIL C=2 w", "CEIL C=1 e1", "CEIL C=2 e1"))
tab = []
for v in [34, 35, 36, 37, 38, 39]:
    L = 2 ** (41 - v); rp = L - 2
    Sv = log2big(comb(2 ** (41 - v), 2 ** (40 - v) - 1)) - (41 - v)
    U1 = log2big(comb(2 * L, rp))
    U2 = log2big((comb(2 * L, rp) + comb(L, rp // 2)) // (2 * L))
    gm = max((comb(L - U, (rp - U) // 2) / comb(L, rp // 2)) * 2.0 ** U for U in range(0, rp + 1, 2))
    base = log2big(comb(L, rp // 2)) + math.log2(gm) + L      # + log2 C - log2 p
    r = dict(v=v, L=L, Sv=Sv, U1=U1, U2=U2, gm=gm, base=base,
             sig_w=L - lp_w, sig_e1=L - 129.5849625,
             c1w=base - lp_w, c2w=base + 1 - lp_w,
             c1e=base - 129.5849625, c2e=base + 1 - 129.5849625)
    tab.append(r)
    print("%3d %5d | %9.4f %9.4f %9.4f | %9.3f | %11.4f %11.4f | %11.4f %11.4f" %
          (v, L, Sv, U1, U2, r['sig_w'], r['c1w'], r['c2w'], r['c1e'], r['c2e']))
print("  (log2 throughout.  'w' = witness tower row p = 3*2^41+1 (log2 p = %.6f, delta_a = 1);" % lp_w)
print("   'e1' = e = 1 prime rows at the live-window FLOOR log2 p = 129.5849625.  B* = 2^%.4f)" % lB)

print()
print("=" * 104)
print("THE CONSISTENCY TEST -- does the proposed shared form CONTRADICT banked THEOREM BB?")
print("=" * 104)
r34 = tab[0]
print("THEOREM BB (statement_addenda/13-wave47-theorem-bb.md:3-9): at break-region TOWER rows")
print("  (delta_a = 1, e >= 3, witness p = 3*2^41+1, q = p^6):  max-shell X_{2^34} >= 2^199.575 > B*.")
print("  The e = 1 prime rows are 'untouched and provably unreachable by the method'.")
print()
print("  ceiling bound on Acc_deep at v=34, witness tower row, C=1 : 2^%.4f" % r34['c1w'])
print("  THEOREM BB's proved floor on the same functional        : 2^%.4f" % BB_v34)
check("BB's floor lies BELOW the ceiling's bound at C=1 (no contradiction)",
      BB_v34 <= r34['c1w'], "2^%.4f <= 2^%.4f, slack %.4f bits" % (BB_v34, r34['c1w'], r34['c1w'] - BB_v34))
imp_excess = BB_v34 - (log2big(comb(128, 63)) + math.log2(r34['gm'])) - (128 - lp_w)
print("  => BB IMPLIES, at the official row:  EXCESS-CRATIO >= 2^%.4f  (i.e. %.4f bits BELOW the" % (imp_excess, -imp_excess))
print("     volume heuristic).  The official object is therefore NOT a counterexample to the ceiling;")
print("     the only banked official-row datum about this functional is CONSISTENT with it.")
check("the shared form is NOT refuted at the official row by BB", imp_excess <= 0.0,
      "implied EXCESS-CRATIO >= 2^%.4f <= 2^0" % imp_excess)
check("the ceiling does NOT de-vacuum v=34 at the TOWER rows (agrees with BB's budget break)",
      r34['c2w'] > lB, "CEIL(C=2) = 2^%.4f > B* = 2^%.4f" % (r34['c2w'], lB))
check("the ceiling DOES de-vacuum v=34 at the e=1 PRIME rows (which BB cannot reach)",
      r34['c2e'] < lB, "CEIL(C=2) = 2^%.4f < B* = 2^%.4f, margin %+.4f bits" % (r34['c2e'], lB, lB - r34['c2e']))
print()
print("  gain at v=35 (where U2 already suffices): U2 margin %+.4f bits -> ceiling margin %+.4f bits (C=2, witness)"
      % (lB - tab[1]['U2'], lB - tab[1]['c2w']))
check("the ceiling strictly improves the v=35 witness-row margin over U2",
      tab[1]['c2w'] < tab[1]['U2'], "%.4f vs %.4f (gain %.4f bits)" %
      (tab[1]['c2w'], tab[1]['U2'], tab[1]['U2'] - tab[1]['c2w']))

print()
print("=" * 104)
print("WHAT THE CEILING IS WORTH TO M4, ROW BY ROW (C = 2; log2)")
print("=" * 104)
print("%3s | %-34s | %-34s" % ("v", "witness tower row (delta_a=1, e=6)", "e=1 prime rows, log2 p = 129.585"))
for r in tab:
    a = "U2 %s B*, CEIL %s B*" % ("<" if r['U2'] < lB else ">=", "<" if r['c2w'] < lB else ">=")
    b = "U2 %s B*, CEIL %s B*" % ("<" if r['U2'] < lB else ">=", "<" if r['c2e'] < lB else ">=")
    print("%3d | %-34s | %-34s" % (r['v'], a, b))
print()
print("  NET: the ceiling changes NO verdict at v >= 35 (U2 already suffices there);")
print("       at v = 34 it de-vacuums ONLY the e = 1 prime rows, and it must NOT de-vacuum the")
print("       tower rows -- and it does not, by %.4f bits." % (r34['c2w'] - lB))

print()
print("=" * 104)
print("TOTAL: %d PASS / %d FAIL" % (PASS, FAIL))
print("=" * 104)
sys.exit(1 if FAIL else 0)
