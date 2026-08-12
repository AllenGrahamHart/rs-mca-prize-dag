#!/usr/bin/env python3
"""The type-2 spend/list ledger is VACUOUS BY SIGN on the whole open bracket.

Source: critical/nodes/rate_half_band_crossing_location/statement.md
        L3613-3625 (Round-35 R-FG-RAZOR addendum, round 35 bank 2).

(C2)'s per-slope floor is (R+1) - w* with w* = |W| = |S_g u S_h| in [r, 2r].
It is positive for EVERY admissible W iff 2r <= R iff a >= 3n/4 -- exactly
the top of the open bracket (the unique-decoding radius).  At razor shape the
adversary takes w* = 2r and the floor is -1,065,151,889,407: vacuous BY SIGN,
not by slack.

Checks
  A. the razor sign arithmetic to the digit;
  B. the equivalence chain 2r <= R  <=>  a >= 3n/4  (exactly, at rate 1/2),
     over a wide integer range and at razor;
  C. the adversary threshold |S_g ^ S_h| >= 2r - R = 62r/63 = 98.412...% of
     r, i.e. adversary-free;
  D. one small cell worked end to end;
  E. that the whole open bracket [k+2^34, 3n/4) lies on the vacuous side.

Stdlib only; nothing imported.
Run: tools/ramguard tiny -- python3 <this file>   (RAMGUARD_TIMEOUT 60s)
"""

from fractions import Fraction

FAIL = []


def bad(m):
    FAIL.append(m)


# ------------------------------------------------------------- razor shape
N = 2 ** 41
K = 2 ** 40
R = N - K                       # = 2^40
RHO = 2 ** 34
A = K + RHO                     # the crossing offset
r = N - A                       # = R - rho = 63*rho

if (R, r, A) != (1099511627776, 1082331758592, 1116691496960):
    bad("razor constants: (R,r,a) = %s" % ((R, r, A),))

# ------------------------------------------------------------------- A
def c2_floor(R_, wstar):
    return (R_ + 1) - wstar


adversary_wstar = 2 * r         # the adversary maximises |W|
floor_razor = c2_floor(R, adversary_wstar)
if floor_razor != -1065151889407:
    bad("razor floor %d, banked -1065151889407" % floor_razor)
if floor_razor >= 0:
    bad("the razor floor is not negative -- the fence would not be by sign")

# the floor is positive at the OTHER end of the admissible range only if...
if c2_floor(R, r) <= 0:
    bad("even at w* = r the floor is nonpositive at razor")   # sanity: it is
# ... and w* = r means |S_g ^ S_h| = r, i.e. the two supports COINCIDE.

# ------------------------------------------------------------------- B
def bracket_equivalences(n, a):
    """at rate one half: k = n/2, R = n-k = n/2, r = n-a."""
    k = Fraction(n, 2)
    R_ = n - k
    r_ = n - a
    return (2 * r_ <= R_, Fraction(a) >= Fraction(3 * n, 4), r_, R_)


for n in range(8, 400, 2):
    for a in range(1, n + 1):
        lhs, rhs, _, _ = bracket_equivalences(n, a)
        if lhs != rhs:
            bad("2r<=R  <=>  a>=3n/4 fails at (n,a) = (%d,%d)" % (n, a))
            break
    else:
        continue
    break

lhs, rhs, _, _ = bracket_equivalences(N, A)
if lhs or rhs:
    bad("the crossing offset should be on the VACUOUS side: 2r<=R is %s, "
        "a>=3n/4 is %s" % (lhs, rhs))
if 2 * r <= R:
    bad("2r <= R at razor -- the ledger would not be vacuous")

# ------------------------------------------------------------------- C
thresh = 2 * r - R
if thresh != 62 * RHO:
    bad("2r-R = %d, want 62*rho" % thresh)
if Fraction(thresh, r) != Fraction(62, 63):
    bad("2r-R is not 62r/63")
pct = float(Fraction(62, 63)) * 100
if abs(pct - 98.412698) > 1e-5:
    bad("threshold percentage %.6f, banked 98.41%%" % pct)
if thresh > r:
    bad("the threshold exceeds r, so it would be unattainable rather than "
        "adversary-free")

# ------------------------------------------------------------------- D
# one small cell: n=22, k=11, R=11, rho=2, r=9, a=13.
n0, k0, rho0 = 22, 11, 2
R0 = n0 - k0
r0 = R0 - rho0
a0 = n0 - r0
if (R0, r0, a0) != (11, 9, 13):
    bad("small cell shape %s" % ((R0, r0, a0),))
if c2_floor(R0, 2 * r0) != 12 - 18:
    bad("small cell floor arithmetic")
if c2_floor(R0, 2 * r0) >= 0:
    bad("small cell floor should be negative")
if 2 * r0 <= R0:
    bad("small cell should be on the vacuous side")
if Fraction(a0, n0) >= Fraction(3, 4):
    bad("small cell should have a < 3n/4")
if 2 * r0 - R0 != 7:
    bad("small cell threshold")

# ------------------------------------------------------------------- E
# every offset in [k+2^34, 3n/4) is vacuous by sign.
# NOTE the bracket is HALF-OPEN: a = 3n/4 = K + 2^39 is its excluded top,
# where the floor is exactly +1.  Every a strictly below it is vacuous.
a_top = (3 * N) // 4
if a_top != K + 2 ** 39:
    bad("3n/4 is not k + 2^39 at rate one half")
for a in (A, A + 1, A + 2 ** 30, K + 2 ** 38, a_top - 1):
    if not (A <= a < a_top):
        bad("test offset a=%d is outside the open bracket" % a)
    rr = N - a
    if c2_floor(R, 2 * rr) >= 0:
        bad("offset a=%d is NOT vacuous by sign" % a)
# and at the excluded top the sign flips exactly, to +1.
if c2_floor(R, 2 * (N - a_top)) != 1:
    bad("the floor at a = 3n/4 is %d, want exactly +1"
        % c2_floor(R, 2 * (N - a_top)))

if FAIL:
    for m in FAIL:
        print("FAIL " + m)
    raise SystemExit(1)
print("TYPE2_LEDGER_SCOPE_FENCE_PASS razor (C2) floor at w*=2r is %d "
      "(banked to the digit); 2r<=R <=> a>=3n/4 verified for all even "
      "n<=398 and at razor; threshold 2r-R = 62r/63 = %.6f%% of r "
      "(adversary-free); small cell n=22 gives floor %d and threshold %d; "
      "the whole bracket [k+2^34, 3n/4) is vacuous by sign and the sign "
      "flips exactly at a = 3n/4"
      % (floor_razor, pct, c2_floor(R0, 2 * r0), 2 * r0 - R0))
