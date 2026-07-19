# C2'' F-ROUND 2 — RESULTS (exact tables + Modal provenance)

Worker: fresh-context falsification worker, F-round 2, 2026-07-13. Repo
READ-ONLY (no writes inside /prize or /prize-codex-...). Pre-registration
`c2r2_falsifiers.md` fixed BEFORE any falsifier computation.

## Modal provenance

- App (real run): `rs-mca-dli-c2r2` — `ap-09mdHKo86TqQrV3NmKWNVz`
  (https://modal.com/apps/allengrahamhart/main/ap-09mdHKo86TqQrV3NmKWNVz)
- App (dry-run plan): `ap-74mNUk81TYBQmq1UNvKmz3`
- Script: `c2r2_census_modal.py` (self-contained; kernels COPIED VERBATIM from
  M1 `m1_dli_m1_tower_census_modal.py`). Run via
  `tools/ramguard modal -- ~/.venvs/modal/bin/modal run c2r2_census_modal.py`.
- Shard plan (all shards << 280 s): 1 full-grid worker (t=3 q=193, 1.90 GB) +
  172 direction chunks (~87–90 s each) + 3 marginal workers + shard-0 gate.
- SHARD-0 GATE = PASS (banked 8-row n=32 replay + strategy-B == strategy-C at
  n=64 t=2 q=193). This is the positive control on Modal.

## Positive controls (both PASS)

- LOCAL (`c2r2_local.py`, ramguard tiny): M1 kernels reproduce all 8 banked
  n=32 f2b ratios (BANKED_F2B_RATIOS) AND the 8 pose bulk values
  {0.998,1.010,0,0,1.033,1.066,0.760,0}; BULK GM over positive rows =
  0.966561 → 0.967 (banked). Kernel copy validated at n=64 t=2 q=193
  (strategy B==C exact; ratio/bulk match M1 banked).
- MODAL: t=3 q=193 recomputed on Modal reproduces M1 banked ratio/bulk exactly
  (1.000000 / 1.000000) — validates the t=3 (g=1 projective) kernel path.

## Mutation controls (all required-to-trip; PASS)

| control | injected | result |
|---|---|---|
| MUT-i  F-b on stripped (not bulk) | use `stripped_mean_ratio` | 2.8742³³ = 2^50.26 > 2^21 → **FIRES** (accident-pricing is load-bearing) |
| MUT-ii F-a synthetic super-polylog | bulk = q^0.5 | **FIRES** (proxy detects genuine growth) |
| MUT-iii F-c forced violation | all 34 cells accident (E≈4.0) | Poisson-binomial p = 2.2e-31 < 1e-3 → **TRIPS** |

## New n=64 rows computed this round (Modal)

| t | q | octave | raw ratio | stripped_mass | BULK | accidents |
|---|---|---|---|---|---|---|
| 2 | 11777 | 13 | 1.0000 | 1.0000 | 1.0000 | none |
| 2 | 17729 | 14 | 1.0007 | 1.0007 | 1.0007 | none |
| 3 | 193 (PC) | 7 | 1.0000 | 1.0000 | 1.0000 | none |
| 3 | 641 | 9 | 1.0000 | 1.0000 | 1.0000 | none |

Combined set for the verdict reads: 8 n=32 calibration rows + 45 M1 banked
n=64 rows + 3 new unique n=64 rows = 48 unique n=64 rows.

## F-a READ (octave-slope proxy over the WIDENED grid)

Depths tested: t=2 (octaves **7–14**, wider than M1's 7–13), t=3 (octaves 7–9).
Bulk ratio ≈ 1.000 at every scale; the new octave-14 point q=17729 gives
bulk = 1.0007, s₁₄ = 0.06901, continuing the strictly DECREASING slope
sequence s_j (j=7..14: 0.1333, 0.1176, 0.1053, 0.0952, 0.0870, 0.0800,
0.0741, 0.0690).

- depth t=2: does not fire (8 octaves; s strictly decreasing).
- depth t=3: does not fire (3 octaves; s decreasing).
- **F-a KILL LINE: fires at 0 depths (requires ≥ 2) → F-a NOT fired.**

## F-b READ (packet transport x³³ vs 2²¹, exact Fraction)

- worst BULK ratio (clause ii, over ALL 56 rows) = **1.066159** at n=32
  (t=3, q=193); at n=64 the worst is only 1.0019 (M1 q=7937) / 1.0007 (new
  q=17729). Stacked: 1.066159³³ = **2^3.0499** (exact: bulk³³ ≤ 2^21).
- worst ABSOLUTE accident charge (clause iii, counted once) = 2^0.0009
  (n=32 t=2 q=8353, mass 320, frac 5.97e-4).
- TOTAL worst replayable-tower charge = **2^3.0508** → **reserve usage =
  14.53 % of the 21-bit reserve** (≈ 18 bits / 85 % margin remaining).
- **F-b NOT fired (reserve intact).**
- [NOT-falsifier, reported not scored] stripped-stacked tower 2.8742³³ =
  2^50.26 (n=32 t=4 q=97) — the per-junction-uniform proxy the pose already
  refutes; excluded per pre-registration.

## F-c READ (Poisson window law, extended census)

- Fixed shape (n=64, t=2); **34 census rows** (M1's 32 + new q=11777, 17729),
  all k=3 rare-window cells with λ₃ = 620/q ≤ 0.44; new octave-14 cell λ₃=0.0350.
- PRIMARY exceedance frequency: **X = 0** accidents vs E = 4.042; exact
  Poisson-binomial two-sided **p = 2.365e-2**.
- SECONDARY orbit quanta: **T = 0** vs Poisson(λ=4.438); exact **p = 2.365e-2**.
- theta spot-check {2,3,4}: **0 accident cells at every theta** (window is
  ≤ mean-field; theta-insensitive).
- **F-c KILL LINE: p < 1e-3 on either test → F-c NOT fired.**

## SUMMARY

| falsifier | fired? | scope run | worst statistic |
|---|---|---|---|
| F-a | NO | t=2 oct 7–14, t=3 oct 7–9 (2 depths) | bulk ≤ 1.0007 (n64), s_j decreasing |
| F-b | NO | 56 rows (n32 + n64), packet x³³ | reserve usage 14.53 % |
| F-c | NO | 34-row census, θ∈{2,3,4} | X=0, p=0.0237 |

DEFERRED (compute-bound, named): F-a 3rd depth t=4 (~194 dir-chunks) and t=3
octave-10 q=1153 (~385 chunks); F-c 40+ row census (each new row q>10369 =
30+ chunks). None can fire "for free"; deferred, not cleared beyond 34 rows.
