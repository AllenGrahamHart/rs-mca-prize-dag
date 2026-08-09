#!/usr/bin/env python3
"""Cheap structural read of #1148's fixture, straight from the file, using
the SAME parse as their own A_verify_SP01zxaa_Schur_power_profile.py:

    locator_i(X) = prod_{r in U \\ B_i} (X - r),   U = union of the 16 branches

Purposes:
 (1) resolve the 08-03 audit's FLAG F5 (undefined "509 core rows", "1,023-point
     fixture domain", "degree 479");
 (2) measure the PAIRWISE ROOT-SET INTERSECTIONS of the 16 locators, which is
     exactly the hypothesis the (PC3) anticode/packing instrument needs.

Stdlib only, set arithmetic. Run via tools/ramguard tiny.
"""
from math import comb, log2

FIX = ("notes/pilots_20260809/pr_harvest/replay/1148/experimental/data/"
       "certificates/atlas-full-affine-hull/SP01zxa_quadratic_cover_pair_input.txt")
out = []


def P(*a):
    line = " ".join(str(x) for x in a)
    out.append(line)
    print(line)


tok = iter(map(int, open(FIX, encoding="ascii").read().split()))
p = next(tok)
core = [next(tok) for _ in range(next(tok))]
nb = next(tok)
params, branches = [], []
for _ in range(nb):
    a = next(tok)
    b = next(tok)
    params.append((a, b))
    branches.append({next(tok) for _ in range(next(tok))})

U = set().union(*branches)
deg = len(U) - len(branches[0])
P("field p                    =", p, "= 2^31-1?", p == 2 ** 31 - 1)
P("core size                  =", len(core))
P("branch count               =", nb)
P("branch sizes               =", sorted({len(b) for b in branches}))
P("|U| (union of branches)    =", len(U))
P("locator degree |U|-|B_i|   =", deg, " [their stated degree 479 -> %s]" % (deg == 479))
P("core disjoint from U?      =", len(set(core) & U) == 0)
P("|U| + |core|               =", len(U) + len(core),
  " [their stated 1,023-point fixture domain -> %s]" % (len(U) + len(core) == 1023))
P("degenerate parameter pairs =", [(i, params[i]) for i in range(nb) if params[i][1] == 0])
P("")
P("F5 RESOLVED: the '1,023-point fixture domain' is  U (514 branch roots)")
P("            DISJOINT-UNION core (509 evaluation points); each locator is")
P("            monic of degree |U|-35 = 479 with all roots inside U; the")
P("            '509 core rows' are the evaluation coordinates.")
P("")

# pairwise root-set intersections
pair = []
for i in range(nb):
    for j in range(i + 1, nb):
        # roots_i = U \ B_i ; |roots_i cap roots_j| = |U| - |B_i union B_j|
        inter = len(U) - len(branches[i] | branches[j])
        pair.append((inter, i, j))
mn = min(x[0] for x in pair)
mx = max(x[0] for x in pair)
P("PAIRWISE ROOT-SET INTERSECTIONS of the 16 split locators (%d pairs)" % len(pair))
P("   min = %d   max = %d   (degree = %d)" % (mn, mx, deg))
P("   distribution:", sorted({x[0] for x in pair}))
P("")
P("(PC3) HYPOTHESIS TEST -- l1_rootfree_rational_q_projective_packing")
P("   (PC3) is stated for a space V with dim V = D+1 whose distinct members")
P("   have root-set intersection <= D-1.  Here the linear span has dim 16, so")
P("   (PC3) would need pairwise intersection <= 14.  MEASURED max = %d." % mx)
P("   => (PC3) AS LITERALLY STATED DOES NOT APPLY to #1148's flat: %s"
  % ("confirmed (max %d > 14)" % mx if mx > 14 else "it would apply"))
P("")
P("   The honest packing ceiling at the MEASURED overlap cap r = %d is" % mx)
r = mx
ceil_meas = comb(1023, r + 1) // comb(deg, r + 1)
P("      C(1023,%d)/C(479,%d) = %d   (log2 = %.3f)  vs TRUTH 16 (log2 4.000)"
  % (r + 1, r + 1, ceil_meas, log2(ceil_meas)))
P("      looseness at the measured overlap cap: 2^%.3f" % (log2(ceil_meas) - 4.0))
P("")
P("   SELF-CORRECTION to mystery7_calibration.py: the dimension-driven")
P("   ceiling C(1023,15)/C(479,15) = %d (log2 %.3f) is NOT a valid bound"
  % (comb(1023, 15) // comb(479, 15), log2(comb(1023, 15) // comb(479, 15))))
P("   here, because (PC3)'s overlap hypothesis fails by a factor of 30. It is")
P("   only 'what the instrument would give IF its hypothesis tracked the")
P("   dimension'. The VALID anticode ceiling at this flat is the 2^%.1f one."
  % (log2(ceil_meas) - 4.0))
P("")
P("=" * 74)
P("THE COMPLEMENT (BRANCH) COORDINATES -- a concrete instrument lead")
P("=" * 74)
bpair = [(len(branches[i] & branches[j]), i, j)
         for i in range(nb) for j in range(i + 1, nb)]
bmx = max(x[0] for x in bpair)
P("  root sets are complements: roots_i = U \\ B_i, |B_i| = 35 inside |U| = 514.")
P("  |roots_i cap roots_j| = |U| - 70 + |B_i cap B_j| = 444 + |B_i cap B_j|.")
P("  MEASURED branch intersections |B_i cap B_j|: max = %d, distribution %s"
  % (bmx, sorted({x[0] for x in bpair})))
P("  So the 16 branches are 35-subsets of a 514-set, pairwise meeting in <= %d"
  % bmx)
P("  points (and 16*35 = %d > 514, so they cannot be disjoint)." % (16 * 35))
cc = comb(len(U), bmx + 1) // comb(35, bmx + 1)
P("  ANTICODE BOUND IN THE COMPLEMENT: C(%d,%d)/C(35,%d) = %d (log2 %.3f)"
  % (len(U), bmx + 1, bmx + 1, cc, log2(cc)))
P("  vs TRUTH 16  ->  LOOSENESS 2^%.3f" % (log2(cc) - 4.0))
P("")
P("  THE SAME INSTRUMENT IN THE SAME COORDINATES AT OUR OWN FIXTURE")
P("  (l1_m31_fixed_support_divisor_direction_cap_route_cut, PROVED):")
P("     J_a = R*(X-a), a in S \\ R0, |R0| = t-1 = 4979, |S| = m = 72428.")
P("     every pair shares exactly |R0| = 4979 = deg-1 roots (MAXIMAL overlap).")
P("     the sunflower-core count is EXACT: m - (t-1) = %d = the node's %d"
  % (72428 - 4979, 67449))
P("     looseness 2^0.000 -- the right instrument is EXACT there.")
P("")
P("  READ-OFF (CANDIDATE lead for mystery 7, not a theorem):")
P("    at BOTH exhibited flats the members share almost all their roots")
P("    (overlap/degree = %.4f theirs, %.4f ours), which is exactly the regime"
  % (mx / deg, 4979 / 4980))
P("    where a root-coordinate anticode/packing argument is empty. Changing")
P("    coordinates to the small SYMMETRIC-DIFFERENCE data (branch sets there,")
P("    the sunflower core here) turns a 2^%.0f-vacuous instrument into one that"
  % (log2(ceil_meas) - 4.0))
P("    is 2^%.1f loose (theirs) and EXACT (ours)." % (log2(cc) - 4.0))

with open("notes/pilots_20260809/pr_harvest/fixture1148.txt", "w") as f:
    f.write("\n".join(out) + "\n")
