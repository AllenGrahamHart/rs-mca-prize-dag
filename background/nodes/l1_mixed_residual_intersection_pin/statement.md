# L1 mixed-residual intersection pin

- **status:** PROVED
- **role:** compose the independent root-pinning and B11 anchor gates
- **consumers:** `petal_mixed_amplification`, `l1_mixed_petal_amplification`

## Statement

Work in one maximal-sunflower chart at the L1 lower cutoff, with generated
field size `q=poly(n)`. Put `ell=sigma+1`. For a non-planted listed word let

```text
d = missed-core defect,
r = background agreements,
t = number of touched petals,
h = total petal agreements,
u = t ell-h,
p = sum_i min(|S_i|,ell-|S_i|),
e = max(0,2d+1-h).
```

Write the positive petal deficits in increasing order as

```text
v_(1) <= v_(2) <= ...,
G_2 = v_(1)+v_(2),
G_R = (ell-r)+v_(1).
```

Every non-planted word touches at least two petals, so these quantities are
defined. For arbitrary fixed nonnegative integers

```text
E_root, E_d, V_2, V_R,
```

the union of the two classes

```text
p+e <= E_root,                                             (I1)

d <= ell+E_d  and  (G_2 <= V_2 or G_R <= V_R)             (I2)
```

is polynomially bounded in `n`, with an exponent depending only on the four
fixed thresholds and the fixed polynomial-field exponent.

Consequently, after these proved payments the exact residual lies in

```text
p+e > E_root
and
(d > ell+E_d or (G_2 > V_2 and G_R > V_R)).               (I3)
```

This holds simultaneously with the proved reserve rich-fiber condition: one
petal contains at least

```text
ceil(ell/M) >= ceil(ell^2/(n-k+1)) = Omega(n/log_2^2 n)
```

agreements in one value fiber of `W/L_D`.

The proved `l1_two_petal_small_support_anchor_closure` removes one further
subbranch: if exactly two petals are touched and the smaller support is
bounded by any fixed `A`, then the word is already B11-paid. In particular,
the unpaid singleton-petal mixed branch has `t>=3`.

The proved `l1_polarized_b11_box_closure` gives the simplest aggregate form.
For every fixed `P,E`, the whole class

```text
p<=P,       d<=ell+E
```

is B11-paid. Thus the live residual may be restricted to

```text
p>P       or       d>ell+E,                              (I4)
```

for every fixed box, together with `(I3)` and the rich-fiber condition.

Inside the bounded-`p`, growing-`d-ell` side of `(I4)`, the proved
`l1_bounded_polarity_marked_full_pencil_reduction` supplies a canonical
bounded-mark full-petal identity. Thus that side's remaining theorem is
uniform stability of the existing full-petal split-pencil payment under a
fixed-degree mark factor, not an arbitrary mixed-support census.

The proved `l1_marked_constant_shift_subtwoell_exclusion` supplies the first
such stability result. If at least three dense petals lie in one common
constant-shift pencil, that subbranch is empty whenever their total mark
degree is `v` and `d+v<2ell`; in particular `d+p<2ell` suffices. The
two-dense, arbitrary-locator, and higher marked-degree branches remain.

More generally, `l1_marked_constant_shift_multistrip_exclusion` proves that
in strip `m ell<d`, the common-pencil branch has at most `2m` selected dense
petals unless `d+v>=(m+1)ell`. With `v<=p`, the easier upper-bound test is
`d+p<(m+1)ell`. Thus high-petal common-pencil cells are excluded uniformly
across all strips; low-petal and arbitrary-locator cells remain.

Combining the same theorem with the list threshold pins every away-from-
boundary common-pencil survivor in strip `m` to

```text
ceil((d-p+1)/ell) <= T_dense <= 2m.
```

Thus the surviving common-pencil problem is a bounded petal-width
classification in each strip, not an unrestricted many-petal family.

At the upper endpoint `T_dense=2m`, the proved
`l1_marked_constant_shift_extremal_kernel_normal_form` gives an exact
two-generator polynomial matrix. Its determinant is

```text
kappa product_(i=1)^(2m)(Z-a_i),
```

and its coefficient gcd divides the selected mark locator. Explicit
saturated examples exist in every strip, so this endpoint must be counted or
profile-owned; it cannot be removed by strengthening the rank exclusion.

The proved `l1_marked_constant_shift_forney_window_normal_form` extends the
endpoint to every `T_dense=t<=2m`. Each survivor has one reduced-basis index

```text
max(0,t-m)<=mu<=floor(t/2),       nu=t-mu,
```

determinant `kappa product_i(Z-a_i)`, and exactly `2m-t+2` coefficient
generators. Every admissible index pair is populated by a saturated family.
Thus the complete common-pencil residue is a finite Forney-stratum pricing
problem; only arbitrary-locator cells remain outside this module atlas.

Finally, `l1_marked_common_pencil_crt_fiber_bound` removes hidden numerator
multiplicity. For fixed defect locator and marks, every cell with `t>=m+1`
has at most one numerator. At `t=m`, threshold arithmetic bounds the affine
CRT fiber by `q^(2p)`. Thus for fixed `p<=P` the numerator factor is
polynomial, and the sole non-polynomial common-pencil quantity is the number
and first-match multiplicity of squarefree defect locators in the finite
Forney strata.

In a genuine quotient/coset chart,
`l1_marked_common_pencil_quotient_boundary_router` now factors each such
locator uniquely as

```text
F_D=L_(B_D) product_(a in A_full(D))(P-a),
```

where `B_D` contains no complete quotient fiber. For every fixed boundary
cap, the choices of `B_D` and all CRT numerators cost only a polynomial
factor. Thus the fixed-chart common-pencil locator frontier narrows again to
the actual full-fiber quotient-core census or to defect locators whose
partial-fiber boundary escapes every fixed cap. This is not exact-periodic
ownership and does not settle first-match overlap across source charts.

At the L1 cutoff, `l1_quotient_chart_bounded_core_boundary_closure` also
counts the full-fiber census directly. A source chart has only `O(log n)`
complete petal and core fibers, so all dense/sparse support orientations and
all quotient-core subsets together cost `2^O(log n)=poly(n)`. Consequently
every fixed `(p,beta)` box is polynomial per source chart. The strict Forney
window uses the `q^(2p)` CRT bound; on its thin complement,
`l1_marked_common_pencil_next_strip_boundary_fiber_bound` forces at least
`m+1` dense petals and gives `q^p`. The common-pencil frontier is therefore
reduced to unbounded partial-core-fiber boundary and cross-chart aggregation.

The one-sided boundary condition sharpens to symmetric core polarity. On
each complete core fiber `T_a`, put

```text
p_core=sum_a min(|D intersect T_a|,ell-|D intersect T_a|).
```

Node `l1_quotient_chart_bipolar_entropy_closure` encodes the defect by one
full/empty orientation bit per core fiber plus exactly `p_core` exceptional
points. Since petal and core fibers together number `O(log n)`, every fixed
`(p,p_core)` box is polynomial per source chart throughout every strip. Thus
the bounded-`p` quotient-chart common-pencil residue has unbounded symmetric
core polarity, not merely a large one-sided boundary, unless it arises from
cross-chart aggregation.

That growing parameter now has an exact signed-quotient normal form. If
`A_+` is the set of dense core fibers, `H` their holes, and `S` the occupied
points in sparse core fibers, then

```text
F_D L_H=L_S product_(a in A_+)(P-a),
deg L_H+deg L_S=p_core.
```

The triple `(A_+,H,S)` is canonical and reconstructs `D`. Hence the remaining
fixed-chart quotient/coset problem is a growing signed-mark quotient census
coupled to the petal numerator constraints, rather than an arbitrary
squarefree-locator count. No periodic owner follows from this identity.

Intrinsic quotient chart multiplicity is also polynomial. For a fixed
intrinsic fiber partition and received word, a core/petal role assignment
determines every source member uniquely from its agreements on the
`(k-1)`-point core plus one full petal. There are at most `3^(n/ell)` such
assignments per scale and only logarithmically many dyadic scales. At the L1
cutoff this is polynomial. Hence every fixed `(p,p_core)` box is globally
polynomial across intrinsic complete-fiber quotient charts; the growing
signed-mark census no longer carries an extra intrinsic chart multiplier.

Partial source cores no longer form an undifferentiated exception. Relative
to an intrinsic quotient partition define `p_layout` as the core's symmetric
fiber polarity and `p_defect` as the missed-core set's symmetric polarity
inside each actual core slice. Together with petal polarity `p`, four
orientation vectors over `O(log n)` fibers and bounded exception sets encode
all source charts and contributors. Thus every fixed
`(p_layout,p_defect,p)` box is globally polynomial across intrinsic dyadic
scales. In the bounded-`p` intrinsic branch, either layout or defect polarity
must grow.

Thus a super-polynomial mixed/partial family cannot merely escape one of the
two ledgers. For every fixed box it must escape both polarized root pinning
and the B11 anchor gates, while retaining the source-coupled rich fiber. Since
`p<=u`, this is strictly sharper than the former `u+e` residual.

## Scope

This is a strict intersection pin, not a count of `(I3)` or `(I4)`. It does not prove
that any parameter tends to infinity uniformly without passing to a residual
subfamily, classify rich fibers, or promote either consumer.
