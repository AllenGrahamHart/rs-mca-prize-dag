#!/usr/bin/env python3
"""D2/D3: the mystery-7 calibration exhibit.

MYSTERY 7 (roadmap sec.12 r5) needs a max-to-mean bound for monic SPLIT
LOCATORS in a linear/congruence flat whose projective dimension grows with n,
UNIFORM IN THE DIMENSION.  The instrument that fails is the anticode/packing
ceiling (PC3) of background/nodes/l1_rootfree_rational_q_projective_packing:

    |P(V) cap Dloc_j(H')|  <=  floor( C(n', D) / C(j, D) ),   D = dim V - 1

whose exponent D grows with the flat dimension.  This script prices (PC3)
against the TRUTH at the only two exhibited fixtures in the M31 family:

  OURS   background/nodes/l1_m31_fixed_support_divisor_direction_cap_route_cut
         (PROVED): dim V = 6, degree t = 4980, support m = 72428,
         split members = m - t + 1 = 67449.
  THEIRS maelcar PR #1148 (synthesis PROVED-replayed by this pilot):
         affine_dimension = 15, vertex_count = 16, degree 479, domain 1023,
         split members in the hull = exactly 16.

Stdlib only, exact integers. Run via tools/ramguard tiny.
"""
from math import comb, log2

P31 = 2 ** 31 - 1
out = []


def P(*a):
    line = " ".join(str(x) for x in a)
    out.append(line)
    print(line)


def price(tag, npts, deg, dimV, truth, field=P31):
    """dimV = dimension of the LINEAR span; (PC3) exponent D = dimV - 1."""
    D = dimV - 1
    pack = comb(npts, D) // comb(deg, D)
    # mean: expected number of split degree-`deg` monic locators on `npts`
    # points inside a uniformly random projective flat of the same dimension.
    #   #split classes   = C(npts, deg)
    #   ambient classes  ~ (p^(deg+1)-1)/(p-1)   [monic deg<=`deg` normalised]
    #   flat classes     ~ (p^dimV-1)/(p-1)
    lg_split = log2(comb(npts, deg))
    lg_amb = (deg) * log2(field)          # |P(F[X]_{<=deg})| ~ p^deg
    lg_flat = (dimV - 1) * log2(field)    # |P(V)| ~ p^(dimV-1)
    lg_mean = lg_split + lg_flat - lg_amb
    P("  %s" % tag)
    P("     points n'=%d  degree=%d  dim V=%d (projective dim %d)  TRUTH=%d"
      % (npts, deg, dimV, D, truth))
    P("     (PC3) packing ceiling  C(%d,%d)/C(%d,%d) = %d   (log2 = %.3f)"
      % (npts, D, deg, D, pack, log2(pack)))
    P("     TRUTH log2 = %.3f    ->  INSTRUMENT LOOSENESS = 2^%.3f (factor %.4g)"
      % (log2(truth), log2(pack) - log2(truth), pack / truth))
    P("     mean over a random flat of the same dim: log2 = %.2f" % lg_mean)
    P("     MAX-TO-MEAN (what mystery 7 must bound): 2^%.2f" % (log2(truth) - lg_mean))
    return log2(pack) - log2(truth), log2(truth) - lg_mean


P("!! SELF-CORRECTION, READ FIRST: the DIMENSION-DRIVEN ceilings computed")
P("!! below assume (PC3)'s overlap hypothesis (distinct members share <= D-1")
P("!! roots). fixture1148.py MEASURED the actual overlaps -- 446 of 479")
P("!! (theirs) and 4979 of 4980 (ours) -- so that hypothesis FAILS at BOTH")
P("!! fixtures and these ceilings are NOT valid bounds. They are kept only as")
P("!! 'what the instrument would give if its parameter tracked the dimension'.")
P("!! The VALID numbers, and the instrument lead, are in fixture1148.txt.")
P("")
P("=" * 78)
P("MYSTERY-7 CALIBRATION: the (PC3) anticode/packing ceiling vs the truth")
P("at the two exhibited M31 split-locator flats (p = 2^31-1)")
P("=" * 78)
a_loose, a_mm = price("OURS  l1_m31_fixed_support_divisor_direction_cap_route_cut (PROVED)",
                      72428, 4980, 6, 67449)
P("")
b_loose, b_mm = price("THEIRS maelcar #1148 full-affine-hull rigidity (synthesis replayed)",
                      1023, 479, 16, 16)
P("")
P("=" * 78)
P("THE CALIBRATION (this is the new content)")
P("=" * 78)
P("  flat dim  6 (proj 5):  instrument loose by 2^%.3f" % a_loose)
P("  flat dim 16 (proj 15): instrument loose by 2^%.3f" % b_loose)
P("  looseness GROWTH across the two exhibited dimensions: 2^%.3f" % (b_loose - a_loose))
P("  per extra projective dimension: 2^%.4f  (over %d dimensions)"
  % ((b_loose - a_loose) / (15 - 5), 15 - 5))
P("")
P("  DIRECTION CHECK (the reason a dimension-uniform theorem is not obviously")
P("  false and not obviously easy): the LOWER-dimensional flat carries VASTLY")
P("  MORE split members.")
P("     dim  6 -> 67449 split members")
P("     dim 16 ->    16 split members")
P("  so 'more dimensions => more split members' is FALSE as a monotone")
P("  principle, exactly as l1_m31_fixed_support_divisor_direction_cap_route_cut")
P("  already recorded; #1148 supplies the missing HIGH-dimension data point.")
P("")
P("  MAX-TO-MEAN, the quantity mystery 7 must bound uniformly:")
P("     dim  6 : 2^%.2f" % a_mm)
P("     dim 16 : 2^%.2f" % b_mm)
P("")
P("SANITY: hand-checkable identities from the #1148 synthesis (replayed)")
P("  2^16 - 1                    =", 2 ** 16 - 1, "(all nonempty supports)")
P("  sum_{s=9}^{16} C(16,s)      =", sum(comb(16, s) for s in range(9, 17)))
P("  C(16,8)                     =", comb(16, 8))
P("  136 = C(17,2) = k(k+1)/2    =", comb(17, 2), "-> Schur square MAXIMAL at k=16")
P("  GRS would give 2k-1         =", 2 * 16 - 1)
P("  primary vs audit normals    = 10694457224 vs 10694457231, difference =",
  10694457231 - 10694457224, "(FLAG F4 still open)")

with open("notes/pilots_20260809/pr_harvest/mystery7_calibration.txt", "w") as f:
    f.write("\n".join(out) + "\n")
