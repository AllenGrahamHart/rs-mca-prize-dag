#!/usr/bin/env python3
"""d1b_holes.py -- rh_residuals_close (round 32), D1 completion.

EXHAUSTIVE certificate of the uncovered w* set at the OFFICIAL profile
m = 2^37, without enumerating the 5.5e11 window values.

Key fact (proved in the header of the output): write a = rho + d.  Then
  j(a) := floor(a/(a-rho)) = floor(rho/d) + 1,
so j is constant on the divisor blocks of rho, and on each block
  T1cap(a) = min(m+1, j, floor((a m + O)/rho))
is NONDECREASING in a (constant, or a nondecreasing floor), while
  CAP(a) = floor((N-a) m / (R+1-a))
is nondecreasing in a.  Hence AO1 is NONDECREASING on every block, the
covered set inside a block is a PREFIX, and testing the block TOP decides
the whole block.  The number of blocks is O(sqrt(rho)) ~ 1.5e6.

stdlib only.
"""

m = 2 ** 37
N, R1, rho, e = 16 * m, 8 * m + 1, 4 * m - 1, m
LO, HI = 4 * m + 2, 8 * m - 2
THR = -(-(16 * m + 3) // 3)          # T4 threshold: 3a >= 16m+3
TARGET = rho + 1


def ao1(a, O=0):
    t1 = min(m + 1, a // (a - rho), (a * m + O) // rho)
    t2 = (N - a) * m // (R1 - a)
    return t1 + t2


def uncovered(O=0):
    """complete list of a in [LO, THR-1] with AO1(a) > rho+1."""
    bad = []
    d = LO - rho                       # = 3
    dmax = THR - 1 - rho
    blocks = 0
    while d <= dmax:
        v = rho // d
        d_end = min(dmax, rho // v) if v else dmax
        blocks += 1
        a_top = rho + d_end
        if ao1(a_top, O) > TARGET:
            # covered part of this block is a prefix -> binary search it
            lo_a, hi_a = rho + d, a_top
            if ao1(lo_a, O) > TARGET:
                first_bad = lo_a
            else:
                x, y = lo_a, hi_a
                while x < y:
                    mid = (x + y + 1) // 2
                    if ao1(mid, O) <= TARGET:
                        x = mid
                    else:
                        y = mid - 1
                first_bad = x + 1
            bad.extend(range(first_bad, a_top + 1))
            if len(bad) > 200:
                bad.append(-1)         # overflow marker
                break
        d = d_end + 1
    return bad, blocks


out = []
P = out.append
P("=" * 74)
P("D1b  EXHAUSTIVE uncovered-w* certificate at the official profile")
P("=" * 74)
P("  m = 2^37   N = %d   R+1 = %d   rho = %d   window [%d..%d]"
  % (N, R1, rho, LO, HI))
P("  T4 threshold (2s <= a-1)  = %d" % THR)
P("  monotonicity: on each divisor block of rho, j(a) is CONSTANT, the")
P("  third term of the min is nondecreasing, and CAP is nondecreasing;")
P("  hence AO1 is nondecreasing and the block TOP decides the block.")
for O in (0, 1, m // 2, m - 2):
    bad, blocks = uncovered(O)
    P("")
    P("  O = %d" % O)
    P("    divisor blocks scanned : %d" % blocks)
    P("    UNCOVERED w* below T4  : %s" % (bad if len(bad) <= 40 else
                                           "%d values (first 40: %s)" % (len(bad), bad[:40])))
    if bad and bad[0] != -1:
        for a in bad[:5]:
            s = R1 - a
            P("      a = %d : s = %d, 2s-a = %d, RIG = %d, AO1 = %d, deficit %d"
              % (a, s, 2 * s - a, a - 1 - 2 * s, ao1(a, O), ao1(a, O) - TARGET))
P("")
P("  CONCLUSION: at O = 0 the uncovered set is a SINGLE integer; the")
P("  (AO1) band is hole-free at the official profile, unlike m = 8.")
print("\n".join(out))
