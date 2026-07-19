# C1'-r3 F-ROUND 2 — findings (catches c1r3b-C1 ..)

## c1r3b-C1 — THE DEFERRED ACCIDENT ROW IS PRICED BY THE EXTENDED LEDGER
## (the round's central question, answered)
q=918552577 (v_2=22; the unique in-gate w<=6 accident carrier below 2^32,
deferred from round 1): exact env = (E-1)/r = 46233153981711603/15410754991685632
= **3.000057687** — the w6 accident REALLY pumps the bare envelope, to 3.0x the
iid baseline (the same lone-low-weight-orbit mechanism as the r2 killers; on
bare envelope this row would have TRIPPED the amber-2 line and made the round
MIXED). The extended ledger materializes exactly the designed charge: orbits
w2..8 = {0,0,0,0,1,0,1} — ONE primitive w6 orbit (mass 2N*2^-6 = 1, carrying
the 32 signed vanishers seen by the round-1 accscan) plus one w8 orbit (mass
1/4), W_ext = 5/4. Priced ratio K'_r3 = 5137017109079067/3852688747921408 =
**1.333358972** — inside the legacy fluctuation band [1,2), 3x under the
allowance, NOT a kill under the frozen round-2 lines. The w6 channel
materializes in W_ext and the ledger is LOAD-BEARING at precisely the row
class the r3 design targeted. Cross-checked: independent uint32 mod-p kernel
agrees with the uint64 A_total (A = 32967553792); DP mass invariant exact;
env exact-rational. App ap-T4ajwSnJ73uyVZyXPXI0sQ, peak_rss 14081MB.
Note also env = 3.000058 ~ 1 + 2*(1) hm: env - 1 = 2.000058 ~ 2*W6-mass —
the accident's excess over iid is almost exactly twice the w6 orbit mass;
recorded as an observation (post-hoc, not pre-registered).

## c1r3b-C2 — new-kernel ladder validated end-to-end
uint64 (T-A), uint32-wrap+2xmod-p CRT (T-B), uint16-wrap+4xmod-p CRT (T-C)
all reproduce the exact A_total at q=246415361 (bench, ap-fmoPc2ZAsEivIaxgu3vszL)
and the banked round-1 E-1 fractions at 246415361/81788929/7937/63361; MUT-1
fires on the new code path; uint64 rate 19-22 GB/s effective (q=9.2e8 in 74s
single shard — the round-1 "16GiB memory wall" for this row is GONE with the
2-array slice-add kernel: peak 14.1GB < 16GiB).

## c1r3b-C3 — SURVIVED: all three re-armed kill lines pass on the complete
## census to 1.95e9
KILL-LITERAL: worst exact K'_r3 = 1.401644312 (q=377487361, v_2=23, W_ext=0)
— 2.85x under the allowance, over 153 census rows + 11 probes + the accident
row. KILL-AMBER-2 (K'>=2): ZERO rows. KILL-IIDX: condition (a) fails under
both pre-registered readings — the octave-worst series 1.0082 -> 1.0245 ->
1.4016 -> 1.3334 -> [1.3894 partial] PLATEAUS in [1.33, 1.40] across octaves
28-30 (the 28->29 step DECREASES); saturation, not growth. The round-1
"decisive test" question (does the envelope re-accelerate at 2^30..2^32?) is
answered NO within reach: octave-30 census worst 1.389, octave-31 probe max
1.057.

## c1r3b-C4 — the fluctuation BAND populates but its CEILING saturates
Round 1: 2/33 rows in [1,2), max 1.0245. Round 2: 49/164 rows in [1,2), max
1.4016, and the per-octave max is FLAT (1.40 / 1.33 / 1.39) while the octave
row-count grows 22 -> 56 -> 91. This is extreme-value behavior of an
iid-like spectrum (max of n samples grows in n, saturating), NOT accident
growth: 46 of the 49 band rows have COMPLETELY EMPTY extended ledgers, and
the 6 measured rows carrying w6/w7/w8 orbits sit exactly at the top of the
raw-env list — the ledger reprices the outliers (3.000 -> 1.333, 1.740 ->
1.160, 1.473 -> 0.982) and pulls 3 rows out of the band entirely
(897581057, 1431306241, 2013265921). Consequence
for calibration: the amber-2 line at 2x iid is ABOVE the observed ceiling
with 43% headroom; the old K'>=1 line would now flag 49 rows — the round-1
recalibration (c1r3-C5) is strongly confirmed out of sample.

## c1r3b-C5 — deep-split rows sit AT or BELOW the iid baseline (post-hoc)
The five deepest-v_2 probes: v_2=30 -> env 0.9788, v_2=28 -> 0.9327,
v_2=27 -> {0.889 (after w8 reprice), 1.0085, 0.9924}. Within the census,
worst rows cluster at v_2 in {20,21,23} while v_2 >= 24 census rows all sit
below 1.09. The deeper the dyadic split beyond the gate, the closer the row
hugs the iid baseline — directionally the gate's structural bet, visible in
data. (Post-hoc observation, not a pre-registered line; small samples at
each v_2 level.)

## c1r3b-C6 — L=2 level-uniformity of the iid-saturation picture
Near-gate L=2 ladder (out of hypothesis, instrument): at N=32 the balanced
rows (r = 0.035..0.88) give env 0.933..1.009 — the same iid saturation as
L=1 — and the single above-1 row (q=40961, v_2=13, the DEEPEST feasible
near-gate row) carries one w9 orbit inside the L=2 window [3,9], repricing
1.0093 -> 0.8971. At N=64 (r ~ 1e-11) env <= 0.056. The pre-registered
adverse tripwire (env growing in v_2, extrapolating past 4 by v_2=20) is
NOT tripped at either aspect. The window's level-scaling does the right
relative work at L=2 exactly as at L=1 (mirrors c1r3-C7).

## c1r3b-C7 — machinery: the round-1 memory wall is gone; CRT tiers to 4e9
(a) The factored-substep slice-add uint64 kernel runs q=9.19e8 in 74s at
14.1GB peak (round-1's kernel needed ~3 arrays + np.roll temporaries and
was capped at 2.6e8). Cells <= 4^step <= 2^64 with A < 2^64 strict makes
uint64 UNCONDITIONALLY exact — no headroom guard needed. (b) Wrap-residue
CRT tiers (uint32: 2^32*p1*p2 ~ 2^92; uint16: 2^16*p1..p4 ~ 2^72) reach
q ~ 4e9 within the 16GiB/280s law; the natural-overflow wrap shard is free
of mod passes and doubles as an independent residue. (c) Worker-to-worker
variance ~1.7x is the dominant failure mode (5 timeouts, all recovered by
split/retry/alternate-prime); predicted-time packing should derate the
bench rate by ~1.6x in future rounds. (d) Strategy-C direction sharding
makes L=2 near-gate rows (q to 61441) cheap (8 chunks x ~40-90s).

## c1r3b-C8 — #137 discipline
Census completeness verified mechanically (153/153 tier rows matched against
the family list); every CRT row cross-checked against exact uint64 A where
both exist; every strategy-C assembly passed the exact-divisibility assert;
every DP shard printed its mass invariant; all 52 env>=1 rows have full
ledgers (no survival read rests on an absent ledger); controls preceded
verdict reads. Deferred set enumerated row-by-row (16 oct-30 tail + 189
oct-31 + 4 memory-wall rows).
