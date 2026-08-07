# PRE-REGISTRATION — L1-N10-ELL: the decisive ell-sweep (round 22)

Round 22, 2026-08-07. Coordinator brief; the pilot appends its own
registrations BEFORE any computation. MANDATE: execute the compute
request of record L1-N10-ELL at reachable local scale and attempt to
fire falsifier F-w1. This is mystery 6's first post-re-pose test.

## 0. Sources (quote verbatim first)
- critical/nodes/l1_mixed_petal_amplification/statement.md — the
  Round-21 diagnosis addendum (the re-pose L1-MPA-w, falsifiers
  F-w1/F-w2, the BOX law Lambda = 2*ell+b-2).
- notes/pilots_20260807/l1_pma_diag/ — REPOSE_DRAFT.md,
  d3_ell_sweep.py, a5_scale32.py, a3_exhaustive_exact.py: REUSE this
  machinery (it is coordinator-replayed); do not rewrite from
  scratch what already verifies.
- experiments/prize_resolution/l1_balanced_mixed_growth_census_result.md
  — the banked N10 numbers and schedules.

## 1. Deliverables
- (D1) THE SWEEP: exact retained counts at n=32, ell=2,3 (both
  scalar schedules + the minimal-degree word), and n=24 extended to
  ell=5,6. Attempt n=32 ell=4 ONLY if it fits ramguard local
  (1G/5min per invocation; you may checkpoint across invocations via
  files in YOUR OWN dir). If a cell does not fit, report its exact
  cost (candidates, memory, time estimate) and SKIP it — spec it as
  a Modal request line for the coordinator instead. You may NOT
  launch Modal jobs.
- (D2) THE F-w1 TEST at every completed cell: does any word exceed
  10*BOX(ell)/q? Include adversarial words per cell (minimal-degree
  word mandatory; a filter-guided + random search like a5's; note
  the round-21 finding that the exhaustive max at n=16 was NOT
  filter-extremal, so do not trust the filter to find the max —
  say what your search can and cannot conclude).
- (D3) THE LAW IN ELL: does retained ~ sum_m N_{k+m}(ell) q^{-m}
  (the random-word law) continue to hold as ell grows, or does a
  mixed-petal amplification signal emerge? Derive N_{k+m}(ell)
  closed-form first (extend the round-21 derivation), predict, then
  measure. Prediction before measurement, per cell.
- (D4) THE CLAUSE-(b) SHAPE: the trend of retained/(BOX/q) in ell
  at fixed n — flat, growing, or shrinking? What does the trend
  predict for the ell = Omega(n/log n) regime, stated as an honest
  extrapolation with its epistemic label?

## 2. Falsifiers / honesty
- If F-w1 FIRES (a word with retained > 10*BOX(ell)/q): the
  re-pose must be re-drafted around the witness; report the witness
  with a reproduction script and STOP the positive line. That is a
  successful outcome.
- If F-w2 fires (any contributor at sigma > 2*ell+b-2): clause (a)
  is killed — report immediately, highest priority.
- Census evidence is evidence, never proof; label throughout.
  Search maxima are lower bounds on true maxima — label them.

## 3. Rules
- DRAFT ONLY in notes/pilots_20260807/l1_ell_sweep/. Never edit
  dag.json/nodes/tools; no git; no Modal. COMPUTE LAW: every python3
  invocation via tools/ramguard tiny|local -- python3 ... (literal
  --), from repo root, INCLUDING file patching and JSON peeking.
  2-power grids where a grid is yours to choose (n=24 cells are
  allowed here: they extend the banked round-21 baseline, which is
  the comparison of record). Name every measured functional
  (CATCH-19C). Verbatim quotes with file:line. No REPORT.md — your
  final message IS the report. QUARANTINE: do not read
  notes/pilots_20260802/CAMPAIGN_LEDGER.md at or past line 2487
  (the "ROUND 22 LAUNCHED" marker); do not read the other round-22
  pilot dirs (ge_floor_falsifier, bb_nu_transport, f2_rlocality);
  PASS THIS QUARANTINE CLAUSE VERBATIM to any subagent you dispatch.


# PILOT REGISTRATIONS

Appended 2026-08-07T06:48:10Z (repo HEAD `5ac7a5a52`), BEFORE any
computation in this pilot. Nothing below this line was informed by a
measurement made in this session; only by the four sources quoted in
section 0 of the brief and by the round-21 artifacts they name.

## R0. Object, chart family, and search-space declarations

### R0.1 The object (restated so the enumeration is unambiguous)

Domain `D = mu_n` (the n-th roots of unity in `F_q^*`, so `n | q-1`),
rate 1/2 (`n = 2k`). Maximal-source chart, exactly as
`notes/pilots_20260807/l1_pma_diag/d2_danger_map.py:6-10`:

```text
core C with |C| = k-1, petals T_1..T_t of size ell, background B, |B| = b,
t = floor((n-k+1)/ell),  b = (n-k+1) - t*ell,  so  t*ell + b = k+1.
Received word: U = 0 on C u B,  U = c_i * L_C  on T_i,  c in (F_q^*)^t.
```

A *candidate support* is `S = K u B' u (P \ O)` with `K ⊆ C` (`a=|K|`),
`B' ⊆ B` (`nb=|B'|`), `O ⊆ P` (`om=|O|`), `P = union of petals`. It is a
*mixed floor-band candidate* iff all three of
(i) floor band `|C \ S| >= ell(t-2)`, i.e. `a <= Lambda := 2*ell+b-2`;
(ii) contributor `|S| >= k+1`, i.e. `om <= a+nb-b`;
(iii) mixed: some petal `T_i` has `0 < |T_i \ O| < ell`.
It is *retained* iff there is a `P` with `deg P < k` whose **complete**
agreement set with `U` is exactly `S`.

Write `|S| = k+r`, so `r = a+nb-b-om+1 >= 1`.

### R0.2 Named measured functionals (CATCH-19C)

- `BOX(n,ell,layout)` — number of mixed floor-band candidate supports.
- `N_{k+r}(n,ell,layout)` — the shell-resolved refinement, `|S| = k+r`.
  `BOX = sum_{r>=1} N_{k+r}`.
- `RET(n,ell,layout,w)` — retained count for word `w` (the census
  functional; the banked N10 column "retained").
- `FILT(n,ell,layout,w)` — candidates whose `r` existence conditions all
  hold (i.e. a degree-`<k` interpolant on `S` exists), before the
  exactness guard.
- `RETPRED(n,ell)` — the random-word law, R1 below.
- `EXC(w) := RET(w)/RETPRED` — excess over the random-word law.
- `RATIOBOX(w) := RET(w)/(BOX/q)` — the F-w1 normaliser of record.
- `RATIOSHELL(w) := RET(w)/(N_{k+1}/q)` — proposed sharper normaliser.
- `MAXEXC(n,ell)` — max of `EXC` over the declared search space (R0.5).

### R0.3 Layout families (declared; the layout is a free parameter and
is therefore part of the search space)

- **LAYOUT-A (contiguous)** — verbatim `d3_ell_sweep.py:32-42`:
  `core = 0..k-2`, `bgs = k-1..k-2+b`, petals = consecutive index blocks
  of length `ell`. This is the round-21 `ell`-sweep baseline of record
  (the n=24 comparison the brief names).
- **LAYOUT-B (coset / antipodal)** — the banked N10 layout, verbatim
  `a5_scale32.py:24-31` at `ell=2`, generalised to `ell | n` by taking
  petals to be cosets of `mu_ell` in `mu_n`. Defined only when `ell | n`.
  This is the layout that carries the banked 43/33/2879/2857.

### R0.4 Cell grid (declared in full, before measurement)

`q = 97` throughout (`n | 96` forces `n in {16,24,32,48,96}`; 48 and 96
are out of local reach, so the reachable grid is `n in {16,24,32}` —
this is a hard arithmetic constraint of the multiplicative-subgroup
domain, not a choice).

- n=32 (LAYOUT-A): `ell = 2,3,4,5`. n=32 (LAYOUT-B): `ell = 2,4`.
- n=24 (LAYOUT-A): `ell = 2,3,4,5,6`. n=24 (LAYOUT-B): `ell = 2,3,4,6`.
- n=16 (both layouts): `ell = 2,3` — replication gate only.

**Registered structural caveat, stated before measuring:** the chart
formula gives `t = floor((n-k+1)/ell)`, and the floor band
`a <= Lambda = 2*ell+b-2` is a *restriction* only while `Lambda < |C| =
k-1`, i.e. while `t >= 3`. I predict (P0) that at `n=24` the two cells
the brief names, `ell=5` and `ell=6`, both give `t=2` and hence a
**vacuous band** (`Lambda = k-1 = 11`), so they are *not* floor-band
cells; I will still measure them, but will label them `t=2, band
vacuous` and will not read them as points on the floor-band curve.

### R0.5 Word search space (declared exhaustively, before measurement)

`RET` is invariant under `c -> lambda c` (`lambda in F_q^*`): the filter
conditions are linear in `c` and `U -> lambda U` maps the interpolant
`P -> lambda P`, so the agreement set is unchanged. The word space is
therefore `P^{t-1}(F_q)`, of size `(97^t-1)/96` — 921,414 at `t=4` and
7.4e14 at `t=8`, so exhaustive search is impossible at every `n=32` cell
and I will never claim one.

Per cell I test, in this order:
1. `consec`: `c_i = (i+1) mod q` (banked schedule 1).
2. `geom5`: `c_i = 5^i` (banked schedule 2).
3. `mindeg`: **the minimal-degree word**, defined chart-independently as
   follows. The interpolant of `U` over `D = mu_n` has
   `coeff_s(U~) = (1/n) sum_i c_i D_s(i)` with
   `D_s(i) = sum_{pt in T_i} L_C(x_pt) x_pt^{-s}`. `mindeg` is a nonzero
   `c` killing the largest possible number of top coefficients
   `s = n-1, n-2, ...`; found by nullspace of the top-`j` rows of
   `D`, taking the largest `j` with a nonzero kernel. (At LAYOUT-B,
   `ell=2`, `n=32` this must reproduce `a5_scale32.py:186-188`'s
   `c_i = x_i^2 - x_bg^2` up to scale — registered as a check.)
4. `rand`: 12 words drawn uniformly from `(F_q^*)^t` with pairwise
   distinct entries, `numpy.random.default_rng(20260807)`, drawn in
   cell order (n ascending, then ell ascending, then layout A then B).
   Label: SAMPLED.
5. `ransac`: filter-guided search in the style of `a5_scale32.py:192-227`
   — random `t-1`-subsets of the `s=0` gamma rows, solve for the kernel
   direction, rank by `FILT`, exact-evaluate the top 6. Trials: 1500 at
   cells with `BOX <= 1e6`, 300 at larger cells (cost). Label: SEARCHED.

Round-21's finding that the exhaustive `n=16` maximum was **not**
filter-extremal is registered here as a known limitation: `ransac`
maximises `FILT`, which round-21 showed is anti-correlated with `RET` at
the extreme (a 268,026 filter spike collapsing to 122 exact,
`REPORT.md:50`). I therefore register in advance that **no search in this
pilot can establish an upper bound on the true max**; every reported max
is a lower bound on the true max, labelled SEARCHED.

## R1. Derivation registered before it is checked (DERIVED, to be CHECKED)

Extending the round-21 `BOX` identity to a shell-resolved closed form:

```text
N_{k+r}(n,ell) = sum_{a=0}^{Lambda} sum_{nb=0}^{b}
                 C(k-1,a) * C(b,nb) * M(t,ell,om),   om = a+nb-b+1-r,
   M(t,ell,om) = 0                                      if om <= 0,
   M(t,ell,om) = C(t*ell,om) - [ell | om] * C(t,om/ell) if om >= 1.
BOX(n,ell)  = sum_{r>=1} N_{k+r}(n,ell).
```

(The subtracted term is exactly the non-mixed configurations: every
petal fully met or fully missed <=> `O` is a union of whole petals.)

**The random-word law**, extended to shells (this is the round-21 law
`REPORT.md:40` written per shell):

```text
RETPRED(n,ell) = sum_{r>=1} N_{k+r}(n,ell) * q^{-r} * (1 - 1/q)^{n-k-r}.
```

**The existence test I will use** (replaces the round-21 "drop `m-1`
points" filter, which reduces `S` to a `(k+1)`-subset only when `b=1`
and is therefore not usable at the `b=2` cells this sweep needs): for
`|S| = k+r`, a degree-`<k` interpolant on `S` exists **iff**

```text
sum_{j in S} U_j x_j^{s+1} prod_{l in D\S} (x_j - x_l) = 0,  s = 0..r-1.
```

(top-`r` coefficients of the degree-`<k+r` interpolant vanish; the
weights use `prod_{l in D, l != j}(x_j-x_l) = n x_j^{-1}` on `mu_n`.)
This is necessary AND sufficient, so `FILT` here is the exact existence
count, not a superset. **Registered self-correction, pre-measurement:**
`d3_ell_sweep.py:84-86` computes `R = drop[:m-1]`, which lands on a
`k`-point subset when `b >= 2`; requiring the divided difference to
vanish on a `k`-point set is a *stronger* condition than membership, so
that script would UNDERCOUNT at `b>=2` cells. All round-21 cells have
`b in {0,1}` so no banked number is affected; but two of my n=32 cells
(`ell=3`, `ell=5`) have `b=2`, so I must not reuse that filter there.

## R2. Predictions (each with its falsifier)

- **P0 (structure).** At `n=24`, `ell=5` gives `(t,b)=(2,3)` and `ell=6`
  gives `(t,b)=(2,1)`; both have `Lambda = 11 = k-1`, band vacuous.
  Falsifier: any other `(t,b)`.
- **P1 (closed form).** The R1 closed form equals the enumerated
  `BOX` and every `N_{k+r}` at every completed cell, and reproduces the
  banked candidate totals 5,096 (`n=16`) and 386,640 (`n=32`) at
  `ell=2`, LAYOUT-B. Falsifier: any mismatch, anywhere.
- **P2 (replication gate — runs FIRST, before any new number is
  reported).** My engine reproduces exactly: LAYOUT-B `n=16 ell=2`
  consec/geom5 = **43 / 33**; LAYOUT-B `n=32 ell=2` consec/geom5 =
  **2,879 / 2,857**; LAYOUT-A `n=24` consec at `ell=2,3,4` = **475 /
  8,135 / 20,942** (round-21 `REPORT.md:52`). Falsifier: any mismatch —
  in which case I report the discrepancy and report NO new numbers.
- **P3 (F-w1, the mandated test).** F-w1 does **not** fire: for every
  cell and every word in R0.5, `RATIOBOX = RET/(BOX/q) <= 10`.
  Falsifier: `RATIOBOX > 10` for any word — then I report the witness
  with a reproduction script and STOP the positive line.
- **P4 (F-w2).** No mixed floor-band contributor has `sigma > Lambda`.
  I note in advance that *inside* the family this is tautological
  (`|S| <= a + nb + t*ell - 1 <= Lambda + k`, using `om >= 1` which the
  mixed clause forces), so I register a genuine **off-family** test:
  enumerate the relaxed family with `om >= 0` (dropping clause (iii))
  at `n=24 ell=2,3` and `n=32 ell=2`, and verify that every retained
  member with `|S| = k+Lambda+1` has `om = 0`, i.e. is non-mixed.
  Falsifier: a retained member with `|S| > k+Lambda` and `om >= 1`.
- **P5 (D4 shape).** `RATIOBOX` is strictly **decreasing** in `ell` at
  fixed `n` on the schedule words, because `BOX` is increasingly
  dominated by deep shells (`N_{k+2}/N_{k+1} ~ Lambda/(t*ell-Lambda+1)`,
  which grows with `ell`) while `RET` is carried by `r=1`. Quantitative
  form: `RATIOBOX ~ (1-1/q)^{n-k-1} * N_{k+1}/BOX`.
  Falsifier: `RATIOBOX` increases across any consecutive `ell` pair at
  fixed `n` and layout by more than 3 Poisson sigma.
- **P6 (D3 law).** `|EXC - 1| <= 0.10` at every cell/schedule-word with
  `RETPRED >= 100`; within 3 Poisson sigma where `RETPRED < 100`.
  Falsifier: violation at any such cell.
- **P7 (mindeg structural excess).** `EXC(mindeg) <= 1.30` at every
  cell, and does not increase monotonically in `ell`. (Round-21 measured
  a consistent ~16% structural excess at `ell=2`, `n=16` and `n=32`.)
  Falsifier: `EXC(mindeg) > 1.30`, or a monotone rise in `ell` across
  three or more cells.
- **P8 (search max).** `MAXEXC <= 3.0` at every `n=32` cell.
  (Round-21's exhaustive `n=16` max was 2.05x the mean.) Falsifier:
  `MAXEXC > 3.0`. Label: SEARCHED — a lower bound on the true max.
- **P9 (extrapolation, D4).** Registered as an honest extrapolation, not
  a measurement: the consumer regime `ell = Omega(n/log n)` has
  `t = (k+1)/ell = O(log n)`, so the *relevant* direction is small `t`
  with large `ell` — exactly the direction of this sweep. I predict the
  measured `RATIOBOX` trend, extrapolated, stays bounded (does not grow),
  and I will state explicitly what the trend cannot decide.

## R3. Compute-fit declarations

Every `python3` invocation goes through `tools/ramguard tiny|local --
python3 ...` from the repo root. Checkpoints (if any) are written only
inside `notes/pilots_20260807/l1_ell_sweep/`. No Modal launch. For every
cell I attempt and cannot fit, I will report exact cost (candidate
count, peak memory, measured or extrapolated wall time) and emit a
Modal request line for the coordinator instead of running it.

## R4. Epistemic labelling contract

DERIVED+CHECKED = closed forms machine-verified against enumeration.
MEASURED = exact enumeration over a fully specified family.
SEARCHED = maximum over a declared, non-exhaustive search (lower bound
on the true max). SAMPLED = random draw with a declared seed.
Census evidence is evidence, never proof. No status flip, no closure
claim.


# AMENDMENTS AND SELF-CORRECTIONS (appended after measurement; each says
# plainly whether it was pre-registered)

- **A1 (R0.5 deviation, forced).** R0.5 registered "one
  `default_rng(20260807)` stream in cell order". Cells run in separate
  ramguard invocations, so a single stream is not reproducible per cell.
  Actual: `seed = 20260807 + 1000*n + 10*ell + (0 for LAYOUT-A, 1 for
  LAYOUT-B)` (`sweep_run.py:cell_seed`). Nothing was re-drawn or
  re-seeded after seeing a result.
- **A2 (P2 target was wrong; adjudicated).** The gate target
  "LAYOUT-A n=16 ell=3 = 0" came from replaying `d3_ell_sweep.py`. The
  engine says 100 and an independent third code path (`brute.py`, direct
  Vandermonde solve) also says 100 with identical histograms
  `a={2:16,3:30,4:54}`. Cause found: `d3_ell_sweep.py:86`
  `R = set(drop[:m-1])` with `m = a+nb-om`; at `b=0` the whole `r=1`
  shell has `m=0`, and Python's `drop[:-1]` then deletes all but the
  last core point instead of nothing. Every cell quoted in the round-21
  REPORT/addendum has `b=1` (`m>=1`), so no banked number is affected.
  The gate target was corrected to 100 and re-passed.
- **A3 (NOT pre-registered).** `ub_scan.py` (the word-uniform upper
  bound `UB(c) = #{S : g^{(0)}(S).c = 0} >= FILT(c) >= RET(c)`) was
  built AFTER the n=24 exact sweep, to turn the F-w1 test from a search
  into an exhaustive statement wherever `t <= 3`. It is an addition, not
  a registered prediction; its verdicts are labelled EXHAUSTIVE only
  where the word space really is enumerated.
- **A4 (NOT pre-registered; derived then CHECKED).** `degen_word.py`
  proves and evaluates `RET(lambda*(1,...,1))` in closed form, because
  that single word is the only one exceeding the UB threshold at
  n=24 ell=4/6 and n=32 ell=5, and its full evaluation at n=32 ell=5
  exceeds the ramguard local wall. CHECKED: it returns 375,674 at
  n=32 ell=3 and the full engine returns 375,674; it returns 0 at every
  `b<=1` cell and the full engine measured 0 at n=24 ell=4 and ell=6.
- **A5 (grid extension, NOT pre-registered).** R0.4 declared
  `n in {16,24,32}`. After measuring throughput, `n=64` at `q=193`
  became reachable and was added: LAYOUT-B ell=2 (the fourth and
  strongest replication gate: the banked 109,391 / 108,600), LAYOUT-A
  ell=2 and ell=3.
- **A6 (declared but not run).** n=32 ell=6 and ell=8 were in the R0.4
  grid. Measured cost is ~93 s/word (reachable); they were skipped for
  session time, not for cost. They are `t=2` vacuous-band cells and the
  n=24 `t=2` cells already cover that regime.
