# petal_mixed_amplification

- **status:** CONDITIONAL
- **closure:** proof from PMA stage predicates
- **refs:** `proof_sketch/s7_list_side.md#4`

## Statement

Count degree-`<= d` polynomials `W` with many zeros across the shifted-target
family

```text
W - c_i L_D on T_i.
```

Super-polynomial amplification must force quotient structure, low defect, or
another explicitly budgeted structured family.

## Ledger

CONDITIONAL (Codex fresh-base pass): `pma_aux_list_reduction` converts extras
to the auxiliary RS list, `pma_johnson_regime` covers the classical
few-petal range, and `pma_wide_residual` is the remaining many-petal primitive
residual.

AMBER STRESS 2026-07-06: `pma_correlated_target_search.py` varied the defect
locator and correlated petal scalar pattern in the `F_109, ell=3, d=5` toy
window.  It completed `10` exact profiles and `3` sampled `M=12` profiles under
the cap; exact `M=9` profiles had at most `176` threshold candidates, and no
large spread-residual alarm appeared.

---

## RE-POSE ADDENDUM (2026-07-16, wave-8 audited import; v4 statement body verbatim — master text above preserved per #104)


- **status:** TARGET
- **role:** corrected post-top-band polynomial/profile frontier
- **consumer:** `imgfib`

## Statement

Under the polynomial generated-field, entropy-reserve, and lower-cutoff
hypotheses stated in `imgfib`, first-match every maximal-sunflower contributor
by carried source layout. After charging exact-periodic and every other
natural-scale quotient/profile class once, the aggregate contribution outside
the layout-anchored top band admits a complete disjoint allocation

```text
#post-top primitive residual <= n^B
```

for one printed family-uniform constant `B`, while every non-polynomial
natural-scale profile is charged once to an explicit quotient/profile column. The
allocation must compose with the reserve and profile hypotheses in
`imgfib`; merely naming a larger exponent is not sufficient.

For petal size `ell=sigma+1`, one carried source layout has the exact
rational-map form

```text
R=W/L_D,
deg W<=d,
D subset C,
#{y in T:R(y)=c_(petal(y))}+r >= ell+d,
```

with `W` nonzero on the exact missed-core set `D`. The proved reserve
reduction shows that every non-planted residual has one petal containing at
least

```text
ceil(ell/M) >= ceil(ell^2/(n-k+1))
```

points of one value fiber of `R`. This is `Omega(n/log^2 n)` at the lower
cutoff. The proved `pma_saturated_mixed_support_kernel` theorem strengthens
this to an exact interpolation-kernel reduction. If `a_*` is the largest
background/petal label class in the exact noncore support, then

```text
rank T_(X,d)>=a_*-1>=m_rich-1.
rank T_(X,d)=min(d,w),       w=|X|-d-1,
```

Exact defect makes the rational pencil reduced: `gcd(L_D,W)=1`, distinct
fiber polynomials are pairwise coprime, and common-factor kernel components
are duplicate lower-defect representations rather than new codewords. The
same theorem bounds the split monic locators for this fixed exact support by

```text
binom(k-1,max(0,d-w)).
```

The complete target must now absorb, sharpen, or profile-own these canonical
root-pinned charges and sum exact supports while handling every defect and
background state, below-floor full petals, and mixed/diffuse partial petals.

The proved `pma_petal_pattern_root_pinning_ledger` performs the first
nontrivial aggregate. If `t` petals are touched in `h` petal points, then

```text
#cell(d,t,h)
 <= binom(M,t) binom(t ell,h)
    binom(k-1,max(0,2d+1-h)).
```

No background-support multiplier appears: the petal pattern and locator
determine the numerator and hence its background roots. Writing

```text
u=t ell-h,       e=max(0,2d+1-h),
```

every fixed `u+e` region is polynomial at the lower cutoff. The live
aggregate residual is therefore restricted to `u+e->infinity`. For full
petals this means `2d+1-t ell->infinity`; growing `d-ell` alone is no longer
an open regime.

The proved `pma_full_petal_band_composition` theorem now composes this ledger
with the layout-anchored top band using the correct parameters. The carried
chart contains all `M` source petals, while `t` counts only those touched by
the codeword; the equality `M=t` is false in general. All full-petal sources
with `M<=3` are paid, as is the `M=4,t=4` stratum. A remaining full-petal
family must satisfy

```text
M>=4,       d<ell(M-2),       t<2M-4,
max(0,2d+1-t ell) -> infinity.
```

Mixed and diffuse partial-petal profiles retain the general `u+e->infinity`
condition.

The proved `pma_coset_subtwoell_saturation_exclusion` theorem removes a sharp
scoped subcase. In a genuine constant-shift locator pencil `P-a_i`, exact
saturation excludes every full-petal contributor with

```text
t>=3,       ell<d<2ell.
```

Both boundaries are sharp: saturated examples exist for `t=2` inside the
strip and at `d=2ell` with three petals. This does not yet remove a universal
PMA stratum. Multiplicative-coset charts are the special case `P=X^ell`; the
carried G1 atlas has those petals in the paid top band. No proved source
theorem places every surviving below-band layout in one common constant-shift
pencil. The arbitrary-locator complement therefore remains in this target. A
future source bridge would eliminate the entire `M=4,t=3` stratum, because
root pinning pays `d<=ell` and the top band pays `d>=2ell`.

The proved `pma_arbitrary_petal_source_realizability` theorem rules out a
source-only version of that bridge. Maximal sunflower sources exist for every
arbitrary disjoint petal partition, even on a smooth multiplicative domain,
and their locator polynomials need not share any nonconstant coefficient.
Therefore a usable common-pencil bridge must depend on the particular
surviving contributor and give a bounded-to-one rechart, or the
arbitrary-locator branch must be counted directly. The construction does not
itself produce an unpaid residual contributor and is not a PMA counterexample.

The proved `pma_three_petal_mu_basis_reduction` theorem gives the exact normal
form for that arbitrary-locator branch. For three touched full petals in the
strict strip, write `d=ell+s` and

```text
W-c_iF=L_iA_i,       deg A_i<=s.
```

The three locator products obey one exact syzygy. The syzygy module has a
reduced basis of degrees `mu` and `ell-mu`. Exact-defect saturation forces

```text
s<ell/2  ==>  mu=s and one projective candidate,
s>=ell/2 ==>  mu>=ell-s and dim=2s-ell+2.
```

In the second branch every candidate is `up+vq`, where the two coefficient-
degree allowances sum to `2s-ell=e-1`. Thus the remaining `M=4,t=3` problem
is no longer an arbitrary locator-triple census: it is the split-monic exact-
defect locus inside four fixed two-generator families. The basis-pair
determinant is a nonzero scalar times `L_1L_2L_3`, so for a core-divisor
candidate saturation is exactly `gcd(u,v)=1`. Counting the primitive pairs
for which `uF_p+vF_q` divides the core locator, with first-match multiplicity,
remains open.

The proved `pma_official_rate_small_source_degree_sieve` now removes entire
official source scales before that count. At rate `1/r`, a maximal source with
`M<=r-2` has `ell>=k+1`, while every exact core defect has `d<=k-1`; hence no
strict `d>ell` full-petal residual exists. In particular, rates `1/8` and
`1/16` have no strict residual for `M<=6` and `M<=14`, respectively. For rate
`1/4`, `M=4,t=3`, the upper mu-basis branch is possible exactly when the
background remainder satisfies

```text
2b>=ell+8.
```

The complementary branch contributes at most `4k` codewords per carried
source. Thus the `M=4,t=3` split-core-divisor count remains only at rate
`1/2` and in the rate-quarter large-background upper branch. The `M=4,t=2`,
larger-`M`, and partial-petal branches remain separate.

The proved `pma_three_petal_projective_johnson_bound` closes the remaining
rate-quarter upper branch. Distinct primitive mu-basis coefficient pairs have
core-root sets intersecting in at most `e-1`; therefore one fixed module has

```text
L <= N(d-e+1)/(d^2-N(e-1))
```

whenever the denominator is positive. It is positive for every rate-quarter
`M=4,t=3` cell, giving a complete `16n^3` per-source payment. At rate `1/2`,
all backgrounds `b<=6` and every other positive-denominator cell are paid.
Writing `d=2ell-a`, the only surviving three-petal cells satisfy

```text
b>=7,
1<=a<=floor((b-3)/4),
ell(4a-b+2)+a^2+2ab-4a<=0.
```

Thus no rate-quarter `M=4,t=3` branch remains. The explicit rate-half tail,
`M=4,t=2`, larger-`M`, and partial-petal branches remain open.

The old finite specialization `#Post<=B_post<=n^6` is false.
`pma_sigma_one_d4_generic_source_obstruction` proves that at
`(q,n,k)=(65537^2,65536,32768)` a valid source has more than `n^6`
primitive post-owner codewords already in exact cell `(d,r,a)=(4,0,6)`.
Any correct theorem must therefore print and pay this generic floor rather
than route it back to the retired `pma_wide_residual` allocation.
The variable-defect extension is superpolynomial at sigma one, so no uniform
sigma-one polynomial theorem is available. This is not an `imgfib` falsifier:
sigma one lies outside its lower cutoff, and the collision-free construction
is empty once `ell>M`.

## Scope

This target preserves all proved source reductions and global owners. It does
not assert the false `n^6` suballocation, borrow an unruled profile allowance,
count all vectors in a raw interpolation kernel, or demand a uniform
polynomial outside the stated reserve. Finite sigma-one rows require separate
exact safe/unsafe ledgers and may use the proved variable-defect family as a
lower obstruction.

## Falsifier

For every fixed `B`, an infinite reserve-admissible row/source family of
post-owner residuals larger than `n^B` after all legitimate natural-scale
profile charges; or a certified reserve-admissible row whose complete profile
allocation misses the target.

---

## WAVE-9 UPDATE (2026-07-17; pin body — supersedes the wave-8 addendum content, both preserved)


- **status:** TARGET
- **role:** corrected post-top-band polynomial/profile frontier
- **consumer:** `imgfib`

## Statement

Under the polynomial generated-field, entropy-reserve, and lower-cutoff
hypotheses stated in `imgfib`, first-match every maximal-sunflower contributor
by carried source layout. After charging exact-periodic and every other
natural-scale quotient/profile class once, the aggregate contribution outside
the layout-anchored top band admits a complete disjoint allocation

```text
#post-top primitive residual <= n^B
```

for one printed family-uniform constant `B`, while every non-polynomial
natural-scale profile is charged once to an explicit quotient/profile column. The
allocation must compose with the reserve and profile hypotheses in
`imgfib`; merely naming a larger exponent is not sufficient.

For petal size `ell=sigma+1`, one carried source layout has the exact
rational-map form

```text
R=W/L_D,
deg W<=d,
D subset C,
#{y in T:R(y)=c_(petal(y))}+r >= ell+d,
```

with `W` nonzero on the exact missed-core set `D`. The proved reserve
reduction shows that every non-planted residual has one petal containing at
least

```text
ceil(ell/M) >= ceil(ell^2/(n-k+1))
```

points of one value fiber of `R`. This is `Omega(n/log^2 n)` at the lower
cutoff. The proved `pma_saturated_mixed_support_kernel` theorem strengthens
this to an exact interpolation-kernel reduction. If `a_*` is the largest
background/petal label class in the exact noncore support, then

```text
rank T_(X,d)>=a_*-1>=m_rich-1.
rank T_(X,d)=min(d,w),       w=|X|-d-1,
```

Exact defect makes the rational pencil reduced: `gcd(L_D,W)=1`, distinct
fiber polynomials are pairwise coprime, and common-factor kernel components
are duplicate lower-defect representations rather than new codewords. The
same theorem bounds the split monic locators for this fixed exact support by

```text
binom(k-1,max(0,d-w)).
```

The complete target must now absorb, sharpen, or profile-own these canonical
root-pinned charges and sum exact supports while handling every defect and
background state, below-floor full petals, and mixed/diffuse partial petals.

The proved `pma_petal_pattern_root_pinning_ledger` performs the first
nontrivial aggregate. If `t` petals are touched in `h` petal points, then

```text
#cell(d,t,h)
 <= binom(M,t) binom(t ell,h)
    binom(k-1,max(0,2d+1-h)).
```

No background-support multiplier appears: the petal pattern and locator
determine the numerator and hence its background roots. Writing

```text
u=t ell-h,       e=max(0,2d+1-h),
```

every fixed `u+e` region is polynomial at the lower cutoff. The live
aggregate residual is therefore restricted to `u+e->infinity`. For full
petals this means `2d+1-t ell->infinity`; growing `d-ell` alone is no longer
an open regime.

The proved `pma_full_petal_band_composition` theorem now composes this ledger
with the layout-anchored top band using the correct parameters. The carried
chart contains all `M` source petals, while `t` counts only those touched by
the codeword; the equality `M=t` is false in general. All full-petal sources
with `M<=3` are paid, as is the `M=4,t=4` stratum. A remaining full-petal
family must satisfy

```text
M>=4,       d<ell(M-2),       t<2M-4,
max(0,2d+1-t ell) -> infinity.
```

Mixed and diffuse partial-petal profiles retain the general `u+e->infinity`
condition.

The proved `pma_coset_subtwoell_saturation_exclusion` theorem removes a sharp
scoped subcase. In a genuine constant-shift locator pencil `P-a_i`, exact
saturation excludes every full-petal contributor with

```text
t>=3,       ell<d<2ell.
```

Both boundaries are sharp: saturated examples exist for `t=2` inside the
strip and at `d=2ell` with three petals. This does not yet remove a universal
PMA stratum. Multiplicative-coset charts are the special case `P=X^ell`; the
carried G1 atlas has those petals in the paid top band. No proved source
theorem places every surviving below-band layout in one common constant-shift
pencil. The arbitrary-locator complement therefore remains in this target. A
future source bridge would eliminate the entire `M=4,t=3` stratum, because
root pinning pays `d<=ell` and the top band pays `d>=2ell`.

The proved `pma_arbitrary_petal_source_realizability` theorem rules out a
source-only version of that bridge. Maximal sunflower sources exist for every
arbitrary disjoint petal partition, even on a smooth multiplicative domain,
and their locator polynomials need not share any nonconstant coefficient.
Therefore a usable common-pencil bridge must depend on the particular
surviving contributor and give a bounded-to-one rechart, or the
arbitrary-locator branch must be counted directly. The construction does not
itself produce an unpaid residual contributor and is not a PMA counterexample.

The proved `pma_three_petal_mu_basis_reduction` theorem gives the exact normal
form for that arbitrary-locator branch. For three touched full petals in the
strict strip, write `d=ell+s` and

```text
W-c_iF=L_iA_i,       deg A_i<=s.
```

The three locator products obey one exact syzygy. The syzygy module has a
reduced basis of degrees `mu` and `ell-mu`. Exact-defect saturation forces

```text
s<ell/2  ==>  mu=s and one projective candidate,
s>=ell/2 ==>  mu>=ell-s and dim=2s-ell+2.
```

In the second branch every candidate is `up+vq`, where the two coefficient-
degree allowances sum to `2s-ell=e-1`. Thus the remaining `M=4,t=3` problem
is no longer an arbitrary locator-triple census: it is the split-monic exact-
defect locus inside four fixed two-generator families. The basis-pair
determinant is a nonzero scalar times `L_1L_2L_3`, so for a core-divisor
candidate saturation is exactly `gcd(u,v)=1`. Counting the primitive pairs
for which `uF_p+vF_q` divides the core locator, with first-match multiplicity,
remains open.

The proved `pma_official_rate_small_source_degree_sieve` now removes entire
official source scales before that count. At rate `1/r`, a maximal source with
`M<=r-2` has `ell>=k+1`, while every exact core defect has `d<=k-1`; hence no
strict `d>ell` full-petal residual exists. In particular, rates `1/8` and
`1/16` have no strict residual for `M<=6` and `M<=14`, respectively. For rate
`1/4`, `M=4,t=3`, the upper mu-basis branch is possible exactly when the
background remainder satisfies

```text
2b>=ell+8.
```

The complementary branch contributes at most `4k` codewords per carried
source. Thus the `M=4,t=3` split-core-divisor count remains only at rate
`1/2` and in the rate-quarter large-background upper branch. The `M=4,t=2`,
larger-`M`, and partial-petal branches remain separate.

The proved `pma_three_petal_projective_johnson_bound` closes the remaining
rate-quarter upper branch. Distinct primitive mu-basis coefficient pairs have
core-root sets intersecting in at most `e-1`; therefore one fixed module has

```text
L <= N(d-e+1)/(d^2-N(e-1))
```

whenever the denominator is positive. It is positive for every rate-quarter
`M=4,t=3` cell, giving a complete `16n^3` per-source payment. At rate `1/2`,
all backgrounds `b<=6` and every other positive-denominator cell are paid.
Writing `d=2ell-a`, the only surviving three-petal cells satisfy

```text
b>=7,
1<=a<=floor((b-3)/4),
ell(4a-b+2)+a^2+2ab-4a<=0.
```

The proved `pma_ratehalf_core_triple_excess_reduction` now gives that tail a
constant-size failure certificate. Fixing the touched triple identifies its
contributors with a core Reed-Solomon list of length `N=4ell+b-2`, dimension
`K_0=ell+b-1`, and agreement `m=2ell+b+a-2`. Any three contributors force,
after removing their common pair-difference factor, a nonconstant rational map
`phi` satisfying

```text
|phi^-1({0,1,infinity}) intersect (C\T)|>=2r+3a,
```

where `r=deg phi` in reduced form. If no such source-coupled certificate
exists, all four touched triples and all tail defects contribute at most `8n`
codewords per carried source. This is not a generic smooth-core property: an
exact smooth order-100 arbitrary-core fixture realizes the required excess at
the first `J=0` tail row.
The remaining theorem must use the special PMA core word
`y=-P_*/(L_1L_2L_3)` or route the certificate to a legitimate natural-scale
owner. Thus no rate-quarter `M=4,t=3` branch remains. Only these source-coupled
rate-half certificates, `M=4,t=2`, larger-`M`, and partial-petal branches remain
open.

The proved `pma_ratehalf_source_aligned_gcd_excess` theorem makes that source
coupling explicit. Let `E_c` be the degree-`<3ell` CRT polynomial satisfying
`E_c=c_i mod L_i`. Euclidean division gives

```text
L_C E_c=P_*+L_1L_2L_3Y,
```

so `y=Y|_C`; for fixed core and petals these words form a three-dimensional
linear code of minimum distance at least `K_0=ell+b-1`. For three contributors
put `P_i=P_*+LH_i`, `A=H_1-H_2`, and `B=H_1-H_3`, and define

```text
u_12=deg gcd(L_C,A,P_1),
u_13=deg gcd(L_C,B,P_1),
u_23=deg gcd(L_C,B-A,P_2),
tau =deg gcd(L_C,A,B,P_1).
```

The remaining tail certificate is exactly

```text
u_12+u_13+u_23-tau>=2(K_0-1)+3a.
```

This excludes ambient equality fibers that do not carry the actual source
value. A closing theorem may now target this aligned gcd inequality directly
or own every solution at its natural scale.

The proved `pma_ratehalf_source_crossratio_fiber_reduction` removes the two
redundant source-label coordinates. Affine changes of the labels preserve all
agreement sets, so every distinct triple normalizes to `(0,1,lambda)`. Modulo
the core `RS(C,K_0)` code, this is the projective one-parameter family of the
source quotient code. If `P_2,P_3` are the source numerator bases for
`(0,1,0)` and `(0,0,1)`, then

```text
P_2=L_1L_3R_2,       P_3=L_1L_2R_3,
deg R_2,deg R_3<ell.
```

Thus the coefficient of `lambda` vanishes on at most `ell-1` core points.
After removing their maximum overlap weight, every three-contributor tail
cell retains at least

```text
2b+3a-2
```

weighted nonexceptional incidences, all voting for the unique cross-ratio

```text
lambda=-(P_2(x)+L(x)h(x))/P_3(x).
```

The selected `M=4,t=3` endpoint is now a uniform count or owner for this
positive weighted `lambda` fiber.

The proved `pma_ratehalf_two_petal_support_fiber_reduction` removes the
contributor polynomial from that endpoint. For an exact `m`-point core
agreement set `S`, the second-petal congruence uniquely determines

```text
V_S=rem_(L_2)(L_3R_2 L_S^(-1)).
```

The third-petal congruence defines the support map

```text
Phi(S)=rem_(L_3)(L_SV_S(L_2R_3)^(-1)).
```

Exact contributors are in bijection with the guarded fiber

```text
|S|=m,
deg V_S<=ell-a,
gcd(V_S,L_C/L_S)=1,
Phi(S)=lambda as a constant polynomial.
```

The inverse is `H_S=(L_SV_S-F_lambda)/(L_2L_3)`. No separate missed-core or
coefficient multiplier remains. The selected tail theorem is therefore a
uniform bound or natural-scale owner for this exact guarded subset-map fiber.

The proved `pma_ratehalf_complement_linear_slice_reduction` gives a linear
coordinate form for the same fiber. Write `E_c=L_1Etilde`, put
`M=L_2L_3`, and complement `S` inside the core by
`D=L_C/L_S`, of degree `2ell-a`. Then the exact fiber is

```text
D|L_C, D monic, deg D=2ell-a,
deg rem_M(D Etilde)<=ell-a,
gcd(D,rem_M(D Etilde))=1.
```

Multiplication by `Etilde` is invertible modulo `M`, so the unguarded
condition is a linear slice of dimension `ell-a+1` and codimension
`ell+a-1` in `K[X]/(M)`. This identifies the live endpoint as one precise
BC/SCK-shaped split-in-subspace divisor atom. It does not prove flatness or
an ordinary-prefix conjugacy. After truncation to degree `2ell-a`, the slice
is exactly the already-proved three-petal mu-basis space. On a nonempty
guarded upper-branch cell its dimension is `ell-2a+2`, so this coordinate
change recovers rather than reduces the earlier `e+1` freedom.

The old finite specialization `#Post<=B_post<=n^6` is false.
`pma_sigma_one_d4_generic_source_obstruction` proves that at
`(q,n,k)=(65537^2,65536,32768)` a valid source has more than `n^6`
primitive post-owner codewords already in exact cell `(d,r,a)=(4,0,6)`.
Any correct theorem must therefore print and pay this generic floor rather
than route it back to the retired `pma_wide_residual` allocation.
The variable-defect extension is superpolynomial at sigma one, so no uniform
sigma-one polynomial theorem is available. This is not an `imgfib` falsifier:
sigma one lies outside its lower cutoff, and the collision-free construction
is empty once `ell>M`.

## Scope

This target preserves all proved source reductions and global owners. It does
not assert the false `n^6` suballocation, borrow an unruled profile allowance,
count all vectors in a raw interpolation kernel, or demand a uniform
polynomial outside the stated reserve. Finite sigma-one rows require separate
exact safe/unsafe ledgers and may use the proved variable-defect family as a
lower obstruction.

## Falsifier

For every fixed `B`, an infinite reserve-admissible row/source family of
post-owner residuals larger than `n^B` after all legitimate natural-scale
profile charges; or a certified reserve-admissible row whose complete profile
allocation misses the target.
