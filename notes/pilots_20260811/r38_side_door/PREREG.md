# PREREG — r38_side_door (round 38)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r37_share3_gap/REPORT.md` (round 37)
2. `notes/pilots_20260811/r36_m4_nonsplit/REPORT.md` (round 36)

## Mandate

THE SIDE DOOR — the cheapest potentially-decisive item on the
board. Round 37 derived the (SHARE3-4) prescribable-merge budget
(8 vs demand 11) and the coordinator CHECKED THE LOOPHOLE LEGAL:
one fibre whose slope cubic has a DOUBLE ROOT drops the slot
count 24 -> 23, so **10 merges suffice — which two rounds have
already achieved** — at the cost of its three points having
|A_x| = m-1 = 3, i.e. sum_x(m-d_x) = 3 = 1+O with O = 2, which
fits (SAT2) (O <= 3) and (SAT4) (sum <= 4) EXACTLY at the
identity. YOUR JOB: build the configuration and run the FULL
pipeline. If it survives, it is an m = 4 (BIV-CURVE) witness
candidate — the biggest single event available to the campaign.
If it dies, name the exact axiom that kills it (the per-side and
incidence bookkeeping at the three deficient points is the
unchecked part).

## Deliverables

**D1 — THE DEGENERATE-FIBRE ARITHMETIC, COMPLETE, BEFORE
SEARCHING.** With one fibre {x_1,x_2,x_3} carrying the slope
cubic (Z-alpha)^2(Z-beta): each x_i has A_x = {g-or-h, alpha,
beta} of size 3 = m-1 (the double root contributes ONE slope).
Derive the full ledger: the type-2 slot count (23), the merge
demand (10 for s = 13), the per-side caps at the deficient points
(X'_alpha picks up 3 incidences from one fibre — does the cap
2m-2 = 6 hold? does the PER-SIDE cap m-1 = 3 hold given the
(2,1)/(1,2) split?), the (OUT-m)/(DEG-m) corrected forms at
O = 2, and the (SAT4) identity placement (the deficient points
are INSIDE W — check the round-34 charge bookkeeping: inside
deficiency charges m-2 per unit, so sum eps~ = 3*(m-2)? derive
exactly). ANY axiom that fails here kills the door — check ALL
of them before building.

**D2 — THE BUILD.** Take 10-merge configurations (both prior
rounds have them: |slopes| = 14 draws = 10 merges; your own
regeneration is fine) and impose the degenerate fibre: in the
pencil picture the fibre's cubic has disc = 0 — one further
algebraic condition on the line in P^3; the round-37 Segre
budget arithmetic says what it costs (derive: is a double root
a cost-1 or cost-2 prescription?). Alternatively impose it first
and search for 10 merges around it. Two fields (q = 193, 257).
Target: a complete 13-slope, 27-point, O = 2 configuration
passing D1's full axiom ledger.

**D3 — THE PIPELINE ON ANY SURVIVOR.** W assembly (27 points:
8 fibres + the middle fibre — wait, with the degenerate fibre
among the 8: derive the exact W bookkeeping in D1); per-side
split on actual points; mu(x)-at-middles (the never-verified
check); build G explicitly ((SHARE3-4) form); outside
completion; the bivariate system via bank 2's biv_core.py (COPY
IN AND AUDIT ITS OUTPUT PATHS FIRST — it writes at import); the
full incidence table; layer A run on the result (the witness
would be the first m >= 2 object to face it with a completion).
Two fields. If no survivor: the named killing axiom, with the
measured margin.

**D4 — VERDICT.** The (BIV-CURVE) m-boundary of record; misses
first; cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(D1's ledger closes — no axiom kills the door on paper),
P(a 13-slope O=2 configuration is built), P(it survives the full
pipeline => m=4 witness), P(the killing axiom, if any, is the
per-side cap), expected best outcome (a phrase).
