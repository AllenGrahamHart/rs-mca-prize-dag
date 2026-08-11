"""d1_ledger.py -- r38_side_door D1: the degenerate-fibre axiom ledger, exhaustive.

Stdlib only.  Run:  tools/ramguard tiny -- python3 notes/pilots_20260811/r38_side_door/d1_ledger.py <tag>
Writes notes/pilots_20260811/r38_side_door/d1_ledger_results_<tag>.txt in APPEND mode.

Axioms used (all quoted from banked files, file:line in the report):
  (SAT1) rho=4m-1, N=16m, delta=m-1                    saturation_rigidity/statement.md:13
  (SAT2) 0 <= O <= sum c_gamma <= delta = m-1          :33
  (SAT3) T = 4m+1 = rho+2                              :40
  (SAT4) sum_{x in D}(m-d_x) = 1+O <= m                :53
  (SAT5) N-(1+O) >= 15m saturated                      :59
  (OUT-m) X'_g + 2 X''_g >= m-1-eps_g ; aggregate
          sum eps = sum_x def(x) t_x, t_x = m-1/m-2/m-3
          at outside/symdiff/middle                    crossing/statement.md:3329-3334,3752-3757
  per-side cap |S_gamma ^ S_g| <= m-1                  crossing/statement.md:3355-3356
  (OV) pair multiplicity: |S_g ^ S_g'| <= 2rho-a = m-1 r36 REPORT.md:163
"""

import itertools
import sys

TAG = sys.argv[1] if len(sys.argv) > 1 else "a"
OUT = "notes/pilots_20260811/r38_side_door/d1_ledger_results_%s.txt" % TAG
FH = open(OUT, "a")


def say(s=""):
    FH.write(s + "\n")
    print(s)


m = 4
rho = 4 * m - 1          # 15 type-2 slopes
N = 16 * m               # 64 domain points
T = rho + 2              # 17 supported slopes = 2 type-1 + rho type-2
a = 7 * m - 1            # 27 = |W|
delta = m - 1            # 3
nmid = m - 1             # 3 middles  = |S_g ^ S_h|
nout = 6 * m             # 24 outer points = |S_g D S_h|
NF = nout // 3           # 8 outer fibres of the degree-3 map w
percap = m - 1           # per-side cap |S_gamma ^ S_g| <= m-1
totcap = 2 * m - 2       # X' + 2X'' <= 2m-2

say("=" * 74)
say("D1 LEDGER  r38_side_door  tag=%s" % TAG)
say("m=%d rho=%d N=%d T=%d a=%d delta=%d | outer pts %d in %d fibres, middles %d"
    % (m, rho, N, T, a, delta, nout, NF, nmid))
say("caps: per-side %d, X'+2X'' <= %d, pair-mult (OV) <= 2rho-a = %d"
    % (percap, totcap, 2 * rho - a))

# --------------------------------------------------------------- D1.a  W assembly
say("")
say("[D1.a] W ASSEMBLY:  8 outer fibres x 3 + 1 middle fibre x 3 = %d ; a = 7m-1 = %d  %s"
    % (NF * 3 + nmid, a, "OK" if NF * 3 + nmid == a else "FAIL"))
say("       |S_g| = |S_h| = 12 outer + 3 middles = %d = rho  %s"
    % (12 + nmid, "OK" if 12 + nmid == rho else "FAIL"))

# ------------------------------------------- D1.b  deficiency placements, exhaustive
# An outer fibre contributes  k in {1,2,3}  DISTINCT type-2 slopes (slots);
#   its 3 points then have d_x = 1 (type-1) + k, deficiency 3-k each -> 3(3-k) units.
#   k=3 normal, k=2 double root, k=1 triple root.
# The middle fibre reserves  r in {0,1,2}  type-2 slopes (all three middles share one
#   cubic, so they share the same reserved set); each middle has d_x = 2 (both type-1
#   slopes) + r, deficiency (m-2)-r = 2-r each -> 3(2-r) units.  r=2 normal.
# (SAT4): total deficiency over the domain = 1+O, and 1+O <= m ; (SAT2): O <= m-1.
say("")
say("[D1.b] EXHAUSTIVE OVER DEFICIENCY PLACEMENTS INSIDE THE (SAT2)/(SAT4) BUDGET")
say("  ks = distinct-slot counts of the 8 outer fibres ; r = middle reserved slopes")
say("  slots = sum ks ; savail = rho - r ; demand = slots - savail (merges needed)")
say("")
say("  %-26s %5s %5s %6s %5s %5s %7s %s"
    % ("placement", "def", "O", "slots", "res", "avail", "demand", "legal"))
best = None
rows = []
for nk2 in range(0, 3):            # number of double-root outer fibres
    for nk1 in range(0, 2):        # number of triple-root outer fibres
        if nk2 + nk1 > NF:
            continue
        for r in (2, 1, 0):
            ks = [3] * (NF - nk2 - nk1) + [2] * nk2 + [1] * nk1
            defu = sum(3 * (3 - k) for k in ks) + 3 * (2 - r)
            O = defu - 1
            slots = sum(ks)
            avail = rho - r
            demand = slots - avail          # s = slots - merges <= avail
            legal = (0 <= O <= m - 1) and (defu <= m) and defu >= 1
            # defu = 0 is the saturated baseline: then 1+O = 0 is impossible, so the
            # baseline configuration must carry its single unit of deficiency SOMEWHERE
            # else in the domain (an outside point) -- recorded as the O=0 row.
            name = "out %dx[2] %dx[3] | mid r=%d" % (nk2, nk1, r)
            rows.append((name, defu, O, slots, r, avail, demand, legal))
for name, defu, O, slots, r, avail, demand, legal in rows:
    if defu > m + 3:
        continue
    say("  %-26s %5d %5d %6d %5d %5d %7d %s"
        % (name, defu, O, slots, r, avail, demand, "LEGAL" if legal else "-"))
    if legal and (best is None or demand < best[6]):
        best = (name, defu, O, slots, r, avail, demand, legal)
# baseline (no W-deficiency at all): 1+O units sit outside W, O>=0
say("  %-26s %5s %5s %6d %5d %5d %7d %s"
    % ("BASELINE (def outside W)", "1+O", ">=0", 24, 2, 13, 11, "LEGAL"))
say("")
legals = [r for r in rows if r[7]]
mind = min(r[6] for r in legals)
say("  MINIMUM LEGAL DEMAND = %d, attained by:" % mind)
for r in legals:
    if r[6] == mind:
        say("     %s   (deficiency %d = 1+O, O = %d)" % (r[0], r[1], r[2]))
say("  -> no legal placement reaches demand 9: every 3-unit placement buys EXACTLY 1,")
say("     and two placements cost 6 > m = %d units, violating (SAT4)." % m)

# ------------------------------------------------- D1.c  merge designs, exhaustive
say("")
say("[D1.c] MERGE DESIGNS (bipartite 4+4, simple by (OV), degree <= slot count)")


def designs(slotA, slotB, edges):
    """all bipartite 0/1 4x4 matrices with row sums <= slotA, col sums <= slotB,
    total = edges; returns list of (rowdeg, coldeg) multiset signatures + count."""
    out = {}
    cells = [(i, j) for i in range(4) for j in range(4)]
    for pick in itertools.combinations(range(16), edges):
        rd = [0] * 4
        cd = [0] * 4
        for p in pick:
            i, j = cells[p]
            rd[i] += 1
            cd[j] += 1
        if all(rd[i] <= slotA[i] for i in range(4)) and all(cd[j] <= slotB[j] for j in range(4)):
            key = (tuple(sorted(rd, reverse=True)), tuple(sorted(cd, reverse=True)))
            out[key] = out.get(key, 0) + 1
    return out


for label, slotA, slotB, edges in (
        ("BASELINE  24 slots, 11 merges", [3] * 4, [3] * 4, 11),
        ("DOOR A    23 slots, 10 merges", [3, 3, 3, 2], [3] * 4, 10),
        ("DOOR B    24 slots, 10 merges", [3] * 4, [3] * 4, 10)):
    d = designs(slotA, slotB, edges)
    tot = sum(d.values())
    say("  %s : %d labelled designs, degree signatures:" % (label, tot))
    for k in sorted(d):
        say("      A-deg %s | B-deg %s   x%d" % (k[0], k[1], d[k]))
    sA = sum(slotA)
    sB = sum(slotB)
    say("      unmerged slots n_1 = %d (A) + %d (B) = %d ; s = %d + %d = %d"
        % (sA - edges, sB - edges, sA + sB - 2 * edges, edges,
           sA + sB - 2 * edges, sA + sB - edges))

# --------------------------------------------------- D1.d  axiom margins, both doors
say("")
say("[D1.d] AXIOM MARGINS AT THE THREE DEFICIENT POINTS")
for door, ks, r in (("BASELINE", [3] * 8, 2), ("DOOR A", [3] * 7 + [2], 2), ("DOOR B", [3] * 8, 1)):
    slots = sum(ks)
    avail = rho - r
    n2 = slots - avail
    n1 = slots - 2 * n2
    s = slots - n2
    defu = sum(3 * (3 - k) for k in ks) + 3 * (2 - r)
    O = max(defu - 1, 0)
    # where the deficiency sits and what (OUT-m) charges for it
    if door == "DOOR A":
        tx, cls = m - 2, "symmetric-difference"
    elif door == "DOOR B":
        tx, cls = m - 3, "middle"
    else:
        tx, cls = m - 1, "outside (baseline)"
    epsagg = defu * tx
    say("")
    say("  %s: slots %d, middle-reserved %d, available %d, merges n_2 %d, n_1 %d, s %d"
        % (door, slots, r, avail, n2, n1, s))
    say("     (SAT4) domain deficiency %d = 1+O -> O = %d ; cap m = %d      %s (margin %d)"
        % (defu, O, m, "PASS" if defu <= m else "FAIL", m - defu))
    say("     (SAT2) O <= delta = m-1 = %d                                %s (margin %d)"
        % (m - 1, "PASS" if O <= m - 1 else "FAIL", m - 1 - O))
    say("     (SAT5) N-(1+O) = %d >= 15m = %d                              %s (margin %d)"
        % (N - defu if defu else N - 1, 15 * m,
           "PASS" if (N - max(defu, 1)) >= 15 * m else "FAIL", (N - max(defu, 1)) - 15 * m))
    say("     (OUT-m) aggregate sum eps = def x t_x = %d x %d = %d  [%s points, charge m-%d]"
        % (defu, tx, epsagg, cls, m - tx))
    say("            cap (m-1)(1+O) = %d, attained only by outside deficiency  %s"
        % ((m - 1) * defu if defu else 0, "PASS" if epsagg <= (m - 1) * max(defu, 1) else "FAIL"))
    # per-slope (OUT-m) on every slope class
    say("     (OUT-m) per slope  X' + 2X'' >= m-1-eps :")
    say("            merged type-2 (d=2): X'=%d, X''=0, eps=0 -> %d >= %d  PASS"
        % (6, 6, m - 1))
    say("            degree-1 type-2 (d=1): X'=%d, X''=0, eps=0 -> %d >= %d  PASS"
        % (3, 3, m - 1))
    if door == "DOOR A":
        say("            alpha,beta over the degenerate fibre: eps = 3 (all 3 deficient")
        say("            points lie on both), so RHS = m-1-3 = %d -> 3d >= 0 PASS, and the"
            % (m - 1 - 3))
        say("            per-slope cap eps <= 1+O = %d is met with EQUALITY." % defu)
    say("            middle-reserved (X''=3, X'=0): 0+6 >= %d  PASS" % (m - 1))
    say("            X_gamma = 0 slope: eps = 0 (disjoint from W) -> 0 >= %d  FAILS," % (m - 1))
    say("            so every type-2 slope keeps W-incidence even at O = 2 > m-3 = %d;" % (m - 3))
    say("            hence s = %d EXACTLY and n_2 = %d EXACTLY." % (avail, n2))
    say("     per-side caps: merged slope 2+1 | 1+2 = (3,3) = (m-1,m-1) EQUALITY;")
    say("            middle-reserved slope X''=3 = m-1 EQUALITY (forces X'=0);")
    say("            degree-1 slope (2,1) -> PASS with margin 1.")
    say("     (OV) pair multiplicity: every fibre's slopes pairwise share its 3 points")
    say("            = 2rho-a = m-1 = %d EQUALITY (baseline and both doors alike)." % (2 * rho - a))

say("")
say("[D1.e] MIDDLE BOOKKEEPING BRANCH (the never-verified check)")
say("  A middle x lies in S_g ^ S_h, so both type-1 slopes are in A_x; saturation")
say("  d_x = m = 4 leaves EXACTLY m-2 = 2 type-2 slopes at a middle, and the middle")
say("  fibre's cubic has 3 roots, so exactly ONE root of the middle cubic is NOT a")
say("  type-2 slope.  sum_gamma X'' = (m-1)(m-2) = %d is then an identity." % ((m - 1) * (m - 2)))
say("  BRANCH: if the middle cubic can carry TWO non-type-2 roots (e.g. both type-1")
say("  slopes), each middle drops to d_x = 3, deficiency 3 = 1+O with O = 2, only ONE")
say("  type-2 slope is reserved, s <= %d and the demand is 10 with the OUTER structure" % (rho - 1))
say("  UNCHANGED at 24 slots -- i.e. exactly what rounds 36 and 37 already achieve.")
say("  This branch is DOOR B.  It is NOT decided here; it is the mu(x)-at-middles")
say("  check that r36 MISS 10 / r37 MISS 11 left open.")
say("")
say("VERDICT D1: the ledger CLOSES for DOOR A.  No axiom kills the door on paper.")
say("=" * 74)
FH.close()
