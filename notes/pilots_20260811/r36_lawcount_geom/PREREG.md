# PREREG — r36_lawcount_geom (round 36)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r35_rout_layer_a/REPORT.md` (round 35)
2. `background/nodes/rate_half_layer_a_saturation_count_route_fence/statement.md` (Codex, wave 59 — PROVED)

## Mandate

THE GEOMETRY-CONSTRAINED (LA-W COUNT) RANK THEOREM — round 36's
anchor #1, RE-POSED after Codex's fence. Round 35 proved layer A
kills the m=2 and m=3 W-layer witnesses from their inside-W
incidences alone (measured nullity 0, both fields, completion-
independent) and posed (LA-W COUNT): at a = 7m-1 with W saturated,
the a*m incidence rows on the (rho+1)(m+1) biform coefficients
have FULL RANK for m >= 2 (excess 3m^2-5m, negative only at m=1).
Codex then PROVED the bare form FALSE within hours (anchor 2):
Q = Z^2-X^4 on 13 saturated points of mu_16 has nullity 4 — the
count alone promotes nothing. The fence's own scope note names
what it does NOT touch: configurations where W is the union of
two degree-rho slope supports with the split-biform /
support-intersection / Hankel-source constraints. YOUR JOB: prove
the rank theorem WITH the endpoint geometry — or map exactly how
much geometry the fence family survives. A theorem here closes
every saturated a = 7m-1 configuration at once, unconditionally,
making layer A a standalone exclusion instrument.

## Deliverables

**D1 — THE HYPOTHESIS LADDER.** Order the banked constraints from
weakest to strongest: (H1) W = S_g u S_h, two degree-rho slope
supports, |S_g ^ S_h| = m-1; (H2) the (OV) pair caps; (H3) the
type-2 fibre structure ((BIV-CURVE)-shaped A_x); (H4) the
Hankel-source constraint. For each rung: does the fence family
(or ANY nullity > 0 family) survive? Build the ablation ladder —
the fence generalizes (A(X)*Q kernels for other invariant Q; how
big is the family and which rung kills it?). The MINIMAL
hypothesis set that forces nullity 0 is the deliverable even if
the proof does not land.

**D2 — THE PROOF ATTEMPT.** With the minimal set from D1: the
rank statement. Instruments in scope: the RNC node's machinery
(the m+1 independent forms, separation rank), the measured kills
at m=2 (26 rows) and m=3 (60 rows) as data, the m=1 sign change
(nullity exactly 2, 16/16 — any proof must produce it), and the
fence as the MANDATORY regression (your proof must FAIL on the
fence's configuration; identify exactly which hypothesis it uses
where). A proof for m=2 alone is already a bank.

**D3 — THE FENCE FAMILY.** Classify the nullity > 0 saturated
configurations at excess > 0: the fence takes W inside a proper
subgroup with Q an invariant biform — is EVERY counterexample of
this invariant/subgroup type? A structure theorem for the failure
locus is the dual route to D2 and may be cheaper.

**D4 — VERDICT.** Theorem / partial (named minimal hypotheses,
named gap) / the failure-locus structure; misses first;
cross-pilot flag (do NOT read siblings) for anything bearing on
the realizability lane.

## Blind priors to register

P(the rank theorem lands this round at m=2), P(at general m >= 2),
P(H1 alone suffices), P(the fence family is exactly the
invariant/subgroup type), P(the m=1 sign emerges naturally from
the proof).

---

## Pilot registrations

Written with the Edit tool after reading EXACTLY the two named
anchors (`r35_rout_layer_a/REPORT.md`,
`background/nodes/rate_half_layer_a_saturation_count_route_fence/statement.md`)
and BEFORE any other read, any grep, any `ls`, and any interpreter
invocation. Everything below is derived from those two files alone.
No addenda will be made after execution starts; registration errors
will be reported as misses, not edited.

### R0 — notation fixed from the anchors alone

`m >= 1`; `N = 16m`, `rho = 4m-1`, `T = rho+2 = 4m+1`, `D = mu_N`,
`W subset D` with `a = |W| = 7m-1`, `Gamma` the slope set with
`|Gamma| = T`. Layer-A biform `Q(Z,X) = sum_{i=0..m} P_i(X) Z^i`,
`deg P_i <= rho`, so `(m+1)(rho+1) = 4m(m+1)` unknowns. Saturation:
`A_x := {gamma in Gamma : (gamma,x) in I}` has `|A_x| = m` for every
`x in W`, so `|I| = am = (7m-1)m` and the count excess is
`am - 4m(m+1) = 3m^2-5m` (anchor 1 `REPORT.md:186-190`, anchor 2
`statement.md:58`). `E_I` is the `|I| x 4m(m+1)` evaluation matrix
`gamma^i x^t`. `sigma_W(X) = prod_{x in W}(X-x)`, `deg = 7m-1`.

### R1 — BLIND PRIORS (the five demanded, plus auxiliaries)

- **R1.1** `P(the rank theorem — nullity 0 under a named geometric
  hypothesis set — lands this round at m=2) = 0.22`.
- **R1.2** `P(it lands at general m >= 2 this round) = 0.10`.
- **R1.3** `P(H1 alone suffices to force nullity 0) = 0.25`. I lean
  NO: H1 constrains only 2 of the `4m+1` slopes.
- **R1.4** `P(the fence family is EXACTLY the invariant/subgroup
  type) = 0.15`. I lean NO (see R2.2/R2.3: I expect a strictly
  larger "low-Pade-complexity" family).
- **R1.5** `P(the m=1 sign change emerges naturally from the proof,
  i.e. the proof's mechanism itself produces nullity exactly 2 at
  m=1) = 0.55`.
- **R1 aux a** `P(the fence generalizes to an infinite family, one
  member for every m >= 2) = 0.80`.
- **R1 aux b** `P(the minimal hypothesis set I end with is strictly
  larger than {H1}) = 0.75`.
- **R1 aux c** `P(I ship a partial with named gap rather than a
  theorem) = 0.70`.
- **R1 aux d** `P(at least one of my "new" objects subtracts to a
  banked/PROVED node) = 0.85` (round 35 subtracted eleven).
- **R1 aux e** `P(a computational search finds a nullity>0
  configuration satisfying H1 at m=2) = 0.35`.

### R2 — FALSIFIABLE DERIVATIONS, committed in advance

These are derived now, from the anchors only, before any
computation. Each is stated so it can be refuted.

- **R2.1 (LA-PADE reduction).** Claim: for `x in W`, `Q(Z,x)` is a
  degree-`<= m` polynomial in `Z` vanishing on the `m` distinct
  points `A_x`, hence `Q(Z,x) = P_m(x) prod_{gamma in A_x}(Z-gamma)`
  and therefore
  ```text
  P_{m-j}(x) = (-1)^j e_j(A_x) P_m(x)   for all x in W, j=1..m.
  ```
  Sub-claim: `P_m == 0` forces `Q == 0` (each `P_i` would vanish on
  `7m-1 > rho = 4m-1` points). Hence with `E_j` the interpolant of
  `x -> e_j(A_x)` on `W`,
  ```text
  nullity(E_I) = dim intersect_{j=1..m} K_j,
  K_j = { P in F[X]_{<=rho} : deg( E_j P mod sigma_W ) <= rho }.
  ```
  Each `K_j` is the kernel of a `(3m-1) x 4m` Hankel-type matrix
  (Pade/Kronecker), so `dim K_j >= 4m-(3m-1) = m+1`, and the
  expected intersection dimension is
  `(m+1) - (m-1)(4m-(m+1)) = -(3m^2-5m)`, reproducing the excess.
  `P(R2.1 verifies computationally on the fence and on the m=1
  witnesses) = 0.85`.
- **R2.2 (exact nullity formula).** With `(n_j,p_j)` a reduced basis
  of the Pade lattice `{(n,p) : n == E_j p mod sigma_W}` of degrees
  `d_j <= d'_j`, `d_j + d'_j = 7m-1`:
  ```text
  dim K_j = max(0, 4m-d_j) + max(0, 4m-d'_j),
  ```
  and in the unbalanced regime (`d_j <= 3m-1` for all j)
  `K_j = p_j * F[X]_{<= 4m-1-d_j}`, whence
  ```text
  nullity = max(0, 4m - deg lcm(p_1..p_m) - max_j delta_j),
  delta_j = max(0, deg n_j - deg p_j).
  ```
  **Mandatory fence regression, computed in advance:** at the fence
  (`statement.md:25,37`) `A_x = {x^2, -x^2}`, so `e_1(A_x) = 0` and
  `e_2(A_x) = -x^4`; therefore `E_1 = 0` (`p_1=1, n_1=0, delta_1=0`),
  `E_2 = -X^4` (`p_2=1, n_2=-X^4, delta_2=4`), `lcm = 1`, and
  `nullity = 8-0-4 = 4` — exactly `(LAW3)` (`statement.md:52`).
  **Mandatory m=1 regression, computed in advance:** `m=1` gives
  `4m=4`, `deg sigma_W = 6`, generic `d_1 = d'_1 = 3`, so
  `dim K_1 = (4-3)+(4-3) = 2` — exactly the banked nullity 2, with
  NO special structure required. `P(both regressions verify) = 0.85`.
  If either fails, R2.1/R2.2 are refuted and I say so first.
- **R2.3 (the fence generalizes to EVERY m — an infinite family).**
  Take `Q_0 = Z^m - X^{2m}` (bidegree `(m,2m)`, `2m <= rho` for
  `m >= 1`). The map `x -> x^{2m}` on `mu_{16m}` has image `mu_8`
  and fibres of size `2m`. Choose 4 fibre values, giving `8m`
  points; take `W` = any `7m-1 <= 8m` of them; take `Gamma` = the
  `4·m` m-th roots of the 4 values, plus 1 spare slope `eta` with
  `eta^m` outside the 4 values, so `|Gamma| = 4m+1 = T` exactly.
  Then every `x in W` is saturated by exactly `m` slopes
  (`gamma = omega x^2`, `omega in mu_m`), `|S_gamma| <= 2m <= rho`,
  and `ker` contains `A(X)Q_0` with `deg A <= rho-2m = 2m-1`:
  ```text
  nullity >= 2m   for every m >= 2.
  ```
  At `m=2` this is `Q_0 = Z^2-X^4`, `W subset mu_16`, `Gamma = mu_8
  + eta`, `nullity >= 4` — **it reproduces Codex's fence exactly**
  (`statement.md:12-13,25,37,52`), which is the calibration. Predicted
  first new instance: `m=3`, `Q_0 = Z^3-X^6`, `D = mu_48`, `W` = 20
  points in 4 fibres of `x -> x^6`, `|Gamma| = 13`, **nullity >= 6**.
  `P(the m=3 instance verifies at nullity exactly 6, two fields) =
  0.85`. If it verifies, the bare `(LA-W COUNT)` is dead at EVERY
  `m >= 2`, not only at `m=2`.
- **R2.4 (H1 kills the binomial/subgroup family, by the banked
  gcd).** In any `Q_0 = Z^m - cX^k` family the supports have
  `|S_gamma| <= gcd(k,16m)`. H1 demands two supports of size
  `rho = 4m-1`, and `gcd(4m-1,16m) = gcd(4m-1,4) = 1` since `4m-1`
  is odd. So no binomial-invariant fence can satisfy H1.
  `P(this argument survives) = 0.80`. NOTE IN ADVANCE: this gcd is
  a **banked PROVED** fact (round 35 CATCH-24A row 3 cites
  `rate_half_type2_fr_quartic_coset_biform_lift_obstruction/proof.md:66-72`);
  I will claim only the application, never the arithmetic.
- **R2.5 (the failure locus is NOT the invariant/subgroup type).**
  Predicted structure theorem: `nullity > 0` iff the slope map has
  low Pade complexity in the sense of R2.2 — in particular ANY
  `Q = Z^m - f_1(X)Z^{m-1} + ... + (-1)^m f_m(X)` with
  `D := max_j deg f_j <= rho` and with its `W`-fibres landing in only
  `4m+1` slopes gives `nullity >= 4m-D`. The counting window is
  `ceil((7m^2-m)/(4m+1)) <= D <= 4m-1`, non-empty for every
  `m >= 1`, so I expect NON-subgroup members. `P(I exhibit a
  nullity>0 saturated configuration at m=2 whose `Q` is NOT of the
  form `A(X)(Z^m-cX^k)` and whose slope set is not a coset of a
  subgroup) = 0.45`.
- **R2.6 (H1 forces nullity <= 1 in the polynomial regime).** If
  `p_j = 1` for all `j` (polynomial slope map) then
  `nullity = 4m - D`; H1 needs a support of size `rho = 4m-1 <= D`,
  so `D = 4m-1` and `nullity <= 1`. `P = 0.70`.
- **R2.7 (zero-power in advance — declared, not to be tried).**
  Weil/Chebotarev and any rational-point-count instrument is vacuous
  at official scale (`N = 16m` vs `sqrt(q)`, `q > 2^167`); I will not
  run them and will not report them. Value-level `mu_N` conditions
  are exact but cost `~q^{-c}` against a `Theta(m^2)`-dimensional
  parameter space (round 35 R2.6, confirmed there): not tried.

### R3 — MISS-2 GUARD (mean-vs-max), mandatory

Round 35's MISS 2 was a **maximum read off a sample and reported as
a bound** (`REPORT.md:32`, bank 1's "`Rout <= 3`" contradicted by its
own `maxRout = 4`). Registered guards:

- **R3(a) NO SAMPLED MAXIMUM IS EVER A BOUND.** Every extremal claim
  ("nullity is always 0", "no counterexample exists", "the maximum
  support is `2m`") is reported with (i) its denominator, (ii)
  whether the enumeration was exhaustive or sampled, (iii) the
  running maximum against sample size when sampled. A *mean* over a
  sample is never used to support a *max* claim and vice versa: I
  will print the **full distribution** (nullity histogram with
  counts) wherever I print any nullity summary, exactly so a single
  outlier cannot be lost in a mean.
- **R3(b) COUNTING EXCESS NEVER CERTIFIES RANK.** `3m^2-5m > 0` is
  the refuted implication (anchor 2 is precisely its refutation).
  No rank/nullity conclusion in this report will be drawn from a
  dimension count; ranks are measured or proved.
- **R3(c) DISTRIBUTION, NOT BEST CASE.** For every hypothesis rung I
  report the nullity distribution over the whole ablation sample,
  not the most favourable configuration.
- **R3(d) TWO-FIELD.** Every structural claim is confirmed on two
  fields (`q = 97` and `q = 193`, both `= 1 mod 32` and `mod 48`, so
  `mu_32` and `mu_48` are available). Single-field results are
  labelled single-field in the misses section.

### R4 — ZERO-POWER PRE-DECLARATIONS

1. **`m=1` has zero power for the rank theorem**: the excess is
   `-2`, nullity 2 is forced by the count, so no `m=1` datum can
   support any `m >= 2` rank claim. It is a regression only.
2. **A failed search is not a proof.** If I search for an
   H1-satisfying nullity>0 configuration and find none, that is
   zero-power unless the search is exhaustive over a stated finite
   set; I will state the set and its size, or declare zero power.
3. **Nullity 0 on structured objects is evidence about those
   objects only** (round 35 zero-power 6); it never shows
   non-existence of a counterexample.
4. **Any "the fence family is exactly X" claim is zero-power in the
   direction of exhaustiveness** unless I enumerate all saturated
   configurations at some `(m,q)`, which I expect to be infeasible
   for `m >= 2`; if I cannot, I report the classification as a
   theorem about a *named* subfamily plus an unclassified remainder.
5. **All results are `(SAT3)`-conditional / hypothesis-class
   conditional**: round 35 zero-power 1-2 record that the `T=rho+2`
   class may be empty at `m >= 2`, in which case every statement
   here — the theorem AND the fence — is vacuous. This does not
   change which is true, but it caps the value of both.
6. **No claim about realizability of any configuration in the
   endpoint lane** is made from a layer-A construction; the fence
   family is a layer-A object, not a realized `(SAT3)` pencil.
7. **Field-characteristic caveat pre-declared**: the generalized
   fence (R2.3) needs `mu_{16m} subset F` and `char` prime to `m`;
   at `m` divisible by `char` the `m` roots collide and saturation
   fails. Declared before measuring.

### R5 — SUBTRACTION PLAN (CATCH-24A), before any novelty claim

Own-repo greps under `critical/` and `background/` (never
`dag.json`, with the full `--exclude-dir` set) for, at minimum:
`Pade`/`Padé`/`pade`, `Hankel kernel`, `Kronecker`, `minimal
denominator`, `rational interpolation`, `Cauchy interpolation`,
`elementary symmetric`, `e_j(A_x)`, `slope map`, `lcm`, `LA-W`,
`LA-W COUNT`, `3m^2-5m` and `3m^2 - 5m`, `Z^2-X^4`, `Z^m`,
`binomial biform`, `invariant biform`, `subgroup`, `coset`,
`gcd(4m-1,16m)`, `saturation count`, `fence`, `nullity`,
`separation rank`, `rational normal curve`, `split biform`,
`support intersection`, `OV`, `Hankel-source`, plus the hyphenated
and infixed variants (`Pade-Hankel`, `low-complexity`,
`slope-map`, `Hankel source`, `split-biform`,
`support-intersection`) that round 34's catch demands. Any object
that lands is reported as BANKED, with `file:line`, before I call
anything new.

### R6 — EXPECTED MISSES (registered so they cannot be spun)

(i) at least one ramguard wall/OOM failure (round 35 had four);
(ii) my `e_j`/`E_j` convention may differ in sign from the banked
`Q_Z(x)` convention — I will cross-check against the fence's own
`(LAW3)` before believing any number; (iii) I may misidentify which
banked node states H2/H3/H4 and quote the wrong hypothesis — I will
quote `file:line` for each rung; (iv) I expect to over-claim novelty
on the Pade/Hankel reduction and be subtracted by the Hankel/apolar
machinery already in the endpoint nodes; (v) I may fail to build the
`m=3` generalized fence inside the wall.

### R7 — EXECUTION ORDER

D1 (read the banked hypothesis statements; build the ladder) -> D2
(the proof attempt under the minimal set, with the fence as
mandatory regression) -> D3 (the failure-locus classification) ->
D4 (verdict). Registrations closed.
