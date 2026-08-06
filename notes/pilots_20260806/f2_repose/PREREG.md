# PRE-REGISTRATION — THE F2 RE-POSE: the lane rebuilt from the consumer down (round 20, GENERATIVE)

Round 20, 2026-08-06. Coordinator-authored brief; the pilot appends
its own registrations BEFORE any computation. The reading rulings
are now of record (CAMPAIGN_LEDGER 2026-08-06; f2_o1_status_split
addendum): Lambda parity = A, ensemble = the slice, PP5.0 = sum —
and their accepted consequence is that **(O1) as posed is FALSE on
every admissible row**. The F2 lane needs its honest replacement,
built from the consumer down. That is this pilot.

## 0. The state (quote verbatim before working)

- background/nodes/f2_o1_status_split (+ the rulings addendum) —
  what is false and why; the minimal surviving form
  E_{c in K1}[T_W(c)] = 2^{n/2}·Z_1^e EXACTLY on the three
  generating classes; the non-generating kill (ADM-B/Z-3).
- background/nodes/f2_z1_mass_knife_edge (post-corrections) — the
  mass terminal, the tail-count criterion, NO named route, the
  Prop-10 lead.
- background/nodes/f2_admissible_object — the exact structure
  (ADM-2 direct sum, dim L exact, the three-class census, C1).
- The CONSUMER side: what does the prize-level statement actually
  need from this lane? Trace the (O1) => (O2) => ... chain upward
  (f2_opening PROOFS; the fence CATCH-G analysis in
  o1_generating_adversary) and identify the WEAKEST statement about
  the F2 object that still feeds the chain — (O1) was one choice of
  intermediate; the consumer may be satisfiable by less.

## 1. Pre-registered deliverables

- **(R1) THE CONSUMER CONTRACT.** State exactly what the downstream
  chain needs from the F2 lane, at which rows, quantified how. Not
  what (O1) claimed — what the CONSUMER requires. If the fence
  demands the slice ensemble (ruled), write the contract in slice
  terms. This is the spec the re-pose must meet.
- **(R2) THE RE-POSED INTERMEDIATE at generating rows.** Given the
  contract and the proved structure: the candidate of record is the
  mass form (Z_1 tail-count), but test WEAKER candidates first —
  does the consumer need the full 2^{n/2+o(n)} mean, or a
  quantile/median statement (Z-FLOOR is tight within 2x of the
  ensemble mean — a MEDIAN version may be provable where the mean
  target is false)? Does it need all rungs or fewer? Pose the
  weakest sufficient intermediate, with its falsifier.
- **(R3) THE NON-GENERATING ROWS.** The lane must cover them (scope
  ruling). The K1 identity fails there by 2^{Theta(n)} — so K1 is
  the WRONG intermediate on those rows. What structure survives?
  Candidates to price: (i) the coset/class decomposition (ADM-1/2
  still holds — dim L exact — only the BALANCE dies); (ii) a
  different window (the failure is at the full-group window; do
  partial windows retain margin?); (iii) the consumer contract may
  be dischargeable at non-generating rows by a DIFFERENT lane
  entirely (the ord < e structure makes the row "smaller" — does an
  existing proved node cover small-ord rows?). Deliver at least one
  candidate intermediate per (i)-(iii) with a verdict each.
- **(R4) THE LANE STATEMENT DRAFT.** A NODE-DRAFT-style statement
  of the re-posed lane obligation (both row classes), with what is
  proved / open / false clearly separated — the coordinator mints
  after audit.

## 2. Pre-registered falsifiers / honesty clauses

- The consumer contract must be QUOTED from the chain's actual
  text, not inferred — if the chain is ambiguous about what it
  needs, that ambiguity is a reported finding with the candidate
  readings priced.
- A re-posed intermediate that is merely "not yet refuted" must be
  labelled as such, with its falsifier pre-registered; do not
  present survivable-so-far as sound.
- If NO intermediate meets the contract at some row class, say so
  plainly — "the lane has no candidate at non-generating rows" is a
  reportable verdict and changes the board honestly.

## 3. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/f2_repose/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/tail_count/ (sibling this round). Do NOT
  read CAMPAIGN_LEDGER entries appended after the "ROUND 20
  LAUNCHED" marker.
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# APPENDIX — PILOT PRE-REGISTRATION (Opus 5, 2026-08-06, round 20)

Appended BEFORE any computation and before verifying any of the
quotes below (which reached me via a read-only search agent and are
NOT yet checked against the files). Everything numeric here is a
PREDICTION at risk.

## The hypothesis I am about to test

Reading the state, I formed one structural hypothesis before
computing anything: **(O1)'s target `2^{n/2+o(n)}` is not the
consumer's requirement — it is a strictly stronger statement the lane
chose.** The consumer chain terminates in an ALIGNMENT RATIO with an
explicitly stated FINITE tolerance (`2^{1.05e12}`), not in a
`2^{o(n)}` demand. If so, the whole re-pose changes character: the
question is not "can we prove `Z_1 <= 2^{o(m)}`" (no named route)
but "how many of the tolerance's bits does the K1 class actually
need", and the answer may be payable by instruments already banked.

## Registered predictions (each with its falsifier)

**(B1) THE CONTRACT IS A RATIO CONTRACT WITH A Theta(n) TOLERANCE.**
PREDICT: the consumer's stated requirement on the F2 lane is
`|sum_{c!=0} eps_c exp(S_c) - STRUCT DRIFT| <= TOL * sqrt(sum_{c!=0}
exp(2 S_c))` with `log2 TOL = 1.05e12` at official prize-max rows,
i.e. `TOL = 2^{0.4775 n}` at `n = 2^41` — Theta(n), NOT `o(n)`.
COROLLARY PREDICTED: (O1) is strictly stronger than the contract by
a Theta(n) margin, and its falsity therefore does NOT by itself
break the consumer.
FALSIFIER: the consumer text demands `2^{o(n)}` as a requirement
rather than an ambition; or `1.05e12` is a budget for a different
quantity (a count, not a ratio); or the tolerance is already spent.

**(B2) THE SUM READING IS EXACTLY THE 49.5G-BIT OVERSHOOT.**
PREDICT: `log2|K1| = n/2 = 1.0995e12` exceeds the tolerance
`1.05e12` by `4.95e10` bits, and this number is IDENTICAL to
BRIEF5's "`n_r/2` fails by 49.5G bits" — i.e. the average-vs-sum
seam (`f2_adm` D5) and the consumer's threshold `theta* =
0.4774920` are the same inequality seen from two ends. PREDICT the
two numbers agree to better than 1%.
FALSIFIER: they differ by more than 1%; or `sum_r n_r != n - o(n)`.

**(B3) THE CAUCHY-SCHWARZ RE-POSE — the weakest candidate, tested
first.** PREDICT: the K1 class's contribution to the alignment
NUMERATOR is bounded against its own L2 norm UNCONDITIONALLY, with
NO input about `Z_1` whatsoever, by
`sum_{c in K1} T_W(c) <= sqrt(|K1|) * sqrt(sum_{c in K1} T_W(c)^2)`
(Cauchy-Schwarz, all K1 terms non-negative), i.e. ratio
`<= 2^{(1/2)log2|K1|} = 2^{n/4} = 2^{5.497e11}`. PREDICT
`n/4 < 1.05e12`, so the K1 class fits the contract using 52.4% of
the tolerance with NO mass bound at all.
FALSIFIER: the consumer's denominator is not an L2 norm over the
same index set; the STRUCT DRIFT subtraction cannot be attributed
class-by-class (PP5.0) so the class split is illegitimate; the
remaining classes cannot fit in the residual 47.6%; or `n/4 >=
1.05e12`.
I REGISTER IN ADVANCE that if B3 holds it is a TRIVIALITY meeting a
weak contract, not a theorem about the F2 object, and I will label it
as such.

**(B4) THE MASS FORM HAS AN UNCONDITIONAL VALUE INSIDE TOLERANCE.**
PREDICT: `tern_route_b` THEOREM 7 (`Z_1 <= 2^{0.8908 S}`,
unconditional) with `S = m/e`, `Z(L) = Z_1^e`, `m = n/2 = 2^40`
gives `Z(L) <= 2^{0.8908 m} = 2^{9.79e11}`, and `9.79e11 < 1.05e12`
— so even the MASS form is already inside the consumer's tolerance
unconditionally, with ~7.1e10 bits of slack.
FALSIFIER: the arithmetic fails; `S != m/e`; THEOREM 7 does not
apply at admissible `p`; the exponent is per-`S` not per-`m`.

**(B5) THE MEDIAN CANDIDATE IS INSUFFICIENT (tested before the
stronger ones, as mandated).** PREDICT: a median/typical-value form
("`T_W(c) <= 2^{n/2+o(n)}` for at least half of `c in K1`") does NOT
meet the contract, because PP5.0 is RULED = SUM and a sum is
tail-dominated; a median statement is compatible with a single
frequency carrying `4^m`. PREDICT the quantile form that IS
sufficient is the already-banked TAIL-COUNT criterion, which is
EQUIVALENT to the mass bound, not weaker. So the weakening that
actually buys something is in the TARGET EXPONENT (B3/B4), not in
the moment order.
FALSIFIER: an argument that a median plus the banked pointwise floor
recovers the sum; or PP5.0 re-read as an average.

**(B6) NON-GENERATING ROWS — the C-S form is k-MONOTONE THE RIGHT
WAY.** PREDICT: the C-S bound uses only `log2|K1|_eff = (k/e)(n/2)`
(LEMMA ADM-3), so at `k < e` it gives `2^{(k/e)(n/4)}` — STRICTLY
BETTER than at `k = e`, exactly the opposite direction to (O1),
which is FALSE there by `2^{Theta(n)}`. PREDICT this is a live
candidate intermediate at non-generating rows, and PREDICT the mass
form is NOT (Z-3's excess `2^{m(1-(k/e)(tL/n))}` reaches `m = n/2 =
1.0995e12 > 1.05e12` in the limit, busting the tolerance).
FALSIFIER: `dim L <= k|Lambda|` does not bound `log2|K1|` (it bounds
`dim L`, a different object) — I flag this as the likeliest way B6
dies, and will check it explicitly rather than assume it.

**(B7) PARTIAL WINDOWS (R3(ii)).** PREDICT: partial windows retain
FULL margin (THEOREM A's exact discharge, `Z = 1`) but only up to
order layers `a <= 42 - log2 L`, i.e. 0.78% of the domain at
prize-max, and every moving rung misses by >= 39x — so route (ii)
is a real but quantitatively tiny candidate, not a cover.
FALSIFIER: a moving rung where Lemma 2's hypothesis is satisfiable.

## Honesty clauses I bind myself to

1. If B3 holds I will state plainly that the F2 lane's (O1)
   obligation was over-posed relative to its own consumer, and that
   the surviving hard content is PP5.0 (which has no statement),
   not `Z_1`.
2. Any candidate that is merely "not yet refuted" gets that label
   and a pre-registered falsifier, per section 2.
3. If the class decomposition of the alignment numerator cannot be
   justified from the chain's text, B3 and B6 are DOWNGRADED to
   "conditional on PP5.0" and I say so in the headline, not the
   residuals.
4. I will report the reading ambiguity in the contract (which `b`
   scale; which index set; ratio-vs-absolute) as a finding with
   candidate readings priced, per section 2 clause 1.
