# C1'-r3 F-ROUND 1 — results (exact tables + Modal app ids)

- **predicate:** C1'-r3 (`c1r3_pose.md`): gate v_2(q-1) >= 20 (analogue of official 41),
  extended RAW ledger w in [2,8] at L=1, allowance 4, E-1 <= 4r(1+W_ext).
- **K'_r3** = (E-1)/(r(1+W_ext)); LITERAL kill K'>4; AMBER watch K'>=1; verdict path
  exact rational throughout (Fraction/bigint; floats are display).
- **scripts (scratchpad):** `c1r3_census_modal.py` (all modes), `c1r3_pose_arith.py`,
  `c1r3_trendfit.py`, `c1r3_primecheck.py`. Pre-registration: `c1r3_falsifiers.md`
  (frozen before any round computation).
- **family:** COMPLETE census of gated Proth primes q = c*2^k+1 (odd c, k>=20) below
  2^28 — 33 rows, octaves 2^22..2^27 (2^25 octave empty of such primes), v_2 range
  20..25. Enumerated locally (ramguard tiny) + independently inside `accscan`.

## Controls (ALL PASS)

- **Grounding (local ramguard tiny):** q=7937 A_total DP -> E-1 =
  15584479363607/144115188075855872, exact match to banked M2 record.
- **PC1 (r2 kill reproduction, verbatim kernel, r2 window [2,6]):** q=7937
  K'=0.246909 (W_cl=236, orbits {2:0,3:2,4:8,5:31,6:126}); q=63361 K'=6.199084
  (W_cl=76); q=65921 K'=4.481241 (W_cl=72); q=204353 K'=4.284843 (W_cl=50). All
  E-1 fractions asserted EQUAL to the c1r2 banked values. App ap-B5ctxJp7GZ2W2IppRo3QT2.
- **PC2 (gate excludes killers):** v_2(q-1) = 7 / 7 / 6 at 63361 / 65921 / 204353
  — all < 20, all OUT of r3 hypothesis (exact asserts).
- **M1 mutation (required to trip):** q=63361, gate dropped, r2 window -> K'=6.199084
  > 4 fires the r3 detector. PASS.
- **PC3 (repricing under the r3 extended ledger, gate ignored) + enumerator
  cross-validation** (app ap-dtZ5jqSJ3jOAgKerm07xKB): optimized numpy enumerator ==
  verbatim kernel at w2..6 on all three killers; w7 counts == banked window-probe
  (131/119/45):

  | q | orbits w2..8 | W_r2 | W_ext | K'(r2 win) | K'(w<=7) | K'_ext (exact) |
  |---|---|---|---|---|---|---|
  | 63361 | {0,1,3,10,36,131,510} | 76 | 269 | 6.199084 | 3.349680 | **1.767887** = 2029645184561543/1148062877614080 |
  | 65921 | {0,1,3,9,34,119,470} | 72 | 249 | 4.481241 | 2.468910 | **1.308522** = 144718745038723/110597085593600 |
  | 204353 | {0,1,3,6,18,45,128} | 50 | 209/2 | 4.284843 | 2.973156 | **2.071346** = 1498428331827445/723408102883328 |

  All three killers repriced BELOW 4 by the extended window alone (and excluded by
  the gate anyway) — both pre-registered checks hold.
- **M2 (allowance 1e-6):** fired at all 33 in-gate rows (E-1 > 0 asserted everywhere).
- **M3:** NO in-gate row has (E-1)/r > 4, so M3 degrades to M2 as pre-registered
  (recorded; the ledger is not load-bearing at any scanned gated row — the bare
  envelope already sits under the allowance).
- **DPX (two independent E paths):** q=7340033 A_total = 2518452419008 via my DP ==
  banked `signed_all_census` marginal. App ap-JiMMaSY2SNLPJT75TcwKWa.
- **DP integrity at every row:** int64 headroom guard + exact hi/lo mass invariant
  sum(dp) == 4^32 (== 4^64 mod p per CRT prime at N=64).

## GATE-MIRROR (KILL-GATE-MIRROR: NOT FIRED) — app ap-2clxO3UDzu0GQwJdipHpm1

Analogue weight-3 norm census (order 64, all 19,840 reduced signed polys, exact
3-prime CRT with modulus > 2*3^32, full factorization): **24 unique norms, 22
distinct prime divisors, MAX v_2(p-1) = 16 at p = 65537.** No divisor reaches the
gate 20 => the analogue weight-3 channel is PROVABLY EMPTY at every gated prime of
ANY size (mirror of `dli_wcl_weight3_ambient_exclusion`: official max 18 < 41).
Consistency: all three r2 killers appear among the divisors (each divides a
weight-3 norm). Only divisor with v_2 >= 10: 65537 (v_2=16, out-of-gate by 4).

**Operative scan** (`accscan`, app ap-qJWbtAPkd09X07AK7TdPYQ): ALL 401 gated Proth
primes below 2^32: weight-3, weight-4, weight-5 signed-vanisher channels EMPTY at
every one; weight-6 nonempty at exactly ONE row: q=918552577 (v_2=22, 32 signed
w6 vanishers) — beyond the DP envelope (q > 2^28), DEFERRED to round 2 (the one
known in-gate accident row below 2^32).

## FULL-SPECTRUM SLICE — all 33 in-gate rows, L=1, N=32 (exact; sorted by q)

| q | v2 | (E-1)/r | orbits w7,w8 | W_ext | K'_r3 | verdict |
|---|---|---|---|---|---|---|
| 7340033 | 20 | 1.230120 | 3, 6 | 3 | 0.307530 | survives |
| 13631489 | 20 | 0.785299 | 0, 3 | 3/4 | 0.448742 | survives |
| 23068673 | 21 | 0.380929 | 0, 0 | 0 | 0.380929 | survives |
| 26214401 | 20 | 1.035845 | 1, 1 | 3/4 | 0.591912 | survives |
| 28311553 | 20 | 0.866978 | 0, 2 | 1/2 | 0.577986 | survives |
| 69206017 | 21 | 0.741365 | 0, 0 | 0 | 0.741365 | survives |
| 70254593 | 20 | 0.942369 | 0, 1 | 1/4 | 0.753895 | survives |
| 81788929 | 21 | 1.008154 | 0, 0 | 0 | **1.008154** | **AMBER** |
| 101711873 | 20 | 0.997912 | 0, 0 | 0 | 0.997912 | survives |
| 104857601 | 22 | 0.922993 | 0, 0 | 0 | 0.922993 | survives |
| 111149057 | 21 | 0.954379 | 0, 0 | 0 | 0.954379 | survives |
| 113246209 | 22 | 0.709742 | 0, 0 | 0 | 0.709742 | survives |
| 120586241 | 20 | 0.625868 | 0, 0 | 0 | 0.625868 | survives |
| 132120577 | 21 | 0.779668 | 0, 0 | 0 | 0.779668 | survives |
| 136314881 | 21 | 0.678814 | 0, 0 | 0 | 0.678814 | survives |
| 138412033 | 22 | 0.783785 | 0, 0 | 0 | 0.783785 | survives |
| 141557761 | 20 | 0.949246 | 0, 1 | 1/4 | 0.759397 | survives |
| 147849217 | 20 | 1.222305 | 0, 1 | 1/4 | 0.977844 | survives |
| 155189249 | 22 | 0.831432 | 0, 0 | 0 | 0.831432 | survives |
| 158334977 | 20 | 0.912148 | 0, 0 | 0 | 0.912148 | survives |
| 163577857 | 22 | 0.776242 | 0, 1 | 1/4 | 0.620994 | survives |
| 167772161 | 25 | 0.883271 | 0, 0 | 0 | 0.883271 | survives |
| 169869313 | 21 | 0.989577 | 0, 0 | 0 | 0.989577 | survives |
| 185597953 | 20 | 0.745830 | 0, 0 | 0 | 0.745830 | survives |
| 186646529 | 21 | 1.122901 | 1, 0 | 1/2 | 0.748600 | survives |
| 199229441 | 21 | 0.895932 | 0, 0 | 0 | 0.895932 | survives |
| 204472321 | 20 | 0.858202 | 0, 0 | 0 | 0.858202 | survives |
| 211812353 | 21 | 0.812069 | 0, 0 | 0 | 0.812069 | survives |
| 221249537 | 20 | 0.933197 | 0, 0 | 0 | 0.933197 | survives |
| 230686721 | 22 | 0.780084 | 0, 0 | 0 | 0.780084 | survives |
| 246415361 | 20 | 1.024517 | 0, 0 | 0 | **1.024517** | **AMBER** |
| 249561089 | 21 | 0.725317 | 0, 0 | 0 | 0.725317 | survives |
| 257949697 | 21 | 0.748986 | 0, 0 | 0 | 0.748986 | survives |

(w2..6 orbit counts are 0 at every row — matching the accscan emptiness.)

- **NO LITERAL KILL:** worst K'_r3 = **1.024517293** (q=246415361), margin 3.9x
  under the allowance 4.
- **AMBER (K'>=1) FIRED at 2 rows,** exact: q=81788929 K'_r3 =
  2766759940242725/2744381056483328 > 1; q=246415361 K'_r3 =
  1058880560632659/1033540934303744 > 1. Both have EMPTY extended ledgers — the
  trips are bare-envelope fluctuations, not accident rows.
- Exact E-1/r fractions for every row are in the shard outputs (session task logs);
  each row printed its exact E-1, r, K'_r3.

## KILL-TREND evaluation (`c1r3_trendfit.py`) — NOT FIRED (literal)

Per-octave worst K'_r3: 0.30753 (2^22) -> 0.44874 (2^23) -> 0.59191 (2^24) ->
1.00815 (2^26) -> 1.02452 (2^27). Monotone increasing across all 5 populated
octaves (condition 1 HOLDS), but the log2-linear LS extrapolation crosses 4 at
log2(q) = **32.74 > 32** (condition 2 FAILS; predicted K'(2^32) = 3.34). Secondary
reads agree: first-to-last chord crosses at 33.61; last-two-octave slope has
collapsed to 0.0146 bits/octave (crossing at 2^162). Step slopes decelerate
+0.610 -> +0.424 -> +0.468 -> +0.015 bits/octave: saturation, not runaway.
AMBER-trend variant (crossing 1 before 2^32): already crossed (the two ambers) —
consistent with the MIXED verdict, adds nothing beyond KILL-AMBER.

**Structural reading (finding c1r3-C5):** under iid fibers E-1 = (q-1)*2^-N, i.e.
(E-1)/r -> 1 exactly. The gated bulk converges to this iid baseline from below;
the worst observed excess over iid is +2.45%. The saturation ceiling of the trend
is the iid line, 4x under the allowance.

## Aspect probe N=64 (survival-only; app ap-HHrZToB6btIK7dNsensitm)

q=7340033: (E-1)/r = 0.009869, partial ledger w2..6 = 6 (one w5, one w6 orbit),
K'_r3 <= 0.001410. q=13631489: (E-1)/r = 0.005780, W_partial = 8 (four w6),
K'_r3 <= 0.000642. Survival confirmed at aspect 64 with margins > 700x; the
near-balance regime (r -> 1) at N=32 is where all tension concentrates.

## Deferred / gaps (honest)

- **q=918552577** (the unique in-gate w<=6 accident row < 2^32): DP infeasible on
  the 16GiB worker (q-array 7.3GB, ~3 live arrays) — DEFERRED; round-2 priority 1.
- In-gate rows q in [2^28, 2^32): accident channels scanned (empty except above);
  exact K'_r3 unreachable this round (same memory wall).
- L=2 in-gate: EMPTY at N=32 (gate vs H2); not testable this round.
- Two pair-shards (169869313+185597953, 186646529+199229441) hit the 270s ceiling
  and were rerun as four single-row shards (shrink per compute law) — ALL FOUR
  completed; no data gap in the 33-row slice.

## Modal app ids (captured; uncaptured shards replayable via script + args)

controls ap-B5ctxJp7GZ2W2IppRo3QT2; reprice ap-dtZ5jqSJ3jOAgKerm07xKB; w3census
ap-2clxO3UDzu0GQwJdipHpm1; accscan ap-qJWbtAPkd09X07AK7TdPYQ; dpx
ap-JiMMaSY2SNLPJT75TcwKWa; aspect ap-HHrZToB6btIK7dNsensitm; rows:
ap-PkKRMiDbS3AAHf6HHhXl6p (5 small), ap-tXUuEtpVakAAHruBLvjRlB,
ap-DeA41S5LR2KolYrTqkMu0M, ap-0fKBzAYjd54aPfNuJgg0l3 (octave 26),
ap-LagbsSjBFCRJHslOjKNCN5, ap-qMO50wBfA4Z8Tkb9nqA07q, ap-MeqmpaLI9RLGj7AETJR5B7,
ap-XNwIaHyWIGvmztLdN6fvPV, ap-Zg7nf4ZpRyYn3hOMqzHych (octave 27 pairs); the
remaining single-row shards ran successfully with app ids not captured (tail
truncation) — replay via `c1r3_census_modal.py row <q>`. peak_rss 103MB-9.3GB,
all under the 16GiB worker; every shard except the two shrunk-and-rerun pairs
finished well inside the 270s ceiling. Total cost: cents-scale (~30 shards).
