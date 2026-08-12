# PREREG — r38_urate_genericity (round 38)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r37_urand/REPORT.md` (round 37)
2. `background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md`

## Mandate

R-URATE + R-GENERICITY — the two finite lemmas that pin the
far-CA count. Round 37 refuted Statement U and re-priced
B_ca^far(k+2^34) = r+1 + Theta(n/rho): the constructive floor
r+1+126 needs R-GENERICITY (the engineering matrix has full rank
j(rho+1) at razor parameters and a kernel vector exists meeting
the four open side-conditions — each held 60/60 at every
reachable cell); the matching cap needs R-URATE (the exchange
rate rho is tight: T_rand <= 2(r+1)/rho, a rank statement on the
j(rho+1) x (2(r+1)+j) incidence matrix). Both are self-contained
linear algebra over F_q[x]. YOUR JOB: prove them — or find the
structured rank-drop that breaks them (which would mean MORE
U-rand slopes than the cap, moving the count again). SECONDARY:
the carrier-exhaustiveness residue (is (X-x_0)P(X^2) the ONLY
parity-collapsing carrier at odd r? — closes R-USYM completely).

## Deliverables

**D1 — THE MATRIX, STRUCTURED.** The engineering system: rows =
j blocks of (rho+1) evaluations lambda_i Z_{Y_i}(x) + e_0(x) +
gamma_i e_1(x) = 0 on A_i; unknowns = (e_0,e_1) on W (2(r+1)
values) + lambda_1..j. Its structure: Vandermonde-like blocks
glued along the shared (e_0,e_1) columns. Derive when it has
full rank: transversality of the A_i (pairwise intersections?),
the Z_{Y_i} nonvanishing pattern, char conditions. A CLEAN
sufficient condition (e.g. "the A_i pairwise intersect in
< rho+1 points and the Y_i are distinct") provable by a
Vandermonde/exchange argument would BE R-GENERICITY's rank half.

**D2 — R-URATE.** The cap direction: show no configuration of
j > (2(r+1)-1)/rho codeword-mediated slopes is consistent — i.e.
the joint system for j slopes ALWAYS has only the zero solution
past the cap (the pilot's kernel arithmetic says dim would go
negative; the gap is whether NON-minimal-spend or mixed-spend
configurations evade the count — the rho-1 law is
spend-independent, so derive the joint version: j slopes at
arbitrary spends cost SUM of what? prove the additivity or find
the discount). If additivity holds, R-URATE follows and
B_ca^far(k+2^34) = r+1 + 126 EXACTLY (modulo D1's half).

**D3 — THE SIDE-CONDITIONS + THE CARRIER RESIDUE.** (a) The four
genericity side-conditions (lambda_i != 0; chi injective on W;
gamma_i off the fibre slopes; column-farness): show each is a
nonempty Zariski-open on the kernel (or exhibit the failure).
Measure at 2-3 more cells to tighten the 60/60. (b) The
carrier-exhaustiveness question: classify error supports T with
e_1/e_0 = x^2 whose parity collapse survives — is the
(X-x_0)P(X^2) family everything at odd r? A completeness lemma
closes R-USYM; a new carrier re-opens it (then measure its
threshold).

**D4 — VERDICT.** The far-CA pin's status (unconditional /
still-modulo-what); misses first; cross-pilot flag (do NOT read
siblings). Faithfulness conditions mandatory on all cells.

## Blind priors to register

P(D1's rank half proved), P(R-URATE's additivity holds),
P(the +126 becomes unconditional this round), P(a new carrier
exists), P(the count moves AGAIN (cap broken)).

---

# Pilot registrations (r38_urate_genericity)

**Provenance disclosure, up front.** Everything below was written after
reading exactly two files — `r37_urand/REPORT.md` and
`rate_half_ca_hankel_split_pencil_equivalence/statement.md` — and
NOTHING else. No grep, no `ls`, no interpreter, no third read preceded
this block. Every derivation in R2 and every razor constant in R3-A was
carried out **in head** from those two anchors before writing; they are
registered as PREDICTIONS to be machine-checked, not as results. Where a
derivation is only sketched in head I say so.

## R1 — Dictionary, razor constants (blind), faithfulness-gated cells

**R1.1 Dictionary (fixed for the round).** `C = RS[F_q, D, k]`, `n=|D|`,
`R=n-k`, `d_min=R+1` (MDS). `rho := R-r`. Split-locator degree `r`.
`W` = the common support carrying `(e_0,e_1)`, `|W| = r+f`; **this round
is the `f = 1` stratum throughout, so `|W| = r+1`**. `h_gamma :=
(e_0+gamma e_1)|_W`. `u = h_gamma + c`, `c in C`; `c = 0` <=> fibre
slope. `chi : W -> P^1`, `x |-> [e_0(x):e_1(x)]`; fibre slopes are
`{-e_0(x)/e_1(x)}`, so `T_fib = |chi(W)|`. Engineering data per slope
`i`: `P_i subset D\W` with `|P_i| = rho + s_i` (`s_i >= 0` = excess
spend), `A_i subset W` with `|A_i| >= |P_i|+1`, `Y_i := (D\W)\P_i`
(`|Y_i| = k-1` at `s_i = 0`), `Z_Y(x) := prod_{y in Y}(x-y)`,
`Z_{Y_i}(x) != 0` for all `x in W` (since `Y_i n W = empty`) — I call
this **the nonvanishing pattern** and it is used in every argument below.
`a` = the anchors' fourth cell parameter, `a = R+2` at every anchor cell.
**Faithfulness gate (mandatory on EVERY cell I report): `a > R+1`,
`a-1 > r`, `4rho < R`.** Any cell failing any of the three is excluded
from every conclusion, and I will print the three booleans per row.

**R1.2 Razor constants, registered BLIND (in-head arithmetic, to be
machine-checked; any disagreement is a MISS I will report as such).**

```
rho = 2^34 = 17,179,869,184        R = 2^40 = 64 rho        k = R
n   = 2^41 = 2,199,023,255,552     r = 63 rho = 1,082,331,758,592
r+1 = 1,082,331,758,593            2(r+1) = 2,164,663,517,186
N := |D\W| = n-(r+1) = 1,116,691,496,959 = 65 rho - 1
k-1 = 1,099,511,627,775
(A) 2r/rho          = 126        EXACTLY  (my predicted max j; see R2)
(B) 2(r+1)/(rho+1)  = 125.99999999...  floor 125   [126(rho+1)=2,164,663,517,310 > 2(r+1)]
(C) 2(r-1)/(rho-1)  = 126.0000000072   floor 126   [126(rho-1)=2,164,663,517,058 <= 2(r-1)=2,164,663,517,182]
(D) 2(r-rho) = 124 rho = 2,130,303,778,816 ; sqrt = 1,459,556 (to 7 s.f.)
(E) break-even m* := rho+1-sqrt(2(r-rho)) = 17,178,409,629 (approx)
(F) log2 C(N,rho) ~ N*H2(1/65) = 1.116691497e12 * 0.114676 = 1.2806e11
(G) pigeonhole ceiling m_pig := 1 + floor(log2 C(N,rho)/log2 q) at
    q = 2^128  =>  m_pig ~ 1.0005e9
(H) margin m*/m_pig ~ 17.2                (the round's headline margin)
```

**R1.3 Cell table (all faithful by construction; `a := R+2`).**

| id | n | k | R | r | rho | 4rho<R | C(n,r) | role |
|---|---|---|---|---|---|---|---|---|
| C1 | 20 | 10 | 10 | 8 | 2 | 8<10 | 125,970 | anchor replay, censusable |
| C2 | 24 | 12 | 12 | 10 | 2 | 8<12 | 1,961,256 | anchor replay |
| C3 | 26 | 13 | 13 | 10 | 3 | 12<13 | 5,311,735 | **DISCRIMINATOR #1** |
| C4 | 34 | 17 | 17 | 13 | 4 | 16<17 | 9.3e8 | anchor replay, rank-only |
| C7 | 22 | 11 | 11 | 9 | 2 | 8<11 | 497,420 | **NEW**, censusable |
| C6 | 28 | 14 | 14 | 11 | 3 | 12<14 | 21,474,180 | **NEW**, rank-only |
| C11 | 32 | 16 | 16 | 13 | 3 | 12<16 | 3.5e8 | **NEW, DISCRIMINATOR #2** |
| C9 | 36 | 18 | 18 | 14 | 4 | 16<18 | 5.6e9 | **NEW**, rank-only |

Domain types: `intZ = {+-1..+-n/2}` and `mu_n < F_q^*` (a multiplicative
subgroup, the razor's own type). Every structural claim needs **two
fields** and, where reachable, **two domain types**.

## R2 — Falsifiable derivations (all done in head from the anchors)

**R2a — THE MATRIX IS A LINE-PENCIL INCIDENCE, AND IT DECOUPLES.** Order
the unknowns `(e_0|_W, e_1|_W, lambda_1..lambda_j)`. The row for
`(i, x in A_i)` is `[ delta_x | gamma_i delta_x | 0..Z_{Y_i}(x)..0 ]`.
Hence the system says: **the point `p_x := (e_0(x), e_1(x)) in F^2` lies
on the `d(x)` lines `L_{i,x} : X + gamma_i Y + lambda_i Z_{Y_i}(x) = 0`,
`i in I(x) := {i : x in A_i}`**, and the `A_i`-blocks interact ONLY
through `p_x`. Two lines with distinct `gamma` are never parallel, so:
`d(x) <= 2` is always solvable and determines `p_x`; `d(x) >= 3` is a
**concurrency** condition, `d(x)-2` linear conditions on `lambda`.

**R2b — EXACT RANK FORMULA (registered).** With the `gamma_i` pairwise
distinct and `Y_i n W = empty`, let `d(x) := |I(x)|`, `n_d := #{x:
d(x)=d}`, `L := sum_{x in W} max(d(x)-2, 0)`, and let `Phi` be the
`L x j` concurrency matrix (row for the `s`-th excess line at `x`:
coefficients `Z_{Y_a}(x)(gamma_c-gamma_b)` etc., **all nonzero** by the
nonvanishing pattern + distinctness). Then

```
rank(M) = j(rho+1) - L + rank(Phi)                              (R2b-1)
dim ker(M) = (j - rank Phi) + 2 n_0 + n_1                       (R2b-2)
M has FULL ROW RANK j(rho+1)  <=>  rank(Phi) = L  ( needs L <= j ).
```

**R2c — D1's CLEAN SUFFICIENT CONDITION (this is R-GENERICITY's rank
half).** *If the `gamma_i` are pairwise distinct, `Y_i n W = empty`, and
**every point of `W` lies in at most two of the `A_i`**, then `L = 0`,
`Phi` is empty, `M` has full row rank `j(rho+1)`, `lambda` is
COMPLETELY FREE, and `dim ker M = j + 2(r+1) - j(rho+1) = 2(r+1) -
j rho`.* Feasible iff `j(rho+1) <= 2(r+1)`, i.e. `j <= 125` at the razor
(R1.2-B). Explicit witness: lay `W` in a cycle and take the `A_i` to be
`j` consecutive arcs of length `rho+1` wrapping at most twice. **This is
a Vandermonde/exchange argument (the per-point `2 x d(x)` system with
nodes `gamma_i` has rank `min(2,d(x))`) and it is UNCONDITIONAL.**

**R2d — THE `m = 1` DESIGN, AND WHY 126 IS THE RAZOR NUMBER.** Take one
distinguished `x* in W` lying in ALL `j` sets, and let every other point
of `W` lie in exactly two. Then `sum_x d(x) = j(rho+1) = j + j rho` needs
`j rho = 2(|W|-1) = 2r`, i.e. **`j = 2r/rho`, which at the razor is
`126` EXACTLY** (R1.2-A). The concurrency at `x*` is solved in closed
form: for any `(u,v) := p_{x*} in F^2`,

```
lambda_i = -(u + gamma_i v)/Z_{Y_i}(x*)                          (R2d-1)
```

so `ker Phi` is exactly 2-dimensional, `rank Phi = j-2 = L`, **`M` has
FULL ROW RANK**, and `dim ker M = 2` — which is precisely the "kernel
dimension exactly 2 at `j = 126`" the anchor measured
(`r37_urand/REPORT.md:221`). The `A_i \ {x*}` form a `rho`-regular
multigraph on `j` vertices with `63 rho` edges; the two-layer partition
(two partitions of `W\{x*}` into `63` blocks of size `rho`) realises it.

**R2e — SIDE-CONDITION 1 (`lambda_i != 0`) IS PROVED, NOT GENERIC.** By
(R2d-1), `lambda_i = 0` iff `u + gamma_i v = 0` iff `[u:v] =
[-gamma_i:1]`. So **exactly `j` of the `q+1` projective points of
`ker M` are bad, one per slope**. For `q > 2^128` and `j = 126`,
`q+1-126 > 0`: an explicit finite count, no genericity.

**R2f — SIDE-CONDITION 3 (`gamma_i` off the fibre slopes) IS PROVED.**
For `x in A_i`, `e_0(x)+gamma_i e_1(x) = -lambda_i Z_{Y_i}(x) != 0`
automatically. For `x notin A_i` it is a LINEAR form in `(u,v)`; the
`2x2` matrix `M_x` taking `(u,v)` to `(e_0(x),e_1(x))` has
`det M_x = c_a(x) c_b(x) (gamma_a-gamma_b)^2 != 0` where
`c_i(x) := Z_{Y_i}(x)/Z_{Y_i}(x*)`, so `[1,gamma_i] M_x != 0` and each
form kills at most ONE projective point. Union bound: at most
`j(r+1) ~ 1.36e14` bad points out of `q+1 ~ 3.4e38`. **PROVED.**

**R2g — SIDE-CONDITION 2 (`chi` injective) SPLITS.** `chi(x) = [M_x
(u,v)]` is a projective transform of `[u:v]`, so `chi(x) = chi(y)`
identically iff `M_x prop M_y`. For `x,y` in DIFFERENT block-pairs this
is a nontrivial quadratic in `(u,v)`: `<= 2` bad projective points per
pair, `<= (r+1)^2 ~ 1.2e24 << q`. **PROVED by union bound.** For `x,y`
in the SAME block-pair `(a,b)` it reduces to
`g(x) = g(y)` with `g := Z_{P_b}/Z_{P_a}` (degree `<= rho`), a condition
on the DESIGN, not on `(u,v)`. Multi-edges are forced (a `rho`-regular
simple graph on `126` vertices needs `rho <= 125`), so this residue is
real. **Relaxation registered:** the lower bound only needs
`|chi(W)| + j > r+1`, i.e. **at most `j-1 = 125` collisions are
tolerable**, so `chi` need not be injective.

**R2h — SIDE-CONDITION 4 (column-farness) SPLITS INTO A PROVED CASE AND
A RESIDUE.** Column-close via `S`, `|S| <= r`, means `y_0,y_1 in V_S`.
*Case A, `|S u W| <= R`:* MDS gives `V_S n V_W = V_{S n W}`, so
`supp(e_0) subset S n W`, `|S n W| <= r < r+1` — **contradicted by
`e_0` having full support on `W`**, itself an `(r+1)`-term union bound in
`(u,v)`. **PROVED.** *Case B, `|S u W| >= R+1`:* needs a nonzero `c_0 in
C(S u W)` agreeing with `e_0` on `W\S`; the restriction map
`C(SuW) -> F^{W\S}` is injective (kernel `= C(S) = 0` since `|S| < R`)
with image of codim `R-|S| >= rho`. So Case B is `2rho` conditions per
`S` — and the number of `S` is `C(n,r)`, so any union bound here is a
FIRST MOMENT. **DECLARED as the residue (ZP below); not proved.**

**R2i — R-URATE, THE RIGOROUS PER-SLOPE COST.** For a codeword-mediated
slope at spend `s`, `c_i in C(W u P_i)` has `dim = |P_i|-rho+1`, so
`c_i|_W` ranges in a space `U_i` of that dimension, and vanishing on
`A_i` gives `e_0 + gamma_i e_1 in G_i := U_i + F^{W\A_i}` with

```
codim_{F^W}(G_i) >= (r+1) - (|P_i|-rho+1) - (r+1-|A_i|) >= rho.   (R2i-1)
```

**`rho`, EXACTLY, INDEPENDENT OF THE SPEND `s_i` — a subspace statement,
not a count.** The slope itself is one parameter, so the 2-plane
`Pi := span(e_0,e_1)` must meet the codim-`rho` `G_i` nontrivially:
`rho-1` conditions. This is the anchor's `rho-1` law made rigorous.

**R2j — THE ADDITIVITY, AND THE TRADE-OFF LAW (the round's core
prediction).** In the design direction, additivity is EXACT and given by
(R2b-1). The only way to buy `j > 2r/rho` is a **rank drop in `Phi`**.
The natural rank drop is: let `A* subset W`, `|A*| = m`, lie in all `j`
sets. Then `L_x := {lambda : lambda_i Z_{Y_i}(x) = -(u+gamma_i v)}` is a
2-plane, and `L_x = L_{x'}` iff `Z_{Y_i}(x)/Z_{Y_i}(x')` is independent
of `i`, i.e. iff `Z_{P_i}|_{A*}` are all proportional to one function
`psi`. **When that holds, writing `phi := Z_{D\W}/psi`, the system forces
`e_0 = a phi` and `e_1 = b phi` on `A*` — so `chi` is CONSTANT on `A*`
and `T_fib` loses `m-1`.** Hence

```
T <= (r+2-m) + floor( 2(r+1-m)/(rho+1-m) ) =: T_max(m).           (R2j-1)
```

**Registered evaluation at the razor:** `T_max(0) = (r+1)+126`,
`T_max(1) = (r+1)+126`, `T_max(2) = (r+1)+125`, `T_max(3) = (r+1)+124`;
`T_max` only re-crosses `T_max(1)` once `2(r-rho)/(rho+1-m)^2 >= 1`,
i.e. `m >= m* ~ 1.718e10` (R1.2-E). The rank drop must be REALISED, and
the only mechanism I can see is pigeonhole over `rho`-subsets `P_i`,
which caps `m` at `m_pig ~ 1.0e9` (R1.2-G). **Margin `~17.2x`
(R1.2-H): the cap survives.**

**R2k — THE COSET ATTACK IS CLOSED (in head).** On `D = mu_n`, if `P` is
a coset `cH` of the order-`rho` subgroup then `Z_P(X) = X^rho - c^rho`.
Requiring `X^rho - c_i^rho = mu_i psi(X)` on `A*` for all `i`: for
`m >= 3`, differencing two points forces `mu_i` independent of `i`, then
`c_i^rho` independent of `i`, i.e. all `P_i` are the SAME coset.
**So the razor's own domain type gives `m <= 2` on coset families, which
by (R2j-1) is WORSE than `m = 1`.**

**R2l — CARRIER EXHAUSTIVENESS (D3b), a two-line degree-parity proof.**
Write `sigma(X) = sigma^e(X^2) + X sigma^o(X^2)`. On a negation-closed
`D` with `y_m = 0` for even `m`, rows `2s` and `2s+1` of `M_r(y)` carry
the SAME vector `Z^(s)` acting on `sigma^o` and `sigma^e`. The two
condition families FUSE (count drops `rho -> ceil(rho/2)`) **iff
`sigma^e` and `sigma^o` are linearly dependent**. That happens iff

```
sigma = (X - x_0) p(X^2)      (deg always ODD)   or
sigma = q(X^2)                (deg always EVEN).
```

**At ODD `r` the second is impossible by degree parity, so
`(X-x_0)P(X^2)` IS the complete list. R-USYM's carrier residue closes.**
(`sigma^e = 0` is the `x_0 = 0` member; `sigma^o = 0` is the even case.)
Registered caveat: this classifies **locator-side** fusion only; a
pencil-side degeneracy of the `Z^(s)` is a different mechanism and is
declared unmeasured.

## R3 — Priors and predictions

**R3.1 The five priors the brief demands (blind).**

| id | statement | P |
|---|---|---|
| **B-1** | D1's rank half is PROVED this round (a clean sufficient condition, provable by Vandermonde/exchange, that forces full rank `j(rho+1)`) | **0.80** |
| **B-2** | R-URATE's additivity HOLDS (the joint cost of `j` slopes is the sum, no discount) | **0.55** |
| **B-3** | the `+126` becomes UNCONDITIONAL this round (all four side-conditions discharged at razor parameters) | **0.15** |
| **B-4** | a NEW parity-collapsing carrier exists at odd `r` (i.e. `(X-x_0)P(X^2)` is NOT exhaustive) | **0.12** |
| **B-5** | the count moves AGAIN — the cap `2(r+1)/rho` is broken and `B_ca^far` exceeds `r+1+126` | **0.20** |

Calibration notes, registered so the outcome can convict me: B-1 is high
because R2c is already written down and I believe it; B-2 is near a coin
because I can prove additivity in the DESIGN direction (R2b) and I can
also see the escape hatch (R2j) — the honest answer is "holds within a
normal form"; B-3 is low because R2g and R2h are genuinely open and I
say so BEFORE running anything; B-4 is low because R2l looks like a
complete proof to me; B-5 is low-but-not-negligible because R2j is a
mechanism I found myself and it could beat the count at some `m`.

**R3.2 Supporting priors (blind).**

| id | statement | P |
|---|---|---|
| B-6 | max attainable `j` equals `floor(2r/rho)` (my `m=1` formula), NOT `floor((2(r+1)-1)/rho)` (the anchor's cap) | 0.70 |
| B-7 | at C3 (`n=26,rho=3,r=10`) `j = 7` is UNREACHABLE — the anchor's miss 3 is CAP-limited, not search-limited | 0.70 |
| B-8 | at C11 (`n=32,rho=3,r=13`) max `j = 8`, not 9 (second discriminator) | 0.65 |
| B-9 | `dim ker M = 2` exactly at the `m=1` design with `j rho = 2r` | 0.85 |
| B-10 | the number of BAD projective `(u,v)` (some `lambda_i = 0`) is exactly `j` | 0.80 |
| B-11 | `m >= 2` designs FAIL at every small cell (the `Z_{P_i}|_{A*}` proportionality is unrealisable there) | 0.75 |
| B-12 | `T = (r+1)+j` exactly at every new censusable cell, column-far | 0.70 |
| B-13 | `>= 1` banked or anchor statement needs correction | 0.80 |
| B-14 | `>= 1` of my own registered predictions is refuted by my own runs | 0.70 |
| B-15 | `B_ca^far(k+2^34) < 2^128` moves | **0.02** |
| B-16 | the coset computation `Z_{cH}(X) = X^rho - c^rho` holds and `m <= 2` follows | 0.85 |

**R3.3 A-predictions (exact numbers, registered blind; a wrong digit is
a MISS I will report even if the use is unaffected).**

- **A-1** Razor: `2r/rho = 126` exactly; `floor(2(r+1)/(rho+1)) = 125`;
  `floor(2(r-1)/(rho-1)) = 126`; `126(rho+1) = 2,164,663,517,310`;
  `126(rho-1) = 2,164,663,517,058`; `2(r-1) = 2,164,663,517,182`.
- **A-2** `N = |D\W| = 1,116,691,496,959 = 65 rho - 1`; `k-1 =
  1,099,511,627,775`; `N - rho = k-1`.
- **A-3** `2(r-rho) = 2,130,303,778,816`; `sqrt = 1,459,556` to 7 s.f.;
  `m* = 17,178,409,629`.
- **A-4** `log2 C(N,rho) = 1.2806e11` (2 s.f. only — I claim 2 s.f.);
  `m_pig = 1.0e9` (2 s.f.); margin `m*/m_pig = 17` (2 s.f.).
- **A-5** Max `j` by cell (my `m=1` formula `floor(2r/rho)`):
  C1 **8**, C2 **10**, C3 **6**, C4 **6**, C7 **9**, C6 **7**,
  C11 **8**, C9 **7**. The anchor's cap `floor((2(r+1)-1)/rho)` gives
  C1 8, C2 10, C3 **7**, C4 6, C7 9, C6 7, C11 **9**, C9 7 — the two
  formulas differ ONLY at C3 and C11.
- **A-6** Total `T` at the `m=1` construction: C1 `9+8=17`,
  C7 `10+9=19`, C3 `11+6=17`, C2 `11+10=21`, C6 `12+7=19`.
  (C3 `= 17` retrodicts the anchor's full-census `T = 17`,
  `r37_urand/REPORT.md:205`.)
- **A-7** `m = 0` (no common point) gives `floor(2(r+1)/(rho+1))`:
  C1 6, C7 6, C3 5, C4 5 — strictly worse than `m=1` by `>= 1` slope at
  every cell, and `T_max(0) = T_max(1)` at the razor only.
- **A-8** Rank of the parity system on the carrier `(X-x_0)P(X^2)`
  equals `ceil(rho/2)`, and on a NON-carrier degree-`r` split locator it
  equals `min(rho, r+1)` generically: at rho=3 that is 2 vs 3, at rho=4
  it is 2 vs 4.
- **A-9** (semi-blind) The number of degree-`r` squarefree split
  locators with `sigma^e prop sigma^o` at odd `r` equals exactly the
  size of the `(X-x_0)P(X^2)` family — i.e. the classification is
  EXHAUSTIVE with excess 0 at every cell tested.

## R4 — MISS-2 GUARD (six clauses, binding on every claim I make)

1. **MAX, NOT MEAN.** `B_ca^far` is a MAXIMUM over pencils. No first
   moment, no `E[T]`, no Poisson/`mu_1` heuristic may support any
   verdict in either direction. Where I use one (R2g, R2h) I label it
   ZERO POWER at the point of use.
2. **EMPTINESS IS NEVER PROMOTED.** "I found no configuration at
   `j = j_0+1`" is a search result, never "`j_0` is the maximum".
   The anchor's own miss 3 is exactly this failure and I will not
   repeat it: my `j` ladders are CONTIGUOUS from 1, with the `tries`
   budget printed per rung.
3. **CODIMENSION != EMPTINESS.** (R2i-1) says `codim G_i >= rho`. It
   does NOT say the intersection is empty. Indeed R2d shows a
   codim-`(rho-1)` locus is NON-empty. No dimension count is a proof.
4. **RANK != EXISTENCE OF A GOOD KERNEL VECTOR.** Full row rank
   (R2b/R2c) proves the kernel's DIMENSION. The four side-conditions
   are separate and each is discharged separately or declared open.
5. **THE FOUR FUNCTIONALS ARE NEVER EQUATED.** `T`, `T_fib`, `T_sym`,
   `T_rand` are distinct exhaustive counts. In particular
   `T = T_fib + j` is a MEASUREMENT at census rows, and only
   `T >= T_fib + j` is ever used for a lower bound.
6. **AVERAGING OVER PENCILS IS FORBIDDEN AS EVIDENCE.** A clean null on
   generic pencils is not a fence (the anchor's own `4.5e4x` failure,
   `r37_urand/REPORT.md:171`). Every conclusion is about a NAMED pencil.
7. **NEW THIS ROUND — RETRODICTION IS NOT PREDICTION.** A-5/A-6 partly
   retrodict the anchor's measured `j` and `T`. Those rows are marked
   RETRODICTION and carry no confirmatory weight; only C3, C11, C7, C6,
   C9 carry predictive weight, and C3/C11 are the only discriminators.

## R5 — ZERO-POWER DECLARATIONS (pre-registered)

1. **ZP-1 (no widening).** All machine numbers at `q <= 999983`,
   `R <= 18`, `rho <= 4`, `r <= 14`. Registered NOW so that no widening
   can be taken later. Every razor number is a closed-form evaluation.
2. **ZP-2 (faithfulness).** Zero power from any cell failing
   `a > R+1`, `a-1 > r`, `4rho < R`. Booleans printed per row.
3. **ZP-3 (first moment).** The `mu_1` / Poisson model has ZERO POWER in
   both directions and supports no verdict. Used only as a descriptor.
4. **ZP-4 (column-farness, Case B).** R2h Case B is a first-moment
   argument over `C(n,r)` supports. **DECLARED ZERO POWER.** I will not
   claim column-farness at razor parameters; I claim it only where a
   census MEASURES it.
5. **ZP-5 (chi injectivity, same-block-pair).** R2g's same-block-pair
   residue is a condition on the DESIGN, and any "generic `P_i` works"
   statement is a first moment. **DECLARED ZERO POWER at the razor.**
   Only the `<= 125`-collisions RELAXATION is used for the bound.
6. **ZP-6 (dimension counting is not a proof).** Restated from the
   anchor's ZP-6 and binding here.
7. **ZP-7 (the cap direction).** R2i gives a per-slope codimension; it
   does NOT bound the number of slopes, because the family of subspaces
   `G_i` is astronomically large. **Any cap proved this round is a cap
   WITHIN A NAMED NORMAL FORM (R2j), never over all configurations.**
   Declared before any run.
8. **ZP-8 (the rank-drop search).** My `m >= 2` search is over the
   `Z_{P_i}|_{A*}`-proportional normal form ONLY. Other rank drops of
   `Phi` are unenumerated; a negative result is "none in this normal
   form", never "none".
9. **ZP-9 (two-field rule).** Every structural claim needs `>= 2`
   fields; single-field rows are descriptive only.
10. **ZP-10 (siblings).** No round-38 sibling directory will be read;
    no `ls` of the parent will be run. Names taken from
    `CONSTRAINTS.md:36-38`.
11. **ZP-11 (automorphisms).** `T_sym` classification tests only
    `x -> -x`. Other automorphisms of `D` are unmeasured.
12. **ZP-12 (characteristic).** Every field used is an odd prime. Char 2
    and non-prime `q` are unmeasured; Frobenius mechanisms for `c` are
    declared absent from the evidence base.
13. **ZP-13 (pigeonhole ceiling).** `m_pig` (R1.2-G) is an
    INFORMATION-THEORETIC ceiling on one named mechanism. It is not a
    proof that no algebraic family achieves larger `m`. The margin
    `17.2x` is therefore a margin against pigeonhole, not against
    algebra. **This is the single most likely place for the cap to
    break, and I name it before running anything.**
14. **ZP-14 (locator-side only).** R2l classifies locator-side parity
    fusion. Pencil-side degeneracy of the `Z^(s)` vectors is a distinct
    mechanism, unmeasured.
15. **ZP-15 (`mu_n` arithmetic).** The `mu_n` cells use `q ~ 2e5..9e5`.
    Zero power over the razor subgroup's 2-power-order arithmetic
    (`n = 2^41`, `q > 2^128`).

## R6 — Deliverable registrations and falsifiers

- **D1** delivers (R2a, R2b, R2c, R2d) plus machine verification of
  (R2b-1)/(R2b-2) at `>= 4` cells and `>= 2` domain types.
  **FALSIFIER F-1:** if the measured `rank(M) != j(rho+1) - L +
  rank(Phi)` at ANY faithful cell, R2b is refuted and I report it as the
  headline miss.
- **D2** delivers R2i (rigorous per-slope codim), R2j (the trade-off
  law), R2k (coset attack closed), and the verdict on R-URATE.
  **FALSIFIER F-2:** if any cell exhibits `j > floor(2r/rho)` with all
  four side-conditions holding and column-far, then B-5/B-6 are refuted,
  the cap is broken, and the far-CA count moves again. I will search for
  this actively at every cell (contiguous `j` ladder, `j` up to
  `floor(2r/rho)+3`).
- **D3** delivers the four side-conditions (R2e/R2f PROVED, R2g/R2h
  split), `>= 3` new cells beyond the anchor's 60/60, and R2l's
  completeness lemma. **FALSIFIER F-3:** if a degree-`r` squarefree
  split locator at ODD `r` fuses the parity blocks WITHOUT being of the
  form `(X-x_0)P(X^2)`, R2l is refuted and R-USYM re-opens.
- **D4** delivers the verdict, misses-first, and cross-pilot flags.
  **No node surgery: AUDIT-AND-DRAFT.**

## R7 — Compute plan

`<= 5` interpreter invocations, every one `tools/ramguard local --
python3 ...` from the repo root with a literal `--` and
`RAMGUARD_TIMEOUT=290`, stdlib only (`sys, math, random, itertools,
fractions`). No Modal, no network, no git, no subagents. **No bare
`python3` for any purpose whatsoever — not for patching, not for probes,
not as an empty heredoc between edits.** Every results file is opened
`"a"` (append) and flushed after each emit; **no results-producing run
is piped through `head`** (`tail -n N` only, then `grep -n`/`sed -n`).
**No banked script is imported**; every helper is duplicated per file
(the anti-import pattern). If I ever do copy one, I will grep it for
`open(`/`write` and repoint its paths with the Edit tool BEFORE the
first import.

- **g1** — rank theory: build `M` explicitly at C1, C7, C2, C3, C6, C11,
  C4, C9 on `intZ` and `mu_n`; verify (R2b-1), (R2b-2), `dim ker = 2`,
  the exact count of bad projective `(u,v)`, and the contiguous `j`
  ladder up to `floor(2r/rho)+3` for `m = 0,1,2,3`.
- **g2** — census: full `C(n,r)` sweep at C1(`mu_20`, 2 fields),
  C7(`intZ` + `mu_22`), C3(`mu_26`) of the constructed pencil;
  `T`, `T_fib`, `T_rand`, column-farness, faithfulness booleans.
- **g3** — side conditions + rank-drop search: measure `lambda != 0`,
  `chi` injectivity (and the collision count), `gamma_i` off-fibre,
  column-farness over `>= 200` draws per cell; search the `m >= 2`
  normal form for `Z_{P_i}|_{A*}` proportionality; verify R2k.
- **g4** — carrier exhaustiveness: enumerate all degree-`r` squarefree
  split locators at odd-`r` negation-closed cells, test
  `sigma^e prop sigma^o` against membership in `(X-x_0)P(X^2)`, and
  measure the parity-system rank (A-8).
- **g5** — razor closed forms: A-1..A-4, `T_max(m)` table, `m*`,
  `m_pig`, the margin, and `log2(r+1+j)` for the record.

**No registration below this line will be edited after the first
interpreter invocation.**
