# FLOOR-BUDGET SLACK SCAN (2026-07-09)
# Codex's retarget tactic (F3: H3-ACT(16) -> H3-ACT(4096), 256x weaker)
# applied to the other floors with printed constants: F4 / F5 / F7.

Status: AUDIT (exact arithmetic + banked-verifier citations; verifier
notes/slack_scan/floor_budget_slack_scan.py, digest
FLOOR_BUDGET_SLACK_SCAN_PASS). Negative results are results: two of
three floors have NO material retarget, and that is now a banked
guardrail rather than an untested hope.

## F5 (xr_smallcore 16n^3): RETARGET-DEAD

Consumer chain: xr_clean_residual_any_gate -> r2_clean_rates, with
sufficiency the poly-forcing compiler (banked, 52/52 exact integers):
16 n^3 <= s_lo(A) at all six clean-rate candidates, prize rows tight
at 29 n^3. Recomputed consistency: 29 * (2^41)^3 = 2^127.86 vs the
banked prize-max allowance ~2^127.9 (match).

  max uniform retune: 16 -> 29, i.e. 0.86 bits. NOTHING to spend.

Consequence for the F5 program: the anti-concentration heart must
deliver the n^3-shaped count essentially as stated; no weaker uniform
target exists. (Sub-prize candidates individually have orders more
room — s_lo ~ 2^122 vs small n^3 — but the uniform-in-row form is
pinned by prize-max, and the consumer consumes the uniform form.)

## F4 (petal n^B): NOT BINDING — the floor has real room

The paid family (banked F4-A2b + Pro floor-window 4) saturates to the
degree-6 binomial column C(core, 6), core = n + c. Exact recompute at
the four official maximal rows n = 2^41..2^44:

  log_n C(n+6,6) = 5.7685 / 5.7740 / 5.7793 / 5.7843  (banked <= 5.785)
  room to B = 6:  ~9.5 bits at every row; the c-sweep column (c = 14)
  has the SAME exponent (degree stays 6; only the base shifts).

So the n^6 budget already carries ~9.5 bits of slack over everything
the instruments have ever produced, and the excess-c growth is
degree-6 binomial — absorbed uniformly. B_max ABOVE 6 is gated by the
codegree-conversion emission (imgfib -> list_safe), not by the paid
family: NAMED OPEN CELL (compute only if the F4 route ever needs
super-6 room; nothing currently does).

## F7 (worst_word envelope): NO FREE SLACK WITHOUT A CONVENTIONS DECISION

Banked QA.22 gate (27/27 exact big integers): the four-column split
fits under B* at all six candidates; prize rows show 27.0 / 60.6+ bits
of WITHIN-COLUMN (staircase) room after the 16n^3 + B_tan reserve, but
the aggregate-vs-B* line at prize rows is 0.9 bits under QA.22's
conservative convention. Spending the within-column room on the
challenger envelope would be a RE-ATTRIBUTION across columns — a
conventions decision governed by the QA.22 notes, not free arithmetic.
FLAGGED, not spent. Until then the envelope certification target
stays as stated (count law ~ K_cell/q^sigma, certified rowwise).

## Scan conclusion

The retarget tactic pays exactly once more beyond F3: F4 (9.5 bits of
standing room + a named path to more). It is provably dead on F5
(0.86 bits) and blocked-pending-conventions on F7 (0.9-bit aggregate
line). The kernel-summit instances therefore cannot be softened by
consumer arithmetic — the mildest-instance ordering (F2 ~2%
sub-balance margin first) stands, and the effective energy dichotomy
(F2 packet, same day) is the intended opener.
