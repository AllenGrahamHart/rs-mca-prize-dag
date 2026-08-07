# FABLE_AUDIT — l1_ell_sweep (round 22, agent 4 of 4 — ROUND COMPLETE)

**Auditor:** Fable, 2026-08-07. **Verdict: BANKED, MAINTAINER-LEVEL —
the decisive sweep was executed beyond its brief (n=32 reached
ell=5, the deepest proper-band cell, BOX = 1.6e9; n=64 added at
ell=2,3) and F-w1 is not merely silent but EXHAUSTIVELY silent at
four cells: at n=24 ell=4/5/6 and n=32 ell=5 the pilot enumerated
the ENTIRE legal word space (96 or 9,216 projective words) via a
word-uniform upper bound and adjudicated every exceedance exactly —
so at those cells no received word of the chart family can fire the
falsifier, closing the "search missed the max" objection that
round 21 itself raised. The random-word law holds in ell to 0.1%
at the three largest cells. Clause (b) remains entirely open, and
the pilot says so plainly.**

Replay: gate.py ALL PASS (three code paths; the banked histograms
character-identical; round-21's 3,273 and 122 reproduced);
degen_word.py closed form reproduces 375,674 (= the full engine's
independent value at n=32 ell=3) and 1,594,308 (n=32 ell=5), plus
the b <= 1 theorem giving RET(lambda*1) = 0 with no computation.
REPORT.md persisted verbatim (task ad4f92852e755bdbd).

ADOPTED:
- **The F-w1 verdict of record**: silent at all 14 cells (max
  RET/(10*BOX/q) = 0.091); EXHAUSTIVE at the four named cells. The
  one word class the word-uniform bound flagged (the constant-
  scalar word) was adjudicated exactly every time: RET = 0 when
  b <= 1 (proved: U agrees with the codeword lambda*L_C off the
  background, forcing r <= b-1), 0.0096 of threshold at b = 2.
- **The normaliser amendment (to apply post-merge)**: F-w1's
  10*BOX/q loosens with ell (deep shells swell; 2.9x more generous
  at n=32 ell=5 — in exactly the regime the re-pose says carries
  the content). The re-pose of record will be amended to the
  shell-resolved normaliser 10*N_{k+1}(ell)/q, against which the
  measured law is flat (RET = (1-1/q)^{n-k-1} * N_{k+1}/q to ~1%
  with NO ell dependence). Same closed form, already computed.
- **The bug catch on round-21's d3_ell_sweep.py** (b <= 1-only
  filter, two failure modes; the unquoted n=16 ell=3 zero is
  wrong, true 100). NO banked number affected — verified against
  the round-21 REPORT and my addendum. Warning note filed in the
  l1_pma_diag dir.
- **P0 scope discipline**: the brief's n=24 ell=5,6 cells are
  t=2/band-vacuous and are NOT points on the floor-band curve —
  the pilot predicted this before computing and measured them
  anyway with the label. My brief was imprecise; the pilot
  corrected it. The proper-band frontier is n=32 ell=5.
- **The off-family band test** (registered replacement for the
  tautological in-family F-w2): with the band DROPPED, exact-
  agreement semantics still enforce sigma <= Lambda at the tested
  cells (formal ceiling k+11, measured max k+3) — clause (a)'s
  conclusion is not carried by the band definition alone. And the
  band is a real 48.6x mass restriction. Both directions honest.
- **The P7 refinement**: round-21's "~16% structural excess" of
  the minimal-degree word is a COSET-LAYOUT ell=2 phenomenon
  (mu_2 antipodal petal symmetry; 15.9%/17.4% at LAYOUT-B ell=2,
  0.20% at LAYOUT-B ell=4, <= 2% at LAYOUT-A everywhere) — it
  does not grow with ell.
- **The extrapolation, honestly labelled**: under the measured law
  the census regime (sigma=1) and consumer regime (sigma=ell-1)
  are separated by ~10^12 in log2 mass at official rows, driven by
  q^{-sigma}; the pilot states plainly this says nothing about
  adversarial words, which is the open content. Also the honest
  caveat that the fixed-n sweep moves t DOWN while the official
  regime has t growing — the conservative direction, stated.
- **Modal request lines** (none launched): L1-N10-ELL-48-4 (23
  CPU-h, best value), L1-N10-ELL-64-4 (895 CPU-h), 64-5 marked DO
  NOT LAUNCH. To be filed in the compute-request pipeline
  post-merge.

HONEST LEDGER accepted: amendments A3/A4/A6 (the word-uniform
bound, the degenerate-word closed form, the skipped-cells list)
recorded as NOT pre-registered in a separate PREREG section; the
engine's exact test derived and registered BEFORE measuring; JSONL
checkpoints for every word. Quarantine absolute; no subagents.

ROUND 22 COMPLETE (4/4 banked). Aggregate: one first-of-record
upper bound (U2, crossing), one proved anti-transport (AT,
M-route), one two-sided falsifier resolution with a repriced
(b)-route (mystery 5, ~20 orders), one retired-constant +
proved-floor diagnosis (mystery 2, +1.7% optimality), and one
exhaustive falsifier silence with a sharpened falsifier (mystery
6). Cross-round signal: FOUR lanes now converge on the
constant-weight / ternary-min-distance instrument cluster
(integer_code_distance_cert + the constant-weight Z-FLOOR cell).
NEXT (post-merge): amend F-w1's normaliser in the re-pose of
record; apply the deferred U2 addendum; file the Modal lines;
re-derive the mystery accounting on the 28-red board.
