# Proof

Let `H` be the large class and let `mathcal A` be the aligned set from the
dependency. For `u in mathcal A`, write

```text
K_u=c(u)P_HR(u,Z)                                   (1)
```

with `c(u)` nonzero. The aligned row gcd is the fixed static denominator
`B`. At an internal slope `xi_i`, the calibrated bounded-tail formula gives

```text
K_u(xi_i)=chi(u)B(xi_i)mu_iN_i(u).                  (2)
```

All factors outside `N_i` are nonzero. Thus, for any internal indices `i,j`
and every aligned `u`,

```text
R(u,xi_i)N_j(u)=c_ij R(u,xi_j)N_i(u)                (3)
```

for one nonzero constant `c_ij`. Both sides have `U`-degree at most four,
while `|mathcal A|>=e-44>4`. Hence `(3)` is a polynomial identity in `U`.

Choose two good pair indices. Their norms are the coprime quadratics
`(U-u_i)^2` and `(U-u_j)^2`, with `u_i!=u_j`. Equation `(3)` implies
`N_i|R(U,xi_i)`. Both are nonzero of degree at most two, so they are
proportional. Repeating against one fixed good index proves `(QPRD2)` for
all at least `e-t` good indices.

Write `k=deg_Z R(u,Z) in {1,2,3,4}`. The dependency constructs `R` by
factoring `P_H` coefficientwise, so every `R_j` has degree at most `k`;
equivalently, any coefficient above degree `k` would be a quadratic in `U`
vanishing at more than two aligned coordinates.

The discriminant

```text
Delta(Z)=R_1(Z)^2-4R_2(Z)R_0(Z)                     (4)
```

has degree at most eight. It vanishes at every good internal slope by
`(QPRD2)`. Since `e-t>8`, it is identically zero. This proves
`(QPRD3)--(QPRD4)`. The coefficient `R_2` is nonzero because the good norm
quadratics have nonzero leading coefficient.

Fix an aligned `u`. Let `delta` be a root of the nonconstant squarefree
polynomial `R(u,Z)`. In `(QPRD4)`, the order of the right-hand side at
`delta` is even, whereas the order of `R(u,Z)` is one. Therefore
`ord_delta(R_2)` is positive and odd. Every one of the `k=deg R(u,Z)`
distinct roots is a root of `R_2`. Since `deg R_2<=k`, the two polynomials
are proportional.

Thus every aligned residual is projectively `[R_2]`, and every aligned
complement is projectively `[P_HR_2]`. But calibrated evaluation at three
good internal indices shows distinct orbit coordinates give distinct
projective complements: proportionality for `u,v` would imply

```text
(u-u_i)^2=c(v-u_i)^2
```

at three distinct `u_i`, forcing `u=v`. Here the official characteristic is
odd: three roots make the quadratic identity in `u_i` identically zero, its
leading coefficient gives `c=1`, and its linear coefficient gives `u=v`.
The aligned set has far more than one coordinate, a contradiction. QED.
