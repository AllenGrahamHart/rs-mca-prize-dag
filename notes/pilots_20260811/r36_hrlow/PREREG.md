# PREREG — r36_hrlow (round 36)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r35_fg_razor/REPORT.md` (round 35)
2. `background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md`

## Mandate

R-HRLOW — THE NEW LOAD-BEARING FAR-CA RESIDUAL. Round 35
restructured the far-CA residuals around the stacked rank h_r:
R-FG (h_r = 2rho, ring structure) carries no structural bad-slope
floor and cannot host the extremal count; **LB1 (h_r = rho+1, the
minimal nonzero increment) has an EXACT floor T_1 = r+1,
field-size independent, attaining (C3) at zero bits and beating
its own first moment by 6.7e11 bits** — via the only known
mechanism in the lane: a fixed (r+1)-point set T with the r+1
locators T\{t}. THE QUESTION OF RECORD: is LB1 the unique
beat-the-moment object, or does the h_r = rho+2..rho+O(1) band
carry analogues? If the low-h_r band above LB1 is moment-bound
(no structural floor), the extremal count is LB1-limited and an
upper-bound campaign can target B_ca^far's exact value. Anchor
1's faithfulness conditions are MANDATORY on every cell:
a > R+1, a-1 > r, 4rho < R (the k=1 trap inverted a headline).

## Deliverables

**D1 — THE h_r = rho+1 STRATUM CLASSIFIED.** Is LB1 the ONLY
h_r = rho+1 column-far family? Parameterize: dim K_0 = r-rho,
increment 1 — what does one increment dimension force? Anchor 1's
p*(LB1) = max(rho+1, floor((R+2)/2)) law: prove or refute its
CONVERSE (does h_r = rho+1 force the LB1 shape / that p*?). A
classification theorem here decides whether "LB1-limited" is even
well-posed. Test at >= 2 razor-faithful shapes, >= 2 fields.

**D2 — THE h_r = rho+2 BAND.** Census + construction: does a
two-increment analogue of LB1's mechanism exist (two fixed point
sets? a 2-dimensional locator pencil over a fixed support)?
Measure T and T_1 across the mu_1 subcritical threshold exactly
as anchor 1 did (its Poisson-envelope method is banked in its
dir — copy scripts, AUDIT OUTPUT PATHS first). The deliverable is
the presence/absence of a structural floor at h_r = rho+2, both
fields, with the mechanism named if present.

**D3 — THE STRUCTURAL-FLOOR DICHOTOMY, POSED.** From D1+D2: pose
"column-far razor pencils have a structural T-floor iff <named
condition on h_r / the increment structure>" with falsifiers and
the exact relation to (C3)'s e+1 cap (LB1 attains it — is
attainment the mechanism?). What would an upper-bound campaign
need: state the exact statement whose proof gives
B_ca^far(k+2^34) <= <closed form>, and which banked instruments
could carry it.

**D4 — VERDICT.** The far-CA residual map after the round;
misses first; cross-pilot flag (do NOT read siblings). Remember
anchor 1's scope fence: the type-2 ledger is VACUOUS on the open
bracket — do not import it; and q_crit/theta are razor-row
constants.

## Blind priors to register

P(LB1 unique at h_r = rho+1), P(the p* converse holds), P(an
h_r = rho+2 structural floor exists), P(the dichotomy poses
cleanly with (C3)-attainment as the mechanism), P(the upper-bound
statement is stateable this round).

---

## Pilot registrations

Written after reading CONSTRAINTS.md, this PREREG, and EXACTLY the
two named anchors (`r35_fg_razor/REPORT.md`,
`rate_half_ca_hankel_split_pencil_equivalence/statement.md`).
**No other read, no grep, no ls, no interpreter invocation has
occurred.** Everything below was derived in-head from the two
anchors before any machine number existed. Nothing in this block
will be edited afterwards.

### R1. Dictionary and cell table (fixed in advance)

Razor: `R = k = 2^40`, `rho = a-k = 2^34`, `r = n-a = R-rho`,
`n = 2R = 2^41`. Hankel `M_r(y)` is `rho x (r+1)`; stacked rank
`h_r in [rho, 2rho]`; `dim K_0 = r+1-h_r`; increment `= h_r-rho`.

**Faithfulness is MANDATORY on every cell: `a > R+1`, `a-1 > r`,
`4rho < R`.** My cell table, checked by hand now:

| cell | n | k | R | rho | r | a | 4rho<R | a>R+1 | a-1>r |
|---|---|---|---|---|---|---|---|---|---|
| H1 | 20 | 10 | 10 | 2 | 8 | 12 | 8<10 Y | 12>11 Y | 11>8 Y |
| H2 | 22 | 11 | 11 | 2 | 9 | 13 | 8<11 Y | 13>12 Y | 12>9 Y |
| H3 | 24 | 12 | 12 | 2 | 10 | 14 | 8<12 Y | 14>13 Y | 13>10 Y |
| H4 | 26 | 13 | 13 | 3 | 10 | 16 | 12<13 Y | 16>14 Y | 15>10 Y |
| H5 | 28 | 14 | 14 | 3 | 11 | 17 | 12<14 Y | 17>15 Y | 16>11 Y |

Any `k=1` cell is **excluded by construction** (anchor 1 miss 1).
Fields: at least two per structural claim, from
`{101, 349, 1009, 10007, 65537}`; a char-2 field
(`GF(32)` or `GF(64)`) is a **stretch** target for R7 only.

### R2. The derivation I commit to IN ADVANCE (falsifiable)

Let `T subset D`, `s = |T|`, and let both syndromes come from
errors supported on `T`: `y_j = syn(e_j)`, `e_0` nonvanishing on
`T`, and let `L` be the interpolation on `T` of the ratio
`lambda_t = e_1(t)/e_0(t)`, `d := deg L`. With
`v_x = 1/prod_{y in D, y != x}(x-y)` (anchor 2 convention),
`W := {w in F^T : sum_x w_x x^i = 0, 0 <= i < rho}`,
`w_x = h(x)/tau_T'(x)`, `deg h <= s-1-rho`, and
`E := prod_{y in D\T}(x-y)`:

- **(R2a)** for `s = r+1`, `K_0 ~= {h : deg h <= r-rho,
  deg(L h mod tau_T) <= r-rho}`, hence for `d <= rho` (no
  wraparound) **`dim K_0 = r-rho-d+1` and `h_r = rho+d`.**
  Sanity: `d=1` gives `dim K_0 = r-rho`, `h_r = rho+1` — anchor 1's
  measured LB1 values, reproduced by the derivation, not fitted.
- **(R2b)** the `E` here equals anchor 1's
  `E = prod_{y in D\T}(x-y)` of degree `a-1` (because
  `1/(u_0(x) tau_T'(x)) = E(x)` when `e_0 == 1`), so
  `Ann(V)_i = {sigma : deg sigma <= i, sigma = E g mod tau_T,
  deg g <= i-rho-d}` and the shifted minimal indices sum to
  `(r+1)+(rho+d) = R+1+d`.
- **(R2c)** hence **`p*(d) = max(rho+d, floor((R+1+d)/2))`**,
  `d* = min(a-1, that index)`. At `d=1` this IS anchor 1's
  `max(rho+1, floor((R+2)/2))` — the formula is a strict
  generalisation, and it reproduces anchor 1's 5/5 measured
  `p*(LB1) = 6,6,7,7,8` at `R=10..14` with no free parameter.
- **(R2d)** bad slopes from this mechanism: `e_0 + gamma e_1`
  vanishes at `t` iff `gamma = -1/L(t)`, so the support of the
  slope-`gamma` error is `s - |L^{-1}(-1/gamma) cap T|`. A degree-`r`
  split locator containing that support exists iff the support has
  size `<= r`. Therefore, writing `f := s-r`:
  - **column-far forces `s >= r+1`** (else `K_0` contains a split
    locator: `f >= 1`);
  - **>= 1 bad slope forces `s <= r+d`** (`f <= d`);
  - **the structural bad-slope count is exactly the number of
    values of `L` on `T` with fibre size `>= f`.**
- **(R2e) THE CAP.** Fibres of size `>= f` inside a set of size
  `s = r+f` number at most `(r+f)/f = r/f + 1 <= r+1`, maximised at
  `f = 1`. **So `T_1 <= r+1` on the whole common-support family,
  with equality iff `s = r+1` AND `L` is injective on `T`.**
- **(R2f) THE FLOOR.** At `s = r+1` (`f=1`) every value of `L` is a
  bad slope, and a degree-`d` `L` has fibres of size `<= d`, so
  **`T_1 >= ceil((r+1)/d)`** — a structural floor at EVERY
  `h_r = rho+d`, decaying like `1/d`, never below `(r+1)/rho = 63`
  at the razor.
- **(R2g) `d = 1` forces `s = r+1` exactly** (from `1 <= f <= d`),
  and a degree-1 `L` is injective, so `T_1 = r+1` is **forced**, not
  chosen. That is my proposed classification theorem for D1.

### R3. Blind priors (the five the brief names, plus mine)

| id | statement | P |
|---|---|---|
| B-1 | **LB1 unique at `h_r = rho+1`**, read as: the `h_r=rho+1` column-far stratum carrying a structural floor is exactly R2's `d=1` common-support family (LB1 up to `(T, e_0, e_1)`) | **0.60** |
| B-1' | a genuinely different `h_r=rho+1` mechanism exists with `T_1 >= 3` and NOT common-support | **0.20** |
| B-2 | **the `p*` converse holds**: `h_r = rho+1` (column-far) forces `p* = max(rho+1, floor((R+2)/2))` | **0.55** |
| B-2' | my generalised law R2c `p*(d) = max(rho+d, floor((R+1+d)/2))` is confirmed at `d=2`, >= 2 shapes, >= 2 fields | **0.60** |
| B-3 | **an `h_r = rho+2` structural floor exists** (some `h_r=rho+2` column-far family has `T_1` bounded below by a field-size-independent function of `r` that exceeds its own first moment) | **0.75** |
| B-3' | that floor is `>= ceil((r+1)/2)` and is ATTAINED at `r+1` by an injective quadratic ratio (so `h_r=rho+2` reaches LB1's extremal value) | **0.55** |
| B-4 | **the dichotomy poses cleanly** with a named condition | **0.70** |
| B-4a | the named mechanism is **(C3)-attainment** (`T_1 = e+1`) | **0.30** |
| B-4b | the named mechanism is instead **support-size/fibre counting** (`f = s-r = 1` and `L` injective), with (C3)-attainment a *consequence* not a cause | **0.60** |
| B-5 | **the upper-bound statement is stateable this round** (exact statement whose proof gives a closed form for `B_ca^far(k+2^34)`) | **0.65** |
| B-5' | it is stateable AND `B_ca^far(k+2^34) < 2^128` moves this round | **0.03** |

Additional pre-registrations, each falsifiable:

| id | prediction | P |
|---|---|---|
| A-1 | R2a: `h_r = rho+d` and `dim K_0 = r-rho-d+1`, measured at >= 2 shapes, >= 2 fields, `d in {1,2}` | 0.85 |
| A-2 | **exact numbers**: `p*(2) = 6,7,7,8,8` at `R = 10,11,12,13,14` (`rho = 2,2,2,3,3`) | 0.55 |
| A-3 | `dim K_0(d=2) = r-rho-1 = 5,6,7,6,7` at H1..H5 | 0.80 |
| A-4 | R2g: every `d=1` common-support column-far cell has `s = r+1` and `T_1 = r+1` exactly, field-size independent | 0.85 |
| A-5 | R2e: NO common-support cell, any `d <= rho`, any field, has `T_1 > r+1` | 0.80 |
| A-6 | R2f: at `d=2`, `s=r+1`, a NON-injective quadratic gives `T_1` strictly between `ceil((r+1)/2)` and `r+1`, and at least one cell attains `ceil((r+1)/2)` | 0.50 |
| A-7 | the `s = r+2`, `d=2` sub-branch gives `T_1 <= floor((r+2)/2) < r+1` | 0.60 |
| A-8 | total `T` exceeds `T_1` at small `q` (accidental slopes) and equals `T_1` once `mu_1 = C(n,r)/q^rho << 1`, Poisson envelope `T/q <= 1-e^{-mu_1} + 0.10` at >= 8 measured rows (semi-blind: calibrated on anchor 1's published rows, so declared semi-blind) | 0.70 |
| A-9 | a random/exhaustive column-far pencil search at H1 finds `h_r = rho+1` instances that are NOT common-support | 0.45 |

### R4. MISS-2 GUARD (mean-vs-max) — registered

1. **No mean is ever used against a cap or a floor.** Every `T_1`
   or `T` compared with `r+1`, `ceil((r+1)/d)`, `C(w*,r)` or any
   banked cap is an **exact count** at a named cell/field, or an
   explicit **max/min over a named finite set**. Means appear only
   as descriptors and are labelled as such.
2. **A floor claim is a MIN over the cell family; a cap claim is a
   MAX.** I will not report "average `T_1 = r+1`" as a floor.
3. **A census that is empty proves nothing about a larger cell**;
   emptiness at one `(shape, field)` is reported as that, never
   promoted to a quantifier.
4. **Codimension is not emptiness** (anchor 1's guard, retained):
   `dim K_0` statements never license "no split locator".
5. **The first moment has zero power in both directions** — it is
   wrong by `6.7e11` bits at the razor. No `E[T]` supports any
   verdict here; envelopes are descriptive only.
6. **Max-quantified claims ("no cell exceeds `r+1`") carry an
   explicit zero-power declaration** naming the search space
   actually swept.

### R5. Zero-power pre-declarations

- **ZP-1.** No razor-scale computation will exist. All machine
  numbers at `q <= 65537` (plus at most one char-2 field of size
  `<= 64`), `R <= 14`, `rho <= 3`, `r <= 11`. Every razor statement
  is a closed-form evaluation, never a measurement.
- **ZP-2.** Zero power from any `k=1` cell for any `p*`, `h_r` or
  `T_1` claim (anchor 1 miss 1). None will be used.
- **ZP-3.** Zero power from the first-moment model in both
  directions at the razor (anchor 1 ZP-3, inherited).
- **ZP-4.** Unless I run an EXHAUSTIVE sweep of column-far pencils
  at a named cell, every uniqueness/classification claim is scoped
  **"within the common-support family"** and I claim zero power
  over pencils outside it. If a sweep is only a sample, "no other
  mechanism found" is reported as a sample statement with the
  sample size, never as a quantifier.
- **ZP-5.** Zero power over `char F_q` beyond the fields actually
  run. If the char-2 stretch (R7) is not reached, the char-2
  injectivity remark is declared **unmeasured**, not asserted.
- **ZP-6 (scope fence, from anchor 1).** The type-2 spend ledger
  `(C2)` is **VACUOUS by sign on the whole open bracket
  `[k+2^34, 3n/4)`** and I will **not import it**. Where I need an
  incidence cap I derive it myself from `C(w*, r)` / fibre
  counting and say so. `q_crit`, `theta_1`, `theta_2` are
  **razor-row constants** and will not be read as row-level
  constants.
- **ZP-7.** `T` (total) and `T_1` (structural) are different
  functionals. No claim that they are equal at any field where
  `mu_1` is not `<< 1`. Accidental (type-2) slopes are field-size
  dependent and support no structural claim.
- **ZP-8.** Anchor 1's D1.2 "`h_r = p*` ⟹ FG" reading is known
  false (anchor 1 miss 2 / flag 3). I will use the two
  principality tests separately and never treat `h_r = p*` as an
  FG criterion.
- **ZP-9.** Every structural claim requires **>= 2 shapes AND
  >= 2 fields** (two-field confirmation). Any single-field or
  single-shape result is reported as such and carries no
  quantifier.

### R6. Deliverable-level registrations

- **D1** — I will (i) verify R2a/R2c/R2g at H1..H5 over >= 2 fields;
  (ii) attempt a search for `h_r = rho+1` column-far pencils
  outside the common-support family (A-9); (iii) state the
  classification theorem with its exact hypotheses and whichever of
  "proved / proved-within-family / refuted" the evidence supports.
- **D2** — construct `d=2`, `s=r+1` (injective and non-injective
  `L`) and `d=2`, `s=r+2`; measure `h_r`, `dim K_0`, `p*`, `T`,
  `T_1` across the `mu_1 = 1` threshold at >= 2 shapes, >= 2
  fields; report presence/absence of the floor and NAME the
  mechanism.
- **D3** — pose the dichotomy in the form "column-far razor pencils
  have a structural `T`-floor iff <condition>", with explicit
  falsifiers, and state the exact upper-bound statement plus the
  banked instruments that could carry it.
- **D4** — verdict, misses first, cross-pilot flag; no sibling read.

### R7. Compute plan

`<= 6` interpreter invocations, **every one** as
`tools/ramguard tiny -- python3 ...` (`RAMGUARD_TIMEOUT=55`) or
`tools/ramguard local -- python3 ...` (`RAMGUARD_TIMEOUT=290`),
from the repo root, with the literal `--`. Stdlib only
(`sys`, `math`, `itertools`, `fractions`). No Modal, no network,
no git, no subagents. **No bare `python3` for any purpose,
including patching, probing or no-ops.**

Intended scripts (fresh implementations, in my own directory):
`f1_family.py` (R2a/R2c/R2g at H1..H5, `d = 1,2,3`, several
fields), `f2_band.py` (the `h_r = rho+2` census and the `mu_1`
sweep), `f3_search.py` (A-9: sweep for non-common-support
`h_r = rho+1`), `f4_razor.py` (`tiny`: razor-scale closed forms).

**IMPORTED-SCRIPT RULE, pre-committed.** If I copy any banked
script (e.g. anchor 1's Poisson-envelope code), I will FIRST grep
the copy for `open(`, `write`, and results paths and repoint every
path into `notes/pilots_20260811/r36_hrlow/` with the Edit tool
**before the first import**, because imports can write at import
time. My default is to write fresh scripts and import nothing.

**WRITE DISCIPLINE.** All file edits via Edit/Write. No `sed -i`,
`awk -i`, `perl -i`, `tee`, or shell redirection onto an existing
file. Scripts write only their own `*_results.txt` inside my
directory.

**QUARANTINE.** I will never open
`notes/pilots_20260802/CAMPAIGN_LEDGER.md`, never read
`r36_lawcount_geom`, `r36_sat3_on_l2`, `r36_m4_nonsplit`, and
never `ls` the parent. Every recursive grep carries
`--exclude-dir` for those three plus `pilots_20260802`,
`prize-codex-*`, `.git`, `__pycache__`, and `--exclude=dag.json`.
`dag.json` is never opened.

**Honest disclosure.** The R2 derivation, the cell table, the
faithfulness checks, and the `p*(2)` numbers in A-2 were computed
in-head from the two anchors before this block was written; A-8's
envelope is **semi-blind** (calibrated against anchor 1's
published `T` rows).
