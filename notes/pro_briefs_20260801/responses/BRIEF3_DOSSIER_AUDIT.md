# Fable audit of the Brief-3 Pro dossier — 2026-08-01

**Verdict: SOUND.** All five route-critical corrections verified; two of
our brief's three routes corrected; the third (witness-family injection)
survives and is strengthened into the dossier's payment-key rule. No DAG
status changes.

## Replay and verification record

- Companion script: full PASS under `ramguard local`. Verified content:
  six-row ledgers and budgets; rank-3-paid/rank-4-open frontier replays;
  the component payoff breakpoints (4/4/4 RowC, 12/11/10 prize) computed
  from the exact CA-GRK cap; the induced-matching fence (758/494/309-bit
  lower bounds vs the 33-bit budget); the literal 256-bit field's q/8n^3
  ratio (130 bits, with 2^41 | q-1 checked); the 134-bit extension-record
  explosion at the first RowC shell with EC4 slack verified pairwise; the
  F_5 rank fence; the 2^35-1 > 2^34 preterminal tree fence with the
  banked area/drop laws satisfied along every path; the rank-five
  reuse-core arithmetic (b=C(m,4), c, line caps — all six values).
- Hand checks: the greedy induced-matching argument (chosen exact-h edges
  pairwise at distance > h => isolated d_C=0 components; deletion count
  2(D_<=h+1)D_h per pick => M >= V/4(D_<=h+1)); 16n^3 = 2^34 at RowC;
  the union identity |E ∪ F| = r + j and the j=h <=> size-k core
  equivalence.
- Import audit: all seven spot-checked background nodes exist
  (component atlas, Segre atlas, fundamental-circuit owner, collision
  ledger, dimension-area law, Plotkin width, split-pencil reduction) —
  the dossier's picture of the lane's banked maturity is faithful.

## Corrections to Brief 3 (addendum written into the brief)

1. **Route 1 ("rational points on a bounded-degree variety") — REFUTED
   as stated.** Bounded degree is not the currency: any surviving
   positive-dimensional parameter leaks ~q/8n^3 ~ 2^130. Corrected form:
   every terminal cell must be empty, zero-dimensional with a q-free
   degree bound, or uniquely reconstructed from an n-indexed key.
2. **Route 2 ("core-sharing graph degeneracy argument") — the graph half
   is REFUTED** by the induced-matching fence (support structure cannot
   bound component counts); the witness-charging half survives.
3. **Our sharpest question (witness family + injection) — SURVIVES,
   strengthened:** the dossier's payment-key rule is exactly that
   witness-injection, with the added mandatory constraint that keys be
   q-free. Route 3 (per-rate finite outer loop) is unaffected.

## What I accept beyond the corrections

- The two authorization gates (nonuniform completeness; trade-rank
  funnel-or-payment) as hard preconditions on any rank-two fleet — the
  identified failure mode ("close a beautiful but non-exhaustive branch")
  is exactly the trap the lane's maturity invites.
- The component payoff ladder as the lane's pricing instrument (CA-GRK
  stops paying at small excess; the target is the weighted sum CP3/CP4,
  never per-component caps).
- The P-A1/P-A2 track separation (different final currencies; shared
  software only).
- The Bellman + slope-flow-conservation architecture for P-A2 — the same
  machinery family as Brief 2's adopted core, which makes the descriptor
  collision audit and the child-partition certificate reusable patterns
  across both lanes.

## Points of caution

- The circuit-star external-zero compression (CSEC1) is the genuinely
  new local theorem and its shape (coordinate-triple key) is a design
  target, not a derivation; the dossier is explicit about this.
- The five fences are abstract route fences, not RS counterexamples —
  they kill inference patterns, not the targets.
- Nothing minted from this dossier yet: the two cheap bankables (route
  fences as a background note; the payoff ladder as an exact table node)
  are worker-shaped and can be minted with the Phase-0 compiler work.

## Adopted posture

CONDITIONAL GO with Pro's ordering: (1) bank the five fences + payoff
ladder (cheap, worker-shaped); (2) the exact toy owner/descent compiler
(PP3.3) — owner semantics are the highest-risk component and the compiler
falsifies them before theorem-scale algebra; (3) the two gates (PP3.4,
PP3.6); (4) circuit-star compression (PP3.7); (5) RowC rank-five fleet
only after semantics freeze; (6) prize uniform owner theorem and P-A2
Bellman in parallel. The frontier-moving list (§19) is adopted as the
lane's progress filter.

[CORRECTION 2026-08-02: the "j=h <=> size-k core equivalence" and any
"post-strip cores <= k" framing above re-source via the ratified R2/Route
T partition: the rung proves forcing only; the band [k+1, A-1] is charged
by xr_graded_tangent_band_charge; P-A1's exact-k predicate is unchanged.
Pro is paused; this record is historical.]
