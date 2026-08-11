# PREREG — rh_moving_kernel (round 33)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/rh_farca_upper/REPORT.md` (round 32)
2. `background/nodes/rate_half_ca_hankel_fixed_kernel_branch/statement.md`

## Mandate

R-MOVING / R-DEEP: the far-CA deep stratum is the safe half's whole
exposure (UB-NEAR discharged the rest). Round 32 located the crack:
in the wide regime the generic kernel of the syndrome Hankel pencil
is a TWO-GENERATED apolar truncation (generators of degrees p and
R+1-p, both entering since p >= R+1-r); the kernel splits as
(r+1-p) shifts of P and (r+p-R) shifts of Q'; the two multiplicities
sum to 2r+1-R ~ 2^40 while their weighted Kronecker sum is
<= rho <= 2^34 — SO AT LEAST ONE GENERATOR IS FORCED FIXED (defined
over F, slope-independent), and column-farness forbids THAT
generator from being D-split-squarefree — exactly the (HK2)
mechanism's hypothesis, half-satisfied for free. YOUR JOB: bound the
slopes contributed by the OTHER (moving) generator — the wide-regime
replacement for (MI1)/(MI2).

## Deliverables

**D1 — THE FORCED-FIXED LEMMA, proved.** Make round 32's
multiplicity arithmetic a theorem: state exactly which generator
(low or high degree) is forced fixed, under which inequality on
(r, R, rho), with the Kronecker identity quoted (sum eps + sum eta
+ delta = rho). Verify at the round-32 cells (the d6 pencils are
banked in rh_farca_upper/).

**D2 — THE MOVING-GENERATOR BUDGET.** For a bad slope gamma, the
kernel member in D_r(D) (the split locator) decomposes over the two
generators. The fixed generator contributes a FIXED factor
(column-far => not D-split-squarefree). Derive what the moving
generator must supply and bound the slope count: candidate shapes —
a divisor count on the fixed factor's complement (the (MI2) shape
with the fixed generator playing Q_Z), or an (HK2)-style minor
argument on the moving block alone. ANY finite bound on the deep
stratum is the first ever.

**D3 — SMALL-SCALE STRUCTURE.** At the wide-regime cells (copy
rh_farca_upper/d6_kernel_structure.py + d3_wide.py): measure the
two-generator split per bad slope (degrees p, R+1-p; which is
fixed; what the moving factor does at each bad slope). Test D2's
candidate bound against measured T. Pre-register expectations.

**D4 — VERDICT + R-KER cross-check.** Does the bound reach
B_ca^far(k+2^34) < 2^128? If partial, the exact stratum covered.
Cross-check against LB1 (its pencils MUST satisfy your bound —
T = r+1 there; if your bound is < r+1 anywhere LB1 lives, your
bound is WRONG — use LB1 as the built-in falsifier). Misses first.

## Blind priors to register

P(forced-fixed lemma proves cleanly), P(any finite deep-stratum
bound this round), P(the bound beats 2^128 at the razor), which
generator you expect forced (low/high degree).
