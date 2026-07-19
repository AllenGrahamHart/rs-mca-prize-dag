# rate_half_band_closure

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/flip_packets/rate_half_coverage_gap.md']

## Statement

Cover the 2,978,147-radius band at prize-max rate 1/2 (M_max = 2^33 vs sigma* = 8,592,912,738) by a new mechanism (quotient windows and integrality both fall short) — or the rate-1/2 determination lands bracket-grade there. Rates 1/4, 1/8, 1/16 need nothing (clean by margins < -121). THE rate-1/2 battlefield node.

## Attack surface

a third mechanism for the band: extended quotient scales, averaged conversion at giant M, or the B2b-style balance analysis

## Falsifier

a band radius provably uncoverable by any priced mechanism

## [LIST-SIDE RETIREMENT + MCA/CA RE-SCOPE (wave-8 audited, 2026-07-16)]

The GRAND-LIST-DECODING half of this obligation is RETIRED BY THEOREM:
`rate_half_cyclic_rotated_prefix_floor` (PROVED, imported; + background
`rate_half_fixed_tail_prefix_floor`) proves the entire residual band
2^33 < sigma <= sigma* list-unsafe at sigma* — the trigger count
> q/2^128 is exactly the prize's |Lambda(C^{==m})| <= 2^-128 |F| object
— for ordinary + every constant common-support arity, every admissible
q < 2^256 (margin 75.0796 bits at q=2^256; cap boundary 256.0366 > 256;
agreement = k+sigma* exact). With the banked safe side, the rate-1/2
LIST crossing is DETERMINED; list_adjacency_closing consumes the PROVED
node directly. REMAINING for this red: the support-wise MCA/CA crossing
only (trigger ~ q/k). GUARD (verbatim, audited): any MCA-side argument
must not reuse the list threshold q/2^128 as an MCA surrogate — the two
triggers are different objects (separation measured:
notes/rate_half_trigger_separation_modal.py).

## [CORRECTION to the wave-8 addendum above (2026-07-17, w9-C2 — our
## own overclaim, caught by the wave-9 audit via v4's scope audit)]

The sentence "With the banked safe side, the rate-1/2 LIST crossing is
DETERMINED" is WITHDRAWN. The "banked safe side above sigma*" was
planning prose, not an in-repo theorem (the Paper D pincer stops at
half distance; r2_clean_rates excludes rate 1/2), and the s = c-1
instantiation of the cyclic floor proves list-unsafety THROUGH
sigma_0 = 8,594,128,895 > sigma*. Corrected state: the LIST UNSAFE
side is proved through sigma_0 (the cyclic floor node, strengthened);
the LIST SAFE side is OPEN (field-dependent); the crossing is NOT
determined. The retirement claim narrows accordingly: what is retired
is the unsafety obligation on the band, not the crossing location.
This node's own open content remains the MCA/CA half — now re-posed by
the audited v4 work as (RH-ADJ): find field-dependent a_RH(q) >=
k + 8,594,128,896 with B_mca(a_RH) <= floor(q/2^128) < B_mca(a_RH - 1).

## FIXED-CROSSING REFUTATION + FIELD-DEPENDENT RE-POSE (wave-9 audited, 2026-07-17; pin statement body — master text above preserved per #104)


- **status:** TARGET
- **closure:** proof
- **current object:** rowwise support-wise MCA adjacent certificate
- **refs (legacy repo):** `experimental/notes/roadmaps/flip_packets/rate_half_coverage_gap.md`

## Statement

Let

```text
n=2^41,       k=2^40,       C=RS[F,D,k],
2^128<q=|F|<2^256,          n divides q-1,
B*(q)=floor(q/2^128),
```

where `D` is a multiplicative coset of order `n`. Produce an explicit
row-computable agreement `a_RH(q)` and prove the exact adjacent certificate

```text
B_mca(a_RH(q)) <= B*(q) < B_mca(a_RH(q)-1).              (RH-ADJ)
```

Here `B_mca(a)` is the maximum number of finite slopes carrying a failed
support-wise MCA witness with agreement at least `a`. Equivalently,
`B_mca(a)/q=epsilon_mca(C,1-a/n)` under the closed finite-slope convention.
The range `q<2^128` is the already-settled degenerate regime with grand
threshold zero; equality `q=2^128` cannot admit this order-`2^41`
multiplicative domain.

## Proved lower bracket and refutation

Put

```text
c=2^22,       d=2048,
sigma_0=dc+c-1=8,594,128,895.
```

The strengthened proved node `rate_half_cyclic_simple_pole_mca_floor` gives

```text
B_mca(k+sigma_0)>B*(q)                                    (RH-LOW)
```

for every field in scope. Consequently every valid adjacent certificate
must satisfy

```text
a_RH(q) >= k+sigma_0+1.                                  (RH-BRACKET)
```

This refutes the former fixed claim at

```text
k+8,592,912,738+1 <= k+sigma_0.
```

Thus `sigma*=8,592,912,738` is not the rate-half crossing, and the old
`(RH-SAFE)` statement must not be consumed downstream. The conjectural
corridor map that printed this point is also not an optimality certificate
for rate `1/2`.

## Exact safe-side reduction

For any proposed agreement `a`, the proved sparsification identity in
`rate_half_mca_sparse_layer_reduction` writes

```text
B_mca(a)=max(B_ca^far(a), S_sparse(a)).                   (RH-SPLIT)
```

Therefore the safe half of `(RH-ADJ)` is exactly the conjunction

```text
B_ca^far(a_RH(q)) <= B*(q),
S_sparse(a_RH(q)) <= B*(q).
```

The first term is the plain correlated-agreement upper problem for
column-far pairs. The second is the budget-restricted sparse mutual layer.
Neither is supplied by the deep or half-distance pincer at this
near-capacity radius.

The proved `rate_half_sparse_pinning_rigidity` theorem further reduces the
sparse term. At `a=k+tau`, every non-tangent bad slope requires support
`e>=tau+1`, a nonzero ambiguity polynomial with cofactor degree at most
`e-tau-1`, and at least `A-e+tau+1+u` active matches consistent with one
slope. For `q>=2^168`, all tangent slopes already fit `B*(q)`, so only this
coupled non-tangent system remains on the sparse side.

## Attack surface

Locate a candidate at or above `(RH-BRACKET)`, then prove both upper bounds in
`(RH-SPLIT)` and an adjacent lower witness. A complete first-match/profile
ledger may prove both upper terms; a stronger explicit lower family may move
the bracket farther before the upper work begins.

## Falsifier

For any proposed formula `A(q)`, either an admissible row with
`B_mca(A(q))>B*(q)` or failure to prove
`B_mca(A(q)-1)>B*(q)` falsifies that adjacent formula. The previously proposed
constant formula is already falsified by `(RH-LOW)`.

## QUADRATIC EXACT RANGE + SAFE BRACKETS + HANKEL SUITE + OPTIMIZED FLOOR (wave-10 audited, 2026-07-18 — the reconciled v4+v5 state; all previous poses preserved above)

**THE CROSSING IS DETERMINED for every admissible 2^128 < q < 2^167:** a_RH(q) = n - floor(q/2^128) + 1, unconditional. Composition: the quadratic staircase equality (mca_quadratic_prize_rows) covers B = floor(q/2^128) <= B_Q = 389,500,552,609 (~2^166.503); the (RQ4) equivalence reduces B_Q < B <= 2^39+1 to the single far-CA bound; the Hankel suite's unconditional layer B_ca^far(n-r) <= r+1 (every r <= 2^39-2) supplies it; the universal coordinate-tangent family (mca_full_agreement_endpoint, in-repo since wave-6) supplies the adjacent unsafe witness. The wave-9 PR4 q >= 2^168 caveat is bypassed below 2^167.

**EXACT RESIDUAL of (RH-ADJ):** budgets 2^39 (strict A=3, s=0, e in [2^37, floor((2^39-1)/3)]) and 2^39+1 (A=3 e >= 2^37+1, plus A=1 rows) — recorded per w10-H1 as the explicit open-budget set {2^39, 2^39+1}; beyond 2^167, brackets only: a_RH in [k+2^34, 3n/4] for q >= 2^169, [k+2^34, n] otherwise. The k+2^34 floor (v5's optimized re-instantiation, c=2^33, d=1, field-independent list 2^242.65) SUPERSEDES the former k+8,594,128,896 bracket lines and sigma_0 as the forward-facing constant (sigma_0 retained as history — forced-corrections authority, proved constant improvement).

**Hankel suite note (w10-H5):** the seven strict-endpoint nodes rigidify the residual profile at strict budget e=m only — they are NOT q-axis coverage progress. The five wave-9 guidance lines and the three pre-suite 'Remaining proof' lines are superseded, not deleted (w10-H2).

**LIST side (v5, audited):** the safe side is now OWNED by the TARGET pose rate_half_list_adjacent_crossing (the w9-C3 repair vehicle); the exact-integer Johnson anchor is PROVED; the list crossing is DETERMINED for budgets B* in {1,2} at a_L = 3n/4; the proved unsafe reach doubles to excess 2^34-1.

## STRICT `A=3` ALL-DEGREE SLOPE-SLACK LEDGER (2026-07-18)

The maximal-rank kernel-curve reduction is no longer confined to the first
endpoint `e=2^37`. For every live strict-budget degree

```text
m=2^37<=e<=floor((2^39-1)/3),
```

the primitive apolar generator has exact separation rank `e+1` and traces a
degree-`e` rational normal curve. If `T` supported slopes violate the desired
strict cap and

```text
h=4e+1-T,
```

then

```text
0<=h<=4(e-m),
C=4e-(2^39-1)+h(2^39-1)+O<=e+h(2^39-1).
```

Here `C` is the exact total deficit from full parameter capacity over the
`2^41` domain rows and `O<=2^39-1-3e` is the root-omission budget. At least
`max(0,2^41-e-h(2^39-1))` rows are saturated, at least
`T-(2^39-1-3e)` supported columns are squarefree and completely domain-split,
and the root-incidence matrix has exact rank `e+1` and exact two-sided
product-code weight.

On the sharp-cap face `h=0`, the complete domain norm is a
`(2^39-1)`st power of the supported-slope polynomial up to numerator degree
`O` and residual degree at most `e`. At least `2^41-e` domain rows admit the
corresponding exact complementary factorization. This generalizes the former
endpoint norm identity to every sharp-cap parameter degree.

On the same face, every geometric component degree is quantized. Writing
`g=4e-(2^39-1)` and `a_i=4e_i-r_i`, the `a_i` are nonnegative, sum to `g`,
and each lies in a necessary interval of width less than one half determined
by `e_i`. Thus each parameter degree allows at most one component `X`-degree.
The endpoint's unique defect-one component is the specialization `g=1`.

The old endpoint is precisely `e=m,h=0`. The endpoint component and
norm-factorization theorems remain endpoint-only; this new ledger instead
stratifies every larger strict `A=3` degree. It does not exclude a stratum or
close the rate-half crossing.

## HALF-DISTANCE `A=3` ALL-DEGREE SLOPE-SLACK LEDGER (2026-07-18)

The transpose-shaped `A=3` branch at budget `2^39+1` now has the same exact
router. For every live degree

```text
2^37+1<=e<=floor((2^39-1)/3),
```

the primitive degree-`2^39-1` apolar generator has separation rank `e+1` and
traces a degree-`e` rational normal curve. A failure of the required
`T<=2^39+1` bound has

```text
h=4e+1-T,       0<=h<=4(e-2^37)-1,
C=4e-(2^39-1)+h(2^39-1)+O<=e+h(2^39-1).
```

The same exact saturation, clean-column, product-code, sharp-cap norm, and
component-degree ledgers hold. Clean `Q_gamma` fibers have `2^39-1` domain
roots and are factors of the supported degree-`2^39` locators; they are not
silently identified with those full locators.

At the first live degree `e=2^37+1`, only `h=0,1,2,3` are possible. Every one
has at least `3*2^37+2` saturated domain rows and at least `3*2^37+6`
completely split generic columns. This does not exclude those four strata.
The separate half-distance `A=1` profiles remain outside this theorem.

## HALF-DISTANCE `A=1` CORE-STRATIFIED LEDGER (2026-07-18)

The remaining half-distance Hankel family is now structurally routed as
well. The proved fixed core has size `s in {0,1,2}`. After stripping it, put

```text
rho=2^39,       d=rho-s,       Delta=d-(1+s)e,
L=(2^41-s)e+Delta,
T_max=floor(L/d),       eta=L-T_max*d.
```

Every residual generator has separation rank `e+1` and traces a rational
normal curve. A failure of `T<=rho+1`, with `ell=T_max-T`, satisfies

```text
C=ell*d+eta-Delta+O<=ell*d+eta,       O<=Delta.
```

It has at least `max(0,2^41-s-ell*d-eta)` saturated residual rows, at least
`T-Delta` completely split clean columns, and an exact rank-`e+1`
product-code incidence word. On `ell=0`, the residual norm degree is at most
`eta`; component chambers have width below two and are unique for `s=1,2`.

At the first live degree `e=2^37+1`, the three cores leave only `3+4+4`
slack strata. Their worst-case saturation guarantees are respectively
`5*2^37+1`, `3*2^37+1`, and `2^37+1`. No stratum is excluded.

## `A=1`, CORE-ONE MAXIMAL-DEGREE EXCLUSION (2026-07-18)

One sharp-cap face has a stronger exact classification. For `s=1` and
`e=2^38-1`, the residual generator has a unique component

```text
(r_*,e_*)=(2e_*+1,e_*),
```

while every other component has `(r_i,e_i)=(2e_i,e_i)`. If their total
parameter degree is `b`, then

```text
5b<=e,       b<=54,975,581,388,
e_*>=219,902,325,555,       r_*>=439,804,651,111.
```

The full residual generator has separation rank `e+1`, so the dominant
component has separation rank at least five. This excludes separated
pullbacks and all rank-one through rank-four mixed models on that face. At
least `8*2^37-4` supported slopes and `14*2^37` residual domain rows split
every component. The remaining rank-at-least-five component is not excluded.

## CORE-ONE MIDDLE-HANKEL COFACTOR IDENTITY (2026-07-18)

On the same `s=1,e=2^38-1` face, contraction gives a square symmetric
middle-Hankel pencil `M` of size `2^39` and generic rank `2^39-1`. If `q` is
the residual apolar coefficient vector, then

```text
adj M=lambda*q*q^T,
```

where `lambda` is one nonzero linear form. It is the exact gcd of all nonzero
maximal minors and the unique size-one regular Kronecker block. Thus there is
only one projective rank-drop slope, of loss exactly one, and every residual
root omission is concentrated there. On sharp cap,

```text
O in {0,1},       C=(2^38-1)-1+O.
```

This supplies explicit cofactor equations for the surviving rank-at-least-
five dominant component; it does not yet exclude it.

## CORE-ONE COMPONENT NORM LOCALIZATION (2026-07-18)

Every component omission and component intersection on this face is now
localized at the unique `lambda=0` slope. If `b` is total residual parameter
degree, the dominant component has

```text
(r_*,e_*)=(2e_*+1,e_*),       sr(Q_*)>=5,
deg S_*=C_*=e-5b-1+D_*,       D_* in {0,1},
```

and splits completely on at least `14*2^37+5b` residual domain rows. Every
residual `(2e_i,e_i)` component has norm residual degree `5e_i+D_i`. Each
component separately satisfies an exact power-norm identity and complementary
factorization. The dominant mixed norm object remains open.

## CORE-ONE TWO-SIDED COMPLEMENT WELD (2026-07-19)

The dominant component has both a domain-saturated complement

```text
Q_* V+P_X W=P
```

and a slope-clean complement `Q_* A+P_cl B=G_X`. Eliminating the shared
clean-slope product gives one biform `K` with

```text
W B-B_X E_Z=Q_* K,
V B+A E_Z=-P_X K,
deg_X K<=2^41-2,       deg_(U,V)K<=4e.
```

Here `B_X` has degree at most `e-5b-1+D_*` and `E_Z` has degree at most one.
This is the selected two-sided matrix-factorization normal form for the
remaining mixed component. It is not yet a contradiction.

## CORE-ONE ZERO-WELD QUARTIC BOUNDARY (2026-07-19)

The branch `K=0` is now excluded except in one exact profile:

```text
b=0,       D_*=1,
F(U,V)-G_0(X)=Q_*(U,V;X)V_0(U,V;X),
deg F=4e,       deg G_0=8e+4,
deg Q_*=(2e+1,e),       deg V_0=(6e+3,3e).
```

Here `F` splits on all `4e` clean slopes and `G_0` splits on all but exactly
three residual-domain points. Thus `Q_*` is a one-quarter bidegree factor of
a quartic separated difference. Every profile with residual components,
every `D_*=0` profile, and the other exceptional-factor allocation has
`K!=0`. The quartic boundary and nonzero-weld branch remain open.

## CORE-ONE ZERO-WELD EXCLUSION (2026-07-19)

The quartic boundary is also impossible. Its component-capacity ledger gives
`C_*=e`. At every root of `G_0`, the degree-`e` form `Q_*(U,V;x)` divides the
squarefree clean-slope product `F` and is saturated. At each of the three
omitted domain points it has no clean-slope root and at most the one
exceptional supported root. Those three rows alone therefore give

```text
C_*>=3(e-1)>e,
```

contradicting `C_*=e`. Hence `K!=0` on every profile of this official
core-one maximal-degree sharp cap. Only the nonzero-weld coupled matrix
factorization remains open on this face.

## CORE-ONE NONZERO-WELD TRACE DESCENT (2026-07-19)

The surviving weld has an exact fiberwise router. At a nonsaturated domain
row `x`, let `R_x=gcd(Q_x,P_cl)`. Then

```text
A_x=Phat_x H_x,       B_x=-Qhat_x H_x,
W_x=R_x J_x,          K_x=-H_xJ_x,
deg Qhat_x=delta_x+epsilon_x,
sum_x delta_x=C_*.
```

If `D_*=1`, the exceptional-slope gcd has degree at least `e+3b`, while its
complementary quotient has degree at most `c+1`. Exhaustively, either one of
these defect traces of `K` is nonzero, or

```text
B_XE_Z divides K,       W_1B_1-1=QK_1,       K_1!=0,
deg_X K_1<=D_0-1-c,     deg_parameter K_1<=T-1-D_*.
```

This replaces the undifferentiated nonzero-weld search by active-trace and
strict factor-descent branches. Neither branch is yet excluded.

## CORE-ONE TRACE-FREE ALLOCATION RIGIDITY (2026-07-19)

The trace-free leaf has no arbitrary prime allocations. Its norm residual is
exactly

```text
S_*=product_x N_x,       deg N_x=delta_x,
sum_x delta_x=C_*.
```

Every bad domain factor divides both `A,B`. The apparent alternative would
require

```text
Qhat_x divides E_Z.
```

That divisibility forces `epsilon_x=1`, hence
`deg Qhat_x=delta_x+1>=2>deg E_Z`, a contradiction.

The exceptional factor has two allocations. In its `B`-allocation,
`Q(gamma_0;X)` is a squarefree degree-`r-1` divisor of `G_X`. After these
forced allocations, the trace-free leaf is exactly

```text
Q V_1+P_X W_1=P_cl Z_B,
Q A_1+P_cl Z_B B_1=P_X,
W_1B_1-1=QK_1,       K_1!=0.
```

This reduced complement square and the separate active-trace leaf remain
open.

## CORE-ONE TRACE-FREE WELD EXCLUSION (2026-07-19)

The reduced complement square is impossible. Its `Z_W=E_Z` exceptional
allocation contradicts the proved positive degree of
`gcd(Q(gamma_0;X),P_X)`. In the other allocation, and also when `D_*=0`, the
second reduced complement is

```text
Q A_1+P B_1=P_X.
```

Thus every supported `Q_gamma` divides `P_X`. A bad domain row then has no
supported roots, so the exact capacity becomes `C_*=c e_*`. The only possible
numerical profile is `b=0,D_*=1,c=1`. There the exceptional fiber has degree
`r-1`, forcing `deg_X A_1(gamma_0)=D_0-r`; but `B_X|A` and
`deg_X A=D_0-r` give `deg_X A_1<=D_0-r-1`. This contradiction closes the
trace-free leaf. Every surviving profile on this face has an active trace of
`K`.

## CORE-ONE ACTIVE-TRACE CORE (2026-07-19)

Cancel every bad-domain factor whose `K` trace is zero, and allocate a zero
exceptional trace when present. The surviving system is exactly

```text
Q V_a+P_X W_a=P_cl Z_B E_a,
Q A_a+P_cl Z_B B_a=P_X X_1,
W_aB_a-X_1E_a=QK_a,
```

where every root of `X_1` is an active domain trace and `E_a=E_Z` exactly
when the exceptional trace is active. Capacity allows no zero domain trace
unless `b=0,D_*=1`, and then only

```text
c=1: exceptional-only activity; or
c=2: one zero row and one active domain row of deficit one.
```

Otherwise every bad-domain trace is active. These active cores remain open.

## CORE-ONE EXCEPTIONAL-TRACE ALLOCATION (2026-07-19)

The first active-core complement is always

```text
Q V_a+P_XW_a=P.
```

When the exceptional trace is zero, its `Z_W=E_Z` allocation contradicts the
positive saturated gcd. It must divide `B`, every domain trace must be active,
and `Q(gamma_0;X)` is a squarefree degree-`r-1` divisor of `G_X`. The active
face is therefore reduced to exactly three systems: `D_*=0`; `D_*=1` with an
active exceptional trace; or `D_*=1` with a zero exceptional trace and every
domain trace active. All three remain open.

## CORE-ONE EXCEPTIONAL-TRACE NONVANISHING (2026-07-19)

The zero-exceptional system is impossible. It would give a squarefree
degree-`r-1` fiber `q_0` and

```text
q_0 A_a(gamma_0;X)=G_X,
```

requiring `deg_X A_a(gamma_0)=D_0-r+1`. But every domain trace is active in
that branch, so `A_a=A` and the exact global degree is only `D_0-r`. Thus a
`D_*=1` core always has an active exceptional trace. Only the `D_*=0` and
active-exceptional `D_*=1` systems remain.

## CORE-ONE ACTIVE TWO-SIDED PARTITION (2026-07-19)

Let `z=deg X_0` and `R_X=G_X/X_0`. Every clean slope and saturated domain row
now gives an exact squarefree complementary partition:

```text
Q(gamma;X)A_a(gamma;X)=R_X,
deg(Q_gamma,A_gamma)=(r,D_0-z-r);

Q(U,V;x)V_a(U,V;x)=P,
deg(Q_x,V_x)=(e_*,T-e_*).
```

Both quotients attain their global degree bounds and have root sets disjoint
from those of `Q`. The total clean incidence of active bad rows is
`c e_*-C_*-E_bad`, with the explicit formulas `(ATP8)`. This degree-tight
two-sided divisor family is the remaining object to classify.

## CORE-ONE ACTIVE INCIDENCE RECONSTRUCTION (2026-07-19)

The partition family now has an exact incidence-only gate. On saturated rows
and clean slopes, join a pair when it is a nonincidence. This graph is
connected, with each same-side pair sharing a neighbor. If `F_gamma` and
`G_x` are the monic domain and slope locators, its edge labels satisfy

```text
F_gamma(x)/G_x(gamma)=b_x/a_gamma.
```

Hence all alternating-cycle products are one and the fiber scalars are
recoverable up to a common factor. Conversely, after this potential pass,
the proposed partitions come from a unique biform exactly when every scaled
coefficient vector of `a_gamma F_gamma` belongs to
`RS[Z_cl,e_*+1]`. The saturated fibers then follow automatically. Remaining
classification must impose this deterministic gate before the Hankel,
adjugate, irreducibility, and active-trace constraints. The scaled clean and
saturated locator matrices and the core value matrix all have exact rank
`sr(Q)`, at least five and exactly `e+1` on the `b=0` branch.
