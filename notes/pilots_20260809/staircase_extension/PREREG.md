# PREREG — staircase_extension (round 27)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

The wave-10 composition on rate_half_band_closure proved: for every
admissible 2^128 < q < 2^167, a_RH(q) = n - floor(q/2^128) + 1,
UNCONDITIONAL (statement.md section "QUADRATIC EXACT RANGE ...",
line ~160). Its anatomy: the quadratic staircase equality
(mca_quadratic_prize_rows) covers B = floor(q/2^128) <= B_Q =
389,500,552,609 ~ 2^166.503; the (RQ4) equivalence reduces
B_Q < B <= 2^39+1 to the single far-CA bound; the Hankel
unconditional layer B_ca^far(n-r) <= r+1 covers every r <= 2^39-2;
the coordinate-tangent family supplies the adjacent unsafe witness.
EXACT RESIDUAL: budgets {2^39, 2^39+1} (strata recorded per w10-H1).
Beyond 2^167: brackets only, a_RH in [k+2^34, 3n/4] (q >= 2^169) or
[k+2^34, n]. The razor slice needs budgets ~2^128. Your job: close
the two-budget residual, diagnose the boundary, and price the
razor-scale analogue honestly.

## Deliverables

**D1 — THE TWO-BUDGET RESIDUAL {2^39, 2^39+1}.** The smallest named
open piece on this node. Read the w10-H1 strata (budget 2^39:
strict A=3, s=0, e in [2^37, floor((2^39-1)/3)]; budget 2^39+1:
A=3 e >= 2^37+1 plus A=1 rows) and the far-CA layer's proof to see
exactly why r = 2^39-1 and 2^39 escape it. Attempt the close: either
extend the Hankel layer's argument by the two steps, or find a
dedicated argument for the two strata, or exhibit why they are
genuinely harder (a structural obstruction at the boundary is a
bankable finding). Register your route and expected outcome first.

**D2 — THE BOUNDARY DIAGNOSIS.** For each of the three layers
(staircase equality; (RQ4) equivalence; far-CA Hankel), answer: is
its stopping point an artifact of the proof budget (a finite
computation that was run to a chosen depth) or structural (the
argument itself degrades)? The answer determines whether "extend to
razor" is a computation, a new theorem, or impossible by this route.
Own-repo read first: mca_quadratic_prize_rows and the Hankel suite
nodes are PROVED — their proofs state their own domains.

**D3 — THE RAZOR-SCALE PROBE.** The formula a_RH = n - B + 1 is
exact on 2^128 < q < 2^167. Test the MECHANISM beyond: at scaled
band-analogue rows (accessible q, scaled n where the full a_RH is
exactly computable), does the staircase-shaped formula continue
through and past the scaled analogue of the 2^167 boundary?
Register the scaling map and predictions first. A deviation
LOCATES where new mathematics starts; continuation is evidence the
bracket [k+2^34, 3n/4] is slack.

**D4 — THE BRACKET.** Beyond 2^167 the bracket floor k+2^34 comes
from the optimized v5 re-instantiation (c=2^33, d=1). Attempt any
improvement of either end using the wave-10 machinery + the K5
witness-kernel routes named in WP5 (averaged conversion at giant M;
B2b balance). Price what a full razor determination would need if
D2 says "new theorem."

## Escape tests (before the main work)

- Replay the wave-10 arithmetic anchors: B_Q = 389,500,552,609;
  the a_RH formula at 3 sample q below 2^167; the bracket constants.
- Verify one Hankel-suite node's verifier (SCRATCH COPY) passes
  before leaning on its layer.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4062; do not read the other round-27 pilot dirs
  (pincer_formalization, nonpoly_flank_census, cancellation_recon).
  Pass this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY (the round-26 lesson).
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with
  results files for >10-min runs.
- DRAFT-ONLY: writes only in
  notes/pilots_20260809/staircase_extension/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Own-repo grep before claiming anything is missing (CATCH-24A) —
  this brief's own citations are a starting map, not a boundary.
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)
