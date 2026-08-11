The harness refused the `REPORT.md` write (subagent policy), so per the brief I return the full report text verbatim below. The directory contains 16 files and no `REPORT.md`.

**Headline for relay:** the D1 regression **kills `(NS-m)` as stated** — exhaustively, on bank 3's 16 realized `m=1` pencils — and it kills it for a diagnosable reason: `(NS-m)` counts **all** `F_q`-roots of `h_gamma`, while only the roots **in `W`** can ever bear on closure. At `m=1` the W-local form holds `5280/5280` while the stated form fails `4800/5280`. The layer-A control PASSED (nullity exactly `1`, `16/16`). D2's Wronskian instrument is **walled** — a totally split fibre is reduced, hence unramified, so the rigidity spends nothing of either Plücker budget (my registered ratio `-> 5/12` came out exactly). But a theorem did land from the layer-A variables by `deg_x` additivity plus fibre disjointness: **the kernel biform `Q(Z,x)` cannot split into linear factors over `F_q(x)` for any `m >= 2`, and always has an irreducible factor of `Z`-degree `>= ceil((3m+1)/4)`** — verified exhaustively over every factorisation profile for `m = 1..40`, with `m = 1` sitting exactly on the boundary. **My "span/RNC" reading of layer A is a PROVED node** (CATCH-24A caught it), and my first `a=7` table shipped the wrong sign before the exhaustive rerun corrected it (MISS 2).

---

# REPORT — r34_layer_a (round 34)

## VERDICT (first)

**`(NS-m)` as stated is FALSE, restated, and the restatement survives the
regression. The Wronskian attack is walled. A different theorem landed.**

1. **`(NS-m)` IS REFUTED AT `m=1`, EXHAUSTIVELY.** On bank 3's 16 realized
   `(SAT3)` pencils (`q=17`, `D = mu_16`), at the realized `a* = w* = 7m-1 = 6`
   the degree budget is `d = a-(4m+2) = 0`, every type-2 `h_gamma` is a
   **nonzero constant**, and both stated forms of `(NS-1)` fail in `0/480`
   type-2 slopes. At the planted `a = 7` the stated root-count form fails in
   `4800/5280` measurements over every admissible `H`.
2. **THE RESTATEMENT, AND IT PASSES.** `(NS-m)` counts *all* `F_q`-roots;
   closure only ever needs the roots **in `W`**. The W-local form
   **`(NS-W-m)`: `#{roots of h_gamma in W, with multiplicity} <= d-m`**, under
   the hypothesis `d >= m`, still implies closure, is strictly weaker than
   `(NS-m)`, and holds in **`5280/5280`** `m=1` measurements where `(NS-m)`
   fails in `4800`. The separating configurations are explicit: `h_gamma` of
   degree `1` with its single rational root **outside** `W`, so
   `X_gamma = 0 <= d-m = 0` (closure holds) while `(NS-1)` is violated.
3. **THE ROUND'S THEOREM, and it is not the Wronskian.** In the layer-A
   variables, `deg_x` additivity in `F_q[x][Z]` plus disjointness of the
   fibres of each irreducible factor forces
   ```text
   T*rho - O  <=  sum_j min( T*d_j , N*m_j ),      sum_j d_j <= rho,
   ```
   over the factorisation `Q = c(x) prod_j Q_j(Z,x)` into irreducibles over
   `F_q(x)`, `m_j = deg_Z Q_j`, `d_j = deg_x Q_j`. Consequences, verified
   exhaustively over **every** partition profile for `m = 1..40`, `0`
   violations: **at most one factor is "small"; `Q` splits into linear factors
   over `F_q(x)` only at `m = 1`; every surviving profile carries an
   irreducible factor of `Z`-degree `>= ceil((3m+1)/4)`, and that bound is
   exactly attained at every `m`; at `m = 2,3,4` the only survivor is `Q`
   irreducible.** `m=1` sits on the boundary with the realized numbers
   exactly: one branch, `delta_1 = 3 = rho`, `T*delta_1 = 15 = N-1`.
4. **THE WRONSKIAN INSTRUMENT IS WALLED, with numbers.** A totally split
   fibre is reduced, hence **unramified**, so the banked rigidity spends
   **nothing** of the Plücker budget in either picture. W-picture budget
   `(m+2)(d-m-1)` against the `(NS-m)` aggregate demand `rho*m` runs
   `0.3000, 0.3810, 0.4107, 0.4165, 0.4167, 0.4167` at
   `m = 4,7,16,64,1024,2^20` — `-> 5/12`, exactly the number I registered
   before computing. A-picture budget `(m+1)(3m-1) ~ 3m^2` is consumed only by
   `O <= m-1`: slack by a factor `~3m`. Ramification measures **multiplicity**;
   `(NS-m)` measures **rationality**; the two are independent.

---

## MISSES FIRST

1. **I NEARLY SHIPPED THE WRONG SIGN OF THE `a=7` VERDICT, AND THE WRONG
   TABLE IS IN A RESULTS FILE.** `d1_calib.py` picks the *first* admissible
   kernel element. At `a=7` the nullity is `2` and the first admissible
   element it found is the degenerate `deg h_gamma = 0` one, so
   `d1_calib_results.txt` prints **`NS-A 480/480`** — i.e. "`(NS-1)` holds at
   `a=7`". That is a sampling artifact. `d1b_exhaustive.py` sweeps **every**
   projective kernel element and gets `480/5280`: `(NS-1)` **fails** in
   `4800/5280`. The stale line stands in `d1_calib_results.txt` and I flag it
   here rather than silently regenerating it.
2. **MY "TRANSPARENT FORM OF LAYER A" IS A PROVED NODE.** I derived "the `T`
   locators span at most `m+1` dimensions and `gamma |-> [c_gamma L_gamma]` is
   a degree-`m` rational curve" and thought it new for about ten minutes. It
   is `background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/statement.md:16-40`
   `(RNC1)-(RNC3)`, **PROVED**, and *stronger* than what I had (the `m+1`
   forms are linearly **independent**, separation rank **exactly** `m+1`). The
   CATCH-24A grep caught it before the write-up; nothing here claims it.
3. **ONE OF MY CONTROLS NEVER FIRED AND I DID NOT FIX IT.** `d3b_cx_form.py`'s
   positive control (build `A_x` from a random bidegree-`(rho,m)` `Q`, so a
   solution exists by construction) produced **`0` usable instances** in `400`
   draws at each field — a random quadratic in `Z` splits at all `32` domain
   points with probability `~2^-32`. The control is reported **INCONCLUSIVE**
   in the results file. The right constructor (take the branches to be
   polynomials: `Q = Q_2(x)(Z-alpha(x))(Z-beta(x))` with
   `deg Q_2 <= 5`, `deg alpha, beta <= 1`) is obvious in hindsight and I ran
   out of budget. So the `c_x` builder rests on **two** controls only: it
   agrees with bank 2's `c_gamma` builder on the `m=1` witnesses (nullity `1`,
   `16/16`) and on bank 2's `m=2` exhibit (nullity `0`, both fields).
4. **ONE RAMGUARD RUN FAILED.** Invocation 4 (`d3_scale.py`) died with a
   `TypeError`: `biv_core.poly_from_roots(roots, q)` and
   `d1_calib.poly_from_roots(roots)` have different signatures and I imported
   both into one namespace. Self-caught, one-line fix, rerun as invocation 5.
5. **THE `m=1` STRATUM IS DOUBLY DEGENERATE, AND ONE OF THE TWO DEGENERACIES
   I LEARNED FROM THE REPO, NOT FROM MY REGISTRATION.** I registered `m=1`'s
   structural disjointness (R4.2). What I did **not** know is that the
   realized `a* = w* = 6 = 2rho = 8m-2` is exactly the stratum that
   `critical/nodes/rate_half_band_crossing_location/statement.md:582-584`
   declares **empty for every `m >= 2`** ("`w* = 2rho` forces pairwise-disjoint
   full-size supports, i.e. `T*rho <= N`, true only at `m = 1`"). So every
   `m=1` counterexample to `(NS-m)` lives in a banked-empty stratum. The
   refutation of the literal quantifier stands; its reach into `m >= 2` does
   not.
6. **TWO-FIELD CONFIRMATION IS IMPOSSIBLE AT `m=1` AND EVERY `m=1` NUMBER
   HERE IS SINGLE-FIELD.** `rh_sat3_realizability/d1_m1_results.txt:9-13`
   records `max T = 3` at `q = 97, 113, 193, 241, 257` — only `q = 17` realizes
   `T = rho+2` at `m=1`. This is structural, not a shortcut, but it means the
   entire D1 calibration rests on one field.
7. **`a = 7` AND `a = 8` ARE PLANTED, NOT REALIZED.** The realized joint
   support is `a* = 6`. The only *non-vacuous* `(NS-1)` measurements (`d >= 1`)
   therefore sit at a **planted** `W`, exactly as bank 1's planted census did
   (`rh_psi_degree/REPORT.md:284-292`). At the realized `W` the statement is
   not merely false, it is unsatisfiable (`need_X = d-m = -1 < 0`).
8. **I DID NOT PROVE `(NS-m)`, `(NS-W-m)`, OR CLOSURE.** The theorem I proved
   is about a **different object**: the factorisation of `Q(Z,x)` over
   `F_q(x)` (`Z`-direction), not the factorisation of `h_gamma` over `F_q`
   (`x`-direction). It answers the brief's D2 question — "does the budget
   force `>= m` non-split degree in the transverse direction?" — **for the
   layer-A object and not for `h_gamma`**. The mandate's D2 as literally posed
   is unmet.
9. **THE `(3m+1)/4` CONSTANT IS THE TRUTH OF MY COUNTING SYSTEM, NOT
   NECESSARILY OF THE CONFIGURATION.** `d2_transverse_results.txt [B]` shows
   `min over survivors of max m_j == ceil((3m+1)/4)` at every `m` in `1..40`,
   i.e. my inequality cannot be improved by better bookkeeping. It says
   nothing about whether the surviving profiles are *realizable*.
10. **"THE BINDING SUB-SYSTEM IS ANY 4 BLOCKS" IS MEASURED FOR ONE ORDERING.**
    I measured that the **first four** locators of bank 2's `m=2` exhibit, in
    slope order, already span `4 > m+1 = 3`. All nine span `8 = rho+1`. I did
    not enumerate `4`-subsets; "any" is an inference, not a measurement.
11. **I ADDED NOTHING AT `m >= 3`.** No `m=3` structured candidate was built.
    Bank 2's named decisive computation (`rh_bivariate_system/REPORT.md:501-503`,
    a constructive search at `m=3,4`) remains untouched.

---

## CATCH-24A — own-repo subtraction, run BEFORE every novelty claim

| object | in-repo prior | verdict |
|---|---|---|
| layer A as "the locators span `<= m+1` dimensions / `gamma |-> [c_gamma L_gamma]` is a degree-`m` rational curve" | `background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/statement.md:16-40` `(RNC1)-(RNC3)`, **PROVED**: the `m+1` forms are linearly independent, separation rank **exactly** `m+1`, `nu_Q` a degree-`m` rational normal curve | **BANKED AND PROVED, and stronger than my version.** MISS 2. My `16/16` `m=1` span measurement is an independent confirmation of the node at `m=1`, nothing more. |
| layer A itself (bidegree-`(rho,m)` `Q(Z,x)`, `(rho+1)(T-m-1) = 12m^2` conditions) | `rh_bivariate_system/REPORT.md:483-497`; `saturation_rigidity/proof.md:5-6,15` | banked; it is my mandate. I reproduce bank 2's kill and add the `c_x` shadow. |
| `d_x <= m`, `sum_x(m-d_x) = 1+O <= m`, `>= 15m` saturated points, `Q_Z(x)` **nonzero** at every domain point | `background/nodes/rate_half_ca_hankel_endpoint_saturation_rigidity/statement.md:10-14,38-70` (read directly, not via the anchors) | banked; `(SAT1),(SAT3),(SAT4),(SAT5)` and the nonvanishing line are the **hypotheses of my theorem**, quoted not derived. |
| `m = 1` is structurally disjoint from residual (ii) | `critical/nodes/rate_half_band_crossing_location/statement.md:585-588` | banked. |
| `a = 8m-2` is vacuous for every `m >= 2` (`w* = 2rho => T*rho <= N`, only at `m=1`) | `critical/nodes/rate_half_band_crossing_location/statement.md:582-584` | banked, **and it is the stratum my `m=1` counterexamples live in**. MISS 5. |
| the 16 realized `m=1` `(SAT3)` pencils; `(SAT3)` realizable only at `q=17` | `rh_sat3_realizability/d1_m1_results.txt:5-25`, `d2_realize_results.txt:6-48` | banked; my enumeration **re-derives all 16 and contains both banked witnesses** (`d1_calib_results.txt [A]`). |
| `(NS-m)`, `(C2)`, `need_X = d-m`, `Eneed = m`, the argmax `a=(20m-2)/3` | `rh_psi_degree/REPORT.md:331-341,266-276` | banked; my mandate's target. New here: the W-local separation and the `d >= m` hypothesis. |
| `(BIV-H)`, `(BIV-CURVE)`, `build_S2`, the `m=2` exhibit and its layer-A kill | `rh_bivariate_system/REPORT.md:216-221,352-359,447-466`, `d4_exhibit_results.txt`, `d5_layerA_results.txt` | banked; **reproduced exactly** (nullity `0`, both fields, three controls PASS). |
| Wronskian / Plücker / ramification / Stöhr–Voloch as instruments in this lane | greps over `critical/`, `background/`: `Wronskian` and `ramification` occur only in the `l1_mixed_petal`, `rate_half_list_adjacent_crossing`, `dli` and `rate_half_band_closure` lanes; `inflection`, `osculating`, `order sequence` return **zero files repo-wide**; `Stöhr/Voloch` only in `f3_*` | the *application to this lane* is new; the **result is negative** (the instrument is walled), so the novelty buys nothing. |
| `Q` irreducible / splitting over `F_q(x)`; branch structure of the kernel biform | greps for `F_q(x)`, `rational function field`, `splits into linear`, `totally split over` over `rate_half_band_crossing_location/`, `rate_half_band_closure/`, the RNC node and the saturation node: **zero hits**. The RNC node's own claim contract says its scope is "**not each irreducible component**" and names "the multiplicative-domain evaluation hyperplanes" as a next gate | claimed **new**, and it is the round's one positive object. It is exactly inside the gate the node points at, and outside the node's stated scope. |
| "no contradiction follows from the incidence counts alone" | `.../rational_normal_kernel_curve/claim_contract.md` (Nonclaims) | **consistent with my theorem**: I derive no contradiction, only a restriction on the factorisation profile. Quoted so that nobody reads my result as contradicting that nonclaim. |

---

## D1 — THE `m=1` CALIBRATION (the gate)

### D1.0 Reproduction of bank 3

`d1_calib_results.txt [A]`: my exhaustive scan re-derives **16** `T = rho+2`
locator families over `D = mu_16 < F_17`, matching
`rh_sat3_realizability/d2_realize_results.txt:46`, and **both** banked
realized witnesses appear in my enumeration. `[B]`: `16/16` charts have all
`T = 5` slopes finite, supports **pairwise disjoint**, `|covered| = rho*T = 15`,
one uncovered point `x_0`.

> **Structural fact (`m=1`).** `d_x <= e = m = 1` forces the `T` supports
> pairwise disjoint, so at the canonical `W = S_g u S_h` every type-2 slope
> has `X_gamma = |S_gamma ^ W| = 0` **identically**. Any `m=1` confirmation
> of a bound on `X_gamma` is therefore vacuous by construction.

### D1.1 The layer-A control — PASS

`d1_calib_results.txt [C]`, `(rho+1)(T-m-1) = 12` conditions on `T = 5`
unknowns `c_gamma`:

```text
nullity histogram over the 16 realized witnesses : {1: 16}
kernel with EVERY c_gamma != 0                   : 16/16
predicted kernel vector c_gamma = lead(A + gamma B) in the kernel : 16/16
```

Nullity is **exactly** `1`, as it must be for a genuine pencil (the solution
space is `{lambda (A + Z B)}`). The mandate's built-in control passes, and it
passes in the strong form: not merely `nullity >= 1`, but the *predicted*
kernel vector is recovered. Independently, `d3b_cx_results.txt [m=1]`: the
dual `c_x` builder (`17` unknowns, `24` conditions) also returns nullity `1`
in `16/16`. **The layer-A builder is not wrong.**

### D1.2 `(NS-1)` measured, exhaustively

`d1b_exhaustive_results.txt` builds **every** `W` with
`S_g u S_h subseteq W subseteq D`, `|W| in {6,7,8}` — `16` pencils `x` `10`
type-1 pairs `x` `(1+10+45)` extensions = **8960** systems — and tests
admissibility **exactly** (for `x in W` the map `v |-> H_v(.,x)` is linear on
the kernel `K`, so an admissible element exists iff no `x` kills all of `K`;
a space over `F_q` is never a union of `<= q` proper subspaces and
`|W| <= 8 < 17`).

```text
 a #t2pts  x0inW  cases admissible        nullities  killed-by-t2pt
 6      0  False    160        160         {1: 160}               0
 7      0   True    160        160         {2: 160}               0
 7      1  False   1440          0        {1: 1440}            1440
 8      1   True   1440          0        {2: 1440}            1440
 8      2  False   5760          0        {1: 5760}            5760
```

> **THEOREM (`m=1`, exhaustive).** A `W` containing a type-1 pair admits an
> admissible `H` **iff** it contains no point of a type-2 support. Hence at
> `m=1`, `X_gamma = 0` for every type-2 slope in every admissible `W`,
> `a in {6,7}` only, and **`a = 8m = 8` is unreachable**. `0` exceptions in
> `8960`. The mechanism: the two type-1 slopes force `H = (Z-g)(Z-h)G(x)`
> with `deg_Z G <= m-1 = 0`, so `G` is `Z`-free and any type-2 point
> `y in W` forces `G(y) = 0`, annihilating the whole fibre `H(.,y)`.

That mechanism is **specific to `m=1`** (`deg_Z G = m-1 = 0`); at `m >= 2`
there is no collapse.

`(NS-1)` over **every** admissible `H` (all projective kernel elements):

```text
 a  x0inW   admH   tot2   NS-A   NS-B   NS-W   CLOS  SPLIT        deg h     #F_q-roots
 6  False    160    480      0      0      0      0      0     {0: 480}       {0: 480}
 7   True   1760   5280    480      0   5280   5280   4800 {0:480, 1:4800} {0:480, 1:4800}
```

`NS-A` = `#F_q-roots(h_gamma) <= d-m`; `NS-B` = nonsplit degree `>= m`;
`NS-W` = `#roots in W <= d-m`; `CLOS` = `X_gamma <= d-m`; `SPLIT` = `h_gamma`
splits completely over `F_q`. Identity checks `(AGG)`, `(FIB)`,
`Rin = X + n - ov`: **`9600/9600`**.

**Readings.**

1. **At the realized `a* = 6` everything fails**, because `need_X = d-m = -1`
   is negative: `X_gamma = 0 > -1`. The ledger's own requirement is
   unsatisfiable at `m=1`, which is precisely the banked structural
   disjointness (`statement.md:585-588`) showing up as arithmetic.
2. **At `a = 7` the stated `(NS-1)` fails in `4800/5280`** while **`CLOS`
   holds in `5280/5280`**. Exemplar (`d1b_exhaustive_results.txt [D]`):
   `h = [15,15]`, `deg 1`, root `16`, `X = 0`, `Rin_mult = 0`, `nonsplit = 0`.
   The root is rational and **outside `W`**.
3. **Bank 1's falsifier F4 fires in one reading and not the other.** F4
   (`rh_psi_degree/REPORT.md:423-425`) asks for a realizable `T = rho+2`
   pencil with a type-2 `h_gamma` that splits completely. Over `F_q`: **fired,
   `4800` instances**. Over `W`: **did not fire**, `Rin_mult = 0` in
   `5280/5280`. F4 was declared "NOT EXERCISED and unexerciseable at census
   scale"; it is now exercised, at `m=1`, and the two readings of it disagree.

### D1.3 The restatement

> **`(NS-W-m)`.** For every type-2 slope of a strict-`A=3` column-far pencil
> at `T = rho+2` **with `d = a-(4m+2) >= m`**: `h_gamma` has at most `d-m`
> roots **in `W`**, counted with multiplicity.

- It **implies closure**: `X_gamma <= #{roots of h_gamma in W} <= d-m`.
- It is **strictly weaker** than `(NS-m)` (which also budgets the roots
  outside `W`, and the `nonsplit` gloss additionally needs `deg h_gamma = d`).
- It **survives the `m=1` regression**: `5280/5280` at `a=7`, where `d = 1 = m`
  so the hypothesis bites; at `a=6`, `d = 0 < m` and the hypothesis correctly
  excludes the case in which `need_X` is negative.
- At the argmax `a = (20m-2)/3`, `d = (8m-8)/3 >= m` for every `m >= 2`, so
  the hypothesis is **free** everywhere the ledger needs it.

**Two forms of `(NS-m)` are inequivalent and the bank-1 text uses both.**
"at most `d-m` roots with multiplicity" and "at least `m` of its degree in
irreducible factors of degree `>= 2`" agree only when `deg h_gamma = d`. At
`a=7`, `m=1` the `480` degenerate `H` give `deg h = 0`: the root-count form
holds and the irreducible-factor form fails. The operative form for closure
is the **root count**; the factor form is a gloss that needs `deg h = d`
(bank 1 measured `97.8%`, `rh_psi_degree/REPORT.md:326-329`).

---

## D2 — THE WRONSKIAN ATTACK (walled), AND WHAT REPLACED IT

### D2.1 The budget, derived and evaluated

`H(Z,x) = sum_{j=0}^{m+1} Z^j f_j(x)`, `deg f_j <= d`, so the `f_j` span a
`g^{m+1}_d` on `P^1`. Plücker at genus `0` gives total ramification weight
`(r+1)(d-r) = (m+2)(d-m-1)`; in char `p` the Stöhr–Voloch form
`deg R = (r+1)d - 2 sum eps_i` can only be **smaller**. In the layer-A
picture `Q_0,...,Q_m` span a `g^m_rho`, budget `(m+1)(3m-1)`.

```text
       m     a=argmax          d     W-budget     A-budget   demand rho*m    W/dem   O<=m-1
       4           26          8           18           55             60   0.3000        3
       7           46         16           72          160            189   0.3810        6
      16          106         40          414          799           1008   0.4107       15
      64          426        168         6798        12415          16320   0.4165       63
    1024         6826       2728      1747278      3147775        4193280   0.4167     1023
 1048576      6990506    2796200 1832519030094 3298536980479  4398045462528   0.4167  1048575
```

`W/demand -> 5/12 = 0.41667` — **R2.5 registered this number before the
computation**. The A-budget `~3m^2` is consumed only by `O <= m-1`: slack by
`~3m`.

### D2.2 Why the instrument cannot work (R2.6, confirmed analytically)

A totally split fibre `P_x(Z)` is **reduced**, hence **unramified**. The
banked rigidity ("all `a` fibres totally split") therefore spends **zero** of
either budget. Ramification bounds **multiplicity**; `(NS-m)` bounds
**rationality**; the two are logically independent. In dual terms: the
rigidity says the hyperplane `phi(x)^perp` meets the rational normal curve in
`m+1` distinct **rational** points — a condition on the field of definition of
a reduced intersection, invisible to any Wronskian. **The brief's D2 framing
("what total fibre-splitness costs against the budget") is misposed: it costs
nothing.** I registered this as R2.6 at `P = 0.65` before computing and I
report it rather than manufacture a cost.

Per **R3** I do **not** conclude the route is dead: the budget is over the
whole linear series while the `h_gamma` are the members indexed by the
rational normal curve only, and a per-member bound can hold with every
aggregate reading failing.

### D2.3 THE THEOREM: transverse non-splitting of the kernel biform

Hypotheses, all banked and quoted: `deg_Z Q <= m`, `deg_x Q <= rho = 4m-1`
(`rational_normal_kernel_curve/statement.md:16-40`, PROVED); `D = mu_N`,
`N = 16m`; `|Gamma| = T = 4m+1` `(SAT3)`; `sum_x d_x = Nm-(1+O)`, `O <= m-1`
`(SAT1),(SAT4)`, `saturation_rigidity/statement.md:10-14,49-53`; and **`Q(.,x)`
is a nonzero parameter polynomial at every domain point**
(`saturation_rigidity/statement.md:49`).

Factor `Q = c(x) prod_j Q_j(Z,x)` into irreducibles over `F_q(x)`,
`m_j := deg_Z Q_j >= 1`, `d_j := deg_x Q_j`.

> **(1)** `deg_x` is **additive** on products in the domain `F_q[x][Z]` (the
> `x`-leading coefficient of a product is the product of the `x`-leading
> coefficients, and is nonzero). Hence `sum_j d_j <= deg_x Q <= rho = 4m-1`.
> **No cancellation caveat.**
>
> **(2)** For fixed `j`, `#{x in D : Q_j(gamma,x) = 0} <= d_j`, so
> `sum_{gamma in Gamma} n_{j,gamma} <= T d_j`.
>
> **(3)** For fixed `x`, `Q_j(.,x)` is not identically zero (else `Q(.,x)` is),
> so it has `<= m_j` roots; hence `sum_{gamma} n_{j,gamma} <= N m_j`.
>
> **(4)** `c` has **no zero in `D`** (a zero would make `Q(.,x)` vanish
> identically, contradicting `statement.md:49`), so
> `u_gamma <= sum_j n_{j,gamma}` and, with
> `sum_gamma u_gamma = sum_x d_x = T rho - O`,
> ```text
> T*rho - O  <=  sum_j min( T*d_j , N*m_j ),      sum_j d_j <= rho.
> ```

Call `Q_j` **small** if `T d_j < N m_j` (equivalently `d_j <= 4m_j - 1`) and
**big** otherwise (then `d_j >= 4m_j`). Let `t` = number of small factors and
`M_s = sum_{small} m_j`. Substituting `d_j <= 4m_j-1` for the small factors
and `min = N m_j` for the big ones collapses (4) to

```text
(4m+1) t  <=  4 M_s + 1 + O  <=  4 M_s + m .
```

> **THEOREM (r34 — FACTOR-DEGREE DICHOTOMY).**
> **(i)** `t <= 1`. (`t >= 2` forces `4M_s >= 7m+2`, i.e. `M_s > m`.)
> **(ii)** `t = 0` is impossible: all factors big gives
> `sum_j d_j >= 4 sum_j m_j = 4m > 4m-1 = rho`.
> **(iii)** So `t = 1` exactly, and the unique small factor has
> `Z`-degree `m_1 >= (3m+1)/4`.
> **(iv)** In particular, for `m >= 2` **`Q(Z,x)` does not split into linear
> factors over `F_q(x)`** — the `m` slope branches cannot all be rational
> functions of `x`. For `m in {2,3,4}`, `Q` is **irreducible** over `F_q(x)`.
> **(v)** At `m = 1` the theorem is **tight and realized**: one branch,
> `delta_1 = 3 = rho`, `T delta_1 = 15 = N - 1`.

**Exhaustive verification** (`d2_transverse_results.txt [B],[C]`): for every
`m = 1..40` and **every** partition profile `(m_j)` of `m`, the exact maximum
of `sum_j min(T d_j, N m_j)` subject to `d_j >= 1`, `sum d_j <= rho` was
computed and compared against `T rho - (m-1)` (the most generous `O`).

```text
   m  #partitions  #surviving  all-ones survives?  min over survivors of max m_j  ceil((3m+1)/4)
   1            1           1                True                              1               1
   2            2           1               False                              2               2
   4            5           1               False                              4               4
   8           22           2               False                              7               7
  16          231           7               False                             13              13
  40        37338          97               False                             31              31

VIOLATIONS of the theorem over m = 1..40: 0   PASS
```

`min over survivors of max m_j == ceil((3m+1)/4)` at **every** `m`: the
constant is exactly the truth of the counting system, not a lossy bound.
Survivors at small `m`: `m=2: [(2,)]`, `m=3: [(3,)]`, `m=4: [(4,)]`,
`m=5: [(5,), (4,1)]`, `m=8: [(8,), (7,1)]`.

**Relation to the mandate.** This is the transverse-splitting question
answered — *for the layer-A object `Q` in the `Z`-direction*, not for
`h_gamma` in the `x`-direction. It does **not** prove `(NS-m)` or
`(NS-W-m)`. It is the first proved obstruction to the branches of the kernel
curve being rational, and it is exactly the case that `m=1` realizes.

### D2.4 Falsifiers, pre-registered here

- **F-A (kills the theorem).** A strict-`A=3` configuration at `T = rho+2`
  satisfying `(SAT1),(SAT3),(SAT4)` and the RNC node whose `Q` splits into
  linear factors over `F_q(x)` at some `m >= 2`. Exercised only through the
  combinatorial core (`m = 1..40`, `0` violations); a hit means one of the four
  hypotheses is misquoted.
- **F-B (kills step (4)).** A configuration whose `c(x)` has a zero in `D`.
  Excluded by `saturation_rigidity/statement.md:49`; a hit means that line has
  been misread.
- **F-C (would restore `(NS-m)`).** A type-2 `h_gamma` at `m >= 2` whose
  `F_q`-roots outside `W` are provably `<= Rout` for a useful `Rout`. Bank 1
  measured `Rout <= 3` in `648/648` (`rh_psi_degree/REPORT.md:326-328`) — if
  that is a theorem rather than a sample, `(NS-m)` and `(NS-W-m)` are within
  `O(1)` of each other and the restatement is cosmetic. **Untested.**
- **F-D (would close residual (ii)).** A proof of `(NS-W-m)` at the argmax, or
  of `X_gamma <= d-m` directly.
- **F-E (inherited, live).** `rh_psi_degree/REPORT.md:426-427` F5, `(NEWCAP)`
  violation.

---

## D3 — LAYER-A RANK AT SCALE

### D3(a) the `m=1` witnesses — control, and a cross-builder check

`d3_scale_results.txt [a]`:

```text
locator SPAN rank over the 16 witnesses (banked bound m+1 = 2) : {2: 16}
W-layer nullity by |W|                                        : {6: {1:160}, 7: {2:160}}
CROSS-BUILDER  my bivH nullity == bank 2's build_S2 nullity    : 320/320
```

Three independent builders now agree on the same objects: my `(BIV-H)`
builder, bank 2's `build_S2`, and the `c_x` shadow. The span `= 2 = m+1`
confirms the PROVED RNC node at `m=1` (MISS 2: the node, not me).

### D3(b) bank 2's `m=2` exhibit — reproduced, and **what binds**

`d3b_replay_results.txt` (bank 2's `d5` re-run from my copy): layer-A nullity
`0` at `q=97` and `q=193`, `48` conditions on `9` unknowns, with CTRL-1
(positive, nullity `1`, all-nonzero kernel), CTRL-2 (analytic, nullity
`= m+1 = 3` exactly) and CTRL-3 (negative, nullity `0`) all **PASS**.

`d3_scale_results.txt [b]` diagnoses the kill:

```text
q= 97  layer-A nullity 0 ; locator SPAN rank 8 of 8   (banked bound m+1 = 3)
q=193  layer-A nullity 0 ; locator SPAN rank 8 of 8
       the FIRST 4 locators already span 4 > m+1 = 3
```

**Which equations bind:** not `48` conditions marginally, but the span. The
first four blocks alone already exceed the banked bound; all nine fill the
whole `P^rho`. The exhibit is not near-miss-killed, it is maximally far from
layer A. `d3b_cx_results.txt` confirms from the dual side: `d_x` profile
`{1:1, 2:31}`, `34` unknowns, `72` conditions, **nullity `0`**, both fields.

### D3(c) structured `m=2` candidates

`d3_scale_results.txt [c]`: bank 2's `(BIV-CURVE)` fibre constructor, `40`
fresh seeds per field:

```text
q= 97  built 40 ; LAYER A kills 40 ; survives 0 ; locator span ranks {8: 40}
q=193  built 40 ; LAYER A kills 40 ; survives 0 ; locator span ranks {8: 40}
```

**`80/80` killed, every one with span rank `8`.** `(BIV-CURVE)` and layer A
are effectively **orthogonal**: satisfying the W-layer's joint condition buys
nothing at all toward the full-domain one. This sharpens bank 2's own
cross-pilot flag (`rh_bivariate_system/REPORT.md:494-497`): the reason to
spend the lane on layer A is not that layer A is `3x` stronger by deficit
count, it is that the W-layer's structured solutions land in the *worst*
possible position for layer A.

**Zero power caveat.** These are `80` configurations from one constructor.
They can falsify "the fibre method produces layer-A-consistent candidates";
they establish nothing about the existence of such candidates.

---

## D4 — VERDICT

**`(NS-m)` is RESTATED, not proved and not merely walled. The `m=1`
regression is decisive and diagnostic.**

- **Status of `(NS-m)` as stated: FALSE.** The hypothesis class is nonempty at
  `m=1` (16 realized pencils) and the conclusion fails on all of it: `0/480`
  at the realized `a*`, `480/5280` at the only `d >= 1` admissible `W`. Both
  stated forms fail; they are also inequivalent to each other.
- **Status of the restatement `(NS-W-m)` (`d >= m`, roots counted in `W`
  only): SURVIVES.** `5280/5280`, and it still implies closure. This is the
  statement the coordinator should carry forward; `(NS-m)` should be retired
  or demoted to a corollary of `(NS-W-m)` + a bound on `Rout`.
- **Status of the reach of the refutation: LIMITED, and I say so first.**
  Every `m=1` counterexample lives in the `a = 2rho` stratum that
  `statement.md:582-584` proves **empty for `m >= 2`**, and the `m=1`
  mechanism (`deg_Z G = m-1 = 0`) is a degeneracy with no `m >= 2` analogue.
  Geometrically the layer-A curve at `m=1` is a degree-`1` rational normal
  curve — an isomorphism `P^1 -> P^1` whose "hyperplane sections" are single
  points. **The entire `m >= 2` geometry is invisible at `m=1`.** The
  regression can and did kill the literal quantifier; it cannot support the
  statement, exactly as registered (R2.4).
- **Status of D2's instrument: WALLED, with the number.** Ramification cannot
  see rationality; the budget is slack by `~3m` in the layer-A picture and
  short of the demand by `5/12` in the W-picture.
- **What replaced it: a proved transverse non-splitting theorem** for the
  kernel biform, tight at `m=1`, excluding rational branches for all `m >= 2`
  and forcing an irreducible factor of `Z`-degree `>= ceil((3m+1)/4)`.

**Where the next instrument should go.** Not to any ramification budget, and
not to `(NS-m)` as written. Two concrete continuations, in order:

1. **Push the factor-degree dichotomy into the RNC node's stated gate.** The
   node's own "next exact gate" is "the Hankel/apolar coefficient-chain
   equations, the multiplicative-domain evaluation hyperplanes, or the
   norm/Bezout factorization". My inequality uses only the *cardinality* of
   `D`; using that `D = mu_N` is a **multiplicative group** is untouched and is
   the obvious next term. The surviving profiles are so few (`1` profile at
   `m=2,3,4`; `97` at `m=40`) that a single further constraint may empty them.
2. **Decide `Rout`.** If bank 1's measured `Rout <= 3` is a theorem, then
   `(NS-m)` and `(NS-W-m)` differ by `O(1)` and my restatement is cosmetic; if
   it is not, `(NS-m)` was never the right target and the W-local form is the
   only one worth attacking. This is a cheap question and it decides whether
   the round's D1 result is a correction or a redirection.

**Recommended node work (AUDIT-AND-DRAFT; I applied nothing).** An addendum
to `rate_half_band_crossing_location`'s bank-1 paragraph recording that
`(NS-m)` is refuted at `m=1` on the realized `(SAT3)` witnesses, that the
two forms in which it is stated are inequivalent, and that `(NS-W-m)` with
`d >= m` is the surviving sufficient statement. A new background node for the
factor-degree dichotomy, cited to `rational_normal_kernel_curve` and
`endpoint_saturation_rigidity`, with the `m=1` tightness as its calibration.

---

## PREDICTIONS vs OUTCOMES

| registered | outcome |
|---|---|
| R1 `P((NS-m) survives the m=1 calibration as stated) = 0.10` | **RESOLVED NO** — refuted exhaustively, and for exactly the registered reason (`d <= 2` at `m=1`) |
| R1 `P(survives non-vacuously) = 0.03`, `P(vacuously) = 0.07` | both **NO**: it fails non-vacuously (`h_gamma != 0` in every case) |
| R1 `P(Wronskian budget yields the theorem this round) = 0.05` | **RESOLVED NO** — the budget cannot see rationality. A theorem landed by a *different* instrument (MISS 8) |
| R1 `P(layer A consistent on all 16 m=1 witnesses) = 0.85` | **HIT**, `16/16`, nullity **exactly** `1`, all-nonzero kernel, predicted kernel vector recovered |
| R2.1 `d = 0` at `m=1, a=6`, every `h_gamma` constant, `P=0.90` | **HIT** `480/480` |
| R2.2 `(NS-1)` violated at `a=6`, `P=0.92` | **HIT** `0/480`, both forms |
| R2.3 restatement is degree-budget-shaped, `P=0.60` | **HIT** — the hypothesis is `d >= m`; but the *substance* of the restatement is the W-local root count, which I did **not** anticipate |
| R2.4 the `m=1` regression can only kill, never certify, `P=0.75` | **HIT and strengthened** — the stratum is banked-empty for `m >= 2` (MISS 5) |
| R2.5 W-budget `(m+2)(5m-11)/3` `<` demand `rho*m`, ratio `-> 5/12`, `P=0.70` | **HIT exactly**, `0.41667` |
| R2.6 totally split fibres cost the ramification budget nothing; D2's framing misposed, `P=0.65` | **HIT** — and it is why D2 as posed could not be delivered |
| R3 MISS-2 guard (aggregate bounds refute, never prove) | **USED, and it is how the theorem works**: the counting inequality is an upper bound on a SUM, used only to *refute* factorisation profiles. I did not claim `(NS-m)` from any aggregate and did not declare the route dead from `budget < demand` |
| R4.1 no infeasibility claim from random-embedding nullity `0` | **HONOURED** — the `80/80` `m=2` kills are reported as falsifications of a constructor, not as evidence of non-existence |
| R4.5 `T_2 <= 1` would make max-vs-mean powerless at `m=1` | **DID NOT FIRE**: `T_2 = 3`. But `X_gamma = 0` identically, so max `=` mean `= 0` and the comparison is powerless anyway, for a different reason |
| R6 "the builder will need a degenerate-case fix; expect a control failure" | **HIT twice** — invocation 4's `TypeError` (MISS 4) and the `c_x` positive control that never fired (MISS 3) |
| R6 "expect NOT to prove `(NS-m)`; deliver a POSED statement + `m=1` restatement" | **HIT** — plus one unregistered proved theorem |

---

## ZERO-POWER DECLARATIONS

1. **Every `m=1` number here is SINGLE-FIELD.** `q = 17` is the only field in
   which `(SAT3)` is realized at `m=1`
   (`rh_sat3_realizability/d1_m1_results.txt:9-13`). No two-field
   confirmation is possible; this is structural, not a shortcut taken.
2. **`m=1` can refute a `forall m` statement and can never support one.** It
   is banked structurally disjoint (`statement.md:585-588`) and its realized
   stratum is banked empty for `m >= 2` (`statement.md:582-584`).
3. **The `m=1` confirmation of `X_gamma = 0` is vacuous as evidence for
   `m >= 2`:** `e = m = 1` forces the supports disjoint, so `X_gamma = 0` is
   automatic at the canonical `W` before any instrument is applied.
4. **The layer-A geometry degenerates at `m=1`** to a degree-`1` rational
   normal curve, i.e. an isomorphism `P^1 -> P^1` with point "hyperplane
   sections". Nothing about the `m >= 2` incidence geometry is tested.
5. **`16` witnesses and `8960` `W` are exhaustive *within `m=1`* and a sample
   of nothing else.**
6. **The `80` `m=2` layer-A kills falsify a constructor, not an existence
   claim.** No search for a layer-A-consistent `m=2` configuration was run;
   absence where none was sought is not evidence (bank 2's MISS 4 arithmetic:
   per-draw detection probability `~q^{-Theta(m^2)}`).
7. **The factor-degree theorem is verified only through its combinatorial
   core** (`m = 1..40`, every partition). Steps (1)-(4) are proved from quoted
   banked hypotheses; no `m >= 2` configuration was constructed to test them
   against, because none exists to test against.
8. **`(3m+1)/4` is the exact truth of my inequality, and says nothing about
   realizability** of the surviving profiles (MISS 9).
9. **All rational-point instruments remain vacuous here** (`q > 2^167` at
   official scale against `O(m^2)` incidences) — declared before being tried,
   and not tried. Chebotarev-style densities for the branch covering are in
   the same position: the error term `~g sqrt(q)` swamps the `T = 4m+1` points
   at issue.
10. **`(SAT3)`-conditionality carries forward at `m >= 2`.** The `m=1`
    witnesses are genuinely realized; nothing here builds a realizable pencil
    at any `m >= 2`.

---

## MEASURED FUNCTIONALS (CATCH-19C)

`m, N=16m, rho=4m-1, R=8m, e=m, delta=m-1, T=rho+2, T_1, T_2`; `S_gamma,
u_gamma, O, d_x, A_x, x_0`; `W, a, d = a-(4m+2), need_X = d-m, X_gamma,
n_gamma, ov_gamma, F_gamma, mu(x)`; `H(Z,x)`, `H_t`, `h_gamma`, `deg h_gamma`,
`Rin`, `Rin_mult`, `Rout`, `nonsplit`; layer-A `rank`/`nullity`, the kernel
vector `c_gamma`. **New here:** the exact admissibility predicate (`H(.,x)
!= 0` for every `x in W`) and its linear-algebra test; the **locator span
rank**; the **`c_x` shadow** of layer A and its unknown count
`N + sum_x (m-d_x+1)`; the projective kernel sweep count `admH`; the
factorisation profile `(m_j, d_j)`, `delta_i = deg alpha_i`, the small/big
split, `t`, `M_s`, `M_b`; `max_cover(part, m)`; the W- and A-picture Plücker
budgets. **Registered but not measured:** `Rout` at `m >= 2` (F-C) — I name it
as the deciding quantity and did not measure it; and the `m=3` structured
candidate (D3(c)'s `m=3` half), declared rather than quietly dropped.

---

## COMPLIANCE

**Registrations.** `R0` (the `m=1` arithmetic, derived from the anchors alone
so that the calibration is a test and not a fit), the three mandated blind
priors `R1` with their split, six falsifiable derivations `R2.1-R2.6`, the
MISS-2 guard `R3` in its three clauses, six zero-power flags `R4`, the
subtraction plan `R5`, the expected misses `R6` and the execution order `R7`
were appended to `PREREG.md` under `## Pilot registrations` with the Edit
tool **after reading exactly the two named anchors and before any other read,
any grep, any `ls`, and any interpreter invocation.** No post-registration
addenda; nothing was edited afterwards.

**Compute law — NO BREACH. Seven interpreter invocations, all seven under
`tools/ramguard`, from the repo root, with the literal `--`.** All seven used
the `local` profile: `RAMGUARD_TIMEOUT=280` (`d1_calib`, `d1b_exhaustive`,
`d5_layerA_bank2`, `d2_transverse`) and `RAMGUARD_TIMEOUT=290` (`d3_scale`
`x2`, `d3b_cx_form`). **Zero bare `python3` invocations** — no file patching,
no string replacement, no no-op probe, no empty heredoc; every file edit used
the Edit or Write tool. **Ramguard status: one FAILURE** — invocation 4
(`d3_scale.py`) exited with a `TypeError` (MISS 4), fixed with the Edit tool
and rerun as invocation 5. No timeout kill and no OOM kill on any run.
Stdlib only (`sys`, `random`, `itertools`); no third-party imports, no Modal,
no network, no git, **no subagents spawned**.

**RAM discipline.** `dag.json` **never opened** at any line. File-at-a-time
reads with bounded windows on every large file (`statement.md` by
`sed -n`/`grep -n` only, never in full — windows `582-595` and `3020-3060`;
the saturation node by two windows; the RNC node's statement `1-60,60-95` and
proof `1-45`). All computation is at `q in {17, 97, 193}` on systems of at
most `34` unknowns; the largest object materialised is the `8960`-case `m=1`
sweep, checkpointed by writing each script's own results file.

**Quarantine.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` **never opened and
never appeared in any grep output**. The sibling `r34_*` directories under
`notes/pilots_20260811/` were **never read and never listed**:
`notes/pilots_20260811/` was never `ls`-ed; every directory listing named a
specific permitted subdirectory (`rh_sat3_realizability/`,
`rh_bivariate_system/`); every recursive grep was rooted at `critical/`,
`background/`, or a named node directory, **never at `.` or `notes/`**, so no
`--exclude-dir` was needed and no output filtering was used. No path
containing `prize-codex-` was touched. The round-33 `rh_*` directories were
read as permitted.

**Write scope.** Every write is inside `notes/pilots_20260811/r34_layer_a/`:
`PREREG.md` (registrations appended); verbatim copies `biv_core.py`,
`d4_exhibit_bank2.py`, `d2_hankel_realize_bank3.py`; `d5_layerA_bank2.py`
(bank 2's `d5` with **two disclosed one-line edits** — the `sys.path` insert
now points at my own copy, and the output path now writes
`d3b_replay_results.txt` inside my directory instead of bank 2's, which would
have been an out-of-scope write); my own `d1_calib.py`, `d1b_exhaustive.py`,
`d3_scale.py`, `d3b_cx_form.py`, `d2_transverse.py` and their five results
files, plus `d3b_replay_results.txt` and a `__pycache__` created by the
imports. **`REPORT.md` itself was REFUSED by the harness** ("Subagents should
return findings as text, not write report files"), so this report is returned
verbatim as the final message per the brief's fallback clause; the directory
therefore contains 16 files and no `REPORT.md`. **No** `dag/`, `nodes/`,
`critical/`, `background/`, `experiments/` or `tools/` edits; no git; the
session scratchpad was not needed and not used. AUDIT-AND-DRAFT respected: the
node recommendations in D4 are recommendations only — **nothing was applied**.

**Banked scripts.** `biv_core.py`, `d4_exhibit.py` and `d5_layerA.py` were
copied from `rh_bivariate_system/` **before use**; `diff -q` confirms
`biv_core.py` is byte-identical. `rh_sat3_realizability/d2_hankel_realize.py`
was copied for provenance but **was never executed** — I say so plainly; its
exhaustive scan is re-implemented in `d1_calib.py` and the re-implementation
is checked against the banked output (16 families, both printed witnesses
present). Bank 2's `build_S2` was used unmodified as the second W-layer
builder and agrees with mine `320/320`.

**Method discipline.** Own-repo greps (CATCH-24A) preceded every novelty
claim and produced **eleven subtractions**, one of which (the RNC node) is the
whole of what I would otherwise have claimed as this round's structural
insight. Every quantifier claim carries a `file:line` or an exhaustive count
with its denominator. Every max/min-quantified claim carries a zero-power
declaration. Two-field confirmation on every `m >= 2` structural claim
(`F_97`/`F_193`); the `m=1` single-field limitation is declared as MISS 6 and
zero-power 1 rather than glossed. Three independent builders were made to
agree before any W-layer number was believed. The four self-caught errors —
the `a=7` kernel-sampling artifact, the failed invocation, the control that
never fired, and the near-claim of a proved node — are reported as errors, in
the misses section, ahead of the results.
