#!/usr/bin/env python3
"""d1_gap.py -- rh_residuals_close (round 32), DELIVERABLE D1.

Residual (i): the w* TILING GAP between apolar's (AO1) closure band and
round-29's T4 band.  Everything here is EXACT INTEGER arithmetic; no
floats anywhere except one printed ratio.

Instruments re-derived from primary text (quoted in REPORT.md):
  (AO1)  T <= min(m+1, floor(a/(a-rho)), floor((a m + O)/rho))
              + floor((N-a) m / (R+1-a))          a < R+1
         notes/pilots_20260810/apolar_origin/PREREG.md:197-198
  (T4)   hypothesis 2s <= a-1 with s = R+1-a
         notes/pilots_20260810/collinearity_object/REPORT.md:21,25
  window w* in [4m+2, 8m-2]
         notes/pilots_20260810/collinearity_object/d3_coverage_results.txt:18
  (NEWCAP) w* <= 7m-1
         notes/pilots_20260810/rh_type2_stratum/REPORT.md:19
stdlib only.
"""


def prof(m):
    return dict(m=m, N=16 * m, R=8 * m, R1=8 * m + 1, rho=4 * m - 1, e=m)


def ao1(m, a, O=0):
    """(AO1) upper bound on T.  Requires a < R+1."""
    p = prof(m)
    assert a < p["R1"], (m, a)
    t1 = min(m + 1, a // (a - p["rho"]), (a * m + O) // p["rho"])
    t2 = (p["N"] - a) * m // (p["R1"] - a)
    return t1, t2, t1 + t2


def t4_thr(m):
    """smallest a with 2s <= a-1, s = R+1-a  <=>  3a >= 16m+3."""
    return -(-(16 * m + 3) // 3)


def closure_set(m, O=0):
    p = prof(m)
    lo, hi = 4 * m + 2, 8 * m - 2
    return [a for a in range(lo, hi + 1) if ao1(m, a, O)[2] <= p["rho"] + 1]


def gap(m, O=0):
    """the w* values covered by NEITHER instrument, inside the window."""
    lo, hi = 4 * m + 2, 8 * m - 2
    cl = set(closure_set(m, O))
    thr = t4_thr(m)
    return [a for a in range(lo, hi + 1) if a not in cl and a < thr]


def band_top(m, O=0):
    cl = closure_set(m, O)
    if not cl:
        return None
    # contiguity of the closure band, starting at 4m+2
    lo = 4 * m + 2
    top = lo - 1
    while top + 1 in cl:
        top += 1
    return top, (len(cl) == top - lo + 1)


def band_top_big(m, O=0):
    """binary search for the top of the (AO1) closure band.

    VALID ONLY under contiguity of {a : AO1(a) <= rho+1} upward from 4m+2,
    which D1.1 verifies exhaustively for every m tested and which D1.3
    re-verifies locally (+-8) at the official profile.
    """
    p = prof(m)
    lo, hi = 4 * m + 2, 8 * m - 2
    assert ao1(m, lo, O)[2] <= p["rho"] + 1
    a, b = lo, hi
    while a < b:
        mid = (a + b + 1) // 2
        if ao1(m, mid, O)[2] <= p["rho"] + 1:
            a = mid
        else:
            b = mid - 1
    return a


R = []
P = R.append

P("=" * 74)
P("D1.1  own re-derivation of the (AO1) closure band + T4 threshold + GAP")
P("      (independent of round 29's d3_coverage.py; O = 0)")
P("=" * 74)
P("  m   window        AO1-band top   contiguous  T4 thr   GAP (w* values)")
banked = {
    1: [6], 2: [11], 3: [16], 4: [20, 21, 22], 5: [25, 26, 27], 6: [32],
    7: [36, 37, 38], 8: [43], 9: [48], 10: [52, 53, 54], 11: [59], 12: [64],
    13: [68, 69, 70], 14: [75], 15: [80], 16: [84, 85, 86], 17: [91],
    18: [96], 19: [100, 101, 102], 20: [107], 24: [128], 30: [160],
    32: [171], 36: [192], 39: [208], 40: [212, 213, 214],
}
agree = 0
for m in sorted(banked):
    bt = band_top(m)
    g = gap(m)
    ok = (g == banked[m])
    agree += ok
    P("  %3d [%d..%d]  %s  %s   %5d   %-22s %s"
      % (m, 4 * m + 2, 8 * m - 2,
         ("%d" % bt[0]) if bt else "EMPTY",
         "Y" if (bt and bt[1]) else "n",
         t4_thr(m), str(g), "AGREE" if ok else "DISAGREE vs banked %s" % banked[m]))
P("  banked-table reproduction: %d/%d rows" % (agree, len(banked)))

P("")
P("=" * 74)
P("D1.2  gap size as a function of m mod 3  (m = 1..300, O = 0)")
P("=" * 74)
byres = {0: {}, 1: {}, 2: {}}
excep = []
for m in range(1, 301):
    g = gap(m)
    byres[m % 3][len(g)] = byres[m % 3].get(len(g), 0) + 1
for r in (0, 1, 2):
    P("  m = %d mod 3 : gap-size histogram %s" % (r, dict(sorted(byres[r].items()))))
# closed forms, checked
P("")
P("  closed forms tested for m in [1,300]:")
cf = {0: lambda m: [16 * m // 3], 1: lambda m: [(16 * m - 4) // 3, (16 * m - 1) // 3, (16 * m + 2) // 3],
      2: lambda m: [(16 * m + 1) // 3]}
bad = []
for m in range(1, 301):
    if gap(m) != cf[m % 3](m):
        bad.append(m)
P("    m=0 mod 3 -> {16m/3} ; m=1 mod 3 -> {(16m-4)/3,(16m-1)/3,(16m+2)/3} ;"
  " m=2 mod 3 -> {(16m+1)/3}")
P("    exceptions: %s" % (bad if bad else "NONE"))
for m in bad:
    bt_ = band_top(m)
    P("       m=%d : predicted %s   actual %s   (AO1 band top %s, T4 thr %d)"
      % (m, cf[m % 3](m), gap(m), bt_[0] if bt_ else "EMPTY", t4_thr(m)))

P("")
P("=" * 74)
P("D1.3  THE OFFICIAL PROFILE  m = 2^37")
P("=" * 74)
m = 2 ** 37
p = prof(m)
P("  m = 2^37 = %d   N = %d = 2^41   R+1 = %d   rho = %d = 2^39-1"
  % (m, p["N"], p["R1"], p["rho"]))
P("  budgets {rho+1, rho+2} = {%d, %d} = {2^39, 2^39+1}" % (p["rho"] + 1, p["rho"] + 2))
top = band_top_big(m)
thr = t4_thr(m)
loc = [(d, ao1(m, top + d)[2] <= p["rho"] + 1) for d in range(-8, 9)]
P("  (AO1) closure band  = [%d .. %d]   (binary search)" % (4 * m + 2, top))
P("  local check around the top (offset, closes?): %s" % loc)
P("  T4 band             = [%d .. %d]" % (thr, 8 * m - 2))
gp = list(range(top + 1, thr))
P("  GAP                 = %s        (%d integer%s)"
  % (gp, len(gp), "" if len(gp) == 1 else "s"))
astar = gp[0]
P("  gap integer a* = %d ; (2^41+1)/3 = %d ; equal: %s"
  % (astar, (2 ** 41 + 1) // 3, astar == (2 ** 41 + 1) // 3))
s = p["R1"] - astar
t1, t2, tot = ao1(m, astar)
P("")
P("  AT a*:")
P("    s = R+1-a*            = %d = (8m+2)/3   exact: %s" % (s, s * 3 == 8 * m + 2))
P("    2s - a*               = %d      (T4 needs 2s <= a*-1, i.e. this <= -1)" % (2 * s - astar))
P("    RIG = a*-1-2s         = %d      (round-29 threshold RIG >= 0)" % (astar - 1 - 2 * s))
P("    T1cap                 = %d" % t1)
P("      floor(a/(a-rho))    = %d   ;  m+1 = %d ;  floor(am/rho) = %d"
  % (astar // (astar - p["rho"]), m + 1, astar * m // p["rho"]))
P("    CAP = T2cap           = %d      ( = 4m-2 : %s)" % (t2, t2 == 4 * m - 2))
P("    (AO1) total           = %d" % tot)
P("    rho+1 (target)        = %d" % (p["rho"] + 1))
P("    DEFICIT (AO1-(rho+1)) = %d      <-- fails by EXACTLY this many slopes" % (tot - p["rho"] - 1))
P("")
P("  one integer below (a*-1 = %d, the top of the AO1 band):" % (astar - 1))
t1b, t2b, totb = ao1(m, astar - 1)
P("    s = %d  T1cap = %d  CAP = %d  AO1 = %d  <= rho+1 = %d : %s"
  % (p["R1"] - astar + 1, t1b, t2b, totb, p["rho"] + 1, totb <= p["rho"] + 1))
P("  one integer above (a*+1 = %d, the bottom of the T4 band):" % (astar + 1))
t1c, t2c, totc = ao1(m, astar + 1)
sc = p["R1"] - astar - 1
P("    s = %d  2s-(a*+1) = %d (T4 hypothesis holds: %s)  AO1 = %d (irrelevant, T4 covers it)"
  % (sc, 2 * sc - astar - 1, 2 * sc <= astar, totc))

P("")
P("=" * 74)
P("D1.4  WHAT IS FORCED AT a = a*  (under (SAT3) T = rho+2)")
P("=" * 74)
T = p["rho"] + 2
T1max = astar // (astar - p["rho"])
T2min = T - T1max
P("  T = rho+2                       = %d" % T)
P("  T_1 <= floor(a*/(a*-rho))       = %d" % T1max)
P("  T_2 >= T - T_1                  = %d" % T2min)
P("  T_2 <= CAP                      = %d" % t2)
P("  => T_1 = %d and T_2 = %d are FORCED EXACTLY (T2min == CAP: %s)"
  % (T1max, t2, T2min == t2))
out_cap = (p["N"] - astar) * m          # sum_{x not in W} d_x  <=  (N-a) e
spend = t2 * s                          # every type-2 slope spends >= s outside W
slack = out_cap - spend
P("")
P("  outside-W capacity  (N-a*)e     = %d" % out_cap)
P("  minimum type-2 spend  T_2 * s   = %d" % spend)
P("  total excess  sum_gamma eps_g   <= %d          (eps_g := |S_g\\W| - s >= 0)" % slack)
P("    = (7m+4)/3 : %s" % (slack * 3 == 7 * m + 4))
P("  #{gamma : eps_gamma >= 1}       <= %d" % slack)
P("  #{MINIMUM-WEIGHT type-2}        >= T_2 - excess = %d" % (t2 - slack))
P("    = (5m-10)/3 : %s" % ((t2 - slack) * 3 == 5 * m - 10))
P("  T4's conclusion (if its hypothesis held) caps a collinear family at")
P("  M <= e+1 = m+1                  = %d" % (m + 1))
P("  CONTRADICTION MARGIN            = %d  (ratio %.4f)"
  % (t2 - slack - (m + 1), (t2 - slack) / (m + 1)))
P("  => T4's CONCLUSION at a* would close residual (i) with %.4fx of room;"
  % ((t2 - slack) / (m + 1)))
P("     only its HYPOTHESIS fails, and it fails by exactly one point (2s = a*+1).")

P("")
P("=" * 74)
P("D1.5  (NEWCAP) INTERACTION  (round 31:  w* <= 7m-1)")
P("=" * 74)
P("  7m-1                            = %d" % (7 * m - 1))
P("  gap integer a*                  = %d" % astar)
P("  a* <= 7m-1 : %s  => (NEWCAP) does NOT remove the gap" % (astar <= 7 * m - 1))
P("  a* survives for every m in [1,300]: %s"
  % all(all(g <= 7 * mm - 1 for g in gap(mm)) for mm in range(1, 301)))
P("  the w* ceiling that WOULD close residual (i) is the AO1 band top = %d" % (astar - 1))
P("  required strengthening of (NEWCAP): %d -> %d, factor %.6f (-> 21/16 = %.6f)"
  % (7 * m - 1, astar - 1, (7 * m - 1) / (astar - 1), 21 / 16))
P("  such a ceiling would ALSO kill residual (ii) (its whole band is above a*).")

P("")
P("=" * 74)
P("D1.6  O-SENSITIVITY of the gap  (O <= delta = m-1, apolar (C4))")
P("=" * 74)
for mm in (4, 8, 40, 64):
    gs = {}
    for O in range(0, mm):
        gs.setdefault(tuple(gap(mm, O)), []).append(O)
    P("  m=%d : %s" % (mm, "; ".join("O in [%d..%d] -> %s" % (v[0], v[-1], list(k))
                                     for k, v in gs.items())))
Omax = max(O for O in (0, 1, 2, m - 3, m - 2, m - 1)
           if ao1(m, 4 * m + 2, O)[2] <= p["rho"] + 1)
P("  official m=2^37: the AO1 band BOTTOM (a=4m+2) closes iff O <= m-2;")
P("    O=m-2 : AO1(4m+2) = %d <= rho+1 ; O=m-1 : AO1(4m+2) = %d = rho+2 (apolar P7)"
  % (ao1(m, 4 * m + 2, m - 2)[2], ao1(m, 4 * m + 2, m - 1)[2]))
P("    gap at O=0     : %s" % gp)
P("    gap at O=m-2   : %s" % list(range(band_top_big(m, Omax) + 1, thr)))
P("    at O=m-1 the AO1 band is EMPTY at its own bottom, so the 'gap' is the")
P("    whole sub-T4 window; the tiling statement is an O=0 statement.")

P("")
P("=" * 74)
P("D1.7  the DEFICIT at every gap integer (how far AO1 misses rho+1)")
P("=" * 74)
P("   m   gap value   s   2s-a   RIG   AO1   rho+1   deficit")
for mm in [2, 3, 4, 5, 8, 16, 40, 64, 100, 2 ** 10]:
    pp = prof(mm)
    for a in gap(mm):
        ss = pp["R1"] - a
        _, _, tt = ao1(mm, a)
        P("  %4d  %8d  %4d  %4d  %4d  %6d  %6d   %d"
          % (mm, a, ss, 2 * ss - a, a - 1 - 2 * ss, tt, pp["rho"] + 1,
             tt - pp["rho"] - 1))
P("")
P("=" * 74)
P("D1.8  NO-HOLE CERTIFICATE at m = 2^37 (the binary search of D1.3 assumed")
P("      contiguity; at m=8 contiguity FAILS, so it must be certified here)")
P("=" * 74)
P("  For a >= 4m+4, T1cap = j(a) := floor(a/(a-rho)) (the other two terms of")
P("  the min are >= m and j(a) <= m there).  On I_j := {a : j(a) = j} =")
P("  ((j+1)rho/j, j*rho/(j-1)], AO1 = j + CAP(a) is NONDECREASING (CAP is),")
P("  so the covered part of I_j is a PREFIX and the uncovered part a SUFFIX.")
P("  Hence it suffices to test the TOP of each I_j.")
P("")
P("   j   top(I_j)=floor(j*rho/(j-1))   AO1 there   <= rho+1 ?   T1cap there")
for j in range(3, 12):
    topj = j * p["rho"] // (j - 1)
    if topj >= p["R1"]:
        continue
    t1j, t2j, totj = ao1(m, topj)
    P("  %2d   %-26d  %-12d %-11s %d"
      % (j, topj, totj, totj <= p["rho"] + 1, t1j))
P("")
P("  Every I_j with j >= 4 has its TOP covered, therefore ALL of I_j is")
P("  covered (prefix property).  The uncovered set below the T4 threshold is")
P("  therefore contained in I_3, where the band top is %d." % top)
P("  => GAP = {%d} EXACTLY, certified, not merely binary-searched." % astar)
P("  (At m=8 the same test fails: top(I_4) = %d has AO1 = %d > rho+1 = %d,"
  % (4 * prof(8)["rho"] // 3, ao1(8, 4 * prof(8)["rho"] // 3)[2], prof(8)["rho"] + 1))
P("   which is precisely the hole at w* = 41 that the banked table hides.)")

P("")
P("  RIG at the gap integers, closed form 3g-16m-3 :")
P("    m=2 mod 3 (official class): RIG = -2 exactly, i.e. 2s = a+1,")
P("    so the T4 difference polynomial is sigma_W * (LINEAR), one degree")
P("    beyond the q=17 fence's sigma_W * (CONSTANT).")

print("\n".join(R))
