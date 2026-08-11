# PREREG — r35_fg_razor (round 35)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r34_pstar/REPORT.md` (round 34)
2. `notes/pilots_20260811/rh_moving_kernel/REPORT.md` (round 33)

## Mandate

R-FG-RAZOR — THE KEY-EQUATION BUDGET AT THE WITNESS COORDINATES.
Round 34 resolved R-PSTAR YES: FG is nonempty at razor shape, by
witnesses A (impulse pair) and B (P* = P_1 P_2, P_1 irreducible of
degree 2^34), with the coordinator's factor-16 correction of
record (FG needs p* <= 2rho = R/32, NOT R/2 — there is an
intermediate stratum 2rho < p* <= R/2 with a fixed generator but
non-principal K_0). The fixed-generator branch of far-CA is
therefore LIVE, and its object is the key equation
C_gamma · sigma ≡ h (mod P*) in the scaled-Vandermonde normal
form (anchor 2). THE QUESTION: does the FG mechanism at razor
shape stay inside the type-2 spend/list budget (producing the
strict-endpoint contradiction), or does it die on a named budget?
The far-CA residual set is {R-FG-RAZOR, R-KER}; this round prices
the first and maps its relation to the second.

## Deliverables

**D1 — THE KEY EQUATION INSTANTIATED.** At witnesses A and B:
write the key equation's exact objects (C_gamma, sigma, h, the
modulus) at razor parameters, and build faithful small-scale
replicas at wide cells (two fields; include cells with 4rho < R —
the separating regime anchor 1 built, since every round-33 cell
was blind to the FG/intermediate distinction). Measure the
degrees-of-freedom vs constraints of the key equation ON the
replicas before any razor claim.

**D2 — THE BUDGET ARITHMETIC AT RAZOR SCALE.** Exact integers,
closed form, pre-committed in your registrations (the anchor-1
R0-i pattern: commit the razor integers in advance; any off by 1
is a registered miss). What does an FG pencil at the razor imply
for the type-2 ledger (spends, X_gamma, the (R+1)-a floor), and
does the implied configuration clear or break the banked caps?
State which banked cap binds first and by how many bits.

**D3 — R-FG vs R-KER STRUCTURE + q_crit.** Does closing R-FG
reduce to R-KER (the kernel budget), are they independent, or do
they exchange under the stacked-rank h_r dictionary? Map it
exactly. SECONDARY (cheap, do last): the q_crit ~ 2^64 check on
the official candidate row — one exact evaluation, two-field
sanity where applicable; zero-power declared beyond the row
checked.

**D4 — VERDICT.** R-FG resolved (either direction) /
walled-with-named-gap; the far-CA residual set after this round
({R-KER} alone, {R-FG, R-KER} still, or restructured); misses
first; cross-pilot flag (do NOT read siblings) for anything
bearing on the realizability or layer-A lanes.

## Blind priors to register

P(the key-equation budget closes at razor — FG breaks a banked
cap), P(R-FG reduces to R-KER), P(the intermediate stratum
2rho < p* <= R/2 carries load this round), P(q_crit passes on the
official candidate), and your pre-committed razor integers
(R0-i pattern).

---

## Pilot registrations (r35_fg_razor) — appended BEFORE any further read

State at time of writing: I have read exactly this PREREG.md,
CONSTRAINTS.md, and the two named anchors
(`notes/pilots_20260811/r34_pstar/REPORT.md`,
`notes/pilots_20260811/rh_moving_kernel/REPORT.md`). Nothing else.
No grep, no `ls` outside my own directory, no interpreter
invocation has occurred. Disclosure: some arithmetic below was
done in-head from the anchors before writing (the razor integers,
the DOF count, the two first-moment exponents); it is registered
here as a commitment, not discovered later. Where a prediction is
calibrated against a number I read in an anchor, I mark it
**semi-blind** rather than pretending it is blind.

### A. Named blind priors (the four the brief demands)

- **R0-a — P(the key-equation budget closes at razor; i.e. the FG
  configuration at razor shape BREAKS a banked type-2 cap and so
  yields the strict-endpoint contradiction) = 0.12.**
  Rationale registered in advance: (i) rounds 32/33/34 each killed
  the hoped-for mechanism, and the base rate for "this round the
  branch closes" in this lane is low; (ii) the key equation's
  first moment runs the WRONG way — see R0-f — every heuristic at
  `q = 2^41` says *all* slopes are bad, which is abundance, not
  contradiction; (iii) witness B saturates the FG1 bracket at
  `p = 2rho`, `m_Q = rho`, the corner with the LARGEST target
  subspace, hence the weakest constraint.
  Complementary registration: **P(R-FG is walled with a named gap
  rather than resolved either way) = 0.55**;
  **P(R-FG resolves NEGATIVELY, i.e. FG demonstrably cannot
  produce the contradiction, by an exhibited or closed-form
  obstruction) = 0.33.**

- **R0-b — P(R-FG *reduces to* R-KER, i.e. closing R-KER closes
  R-FG and the two are not separate work) = 0.25.**
  Split registered: P(independent) = 0.20;
  P(they exchange/are dual under the stacked-rank `h_r`
  dictionary) = 0.25; **P(they NEST — R-FG is the `h_r = p*`
  fibre of R-KER, so R-KER ⟹ R-FG but not conversely) = 0.30.**
  Pre-committed structural claim to be tested (R0-b1, see D-3
  below): the number of `F_q`-linear conditions imposed by the key
  equation is **exactly `rho`, independent of `p`**, in BOTH the
  FG and the general-`h_r` setting; if that holds, the budget
  arithmetic is literally the same count and neither reduces to
  the other. **P(R0-b1 holds) = 0.80.**

- **R0-c — P(the intermediate stratum `2rho < p* <= R/2` carries
  load this round) = 0.20.** It is a band nobody has looked at, it
  is invisible at every round-33 cell, and my mandate is FG. I
  predict it appears only as a boundary remark and a
  non-applicability note (FG2's column-farness equivalence fails
  there). **P(I am forced to build a replica inside the
  intermediate band to answer D1) = 0.30.**

- **R0-d — P(q_crit "passes" on the official candidate) — needs a
  definition, so I fix one now.** "Passes" := the official
  candidate row's field size satisfies `q > q_crit^{(2)} =
  2^{63.9887}`, so that `mu_2 = C(n,r)/q^{2rho} < 1` and the
  random/first-moment model is NOT void there.
  **P(passes) = 0.72.** Sub-registrations:
  P(the official candidate row uses a field of >= 128 bits) =
  0.55; P(it uses exactly `q = 2^128`) = 0.40;
  P(`q < 2^64` at the official row, so the random model is void
  and only construction reaches the far-CA locus) = 0.28.
  Registered in advance: if `q >= 2^128` at the official row then
  `mu_1 < 1` too (threshold `2^{127.9775}`, R0-e), and the
  key-equation budget becomes nonvacuous there — that would be the
  single most consequential outcome of this round, and I flag now
  that I expect the two thresholds to be **within one bit of
  `2^64` and `2^128` respectively**, which is a suspicious
  coincidence with the banked "coverage to `q ~ 2^128`" scale.
  **P(the repo's banked coverage threshold is within a factor 2 of
  `2^{127.977457}`) = 0.50.**

### B. R0-e — pre-committed exact razor constants (R0-i pattern)

Razor shape (round 33 PR-5, anchor 1 D3): `R = k = 2^40`,
`rho = 2^34`, `r = R - rho`, rate-half `n = 2R = 2^41`, `q >= n`,
`D ⊆ F_q` with `|D| = n`. Dictionary I commit to (derived in-head
from the anchors' cell tables `(n,k,a)`): **`R = n-k`,
`r = n-a`, `rho = R-r = a-k`.** Every integer below is committed
now; any off-by-one is a registered MISS.

| # | quantity | committed exact value |
|---|---|---|
| E1 | `R = n-k = 2^40` | 1,099,511,627,776 |
| E2 | `rho = a-k = 2^34` | 17,179,869,184 |
| E3 | `2rho = 2^35` | 34,359,738,368 |
| E4 | `r = R-rho` | 1,082,331,758,592 |
| E5 | `r+1` | 1,082,331,758,593 |
| E6 | `n = 2R = 2^41` | 2,199,023,255,552 |
| E7 | `a = k+2^34` (the argument of `B_ca^far`) | 1,116,691,496,960 |
| E8 | `n-a` (= `r`, consistency check) | 1,082,331,758,592 |
| E9 | `p = deg P*` at witnesses A,B (`= 2rho`) | 34,359,738,368 |
| E10 | `m_P = r+1-p = dim K_0` | 1,047,972,020,225 |
| E11 | `m_Q = p-rho` (saturated `= rho`) | 17,179,869,184 |
| E12 | `deg Q' = R+1-p = m_P+m_Q = r+1-rho` | 1,065,151,889,409 |
| E13 | `(r+1) + m_Q` (key-equation unknowns) `= R+1` | 1,099,511,627,777 |
| E14 | key-equation constraints `= p` | 34,359,738,368 |
| E15 | DOF surplus `= (r+1)+m_Q-p = R+1-p` | 1,065,151,889,409 |
| E16 | `codim{p* <= 2rho} = 2R-3p` | 2,095,944,040,448 |
| E17 | `dim{p* <= 2rho} = 3p-4` | 103,079,215,100 |
| E18 | `codim U_gamma in Lambda = p-m_Q = rho` | 17,179,869,184 |
| E19 | `deg C_gamma <= p-1` | 34,359,738,367 |
| E20 | `(R+1)-a` (reading `a = k+rho`) | −17,179,869,183 |
| E21 | `r/R` exactly | 63/64 |
| E22 | `r/n` exactly | 63/128 |

Committed real constants (float, 6 s.f. after the point):

| # | quantity | committed value |
|---|---|---|
| F1 | `H2(63/128)` | 0.999823883 |
| F2 | `log2 C(n,r) = n·H2(r/n)` | 2.198635975e12 |
| F3 | `theta_2 = n·H2(r/n)/(2rho) = 64·H2(63/128)` | 63.988728 |
| F4 | `theta_1 = n·H2(r/n)/rho = 128·H2(63/128)` | 127.977457 |
| F5 | `log2 mu_1` at `q = 2^41` | 1.494261338e12 |
| F6 | `log2 mu_2` at `q = 2^41` | 7.898867e11 |
| F7 | `log2` (fraction of degree-`2rho` `P*` that are `D`-split-squarefree) at `q=2^41` | −1.153410e12 |

Tolerance registered: E1–E22 exact (integers, no tolerance);
F1–F7 to `±5e-6` relative on the exponent, `±2e6` absolute on F2/F5/F6.
E20 is registered with the caveat that I do not yet know what
"(R+1)−a floor" denotes in the banked type-2 ledger; I commit to
E20 under the reading `a = k+rho` and register
**P(the banked "(R+1)-a floor" uses this same `a`) = 0.45**, with
the alternative readings (`a` = a type-2 spend budget symbol, or
`a` = agreement of a *different* stratum) at 0.55 combined.

### C. Pre-committed falsifiable derivations (to be tested on replicas)

- **D-1 (the DOF identity).** For fixed `gamma`, the `F_q`-linear
  system `{(sigma, h) : deg sigma <= r, deg h <= m_Q-1,
  C_gamma·sigma ≡ h (mod P*)}` has `(r+1)+m_Q` unknowns and `p`
  constraints; its solution space has dimension **exactly
  `(r+1)+m_Q-p`** whenever `gcd(C_gamma, P*) = 1`, and strictly
  more otherwise. At the razor `(r+1)+m_Q = R+1 = E13` exactly
  (this equality is special to `p = 2rho`), and the surplus is
  `E15 = deg Q'`. **Prediction: measured on every replica cell,
  `dim = (r+1)+m_Q-p` at `>= 90%` of slopes, with every deficiency
  explained by `gcd(C_gamma,P*) != 1`. P = 0.85.** Reported as a
  per-cell max deviation, not a mean (MISS-2 guard).

- **D-2 (the constraint count is `rho`, always).** `ker` of the
  reduced pencil mod `P*` is `U_gamma = C_gamma^{-1}·Lambda_{<m_Q}`
  (anchor 2, FG5), of `F_q`-dimension `m_Q = p-rho` inside
  `Lambda` of dimension `p`; hence
  `codim U_gamma = p-(p-rho) = rho` **for every `p` in the FG
  bracket**, and `= E18 = 2^34` at the razor. So "gamma is bad" is
  exactly `rho` linear conditions on `sigma mod P*`, and the FG
  stratum's position `p` does **not** change the constraint count.
  **P = 0.85**, two-field confirmation required.

- **D-3 (R0-b1, the nesting claim).** If D-2 holds, then the
  general-`h_r` (R-KER) count also imposes `h_r - rho <= rho`
  ... more precisely the moving increment is `h_r-rho` and the
  per-slope condition is again `rho`-dimensional at full stacked
  rank. **Prediction: R-FG and R-KER carry the SAME per-slope
  constraint count `rho`, so they nest (R-KER ⟹ R-FG) and do not
  exchange; neither reduces to the other in the sense of making
  the other free. P = 0.55.**

- **D-4 (the bad-slope first moment).** Per slope, the expected
  number of `sigma ∈ D_r(D)` with `sigma mod P* ∈ U_gamma` is
  `mu_1 = C(n,r)/q^{rho}` (density `q^{-rho}` × `|D_r(D)| =
  C(n,r)`). Hence a Poisson envelope
  `T/q <= 1 - exp(-mu_1) + 0.10`. **SEMI-BLIND**: calibrated
  against anchor 1's four published `T` rows (W1 0.882 vs 0.935,
  S2 0.540 vs 0.816, S1 0.470 vs 0.744, S3 0.225 vs 0.384), which
  I read as an anchor — disclosed, not blind.
  **Prediction: the envelope holds at every replica cell (P = 0.75),
  and `T/q` is monotone in `mu_1` across cells (P = 0.70).**
  Razor consequence, registered now: `log2 mu_1 = F5 = 1.49e12`,
  so the heuristic says `T = q` (or `q+1` projectively) — i.e.
  **every slope bad and NO slope-counting contradiction**. This is
  the outcome I expect and it is why R0-a is 0.12.

- **D-5 (the two thresholds).** The key-equation budget is
  nonvacuous only when `mu_1 < 1`, i.e. `q > 2^{theta_1} =
  2^{127.977457}` (F4). Column-farness's own first-moment model is
  nonvacuous only when `mu_2 < 1`, i.e. `q > 2^{theta_2} =
  2^{63.988728}` (F3). **These are the two razor thresholds and
  they differ by exactly a factor 2 in the exponent (P = 0.95,
  since `theta_1 = 2·theta_2` identically at rate-half razor
  shape).**

- **D-6 (witness-B faithfulness).** A replica is *faithful* iff it
  reproduces, at small scale: `p* = p = 2rho`, `K_0` principal with
  `deg gcd(K_0) = 2rho`, `dim K_0 = r+1-2rho`, `P* = P_1P_2` with
  `P_1` irreducible of degree `rho` (so `Lambda` has a field
  factor of degree `rho`), column-far, and `4rho < R`.
  **Prediction: all six hold at all replica cells, 2 fields
  minimum. P = 0.85.** I will report any cell that fails, not drop it.

### D. MISS-2 GUARD (mean-vs-max), pre-registered

1. **Every count used AGAINST a candidate cap is reported as a MAX
   over the sample**, never a mean. Means appear only as
   distribution descriptors and are never used to falsify or to
   support a bound.
2. **A census that never sees an event proves nothing about
   existence** (round 34's lesson, its miss 3/ZP-2). If any event
   is unobserved I will say "unobserved", not "does not occur".
3. **Codimension bounds density, never emptiness** (anchor 1
   miss 7). I will not let a codimension carry an emptiness or a
   budget verdict.
4. **First-moment expectations at razor scale have zero power in
   both directions.** In particular I will NOT let `E[#bad slopes]
   = q` stand as a proof that all slopes are bad, and I will NOT
   let `mu_2 >> 1` stand as a proof that column-far pencils are
   rare — anchor 1's witnesses A and B refute exactly that.
5. **Saturation artefact flag**: at every cell I can reach,
   `mu_1 ∈ [0.4, 3]`, so `T` near `q` is the expected behaviour of
   *any* pencil there. `T` measurements are used as **falsifiers of
   candidate bounds only**, never as support for one.
6. Any per-slope "spend" or "list size" is reported as
   (min, median, max) with the max carrying every claim.

### E. Zero-power pre-declarations

- **ZP-1.** No razor-scale computation will exist in this report.
  All machine numbers will be at `q <= 31`, `R <= 20`, `rho <= 5`.
  Every razor statement is closed-form arithmetic plus elementary
  scale-free proof.
- **ZP-2.** Replicas must have `4rho < R` to separate FG from the
  intermediate band; **every round-33 cell has `2rho >= ceil(R/2)`
  and is structurally blind to the distinction** (anchor 1 D1.2).
  I claim zero power from any cell without `4rho < R`.
- **ZP-3.** The random/first-moment model has **zero power at the
  razor** (`log2 mu_1 = 1.49e12` at `q = 2^41`). Every heuristic I
  quote at razor scale is labelled heuristic and supports no verdict.
- **ZP-4.** I will not measure the density of FG among column-far
  pencils; FG is reached by construction only.
- **ZP-5.** `q_crit` is a first-moment threshold, not a proved
  phase transition. **Zero power beyond the single official
  candidate row I evaluate**; no claim about other rows, other
  rates, or the behaviour of the true count near the threshold.
- **ZP-6.** Any statement about the type-2 spend/list ledger,
  `X_gamma`, or the "(R+1)-a floor" is limited to text I can cite
  at `file:line`. I claim **zero power over ledger variants I do
  not read**, and if I cannot locate a named object I will report
  "not located" rather than reconstruct it.
- **ZP-7.** No claim about `char F_q`, about non-squarefree `P*`
  inside the FG3/FG4 normal form (witness A is deliberately kept
  out of the key-equation analysis), or about canonicity of `P*`
  (anchor 1 D1.4: `dim Ann(V)_{p*} = 3p*+1-2R`, so `P*` is a
  *choice* when `3p* > 2R+1`).
- **ZP-8.** Two-field minimum (I plan `q ∈ {11,13,17,19}`) for
  every structural claim; any claim confirmed at one field only
  will be labelled single-field.

### F. Compute plan

At most **6 interpreter invocations**, every one from the repo
root as `tools/ramguard tiny -- python3 ...` (256M/60s,
`RAMGUARD_TIMEOUT=55`) or `tools/ramguard local -- python3 ...`
(1G/5min, `RAMGUARD_TIMEOUT<=290`), with the literal `--` and the
timeout documented per use. Stdlib only. No bare `python3` for any
purpose including patching, probing or no-ops. All file edits via
Edit/Write; no `sed -i`/`awk -i`/`perl -i`/`tee`/redirection onto
an existing file. Results checkpointed to `*_results.txt` in this
directory after every emit. `dag.json` never opened. Planned:
`e1_replica.py` (faithful witness-B replicas at `4rho < R`,
two+ fields, D-1/D-2/D-6), `e2_budget.py` (key-equation budget
census: `T`, per-slope list sizes, D-4), `e3_razor.py` (closed-form
razor integers E1–E22 and F1–F7, `q_crit`), optional `e4` for the
official-candidate row. Recursive greps use search-level
`--exclude-dir` for `prize-codex-`, `pilots_20260802`, and the
sibling `r35_*` directories.

### G. Miscellaneous registrations

- **P(I find at least one banked statement that must be corrected
  and flagged to the coordinator) = 0.80** (rounds 33 and 34 each
  found one at `crossing_location`).
- **P(the anchor-1 flags 1–4 are still unrepaired in the bank when
  I grep) = 0.70.**
- **P(`B_ca^far(k+2^34) < 2^128` moves this round) = 0.05.** I
  expect to add no bound, as in rounds 33 and 34.
- **P(a named budget kills the FG mechanism outright — a clean
  negative resolution of R-FG) = 0.33** (see R0-a split).
- **P(the far-CA residual set after this round is still
  `{R-FG, R-KER}`) = 0.55**; P(`{R-KER}` alone) = 0.10;
  P(restructured, e.g. into a single `h_r`-indexed family) = 0.35.
- Prediction on my own errors: **P(at least one of E1–E22 is
  wrong) = 0.10**; **P(at least one of F1–F7 is outside its
  tolerance) = 0.15**.

*No registration above will be edited after this point.*
