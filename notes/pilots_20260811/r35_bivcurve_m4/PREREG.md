# PREREG — r35_bivcurve_m4 (round 35)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r34_bivcurve_m34/REPORT.md` (round 34)
2. `background/nodes/u1_x4_direct_column_budget/notes/F3_H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER.md`

## Mandate

THE m = 4 DECISION + THE PARITY FALSIFIER. Round 34 realized
(BIV-CURVE) at m = 3 ((SPLIT-m) + involution) and left m = 4 OPEN
as a searched negative over EXACTLY ONE ansatz class ((SPLIT-4)
with sigma(x) = -x and the forced 3+3+2 split; ceiling 7 of 12
triples). Its own report names the three unexplored routes (its
F2): (a) NON-SPLIT G; (b) sigma(x) = c/x (two fixed points on
mu_64 — a different orbit structure); (c) the un-symmetrised
(3,3,3) split. The obstruction it measured is the (OV) pair cap
forcing the 12 shared slope-triples into a LINEAR 3-uniform
hypergraph — and the repo already holds a PROVED
linear-3-uniform-hypergraph compiler (anchor 2, the u1_x4 lane:
pair-uniqueness forcing linearity, plus finite guardrails) that
the round-34 pilot's grep missed. YOUR JOB: decide m = 4, or
tighten its obstruction to the wider class with the scope stated
exactly; and run the cheap m = 5 parity experiment either way.

## Deliverables

**D1 — THE m = 4 DECISION PROGRAM.** Routes (a)/(b)/(c) in
whatever order your registered analysis ranks them, plus the
compiler import: transport anchor 2's machinery to the m = 4
selection problem (12 triples, degrees <= 3, <= 15 slopes) — does
pair-uniqueness + the guardrails DECIDE satisfiability of the
selection layer, separating it cleanly from the arithmetic
(value-coincidence) layer? Round 34's supply/demand analysis says
the shortfall is in the cross-coincidence term (even-m
sigma-invariant factor injective on orbits) — route (b) changes
exactly that term (fixed points!), so derive its orbit arithmetic
BEFORE searching. Either outcome certified: a witness (full
incidence + (BIV-CURVE) table, two fields) or the obstruction
extended with named scope (what class is excluded, what remains
untouched).

**D2 — THE m = 5 PARITY FALSIFIER.** (SPLIT-5)+sigma all-swapped
(m-1 = 4 factors, no invariant factor forced). A witness CONFIRMS
the parity prediction (odd m easy / even m obstructed, currently 2
data points); a failure REFUTES it. Also check the round-34
caution: at m = 5 the (OV) cap m-1 = 4 re-admits tuple
multiplicity 4 — does the linearity constraint really vanish, and
does that change the selection problem's character?

**D3 — (OUT-m) STRESS TEST, CORRECTED FORM.** The coordinator's
corrections are on the node (round-34 (BIV-CURVE) addendum,
`critical/nodes/rate_half_band_crossing_location/statement.md`):
per-slope X' + 2X'' >= m-1 - eps~ with eps~ <= 1+O; aggregate
(m-1)(1+O); the X = 0 corollary gated on O <= m-3. Stress-test the
corrected statement on every configuration this round produces
(m = 4 candidates, m = 5 witnesses, deficient-point placements
inside vs outside W — the case that refuted the original rider).
A violation of the CORRECTED form is a registered falsifier of a
coordinator-audited statement: report it loudly if it fires.

**D4 — VERDICT.** The (BIV-CURVE) m-boundary of record, updated;
misses first; cross-pilot flag (do NOT read siblings) for anything
bearing on layer A or the realizability layer.

## Blind priors to register

P(m = 4 realizable via route (a)), P(via (b)), P(via (c)),
P(the m = 5 parity witness lands), P(the u1_x4 compiler transports
usefully), P(the corrected (OUT-m) survives all stress).
