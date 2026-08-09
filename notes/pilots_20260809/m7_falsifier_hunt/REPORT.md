# REPORT.md — m7_falsifier_hunt (round 26) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task a65e35334108d236e, 2026-08-09. Pilot: Opus. No edits.

All computation complete. Final report follows.

---

# REPORT — m7_falsifier_hunt (round 26), Opus pilot

## VERDICT (first, before anything else)

**THE REGISTERED FALSIFIER FIRED — literally, at an admissible LIVE cell, and the firing transfers to 156 of the 408 real `k = 2^40` residual rows by exact arithmetic.** Round 25's *conclusion* (the complement re-pose is not a mystery-7 route) survives, but its *stated mechanism* is FALSE for the large-source red and must be corrected.

- **Firing cell C8** = `rate 1/2, M=5, t=3, ell=2, b=u=1, d=5, h=6, e=5, r_J=4, N=9, n=20, q=23` — passes every one of the node's own conditions A1–A11, is LIVE (`J_plain = 25-9·4 = -11 &lt;= 0`), and CJ3 does **not** pay it. Over 256 exact configs: `FIRE_UNION` (|U| &lt; 2d) in **100%** of configs with `m&gt;=2`; `FIRE_KCORE` (kappa&gt;=1) in **44.3%** of configs with `m&gt;=3` (vs round-25's **0/63**); the decisive **`FIRE_SIGMA` (sigma &lt; 2a) in 67.2% (135/201)**. Mean margin `sigma/2a = 0.930` (round-25's cells: 1.24–5.07). Witness: `m=5`, `kappa=0`, `|U|=9`, `sigma=9`, `a=5`, `a'=4`, `OVL_MAX=3`, `delta=2` → **`AC_DIRECT = 25`, `AC_COMP = 21`, measured truth `&lt;= 9`** (trivial ceiling `C(9,5)=126`). `SUBFIRE_MAX = 5` (the whole family is on the winning side).
- **The mechanism is exact arithmetic, not structure**: every defect set is a `d`-subset of the core, so `|U| &lt;= N`; hence **`N + kappa &lt; 2d ⟹ sigma &lt; 2a`**. C8 has `2d - N = +1`. Its matched control **C9** (identical `(t,ell,b,u,d)`, only `M=8` so `N=15`, `2d-N=-5`) fires **0/64** — `FIRE_SIGMA=0`, `FIRE_KCORE=0`, `FIRE_UNION=0`, `KCORE_max=0`. The falsifier switches on and off exactly at `2d = N`.
- **Round 25's kill rationale is refuted for this red.** It said "every mystery-7 cell of ours sits on the wrong side by construction… `sigma/a -&gt; 2.5`". That is proved only for the rate-half `m4_t2` cells (`|C| = 5ell-5`, `d = 2ell-3`). The large-source family allows `d` up to `ell(M-2)-1 ≈ N(1-2/M)`, so `2·dcap &gt; N` for **every** `M &gt;= 5`: **all 408 residual rows** have `2d &gt; N` somewhere in their residual window, and **156 of 408** have `2d &gt; N` inside the node's own CJ-admissible window (all 156 LIVE, `d/N` up to 0.9375, margin `2d-N` up to 9.6e11).
- **BUT the firing is NOT load-bearing, so the route stays dead — for a different reason.** Priced at all 156 rows: `log2 AC_DIRECT` mean **7.73e11 bits**, `log2 AC_COMP` mean **7.32e11 bits**, mean gain **4.11e10 bits** (max 2.84e11) — against a polynomial target of **123–129 bits**. `COMP_is_polynomial` is **false at every one of the 156**. The complement orientation genuinely wins the threshold and is genuinely useless: the annulus ground set is the whole core (`sigma = Theta(N)`) and `delta` is tiny.

**Net: the kill is HARDENED as a conclusion and CORRECTED as a mechanism. It is no longer "every cell is on the wrong side"; it is "the cells on the right side are still 10^11 bits short."**

## Deliverables

### D1 — THE CHART FAMILY (`d1_cells.py`, `d1_cells.txt`)

All 13 hand-registered cells pass A1–A11; **0 failures**. The registered codimension identity `u + t·ell - d - 1 = ell-1` (so `dim V = d-ell+2 = e+1-u`, the round-24 slice-dimension theorem being the `u=0` case) holds at every cell and was re-verified in **28/28** enumeration runs. Independent broad scan (rates × `ell` 2..7 × `b` × `M` × `t` × `u`, `CHARTDIM&lt;=4`, `mu&gt;=0.5`, cost `&lt;=3e7`): **1470 accessible admissible cells**, of which **4** have CJ3 firing, `max e = 7`, `max r_J/d = 6/7` — my registered ladder already contains the extremal root-sharing shapes. Final grid: **25 distinct cells, 28 runs, 8336 exact configs**, spanning rates 1/2, 1/4, 1/8, 1/16, `M = 5..120`, `t ∈ {2,3}`, `ell ∈ {2,3,4}`, `u ∈ {1,2,3}`, `q ∈ {17..257}`, all exact (no sampling anywhere).

**Honest scope limit, registered in advance:** A4 (`max(0,2d+1-t·ell) -&gt; infinity`) is asymptotic; no finite cell satisfies it. Every accessible cell has `e ∈ {3,5,7}`. The hit is a hit **at finite `e`** — which is why the real-row transfer computation (below) is the load-bearing part, not the toy cell.

### D2 — THE MEASUREMENT (`d2_hunt.py`, `out_*.json`, `d5_aggregate.py`)

The generalized chart (`build_flat_general`) is `rh_m4t2_census.build_flat` with `background block -&gt; canonical pick R (|R|=u)`, `2 -&gt; t` touched petals, `4 -&gt; M`. Full contributor filters exactly as banked: primitivity `gcd(F,W)=1` + untouched-petal nonagreement over all `M-t` untouched petals.

**A new exact law, verified at 28/28 runs with 0 violations and ATTAINED at every cell with `m&gt;=2`:**

```
guarded overlap max  =  r_J - |R_1 cap R_2|  &lt;=  r_J - max(0, 2u-b),
and at u = b (R = B forced)   =  d - ell   exactly.
```

This is the node's own `(CJ2)` (`h+|I|+|R|&lt;=2d`) read as a bound on `|I|` instead of summed — **not new mathematics**, but nobody had drawn it. It is strictly better than `(JB3)`'s `r_J` whenever `b&gt;0`. Consequence: **the pencil stratum is deleted**. Split-only members reach `r_J = d-1` in quantity (C4: 49.0% of pairs; K4: 52.2%; C1: 25.4%; C8: 19.3%; F1: 15.1%; C9: 1.55%); **guarded contributors reach it 0 times out of 8336 configs**, and `PENCIL_MAX = 1` in every config of every cell. Round 25's config-18 sunflower phenomenon is therefore systematic at `M &gt;= 5` and **explained**, not just observed.

Guard survival `NSPLIT_G/NSPLIT_S` = 0.378–0.815, matching the registered heuristic `(1-1/q)^{ell(M-t)+d}` within ±0.03 at every cell checked (C1 0.654 vs 0.67; C3 0.625 vs 0.628; C12 0.406 vs 0.423; C13 0.378 vs 0.394; C8 0.660 vs 0.671).

### D3 — THE VERDICT AND THE MARGINS

Per-cell (`m&gt;=3` configs; `MARGIN = mean sigma/2a`; `cap` = the sharp cap above):

| cell | rate | M/t/ell/b/u | d | r_J | 2d−N | cfg | m≥3 | OVL_MAX_G | cap | FIRE_K | FIRE_U | **FIRE_S** | **σ/2a** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **C8** | 1/2 | 5/3/2/1/1 | 5 | 4 | **+1** | 256 | 201 | 3 | 3 | .443 | 1.00 | **.672** | **0.930** |
| **F1** | 1/4 | 15/3/2/1/1 | 5 | 4 | **+1** | 64 | 16 | 3 | 3 | .875 | 1.00 | **.250** | **1.006** |
| **K4** | 1/4 | 12/3/2/1/1 | 5 | 4 | **+3** | 256 | 0 | 3 | 3 | — | 1.00 | — | — |
| **F2** | 1/8 | 35/3/2/1/1 | 5 | 4 | **+1** | 32 | 0 | 3 | 3 | — | 1.00 | — | — |
| C9 | 1/2 | 8/3/2/1/1 | 5 | 4 | −5 | 64 | 64 | 3 | 3 | 0 | 0 | **0** | 1.50 |
| C1 | 1/2 | 5/2/2/1/1 | 3 | 2 | −3 | 256 | 108 | 1 | 1 | .074 | .290 | **0** | 1.282 |
| C2 | 1/2 | 8/2/2/1/1 | 3 | 2 | −9 | 256 | 255 | 1 | 1 | .004 | .004 | **0** | 2.166 |
| C3 | 1/2 | 16/2/2/1/1 | 3 | 2 | −25 | 256 | 256 | 1 | 1 | 0 | 0 | **0** | 5.072 |
| C4 | 1/2 | 5/2/3/2/2 | 5 | 4 | −5 | 64 | 14 | 2 | 2 | .286 | .548 | **0** | 1.248 |
| C5 | 1/2 | 8/2/3/2/2 | 5 | 4 | −14 | 64 | 64 | 2 | 2 | 0 | 0 | **0** | 2.058 |
| C7 | 1/2 | 6/2/4/3/3 | 7 | 6 | −11 | 8 | 3 | 3 | 3 | 0 | .333 | **0** | 1.262 |
| C10–C13, K1–K3, C1b, C2b, T1, T2, T3 | 1/2–1/16 | — | 3–7 | 2–6 | −1..−25 | 1928 | 665 | =cap | — | 0–.10 | .00–.91 | **0** | 1.00–1.97 |

**Every `FIRE_SIGMA` firing (146 in total) is at a cell with `2d &gt; N`; every cell with `2d &lt;= N` fires zero times.** Margins at the hardened cells: `sigma/2a` from **1.00** (K3, the two-member boundary) to **5.07** (C3).

**Power control (R3, the 23b standard).** The matched random-flat arm at identical `(q,d,N,pool,dimension)` fires *more* than the guarded arm at C8 (0.790 vs 0.672) and F1 (0.512 vs 0.250), and reaches `OVL_MAX = r_J = 4` where the guarded arm is capped at 3. So the firing is **not** guard-structure — it is forced arithmetic that the guards partially *suppress*.

**The `b -&gt; ell` trend (T1→T2→T3, fixed `rate 1/2, M=8, ell=4, b=3, q=71, N=33`, `u = 1,2,3`):**

| | u | d | r_J/d | sharp cap | m mean | OVL_MAX_G | OVL_MEAN_G | **OVL_MEAN/d** | **FIRE_KCORE** | KCORE_max |
|---|---|---|---|---|---|---|---|---|---|---|
| T1 | 1 | 5 | 0.400 | 2 | 1.11 | 2 | 0.679 | **0.136** | **0.0435** | 2 |
| T2 | 2 | 6 | 0.667 | 3 | 6.23 | 3 | 1.075 | **0.179** | **0** | 2 |
| T3 | 3 | 7 | 0.857 | 3 | 7.25 | 3 | 1.305 | **0.186** | **0** | 0 |

**Answer to D3's trend question: `b -&gt; ell` raises the mean overlap monotonically (0.136 → 0.179 → 0.186) but DRIVES kappa DOWN (0.0435 → 0 → 0).** The round-25 intuition is refuted: raising `u` also raises the family size (1.11 → 7.25), and a larger family has a smaller common core. And `OVL_MAX` tracks the *sharp* cap (2,3,3), never `r_J` (2,4,6).

### D4 — RED 3 MEMBERSHIP: NOT DECIDED, AND PRICED (`d6_maxmean.py`)

**Honest refusal, as the brief instructs rather than an uncontrolled sample.** The `t &gt;= 4` flats are **not exactly enumerable under the 1G/5min wall**: `CHARTDIM = (t-2)ell + u + 1 &gt;= 6`, minimised at the cheapest admissible `t=4` cell (`rate 1/2, M=6, t=4, ell=2, b=u=1, d=7, N=11, n=24, q=29`), costing `q^5·|pool| = 2.24e8` pool-evaluations ≈ **17 min per config**, i.e. ≈ **2.3 h for a 2-power grid of 8**. That is the cheapest reachable price; I did not spend it and I did not substitute a sample.

**And the test's own functional has no power at the accessible scale.** Max-to-mean at matched dimension, guarded vs matched-random: `dim V = 3`: **3.96 vs 4.43**; `dim V = 4`: **2.38 vs 2.41**; `dim V = 5`: **2.76 vs 2.95**. The guarded flats are statistically indistinguishable from random flats of the same dimension on the discriminating functional — a **power-control failure**, exactly the failure mode round 23b caught in the `(MF)` shape-pun test. So the 23b repaired test cannot decide membership here even at `t &lt;= 3`. **Red 3's mystery-7 membership stays UNDECIDED**; I recommend it is not flipped on this evidence.

### BONUS (unbudgeted, the largest number in this pilot) — `d4_bo_sieve.py`

Deriving the falsifier mechanism forced a hard-law-5 grep, which returned **`background/nodes/l1_background_overlap_singleton_payment` (PROVED)**. Its clause `(BO2)` (`a+s &lt; ell+g` with `a=N-d`, `s=h-d`) is *exactly* my re-derived singleton criterion; my derivation via `(CJ2)` is a **re-derivation of PROVED repo content**, reported as such. The live question is bookkeeping: **has the list threshold that `(BO2)` uses ever been charged against the 408 residual `d`-windows?** It has not — `fpc5_exact.p7_large_source_sieve` caps `d` at `min(ell(M-2)-1, N)` only. Charging the node's own list threshold (`h + |R_j| &gt;= d + ell`, `R_j subset B` ⟹ `u = d-(t-1)ell &gt; b` means **no compatible codeword exists**):

| | d-values | fraction of residual d-mass |
|---|---|---|
| residual total (408 rows) | 201,710,563,424,605 | 1.0000 |
| **EMPTY by the node's own list threshold** | **143,981,892,664,856** | **0.71380442** |
| SINGLETON by the PROVED (BO2) | 1,370,388,278,010 | 0.00679383 |
| *(round-25 CJ3 baseline, recomputed here)* | *3,972,788,690,368* | *0.01969549* ✓ byte-matches |
| **left after EMPTY + SINGLETON** | 56,358,282,481,739 | **0.27940174** |

**35 of 408 rows are entirely empty; 39 are entirely paid.** Per rate: 1/2 → 68.9% empty, 0% singleton; 1/4 → 79.4% / 1.56%; 1/8 → 76.1% / 11.6% (rate 1/16 has **no** residual rows at all, which is *why* round-25's CJ rescue "gets nothing" there). The hardest rows (0% paid) are `rate 1/2, M=5, t=3` and `t=4` at `ell_min` where `b = ell-1`.

**Caveat, stated with the number:** this is on the *same denominator* as round-25's 1.97% (sum of window widths over rows), which is a **3-point sample of each `ell`-window** (`ell_min/ell_mid/ell_max`), not a measure over the full `(ell,d)` grid; and it counts `(row,d)` cells, not distinct `d` (a `d` killed at small `t` may live at larger `t`). Both figures are indicative on the same footing. I also did **not** disentangle the CJ3 band from the singleton band (they can overlap); EMPTY and SINGLETON are disjoint by construction and additive.

**Closing the loop:** of the 156 falsifier-firing rows, **17 are already singletons by the PROVED (BO2)** — the rows where the complement orientation wins most decisively are largely rows that are already trivially paid. The other **139** are genuinely open and genuinely 10^11 bits short.

## Escape tests (run before the main work — all passed)

1. `d4_cj3_audit.py` replay: **BYTE-IDENTICAL** to the banked `d4_cj3_audit.txt` (71 rows, 3,972,788,690,368 d-values, fraction 0.01969549, ledger 0/1/0/82/0/0/0).
2. `d2_arm_a.py 4 97 32 20260809 … full`: `configs_used=32`, `FRAC0=0.71574`, `KCORE 0/32`, `PENCIL_MAX_hist {"1":32}`, `MAXPACK_hist {"4":30,"3":2}` — exactly as registered.
3. `d0_compat.py` (mine): the generalized code in compat mode (`M=4,t=2,u=b=ell-3`, arm-A pool and sampling order) reproduces arm A **config by config** — NSPLIT, full overlap histograms, and chart-points-swept all identical, 32/32, `first_mismatch: null`.

## Predictions vs outcomes — MISSES FIRST

| # | registered | outcome |
|---|---|---|
| **P7** | `OVL_MAX = r_J` attained at ≥3 cells | **REFUTED.** Guarded `OVL_MAX = r_J` at **0** cells except T1 (where the sharp cap coincides). I registered the wrong cap; the correct one is `r_J - max(0,2u-b)`, discovered by the miss |
| **P5** | guarded fire-rate ≤ 3× random ⟹ "small-numbers artefact" | **SPLIT — and my gloss was wrong.** Inequality CONFIRMED (guarded *below* random), but the parenthetical is REFUTED: the firing is forced arithmetic, not an artefact |
| **P3** | `P[kappa≥1 | m≥3] ∈ [0.05,0.60]` at `u=b=ell-1` cells | **PARTIALLY REFUTED.** In-window at C1 (.074), C4 (.286); out at C2 (.004), C3 (0), C5 (0), C7 (0). The window ignored the `m`-dependence |
| **P6/P12a** | `b→ell` raises both `OVL_MEAN/d` and kappa | **SPLIT.** `OVL_MEAN/d` monotone ✓ (.136→.179→.186); kappa **falls** ✗ (.0435→0→0) |
| **P12c** | CJ4 loose by ≥3× at K1–K4 | **MIXED 2/4.** K1 7×✓, K2 3.5×✓, K3 2.33×✗, K4 1.5×✗ |
| **P11** | red-3 membership decided by the 23b test | **NOT REACHED.** `t≥4` not enumerable under the wall (priced, 17 min/config); and the functional fails power control at `t≤3` |
| **P19** | a (SING)-firing cell shows `m≤1` in every config | **CONSISTENT BUT LOW POWER.** S1: 0/4096 configs with `m≥2` — but mean guarded family 0.011, so the test barely has resolution. Every accessible (SING)-firing cell has `mu ≤ 0.06` |
| **P18** | (SING) mass not covered by CJ3 | **NOT COMPUTED.** I did not disentangle the two bands; flagged |
| P1 | ≥6 of 13 cells accessible | **CONFIRMED — 13/13** |
| P2 | codim `= ell-1`, 0 exceptions | **CONFIRMED — 28/28 runs** |
| **P4** | ≥1 cell with a `m≥3` `FIRE_SIGMA` config | **CONFIRMED — 146 firings across C8/F1** |
| P8 | guard survival ≈ `(1-1/q)^{ell(M-t)+d}` ±0.15 | **CONFIRMED — within ±0.03 at every cell checked** |
| P9/P10 | escape replays | **CONFIRMED, byte-identical / config-identical** |
| **P13** | matched control C9 does not fire | **CONFIRMED — 0/64, all three flags off** |
| **P14** | rows with `2d&gt;N` in the CJ window &gt; 0, guess ~150 | **CONFIRMED — 156** |
| **P15** | both orientations vacuous at real rows | **CONFIRMED — 0/156 polynomial; 7.3e11 bits vs a 126-bit target** |
| **P16** | (SHARP) 0 violations | **CONFIRMED — 0/28 runs, attained everywhere** |
| P17 | (SING) rows &gt; 0, none at rate 1/2 | **CONFIRMED — 0.68% of d-mass, exactly 0 at rate 1/2 as hand-derived** |

## Self-corrections, stated plainly

1. **My registered overlap cap was wrong (P7).** I registered `(JB3)/(CJ2)`'s `r_J` as the guarded cap. The measurement refuted it at the first cell; the correct cap is `r_J - |R_1 ∩ R_2|`, which is the *same node's own inequality* un-summed. I found my error by measuring, not by re-reading, which is the wrong order.
2. **My gloss on P5 was wrong.** I wrote that a firing not exceeding 3× the random arm would be "a small-numbers artefact". It is not: it is forced by `2d &gt; N`, shared with the random arm precisely *because* it is arithmetic. The inequality I registered was right; the interpretation I attached to it was not, and I report it rather than quietly re-reading the prediction.
3. **My (SING) "discovery" is a re-derivation of a PROVED node.** `l1_background_overlap_singleton_payment` `(BO2)` is the same statement. I found it by running the CATCH-24A grep *before* claiming novelty — but I had already written the derivation as if it were mine in my own working notes. Hard law 5 fires; nothing here is new mathematics.
4. **I enlarged a registered grid.** CHARTDIM-4 cells were registered at `nconfig = 8`; measured cost let me run C8/K4 at 256 and C9/F1 at 64. Both the `n8` and enlarged runs are kept and reported side by side (`out_*_n8.json`). Enlargement can only sharpen, but it was not the registered number.
5. **Two cells produced no usable signal and carry no claim.** C6 (`ell=4,b=u=3,M=5`, 8 configs) yielded mean 0.5 guarded members and never `m&gt;=2`; K4 at `nconfig=8` likewise. I report them as empty rather than folding them into aggregates.
6. **The 71.4% EMPTY figure inherits the banked sieve's sampling limitation** (3 `ell`-points per `(rate,M,t)`, and `(row,d)` cells rather than distinct `d`). It is on the identical denominator to round-25's 1.97%, so the comparison is fair, but neither is a measure over the full grid. I state this rather than headline "71%".
7. **One scratch file left the pilot directory.** `d4_replay.txt` (an escape-test diff target) and a stray empty `addf.py` went to the session scratchpad `/tmp/claude-1000/...`, which the harness sanctions for temporaries; every substantive artifact is in the pilot dir. Disclosed for completeness.
8. **P18 unresolved.** I did not compute the intersection of the (BO2) singleton band with the CJ3 band, so "EMPTY + SINGLETON + CJ3" must not be summed as 74%; only EMPTY + SINGLETON (72.06%) are additive by construction.

## What reopens, and what I recommend (draft only; no status flips, nothing adopted)

- **Correct the round-25 kill's mechanism** on `background/nodes/l1_rootfree_rational_q_projective_packing` and the falsifier line: the `sigma &lt; 2a` threshold is *not* failed by construction at the large-source red — it is *passed* at 156/408 rows (156 LIVE, `d/N` to 0.9375). The kill now rests on the *pricing* (both orientations `2^Theta(N)` against `n^3`), which is the stronger and honest reason.
- **File the sharp cap** `|D_1 ∩ D_2| &lt;= r_J - |R_1 ∩ R_2|`, `= d - ell` at `u = b`, as a corollary-of-(CJ2) note on `l1_joint_core_background_johnson_bound` / `l1_fpc5_large_source_payment`: 0 violations in 8336 exact configs, attained at every cell, and it is what deletes the pencil stratum.
- **Highest-value follow-up:** charge the node's own list threshold against the 408-row residual windows. `71.38%` of the residual `d`-mass is EMPTY (no compatible codeword) and a further `0.68%` is a singleton by a PROVED node — versus the `1.97%` round 25 banked. If a coordinator replay confirms it, this is the **third** instance of the same bookkeeping mechanism that felled claims (i) and (ii), and it is much larger than either.
- **Do not flip red 3's membership.** The 23b test fails its power control at every accessible cell, and `t &gt;= 4` costs ≈2.3 h of exact enumeration that I did not spend.

**Compliance.** Every registration (R0–R9, P1–P19, E1–E5, the frozen cell list, the `q` grid, the config grid, and all three additions) was appended to `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/m7_falsifier_hunt/PREREG.md` with the `Edit` tool **before** the corresponding computation; the two-stage registration (criteria → arithmetic scan → frozen list) is disclosed in R6. Quarantine observed: `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened at any line; no round-26 pilot directory other than my own was read; **no subagent dispatched**. Compute law: **every** interpreter invocation, including one-liners, JSON peeks and the two file patches, ran as `tools/ramguard tiny|local -- python3` from the repo root — no exceptions; `RAMGUARD_TIMEOUT` was extended to 600/900/1200/1800/2400 s for the CHARTDIM-4 and `M&gt;=35` runs, each documented at its call site. RAM discipline: file-at-a-time reads, `dag.json` never opened (node shards + `grep`/`sed` line ranges only), no bulk directory loads, `&gt;10-min` work run as detached background batches writing results files (`batch1.log`, `out_*.json`). Draft-only: all writes confined to `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/m7_falsifier_hunt/`; no `dag/`, `nodes/`, or `tools/` edits; no git; no Modal; stdlib only. Every measured functional is named (CATCH-19C); config grids are 2-powers (8/32/64/256/4096); no `u = 0` (shift-0) cell was used; the own-repo subtraction (CATCH-24A) was run **before** the only novelty claim I was tempted to make, and it fired.

**Artifacts** (all absolute, all in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/m7_falsifier_hunt/`): `PREREG.md` (brief + all registrations), `d0_compat.py`, `d1_cells.py`/`.txt`, `d2_hunt.py`, `d3_realrows.py`/`.txt`, `d3b_pricing.py`/`.txt`, `d4_bo_sieve.py`/`.txt`, `d5_aggregate.py`/`.txt`, `d6_maxmean.py`/`.txt`, `out_{C1,C1b,C2,C2b,C3,C4,C5,C6_n8,C7_n8,C8,C8_n8,C9,C9_n8,C10,C11,C12,C13,F1,F2,K1,K2,K3,K4,K4_n8,S1,T1,T2,T3}.json`, `replay_ell4_q97_full.json`, `batch1.log`.
