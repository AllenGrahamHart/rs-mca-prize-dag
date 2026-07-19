# DSP8 F-round 1 — results ledger (written as-you-go)

Round spec: dsp8r1_falsifiers.md (pre-registered BEFORE any computation).
Census: dsp8r1_census_modal.py (this directory).

## Controls (local, `tools/ramguard tiny`)

- **PC-1 (router fixture totals)** — pinned replay
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_disjoint_distance_six_split_pencil_router/verify.py`
  printed: `rows=3 targets=195 edges=18 raw_records=200`.
  dsp8r1 census control mode reproduced per-row:
  (17,8): 16/0/0; (97,16): 78/9/152; (193,16): 101/9/48;
  totals 195/18/200 -> **MATCH** (exact).
- **PC-3 (DSP3 identity)** — all 408 achieved fibers of the wave-14 audit
  toy row (32,1153): DSP3 (P = 2|S_t| - diag), DSP2 bijection + root
  checks, DSP4 disjoint<=>distance-6, antipodal two-form equality — all
  assertions PASS.
- **numpy-vs-pure cross-check**: full P-counters identical on rows
  (97,16), (193,16), (1153,32) -> MATCH.
- **MC-1 (census mutation, REQUIRED TO TRIP)**: `mutate_edges` (+1 edge,
  +8 records per row) gives totals 195/21/224 vs banked 195/18/200 ->
  **MISMATCH (TRIPPED as required)**.
- **MC-2 (kill-detector mutation, REQUIRED TO TRIP)**: rhs=-1 makes all
  three control rows report viol=True (LHS=0 > -64/-256) ->
  **TRIPPED as required**.
- PC-2 (wave-5 boundary row constants at (8192,67657729)) runs in the
  official Modal shard below.

## Modal shard ledger

(command form:
`tools/ramguard modal -- ~/.venvs/modal/bin/modal run tools/modal_run_script.py --script <scratchpad>/dsp8r1_census_modal.py --args "<mode args>"`)

| shard | args | status | key output |
|---|---|---|---|
| official | official n=8192 first=4 must=67657729 | DONE ap-3eHOuznIysRtWZkN8YyJKV | 5 rows, all J25=(0,0), LHS=0; boundary row PC-2 exact match (below) |
| n256_a | scan n=256 mstart=256 mend=9766 | DONE ap-qVW3lLQXxo0hqwPIzId8qP | 1395 rows, all vacuous, best maxP=14@p=65537 |
| n256_b | scan n=256 mstart=9766 mend=19532 | DONE ap-n0iYuUt81HIhE2EK3VLJ9C | 1282 rows, all vacuous, best maxP=10@p=2530049 |
| n256_c | scan n=256 mstart=19532 mend=29297 | DONE ap-d7lLHHEDc1PbZs2NP8tHWK | 1233 rows, all vacuous, best maxP=10@p=6032641 |
| n256_d | scan n=256 mstart=29297 mend=39063 | DONE ap-cA7n9FVegftd6z4LQmhZG1 | 1214 rows, all vacuous, best maxP=10@p=7853569 |
| control | control expect=195,18,200 | DONE ap-OQSZbyE3snvgqj1aPpp6Qi | PC-1 MATCH on Modal image; PC-3 PASS; numpy-vs-pure MATCH x3 |
| n32 | scan n=32 mstart=32 mend=52489 pmax=1679616 | DONE ap-v5r74RSODiLxxLN5ZZSh9U | ENTIRE n=32 corridor: 7937 rows, all vacuous, best maxP=10@p=1217 |
| n64_a | scan n=64 mstart=64 mend=78125 | DONE ap-8bSdaAESDEZGhSFWXpagkl | 10882 rows, all vacuous, best maxP=14@p=7937 |
| n64_b | scan n=64 mstart=78125 mend=156250 | DONE ap-OUuWUeUfm2PmeaL6K0N9Pl | 9798 rows, all vacuous, best maxP=6@p=5488961 |
| n128_a | scan n=128 mstart=128 mend=39063 | DONE ap-91WCZlQbmdECrFSoxruaRI | 5429 rows, all vacuous, best maxP=14@p=665857 |
| n128_b | scan n=128 mstart=39063 mend=78125 | DONE ap-mNJWSBEWj4tBUwl9gIbN1x | 4905 rows, all vacuous, best maxP=10@p=6700417 |
| highp64 | highp n=64 count=5 start=1e11 | DONE ap-JbX4PuzzSsDnz3xxfnbjpt | 5 rows ~1e11: all maxP=2, LHS=0 |
| highp128 | highp n=128 count=5 start=1e11 | DONE ap-BDNVUfLfOq6zRNiS0Slkil | 5 rows ~1e11: all maxP=2, LHS=0 |
| highp256 | highp n=256 count=5 start=1e11 | DONE ap-ZdczxiyulwvIWVelaJIV3Z | 5 rows ~1e11: all maxP=2, LHS=0 |
| n512 | scan n=512 mstart=512 mend=19532 | DONE ap-bVBTDSdIZ6RJVqdi47OT8n | 2512 rows, all vacuous, best maxP=18@p=319489 |
| n1024 | scan n=1024 mstart=1024 mend=9766 | PARTIAL ap-cZWIyEGN2I7TLxhXT0UPUD | 803 rows to m=6910, all vacuous, best maxP=18@p=1201153; tail deferred |
| n1024_b | scan n=1024 mstart=6911 mend=9766 | DONE ap-D4pSSlZWn46jdLlvHk8blW | 366 rows, all vacuous, best maxP=12@p=8452097 (n=1024 window now complete: 1169 rows) |
| n2048_a | scan n=2048 mstart=2048 mend=4884 | PARTIAL ap-3hu3Xwz4vke65vMYWlg9Qd | 129 rows to m=2981: TWO RICH ROWS (below); tail deferred |
| n2048_b | scan n=2048 mstart=4884 mend=7325 | VOID ap-2QMoyTP32PiJBqasiPBREa | rows=0 (pmax fence bug, catch dsp8r1-C1) |
| n2048_b2 | scan n=2048 mstart=4884 mend=7325 pmax=15000000 | PARTIAL ap-x0je6EHDDmMws08A7GAk13 | 136 rows to m=5972, all vacuous, best maxP=16; tail deferred |
| n2048_c | scan n=2048 mstart=2982 mend=4884 (v2 numpy) | DONE ap-75PvvrArcE3GavoSdWpG6n | 232 rows, all vacuous, best maxP=16@p=6629377 |
| n2048_d | scan n=2048 mstart=5973 mend=7325 pmax=15000000 (v2) | DONE ap-V6ngaD7XmzJUd6adcmkvVL | 153 rows, all vacuous, best maxP=18@p=14118913 |
| n4096_a | scan n=4096 mstart=4096 mend=4612 pmax=21000000 | PARTIAL ap-SE0zfuVP5W9rlryL2c5PQe | 34 rows to m=4410: ONE RICH ROW (below); tail deferred |
| n4096_b | scan n=4096 mstart=4612 mend=5128 pmax=21000000 | PARTIAL ap-8CvSn9VtR2Q79HdYKSbYFC | 37 rows to m=4942, all vacuous, best maxP=18@p=18997249; tail deferred |
| n4096_c | scan n=4096 mstart=4411 mend=4612 pmax=21000000 (v2) | DONE ap-2U2JbnElMK8zpn1QuANWdG | 28 rows, all vacuous, best maxP=18@p=18358273 |
| n4096_d | scan n=4096 mstart=4943 mend=5128 pmax=21000000 (v2) | DONE ap-LXTDgRpnWt70R5tK2aYK0D | 19 rows, all vacuous, best maxP=16@p=20287489 |
| xcheck1 | xcheck n=2048 p=4360193 | DONE ap-HqnrgENem8jCjkxrVK417f | pure-vs-numpy FULL MATCH (1,665,061 targets), LHS=0 |
| xcheck2 | xcheck n=2048 p=4513793 | DONE ap-hAKCknwKcEzXVJtT1EXpUl | pure-vs-numpy FULL MATCH (1,676,412 targets), LHS=0 |
| xcheck3 | xcheck n=4096 p=16801793 | DONE ap-Vd1GpiNS9Zjnj727rzNmB1 | pure-vs-numpy FULL MATCH (6,604,565 targets), LHS=0 |

## Final coverage table (all shards complete; zero deferred scope)

| scale n | analogue window (exhaustive) | rows | rows with any retained target (P>=25) | max_{t!=1} P | worst LHS/(892n^2) | worst diag ratio_19 |
|---:|---|---:|---:|---:|---|---|
| 32 | ENTIRE corridor [1024, 1679616] | 7,937 | 0 | 10 | 0 (exact) | 0 |
| 64 | [4096, 1e7] + 5 rows ~1e11 | 20,685 | 0 | 14 | 0 | 0 |
| 128 | [16384, 1e7] + 5 rows ~1e11 | 10,339 | 0 | 14 | 0 | 0 |
| 256 | [65536, 1e7] + 5 rows ~1e11 | 5,129 | 0 | 14 | 0 | 0 |
| 512 | [262144, 1e7] | 2,512 | 0 | 18 | 0 | 0 |
| 1024 | [1048576, 1e7] | 1,169 | 0 | 18 | 0 | 0 |
| 2048 | [4194304, 1.5e7] | 650 | 0 | 20 | 0 | 35600/3741319168 ~ 9.5e-6 |
| 4096 | [16777216, 2.1e7] | 118 | 0 | 20 | 0 | 36000/14965276672 ~ 2.4e-6 |
| 8192 (OFFICIAL) | first 5 official primes | 5 | 0 | 20 | 0 | 7200/59861106688 ~ 1.2e-7 |

Total: 48,544 rows measured exactly. LHS = 10J_25^0 + 17J_25^A = 0 at
EVERY row (no row had any target with t != 1 and P(t) >= 25).

## Kill-line outcomes

- KILL-1 (exact row violation): NOT FIRED. LHS = 0 <= 892n^2 at every
  measured row; there was no non-vacuous row at the pinned cutoff.
- KILL-2 (monotone trend at official aspect): NOT FIRED. rho_max(n) = 0
  at all nine scales — a flat-zero sequence; no monotone increase exists
  to extrapolate. The sub-cutoff diagnostic ratio_19 is nonzero only at
  n = 2048/4096/8192 and DECREASES with n (9.5e-6 -> 2.4e-6 -> 1.2e-7);
  the pre-named NOT-kill (b) applies to it regardless.
- Escalation rule: all four maxP >= 19 rows (three analogue + the
  official boundary row) received full exact measurement; the three
  analogue ones additionally passed the full dual-implementation xcheck
  (complete P-counter equality, then field-by-field row equality); the
  official boundary row's numpy path is cross-pinned by PC-2's banked
  wave-5 constants and per-fiber DSP3 assertions.

### Rich rows found by the scans (all SUB-cutoff: max P = 20 < 25, J_25 = 0)

| n | p | rich fibers (t, P, R, generic, N6, class) | X18 | D19 | LHS_19 diag | RHS=892n^2 |
|---|---|---|---|---|---|---|
| 2048 | 4360193 | (523205,20,3,10,45,'0'), (2148238,20,3,10,45,'0') | 12 | (270,0) | 21600 | 3741319168 |
| 2048 | 4513793 | (135336,20,5,10,45,'0'), (3511811,20,5,10,44,'0') | 20 | (445,0) | 35600 | 3741319168 |
| 4096 | 16801793 | (2181395,20,5,10,45,'0'), (2682403,20,5,10,45,'0') | 20 | (450,0) | 36000 | 14965276672 |

Every rich row shows the same TWIN structure as the official boundary row:
exactly two antipodal-free targets, P = 20, 10 generic members, N_6^disj in
{44,45} (all-or-nearly-all disjoint pairs). Banked extremizer row
(2048, 4638721) has P = 18 < 19 (below the diagnostic threshold) —
consistent with its banked (P,R) = (18,7).

Wave-3/4 rationale (adversarial escalation, within the pre-registered
family shape "primes p = 1 mod n for 2-power n"): the banked 7,090-row
sweep bounds P+2R <= 32 at 512..4096 but does NOT resolve the split; P >= 25
with R <= 3 is numerically compatible with it. These shards measure J_25
directly at those scales and re-visit the banked global extremizer row
(2048, 4638721).

### Official n=8192 rows (shard `official`, ap-3eHOuznIysRtWZkN8YyJKV)

| p | maxP (t!=1) | P(1) | rich fibers (t,P,R,generic,N6,class) | X18 | X35 | D25 | D19 | LHS | RHS=892n^2 |
|---|---|---|---|---|---|---|---|---|---|
| 67239937 | 18 | 0 | none | 0 | 0 | (0,0) | (0,0) | 0 | 59861106688 |
| 67280897 | 18 | 0 | none | 0 | 0 | (0,0) | (0,0) | 0 | 59861106688 |
| 67411969 | 18 | 6 | none | 0 | 0 | (0,0) | (0,0) | 0 | 59861106688 |
| 67452929 | 16 | 0 | none | 0 | 0 | (0,0) | (0,0) | 0 | 59861106688 |
| 67657729 | 20 | 0 | (16650852,20,1,10,45,'0'), (40697698,20,1,10,45,'0') | 4 | 0 | (0,0) | (90,0) | 0 | 59861106688 |

**PC-2 PASS (exact)**: boundary row (8192,67657729) reproduces the banked
wave-5 constants: max_t P(t)=20, exactly two rich targets, both R=1,
X18=4, X35=0. New exact structure datum: each rich fiber has 10 generic
members and N_6^disj=45=C(10,2) (all pairs disjoint), both antipodal-free;
sub-cutoff diagnostic D19=(90,0) => LHS_19 = 7200, ratio_19 =
7200/59861106688 ~ 1.2e-7. At the pinned cutoff 25 the row is vacuous:
J_25=(0,0), LHS=0.

Scale windows: n=32 covers its ENTIRE corridor [1024, 1679616]; n=64/128/256
cover [n^2, 10^7] exhaustively + 5 high-p rows each at ~1e11; n=8192 official
rows are the first four official primes + the provenance-identified richest
row 67657729 (in corridor 13<=s<=41 — official, not analogue).
