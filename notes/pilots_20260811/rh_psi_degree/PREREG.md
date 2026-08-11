# PREREG — rh_psi_degree (round 33)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/rh_fr_algebraic/REPORT.md` (round 32 —
   D2.4 is your launch point)
2. `notes/pilots_20260810/apolar_origin/PREREG.md` (round 28 — the
   (C2)/K' machinery definitions)

## Mandate

THE 8/5 ON THE TYPE-2 FRONTIER. Round 32 proved FR-canonical
(X <= 4rho-2a*-... at a minimising pair union) and priced the
residual at 7/4 with the missing step exactly 8/5 at the argmax
a = (20m-2)/3: needed X <= a/4, proved min(a-(4m+2), 4rho-2a).
Round 32's D2.4 identified THE live instrument: psi_gamma =
z_gamma * Q_gamma|_W is a polynomial h_gamma of degree
<= a-(4m+2) in the shortened apolar MDS code K'|_W, whose roots in
W are exactly F_gamma u (S_gamma ^ W). (C2) is "a polynomial has at
most its degree many roots"; the needed statement is "h_gamma has
<= ~a/4 + n_gamma roots although its degree allows more". The mean
weight of psi_gamma over the T slopes is ~5.25m against the 5m-1
that the threshold needs — ~5% headroom; the max-vs-mean step here
is NOT self-defeating (unlike the spend count — round 32's MISS 2
explains why). Wave 58's cycle 49 converged on the same object from
the fence side ("control its aggregate near-minimum-weight fibers
using the common pencil"). YOUR JOB: the aggregate weight attack on
the psi_gamma family.

## Deliverables

**D1 — THE AGGREGATE IDENTITY.** The T polynomials h_gamma live in
one MDS code and are coupled by the common pencil (z_gamma =
c_0 + gamma c_1 — the family is a PENCIL of codewords twisted by
the Q_gamma). Derive the exact aggregate: sum over gamma of
wt(psi_gamma) (or of root counts in W) as a function of the
incidence data — is there a second moment / product identity the
pencil forces? (The saturation identity gives the mean; you need
the instrument that caps the MAX — a Chebyshev-type step inside an
MDS code, or the pencil's Wronskian/resultant.)

**D2 — THE SUBCLASS THEOREM.** Prove X <= a/4 + O(1) (or any
c < 1/3 coefficient) on the largest stratum you can reach —
minimum-weight slopes first (j = 0: kappa = 1/sigma'_{WuS} makes
h_gamma explicit). Exact scope + falsifier per result.

**D3 — SMALL-SCALE MEASUREMENT.** Measure the true max root count
of h_gamma in W at the round-31/32 census scales (copy the banked
decoder from rh_type2_stratum/d3_census.py or
rh_fr_algebraic/d3_frcensus.py). Compare against a/4, the (C2)
degree cap, and the mean. Pre-register expectations. CAVEAT
CARRIED: T = 3 in every reachable pencil — (SAT3) untestable here;
say so wherever it binds.

**D4 — VERDICT.** The 8/5 closed, narrowed, or walled — with the
exact surviving obstruction named. Misses first.

## Blind priors to register

P(the aggregate identity exists and is new), P(X <= a/4 provable on
j=0 this round), expected true max/mean ratio at m=3,4.

## Pilot registrations

Appended by rh_psi_degree (Opus 5) 2026-08-11 with the Edit tool, AFTER
reading exactly the two anchors named above
(`notes/pilots_20260810/rh_fr_algebraic/REPORT.md`,
`notes/pilots_20260810/apolar_origin/PREREG.md`) and BEFORE any further
read, any grep, any `ls`, and any interpreter invocation. Everything
below is derivation-from-the-two-anchors plus prediction. No measurement
has been taken.

### R0 — notation (fixed here)

Strict endpoint: `N = 16m | q-1`, `R = 8m`, `rho = r = 4m-1`, `A = 3`,
`e = m`, `s = 0`, `delta = m-1`. `K = [16m, 8m, 8m+1]` MDS kernel code,
`K' = [16m, 12m-1, 4m+2]` MDS apolarity code (`apolar_origin/PREREG.md
:150-166`). `W` a joint support, `a = |W|`, `(c_0,c_1)` its
representation, `z_gamma = c_0 + gamma c_1`, `F_gamma = {x in W :
z_gamma(x) = 0}`, `n_gamma = |F_gamma|`, `S_gamma` the min-weight
support, `u_gamma = rho - o_gamma`, `X_gamma = |S_gamma ^ W|`,
`p_gamma = |S_gamma \ W| = u_gamma - X_gamma`, `d_x = #{gamma supported
: x in S_gamma}`, `v_gamma` the min-weight representative,
`kappa_gamma = z_gamma - v_gamma in K`, `j_gamma = wt(kappa_gamma) -
(R+1) >= 0`. New here:
`def_in = sum_{x in W}(m - d_x)`, `def_out = sum_{x notin W}(m - d_x)`,
`cancel_gamma = #{x in (W \ F_gamma) ^ S_gamma : z_gamma(x) =
v_gamma(x)}`, `ov_gamma = |S_gamma ^ F_gamma|`,
`d := a - (4m+2)` the `(C2)` degree cap of `h_gamma`,
`Dh_gamma := deg h_gamma`, `Rin_gamma`/`Rout_gamma` = number of roots of
`h_gamma` inside / outside `W` (with multiplicity for `Rout`).

### R1 — BLIND PRIORS (the three the brief demands)

- **P(the aggregate identity exists) = 0.95**;
  **P(it exists AND is new in this lane) = 0.20.** I expect it to be a
  two-line re-reading of the banked counting layer `(C4)`
  (`d_x <= e`, `sum_x (m-d_x) = 1+O`, `apolar_origin/PREREG.md:191-193`)
  and therefore BANKED, not new. What I expect to be new is the
  *consequence* (R2.4), not the identity.
- **P(X <= a/4 + O(1) provable on the j=0 stratum this round) = 0.03.**
  I register in advance that I expect the brief's stratum choice to be
  BACKWARDS: see R2.2 — I predict `j = 0` is the stratum on which `X` is
  MAXIMAL, i.e. exactly the `(C2)`-extremal slopes, and that the target
  is false there rather than provable there.
- **Expected true max/mean ratio at m=3,4: EXACTLY 1.000, with zero
  probative content** (P = 0.90). Reason registered in advance: round
  32 measured `T = 3` in `420/420` pencils and `T_1 = 2` at the
  canonical `W*` in `420/420` (`rh_fr_algebraic/REPORT.md:161,217`), so
  `T_2 = T - T_1 = 1`: there is exactly ONE type-2 slope per pencil and
  max = mean identically. The census cannot measure a max/mean ratio at
  all. Secondary (measurable) prediction: `max X / (a*/4)` at the
  canonical `W*` lies in `[0.80, 1.20]` at `m = 3,4`, and `<= 1` in at
  least 4 of the 6 cells.

### R2 — PRE-REGISTERED DERIVATIONS (claims, to be checked, not yet checked)

Derived from the two anchors before any computation. Each is a hard
falsifiable identity; a single census violation kills it.

**R2.1 (AGG) — the aggregate identity.**
`sum_{gamma supported} X_gamma = sum_{x in W} d_x = a*m - def_in`, with
`0 <= def_in <= 1 + O`. With `T_1` type-1 slopes (`S_gamma subset W`, so
`X = u_gamma`), the type-2 total is
`sum_{type-2} X_gamma = a*m - def_in - T_1*rho + sum_{type-1} o_gamma`.
Dually `sum_{type-2} p_gamma = (N-a)m - def_out` (banked,
`rh_fr_algebraic/REPORT.md:25`). Also registered: `sum_gamma o_gamma =
O` and `sum_{g in P^1} n_g = a`.

**R2.2 (JDEC) — the exact per-slope decomposition.**
For every type-2 slope (`kappa_gamma != 0`; I also register
*type-1 <=> kappa_gamma = 0*):
```
X_gamma = [a - n_gamma - (4m+2)]  -  (o_gamma + j_gamma + cancel_gamma)
                                  +  ov_gamma .
```
So `(C2)` is tight exactly when `o = j = cancel = 0` and `ov = 0`, i.e.
**the j=0 stratum is the (C2)-extremal, X-MAXIMAL stratum.**

**R2.3 (OUT) — where the missing degree lives.**
`Rin_gamma = d - (o_gamma + j_gamma + cancel_gamma)` (roots counted
without multiplicity), hence
`(d - Dh_gamma) + Rout_gamma = o_gamma + j_gamma + cancel_gamma`
whenever every root of `h_gamma` in `W` is simple. **The closure target
`X <= a/4` is exactly the statement `o + j + cancel + n >= 3a/4 -
(4m+2)`, i.e. `~ m` for every type-2 slope at the argmax.**

**R2.4 (SHORTFALL) — the a-independent residual.** Under the hypothesis
`T = rho+2`, `T_1 = 2`: `need_X = rho - o - floor((N-a)m/rho) - 1` and
`mean_X = (am - def_in - 2rho + o_g + o_h)/rho`. I register the exact
identity
```
rho * mean_X  -  rho * need_X  =  4m + O - def_in   (>= 4m - 1 > 0),
```
**independent of `a`.** Predicted consequences: (i) the banked `9/4`,
the round-32 `7/4`, the `9/8` at `a = 7m-1` and the `8/5` are four
readings of ONE `a`-independent invariant equal to `rho+1 = 4m` — one
slope's worth of locator mass; (ii) no choice of `W` can move it.

**R2.5 (ARGMAX, closed form).** The argmax `a = (20m-2)/3` is exactly
the crossing of the `(C2)` floor `p >= 8m+1-a` with the `(FR)` floor
`p >= 2a - 3rho`; the residual factor there is `7m/(4m-1) -> 7/4` and
the `X`-ratio `(rho - 4m/3)/(rho - 7m/3) -> 8/5`, both exactly.

**R2.6 (CROSS) — what `16m/3` is.** The banked closure boundary is
exactly the locus where the `(C2)` floor crosses the FORCED MEAN spend
`(N-a)m/T_2`; equivalently `(AO1)` is precisely the statement "the
proved per-slope floor beats the forced mean". Numeric window: my
aggregate criterion `T_2*(a-(4m+2)) < am - def_in - T_1*rho` with
`T_1 = T1cap` must reproduce the banked thresholds `a_max(8) = 42` and
`a_max(64) = 339` EXACTLY (`rh_fr_algebraic/REPORT.md:57`).

**R2.7 (the MISS-2 guard, registered in advance).** `max >= mean` is an
arithmetic fact, and R2.4 says `need_X < mean_X`; I register NOW that
this does **not** make the route vacuous, for exactly the reason round
32's MISS 2 gives (`rh_fr_algebraic/REPORT.md:25`): `mean_X` is forced
only *inside* the hypothetical `T = rho+2`, so a `T`-free per-slope
bound below it is precisely a refutation. What R2.4 *does* forbid is any
instrument that derives its bound *from* the configuration's own
aggregate. I will not report R2.4 as a route fence.

### R3 — D3 PREDICTIONS (numeric windows, before any run)

- **P3.1** `(JDEC)` holds with ZERO violations in every census cell
  (exact integer identity). Window: `0` violations / all type-2 slopes.
  Prior `0.80` (the `cancel`/`ov` terms are my own and may be
  mis-specified; a violation is a specification bug, and I will report
  it as a miss, not patch it silently).
- **P3.2** `(AGG)` holds with `def_in = 0` in `>= 80%` of pencils and
  `def_in <= 1+O` always. Prior `0.85`.
- **P3.3** `T_2 = 1` in `100%` of reachable pencils, hence
  `max/mean = 1.000` exactly and the D3 max/mean measurement has ZERO
  power. Prior `0.90`.
- **P3.4** `Dh_gamma = d = a - (4m+2)` exactly (full degree) in
  `>= 85%` of type-2 slopes; i.e. the missing `m` does NOT show up as a
  degree defect. Prior `0.75`.
- **P3.5** every root of `h_gamma` in `W` is simple, in `>= 95%` of
  slopes. Prior `0.80`.
- **P3.6** `Rout_gamma` (roots of `h_gamma` outside `W`) has mean
  `< 2` at `m = 2,3,4` and never reaches `m`. Registered as the
  small-scale shadow of the residual, with ZERO probative power over
  `(SAT3)`.
- **P3.7 (CAVEAT CARRIED, unchanged)** `T = 3` in every reachable
  pencil, so `(SAT3)` (`T = rho+2`) is untestable at census scale, and
  every D3 number is structural-only. Prior `0.95`.

### R4 — ZERO-POWER FLAGS DECLARED IN ADVANCE

1. `T_2 = 1` at census scale kills all max-vs-mean measurement (R1).
2. `q > 2^167` at official scale: any Weil / Stohr-Voloch / rational
   point-count instrument on the incidence curve is vacuous, since the
   incidence count is `O(m^2) << q`. I register this before trying it.
3. Moment methods: `max >= mean` caps every symmetric instrument at
   `max <= mean(1+eps)`; the target is `mean - 1`. Registered as a
   limitation on MY instrument choice, not as a route fence (R2.7).

### R5 — ROUTE ORDER (registered)

1. D1 aggregate identity + R2.4 shortfall, verified exactly (primary).
2. D2 via `(JDEC)`: the `j = 0` sub-stratum first as the brief asks —
   and I expect to have to report it as the WRONG stratum (R1).
3. D3 census with the NEW measurables `Dh`, `Rin`, `Rout`, `j`,
   `cancel`, `ov` (the only genuinely new numbers this round).
4. D4 verdict, misses first.
