# Proof

Move `sigma` to affine parameter zero and expand

```text
Qbar(z;T)=sum_(i=0)^e Q_i(T)z^i.                    (1)
```

The complete coefficient chain paired with the `r_sigma+1` specialized
left-kernel multiples gives, for every `0<=i<=e` and
`0<=j<=r_sigma`,

```text
sum_(x in X)eta_x x^j Q_i(x)=0.                     (2)
```

By `(QR21)--(QR22)`, `m=r_sigma+3`, so the weighted Vandermonde matrix in
`(2)` has `m-2` rows and nullity two. The two vectors

```text
(1/L_X'(x))_(x in X),       (x/L_X'(x))_(x in X)    (3)
```

span its nullspace. Indeed, the Lagrange leading-coefficient identity gives

```text
sum_(x in X)R(x)/L_X'(x)=0       for deg R<=m-2,    (4)
```

and `(4)` applies to `R(T)=T^j` and `T^(j+1)` for
`0<=j<=m-3`.

Therefore for every coefficient index `i` there are scalars `a_i,b_i` with

```text
eta_x Q_i(x)=(a_i+xb_i)/L_X'(x).                    (5)
```

Let `A=sum_i a_i z^i` and `B=sum_i b_i z^i`; homogenization gives `(QR23)`.

We next show that `A,B` are independent. If their coefficient matrix had
rank at most one, all nonzero row forms on `X` would be proportional. They
would then share one squarefree set of `e` supported locator slopes. The
same full-locator estimate as in the sharp-pair exclusion puts those `e`
slopes, together with `sigma`, on one codeword pencil: with `H` the one or
two padded heavy rows,

```text
|E_alpha union E_beta union E_delta|
 <=(rho+3+|H|)+rho-(r_sigma+4)
 =2rho+|H|-r_sigma-1<=2rho.                         (6)
```

The chosen orientation gives the last inequality; when both two-simple
endpoint deficits vanish, the endpoint locators have no padding and the
left side is instead at most `2rho-1`.

The residual pencil on that codeword line has joint support
`U=S_alpha union S_beta`. Removing the fixed core gives `|U\{s_0}|=rho+2`
light points. Each has global supported degree `e` and hence misses exactly
one of the `e+1` selected slopes. But the slope `gamma` misses

```text
(rho+2)-(rho-r_gamma-1)=r_gamma+3
```

light points. Summing would give

```text
rho+2=sum_gamma(r_gamma+3)>=3(e+1)=3e+3,
```

contrary to `rho+2=3e+1`. Thus the coefficient-row rank is exactly two, and
`A,B` are linearly independent.

Every `x in X` is light. Its row form therefore has exact degree `e`, is
squarefree, and cuts out its `e` supported locator slopes. If
`A+xB` and `A+yB` were proportional for distinct `x,y`, independence of
`A,B` would force both the proportionality scalar to be one and `x=y`.
This proves row-coordinate injectivity.

Let `G=gcd(A,B)`. A common root of two distinct forms `A+xB,A+yB` forces
both `A` and `B` to vanish there; conversely every root of `G` is common to
all the forms. Squarefreeness of every row form shows that `G` and all
residual factors are squarefree, and that the residual root sets for
distinct `x` are disjoint. All roots lie among the `T=3e+3` supported
slopes, so their union has size

```text
g+m(e-g)<=3e+3.                                     (7)
```

Since every `x in X` belongs to `S_tau`, `tau` is a common root. Since no
`x in X` belongs to `S_sigma`, `sigma` is not a common root. Hence `g>=1`.
Substituting `m=r_sigma+3` into `(7)` gives

```text
(r_sigma+2)g>=r_sigma e-3,                          (8)
```

which proves `(QR25)`.

Finally, at every root `delta` of `G`, the locator `E_delta` contains all of
`X`. Estimate `(6)` therefore applies and puts its assigned center on the
endpoint codeword pencil. That pencil contains the `g` roots of `G` plus
`sigma`; its deficit includes `r_sigma+sum_(delta in Z(G))r_delta`.
Applying the one-third center cap from the sharp-pair exclusion proves
`(QR26)`. QED.
