# Proof

Contract the fixed core factor and work on `D_res=D\{s_0}`. The residual
middle Hankel pencil is symmetric of size `(d+1) x (d+1)`, where
`d=rho-1`, and its primitive kernel has parameter degree `e`.

Move `alpha` to zero and expand

```text
M(z)=M_0+zM_1,
q(z)=sum_(i=0)^e z^i q_i.                           (1)
```

At `alpha`, the contracted error has exactly `d-r_alpha` distinct nonzero
moment sources. Its Vandermonde matrix has full column rank, and its diagonal
source-weight matrix is invertible. Left and right inverses of the
Vandermonde matrix therefore show that `M_0` has rank `d-r_alpha`. Moreover,
its degree-`d` kernel is precisely the polynomials vanishing on those
sources. If `Q_min` is their monic locator, this kernel, on both the left and
right because `M_0` is symmetric, is

```text
Q_min F[X]_(<=r_alpha),                             (2)
```

of dimension `r_alpha+1`.

For `i<e`, pair
`M_0q_(i+1)+M_1q_i=0` on the left with `AQ_min`; for `i=e`, pair the
terminal equation `M_1q_e=0`. Thus, for every `0<=i<=e`, every
`deg A<=r_alpha`, and `X=X_(alpha,beta)`,

```text
sum_(x in X) eta_x A(x)Q_i(x)=0,       eta_x!=0.    (3)
```

Here the source is obtained by subtracting the codeword line through the
two centers and then contracting by `X-s_0`. The core belongs to both error
supports, so it is not in `X`; every contraction factor and every displayed
source weight is nonzero.

Let `m=|X|`. The evaluation matrix in `(3)` has `r_alpha+1` rows. If
`m<=r_alpha+1`, it has full column rank, and `(3)` would force

```text
Q_i(x)=0       for every x in X and every i.         (4)
```

The set `X` is nonempty by column-farness. Equation `(4)` would make one of
its residual domain points a further parameter-independent factor of
`Qbar`. The retained branch has exact core degree one, and that factor was
already contracted, so this is impossible. Hence

```text
m>=r_alpha+2.                                       (5)
```

Since `|S_alpha|=rho-r_alpha`,

```text
m=|S_alpha union S_beta|-|S_alpha|
 =j_(alpha,beta)+r_alpha.                           (6)
```

Equations `(5),(6)` prove `(QRS4),(QRS6)`. Once `m>=r_alpha+2`, the
Vandermonde matrix in `(3)` has rank `r_alpha+1`, so its nullspace has
dimension

```text
m-(r_alpha+1)=j_(alpha,beta)-1.                     (7)
```

The nonzero diagonal weights preserve rank, proving `(QRS5)`. At `j=2`,
the coefficient evaluation matrix has rank at most one and has no zero row,
which proves the proportionality assertion.

Now let one affine codeword line contain the assigned centers at `h>=2`
slopes `A`. Choose two of them. The joint support `U` of the received pencil
minus this codeword line is exactly the union of their two error supports,
so `(QRS6)` gives `|U|>=rho+2`. A nonzero affine coordinate vanishes at at
most one of the `h` slopes. Using the exact error weights `(QRS1)`,

```text
(h-1)(rho+2)
 <=sum_(gamma in A)(rho-r_gamma)
 =h rho-sum_(gamma in A)r_gamma.                    (8)
```

Rearrangement gives `(QRS7)`.

Finally fix `alpha,beta`. Any third slope whose full locator triple has
union at most `2rho` has its assigned center on the codeword line through
the first two centers, by minimum distance `2rho+1`. The line contains at
least the deficits `r_alpha+r_beta`, so `(QRS7)` bounds its total assigned
centers by

```text
floor((rho+2-r_alpha-r_beta)/2).                    (9)
```

There are `T=rho+4` supported slopes. Subtracting `(9)` from `T` gives

```text
rho+4-floor((rho+2-r_alpha-r_beta)/2)
 =ceil((rho+6+r_alpha+r_beta)/2).                   (10)
```

and every center counted there satisfies `(QRS9)`. QED.
