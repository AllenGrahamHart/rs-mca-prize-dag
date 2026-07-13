# C1' F-ROUND 2 — results (exact tables + Modal app ids)

- **predicate:** node `dli_dyadic_k_core` (C1', r2 level-scaled pose).
- **K':** `(E-1)/(r(1+W_cl))`, RAW primitive ledger over w in [L+1,L+5], w_max=L+5.
  LITERAL kill K'>4; AMBER watch K'>=1 (see `c1r2_falsifiers.md`). Verdict path
  exact rational.
- **method:** exact `E = q^L * A_total / 4^N` (A_total = total odd-null signed
  state count, cheap DP); `K' <= (E-1)/r` bounds K' over the whole prime range,
  so W_cl is enumerated only for the finite set with `(E-1)/r >= 1`.
- **scripts (scratchpad):** `c1r2_census_modal.py` (scan+wcl), `c1r2_verify_kill.py`
  (independent banked-kernel verification), `c1r2_window_probe.py`,
  `c1r2_ground.py` (local grounding).

## Controls (PASS)

- **Grounding (local ramguard tiny, `c1r2_ground.py`):** `E = q^L*A_total/4^N`
  reproduces ALL 12 recorded M2 `E-1` values AND the M1 `V_orbits` identity,
  exactly (Fraction). q=7937 (E-1)/r = 58.5175.
- **Positive control (RAW ledger):** L=1 q=7937 -> orbits {3:2,4:8,5:31,6:126},
  W_cl=236, E-1=15584479363607/144115188075855872, **K'=0.246909432** — exact
  match to the M2 record. Raw == M2 (no dedup discrepancy).
- **Mutation control:** q=7937 with W_cl:=0 -> K'=58.5175 > 4 => KILL fires
  (ledger load-bearing; kill detector works).
- **Independent kill verification (`c1r2_verify_kill.py`, banked kernels):**
  sympy.isprime(q)=True and q%64==1 for all kills; A_total via my DP ==
  A_total via banked `signed_all_census`; W_cl via banked `primitive_orbit_count`
  == my counts; DP mass invariant sum=4^32 holds; brute-force weight-3 orbit
  count matches (w3=1 for the kills). All in-hypothesis (2^32>=q, N=32>=16).

## LITERAL KILLS — C1' REFUTED (L=1, N=32, all q=1 mod 64, in-hypothesis)

| q       | (E-1)/r | W_cl | orbits {2,3,4,5,6} | K' (exact float) | exact E-1 |
|---------|---------|------|--------------------|------------------|-----------|
| 63361   | 477.329 | 76   | {0,1,3,10,36}      | **6.199084**     | 2029645184561543/288230376151711744 |
| 65921   | 327.131 | 72   | {0,1,3,9,34}       | **4.481241**     | 723593725193615/144115188075855872 |
| 204353  | 218.527 | 50   | {0,1,3,6,18}       | **4.284843**     | 1498428331827445/144115188075855872 |

- r = q/2^32 for each. **Worst K' = 6.199084 at q=63361** (exceeds the 4-allowance
  by factor 1.55).
- q=204353 is the node's OWN "natural cluster row (k=7)" that motivated the r2
  re-pose; the r2 pose fails there too.
- These are the ONLY literal kills in the L=1 scan to 262144: every row with
  (E-1)/r > 6.199 was enumerated and none beats 63361 (K' <= (E-1)/r).

## AMBER rows (1 <= K' <= 4), L=1 scan to 262144 — 12 rows

| q      | (E-1)/r | W_cl | K'       |
|--------|---------|------|----------|
| 128833 | 28.297  | 12   | 2.176673 |
| 200257 | 20.609  | 9    | 2.060881 |
| 177409 | 21.927  | 10   | 1.993359 |
| 109121 | 31.235  | 17   | 1.735283 |
| 173249 | 27.649  | 15   | 1.728088 |
| 48449  | 151.869 | 92   | 1.633004 |
| 136769 | 24.423  | 14   | 1.628171 |
| 32833  | 94.485  | 59   | 1.574758 |
| 131009 | 27.343  | 18   | 1.439095 |
| 95233  | 32.132  | 24   | 1.285267 |
| 149249 | 17.100  | 14   | 1.139982 |
| 138113 | 22.470  | 19   | 1.123504 |

Smallest-q amber: q=32833 (K'=1.575). Smallest-q literal kill: q=63361.
Reference: q=7937 (the M2 near-worst) K'=0.2469 is dwarfed once the scan passes
the M2 cap q<=12289. First amber ~q=32833; first kill q=63361.

## Window-robustness (`c1r2_window_probe.py`) — kill is NOT a window artifact

Extending the ledger window to the old absolute `w<=7` (the form the pose
explicitly rejected) only demotes kills to high amber:

| q      | K' window[2..6] (POSE) | K' window[2..7] | w7 orbits |
|--------|------------------------|-----------------|-----------|
| 63361  | 6.1991 (KILL)          | 3.3497 (amber)  | 131       |
| 65921  | 4.4812 (KILL)          | 2.4689 (amber)  | 119       |
| 204353 | 4.2848 (KILL)          | 2.9732 (amber)  | 45        |

Even at w<=7, q=63361 sits within 16% of the 4-bound; since the accident
envelope grows with q, w<=7 would also fail at larger q.

## L=2 (second level) — corroborating envelope growth

Scan to q=4001 (in-hypothesis q<=65536; grid q^2). Max (E-1)/r = 1.3227 at
q=3137; W_cl there = 1 (orbits {7:2}), **K'=0.661372** (survives amber). vs the
M2 L=2 max K'=0.034 at q=577. The envelope grows with q at L=2 exactly as at
L=1. Deeper L=2 (q>4001) kill search **DEFERRED** — the (q,q) grid DP timed out
at the 270s Modal ceiling (per compute law: shrink/defer, never rescue locally).

## Modal app ids (captured)

- wcl batch 1 (39 candidates incl. controls): `ap-sH5jggJ2MaJVStnd0LqkeU`
- independent kill verification (final): `ap-FiU7teEc9h8VArvUb8pBI0`
  (first attempt `ap-SidB09w95pBjUSgf62WZRJ` failed only on an int64 sum in the
  invariant check — fixed with object-dtype sum, DP itself was correct)
- L=2 scan (to 4001): `ap-nm0DGReNZNfHIfAaQkgUMv`
- window probe (w7): `ap-eiLmm2b46Zouome9UFKQZu`
- wide L=1 scan (to 262144), wcl batch 2, L=2 wcl, extended L=2 scan (timeout):
  ran successfully (except the timeout); app ids not captured — replay via the
  scripts + args recorded above. peak_rss 74-429MB, all well under 16GiB.
