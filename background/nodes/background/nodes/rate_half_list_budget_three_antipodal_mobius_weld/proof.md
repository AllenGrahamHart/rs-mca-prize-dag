# Proof

Choose `U=G_0`. Since the span has dimension two, some `G_j-G_0` is nonzero;
after relabeling put `V=G_1-G_0`. The polynomials are monic of one degree, so
`deg V<=r-1`. Every `G_i` has a unique expression `U+c_iV`. Pairwise
coprimality and positive degree make the `G_i` distinct, so the `c_i` are
distinct. This proves `(AMW2)`.

Substitute `(AMW2)` in the two relations `(AMW1)`. Independence of `U,V`
gives

```text
sum_i lambda_i=0,             sum_i lambda_i c_i=0,
sum_i lambda_i a_i=0,         sum_i lambda_i a_i c_i=0. (1)
```

Thus the matrix with columns

```text
(1,a_i,c_i,a_ic_i)^T
```

is singular. The `a_i` are distinct because the deleted quadratics are
pairwise coprime, and the `c_i` are distinct by the preceding paragraph.
There is a unique fractional-linear map taking the first three `a_i` to the
first three `c_i`. The standard cross-ratio determinant for the displayed
matrix vanishes exactly when it also takes the fourth `a_i` to `c_i`.
Equation `(1)` therefore proves `(AMW3)`.

Write

```text
T(a)=(alpha a+beta)/(gamma a+delta),
alpha delta-beta gamma!=0.                              (2)
```

No denominator `gamma a_i+delta` vanishes because every `c_i` is finite.
Define

```text
R=delta U+beta V,       S=gamma U+alpha V.              (3)
```

The change from `(U,V)` to `(R,S)` is invertible. Moreover

```text
R+a_iS=(gamma a_i+delta)(U+c_iV)
       =(gamma a_i+delta)G_i.                           (4)
```

This is `(AMW4)` with `mu_i=(gamma a_i+delta)^(-1)`.

Multiplying `(4)` over the four indices and substituting the descent product

```text
product_i G_i=(Y^d-1)/product_i(Y-a_i^2)
```

gives `(AMW5)` with
`kappa=product_i(gamma a_i+delta)`. Every factor is nonzero. QED.
