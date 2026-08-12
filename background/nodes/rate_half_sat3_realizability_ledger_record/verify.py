#!/usr/bin/env python3
"""The (SAT3) realizability-ledger record: three independent corrections,
their stacking, and the C(16m,4m-1) first-moment gate's m=1 calibration.

Source: critical/nodes/rate_half_band_crossing_location/statement.md
        L3428-3439 (round 34: the automorphism quotient; TCAP-DIM re-posed),
        L4380-4396 (round 36: the (ERC2)-forced dim 18 and the stacking),
        L3846-3860 (round 35: the C(16m,4m-1) gate and its double
        calibration at m=1), L3403-3407 (the (L2) overdetermination row),
        L3497-3505 / L3588-3595 (DEF-ID, posed then closed as coincidence).

STATUS: HEURISTIC / RECORD.  Not one of these instruments is a mechanism.
The round-36 close is explicit that counting died as a verdict-carrier three
more times in this lane; this package records the ledger, it does not price
the conclusion.

Checks
  A. the (L2) overdetermination row 4m^2-7m+2 = -1,+4,+17,+38 at m=1..4, and
     that it equals the (BIV-G) deficit 7m^2-9m+2 - (3m^2-2m) identically;
  B. DEF-ID: (m+2)(4m+1) + m(3m-2) = (m-1)(7m-2) + 16m = 7m^2+7m+2, an exact
     identity -- and CLOSED AS A COINCIDENCE, since the shared quantity
     governs neither layer's existence;
  C. the ledger corrections and their stacking: the (ERC2)-forced ambient
     dimension 18 = 23-5 turning the m=2 cell from -1-O into +4-O; the
     automorphism quotient +4..+6; the stacked +8..+10; the preserved
     controls (m=1 at -9..-7, the e=1 ladder -8m-1 < 0 for every m, the
     locator-layer bookkeeping -5 at m=2 and +7 at m=1);
  D. the gate at m=1: C(16m,4m-1) = C(16,3) = 560, the 16 = 16 coincidence,
     and the overestimate 13.75 - log2(16) = 9.75 ~ the banked 2^9.8.

Stdlib only; nothing imported.
Run: tools/ramguard tiny -- python3 \
  background/nodes/rate_half_sat3_realizability_ledger_record/verify.py
(RAMGUARD_TIMEOUT 60s)
NOTE (D9, resolved at wiring): this verifier deliberately refuses to
recompute the gate's bits -- that stance predates the formula's recovery.
The recovered expression (r35_rout_layer_a/REPORT.md, section D3.3) is
carried in statement.md and COMPUTED at both calibration points by
verify_audit.py.
"""

from math import comb, log2

FAIL = []
FLAG = []


def bad(m):
    FAIL.append(m)


# ------------------------------------------------------------------- A
row = [4 * m * m - 7 * m + 2 for m in (1, 2, 3, 4)]
if row != [-1, 4, 17, 38]:
    bad("(L2) overdetermination row %s, want [-1,4,17,38]" % row)
for m in range(1, 60):
    raw = (m + 2) * (4 * m + 1) - 16 * m
    if raw != 4 * m * m - 7 * m + 2:
        bad("raw (L2) deficit mismatch at m=%d" % m)
    bivg = (7 * m * m - 9 * m + 2) - (3 * m * m - 2 * m)
    if bivg != 4 * m * m - 7 * m + 2:
        bad("(BIV-G) deficit mismatch at m=%d" % m)
    reduced = m * (4 * m + 1) - (8 * m - 2)
    if reduced != 4 * m * m - 7 * m + 2:
        bad("reduced (L2) deficit mismatch at m=%d" % m)
neg = [m for m in range(1, 60) if 4 * m * m - 7 * m + 2 < 0]
if neg != [1]:
    bad("the deficit is negative at %s, want only m=1" % neg)

# ------------------------------------------------------------------- B
for m in range(1, 60):
    lhs = (m + 2) * (4 * m + 1) + m * (3 * m - 2)
    mid = (m - 1) * (7 * m - 2) + 16 * m
    rhs = 7 * m * m + 7 * m + 2
    if not (lhs == mid == rhs):
        bad("DEF-ID fails at m=%d: %d %d %d" % (m, lhs, mid, rhs))
# closed as a coincidence: the shared quantity governs NEITHER existence.
# (L2) is nonempty at m=2 despite +4; (BIV-G) is realizable at m=3 despite
# +17.  Both are recorded facts elsewhere in the bank, asserted here as the
# reason the identity carries no weight.
if 4 * 2 * 2 - 7 * 2 + 2 != 4 or 4 * 3 * 3 - 7 * 3 + 2 != 17:
    bad("the two counterexample deficits are not +4 and +17")

# ------------------------------------------------------------------- C
# curve side: (ERC2) forces e = m for (SAT3), so the curve lies on the
# 18-dimensional (L2) component, not the ambient 23-dimensional space.
if 23 - 5 != 18:
    bad("ambient correction 23-5 != 18")
CURVE_CORRECTION = 5
m2_round33 = -1                       # the round-33 cell, modulo -O
m2_after_erc2 = m2_round33 + CURVE_CORRECTION
if m2_after_erc2 != 4:
    bad("the m=2 cell should flip from -1-O to +4-O, got %+d" % m2_after_erc2)

# solution-orbit side: the automorphism group acts freely, orbit dim >= 4
# (AGL_1 x AGL_1) and >= 6 generically (PGL_2 x PGL_2).
AUT_LO, AUT_HI = 4, 6
r34_corrected = (m2_round33 + AUT_LO, m2_round33 + AUT_HI)
if r34_corrected != (3, 5):
    bad("round-34 corrected m=2 excess %s, banked +3..+5" % (r34_corrected,))

stacked = (m2_after_erc2 + AUT_LO, m2_after_erc2 + AUT_HI)
if stacked != (8, 10):
    bad("stacked m=2 excess %s, banked +8..+10" % (stacked,))

# preserved controls
if not all(-8 * m - 1 < 0 for m in range(1, 200)):
    bad("the e=1 ladder is not negative at every m")
m1_band = (-9, -7)
if not (m1_band[0] < 0 and m1_band[1] < 0):
    bad("the m=1 control should stay negative")
locator = {1: 7, 2: -5}
if not (locator[1] > 0 > locator[2]):
    bad("the locator-layer bookkeeping should agree in VERDICT with the "
        "corrected ledger: positive-excess at m=1 is the realized cell")
FLAG.append("the independent locator-layer bookkeeping (-5 at m=2, +7 at "
            "m=1) has the OPPOSITE SIGN CONVENTION to the TCAP ledger "
            "(+3..+5 at m=2, -9..-7 at m=1); the source states the two "
            "'agree in verdict', which is only true after the sign flip. "
            "Recorded so no future reader adds the two rows")

# ------------------------------------------------------------------- D
gate = {m: comb(16 * m, 4 * m - 1) for m in (1, 2, 3, 4)}
if gate[1] != 560:
    bad("C(16,3) = %d, want 560" % gate[1])
if gate[2] != comb(32, 7) or gate[2] != 3365856:
    bad("C(32,7) = %d, want 3365856" % gate[2])
# the 16 = 16 double calibration at q = 17
CALIB_BITS_Q17 = 13.75
REALIZED = 16
if abs(CALIB_BITS_Q17 - log2(REALIZED) - 9.75) > 1e-9:
    bad("the overestimate is not 13.75 - 4 = 9.75 bits")
if abs((CALIB_BITS_Q17 - log2(REALIZED)) - 9.8) > 0.06:
    bad("9.75 bits does not round to the banked 2^9.8")
if log2(REALIZED) != 4.0:
    bad("16 is not 2^4")
CALIB_BITS_Q97 = -0.94
if CALIB_BITS_Q97 >= 0:
    bad("the q=97 calibration should be negative (nothing realized there)")
FLAG.append("the C(16m,4m-1) first-moment gate's EXPRESSION is never "
            "printed in the addendum -- only its calibrated values "
            "(+13.75 bits at q=17, -0.94 at q=97, ~-1952 m^2 bits at "
            "official scale, -61.3 at q=97 after the dim-18 sharpening). "
            "Those values are NOT mutually reconstructible: a pure power "
            "law through the two m=1 points needs exponent 5.85, and "
            "-0.94 - 2*log2(97) = -14.1, not -61.3.  The formula must be "
            "recovered from the pilot before this gate is ever re-priced")

if FAIL:
    for m in FAIL:
        print("FAIL " + m)
    raise SystemExit(1)
print("SAT3_LEDGER_CORRECTIONS_PASS (L2) row %s negative only at m=1 and "
      "equal to the (BIV-G) and reduced deficits identically; DEF-ID exact "
      "for m=1..59 and coincidental (nonempty at +4, realizable at +17); "
      "m=2 cell -1-O -> +4-O (ERC2, 23-5=18) and +3..+5 (automorphism "
      "quotient), stacked +8..+10; controls preserved (m=1 -9..-7, e=1 "
      "ladder -8m-1<0); gate C(16m,4m-1) = %s; m=1 calibration 16=16 with "
      "a %.2f-bit overestimate"
      % (row, [gate[m] for m in (1, 2, 3, 4)], CALIB_BITS_Q17 - log2(REALIZED)))
for f in FLAG:
    print("FLAG " + f)
