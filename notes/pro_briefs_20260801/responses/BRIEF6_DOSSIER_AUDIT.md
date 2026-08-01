# Fable audit of the Brief-6 Pro dossier — 2026-08-01

**Verdict: SOUND — and its primary finding is now a PROVED node.** Two
corrections to our brief accepted; the budget staircase verified end-to-end
and minted as `rate_half_list_cyclic_budget_staircase` (background, req
from the cyclic floor, ev into the crossing TARGET; verifier PASS, six
tiers, validators green, census unchanged).

## Replay and verification record

- Companion script: full PASS under `ramguard local`. Notable content: the
  exact-integer Johnson anchor computed by big-integer bisection AT
  OFFICIAL SCALE (all six ledger rows match, including the 77-bit defect
  at the classical threshold and the exact threshold budget
  332,114,441,762); the six staircase counts; the eight-cell coarse B=3
  atlas derived from scratch (six histograms x deficit-orbit counts
  3/1/1); a LIVE construction of the F_17 three-codeword same-word
  witness (degrees < k, distinctness, agreements 12/11/11); the exact
  packing fence (below 2^128 at 127-from-full, above at 128); and the
  logic guardrails (bracket vs adjacency, failed-upper vs unsafe,
  avg vs max, different-word trap, exact-shell first ownership).
- Hand checks: staircase instantiation against the parent theorem's
  actual hypotheses (`c|n/2` ✓ dyadic, `s=c-1` in range since `c>=2^33`,
  `d=1<=N_0/2-1` ✓); `Lambda(8)=ceil(21/8)=3`,
  `Lambda(16)=ceil(5005/16)=313`, `Lambda(32)=ceil(265182525/32)=8286954`;
  agreement `n/2+c+(c-1)=k+2n/N_0-1`; exact-agreement implies
  threshold-agreement. The `5005 = C(15,9)` echo of the old
  field-semantics catch is a coincidence of binomials, checked exact.
- **Import faithfulness:** the cyclic floor's statement IS fully
  parameterized (not just the optimized N_0=256 instance) — the staircase
  is a legitimate corollary, not a re-derivation. The 13-chamber
  role-labelled atlas exists in the crossing node's attack.md as
  described. The B=1,2 exact crossing and the fixed-tail floor scope
  match.

## Corrections to Brief 6 (addendum written into the brief)

1. **The literal (RHL-ADJ) is vacuous.** Monotonicity + integer values +
   the terminal convention make bare existence trivial. Our brief did
   identify the upper leg as the real mystery, but reproduced the node's
   display without noting its vacuity. The real target is the
   certificate-producing pair; the claim contract amendment (plus the
   B*=0 scope pin — mechanical either way: `q<2^128` rows are either
   below the sufficiently-large floor or have the trivial sentinel) is
   ours to write.
2. **Bisection refinement.** Our sharpest question ("one explicit point
   converts the node to a bisection") stands but under-specified: the
   bisection is sound only over a TOTAL decision oracle. UNKNOWN is not
   UNSAFE.
3. **A fifth-surface lesson.** The staircase sat fully proved inside our
   own banked theorem — nobody had instantiated it below the cap tier.
   Same genre as hard law 5: before hunting new mathematics, exhaustively
   instantiate what the tree already proves.

## What I accept beyond the corrections

- The frontier ledger (U/S per budget interval) as the lane's progress
  currency — every future theorem prices itself there or is background.
- The B=3 two-sided decision semantics (REALIZE / EXCLUDE / UNKNOWN,
  no UNKNOWN-as-exclusion, all-excluded => safe frontier descends) as the
  cheapest validation of the whole program's semantics.
- The four-point lift obligation for the F_17 witness (fibre
  multiplication, field-order conditions, degree cap, first-match roles).
- The exact-shell cumulative-sum discipline (a theorem for one shell is
  not a threshold theorem; per-family caps need a compatibility theorem).

## Points of caution

- The primitive profile envelope (PE1) is the deep open theorem, and
  Pro's own §30 admits it may be the L1 flatness wall in disguise. The
  gates are designed to find that out cheaply; hold them.
- The fieldwise `d>=2` optimizer is PROVABLE but its certificate cost at
  2^256 scale is untested — Gate 2 exists for that.
- The dossier's proposed DAG grammar is advisory; minting stays with us
  (one node minted today; the optimizer and contract nodes can follow as
  they are actually proved/drafted).

## Adopted posture

CONDITIONAL GO. Sequencing: (0) the contract amendment + B*=0 pin — ours,
cheap; (1) staircase MINTED (done today); (2) the fieldwise optimizer as a
Codex-shaped exact-arithmetic node; (3) the B=3 chamber manifest +
two-sided compiler as the first research campaign (worker-shaped:
finite algebra with the coarse 8-cell cross-check banked in the replay);
(4) the exact-shell transport + owner grammar only after gates 0-4.
No field census, no packing revisit, no pairwise-Johnson, no
average-as-max, ever.
