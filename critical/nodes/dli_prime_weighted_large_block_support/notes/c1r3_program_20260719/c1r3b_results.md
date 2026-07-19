# C1'-r3 F-ROUND 2 — results (c1r3b; exact tables + Modal app ids)

- **predicate:** C1'-r3 unchanged (`c1r3_pose.md`): gate v_2(q-1) >= 20 (analogue
  of official 41), extended RAW ledger w in [2,8] at L=1/N=32, allowance 4,
  E-1 <= 4r(1+W_ext). K'_r3 = (E-1)/(r(1+W_ext)); env = (E-1)/r.
- **kill lines (frozen FIRST in `c1r3b_falsifiers.md`):** KILL-LITERAL K'>4;
  KILL-AMBER-2 K'>=2; KILL-IIDX (iid-excess trend crossing 4 before 2^41);
  legacy band [1,2) = NOT-kill (reported).
- **scripts:** `c1r3b_census_modal.py` (all modes), `c1r3b_schedule.py`,
  `c1r3b_runwave.sh`, `c1r3b_collect.py`, `c1r3b_l2collect.py`,
  `c1r3b_ledgersched.py`. All Modal runs via tools/ramguard modal +
  tools/modal_run_script.py (2CPU/16GiB/280s law). Exact-rational verdict path
  (Fraction/bigint); floats display only. FULL per-row table:
  `c1r3b_table.txt` (164 rows); per-shard logs DONE_OK-stamped in logs/.

## Family (LOCAL, ramguard tiny; #137 asserts 1-3 PASS)

Complete re-enumeration of gated Proth primes q = c*2^k+1 (odd c, k >= 20)
below 2^32: **401 primes; 33 below 2^28; 368 in [2^28, 2^32)** — asserted equal
to the round-1 accscan counts. Segment octaves: 2^28: 22, 2^29: 56, 2^30: 91,
2^31: 199. v_2 histogram: {20:186, 21:93, 22:46, 23:20, 24:9, 25:5, 26:4,
27:3, 28:1, 30:1}; deepest v_2 = 30 (q = 3221225473 = 3*2^30+1).

## Kernels + tier ladder (bench-set BEFORE any verdict row; app ap-fmoPc2ZAsEivIaxgu3vszL)

New round-2 kernels (factored sub-step (1+x^s)(1+x^-s) slice-add DP, two
preallocated arrays, no temporaries): **T-A** uint64 exact (unconditionally:
cells <= 4^step, A < 2^64 strict; wrap-sum invariant == 0 mod 2^64); **T-B**
uint32-wrap + uint32 mod-{1073741789, 1073741783} (CRT modulus 2^32*p1*p2 ~
2^92); **T-C** uint16-wrap + uint16 mod-{16381,16369,16363,16361} (modulus ~
2^72; alternate prime 16349 used at one row after a persistent worker-variance
timeout — any coprime modulus completes the CRT). Bench rates at q=246415361:
uint64 17.2s (eff 22 GB/s), u32wrap 8.6s, u32modp 25.3s, u16wrap 4.3s,
u16modp ~13.5s, ledger w2..8 30.4s. Time envelopes all EXCEEDED the memory
caps, so the ladder was memory-bound as pre-registered: Tier A q <= 0.98e9
(70 rows, 1 shard each, packed), Tier B q <= 1.95e9 = Q_census (83 rows, 3
shards each), Tier C = 11 pre-named probes (5 shards each).

## Controls (ALL PASS before any verdict was read; #137 assert 5 PASS)

- **C-REP-1** (bench): q=246415361 (round-1 worst) E-1 == banked exactly;
  ledger w2..8 re-enumerated ALL ZERO == banked W_ext=0.
- **C-XVAL** (bench): T-B trio CRT == exact A; T-C quint CRT == exact A.
- **C-REP-2/C-GROUND/MUT-1** (controls shard): q=81788929 E-1 == banked,
  W_ext == 0, K' = 1.008154437 reproduced; q=7937 E-1 == banked; q=63361
  (gate-dropped, r2 window) FIRES at K' = 6.199084 > 4 with E-1 == banked and
  the fast enumerator revalidated (w2..6 {0,1,3,10,36}, w7 131, W_cl 76).
- **SMOKE (local):** T-A == banked at 7937; T-B/T-C == T-A; L2 strategy-C ==
  L2 grid at q in {193, 257}; L=2 q=193 env = 0.149933 == banked M2 row 0.15.
- **L2-XVAL (at scale):** strategy-C == direct grid at q=12289
  (A = 126288915136), exact divisibility asserted in every assembly.
- **MUT-2:** fired at all 164 rows (E-1 > 0 and env > 1e-6 asserted
  everywhere; K' > 1e-6 at all 52 ledgered rows).

## THE DEFERRED ACCIDENT ROW q=918552577 (v_2=22; app ap-T4ajwSnJ73uyVZyXPXI0sQ)

The unique in-gate w<=6 accident carrier below 2^32 (32 signed w6 vanishers,
round-1 accscan), DP-infeasible in round 1, evaluated EXACTLY this round
(uint64 kernel, 74.4s, peak 14.1GB; independent uint32 mod-1073741789
cross-shard agrees):

```text
A_total = 32967553792
E-1     = 46233153981711603/72057594037927936
env     = 46233153981711603/15410754991685632 = 3.000057687   <- the accident is REAL
orbits w2..8 = {0,0,0,0,1,0,1}: ONE primitive w6 orbit (mass 2N*2^-6 = 1)
               + one w8 orbit (mass 1/4);  W_ext = 5/4
K'_r3   = 5137017109079067/3852688747921408 = 1.333358972  -> band [1,2), NOT a kill
```

The w6 channel MATERIALIZES in W_ext exactly as the r3 design intended; on
the bare envelope this row would have fired KILL-AMBER-2 (env 3.0 > 2) — the
extended ledger is LOAD-BEARING at precisely the targeted accident class,
repricing 3.000 -> 1.333 (3.0x under the allowance).

## SEGMENT CENSUS — COMPLETE below Q_census = 1.95e9 (153/153 rows exact)

Verification: every Tier A + Tier B row measured (collector cross-checked all
CRT residues against exact uint64 A where both exist; 83 crtB assemblies).
Worst rows (full table in c1r3b_table.txt; 52 rows have full ledgers — every
row with env >= 1, #137-complete):

| q | v2 | env | W_ext | K'_r3 (exact) | note |
|---|---|---|---|---|---|
| 377487361 | 23 | 1.401644 | 0 | **1.401644312** = 35507502101438673/25332747971067904 | ROUND WORST |
| 1431306241 | 20 | 1.473264 = 35377985723389915/24013333967405056 | 1/2 (two w8) | 0.982176146 | repriced below 1 |
| 1365245953 | 21 | 1.389420 = 63649405960591697/45810052493213696 | 0 | 1.389420062 | oct-30 census worst |
| 918552577 | 22 | 3.000058 | 5/4 (w6+w8) | 1.333358972 | the accident row |
| 290455553 | 20 | 1.740144 | 1/2 (one w7) | 1.160095862 | oct-28 raw-env worst |

- **NO row with K'_r3 > 4 (literal): worst = 1.4016, a 2.85x margin.**
- **NO row with K'_r3 >= 2 (amber-2): NONE.**
- Legacy band [1,2): **49 rows** (all exact; NOT-kill per pre-registration;
  round 1 had 2/33 — the band POPULATION grows with octave row-count while
  its CEILING plateaus at ~1.4, an extreme-value effect, finding c1r3b-C4).
- w2..6 orbits ZERO at every ledgered row except 918552577 (w6=1) —
  consistent with the round-1 accscan; window orbits present at 5 census
  rows + 1 probe (of the 52 ledgered), sitting exactly at the top of the
  raw-env list and repricing the outliers (3.000 -> 1.333, 1.740 -> 1.160,
  1.473 -> 0.982; 3 rows pulled out of the band entirely).

## Per-octave worsts + KILL-IIDX (the trend line) — NOT FIRED

UB_j = octave max of exact K'_r3 (ledger at every env >= 1 row):

| octave | rows | worst UB (exact K') | at q | worst raw env |
|---|---|---|---|---|
| 2^22-2^27 | 33 | (round-1: 0.3075 / 0.4487 / 0.5919 / — / 1.0082 / 1.0245) | | |
| 2^28 | 22 (complete) | 1.401644 | 377487361 | 1.740144 |
| 2^29 | 56 (complete) | 1.333359 | 918552577 | 3.000058 |
| 2^30 | 75/91 (census to 1.95e9, partial octave) | 1.389420 | 1365245953 | 1.473264 |
| 2^31 | 11 probes only | (probe max K' 1.057409 at 3001024513) | | |

- Condition (a) [eps_j > 0 strictly increasing across the last >= 3 populated
  octaves]: **FAILS under both pre-registered readings.** Strict (complete
  octaves only, 22..29): terminal run [29] has length 1 (1.3334 < 1.4016 at
  28 -> 29 is a DECREASE). Inclusive (octave-30 census-below-cap point
  added): terminal run [29, 30] length 2 < 3. In both cases the series
  PLATEAUS in [1.33, 1.40] across octaves 28-30 — saturation, not growth.
- Condition (b) moot; for the record the 26-29 LS extrapolation crosses 4
  only beyond 2^41 (crossing ~2^43), and adding the plateau/probe points
  flattens it further.
- Probes corroborate saturation: max probe K' 1.0574; the DEEPEST-split rows
  sit AT/BELOW the iid baseline (v_2=30: env 0.978788; v_2=28: 0.932716;
  v_2=27: 0.889 / 1.008 / 0.992).

## Tier-C probes (11/11 evaluated; NOT census; corroboration only)

2013265921 (v27) env 1.111047 K' 0.888837 (one w8 orbit); 2281701377 (v27)
1.008476 (W=0); 2998927361 (v22) 0.990282; 3001024513 (v21) 1.057409 (W=0);
3164602369 (v21) 0.936959; 3175088129 (v22) 1.036810 (W=0); 3177185281 (v21)
0.891504; 3192913921 (v20) 1.009817 (W=0); 3221225473 (v30) 0.978788;
3489660929 (v28) 0.932716; 3892314113 (v27) 0.992359.

## L=2 program (mandate item 3)

**Gated-row wall (documented):** minimal gated prime 7340033 -> (q,q) grid
4.3e14 bytes; strategy-C (the c1r2 round-3 item-4 projective sharding,
sum_{d in P^1(F_q)} N_d identity) still needs q+1 = 7,340,034 one-dimensional
DPs ~ 3.4e15 elem-ops ~ >4000 worker-ceilings: the reachable gated set at
L=2 is EMPTY under the compute/budget law. DEFERRED as a class.

**Near-gate v_2-ladder (instrument; all v_2 < 20, out of hypothesis):**

| N | q | v2 | r | env | ledger/K' |
|---|---|---|---|---|---|
| 32 | 257 | 8 | 1.5e-05 | 0.121291 | — |
| 32 | 12289 | 12 | 0.0352 | 0.964114 | — |
| 32 | 18433 | 11 | 0.0791 | 0.979651 | — |
| 32 | 40961 | 13 | 0.3906 | 1.009277 | one w9 orbit, W=1/8 -> K' = 0.897135 |
| 32 | 61441 | 12 | 0.8789 | 0.933068 | — |
| 64 | 7681 | 9 | 3.2e-12 | 0.036683 | — |
| 64 | 12289 | 12 | 8.2e-12 | 0.009469 | — |
| 64 | 18433 | 11 | 1.8e-11 | 0.055535 | — |

Same picture as L=1: iid-baseline saturation at balance, tiny env off
balance, and the extended window repricing the one above-1 row. The
pre-registered ADVERSE TRIPWIRE (env increasing in v_2 extrapolating past 4
by v_2 = 20) is NOT tripped at either aspect (not even monotone). Strategy-C
machinery validated (xval q=12289 == grid; exact divisibility everywhere);
40961 and 61441 ran as 8 direction-chunk shards each; N=64 rows as 3-prime
CRT grids (primes < 2^49, per-row-sum uint64-safe mass checks).

## Deferred / gaps (honest; pre-registered coverage rule)

- Octave-30 tail (1.95e9, 2.147e9]: 16 rows not censused (1 of them,
  2013265921, probed). Octave-31: 199 rows minus 10 probes = 189 not
  measured (budget law); 4 rows (4076863489, 4194304001, 4276092929,
  4293918721) additionally exceed every kernel's 16GiB memory wall.
- Gated L=2: unreachable (wall above).
- Official aspect N=256L: untouched, as always.

## Shard accounting + failures

~305 worker-runs total (279 scheduled + bench/controls/row918 + 11 ledger
shards + 1 L2-ledger + 8 recovery shards), cents-to-low-$ total. Failures:
5 worker-variance timeouts, ALL recovered by the pre-registered
shrink/retry path (2 dpBrow2 splits, 1 straight retry, 1 mod-p retry, 1
alternate-prime substitution); the three stale DONE_FAIL logs
(B2_1192230913, B2_1286602753, Cp_3221225473_16363) are superseded by
B2w_/B2p_ splits and Cp_3221225473_16349. Zero integrity failures: every
completed shard passed its mass-invariant / CRT / divisibility asserts.

## Modal app ids

bench ap-fmoPc2ZAsEivIaxgu3vszL; controls (see controls.log); row918
ap-T4ajwSnJ73uyVZyXPXI0sQ; all other shards: app id in each DONE_OK log
(logs/<tag>.log, "View run at" line).
