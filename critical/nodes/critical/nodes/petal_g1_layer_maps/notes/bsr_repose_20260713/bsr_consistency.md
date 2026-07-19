# bsr_consistency — task D: the consumer arithmetic under the branch split
# (exact; every number below is a bsr_check.py PASS line)

## D1. Where the column-priced periodic mass lands (pin P3, verified seam)

The P3 emission pin (petal_growth conditional r1/r2, unchanged): the
periodic/staircase branch charges imgfib's QUOTIENT-PROFILE clause,
quantified by the PROVED `dyadic_profile_evaluation`, NEVER n^B. Under the
split this is now the ONLY charge the periodic branch makes:

- gate cells (2 <= M <= t, A = A_own(M)): charge <= 719 * Q_M(A_own) per
  cell (Lemma COL; or SUCCESSOR-A x G1'(D) for chart words);
- composite cells (M > t): charge 719 * column per cell (the replayed
  7-lemma composite; unchanged);
- the two ranges are DISJOINT in (M, A), so no double-charge; within
  [2, t], each class is charged exactly once at its exact-scale cell
  (c(S), |S|) — the stabilizer partition is a partition. The #102 dedup
  device (geometric ledger) is no longer needed for correctness.

## D2. The 719 allowance line (uniformity across all consumers)

719 = floor(n^6 / C(n+6,6)) EXACTLY at all four official maximal rows
n = 2^41..2^44 (bsr_check P5 PASS) — the same integer allowance the floor's
budget arithmetic banked (petal_growth r2, the 9.4919-bit slack integer
sharpening). Under the split, ONE uniform allowance line covers:

- the M > t composite columns (719 x Q_M(A), as before);
- the gate's M <= t cells (719 x Q_M(A_own); truth <= 4 x by COL);
- G1' clause (D)'s atlas cardinality (719 x Q_2(2a'); truth <= 1.002 x
  trivial in scope).

No consumer needs a second constant, and the slack warning of the amber
audit ("the 9.5 bits IS log2(6!), do not spend it inside predicate
exponents") is respected: 719 appears only as the profile-clause allowance,
never inside b1/b3/b4.

## D3. The dyadic_profile_evaluation extension (the one owed consumer item)

The gate mint's route (a) demanded: "a proved extension of
dyadic_profile_evaluation to scales M <= t with the consumer arithmetic
re-verified". The extension's arithmetic is now pre-computed:

- **first-scale dominance (exact bigint, s = 13..20, all four rates):**
  sum over dyadic 2 <= M <= t of Q_M(A_own) <= (1 + 2^-691) * Q_2(k+2).
  (bsr_check P5 PASS; the excess is the M = 4 term, ~Q_2^(1/2).)
- **maximal rows (s = 41..44):** log2(Q_4/Q_2) < -5.4e11 (lgamma; P5 PASS).
- So the M <= t extension adds ONE first-scale column (per band cell) to the
  profile ledger, times the same 719: the absorption question reduces to
  "does the profile clause absorb 719 * Q_2(k+2) (+ 719 * Q_2(k+4) if the
  k+4 cell is consumed)" — the first-scale column at M = 2 being the
  largest column in the whole ledger, this is the profile hypothesis's
  own scale of mass (dyadic_profile_evaluation notes: first-scale dominance
  proved, QA.22 exact). OWED (not claimable from here): re-running the QA.22
  exact evaluation with the M in [2, t] cells included and the 719
  multiplier, against imgfib's reserve arithmetic. This is a computation in
  the PROVED node's own machinery, not new mathematics; it is the single
  item gating the gate's PROVED-pending-audit.

## D4. Consumers of the OLD n^6 form — audit and fate

1. **petal_k4_primitive_bound package (the (64/63)(121/128) ledger).** The
   old package: G1 weighted census -> current-row primitive <= (121/128)n^6;
   periodic classes descended to quotient rows, paid there as
   quotient-primitive within (121/128)(n/M)^6; geometric ledger summed:
   (64/63)(121/128) = 121/126 < 1. Under the split the descended-primitive
   rider is DELETED (its supply is g1a-impossible: the quotient-row band
   census at descended chart words is exponential, and the demand moves to
   the profile clause instead). The package arithmetic becomes
   primitive-only: sum(m_chi+1) <= (121/128) n^6 < n^6. SURVIVES, IMPROVED:
   121/126 -> 121/128 (bsr_check P5 reproduces both coefficients exactly).
   K4's chart-level theorem itself is untouched (row-agnostic, per-chart).
2. **intrinsic_scale_geometric_ledger.** Its hypothesis ("each scale-M class
   injects into a primitive quotient-row family of size <= C(n/M)^6") is now
   known UNSATISFIABLE on the petal lane at fiber-rich cells (g1a corollary:
   the injected family would be the quotient-row band census, which is
   >= C(n'-1,k')/(4q(k'+1)) at worst-case labels). The node stays PROVED
   (the implication is true); its petal edge is RETIRED — sole listed
   consumer was the census gate, which now rides COL. Node-local note owed
   at surgery (per the node-local-notes rule): "petal-lane hypothesis
   vacuous post-#138; edge retired at the branch split."
3. **petal_small_scale_staircase_census.** Old route consumed C(n/M)^6
   quotient bounds (QRL residual). Fate: re-promoted on COL
   (bsr_gate_repromotion.md); QRL T1/T2/T3 remain banked-true, non-load-
   bearing.
4. **petal_chart_carrying_descent 3-C.** Consumed G1's n^6-capped coverage.
   Fate: re-wired to G1' clause (D) (bsr_successor_rewire.md); conditional
   dissolves.
5. **petal_growth (the amber).** Route of record r2 updates: G1-atlas
   (clause (P), floor band) -> first-match -> {per-class: 719 x column to
   the profile clause at ALL scales M >= 2 (gate cells by COL, M > t by the
   composite) | primitive: K4 x clause (P) -> (121/128) n^6}. Re-surgery
   criteria 1/5/6 of r2 map onto the new falsifiers (bsr_falsifiers.md).
   The amber's predicate list shrinks: the census gate leaves the open set
   once D3 lands; the open reds are clause (P) and the G3 compiler's own
   conditional (unchanged).
6. **Nobody else.** grep-audit of dag.json consumers of the G1 budget line:
   petal_growth, petal_small_scale_staircase_census (via SUCCESSOR-A), K4
   package — all covered above. The e22 staircase composite consumes the
   column form already (P3), not the n^6 form.

## D5. What the split does NOT change (for the audit's checklist)

- K4 chart-level theorem (PROVED, b4 = 1) and its pins (G5, #107 retained
  zero, a = ell + d - |R0|): untouched; still consumed by clause (P) only.
- The csp packet Claims 1/2/L0 and all pins #129/#133/#134/#135/#137:
  untouched; consumed by clause (D)/SUCCESSOR-A exactly as before.
- dyadic_profile_evaluation's PROVED content (M > t cells, QA.22): untouched;
  D3 asks for its extension, not its revision.
- Pin P1's owed maintainer line: still owed — but #145 now quantifies the
  stakes exactly (floor band: clause (P) mass poly/empty; wide band:
  clause (P) pre-falsified without a carve-out). The maintainer line should
  be requested WITH the #145 table in hand.
- The below-top band and mixed-petal buckets: outside, as always.

> #155 ANNOTATION (2026-07-13, qme audit): the 2^-691 dominance constant printed in this file is a lg_frac rounding artifact — the exact worst excess is 2^-690.2765..2^-690.2766 at (13, 1/16); honest grid constant (1 + 2^-690). The qme packet carries the corrected form; this record is annotated, not rewritten.
