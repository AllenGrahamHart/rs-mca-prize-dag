# Proof

The projected cell-0 lex basis forces `b^2-6b+1=0`, and that quadratic has
the two deployed roots in `(KBC0P-1)`. Its two equations linear in `c`
give `C_b(t)`. On each branch, the coefficient of `c` and the constant
term are coprime, so a zero coefficient cannot create an omitted projected
component.

Apply the division-free reconstruction of common-kernel uniqueness and
substitute `(KBC0P-1)`. Clearing the common denominator and taking the gcd
of all eight coefficient numerators gives exactly the scale `(KBC0P-2)`.
The common source-label guards imply `t(t^4-1)!=0`, and coprimality excludes
zeros of `D_b`; hence this scale is nonzero on every admissible common
point. Cancelling it preserves the projective coefficient vector. Exact
factorization gives `(KBC0P-3)` and the sealed degree-at-most-eight packet.

For any source root `z`, the product and unsquared sum carried there are

```text
F(z^2)=N/D,             S(z)=-Q/D.
```

Write `p_0=de`, `p_1=-de`, `s_0=d+e`, and `s_1=d-e`. Substituting
`N_j=p_jD_j` proves the first equation in `(KBC0P-5)`. Since
`Q_j=-s_jD_j`, the second equation becomes

```text
D_0^2D_1^2 ((d+e)^2-(d-e)^2-4de)=0,
```

and therefore also vanishes. Thus `(KBC0P-5)` is necessary.

Every actual packet has nonzero leading support `D_j` at all twelve source
labels by the quadratic paired-product interface. Its outside labels are
nonzero and disjoint from the five common labels. The two labels carrying
`DE+` and `DE-` are distinct: equality would make the single-valued product
map satisfy `de=-de`, impossible in odd characteristic with nonzero target
roots. Hence every saturated guard used in `(KBC0P-6)` is necessary.

The exact branch computations both return dimension `-1`, basis size one,
and basis `<1>`, with no stderr. So no representative-sign outside packet
exists. The exact source-projectivity quotient carries complete Vieta
packets throughout all four signs of cell `0`. Deleting that size-four
orbit from the prior 44 raw rows leaves 40 rows in six orbits. QED.
