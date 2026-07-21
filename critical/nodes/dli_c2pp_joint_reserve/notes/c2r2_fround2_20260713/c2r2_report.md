# C2'' F-ROUND 2 — REPORT & VERDICT

Target: CONJECTURE C2'' (node `dli_c2pp_joint_reserve`), pose
`C2PP_POSED_20260710.md`. Round 1 = M1 (n=64 tower census, F-a/F-c, F-b
deferred). Fresh-context falsification worker, 2026-07-13.

## VERDICT: **SURVIVED** (round-2 scope) — no pre-registered falsifier fired

- **F-a NOT fired** — coset-stripped, accident-priced bulk trend flat over a
  grid WIDER than M1 (t=2 octaves 7–14 vs M1's 7–13; t=3 octaves 7–9 densified).
  Fires at 0 of 2 depths (kill needs ≥2). Bulk ≤ 1.0007 at n=64; octave slope
  s_j strictly decreasing.
- **F-b NOT fired** — SCORED for the first time (M1 deferred it), via the M4
  assembly-verifier packet arithmetic x³³ vs 2²¹. Worst replayable-tower charge
  = 2^3.05, **reserve usage 14.53 %** (≈85 % margin). Clears decisively.
- **F-c NOT fired** — Poisson window law on a **34-row** fixed-shape census
  (>30, armed); X=0 exceedances, p=0.0237; theta-insensitive on {2,3,4}.

This is the honest verdict for the SCOPE ACTUALLY RUN. Two extensions are
compute-DEFERRED and must NOT be read as cleared (see Scope below). The F-a
result went "wider" (new octave) but not "deeper" (no new tower depth), so the
F-a sub-result is a widened confirmation, not a full deepening — flagged.

## Per-falsifier outcomes

| falsifier | M1 (round 1) | Round 2 | worst statistic observed |
|---|---|---|---|
| F-a | not fired (t=2 7–13, t=3 7–9) | not fired, **t=2 widened to octave 14** | bulk 1.0007 @ n64 q=17729; s_j ↓ |
| F-b | DEFERRED (unscored) | **SCORED, not fired** | tower 2^3.05 = 14.53 % of 2^21 |
| F-c | not fired (32 rows) | not fired, **34 rows** | X=0, p=0.0237, θ-insensitive |

## Scope covered vs deferred

COVERED:
- F-a: 48 unique n=64 rows (45 M1 + 3 new) at 2 depths; t=2 extended to octave
  14 (q=17729), t=3 densified (q=641); positive control t=3 q=193 reproduced.
- F-b: packet transport scored on all 56 rows (8 n=32 + 48 n=64), exact
  Fraction, incl. the n=32 stripped refuters as the banked NOT-falsifier.
- F-c: census 32 → 34 rows; both Poisson tests; theta ∈ {2,3,4}.
- Controls: modal shard-0 gate PASS; local + modal positive controls PASS;
  3/3 required-to-trip mutation controls PASS.

DEFERRED (compute; named, not cleared):
- F-a 3rd depth t=4 (q=193, g=2, ~194 chunks) — the only path to a genuine
  "deeper" test; F-a's ≥2-depth kill was exercised at exactly 2 depths.
- F-a t=3 octave-10 (q=1153, ~385 chunks) — depth-2 octave range unchanged.
- F-c 40+ row census — each new fixed-shape row is q>10369 (~30+ chunks each).

## Worst stripped ratio / reserve usage observed (headline numbers)

- Worst COSET-STRIPPED (not accident-priced) single-junction ratio: **2.8742**
  (n=32 t=4 q=97) → 2.8742³³ = 2^50.26. This is the banked NOT-falsifier
  (per-junction-uniform proxy); it is NOT a C2'' kill and is excluded per
  pre-registration.
- Worst BULK (coset-stripped AND accident-priced, the clause-(ii) object):
  **1.0662** (n=32 t=3 q=193); at n=64, ≤ 1.0007.
- Worst replayable-tower reserve usage: **14.53 %** of the 21-bit reserve.

## Why nothing fired (mechanism)

At n=64 the entire raw junction ratio (up to 8.4x) is carried by the coset
column (clause i, exact accounting) and orbit-quantized accidents (clause iii);
the residual bulk (clause ii) is ≡ 1 to <1e-3 across 8 octaves and 2 depths,
and no accident class is even populated at theta ≥ 1 (anti-correlated rare
window). The three-part shape absorbs the signal exactly where the pose says it
should. This is empirical support, not a proof — the conjecture asserts this at
EVERY official prize row and at full n=2^s and full 33-junction depth, none of
which is reached by these toy-tower toy-depth measurements.

## Round-3 design (pre-registered directions)

1. **The genuine 3rd depth (F-a "deeper").** Run t=4 (q=193 octave 7, then
   q=257 octave 8) via g=2 projective sharding — the only test that exercises
   F-a's ≥2-depth kill at a NEW depth. Budget ~194+ chunks/row; shard to <90 s.
   Pre-register: bulk trend increasing at BOTH t=4 and one lower depth ⇒ kill.
2. **Depth-2 octave-10 (t=3 q=1153) and a t=2 octave-15 (q~33000)** to push the
   bulk-flatness claim another octave at each depth (~385 / ~150 chunks).
3. **F-c to 50 rows** (add q up to ~20000, ~10 more rare-window cells) — tighten
   the Poisson two-sided p; and add k=4 cells if a very-high-q shape (q≥17980)
   is affordable, to test the window law at a second weight.
4. **F-b at genuine tower depth.** The current transport stacks a single
   junction 33×. Round 3 should transport a MEASURED multi-junction product
   (the real E_U[∏_j ρ_j]_reduced at a small true tower) rather than a stacked
   proxy, to test clause (ii)'s AGGREGATE form directly rather than the
   worst-junction over-estimate. This needs the nested b2b product measurement,
   not the marginal junction census.
5. **theta stress at n=64** in [2,4] with a search for ANY populated accident
   class at higher q (none seen through q=17729) — if one appears, price it and
   re-check the window law and the F-b absolute charge.

## Deliverables (scratchpad, prefix c2r2_)

`c2r2_falsifiers.md` (pre-reg), `c2r2_census_modal.py` (self-contained Modal
census), `c2r2_local.py` (controls + F-b), `c2r2_verdict.py` (final reads),
`c2r2_results.md` (tables + app ids), `c2r2_findings.md` (catches c2r2-C1..C5),
this report, plus `c2r2_new_rows.json`, `c2r2_verdict.json`,
`c2r2_verdict_full.log`, `c2r2_modal_run.log`.
