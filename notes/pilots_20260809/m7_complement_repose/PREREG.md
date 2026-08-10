# PRE-REGISTRATION — MYSTERY 7: THE COMPLEMENT-COORDINATE RE-POSE (round 25)

2026-08-09. Coordinator brief; pilot appends registrations BEFORE
any computation. MANDATE: round-25a sharpened mystery 7's mechanism
— the wall is ROOT-SHARING flats (r/j -> 1), where the anticode
instrument binom(n,r)/binom(j,r) is vacuous; in SYMMETRIC-
DIFFERENCE coordinates the same instrument went from 2^836-vacuous
to 2^7.75-loose (upstream fixture) and EXACT (our M31 fixture).
Turn the lead into a tested re-pose or kill it.

## Sources (quote verbatim first)
- notes/pilots_20260809/pr_harvest/ (fixture1148 measurements; the
  SUPERSEDED calibration banner; the vertex-vs-hull caveat).
- background/nodes/l1_rootfree_rational_q_projective_packing
  round-25a addendum (the calibration of record + the lead).
- The mystery-7 members: the two FPC5 rate-half reds (+ their
  round-23/23b addenda: the cap-4 data, the trivial-owner
  concentration, the guarded-flat structure), f_global_packing_step.
- notes/pilots_20260808/t_petal_lemma/ (the slice machinery) and
  notes/pilots_20260807/mf_wall_adversary/rh_bucket.py (exact chart
  enumeration — REUSE).

## Deliverables
- (D1) THE RE-POSED INSTRUMENT, stated: for a flat of split
  locators with pairwise root-overlap >= j - s (s the symmetric-
  difference radius), the complement anticode bound
  binom(n - (j-s), ?)/binom(s, ?) — derive the correct exact form
  (the harvest showed the shape at two fixtures; write the general
  statement with its hypotheses).
- (D2) THE VERTEX-VS-HULL TEST (the registered caveat, adversarial,
  FIRST): the complement structure was measured on exhibited
  VERTICES; test whether arbitrary split members of the hull/chart
  share the root-overlap structure — at OUR fixtures (the FPC5
  rate-half cells via rh_bucket at ell = 4, 5; the M31 fixture's
  route-cut node data), measure the FULL pairwise-overlap
  distribution over all enumerated split members, not just
  extremal packings. If the distribution is bimodal or the
  overlap collapses off the vertices, the re-pose needs a
  stratified form — say which.
- (D3) THE FPC5 APPLICATION: does the complement instrument PRICE
  the measured caps (the cap-4 at m4_t2; the Bonferroni-3 at the
  LS6 cell)? Exact evaluation at the round-23/23b cells; compare
  against the measured maxima and the old vacuous ceilings.
- (D4) THE CJ2/CJ3 CHART AUDIT (the queued cheap item, same lane):
  l1_joint_core_background_johnson_bound's (CJ2)/(CJ3) is proved
  at arbitrary h — audit its chart hypotheses at M >= 5 against
  l1_fpc5_large_source_payment's cells (the round-23 probe said it
  would rescue 71 residual rows IF the hypotheses transfer; decide
  it).
- (D5) VERDICT + re-pose draft with registered falsifier, or the
  named kill.

## Rules
QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
or past line 3731 (the "ROUND 25 LAUNCHED" marker); do not read the
other round-25 pilot dirs; PASS THIS CLAUSE VERBATIM to any subagent.
RAM DISCIPLINE (binding): file-at-a-time reads; never load dag.json
whole (grep it or read node.json shards); no bulk directory reads.
COMPUTE LAW: every python3 via tools/ramguard tiny|local -- python3
(literal --) from repo root, INCLUDING file patching and JSON
peeking; checkpoint long runs to YOUR OWN dir across the walls.
DRAFT ONLY in your own dir; never edit dag.json/nodes/tools; no git
writes; no Modal; stdlib only. Name every measured functional
(CATCH-19C); 2-power grids where yours to choose (CATCH-Z6); no
shift-0 cells (CATCH-19B). Verbatim quotes with file:line. No
REPORT.md — your final message IS the report.

# PILOT REGISTRATIONS

Appended 2026-08-09 by the Opus pilot BEFORE any `python3` ran (append
made with the `Edit` tool; no interpreter involved). Sources read
first, listed in R0.

## R0. Sources read before registering (read-only, one file at a time)

notes/pilots_20260809/pr_harvest/REPORT.md; .../fixture1148.txt;
background/nodes/l1_rootfree_rational_q_projective_packing/statement.md;
background/nodes/f_global_packing_step/statement.md;
critical/nodes/l1_fpc5_ratehalf_m4_t2_payment/statement.md;
critical/nodes/l1_fpc5_ratehalf_m4_t3_split_slice_payment/statement.md;
critical/nodes/l1_fpc5_large_source_payment/statement.md;
background/nodes/l1_joint_core_background_johnson_bound/statement.md;
background/nodes/l1_m31_fixed_support_divisor_direction_cap_route_cut/statement.md;
notes/pilots_20260807/mf_wall_adversary/rh_bucket.py, ls6_probe.py;
notes/pilots_20260808/t_petal_lemma/REPORT.md, tpetal_cj3_probe.py.

## R1 (D1 DRAFT, registered in advance). THE ANNULUS ANTICODE (PC3')

I register the general form I will test, BEFORE measuring, so that a
mismatch is visible as a failed registration rather than a fitted
statement.

Base lemma (the instrument as it already stands, restated set-
theoretically): if `A_1..A_M` are distinct `a`-subsets of a
`sigma`-set with `|A_i cap A_j| <= rho` for `i != j` and
`0 <= rho < a`, then each `A_i` owns `C(a,rho+1)` distinct
`(rho+1)`-subsets and no `(rho+1)`-subset is owned twice, so
`M <= C(sigma,rho+1)/C(a,rho+1)`.

RE-POSE. Let `T_1..T_M` be the root sets (each of size `j`) of the
split members of the flat. Put

```text
K = intersect_i T_i,   U = union_i T_i,
kappa = |K|,  sigma = |U| - kappa,  a = j - kappa,
r = max_{i!=j} |T_i cap T_j|,   delta = j - r   (half the MINIMUM
                                                 symmetric difference)
```

and work in the ANNULUS `P* = U \ K` with `A_i = T_i \ K`. Then
`|A_i| = a`, `|A_i cap A_j| = |T_i cap T_j| - kappa <= a - delta`, so

```text
(PC3'-direct)  M <= C(sigma, a-delta+1) / C(a, a-delta+1),
(PC3'-comp)    M <= C(sigma, a'-delta+1) / C(a', a'-delta+1),
                    a' = sigma - a,           [complement inside P*]
(PC3'-disj)    if sigma < a + delta then the annulus complements are
               pairwise disjoint and M <= floor(sigma/a').
```

`delta` is invariant under core removal and under complementation, so
the two orientations differ ONLY in `min(a, a')`. REGISTERED
PREDICTION Q1: (PC3'-comp) beats (PC3'-direct) **iff `sigma < 2a`,
i.e. iff `|U| - kappa < 2(j - kappa)`, i.e. iff the members' union is
smaller than twice their common-free degree.** This is the exact
"regime threshold" the brief asks me to derive; everything below is a
test of it.

Consistency check I will run first (must reproduce the harvest):
upstream fixture `sigma = 514 - kappa`, `a = 479 - kappa`,
`a' = 35`, `delta = 479 - 446 = 33`, exponent `a'-delta+1 = 3`, giving
`C(514-kappa,3)/C(35,3)` = the harvest's 3437 at `kappa = 0`. M31
fixture `kappa = 4979`, `a = 1`, `delta = 1`, exponent 1, giving
`C(67449,1)/C(1,1) = 67449` = the node's own count.

REGISTERED FREE SHARPENING TO TEST (Q2): the harvest used `kappa = 0`
at the upstream fixture. If `intersect_i T_i` is nonempty there,
`C(514-kappa,3)/C(35,3)` is strictly smaller than 3437 at zero cost.
I predict `kappa >= 1` (i.e. `|union B_i| < 514`) with probability
~0.5; I will measure it.

## R2 (D2, ADVERSARIAL, RUN FIRST). THE VERTEX-VS-HULL ESCAPE TEST

The caveat of record is verbatim
`background/nodes/l1_rootfree_rational_q_projective_packing/statement.md:85-86`:
"the complement structure is a property of the exhibited VERTICES — an
arbitrary hull member need not have its roots inside U."

Two arms, both at OUR fixtures, both measuring the FULL pairwise
distribution over ALL enumerated split members:

ARM A (FPC5 rate-half m4_t2, `ell = 4, 5`): reuse
`notes/pilots_20260807/mf_wall_adversary/rh_bucket.py`
(`build_flat` + `rref_kernel` + `monic_chart` + `enumerate_split`,
exact bucketed enumeration of the whole monic guarded chart) and add
only measurement. Registered functionals (CATCH-19C):

```text
OVL_HIST_ALL  histogram of |T_i cap T_j| over ALL unordered pairs of
              distinct enumerated split members
OVL_HIST_VERT the same histogram restricted to one MAXIMUM core
              packing (rh_bucket's `maxpack` witness = "the vertices")
KCORE_ALL/VERT   |intersect T_i| over the population / the packing
UNION_ALL/VERT   |union T_i|  over the population / the packing
DELTA         j - max pairwise overlap
ANN_SIGMA, ANN_A, ANN_ACO   the R1 annulus parameters
AC_DIRECT, AC_COMP, AC_OLD  the three anticode values (AC_OLD uses the
              full pool as ambient = the "vacuous ceiling")
```

ARM B (M31 route-cut, scaled analogue): the node exhibits
`m-t+1 = 67449` members `J_a = R(X-a)` inside the SIX-dimensional
`V = span{RX, R, 1, X, X^2, X^3}` (RC1)/(RC3). Those are VERTICES.
The monic degree-`t` members of `V` are exactly
`F = R.(X+beta) + c(X)`, `deg c <= 3`, a `q^5` family; the exhibited
ones are `c = 0`. I will enumerate ALL of them that split on `S` in a
scaled analogue (same shape, small `q`), by last-coordinate bucketing
on `c_0`, and count `M31_EXTRA = NSPLIT - (m-t+1)`. Scale is preserved
by keeping `m >= 2t-4` (the counting condition under which a `c != 0`
member is not excluded outright: such a member meets `R0` in at most
`deg c <= 3` points, so it needs `t-3` roots in `S \ R0`).

KILL CRITERION registered in advance: if `M31_EXTRA > 0` in any
configuration, the round-25a addendum's "at our fixture the complement
count `m-(t-1) = 67449` is the node's own count EXACTLY (2^0)" is not
merely unproved — the quantity it is being compared against is a
LOWER bound on the truth, so "looseness 2^0" is unsupported and could
even be a violated bound. If `M31_EXTRA = 0` everywhere, the vertex
structure survives the hull test at our fixture and I say so.

## R3. PER-CELL PREDICTIONS (registered before running)

- **P1** (ARM A, `ell = 4, 5`): max pairwise overlap over the FULL
  population equals the round-23 sharpened cap `ell-3` (so 1 at
  `ell=4`, 2 at `ell=5`), and the MODE of `OVL_HIST_ALL` is 0, with
  `>= 60%` of all pairs at overlap 0.
- **P2**: `KCORE_ALL = 0` in `>= 15/16` configs at both `ell` (no
  common core in the hull) — hence `kappa = 0` and the annulus
  reduction buys nothing at our cells.
- **P3**: `ANN_ACO > ANN_A` in `100%` of configs (i.e. `sigma > 2a`),
  so by Q1 the complement orientation is STRICTLY WORSE than the
  direct one at every rate-half cell. Parametrically: the ambient is
  the core `|C| = 5ell-5` and `j = d = 2ell-3`, so
  `sigma/a -> 2.5 > 2` for all `ell`, and `5ell-5 < 2(2ell-3)`
  is `ell < -1`, i.e. NEVER.
- **P4** (the vertex/hull separation): `mean(OVL_HIST_VERT) >
  mean(OVL_HIST_ALL)` at both `ell`; concretely at `ell=4` a 4-packing
  of 5-sets into `N=15` points forces total pairwise overlap `>= 5`.
  If instead the packing members are pairwise disjoint I will report
  the prediction as REFUTED.
- **P5** (ARM B): `M31_EXTRA = 0` in `>= 7/8` scaled draws.
- **P6** (D3, m4_t2): the re-posed instrument does NOT price the cap-4.
  Specifically `AC_DIRECT` at the official cell grows like
  `2^{1.61 ell}` (matching the node's own recorded
  `statement.md:129-131` sharpening "improves (RH0b) from
  `2^{2.755 ell}` to `2^{1.61 ell}`") while the measured maximum is 4,
  and `AC_COMP >= AC_DIRECT` for every `ell >= 4`.
- **P7** (D3, LS6): at the round-23 off-tail cell `(ell,b,a)=(4,1,1)`,
  `q=101`, neither orientation reaches the measured max core packing
  3; the proved Bonferroni-3 stays the best instrument. I predict
  `AC_DIRECT > 3` and `AC_COMP > AC_DIRECT`.
- **P8** (hard law 5 subtraction, registered as a suspicion to test):
  the COMMON-CORE orientation of (PC3') is ALREADY deployed in our own
  repo as the fixed-owner bound
  `critical/nodes/l1_fpc5_ratehalf_m4_t3_split_slice_payment/statement.md:113-116`
  (`|F_G| <= binom(2ell+a+b-2,h-g+1)/binom(2ell-a-g,h-g+1)`, i.e. the
  same instrument after removing the common divisor `G`). If so the
  round-25a "own-repo subtraction: complement coordinates appear once
  ... and never against the packing instrument" is incomplete, and the
  measured trivial-owner concentration (52.4% at `g=0`) is already the
  measured failure of the re-pose.
- **P9** (D4, CJ2/CJ3 at `M >= 5`): I predict the hypotheses DO
  transfer (as `(JB3)`'s did), but that a *second* arithmetic
  side-condition beyond the round-24 `u <= b` correction binds and
  cuts the 71 rows further. Confidence 0.6 / 0.4. The hypotheses I
  will audit one by one: (H1) "one maximal-sunflower source chart";
  (H2) "one exact labelled petal support `X` of size `h`" with
  `h = t*ell` at `M >= 5`; (H3) `s = h-d >= 0` and `u = ell-s` with
  `0 <= u <= b` (the round-24 catch); (H4) `r = 2d-h >= 0`;
  (H5) `b = ell-g > 0` vs the large-source `b = S - M*ell`
  identification actually used by `tpetal_cj3_probe.py:80-81` — a
  NOTATION COLLISION I flag in advance: `(CJ1)` defines `b = ell-g`
  (a per-petal background), the probe used `b = S - M*ell` (a global
  background block). If those are different objects the 71-row rescue
  is priced with the wrong `b`.

## R4. Escapes and what would make me abandon the re-pose

- E1: if `OVL_HIST_ALL` at our cells is BIMODAL with a high-overlap
  mode at `>= j - O(1)`, the re-pose needs a STRATIFIED form (bound
  each overlap stratum separately and sum) and I will state it.
- E2: if `KCORE_ALL > 0` systematically, the common-core orientation
  is live at our cells and P3/P6 are wrong.
- E3: if `M31_EXTRA > 0`, the "EXACT at our fixture" calibration is
  withdrawn (see R2 kill criterion).
- E4: if at any FPC5 cell `AC_COMP < AC_DIRECT`, Q1's threshold is
  wrong and the whole R1 statement is mis-derived.

## R5. Compute plan (grids are 2-power where mine to choose, CATCH-Z6)

`ell in {4,5}` (fixed by the node, not mine); `q` primes from the
already-replayed round-23b set `{97,193}` plus `101` for the LS6 cell
(fixed by the prior runs, not mine); configuration counts `16`, `32`
(2-power, mine); M31 scaled draws `8` (2-power, mine); no shift-0
cells. All artifacts in this pilot dir only.
