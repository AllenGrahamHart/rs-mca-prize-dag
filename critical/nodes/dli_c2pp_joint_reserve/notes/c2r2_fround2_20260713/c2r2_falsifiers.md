# C2'' F-ROUND 2 — PRE-REGISTRATION (fixed BEFORE any Round-2 computation)

Worker: fresh-context falsification worker, F-round 2, 2026-07-13.
Target predicate: `dli_c2pp_joint_reserve` (CONJECTURE C2''), pose
`critical/nodes/dli_prime_weighted_large_block_support/notes/C2PP_POSED_20260710.md`.
Round 1 = M1 (tower census, n=64, t<=3): F-a NOT fired (2 depths), F-c NOT fired
(32-row census), F-b DEFERRED (unscored diagnostic only).

This file is written BEFORE running any of the c2r2 experiments. It fixes the
exact ratios / thresholds / scales / depths for F-a, F-b, F-c round 2, plus the
NOT-falsifiers I will report but not score as kills. House Law #1.

## Conventions REUSED VERBATIM from M1 (cited)

Reused exactly from `m1_dli_m1_tower_census_modal.py` (Round 1 driver) and
`c2pp_calibration_20260710.py`:
- n = 64, h = 32, theta = 2.0 (pose convention). Coset column = k = 0.
- fused fiber model {N, B, +, -}, key in F_q^t; component order evens s=1..e
  then odds s=0..o-1 (`fiber_contribs`).
- `decompose_row`: three-part split — COSET (k=0, routed, clause i);
  ACCIDENT (k>=1 with class-conditional mean > theta * unconditional mean,
  clause iii); BULK (the rest, clause ii). Objects: `ratio` (raw), 
  `stripped_mean_ratio` r1, `stripped_mass_ratio` r2, `bulk_ratio`.
- Census kernels `joint_grid_census` (strategy B) and
  `joint_proj_chunk`/`assemble_from_projection` (strategy C projective shards),
  `even_null_census` (cn), `signed_all_census` (asum). All int64 exact with the
  projection-identity exact-division guard.
- Window law `lam_window(h,k,q,o) = C(h,k) 2^k / (2h q^o)` (clause iii).
- Reads `read_Fa` (octave-GM slope proxy) and `read_Fc` (Poisson window law).
- /33 junction convention (33 junctions), R_joint = 21 bits, 2^(21/33)=1.5544.

## F-b transport arithmetic — REUSED from the M4 assembly verifier (cited)

The "packet arithmetic" F-b transports through is pinned in
`m4_assembly_verifier.py::gate_calibration` (lines 402-417) and confirmed in
`m4a_findings.md` line 42: a replayable tower = one junction ratio `x` stacked
over the 33 junctions; its total charge is `x^33`, and it exceeds the joint
reserve iff (exact, Fraction):

        x ** 33  >  2 ** 21          <=>   x > 2^(21/33) = 1.554406...

Boundary sanity (banked): 1.5544^33 < 2^21; refuters 2.752^33 = 2^48.20 and
2.874^33 = 2^50.26 both EXCEED. Those refuters are STRIPPED (coset-stripped but
NOT accident-priced) single-junction ratios — they are the per-junction-uniform
NOT-falsifier (see below); the SURVIVING three-part claim stacks the BULK ratio.

## =============== F-a (round 2) ===============

RATIO (pre-registered, = M1's): per row, `bulk_ratio` from `decompose_row`
(coset-stripped clause i, accident-priced clause iii, theta=2). Continuity
object `s_j = GM(bulk_ratio in octave j) / (j+0.5)` (~ bulk / log2 q).

KILL RULE (pre-registered, = M1's read_Fa, unchanged): at a depth t, F-a FIRES
iff >= 3 octaves populated AND s_j strictly increasing across the top-3
populated octaves AND s_top >= 2 * s_min. F-a KILL iff it fires at >= 2 depths.
Equivalent statement of the pose's "> C log q per junction for every C": the
stripped+priced bulk ratio must grow super-polylogarithmically, i.e.
`log2(bulk_ratio)` must trend upward relative to `log2 q` without bound across
>= 3 increasing q-scales at >= 2 depths. Since a flat bulk gives
`s_j ~ 1/(j+0.5)` (DECREASING), any fire needs genuine bulk growth.

ROUND-2 EXTENSION (wider than M1). M1: t=2 octaves 7-13 (q 193..12289), t=3
octaves 7-9 (q 193,257,449,577). Round 2 adds, on top of the reused M1 rows:
- t=2 WIDER: q = 17729 (octave 14) — extends t=2 to 8 octaves (7..14).
- t=2 fill (also census, below): q = 11777, 13697, 15361 (octave 13).
- t=3 WIDER: q = 641 (octave 9 densify) and q = 1153 (octave 10) — extends t=3
  to octaves 7..10. [q=1153 is the expensive phase; if it does not fit the
  Modal budget it is DEFERRED and t=3 stays octaves 7-9 densified — reported
  as such, NOT inflated.]
- 3rd depth t=4 (q=193, octave 7): PRE-DECLARED DEFERRED (compute: g=2 4-D grid
  ~ 194 direction chunks; out of this round's safe budget). Round-3 design.

F-a verdict scope: SURVIVED if no depth fires over the widened grid actually
run; the deferred t=4 3rd depth and any deferred t=3 octave-10 are stated.

## =============== F-b (round 2, SCORED for the first time) ===============

TRANSPORT (pre-registered, = assembly-verifier packet arithmetic): for every
measured junction/row, take the clause-(ii) object `x = bulk_ratio`. The most
adversarial REPLAYABLE tower stacks the single worst junction at all 33
junctions: total bulk charge = `x_max ** 33` (exact Fraction on the measured
rational; float rows converted via Fraction). Clause-(iii) accidents are added
at their ABSOLUTE, q-independent window-law mass (NOT stacked 33x — that is the
whole point of clause iii): accident bit-charge `a = log2(1 + sum_over_accident_
classes(mass_k / total_unconditional_mass))`, counted ONCE.

KILL RULE (pre-registered): F-b FIRES iff there exists a replayable tower whose
total transported charge exceeds the full reserve, i.e.

        (x_max ** 33) * 2^a  >  2 ** 21          [x_max = max bulk_ratio > 0]

equivalently `33 * log2(x_max) + a > 21`. Search set: the n=32 calibration rows
(8), the reused M1 n=64 rows (t=2 x40, t=3 x4), and the new c2r2 rows. Report
`reserve usage = (33*log2(x_max) + a) / 21`.

NOT A KILL (reported, not scored): the STRIPPED-stacked tower
`stripped_mean_ratio_max ** 33` (the per-junction-uniform proxy). The banked
refuters 2.752^33 / 2.874^33 EXCEED 2^21; per the pose these are explicitly the
already-refuted uniform proxy, NOT the C2'' claim. I will print them and their
reserve-multiples as the banked NOT-falsifier, and confirm my scored path uses
`bulk_ratio` (accident-priced), which the mutation control below shows is
load-bearing.

## =============== F-c (round 2) ===============

FIXED SHAPE (pre-registered, = M1's): (n=64, t=2). Census cell = (row q, class
k in {3,4,5}) with `lam_window(32,k,q,1) <= 1/2` (rare-window regime; over the
frozen list this is exactly k=3). Accident flag: class k conditional mean >
theta=2 * unconditional (from `decompose_row`). Orbit quanta V_k = asum[k] /
2^(h-k) / (2h) (integrality asserted; sub-orbit anomalies flagged, not scored).

KILL RULE (pre-registered, = M1's read_Fc, unchanged):
- PRIMARY (exceedance frequency): X = #cells flagged accident; model
  P_cell = 1 - exp(-lam); exact Poisson-binomial two-sided tail; KILL iff
  p < 1e-3.
- SECONDARY (orbit quanta): T = sum V_k; vs Poisson(sum lam); exact two-sided
  tail; KILL iff p < 1e-3.
- Census NOT ARMED if < 30 rows.

ROUND-2 EXTENSION: reuse M1's 32 census rows (banked in m1_dli_m1_results.json)
+ new census rows q in {11777, 13697, 15361, 17729} => target 36 rows (>=30).
Spot-check theta in {2,3,4} for insensitivity (verdict at theta=2). Any larger
(50+ row) census is DEFERRED (each new census row requires q>10369, i.e. many
direction-sharded Modal calls; reported as DEFERRED not cleared).

## NOT-falsifiers (banked; I will report but NEVER score as kills)

1. Raw unstripped conditional ratios (F2b's 4.25x / 8.40x) — the coset column
   is exact accounting (clause i).
2. Single orbit-quantized spikes consistent with the exact window mean
   (the 6.6x / 9.4x classes; masses exact multiples of 32/64).
3. Per-level, per-junction-uniform, or factorized proxy failures — including
   the stripped-stacked tower 2.752^33 / 2.874^33 (F-b NOT-falsifier above).

## Controls (pre-registered)

- POSITIVE CONTROL: reproduce a banked M1 number exactly — (a) Modal shard-0
  gate: the 8 banked n=32 f2b rows (BANKED_F2B / BANKED_F2B_RATIOS) + n64
  strategy-B==strategy-C at (t=2,q=193); (b) LOCAL: n=32 bulk GM = 0.967 and the
  8 pose bulk values {0.998,1.010,0,0,1.033,1.066,0.760,0} via the M1 kernels.
- MUTATION CONTROL (required-to-trip): (i) F-b scored on `stripped_mean_ratio`
  instead of `bulk_ratio` MUST fire (2.874^33 > 2^21) — proves accident-pricing
  is load-bearing; (ii) F-a fed a synthetic bulk growing as q^0.1 MUST fire;
  (iii) F-c with theta=1 (over-flagging) MUST drop p below the kill line on the
  census. All three verified before trusting the null reads.
- Nonemptiness asserts everywhere (#137): every census/decomposition asserts
  n_null>0, sum(an)==3^h, projection exact-division, >=30 census rows before an
  F-c read.

## Verdict discipline

SURVIVED only if NO pre-registered falsifier fires within the scope actually
run, with deferred parts named. PARTIAL if a reduced round (compute-limited)
with no kill. KILLED if any fires (bank the witness). No weakening of the
coset-strip, the /33 convention, the 21-bit reserve, or the accident pricing.
