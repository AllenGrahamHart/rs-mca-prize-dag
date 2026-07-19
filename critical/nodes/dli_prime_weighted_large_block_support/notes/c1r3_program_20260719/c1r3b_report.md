# C1'-r3 F-ROUND 2 — REPORT (c1r3b)

## VERDICT: **SURVIVED** — no kill line fired; MINTING IS GO

C1'-r3 (pose UNCHANGED from `c1r3_pose.md`: official-admissibility gate
v_2(q-1) >= 41 / analogue 20, extended RAW ledger w in [L+1, L+7], allowance
4) survived its second pre-registered adversarial round with the kill lines
re-armed ABOVE the iid asymptote exactly as the round-1 report prescribed.
Complete census of the in-gate family through Q_census = 1.95e9 (153 rows,
octaves 28-30) + 11 pre-named octave-31 probes + the deferred w6 accident
row, all exact-rational. Nothing was weakened mid-round; all controls
passed before any verdict was read.

## Kill-line outcomes (pre-registered in `c1r3b_falsifiers.md`, frozen first)

- **KILL-LITERAL (K'_r3 > 4) — NOT FIRED.** Worst exact K'_r3 =
  **1.401644312** (q=377487361, v_2=23, W_ext=0, exact
  35507502101438673/25332747971067904) — a 2.85x margin, over 164 exactly
  evaluated rows (153-row complete census + 11 probes, ledgers at all 52
  rows with env >= 1).
- **KILL-AMBER-2 (K'_r3 >= 2) — NOT FIRED.** Zero rows at or above 2. The
  re-armed line sits 43% above the observed ceiling.
- **KILL-IIDX (iid-excess trend) — NOT FIRED.** Condition (a) fails under
  both pre-registered readings: the octave-worst exact-K' series
  1.0082 (26) -> 1.0245 (27) -> 1.4016 (28) -> 1.3334 (29) -> 1.3894 (30,
  census-partial) is NOT increasing on any terminal >= 3-octave run (28->29
  decreases). The envelope PLATEAUS in [1.33, 1.40] — the round-1 "decisive
  test" (does it re-accelerate toward 2^32?) is answered NO: saturation,
  corroborated by the octave-31 probes (max K' 1.0574; deepest-split rows
  at/below the iid baseline: v_2=30 -> 0.979, v_2=28 -> 0.933).
- **Legacy band [1,2): 49 rows (NOT-kill, reported).** The band populates
  (2/33 in round 1 -> 49/164 here) while its ceiling saturates ~1.4 —
  extreme-value behavior of an iid-like spectrum, not accident growth
  (finding c1r3b-C4); 46/49 have completely empty extended ledgers.
- **Controls: ALL PASS.** C-REP-1/2 (both round-1 ambers reproduced exactly
  incl. the worst row), C-GROUND, C-XVAL (T-B/T-C CRT trios == exact uint64
  A), MUT-1 (fires at 6.199 > 4 on the new code path), MUT-2 (fires at all
  164 rows), L2-XVAL (strategy-C == grid at q=12289), plus local SMOKE.
  Zero integrity failures; 5 worker-variance timeouts all recovered by the
  pre-registered shrink/retry path.

## The deferred accident row q=918552577 (mandate priority 1) — ANSWERED

- exact env = (E-1)/r = **3.000057687** (46233153981711603/15410754991685632):
  the w6 accident is REAL in the envelope — 3.0x the iid baseline, above the
  amber-2 line on bare envelope, the same lone-low-weight-orbit mechanism as
  the r2 killers.
- the w6 channel MATERIALIZES in W_ext exactly as designed: orbit spectrum
  w2..8 = {0,0,0,0,1,0,1} — one primitive w6 orbit at mass 2N*2^-6 = **1**
  (carrying the 32 signed vanishers of the round-1 accscan) + one w8 orbit at
  mass 1/4; W_ext = 5/4.
- exact K'_r3 = 5137017109079067/3852688747921408 = **1.333358972** -> the
  legacy fluctuation band [1,2), a 3.0x margin under the allowance. NOT a
  kill; NOT an amber-2. The extended ledger is LOAD-BEARING at precisely the
  accident row class the r3 re-pose targeted — without lever (a) this row
  would have fired KILL-AMBER-2 and forced MIXED.
- integrity: independent uint32 mod-p kernel agrees with the exact uint64
  A_total; mass invariants exact; app ap-T4ajwSnJ73uyVZyXPXI0sQ.

## Segment census + probes (detail in c1r3b_results.md + c1r3b_table.txt)

Complete below Q_census = 1.95e9: octave 28 (22/22), octave 29 (56/56),
octave 30 to the cap (75/91). Probes: 11/11 pre-named octave-31/deep-v_2
rows. Deferred (honest): oct-30 tail 16 rows, oct-31 189 non-probe rows
(budget law; 4 of them beyond every kernel's memory wall). The census worst
rows and their ledgers: 377487361 (K' 1.4016, W=0), 1431306241 (env 1.4733,
two w8 orbits -> K' 0.9822), 1365245953 (1.3894, W=0), 290455553 (env
1.7401, one w7 orbit -> K' 1.1601), 918552577 (below).

## L=2 (mandate item 3)

Gated L=2 rows: reachable set EMPTY this round — wall documented in results
(min gated prime 7340033: (q,q) grid 4.3e14 B; strategy-C q+1 = 7.3e6
1-D DPs ~ 3.4e15 elem-ops >> budget law). Near-gate v_2-ladder instrument
(N=32 to v_2=13, N=64 to v_2=12; strategy-C validated against the direct
grid at scale): the L=2 picture MIRRORS L=1 — iid saturation at balance
(env 0.933..1.009 at r = 0.035..0.88), tiny env off balance (<= 0.056 at
N=64), and the single above-1 row (40961, v_2=13) repriced 1.0093 -> 0.8971
by one w9 orbit inside the L=2 window [3,9]. The pre-registered adverse
tripwire (v_2-graded growth extrapolating past 4 by v_2=20) is NOT tripped
at either aspect. First nontrivial level-uniformity evidence for the r3
shape.

## The minting + amber-cascade prescription (for the banking
## session to execute mechanically; recommendations, not surgery — I am a worker)

### 1. The r3 node statement text (append to `dli_dyadic_k_core` per #104,
###    preserving all history; status stays REFUTED for the OLD pose, the
###    appended block MINTS the r3 successor as the branch's live pose)

> C1'-r3 MINTED (2026-07-19, F-ROUND 2 passed; packets
> notes/c1r3_program_20260719/ + c1r3b round-2 files; catches c1r3-C1..C9,
> c1r3b-C1..): For every generated prime-field full-half-section row
> (q, n'=2N, L) with q = 1 mod n', 2^N >= q^L, N >= 16L, AND the
> official-admissibility gate v_2(q-1) >= 41 (analogue validation proxy:
> v_2(q-1) >= 20 via Proth rows q = c*2^k+1, odd c, k >= 20), let T(lambda),
> E, r = q^L/2^N be as in C1PRIME_LEVEL_SCALED_POSE.md and let W_ext be the
> RAW primitive signed-shift orbit ledger over the EXTENDED window
> L+1 <= w <= L+7 (mass 2N*2^-w per orbit; decision 4a conventions). Then
> E-1 <= 4 r (1 + W_ext). Evidence: round 1 (MIXED under the K'>=1 amber
> line, worst K'_r3 = 1.0245 over the complete 33-row in-gate census < 2^28;
> the two ambers are iid-baseline fluctuations, finding c1r3-C5); round 2
> (SURVIVED; kill lines re-armed above the iid asymptote per the round-1
> pre-registration: literal 4 unchanged, amber-2, iid-excess trend; complete
> census extended through 1.95e9 — octaves 28-30, 153 rows — plus 11
> pre-named octave-31/deep-split probes to v_2 = 30; worst exact K'_r3 =
> 1.401644 at q=377487361, 2.85x under the allowance; the per-octave
> envelope SATURATES in [1.33, 1.40] — no trend kill; 49 rows in the
> iid-fluctuation band [1,2), 46 with empty ledgers; the deferred w6
> accident row 918552577 priced exactly: env 3.000058 -> K'_r3 1.333359 via
> its w6 orbit at mass 1 — the extended ledger load-bearing exactly as
> designed, catch c1r3b-C1; near-gate L=2 ladder to v_2=13 mirrors the L=1
> iid saturation, adverse tripwire not tripped). STATUS: survived TWO
> pre-registered adversarial rounds; unproved; evidence toward marginal
> baseline coverage, not a logical premise of B-WEAK. The r2 refutation of
> the ungated L+5 pose STANDS untouched; ungated rows remain refuted
> forever. Scope caveat: exact verdicts to 1.95e9 census + probes; octave-31
> census and gated L=2 remain open (round-3 items).

Node falsifier field update:

> One official-admissible or analogue-gated row (v_2(q-1) >= 41 / >= 20)
> with E-1 > 4r(1+W_ext) on the full [L+1, L+7] ledger — the census +
> exact-E machinery computes both sides.

### 2. Baseline re-arm wiring (`dli_marginal_baseline100_coverage`
###    conditional.md; supersession appendix per #155-style discipline)

Append a "C1'-r3 re-wiring" section: predicate list becomes
`dli_dyadic_k_core` (r3 block) + `dli_wcl_zone_coverage-EXT`, where the zone
predicate is widened to the extended window:

```text
WCL-ZONE-ext:  W_ext(R, ell_j) <= 1/32 at every scheduled level j
               (window ell_j+1 <= w <= ell_j+7, N_j = 256*ell_j).
```

Per level: E_j - 1 <= 4 r_j (1 + W_ext) <= 4(1 + 1/32) = 33/8, E_j <= 41/8,
and the aggregate arithmetic is UNCHANGED: A(R) <= (41/8)^34 < 2^100 <=>
41^34 < 2^202 (exact integers banked in c1r3_pose.md; 19.8432 bits slack).
The gate hypothesis v_2(q-1) >= 41 is VACUOUS at official rows (ambient
split q = k*2^41+1) — no downstream row is lost; cite
dli_wcl_weight3_ambient_exclusion / weight4 / ell2 siblings /
newton_short_window for the gate's official legitimacy.

### 3. The zone node widening (`dli_wcl_zone_coverage`)

Statement change: ledger window `L+1 <= w(O) <= L+5` -> `L+1 <= w(O) <= L+7`
(rename W_cl -> W_ext or note the widened window in place). At every
scheduled level ell >= 8 the two added weight classes are FREE
(`dli_wcl_newton_short_window_exclusion`: L+7 <= 2L for L >= 7). At
ell in {1 (x2), 2, 4} per-orbit masses 2N_L*2^-w exceed 1/32 throughout the
window, so the bound remains equivalent to slot emptiness; the open-slot
list widens by SIX (next item).

### 4. Six new zone slots (mint as TARGETs, mirroring the four existing
###    slot nodes minted 2026-07-19 at the WCL amber ceremony)

- `dli_wcl_slot_1_7_emptiness` (TARGET): "No reduced signed weight-7
  polynomial vanishes at an order-512 root at any official row (ell=1
  extended window, w = L+6). FALSIFIER: one official-admissible prime
  (q < 2^256, v_2(q-1) >= 41) carrying the vanisher. Minted at the C1'-r3
  adoption; bookkeeping of record = the zone node's
  official_terminal_attack.md."
- `dli_wcl_slot_1_8_emptiness` (TARGET): same shape, weight-8 at order-512
  (ell=1, w = L+7).
- `dli_wcl_slot_2_8_emptiness` (TARGET): "No reduced signed weight-8
  polynomial P has P(w) = P(w^3) = 0 at exact order 1024 at any official
  row (ell=2 extended window)." Same falsifier form.
- `dli_wcl_slot_2_9_emptiness` (TARGET): same at weight 9, order 1024.
- `dli_wcl_slot_4_10_emptiness` (TARGET): "No reduced signed weight-10
  polynomial has the four odd-power vanishings at order-2048 roots at any
  official row (ell=4 extended window)." Same falsifier form.
- `dli_wcl_slot_4_11_emptiness` (TARGET): same at weight 11, order 2048.

Edges: the six new slots wire into `dli_wcl_zone_coverage` exactly as the
four existing slots (1,5), (1,6), (2,7), (4,9) do. Ten emptiness slots
total. The weight-3/4 norm-census machinery is the named attack.

### 5. The dli amber wiring (`dli_prime_weighted_large_block_support` lane)

- The r3 mint does NOT flip the dli node amber by itself: it restores a live
  (twice-survived, unproved) C1' successor to the route
  C1'-r3 + S1 norm-sieve + endpoint rule => DLI-AGG almost everywhere.
- RECOMMENDED amber condition for the branch node `dli_dyadic_k_core`
  watch-line (recorded, not a status flip by this worker): amber-eligible
  when (i) both rounds' packets replay (verifiers), (ii) WCL-ZONE-ext slot
  arithmetic is acknowledged downstream (the six new TARGETs minted), and
  (iii) the maintainer accepts the round-2 amber recalibration (K' >= 2
  above the iid asymptote) as the standing watch line for future rounds.
- The round-2 standing watch for any FUTURE evidence round: literal 4
  (never moved), amber-2, iid-excess trend as frozen in c1r3b_falsifiers.md.

### 6. Round-3 escalation targets (pre-commitments for the next worker)

1. Octave-31 census completion (199 rows; needs either budget dispensation
   or a >16GiB/longer-ceiling compute-law amendment for q > 4.05e9 — 4 rows
   are outside every kernel at the current law).
2. The full-ledger question (drop w_max entirely) stays the round-3
   escalation lever if any new zone slot resists (round-1 report sec. 5).
3. A quantitative iid-approximation theorem under v_2(q-1) large (the bulk
   proof lead; round-1 report item 6) — now with 918552577 as the worked
   example of accident-vs-ledger cancellation.
4. L=2 in-gate remains unreachable exactly; the near-gate ladder (this
   round) is the standing instrument; a proof-side level-uniformity argument
   is the only route to gated L=2.

## Deliverables on disk (scratchpad, prefix c1r3b_)

`c1r3b_falsifiers.md` (pre-registration, FIRST), `c1r3b_census_modal.py`,
`c1r3b_schedule.py`, `c1r3b_runwave.sh`, `c1r3b_collect.py`,
`c1r3b_l2collect.py`, `c1r3b_results.md`, `c1r3b_findings.md`,
`c1r3b_report.md`, `c1r3b_tierA/B/C*.txt`, logs/ (per-shard, DONE_OK-stamped).
