# PREREG — rh_type2_stratum (round 31)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/collinearity_object/REPORT.md` (round 29)
2. `notes/pilots_20260810/apolar_origin/REPORT.md` (round 28)

## Mandate

The residual budgets {2^39, 2^39+1} of RH-AC fail to close for
EXACTLY THREE named reasons (round 29): (i) the 1-or-3-integer w*
tiling gap per m; (ii) THE NON-MINIMUM-WEIGHT TYPE-2 STRATUM, where
the banked cap is 5.04e22 against a budget of 2^39 — a ~39-order
gap and THE BIG ONE; (iii) m = 1. YOUR JOB: residual (ii). Determine
whether the 5.04e22 is crude counting or a real wall: the cap came
from a coarse stratum count; the apolar (AO1) and collinearity (T4)
structure theorems were NOT applied to the non-minimum-weight
stratum. Close it, shrink it, or prove it is the honest frontier.

## Deliverables

**D1 — THE CAP'S ANATOMY.** Reconstruct, file:line, exactly how the
5.04e22 was derived (which count, which stratum definition, which
inequalities). Name every place slack was given away.

**D2 — STRUCTURE TRANSPORT.** Which of the banked structure theorems
(AO1's O=0/m>=2 apolarity route; T4's pencils-only census; U1's
identification; the d_x law) apply to non-minimum-weight type-2
configurations, and with what modifications? Derive the sharpened
cap where they apply; POSE the obstruction where they do not.

**D3 — THE SCALED CENSUS.** At small admissible scales, enumerate
the non-minimum-weight type-2 stratum EXACTLY (the round-29 pilots'
census machinery is banked and readable — copy scripts into your
dir). Measure: actual stratum size vs the 5.04e22-style bound's
small-scale analogue. If the bound is loose by orders of magnitude
at small scales, quantify the looseness trend across >= 3 scales;
pre-register the extrapolation BEFORE running.

**D4 — VERDICT + RESIDUALS.** Either a sharpened cap (exact, with
proof sketch and falsifier), or the honest statement of the wall
with the exact missing ingredient named. Misses first; zero-power
declarations where searches had no power.

## Constraints (binding)

- COMPUTE LAW: never bare python3. `tools/ramguard tiny -- python3 ...`
  (256M/60s) for peeks, `tools/ramguard local -- python3 ...` (1G/5min)
  for real runs, from the repo root, literal `--`. This includes JSON
  peeks and file patching. Stdlib only. No Modal, no network, no git.
- RAM DISCIPLINE: file-at-a-time reads; NEVER open dag.json (node.json
  shards + grep); checkpointed batches with results files for
  anything long.
- WRITE SCOPE: ONLY inside notes/pilots_20260810/rh_type2_stratum/.
  No dag/, nodes/, tools/ edits. No git. Never touch any path
  containing prize-codex-.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md.
  Never read the sibling round-31 dirs (rh_overlap_cap,
  rh_transport_dictionary, rh_e_axis_audit). Round-30 and earlier
  pilot dirs are readable.
- BLIND PRIORS: after reading ONLY the two anchors, append "## Pilot
  registrations" (P(cap crude by >= 10 orders), P(stratum closes
  under 2^39 this round), expected binding obstruction) BEFORE any
  further read.
- REPORT: REPORT.md in your dir; MISSES-FIRST; every quantifier
  claim quoted file:line (CATCH-24C); own-repo greps before novelty
  claims (CATCH-24A); zero-power declarations on max-quantified
  claims; banked scripts from scratch copies only.

## Pilot registrations

Appended with the Edit tool AFTER reading exactly two files
(`collinearity_object/REPORT.md`, `apolar_origin/REPORT.md`) and
BEFORE any other read, any grep, and any interpreter invocation.
Everything below is blind with respect to the rest of the repo.

### R0 — notation I will use (inherited from the two anchors)

Strict `A=3` half-distance profile: `rho = 4m-1`, `N = 16m`,
`R = 8m`, `R+1 = 8m+1`, `e = m`, `A = R+1-2rho = 3`. Official
`m = 2^37`, `N = 2^41`, budgets `{rho+1, rho+2} = {2^39, 2^39+1}`.
`K = [N, N-R, R+1]` MDS kernel code (vanishing power sums `i < R`).
`V = span(c_0,c_1)`, joint support `W`, `a = |W| = w*`, window
`[4m+2, 8m-2]`. `z_gamma = c_0 + gamma c_1`; `S_gamma` = support of
the unique min-weight coset representative `v_gamma`,
`u_gamma = |S_gamma| = rho - o_gamma`, `O = sum_gamma o_gamma`;
`kappa_gamma = z_gamma - v_gamma in K`; `n_gamma = #{x in W :
z_{gamma,x} = 0}`; `d_x` = #supported slopes with `x in S_gamma`;
`T = T_1 + T_2`. NEW symbols I introduce here:
`Z_gamma := W u S_gamma`; `j_gamma := wt(kappa_gamma) - (R+1)` (the
**weight excess**); the stratum in the mandate is
`T_2^{>} := #{type-2 gamma : j_gamma >= 1}` and its complement
`T_2^{=} := #{type-2 gamma : j_gamma = 0}` (weight-extremal, the
one already handled by AO2/T4).

### R1 — D1 anatomy hypothesis (registered as a prediction, not a fact)

I predict the 5.04e22 is the **second summand of (AO1)** evaluated at
the top of the `w*` window:

```
CAP(m,a) := floor( (N-a) * e / (R+1-a) ),   a = 8m-2
CAP(m,8m-2) = floor( (8m+2)*m / 3 )
CAP(2^37, 2^40-2) = 2^38*(2^39+1)/3
                  = 50371909150701174915072  ~ 5.0371909e22
```

and that its derivation is the single incidence count
`T_2 * (R+1-a) <= sum_{x notin W} d_x <= (N-a)*e`, i.e. "every
type-2 slope spends at least `R+1-a` locator roots outside `W`;
each of the `N-a` outside points is spent by at most `e = m`
slopes". **Slack given away, predicted list:** (s1) `R+1-a = 3`
is the *worst-case* per-slope spend, while the saturation identity
`sum_x (m-d_x) = 1+O` forces the *mean* spend to be
`(N-a)m/T ~ 2m`, a factor `~2m/3` of pure loss; (s2) `d_x <= e` is
used as a flat cap although the same identity says `d_x = m` at all
but `1+O` points; (s3) the type-1 term is capped separately and
`min(e+1, floor(a/(a-rho)), ...)` is `= 2` exactly at `a = 8m-2`
(since `(8m-2)/(4m-1) = 2`), so the type-2 term carries the whole
budget; (s4) no structure at all (apolarity, MDS, Hankel) enters.

### R2 — GNF: the generalized reciprocal-locator normal form

Since `K` is (dual-)GRS, the sub-code of `K` supported in a set `Z`
is `{ (f(x)/sigma'_Z(x))_{x in Z} : deg f <= |Z|-(R+1) }`. Hence I
register:

> **(GNF)** For every type-2 slope, `kappa_{gamma,x} =
> f_gamma(x)/sigma'_{Z_gamma}(x)` on `Z_gamma = W u S_gamma`, with
> `deg f_gamma <= j_gamma = |Z_gamma| - (R+1)`.

`j_gamma = 0` recovers AO2 exactly (`f` constant, `kappa_x =
1/sigma'_{W u S}(x)`). I predict AO2/T4 transport **iff** `j = 0`,
and I predict the identification

> **(EQ)** type-2 with equality in `(C2)` (`|S\W| = R+1-a+n`)
> <=> `wt(kappa) = R+1` <=> `j = 0` <=> weight-extremal.

### R3 — TR1: the MDS transport lemma (the route I will try first)

For three slopes collinear on the pencil (`z_3 = alpha z_1 + beta
z_2`), `kappa_3 - alpha kappa_1 - beta kappa_2 = -(v_3 - alpha v_1
- beta v_2) in K` is supported on `S_1 u S_2 u S_3`. Hence:

> **(TR1)** if `|S_1 u S_2 u S_3| <= R = 8m` then `v_3 = alpha v_1
> + beta v_2`, so `S_3 subseteq S_1 u S_2` and the T4 fibre/pencil
> conclusion follows **without** any minimum-weight hypothesis.

Registered as the candidate structure transport for D2. Its cost:
`|S_i| <= rho = 4m-1` gives `|u S_i| <= 12m-3 > 8m`, so TR1 needs a
forced pairwise overlap of total size `>= 4m-3`; I register that
supplying that overlap is the **binding obstruction** (see R6).

### R4 — Predictions (numeric windows, registered blind)

- **P1 (D1 exact).** `5.04e22 = floor((8m+2)m/3)` at `m=2^37`,
  exactly `2^38*(2^39+1)/3 = 50371909150701174915072`. Window: the
  first three significant digits `5.03`/`5.04` and the formula
  `(N-a)e/(R+1-a)` at `a = w*_max = 8m-2`. P(hit) = 0.80.
- **P2 (arithmetic catch on the brief).** The brief's "~39-order
  gap" is imprecise. The honest gap is
  `CAP/(rho+2) = 2^38/3 = 91625968981.33 ~ 9.16e10 ~ 2^36.415`,
  i.e. **~11 decimal orders / ~36.4 binary orders**, not 39.
  P(my reading is the right one) = 0.75.
- **P3 (monotonicity).** `CAP(m,a)` is strictly increasing in `a`
  on `[4m+2, 8m-2]`; `CAP(m,4m+2) ~ 3m` (leading order `3m`), and
  `T_1 + CAP` crosses `rho+1` at `a/m -> 16/3`, reproducing
  apolar's `a_max`. Window: `CAP(m,4m+2)/m in [2.9, 3.0]` for
  `m >= 2^10`; crossing ratio in `[5.30, 5.34]`. P = 0.85.
- **P4 (EQ).** (EQ) holds in 100% of measured configurations at
  every scale I reach. P = 0.75.
- **P5 (GNF).** (GNF) verifies exactly (residual 0) in 100% of
  measured type-2 slopes. P = 0.85.
- **P6 (TR1).** TR1 verifies in 100% of measured collinear triples
  with `|u S_i| <= R`; and the fraction of triples meeting
  `|u S_i| <= R` at `a = 8m-2` is **small** — window `[0, 0.35]`.
  P = 0.6.
- **P7 (the fence is weight-extremal).** The `m=1` fence
  (`W = {1,2,3,5,7,11}`, `q=17`, `a = 6 = 8m-2`) has all three of
  its type-2 slopes at `j = 0`, so `T_2^{>} = 0` there: **the only
  banked failure witness contains none of the stratum the mandate
  is about**. Window: `T_2^{>}(fence) = 0` exactly. P = 0.7.
- **P8 (window degeneracy at m=1).** At `m=1` the window
  `[4m+2, 8m-2] = [6,6]` is a single point, so `m=1` is
  simultaneously residual (iii) and the `a = 8m-2` top; therefore
  `m=1` has **zero power** to separate min- from non-min-weight
  type-2. P = 0.9 (this is a zero-power declaration, R6).
- **P9 (census: the stratum is small at small scale).** Define
  `TRUE(m) := max over sampled pencils with |W| = 8m-2 of T_2^{>}`.
  I register `TRUE(m) <= 2` for `m in {1,2,3,4}` with
  `TRUE(1) = 0`, and the fallback (weaker, near-certain) window
  `TRUE(m) <= rho+2 = 4m+1`. P(strong window) = 0.45,
  P(fallback) = 0.97.
- **P10 (looseness trend, PRE-REGISTERED EXTRAPOLATION).** With
  `CAP(m,8m-2) = floor((8m+2)m/3)` giving `3, 12, 26, 45` at
  `m = 1,2,3,4`, I pre-register the model
  `L(m) := CAP(m,8m-2)/max(1,TRUE(m)) = c*m^p` and predict the
  least-squares `p` fitted over `m in {1,2,3,4}` lands in
  `[1.0, 2.0]`, most likely `[1.6, 2.0]` (because I expect `TRUE`
  to be `O(1)`, while `CAP` is `~(8/3)m^2`). Extrapolated to
  `m = 2^37` this predicts looseness `>> 10` decimal orders, but I
  register in advance that **the only honest, non-circular
  official-scale looseness statement is `CAP/(rho+2) = 2^38/3`**,
  because `T_2 <= T = rho+2` is the failure hypothesis itself.
  P(p in [1,2]) = 0.7.
- **P11 (generic non-extremality).** At `a = 8m-2` under the
  failure hypothesis the *mean* `|S\W|` is `(8m+2)m/T ~ 2m >> 3`,
  so the mean excess `j ~ 2m-3`: the residual stratum is the
  **generic** one and the weight-extremal stratum (AO2/T4's) is the
  thin one. Window: mean `|S\W|/m in [1.8, 2.2]` at official
  parameters, arithmetic only. P = 0.8.
- **P12 (verdict, registered miss-likely).** I do **not** expect to
  close the stratum under `2^39` this round. P(no close) = 0.90.
- **P13 (CATCH-24A subtraction, registered in advance).** I expect
  at least one of {(GNF), (TR1), the pencil-of-Hankel /
  determinantal count `T <= rho+1`} to be **already in-repo**
  (my prior: the Hankel pencil determinant argument is banked, and
  the singular-pencil bucket is the known hard case). I will grep
  before claiming any of them and will report ports as ports.
  P(at least one subtraction lands) = 0.85.

### R5 — Blind priors demanded by the brief

- **P(cap is crude by >= 10 decimal orders)** — read as "an honest,
  non-circular re-derivation available this round brings the
  official-scale cap below `5.04e12`": **0.20**. Read instead as
  "the cap is demonstrably >= 10 decimal orders above the truth"
  (using `T_2 <= T <= rho+2`, which is circular but is the honest
  ceiling): **0.95**, with the exact figure `2^38/3 = 9.16e10`.
- **P(stratum closes under 2^39 this round)**: **0.10**.
- **Expected binding obstruction**: `S_gamma n W != {}` (equivalently
  `j_gamma >= 1`). It destroys the AO2 normal form in two ways at
  once: (a) `kappa_gamma|_W = z_gamma|_W - v_gamma|_W` is no longer
  on the pencil line, so the "reciprocal-locator points are
  collinear" object does not exist; (b) the shortened code on
  `Z_gamma` has dimension `j_gamma+1 > 1`, so the codeword is no
  longer determined by its support — the rigidity that powers both
  AO2 and T4 is exactly what `j >= 1` removes. Secondary predicted
  obstruction: after reformulating as a Hankel/`det` pencil, the
  residual sits in the **singular-pencil bucket** where the
  determinantal count is vacuous.

### R6 — Zero-power declarations (registered in advance)

1. `m = 1` (`q = 17`, `N = 16`) has **zero power** over residual
   (ii): the `w*` window degenerates to the single value `6`, so
   min-weight and non-min-weight type-2 cannot be separated there.
   Every `m=1` number I report is a control.
2. Any `TRUE(m)` I measure is a **max over a sampled set of
   pencils**, never exhaustive over `W` (at `m=2`, `a=14`,
   `C(32,14) = 4.7e8` already), so it is a **lower** bound on the
   true max and has **zero power** to prove the stratum is small.
   It has power only in the falsifying direction.
3. Small-scale census has **zero power** over the official
   `q >= 2^167` regime for any claim that decays in `q`; I will not
   convert a small-`q` count into an official-scale statement.
4. If I report a looseness exponent `p`, it is a fit over four
   points at `m <= 4` and has **zero power** as an extrapolation to
   `m = 2^37`; it is descriptive only.
5. Any statement of the form "no configuration exists" that I get
   from sampling is a **zero-power** statement and will be labelled
   as such rather than reported as a bound.

### R7 — Route order (registered)

(a) D1 anatomy by grep (find the 5.04e22 and the `(N-a)e/(R+1-a)`
derivation, file:line). (b) CATCH-24A subtraction greps for (GNF),
(TR1), the determinantal `T <= rho+1`. (c) D2 derivation +
small-scale exact verification of (EQ), (GNF), (TR1). (d) D3 census
at `m in {1,2,3,4}` (`q` chosen with `16m | q-1`), checkpointed to
results files. (e) D4 verdict. If (c) or (d) overruns, I drop the
largest scale rather than extend, and say so.

### R8 — Compliance plan

Every interpreter invocation `tools/ramguard tiny|local -- python3`
from the repo root with an explicit `RAMGUARD_TIMEOUT`, counted and
reported. Stdlib only. `dag.json` never opened. All writes inside
`notes/pilots_20260810/rh_type2_stratum/` (+ session scratchpad).
`notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened; the three
sibling round-31 dirs never read or listed; no path containing
`prize-codex-` touched. No git, no network, no Modal, no subagents.
Banked scripts run only from md5-verified scratch copies.
