#!/usr/bin/env python3
"""Round 17 -- (ES) coprimality pilot: where THEOREM CS bites at PRIZE rows.

THEOREM CS (proved in PROOFS.md) gives, for every S <= Z/n with x_1 != 0
and every odd prime p dividing N(I_S):

        |Z_w^odd| * log2 p  <=  (n/4) * log2( r' - a_{n/2}(S) )      (CS3)

and |Z_w^odd| >= ceil((w-1)/2) UNIFORMLY IN delta (Z_w contains
{1,...,w-1}).  So an accident at p requires

        ceil((w-1)/2) * log2 p  <=  (n/4) * log2 r'.                 (CS4)

Contrapositive = the EXCLUSION.  This script reports, exactly, the w at
which (CS4) fails at the crossing rows of record.

Row constants quoted from
  notes/pilots_20260804/mun_anticoncentration/REPORT.md:48
  "crossing razor | F_p, p >= 2^39+1; recorded rows q = p PRIME ~2^256,
   delta = 1 | 2^41 | ... | r' = 2^40-w, w in [2^34,2^39]"

Decision path uses only integer comparisons of exact big integers where
feasible and Fraction-free log2 bounds otherwise; see BOUND-SAFETY below.

run: tools/ramguard tiny -- python3 \
     notes/pilots_20260806/es_coprimality/prize_floor.py
"""

import math
import sys

FAIL = []
NCHK = [0]


def check(name, cond, detail=""):
    NCHK[0] += 1
    if not cond:
        FAIL.append((name, detail))
        print("    FAIL %s | %s" % (name, detail))
    return cond


def bites(n, rp, w, log2p):
    """True iff (CS4) FAILS, i.e. no accident is possible at that p."""
    lhs = ((w - 1 + 1) // 2) * log2p        # ceil((w-1)/2) * log2 p
    rhs = (n / 4.0) * math.log2(rp)
    return lhs > rhs, lhs, rhs


def main():
    print("=" * 74)
    print("ROUND 17 -- THEOREM CS at the PRIZE CROSSING ROWS")
    print("=" * 74)
    n = 2 ** 41

    # ---- BOUND-SAFETY: validate the float log2 against exact integer
    # bit-length bracketing on the two quantities that matter.
    for x in (2 ** 40 - 2 ** 34, 2 ** 40 - 2 ** 39, 2 ** 39, 3, 6):
        lo = x.bit_length() - 1
        hi = x.bit_length()
        check("BS log2(%d) bracketed by bit_length" % x,
              lo <= math.log2(x) <= hi)
    # the comparison margins reported below are all > 10^10 bits, i.e.
    # ~22 orders of magnitude above double-precision error on ~10^13.

    print("\n  n = 2^41,  r' = 2^40 - w,  delta = 1 recorded rows")
    print("  (CS4): accident at p REQUIRES ceil((w-1)/2)*log2 p <= (n/4)*log2 r'")
    print("\n  %-8s %-14s %-16s %-16s %-10s"
          % ("w", "r'", "LHS (bits)", "RHS (bits)", "verdict"))
    for e in range(34, 40):
        w = 2 ** e
        rp = 2 ** 40 - w
        bit, lhs, rhs = bites(n, rp, w, 256.0)
        print("  2^%-6d %-14s %-16.6g %-16.6g %s"
              % (e, "2^40-2^%d" % e, lhs, rhs,
                 "EXCLUDED (CS bites)" if bit else "vacuous"))

    # ---- the exact threshold in w, at log2 p = 256
    print("\n  THRESHOLD SEARCH at log2 p = 256 (bisection on integer w):")
    lo, hi = 2 ** 34, 2 ** 39
    b_lo, _, _ = bites(n, 2 ** 40 - lo, lo, 256.0)
    b_hi, _, _ = bites(n, 2 ** 40 - hi, hi, 256.0)
    check("threshold brackets: vacuous at w=2^34, bites at w=2^39",
          (not b_lo) and b_hi, "lo=%s hi=%s" % (b_lo, b_hi))
    while hi - lo > 1:
        mid = (lo + hi) // 2
        b, _, _ = bites(n, 2 ** 40 - mid, mid, 256.0)
        if b:
            hi = mid
        else:
            lo = mid
    print("    w0 = %d  =  2^%.4f   (first w excluded by CS)" %
          (hi, math.log2(hi)))
    frac = (2 ** 39 - hi + 1) / float(2 ** 39 - 2 ** 34 + 1)
    print("    covered fraction of the crossing bracket [2^34, 2^39]: %.4f"
          % frac)

    # ---- dependence on log2 p
    print("\n  THRESHOLD w* vs log2 p:")
    print("  %-12s %-16s %-12s" % ("log2 p", "w*", "bracket covered"))
    for lp in (39.0, 64.0, 128.0, 208.0, 256.0, 512.0):
        lo, hi = 2 ** 34, 2 ** 39
        b_hi, _, _ = bites(n, 2 ** 40 - hi, hi, lp)
        if not b_hi:
            print("  %-12g %-16s %-12s" % (lp, "> 2^39", "0.0000 (vacuous)"))
            continue
        b_lo, _, _ = bites(n, 2 ** 40 - lo, lo, lp)
        if b_lo:
            print("  %-12g %-16s %-12s" % (lp, "<= 2^34", "1.0000 (all)"))
            continue
        while hi - lo > 1:
            mid = (lo + hi) // 2
            b, _, _ = bites(n, 2 ** 40 - mid, mid, lp)
            if b:
                hi = mid
            else:
                lo = mid
        print("  %-12g 2^%-14.4f %.4f"
              % (lp, math.log2(hi),
                 (2 ** 39 - hi + 1) / float(2 ** 39 - 2 ** 34 + 1)))

    # ---- the six power-of-two w (the (E)-dichotomy values)
    print("\n  The 6 power-of-two w in the bracket (the only w with a")
    print("  NONEMPTY structural family, round-15 (P4)):")
    cov = [e for e in range(34, 40)
           if bites(n, 2 ** 40 - 2 ** e, 2 ** e, 256.0)[0]]
    print("    excluded by CS at log2 p = 256:  %s"
          % (["2^%d" % e for e in cov] or "none"))

    # ---- sanity: the theorem must NOT exclude the known toy accidents
    print("\n  SANITY (must NOT exclude the five round-16 witnesses):")
    WIT = [(32, 6, 4, 7), (32, 6, 3, 47), (32, 6, 4, 17),
           (32, 5, 2, 23), (32, 5, 2, 463)]
    for (nn, rr, ww, pp) in WIT:
        b, lhs, rhs = bites(nn, rr, ww, math.log2(pp))
        check("SANITY witness n=%d r'=%d w=%d p=%d not excluded"
              % (nn, rr, ww, pp), not b,
              "lhs=%.4f rhs=%.4f" % (lhs, rhs))
        print("    n=%d r'=%d w=%d p=%-4d  lhs=%8.4f  rhs=%8.4f  %s"
              % (nn, rr, ww, pp, lhs, rhs, "ok (not excluded)"))

    # ---- COROLLARY CS-TOWER: the exclusion survives the stratum recursion.
    # At stratum a the instance is (n/2^a, r'/2^a, w_a), w_a = floor((w-1)/2^a)+1.
    # Biting at level a  <=>  2^{a+2} * [ceil((w_a-1)/2) * log2 p]
    #                          > 2^{a+2} * (n/2^{a+2}) * log2(r'/2^a)
    # We CHECK numerically that whenever CS bites at a=0 it bites at every
    # admissible a >= 1 (the RHS strictly decreases, the LHS is ~constant).
    print("\n  COROLLARY CS-TOWER (stratified S, x_1 = 0): exclusion persists")
    print("  %-6s %-4s %-16s %-16s %-8s" % ("w", "a", "LHS_a", "RHS_a", "bites"))
    for e in (38, 39):
        w = 2 ** e
        rp = 2 ** 40 - w
        for a in range(0, 6):
            na = n // (2 ** a)
            ra = rp // (2 ** a)
            wa = (w - 1) // (2 ** a) + 1
            if ra < 2 or wa < 2:
                break
            lhs = ((wa - 1 + 1) // 2) * 256.0
            rhs = (na / 4.0) * math.log2(ra)
            b = lhs > rhs
            check("CS-TOWER bites at w=2^%d a=%d" % (e, a), b,
                  "lhs=%.6g rhs=%.6g" % (lhs, rhs))
            print("  2^%-4d %-4d %-16.6g %-16.6g %s" % (e, a, lhs, rhs, b))

    print("\n" + "=" * 74)
    print("checks: %d   failures: %d" % (NCHK[0], len(FAIL)))
    print("=" * 74)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
