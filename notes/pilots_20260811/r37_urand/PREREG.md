# PREREG — r37_urand (round 37)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r36_hrlow/REPORT.md` (round 36)
2. `notes/pilots_20260811/r35_fg_razor/REPORT.md` (round 35)

## Mandate

U-RAND — THE LAST UNPRICED FAR-CA MODE. Round 36 reduced the
far-CA residual to STATEMENT U (every bad slope of a column-far
razor pencil admits a locator inside W = S_1 u S_2), which pins
B_ca^far(k+2^34) = r+1 = 2^39.977280 EXACTLY. U's symmetric mode
is condition-killed at razor rho; the remaining mode — **U-rand:
a bad slope whose EVERY locator escapes W, reaching the syndrome
through a codeword** — is completely unpriced (anchor 1's ZP-13).
The first moment has zero power in this lane (wrong by 6.7e11
bits on LB1, 750x on the symmetry excess). YOUR JOB: give U-rand
its first real pricing — structure, census, and either a fence
(named conditions under which T_rand = 0, proof-shaped) or a
counterexample mechanism (a third structured excess). Two cheap
secondaries the round-36 close queued: the rho = 3 symmetric-T
measurement (anchor 1's parity derivation predicts survival at
rho = 3, death at rho >= 4 — unmeasured) and the C(128,63)-vs-
C(127,64) correspondence (the T_sym carrier vs the banked qcore
plateau — one binomial step apart, ratio 128/65; if the
Lam-Leung+nesting cap transports, T_sym inherits a proved cap).

## Deliverables

**D1 — THE ALGEBRA OF A CODEWORD-MEDIATED SLOPE.** A bad slope
gamma has y_0 + gamma y_1 = syn(u) with supp(u) = S_gamma. With
the forced common-support data (e_0, e_1 on W), u = e_0 + gamma
e_1 + c for a codeword c (possibly 0); U-rand slopes are exactly
those where EVERY choice has c != 0 with supp moving off W.
Derive: what does c != 0 cost (weight/degree bookkeeping of
e_0 + gamma e_1 + c landing at weight <= r with support off W)?
Is there a c-side analogue of the fibre map chi? The exact
incidence frame (HS1/HS3) is the banked instrument.

**D2 — THE CENSUS.** At razor-faithful cells (the mandatory
faithfulness conditions: a > R+1, a-1 > r, 4rho < R) across the
mu_1 range, split every measured T into T_fib + T_sym + T_rand
(anchor 1's decomposition) and characterize the T_rand
population: Poisson-like (matches the null in distribution AND
in structure) or carrying its own mechanism? Any structured
T_rand family found = the round's headline (a third excess). Any
clean null = the evidence base for the fence.

**D3 — THE FENCE ATTEMPT + THE TWO SECONDARIES.** (a) Attempt:
named conditions (on q, the domain, the pencil) under which
T_rand = 0 provably — even a partial fence (e.g. T_rand = 0 for
slopes outside a named exceptional set) shapes Statement U's
proof. (b) The rho = 3 symmetric-T cell (two fields — decides
anchor 1's parity prediction and firms the M >= rho threshold).
(c) The C(128,63) correspondence: identify both objects exactly
(the T_sym carrier at M = rho vs the banked plateau's qcore
object), determine whether the banked cap transports, and state
the consequence either way.

**D4 — VERDICT.** U's status after the round (both modes priced /
one still open, with what evidence); the far-CA residual map;
misses first; cross-pilot flag (do NOT read siblings). Remember:
the type-2 ledger is VACUOUS on the bracket (do not import);
q_crit/theta are razor-row constants.

## Blind priors to register

P(T_rand carries a structured mechanism), P(a fence lands this
round), P(the rho=3 symmetric-T survives — anchor 1 predicted
yes), P(the C(128,63) cap transports), P(Statement U's status
improves to one-mode-open-with-evidence).

---

## Pilot registrations

**Provenance statement (honesty).** Written after reading exactly
`CONSTRAINTS.md`, this `PREREG.md`, and the two named anchors
(`r36_hrlow/REPORT.md`, `r35_fg_razor/REPORT.md`) — and nothing
else. No grep, no `ls`, no interpreter invocation, no third file
read has occurred. Every derivation in R2 below was done **in
head** from the two anchors before this block was written; the
razor closed forms in R3-A are in-head arithmetic and are
registered as falsifiable numbers, to be confirmed or refuted by
run 4. A-8 and A-9 are marked **semi-blind** (they are calibrated
against anchor 1's published `T` rows for shape H1). No
registration will be edited after this block is appended.

### R1 — Dictionary, cells, and the MANDATORY faithfulness gate

Conventions inherited from the anchors: `v_x = 1/prod_{y!=x}(x-y)`,
`y_m = sum_{x in D} e(x) v_x x^m` for `m = 0..R-1`,
`M_r(y) = (y_{i+j})_{0<=i<rho, 0<=j<=r}` (a `rho x (r+1)` Hankel),
low-to-high coefficient order; `n = |D|`, `k`, `R = n-k`, `r = n-a`,
`rho = R-r = a-k`; rate half means `k = R = n/2`. A **bad slope**
`gamma` is one with a **split** locator `sigma` (deg `<= r`,
distinct roots `S_gamma subset D`) satisfying
`(M_0 + gamma M_1) sigma = 0` (HS1/HS3). **Column-far** = no `sigma`
with `M_0 sigma = M_1 sigma = 0`.

**FAITHFULNESS IS MANDATORY ON EVERY CELL.** Every row of every
results file will print `4rho<R`, `a>R+1`, `a-1>r` and I will use
**no** row where any of the three is False. At rate half these
reduce to `4rho < R` (since `a>R+1 <=> rho>1` and `a-1>r <=>
2rho>1`), so every registered cell has `rho >= 2` and `R > 4rho`.

Registered cells (negation-closed domain `D = {+-1,...,+-m}`,
`n = 2m = 2R`, `k = R`; this is the round-36 stand-in for the
official row's multiplicative subgroup, which is negation-closed):

| id | n | k | R | rho | r | a | m | `4rho<R` | `a>R+1` | `a-1>r` | `C(n,r)` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 20 | 10 | 10 | 2 | 8 | 12 | 10 | T | T | T | 125,970 |
| C2 | 24 | 12 | 12 | 2 | 10 | 14 | 12 | T | T | T | 1,961,256 |
| C3 | 28 | 14 | 14 | 3 | 11 | 17 | 14 | T | T | T | 21,474,180 |
| C4 | 34 | 17 | 17 | 4 | 13 | 21 | 17 | T | T | T | 927,983,760 |
| C5 | 26 | 13 | 13 | 3 | 10 | 16 | 13 | T | T | T | 5,311,735 |
| K1 (control domain) | 20 | 10 | 10 | 2 | 8 | 12 | — | T | T | T | 125,970 |

C1/C2 carry the **exhaustive total-`T` census**. C3/C4/C5 are
**carrier-only** (their `C(n,r)` is out of stdlib reach inside the
ramguard window — anchor 1 miss 10 / ZP-10, re-declared here as
ZP-4). K1 is C1's shape on the **non**-negation-closed
`D = {1,...,20}`, the two-field control that separates `T_sym`
from the domain.

Fields: `q in {101, 349, 1009, 10007, 65537, 999983}`.
**I register the upper end `q <= 999983` NOW** so that no
"disclosed widening" is needed (anchor 1 miss 9, anchor 2 miss 7).

Families (all with `W = supp(e_0) u supp(e_1) = T`, `|T| = r+1`,
so `f = |W|-r = 1` — the extremal `f=1` stratum where Statement U
is load-bearing):
- **F1 (LB1)**: `T` one-sided (`T subset {1..m}`), `e_0 = 1`,
  `e_1 = x` on `T`. `d = deg L = 1`.
- **F2 (d2-inj)**: `T` one-sided, `e_0 = 1`, `e_1 = x^2`. `d = 2`.
  This is anchor 1's `T = 95 vs r+1 = 9` cell.
- **F3 (d2-sym)**: `T` symmetric (`T = -T`, needs `r+1` even),
  `e_0 = 1`, `e_1 = x^2`. Anchor 1's **second**, larger mechanism.
- **F4 (constructed)**: see R6-c.

### R2 — Falsifiable derivations, committed IN ADVANCE

Let `syn : F_q^D -> F_q^R`, `syn(u)_m = sum_x u(x) v_x x^m`,
`m = 0..R-1`.

**(R2a) The code.** `C := ker syn = { g|_D : deg g <= k-1 }`, an
`[n,k]` **MDS** (generalised Reed-Solomon) code, minimum distance
`d_min = n-k+1 = R+1`. *Reason:* `sum_{x in D} v_x x^j = 0` for
`j <= n-2`, so `deg(g) <= k-1` kills every moment `m <= R-1`;
dimensions match. **Prediction (proof-shaped, to be machine
checked at >= 2 fields, >= 2 shapes): every nonzero `c in C` has
`wt(c) >= R+1`, and the minimum-weight codewords are exactly
`c = lambda * prod_{y in Y}(x-y)|_D` for `(k-1)`-subsets
`Y subset D`, `lambda != 0`, with `supp(c) = D \ Y` of size
exactly `R+1`.**

**(R2b) The codeword decomposition.** For any bad slope `gamma`
with error `u` (`supp u subset S_gamma`, `wt u <= r`) and the
forced common-support data `(e_0,e_1)` on `W` (anchor 1's
common-support theorem), `h_gamma := (e_0 + gamma e_1)|_W`
satisfies `syn(h_gamma) = y_0 + gamma y_1 = syn(u)`, hence
```
    u  =  h_gamma  +  c ,     c in C .
```
`c = 0` <=> the slope is **fibre** (`T_fib`); `c != 0` <=>
**codeword-mediated**. `T_rand` = codeword-mediated and NOT
explained by a domain automorphism (`T_sym`).

**(R2c) THE SPEND LAW — the unconditional partial fence.** Write
`t := |S_gamma \ W|`. Then `c` is supported on `S_gamma u W`, so
`c != 0` forces `|S_gamma u W| >= R+1`, i.e.
```
    t  >=  R + 1 - |W|  =  rho + 1 - f      ( = rho when f = 1 ).
```
Contrapositive, and this is the fence I commit to:
> **FENCE-1 (unconditional).** If `|S_gamma u W| <= R` then
> `c = 0`: `u = h_gamma`, `supp(h_gamma) subset S_gamma n W
> subset W`, and `gamma` is a fibre slope with a locator inside
> `W`. **No bad slope whose locator spends fewer than
> `rho+1-f` points off `W` can be U-rand.**

**Registered prediction A-6: 100% of measured codeword-mediated
incidences satisfy `t >= rho+1-f`, at >= 2 fields and >= 2
shapes; a single counterexample REFUTES FENCE-1 and I will report
it as the round's headline miss.**

**(R2d) `W`-rigidity.** If `|W| <= R` then the `W`-supported
representative pair `(e_0,e_1)` with `syn(e_i) = y_i` is
**unique** (a difference would be a nonzero codeword inside `W`,
weight `<= |W| <= R < R+1`). At `f = 1` and rate half,
`|W| = r+1 <= R` always. So `W`, `e_0`, `e_1`, `chi` are
canonical, not choices.

**(R2e) THE `rho-1` OVER-DETERMINATION LAW (three independent
derivations, all committed now).**
*(i) Degree bookkeeping.* `c = g|_D`, `deg g <= k-1`; `g` vanishes
on `D \ (S u W)` (size `n-|W|-t`), so `g = Z * m` with
`Z = prod_{y in D\(SuW)}(x-y)` and `deg m <= (k-1)-(n-|W|-t) =
|W|+t-R-1`. The prescribed values on `W \ S` (size `f+t`) give
`f+t` equations in `(|W|+t-R)` coefficients of `m` **plus** the
one unknown `gamma`, and the system is **linear in `(m,gamma)`
jointly**. Net over-determination
```
    (f+t) - (|W|+t-R) - 1  =  R - r - 1  =  rho - 1 ,
```
**independent of `t` and of `f`.**
*(ii) Linear algebra.* Same count read off the affine system
`m(x) Z(x) + e_0(x) + gamma e_1(x) = 0`, `x in W\S`.
*(iii) Geometry.* Put `V_S := syn(F_q^S)`, an `|S|`-dimensional
subspace of `F_q^R` (MDS => `syn` injective on any set of size
`<= R`). Then:
- `gamma` is bad via `S` <=> the affine line
  `l = { y_0 + gamma y_1 }` meets `V_S`;
- **column-far <=> no `V_S` contains `l`**, hence **every `S`
  contributes AT MOST ONE slope** (this is the exact reason `T`
  is a count of incidences, one per locator);
- at `f = 1`, `l subset V_W` (dim `r+1`), and `syn|_{F_q^W}` is
  an isomorphism onto `V_W`;
- **`|S u W| <= R  =>  V_S n V_W = V_{S n W}`** (a difference lies
  in `C` and is supported on `S u W`) — codimension `|W \ S|` in
  `V_W`; for `S subset W` that codimension is `1` (this IS `chi`);
- **`|S u W| >= R+1  =>  codim_{V_W}(V_S n V_W) = rho`** generically,
  so an affine line meets it only under `rho` conditions on one
  unknown: **`rho - 1` over-determination.**

So the transition fibre -> codeword-mediated is exactly the jump
**codim `1` -> codim `rho`**: the effective fibre parameter jumps
from `f` to `rho`.

**(R2f) The exact criterion (to be used as the census oracle).**
With `sigma_S` the split locator of `S`, `M_0 sigma_S` and
`M_1 sigma_S` are the images of `y_0, y_1` in
`V_W/(V_S n V_W) ~= F_q^rho`. Then
```
  S gives a bad slope  <=>  M_0 sigma_S and M_1 sigma_S are
                            PROPORTIONAL in F_q^rho, not both 0 ;
  gamma = -(M_0 sigma_S)_i / (M_1 sigma_S)_i .
  T_rand = 0  <=>  for every S with |S u W| >= R+1, the 2 x rho
                   matrix [M_0 sigma_S ; M_1 sigma_S] has RANK 2.
```
I register that this is the **standard key-equation test in
geometric clothing** and that its novelty (CATCH-24A) is only the
`V_W/(V_S n V_W)` reading, not the test.

**(R2g) MINIMAL-SPEND RIGIDITY.** At `f = 1` and minimal spend
`t = rho`: `wt(u) = |supp(c)\W| + |{x in W : h+c != 0}| <= r`
forces `|A| >= t+1` where `A = {x in W : c(x) = -h_gamma(x)}`;
`c` is nonzero on `A` minus at most the single point
`chi^{-1}(gamma)`, so `|supp(c) n W| >= R+1-t = r+1 = |W|`, i.e.
```
  c is a MINIMUM-WEIGHT codeword: wt(c) = R+1 exactly,
  supp(c) = W u (S \ W)  ⊇  W ,  and  c = lambda * Z_Y|_D
  with Y = D \ supp(c), |Y| = k-1, Y n W = empty.
```
**Registered prediction A-7: every minimal-spend U-rand
incidence found has `wt(c) = R+1` exactly and `W subset supp(c)`,
at >= 2 fields.** A minimal-spend incidence with `wt(c) > R+1`
REFUTES R2g.

**(R2h) THE `c`-SIDE ANALOGUE OF `chi`, NAMED.** Define, for each
admissible `Y` (`(k-1)`-subset of `D` disjoint from `W`),
```
    chi_Y : W -> P^2 ,   x |-> [ Z_Y(x) : e_0(x) : e_1(x) ] .
```
Then, at minimal spend, `gamma` is U-rand via `Y` **iff some line
of the dual plane meets `chi_Y(W)` in at least `rho+1` points**
(the line `lambda X_0 + X_1 + gamma X_2 = 0`). The fibre map
`chi` is the degeneration `Z_Y == 0`, where the requirement drops
to `>= f = 1` point. **`chi` asks for a fibre of size `f`;
`chi_Y` asks for a collinear set of size `rho+1`.** This is my
answer to D1's "is there a `c`-side analogue of `chi`".

**(R2i) THE PARAMETER-COUNTING PRICE (heuristic, zero proof
power — see ZP-6).** The adversary's free data at `f = 1` is
`(e_0,e_1) in (F_q^W)^2`, i.e. `2|W| = 2(r+1)` parameters. By
R2e each extra codeword-mediated slope is `rho-1` net conditions.
Hence
```
    T_rand  <=~  2(r+1)/(rho-1)      (parameter-counting cap)
```
and at the razor `2(r+1)/(rho-1) = 2*1,082,331,758,593 /
17,179,869,183 = 126.0000000075 -> floor 126`. **Registered as a
falsifiable number (A-2) and as a HEURISTIC, not a bound.** If it
is right, `T_rand` is `O(n/rho) = O(128)` — additive, not
multiplicative — and `B_ca^far(k+2^34) <= r+1 + O(n/rho)` under U's
symmetric mode being dead. At the small cells `2(r+1)/(rho-1)` is
`18` (C1), `22` (C2), `12` (C3), `28/3=9.33` (C4): **too weak to
test the razor scaling**, and I say so in advance (ZP-5).

**(R2j) Why a structured U-rand family is HARD (the fence's
heuristic half).** A U-rand `c` must vanish on `D \ (S u W)`,
a set of size `>= n - |W| - t`. For `c` to carry *algebraic*
structure its zero set must be an orbit union of a subgroup of
`D`, and then `c = L_B(X) G(X^M)` — which is exactly the banked
orbit-invariant locator algebra, i.e. **the U-sym mode**, already
killed at razor `rho`. **Registered prediction: any structured
`T_rand` family I find will be a disguised `T_sym` family
(P = 0.55); a genuinely non-symmetric structured family is the
round's headline (P = 0.30).**

### R3 — Blind priors

**The five the brief demands:**

| id | prior | P |
|---|---|---|
| B-1 | `T_rand` carries a structured mechanism (a third excess, not a disguised `T_sym`) | **0.30** |
| B-2 | a fence lands this round — *full* fence (`T_rand = 0` provably at razor) | **0.10** |
| B-2' | a fence lands this round — *partial*, proof-shaped, named exceptional set (FENCE-1 or better) | **0.80** |
| B-3 | the `rho = 3` symmetric-`T` mechanism SURVIVES (anchor 1's parity prediction) | **0.62** |
| B-3' | it dies at `rho = 4` (the other half of anchor 1's prediction) | **0.78** |
| B-4 | the `C(128,63)` cap transports from the banked `C(127,64)` plateau | **0.25** |
| B-5 | Statement U's status improves to one-mode-open-**with-evidence** | **0.70** |

**Supporting priors:**

| id | prior | P |
|---|---|---|
| B-6 | FENCE-1 (R2c) holds at 100% of measured incidences | 0.93 |
| B-7 | R2g minimal-spend rigidity holds at 100% of measured minimal-spend incidences | 0.72 |
| B-8 | `T_rand` at the two large fields is Poisson-null-compatible at C1 (matches `N_rand * q^{1-rho}` within a factor 4) | 0.60 |
| B-9 | the spend distribution of `T_rand` incidences CONCENTRATES at `t = rho` (i.e. is NOT null-like) | 0.40 |
| B-10 | I can CONSTRUCT a U-rand slope to order (R6-c), >= 2 fields | 0.75 |
| B-11 | the construction STACKS: `j >= 3` simultaneous engineered U-rand slopes on one pencil | 0.45 |
| B-12 | `B_ca^far(k+2^34) < 2^128` moves | **0.03** |
| B-13 | I find >= 1 banked statement needing correction | 0.75 |
| B-14 | at least one of my own registered predictions is REFUTED by my own runs | 0.70 |

**A-predictions (exact numbers, committed now, in-head):**

- **A-1.** `C(127,64) = C(127,63)` exactly; `C(128,63)/C(127,64) =
  128/65 = 1.9692307692...`; `log2(128/65) = 0.977488`;
  `log2 C(127,64) = 123.1714` (anchor 1's banked value);
  `log2 C(128,63) = 124.1489`. **And a NEAR-COINCIDENCE warning
  registered in advance (anchor 2 miss 5 class):
  `log2(128/65) = 0.977488` is NOT `log2((r+1)/2^39) = 0.977280`;
  they differ in the 4th decimal and I will not read them as the
  same number.**
- **A-2.** `r+1 = 1,082,331,758,593 = 2^39.977280`;
  `rho-1 = 17,179,869,183`; `2(r+1)/(rho-1) = 126.0000000075`,
  floor `126`; `n/rho = 128`; `r/rho = 63`.
- **A-3.** `mu_1 = C(n,r)/q^rho` at C1 = `12.349, 1.0342, 0.12373,
  0.0012579, 2.9329e-05, 1.2597e-07` at `q = 101, 349, 1009,
  10007, 65537, 999983` (cross-check against anchor 1 and 2).
- **A-4.** C1/F1 (LB1) at `q >= 65537`: `T = T_fib = r+1 = 9`,
  `T_sym = T_rand = 0`.
- **A-5.** C1/F2 at `q >= 65537`: `T_fib = 9`, `T_sym = 84 =
  C(m-1, r/2-1) = C(9,3)`, `T_rand` small (`<= 4`). Total
  `T in {93,...,98}` — anchor 1 measured `98` and `95`.
- **A-6.** (R2c) 100% of codeword-mediated incidences have
  `t >= rho+1-f`.
- **A-7.** (R2g) 100% of minimal-spend incidences have
  `wt(c) = R+1` and `W subset supp(c)`.
- **A-8** *(semi-blind — calibrated on anchor 1's `T` rows)*.
  `T_rand ~ N_rand * q^{1-rho}` where `N_rand = #{S : |S u W| >=
  R+1, S != -S}`; Poisson envelope `T_rand <= N_rand q^{1-rho} +
  3 sqrt(N_rand q^{1-rho}) + 3`, at >= 4 (cell, field) rows.
- **A-9** *(semi-blind)*. The `t`-histogram of `T_rand`
  incidences is statistically indistinguishable from the
  `t`-histogram of all `S` with `t >= rho` (no concentration).
- **A-10.** `T_sym(rho=3, symmetric-T) > 0` and
  `T_sym(rho=4, symmetric-T) = 0`, each at 2 fields.
- **A-11.** K1 (non-negation-closed control, C1 shape, F2 family)
  at `q >= 65537`: `T_sym = 0` and `T <= 12`.

### R4 — MISS-2 GUARD (mean-vs-max), six clauses, binding

1. **MAX, NOT MEAN.** Every `T`, `T_fib`, `T_sym`, `T_rand` used
   against any cap or floor is an **exact exhaustive count** or an
   explicit **max/min over a named finite set**. No mean, median
   or average appears in any conclusion. Where I report a mean
   (e.g. a `t`-histogram centroid) it is labelled a *descriptor*
   and carries no verdict.
2. **The first moment has ZERO POWER in both directions** (anchor
   1 ZP-3, anchor 2 ZP-3): it is wrong by `6.7e11` bits downward
   on LB1 and by `750x` downward on the symmetry excess. I will
   **exhibit** it failing rather than trust it, and no `E[T]`
   supports any verdict. In particular **B-8 being HIT does not
   establish that `T_rand` is null** — only that C1 shows no
   excess at C1.
3. **EMPTINESS IS NEVER PROMOTED FROM A CENSUS.** A measured
   `T_rand = 0` at a cell is `T_rand = 0` **at that cell**, never
   "`T_rand = 0`". Anchor 1 miss 2 is the model: a cap proved for
   one sub-count was read as a cap on the total.
4. **CODIMENSION IS NOT EMPTINESS.** R2e's `rho-1`
   over-determination is a *codimension* statement. It does **not**
   prove `T_rand = 0`, and R2i's parameter count is a *heuristic*
   dimension count over a finite field, which is not a proof. Both
   are declared zero-power for any bound (ZP-6).
5. **`T`, `T_fib`, `T_sym`, `T_rand` are FOUR different
   functionals** and I never equate any two, nor read a bound on
   one as a bound on another. `T = T_fib + T_sym + T_rand` is a
   *definition by classification*, and the classification rule is
   printed per incidence.
6. **AVERAGING OVER PENCILS IS FORBIDDEN AS EVIDENCE.**
   `B_ca^far` is a **max over column-far pencils**. Any union
   bound or "almost all pencils" statement is a statement about a
   mean and has zero power against a max. I pre-commit: if my
   parameter count or a union bound comes out favourable I will
   report it as **`P(random pencil)`, never as `B_ca^far`**.

### R5 — ZERO-POWER PRE-DECLARATIONS

- **ZP-1.** No razor-scale computation will exist. All machine
  numbers at `q <= 999983`, `R <= 17`, `rho <= 4`, `r <= 13`.
  Every razor number is a closed-form evaluation.
- **ZP-2.** Zero power from any non-faithful cell. Every row prints
  `4rho<R`, `a>R+1`, `a-1>r`; rows failing any of the three are
  excluded from every conclusion (anchor 2 miss 1).
- **ZP-3.** The first-moment / Poisson model has zero power in
  both directions (R4.2).
- **ZP-4.** **No exhaustive total-`T` census will exist at
  `rho >= 3`** (`C(26,10) = 5,311,735`, `C(28,11) = 21,474,180`,
  `C(34,13) = 9.3e8` are out of stdlib reach in the ramguard
  window). All `rho = 3,4` evidence is **carrier-restricted** (a
  complete sweep of a NAMED sub-family) plus exact structural
  verification. Statements of the form "`T_rand` is small at
  `rho = 3`" are NOT supported and I will not make them.
- **ZP-5.** The parameter-counting cap (R2i) cannot be tested at
  my cells: `2(r+1)/(rho-1)` is `18/22/12/9` there versus `126` at
  the razor, and small `rho` makes it vacuous. I claim **zero
  power on the razor value of the cap**; it is a closed form and a
  heuristic, nothing else.
- **ZP-6.** **Codimension/dimension counting is not a proof.** R2e
  and R2i price `T_rand`; they do not bound it. Any fence I report
  is either (a) unconditional and proof-shaped (FENCE-1), or (b)
  explicitly conditional on a NAMED hypothesis, stated as a
  hypothesis.
- **ZP-7.** Zero power over `char F_q`: every field used is an odd
  prime. Char-2 and non-prime `q` (Frobenius/subfield mechanisms
  for `c`) are **declared unmeasured**.
- **ZP-8.** The type-2 ledger `(C2)/(C3)/(C4)` is **VACUOUS on the
  bracket** (anchor 2 D2.2) and will **not** be imported. Every
  cap here is derived from MDS distance / pigeonhole / degree
  counting in this document. `q_crit`, `theta_1 = 127.977457`,
  `theta_2 = 63.988728` are **razor-row constants** and will not
  be used as row-level constants.
- **ZP-9.** Every structural claim will carry **>= 2 fields**;
  claims that carry only one shape will be labelled as such.
- **ZP-10.** I will not read any sibling round-37 directory
  (`r37_third_solve`, `r37_share3_gap`, `r37_mint_drafts`), and I
  will not `ls` the parent. Names taken from `CONSTRAINTS.md:38-39`.
- **ZP-11.** `T_sym` classification is by the operational test
  "the incidence has an even locator (`S = -S`)". A codeword-
  mediated slope carried by a *different* automorphism of `D`
  would be misclassified as `T_rand`. I declare this in advance
  and will report the automorphism group actually tested
  (`x -> -x` only).
- **ZP-12.** Anchor 1's `C(128,63)` correspondence: I will compute
  both integers and the ratio, and I will read `rate_half_band_
  closure/node.json` to identify the banked object. If the banked
  object's *definition* is not verbatim recoverable from a bounded
  window, I will say **"not identified"** rather than guess.

### R6 — Deliverable registrations and falsifiers

**(a) D1.** Deliver R2a-R2h as a derivation, each clause either
machine-confirmed at `>= 2` fields or explicitly marked
"derivation only". **Falsifier F-1:** any codeword-mediated
incidence with `|S u W| <= R` (kills FENCE-1 and R2a's MDS
distance simultaneously — a two-way check).

**(b) D2.** Exhaustive census at C1 (6 fields) and C2 (>= 2
fields), families F1/F2/F3, plus K1 control. Per bad slope:
`T_fib`/`T_sym`/`T_rand` label, the spend `t`, `wt(c)`,
`|supp(c) n W|`, and whether `c` is minimum weight. **Falsifier
F-2:** a `T_rand` family whose `t`-histogram is concentrated at a
single value across `>= 2` fields AND whose count is field-size
independent = a **third structured excess** (B-1 fires; headline).
**Falsifier F-3:** `T_rand` growing with `C(n,r)` at fixed
`q^{1-rho}`-normalisation beyond the Poisson envelope at `>= 2`
cells.

**(c) D3.** (i) FENCE-1 as the unconditional partial fence, plus a
**conditional fence** stated as: *if for every `(k-1)`-subset `Y`
disjoint from `W` the image `chi_Y(W) subset P^2` has no `rho+1`
collinear points, then `T_rand^{minimal-spend} = 0`* — a named
hypothesis, registered as a hypothesis. (ii) **Constructive
attempt (F4 family):** pick `Y`, pick `A subset W` with
`|A| = rho+1`, pick `lambda`, and DEFINE `e_0(x) := -lambda Z_Y(x)`
on `A` (with `gamma = 0`), then re-derive `W` from the resulting
pencil and check column-farness and `f = 1`. If a U-rand slope
appears **and** `W` is still the forced common support, that is a
constructed third excess. Registered B-10 = 0.75, B-11 = 0.45.
(iii) The `rho = 3` / `rho = 4` symmetric-`T` measurement at C3
(`r+1 = 12` even, so a symmetric `T` exists) and C4
(`r+1 = 14` even), 2 fields each, with C1 as the `rho = 2`
positive control. (iv) `C(128,63)` vs `C(127,64)`.

**(d) D4.** Verdict, far-CA residual map, misses first, cross-pilot
flag. **No node surgery** — AUDIT-AND-DRAFT; all corrections go to
the coordinator as flags.

### R7 — Compute plan

**<= 6 interpreter invocations, ALL via `tools/ramguard`** from the
repo root with a literal `--` and an explicit `RAMGUARD_TIMEOUT`.
Zero bare `python3` for any purpose whatsoever — including
patching, probing, no-ops and empty heredocs. Stdlib only
(`sys`, `math`, `itertools`). No Modal, no network, no git, no
subagents.

1. `g1_census.py` — C1 total census, 6 fields, F1/F2/F3 + K1
   control (`local`, 290s).
2. `g2_rand.py` — codeword extraction, spend/weight/min-weight
   statistics, FENCE-1 and R2g checks (`local`, 290s).
3. `g3_sym.py` — symmetric-`T` carrier at `rho = 2,3,4`
   (C1/C3/C4/C5), 2 fields (`local`, 290s).
4. `g4_razor.py` — closed forms incl. `C(128,63)`, `C(127,64)`,
   `2(r+1)/(rho-1)` (`tiny`, 55s).
5. `g5_construct.py` — the F4 constructive attempt (`local`, 290s).
6. reserve (C2 second-shape census).

**RESULTS-FILE RULES (round-36 losses, binding):** every results
file is opened in **append** mode (`"a"`) or versioned per run;
**never** a blind `"w"`. **No results-producing run is ever piped
through `head`** (anchor 1 miss 1: SIGPIPE destroyed a run) —
scripts write their own files and stdout is inspected afterwards
with `tail`/`sed -n`/`grep`.

**IMPORTED-SCRIPT RULE:** I pre-commit to importing and executing
**zero** banked scripts. Every script is a fresh implementation
against the anchors' conventions. If I nonetheless copy one, I
will `grep` it for `open(` / `write` / results paths and repoint
them with the **Edit** tool BEFORE the first import, since imports
can write at import time.

**WRITE DISCIPLINE:** every file edit through Edit/Write. No
`sed -i`, `awk -i`, `perl -i`, `tee`, or shell redirection onto any
file. Read-only shell (`grep`, `sed -n`, `tail`, `wc`) for
inspection only. Every recursive grep carries, at search level:
`--exclude-dir=r37_third_solve --exclude-dir=r37_share3_gap
--exclude-dir=r37_mint_drafts --exclude-dir=pilots_20260802
--exclude-dir='prize-codex-*' --exclude-dir=.git
--exclude-dir=__pycache__ --exclude=dag.json`.
