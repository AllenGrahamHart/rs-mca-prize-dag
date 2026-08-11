# PREREG — r37_share3_gap (round 37)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r36_m4_nonsplit/REPORT.md` (round 36)
2. `notes/pilots_20260811/r34_bivcurve_m34/REPORT.md` (round 34)

## Mandate

THE ONE-COINCIDENCE GAP. Round 36's (SHARE3-4) class reached the
full 8-of-8 target at m = 4 — the first class ever — and missed
the slope budget by ONE (|slopes| = 14 vs 13 required at q=193;
15 vs 13 at q=257; 40000 ALLOC draws per field). The existence
mechanism is exactly understood: the 3-sharing pencils are
CONSTANT-NORM (fixed root-product costs 1/N on mu_N, decay ~q^-7,
threshold ~690 — refuting the naive q^-12 by 3400x). YOUR JOB:
close the gap or harden it. A 13-slope configuration would be an
m = 4 (BIV-CURVE) witness candidate — and then the FULL round-34
pipeline applies: build G, complete outside W, run the bivariate
system on bank-2's own verifier. That would be a major board
event; treat it as the round's prize and the hardening as the
honest default.

## Deliverables

**D1 — THE FULL CONSTANT-NORM CENSUS.** Round 36's exhaustive
censuses covered the constant-(e1,e3) and constant-e3
SUB-families only (its ZP-3), with a sampled base-triple scan for
general lines. Do better: (a) more fields in the live window
(the mechanism says the supply peaks at moderate q — map the
window 97 <= q <= ~690 densely); (b) the FULL constant-norm
family (Delta with zero constant term is one linear condition on
lines — enumerate it exhaustively where affordable, not by
sub-family); (c) per-pencil, the slope-count distribution under
ALLOC (not just the max) — where does the 13-slope tail actually
sit? The registered arithmetic (demand 11, supply band 9-12)
says the gap is at the edge of the distribution, not beyond it.

**D2 — THE STRUCTURED SLOPE-MERGE.** The shortfall is one
coincidence = one extra pair of fibres sharing a chi-slope. The
constant-norm mechanism already forces one algebraic relation
among the fibre values — derive whether a SECOND relation
(constant e_1 too? a subgroup-structured base triple? w
equivariant under a mu_2 inside mu_64?) can be imposed within the
19 parameters, and what it costs. This is the exact analogue of
round 36's own finding that the finer family (constant-e3 vs
constant-(e1,e3)) mattered — go one level finer, guided by which
coincidences the near-miss draws actually realize (read the data:
WHICH slope pairs merge in the |slopes| = 14 draws?).

**D3 — THE PIPELINE ON ANY 13-SLOPE HIT (or the fences on none).**
If a 13-slope configuration lands: mu(x)-at-middles check (round
36's MISS 10 — never verified), per-side split on actual points,
build G explicitly ((SHARE3-4) form: U~(w)Z^3 - E~_1(w)Z^2 +
E~_2(w)Z - E~_3(w)), outside completion, bivariate system via
bank 2's biv_core.py (copy in; AUDIT ITS OUTPUT PATHS first —
the round-35 breach was exactly this file), full incidence table,
two fields. If none lands: the split sub-case fence (round 36's
R1.13, deficit 5 — make it a verified statement), the sporadic
(non-factoring) sharing residual priced or fenced, and the
honest scope table for the class.

**D4 — VERDICT.** The (BIV-CURVE) m-boundary of record; misses
first; cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(a 13-slope configuration this round), P(it survives the full
pipeline => m=4 witness), P(the second-relation route is the one
that lands), P(the density window map matches ~q^-7), expected
best |slopes| (a number).

---

## Pilot registrations

Appended with the Edit tool after reading EXACTLY the two named
anchors (`r36_m4_nonsplit/REPORT.md`, `r34_bivcurve_m34/REPORT.md`)
and BEFORE any other read, any grep, any `ls`, and any interpreter
invocation. Everything below is derived by hand from the two
anchors' reported numbers plus elementary algebra. No search has
been run.

### R0 — notation carried from the anchors (not re-derived)

`m=4, N=16m=64, rho=4m-1=15, R=8m=32, e=m=4, T=rho+2=17, T_1=2,
T_2=rho=15, a=7m-1=27, delta=m-1=3`; `|S_g ^ S_h| = m-1 = 3`,
`|S_g D S_h| = 6m = 24`. `(SHARE3-4)`:
`G(Z,x) = U~(w)Z^3 - E~_1(w)Z^2 + E~_2(w)Z - E~_3(w)`, `deg w = 3`
on `mu_64`, `deg_w U~,E~_i <= 3`, 19 parameters (7 for `w` + 15 for
`Psi~` projectively - 3 for `PGL_2` on the `w`-line). Anchor-1
budget: `d_gamma <= 2`, pair multiplicity 1, forced `s = 13`.

### R1 — the gap, restated exactly (falsifiable arithmetic)

**R1.1.** 8 complete fibres x 3 type-2 slopes = **24 slot-incidences**.
With `d_gamma <= 2` (from `X'_gamma = 3 d_gamma <= 2m-2 = 6`), a
configuration with `s` distinct slopes has `n_1 + 2 n_2 = 24`,
`s = n_1 + n_2 = 24 - n_2`. So **`s = 24 - (#merges)`**, i.e.
`|slopes| = 13` <=> **exactly 11 merges**, and `|slopes| = 14`
(anchor 1's achieved ceiling) <=> exactly 10 merges. **The whole
round is ONE extra merge.** `P(this restatement is exact) = 0.93`.

**R1.2.** Consequently the merge graph `H` on the 8 fibres has 11
edges, is **simple** (pair multiplicity 1 = linearity), has max
degree 3 (a fibre has only 3 slopes) and degree sum 22, forcing
degree sequence **(3,3,3,3,3,3,2,2)**; with anchor 1's bipartite
`4+4` per-side balance this is **exactly `K_{4,4}` minus a perfect
matching minus one further edge**, degrees `(3,3,3,2 | 3,3,3,2)`.
Two fibres carry one *private* slope each; the other six are fully
shared. `P = 0.88`. (Anchor 1 states the 12-edge/`s=13` certificate
at `r36 REPORT.md:169`; I register the 11-edge form as the exact
target and predict it matches.)

### R2 — the structure theorem I commit to BEFORE any search

**R2.1 (the slope curve).** `R(gamma,t) := U~(t)gamma^3 -
E~_1(t)gamma^2 + E~_2(t)gamma - E~_3(t)` is a **bidegree-(3,3)
form**; the slope triple of the fibre over `t_i` is the root set of
`R(.,t_i)`, and a merge is a common root. Equivalently the map
`gamma |-> [R(gamma,.)] in P(F_q[t]_{<=3}) = P^3` is a **twisted
cubic `C`**, and fibre `i` is the hyperplane `H_i = {P : P(t_i)=0}`.
A merge between `i,j` <=> `C` meets the **line**
`l_ij = H_i ^ H_j = (t-t_i)(t-t_j)F_q[t]_{<=1}`. `P = 0.80`.

**R2.2 (the dimension count — THE central registered number).**
`Psi~` lives in `P^15`; "meets a given line" is codimension 1 on
twisted cubics. **11 merges = 11 conditions, so the 13-slope
variety has expected dimension `15 - 11 = 4` over `F_qbar`,
NON-EMPTY.** Cross-check in intrinsic terms: twisted cubics in
`P^3` form a 12-dim family, `12 - 11 = 1`, plus `PGL_2` on the
`gamma`-line (3, since slope values carry no arithmetic
confinement) `= 4`. **I therefore register that the one-coincidence
gap is NOT a dimension obstruction.** `P(the two counts agree at 4)
= 0.85`. Classical anchor for the same family: the number of
twisted cubics meeting **12** general lines is finite (Schubert's
80160), so 12 merges is the 0-dimensional case and 11 is a curve.

**R2.3 (the affine-combination relation — my main derived tool).**
Fix `U~`; put `v_i = c_i U~(t_i)`, `c_i = 1/W'(t_i)`,
`W = prod_k (t-t_k)` over the 8 selected fibre values. Then
`e_j^{(i)} = E~_j(t_i)/U~(t_i)` and interpolation on any 4 of the 8
nodes gives, for `A = {t_1..t_4}` and `j in B = {t_5..t_8}`,
> **`f_j = sum_{i in A} lambda_ji f_i` with
> `lambda_ji = L_i(t_j) U~(t_i)/U~(t_j)` and `sum_i lambda_ji = 1`,**
where `f_i(Z)` is the monic slope cubic of fibre `i` and `L_i` is
the Lagrange basis on the 4 `A`-nodes. **The four `A`-side slope
cubics are completely free (12 parameters) and determine the four
`B`-side cubics linearly.** `P(the row-sum-1 identity holds) =
0.90`; `P(the whole relation as stated) = 0.75`.

**R2.4 (the solve that R2.3 unlocks).** Because `f_j - lambda_ji f_i
= sum_{k != i} lambda_jk f_k` and a merge on edge `(i,j)` is a
common root `r` of `f_i` and `f_j`, the merge condition is
**`(sum_{k != i} lambda_jk f_k)(r) = 0`**, i.e. *the shared slope is
a root of a cubic that does not involve `f_i` at all*. Hence: given
three of the four `A`-triples, the fourth is **determined** (its
shared roots are roots of explicit cubics), and the residual system
is 9 conditions on 10 parameters (`T_1,T_2,T_3` and the free
private slope `alpha`) — **dimension 1**. I register a
**block-coordinate-descent / fixed-point search** on
`(T_1,T_2,T_3,alpha)` as the round's instrument, in place of anchor
1's ALLOC random draws. `P(this instrument beats ALLOC's 10 merges)
= 0.55`.

**R2.5 (why ALLOC stalled at 10 — registered diagnosis).** ALLOC
prescribes **15 incidences** against 15 projective parameters,
which buys at most `floor(15/2) = 7` merges by construction; the
other 3 were free coincidences. Random free supply is
`C(8,2) * 3*3/q = 252/q` = **1.31 at `q=193`, 0.98 at `q=257`**. So
`7 + ~1.3 ~ 8.3` expected and 10 observed. **The instrument, not
the geometry, is what capped the round at 14 slopes.** `P = 0.60`.

### R3 — the second-relation route (D2), priced in advance

**R3.1 (group equivariance is capped, and the cap is 4).** If `w`
(or `Psi~`) is equivariant under a `mu_k` acting on the fibre-value
line with `Psi~ o nu = tau o Psi~`, a slope fixed by `tau` lies in
**every** triple of its `nu`-orbit, so `d_gamma = |orbit|`. The cap
`d <= 2` therefore forbids every orbit of size `>= 3`, and a `mu_2`
gives at most **one merge per orbit-pair = 4 merges** against the
11 required. **Registered derivation: no group symmetry inside
`mu_64` can close the gap; symmetry buys at most 4 of the 11
merges.** `P = 0.80`. This is my answer, in advance, to the brief's
"`w` equivariant under a `mu_2` inside `mu_64`?".

**R3.2 (constant `e_1` too).** Constant-norm is `e_3` of the *point*
triples constant (one linear condition on lines in `P^3`);
additionally constant `e_1` is a **second** linear condition, so the
constant-`(e_1,e_3)` family is codimension 2 in the line space.
Anchor 1 already measured it as *worse* (`q=257`: 0 pencils with
`>= 9` fibres in constant-`(e1,e3)` vs 731 in constant-`e3`,
`r36 REPORT.md:66,70`). I register in advance that **the second
point-side relation reduces supply and does not merge slopes**,
because point-side symmetric functions do not act on the slope
line. `P(constant-e_1 helps) = 0.10`.

**R3.3 (the route I actually rate highest).** The 11 merges are
bought **algebraically, not symmetrically** — by solving R2.4's
fixed-point system. `P(the winning route is algebraic-solve rather
than extra-symmetry) = 0.70`.

**R3.4 (the degenerate-fibre side door, priced).** If one fibre's
slope cubic has a **double root**, the slot count drops 24 -> 23 and
`s <= 13` needs only 10 merges — exactly what anchor 1 already
achieved. Cost: the 3 points of that fibre have `|A_x| = m-1`, so
`sum_x (m-d_x) >= 3`, which needs `(SAT4)`'s `1+O` with `O >= 2`.
**Registered as a candidate loophole to be priced, not used, unless
`O >= 2` is verified legal from the banked statement.** `P(it is
legal) = 0.20`; `P(I use it as the round's headline) = 0.05`.

### R4 — D1 census predictions

**R4.1 (the window is NOT dense — a hard congruence fence).**
`mu_64 subset F_q^*` requires **`q = 1 mod 64`**. In `97 <= q <= 690`
the admissible prime fields are **exactly {193, 257, 449, 577, 641}
— five, not a dense window**; no prime power in range helps
(`31^2 = 961 > 690`). I register in advance that the brief's
"densely" is arithmetically impossible and that 641 is **the one
field anchor 1 never ran**. `P(exactly these five) = 0.90`.

**R4.2 (the density map).** With anchor 1's four-field max-fibre
sequence `12, 9, 9, 7` at `q = 193,257,449,577`
(`r36 REPORT.md:193-196`) I predict for `q = 641`: **max complete
fibres in `{6,7,8}`, point estimate 7**, and `P(>= 8 at q=641) =
0.35`. For the exponent: fitting `log(per-base 8-line rate)` vs
`log q` over the five fields, I predict the slope lies in
**`[-9,-5]`** (the registered `~q^-7`), `P = 0.45`; and I predict
the **supply does NOT peak at moderate `q` but decreases
monotonically from 193**, `P = 0.70` — i.e. I expect to *contradict*
the brief's "supply peaks at moderate q" phrasing.

**R4.3 (the full constant-norm family).** "`Delta` has zero constant
term" is **one linear condition on lines in `P^3`**, so the full
constant-norm family is a hyperplane section of the line space, and
it strictly contains both of anchor 1's sub-families. I predict the
full family's max complete-fibre count **equals or exceeds** the
constant-`e_3` sub-family's at every field, `P = 0.95` (containment
is trivial; the content is whether it is *strictly* larger:
`P(strictly larger at q=193) = 0.55`).

**R4.4 (the slope-count distribution — the brief's (c)).** I predict
the per-draw `|slopes|` distribution at `k=8` under ALLOC-style
draws is **sharply peaked at 16-18 with a thin left tail**, that the
observed minimum over 40000 draws is 14 (anchor 1's ceiling), and
that the empirical tail is **geometric-like with ratio ~3-6 per
slope**, so 13 sits `~3-6x` beyond 14 in frequency and is
**reachable by an instrument change, not by more draws**. `P(the
tail ratio is in [2,10]) = 0.60`.

### R5 — THE BLIND PRIORS THE BRIEF DEMANDS

- **`P(a 13-slope configuration this round) = 0.25`.**
- **`P(it survives the full pipeline => an m=4 (BIV-CURVE) witness
  | a 13-slope config is found) = 0.35`**; joint **`0.09`**.
- **`P(the second-relation route is the one that lands) = 0.15`**
  (against 0.70 for the algebraic solve, R3.3).
- **`P(the density window map matches ~q^-7) = 0.45`.**
- **EXPECTED BEST `|slopes|` THIS ROUND = `14`** (i.e. I expect to
  tie anchor 1, not beat it). Distribution I commit to:
  `P(<=13) = 0.25, P(=14) = 0.55, P(>=15) = 0.20`.
- `P(m=4 is DECIDED either way this round) = 0.10`.
- `P(the honest deliverable is a hardening, not a witness) = 0.75`.

### R6 — MISS-2 GUARD (mean-vs-max), registered in force

The guard has five clauses; anchor 1's guard fired three times and
killed its own false positive (`r36 REPORT.md:77`), and anchor 2's
MISS 4 was exactly an aggregate-slack-vs-per-block error
(`r34 REPORT.md:131-138`).

1. **No mean is ever evidence about a max, and no max is ever
   evidence about a mean.** Mean merges per draw, mean fully-split
   fibres, mean slope count — none of these may be reported as
   support for a reachability claim, and a reached maximum may not
   be reported as typical.
2. **A slope count is not a configuration.** No `|slopes| <= 13`
   result is reportable until it passes, on the actual object:
   (a) every `d_gamma <= 2`; (b) pair multiplicity exactly 1;
   (c) merge graph simple, bipartite `4+4`, degrees
   `(3,3,3,2|3,3,3,2)`; (d) all 13 slopes distinct and distinct
   from `g,h`; (e) all 8 fibres complete AND split over `F_q`;
   (f) `U~(t_i) != 0` for all `i` (`c_x != 0`); (g) `|W| = 27`.
   A failure of any clause is reported as a killed false positive.
3. **Positive dimension is not existence over `F_q`.** R2.2's
   `dim = 4` is a count over `F_qbar`; I will not infer an `F_q`
   point from it, and if the search fails I will say the dimension
   count is unrealised, not that the count is wrong.
4. **A per-field null is a sampled null.** Base triples, pencils and
   draws are all sampled; every negative is a ceiling under a named
   budget.
5. **Instrument-vs-quantity.** Before reporting any negative I must
   state which quantity the instrument actually optimises, and
   check it is the quantity in the claim (this is the exact failure
   anchor 1 hit with `(DEG-m)` on partial selections,
   `r36 REPORT.md:93`).

### R7 — ZERO-POWER PRE-DECLARATIONS

1. **No search result this round can decide `m=4`.** A negative is
   a ceiling over `(SHARE3-4)` under named budgets and named fields;
   a positive is a `W`-layer object only.
2. **The census is exhaustive only where I say "exhaustive", and
   only over the family named in the same sentence.** Sampled base
   triples are sampled nulls (anchor 1's zero-power 2).
3. **At most 5 fields exist in the window (R4.1); five fields is not
   `q`-uniformity** and nothing here extends to `q ~ 2^167`.
4. **Layer A will not be run**; `(SAT3)`-conditionality (`T=rho+2`)
   is untouched; `m=1` will not be exercised. All three carry
   forward from rounds 34-36 unchanged.
5. **R2.2's dimension count has ZERO power to produce a witness**
   and zero power over the arithmetic constraints (splitting in
   `mu_64`, completeness of fibres); it constrains only the
   `Psi~`-layer.
6. **R3.1's symmetry cap has zero power over non-equivariant
   configurations** — it forbids a route, it does not forbid a
   witness.
7. **If no 13-slope configuration lands, the fences I ship (split
   sub-case, sporadic sharing) are conditional on the same
   `(SHARE3-4)` ansatz** and say nothing about `G` outside the
   Lüroth-pullback lattice.
8. **`(SUPPLY-CODIM)` stays HEURISTIC**; no existence is inferred
   from any positive excess `E` (anchor 1's MISS 11).
9. **`Lüroth` and the pullback lattice are BANKED repo machinery**
   (`background/nodes/f_weight2_inverse/statement.md:9`;
   `critical/nodes/payment_completeness/statement.md:21`, both quoted
   at `r36 REPORT.md:117`). I claim no credit for the device and
   will re-run the CATCH-24A subtraction, hyphenated and infixed
   variants included, before every novelty claim below — in
   particular for `twisted cubic`, `rational normal curve`,
   `bidegree (3,3)`, `merge graph`, `constant-norm`, `K_{4,4}` and
   `coordinate descent`.

### R8 — expected misses (registered so they can be graded)

- **R8.1** I expect at least one of R2.1-R2.4 to be off by a
  constant or an index; the likeliest is the `lambda_ji` normalisation.
- **R8.2** I expect the coordinate-descent search to stall in a
  cycle rather than converge, and to need random restarts and root-
  choice backtracking.
- **R8.3** I expect the binding obstruction, if the search fails, to
  be the requirement that intermediate cubics **split over `F_q`**
  (each update needs a cubic with `F_q`-roots: probability `~1/6`
  per cubic if random, so `~(1/6)^3` per block update) — an
  arithmetic tax invisible to the dimension count.
- **R8.4** I expect `q = 641` to be supply-dead and to add nothing
  but a data point.
- **R8.5** I expect to reach 11 or 12 slopes on some raw count and
  for R6 clause 2 to kill it.
