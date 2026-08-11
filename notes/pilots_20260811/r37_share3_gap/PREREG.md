# PREREG — r37_share3_gap (round 37)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r36_m4_nonsplit/REPORT.md` (round 36)
2. `notes/pilots_20260811/r34_bivcurve_m34/REPORT.md` (round 34)

## Mandate

THE ONE-COINCIDENCE GAP. Round 36's (SHARE3-4) class reached the
full 8-of-8 target at m = 4 — the first class ever — and missed
the slope budget by ONE (|slopes| = 14 vs 13 required at q=193;
15 vs 13 at q=257; 40000 ALLOC draws per field). The existence
mechanism is exactly understood: the 3-sharing pencils are
CONSTANT-NORM (fixed root-product costs 1/N on mu_N, decay ~q^-7,
threshold ~690 — refuting the naive q^-12 by 3400x). YOUR JOB:
close the gap or harden it. A 13-slope configuration would be an
m = 4 (BIV-CURVE) witness candidate — and then the FULL round-34
pipeline applies: build G, complete outside W, run the bivariate
system on bank-2's own verifier. That would be a major board
event; treat it as the round's prize and the hardening as the
honest default.

## Deliverables

**D1 — THE FULL CONSTANT-NORM CENSUS.** Round 36's exhaustive
censuses covered the constant-(e1,e3) and constant-e3
SUB-families only (its ZP-3), with a sampled base-triple scan for
general lines. Do better: (a) more fields in the live window
(the mechanism says the supply peaks at moderate q — map the
window 97 <= q <= ~690 densely); (b) the FULL constant-norm
family (Delta with zero constant term is one linear condition on
lines — enumerate it exhaustively where affordable, not by
sub-family); (c) per-pencil, the slope-count distribution under
ALLOC (not just the max) — where does the 13-slope tail actually
sit? The registered arithmetic (demand 11, supply band 9-12)
says the gap is at the edge of the distribution, not beyond it.

**D2 — THE STRUCTURED SLOPE-MERGE.** The shortfall is one
coincidence = one extra pair of fibres sharing a chi-slope. The
constant-norm mechanism already forces one algebraic relation
among the fibre values — derive whether a SECOND relation
(constant e_1 too? a subgroup-structured base triple? w
equivariant under a mu_2 inside mu_64?) can be imposed within the
19 parameters, and what it costs. This is the exact analogue of
round 36's own finding that the finer family (constant-e3 vs
constant-(e1,e3)) mattered — go one level finer, guided by which
coincidences the near-miss draws actually realize (read the data:
WHICH slope pairs merge in the |slopes| = 14 draws?).

**D3 — THE PIPELINE ON ANY 13-SLOPE HIT (or the fences on none).**
If a 13-slope configuration lands: mu(x)-at-middles check (round
36's MISS 10 — never verified), per-side split on actual points,
build G explicitly ((SHARE3-4) form: U~(w)Z^3 - E~_1(w)Z^2 +
E~_2(w)Z - E~_3(w)), outside completion, bivariate system via
bank 2's biv_core.py (copy in; AUDIT ITS OUTPUT PATHS first —
the round-35 breach was exactly this file), full incidence table,
two fields. If none lands: the split sub-case fence (round 36's
R1.13, deficit 5 — make it a verified statement), the sporadic
(non-factoring) sharing residual priced or fenced, and the
honest scope table for the class.

**D4 — VERDICT.** The (BIV-CURVE) m-boundary of record; misses
first; cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(a 13-slope configuration this round), P(it survives the full
pipeline => m=4 witness), P(the second-relation route is the one
that lands), P(the density window map matches ~q^-7), expected
best |slopes| (a number).
