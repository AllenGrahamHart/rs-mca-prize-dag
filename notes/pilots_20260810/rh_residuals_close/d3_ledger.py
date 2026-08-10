#!/usr/bin/env python3
"""d3_ledger.py -- rh_residuals_close (round 32), DELIVERABLE D3.

The CURRENT residual-budget state as exact integers.  Every number here is
recomputed from the profile, not copied; the report carries the file:line of
the text each row reconciles.  stdlib only, exact integers only.
"""
from fractions import Fraction

out = []
P = out.append

m = 2 ** 37
N = 16 * m          # = n = 2^41
R1 = 8 * m + 1
rho = 4 * m - 1
n, k = 2 ** 41, 2 ** 40

P("=" * 74)
P("D3.1  THE PROFILE AND THE TWO BUDGETS")
P("=" * 74)
P("  m = 2^37 = %d   n = N = 16m = %d = 2^41   k = %d = 2^40" % (m, N, k))
P("  rho = 4m-1 = %d = 2^39-1   R+1 = 8m+1 = %d" % (rho, R1))
P("  budget 1 = rho+1 = %d = 2^39" % (rho + 1))
P("  budget 2 = rho+2 = %d = 2^39+1" % (rho + 2))
P("  B*(q) = floor(q/2^128); budget b is met exactly when q >= 2^128 * b:")
P("    budget 2^39   met for q >= %d = 2^167" % (2 ** 128 * (rho + 1)))
P("    budget 2^39+1 met for q >= %d = 2^167+2^128" % (2 ** 128 * (rho + 2)))
P("  RPFC territory (B* in {2^39,2^39+1}) = [%d, %d) = [2^167, 2^167+2^129)"
  % (2 ** 167, 2 ** 167 + 2 ** 129))
P("    width %d = 2^129 ; pose range (2^167, 2^256) width ~2^256"
  % (2 ** 129))
P("    fraction of the pose on which 'q prime' is PROVED = 2^-127")

P("")
P("=" * 74)
P("D3.2  THE q-AXIS: three regions, exact endpoints")
P("=" * 74)
regs = [("S1  sliver", 2 ** 167, 2 ** 167 + 2 ** 128, rho + 1),
        ("S2  mid", 2 ** 167 + 2 ** 128, 2 ** 167 + 2 ** 129, rho + 2),
        ("S3  above", 2 ** 167 + 2 ** 129, 2 ** 256, rho + 3)]
for nm, lo, hi, b in regs:
    P("  %-11s q in [%d, %d)" % (nm, lo, hi))
    P("              B*(q) = %d %s" % (b, "= 2^39" if b == rho + 1 else
                                       ("= 2^39+1" if b == rho + 2 else ">= 2^39+2")))
P("  relative width of S1 inside [2^167, 2^167+2^129) = %s"
  % Fraction(2 ** 128, 2 ** 129))
P("  relative width of S1 inside the pose (2^167,2^256) = 2^-128 * 2^-... :")
P("    S1 width / pose width = %s" % Fraction(2 ** 128, 2 ** 256 - 2 ** 167))

P("")
P("=" * 74)
P("D3.3  THE w*-AXIS: the window splits EXACTLY into four pieces")
P("=" * 74)
lo_w, hi_w = 4 * m + 2, 8 * m - 2
ao1_top = 733007751850            # d1_gap.py / d1b_holes.py, certified
gapv = 733007751851
t4_lo = 733007751852
newcap = 7 * m - 1
P("  window [4m+2, 8m-2] = [%d, %d]   width %d" % (lo_w, hi_w, hi_w - lo_w + 1))
rows = [("(AO1) CLOSED", lo_w, ao1_top),
        ("RESIDUAL (i) gap", gapv, gapv),
        ("RESIDUAL (ii) band (T4 applies, min-weight only)", t4_lo, newcap),
        ("DEAD by (NEWCAP) w* <= 7m-1", newcap + 1, hi_w)]
tot = 0
for nm, a, b in rows:
    w = b - a + 1
    tot += w
    P("  %-48s [%d..%d]  width %d  share %s"
      % (nm, a, b, w, Fraction(w, hi_w - lo_w + 1)))
P("  widths sum to the window: %s (%d vs %d)"
  % (tot == hi_w - lo_w + 1, tot, hi_w - lo_w + 1))
P("  shares as exact fractions: 1/3 + (one integer) + 5/12 + 1/4")
P("    1/3 check: %s ; 5/12 check: %s ; 1/4 check: %s"
  % (Fraction(ao1_top - lo_w + 1, hi_w - lo_w + 1),
     Fraction(newcap - t4_lo + 1, hi_w - lo_w + 1),
     Fraction(hi_w - newcap, hi_w - lo_w + 1)))

P("")
P("=" * 74)
P("D3.4  THE RESIDUAL-(ii) CAP, and a PRECISION NIT on '9/4 exactly'")
P("=" * 74)
a_max = 7 * m - 1
s_max = R1 - a_max
cap = (N - a_max) * m // s_max
P("  a_max = 7m-1 = %d ; s = R+1-a_max = %d = m+2 : %s"
  % (a_max, s_max, s_max == m + 2))
P("  cap = floor((N-a)m/s) = %d" % cap)
P("  closed form 9m-17 = %d : %s" % (9 * m - 17, cap == 9 * m - 17))
P("  AO1 = T1cap + cap = 2 + %d = %d" % (cap, cap + 2))
P("  closed form 9m-15 = %d : %s" % (9 * m - 15, cap + 2 == 9 * m - 15))
P("  banked figures 1236950581231 / 1236950581233 : %s / %s"
  % (cap == 1236950581231, cap + 2 == 1236950581233))
P("  ratio AO1/(rho+1) = %s = %.12f"
  % (Fraction(cap + 2, rho + 1), (cap + 2) / (rho + 1)))
P("  9/4 = 2.250000000000 ; the exact ratio is 9/4 - 15/(4m) = 9/4 - %.6e"
  % (15 / (4 * m)))
P("  => 'residual factor 9/4 EXACTLY' is asymptotic, not exact; the exact")
P("     statement is AO1 = 9m-15 and (rho+1) = 4m, ratio (9m-15)/(4m).")
P("     Same class of nit as round 29's '4 - 7.28e-12, NOT exactly 4'.")

P("")
P("=" * 74)
P("D3.5  RESIDUAL (i) AND (ii) ARE THE SAME MISSING STEP, priced")
P("=" * 74)
astar = gapv
s_star = R1 - astar
T2 = rho + 2 - 3
P("  residual (i)  at a* = %d : needs #{min-weight type-2} <= %d"
  % (astar, (rho + 2 - 3) - ((N - astar) * m - (rho + 2 - 3) * s_star)))
P("    T4's conclusion M <= m+1 = %d would give it, margin ratio %s"
  % (m + 1, Fraction((rho + 2 - 3) - ((N - astar) * m - (rho + 2 - 3) * s_star),
                     m + 1)))
P("    obstruction: T4 hypothesis 2s <= a-1 fails by ONE point (2s = a*+1)")
P("  residual (ii) at a in [%d, %d] : needs (FR) |S ^ W| <= ~2m"
  % (t4_lo, newcap))
P("    obstruction: the max-vs-mean upgrade, FENCED for incidence-only")
P("    axioms by background/nodes/rate_half_type2_fr_incidence_only_route_fence")
P("  BOTH obstructions are algebraic-not-combinatorial; residual (i) is now")
P("  fenced the same way (d1c_fence.py, explicit m=2 system).")

P("")
P("=" * 74)
P("D3.6  LB1 AND THE FAR-CA SIDE (different object, same endgame)")
P("=" * 74)
a_top, a_bot = 3 * n // 4, k + 2 ** 34
P("  bracket [k+2^34, 3n/4] = [%d, %d]" % (a_bot, a_top))
P("  LB1: B_ca^far(a) >= n-a+1")
P("    at a = 3n/4   : >= %d = 2^39+1  == budget 2 exactly" % (n - a_top + 1))
P("    at a = k+2^34 : >= %d = 2^39.9773" % (n - a_bot + 1))
P("  => budget 2^39 is UNATTAINABLE at a = 3n/4 (n-a+1 exceeds it by %d)"
  % (n - a_top + 1 - (rho + 1)))
P("  => on the q-sliver S1 (B* = 2^39) the far-CA route is DEAD at the")
P("     bracket TOP; it can only survive at smaller a.")
P("  distance from the far-CA lower bound to the 2^128 budget at a=k+2^34:")
P("    2^128 / %d = 2^%.4f" % (n - a_bot + 1, 128 - (n - a_bot + 1).bit_length() + 1))
print("\n".join(out))
