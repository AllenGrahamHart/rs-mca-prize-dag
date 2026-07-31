# Proof

Work over the deployed characteristic `P=2130706433`. The corrected
fraction-free reconstruction gives the exact relative scale

```text
-3(b-1)(b+1)(p-1)(w-1)(w+1)
  (p+2t+4)(4p+2t+1)(5p+4t+5)
-------------------------------------------------- .
       pw-4p+2tw-2t+4w-1
```

After clearing this denominator and removing exactly `w^2(p-1)^2`, all four
swapped-allocation equations are reciprocal quartics in `b`. Coefficientwise
reciprocity is checked before replacing
`b^2+b^-2` by `trace^2-2`. The resulting equations are quadratic in
`trace`, with `(total degree, terms)`

```text
(18,1116), (18,1267), (15,536), (15,603).
```

Let `M(p,t,w)` be their `4 x 3` coefficient matrix. A common trace root
implies `rank(M)<=2`. The four maximal minors factor into open/boundary
factors and residuals of `133,159,155,158` terms. If the first two rows have
kernel coordinates `(K_2,K_1,K_0)`, a trace point also requires
`K_2 K_0-K_1^2=0`; this equation remains necessary when the cross product
vanishes.

## Divisorial support

Eliminating `w` from residual minor 0 against residual minors 1, 2, and 3
shows that their common divisorial support, after open factors, is

```text
L = 4p+5t+4,
H = pt+5p+t.
```

On `L=0`, the gcd of all four minors with the conic is associate to

```text
t^2(t+1)(t+4)(w-1),
```

which is supported on `q(1)=0`, the endpoint discriminant, or `w=1`.

Over the function field of `H`, all four residual minors share one linear
root in `w`. Its conic value is nonzero generically. The norm of that value
has degree 26 in `t` and six irreducible factors. Four factors are entirely
on the base forbidden product. The other two, of degrees one and two, each
leave one determinant/conic `w` root; direct substitution in all four
original trace quadratics gives gcd one. The sole root-formula denominator
is `t+5`; together with `H` it would force `-5=0`, so it has no affine
component point.

## Off-common support

After dividing all common and open factors from the three star projections,
their cofactors have digests

```text
bd7f29ac722c6a42084e9a65f6c687daf9cef0d13d121ce129e7ce606fd28d92
8abd5c5c46bd6380dce7581bf0b2c681ab58d48a664693ee9055ea97fe0c3fce
e5d10f1a8637f850e6dacf0a94de67047ec5330cdbd80a475dbdc586a50665cd
```

The gcd of the first/second and first/third `p`-resultants has degree 61 in
`t`, digest
`7389a31916a65e1ba453c98863cf77c22bd5b3ac3747d5b7ed50f9e4334a9580`,
and seven distinct irreducible factors. They are all linear. Exact endpoint
gcds produce eight distinct `p` candidates, and each kills at least one
factor of

```text
p(p-1)(p-t+1)(p+t+1)(p+2t+4)
(4p+2t+1)(5p+4t+5)(t^2-4p).
```

Thus neither a common component nor a finite off-common intersection
contains an admissible determinant/conic point. Since every common root of
the original four trace quadratics would give such a point, the cell is
empty.
