# Proof

For `y!=x_i`, factorization of the six-set locator gives

```text
Lambda'_X(y)=(y-x_i)Lambda'_(S_i)(y).
```

Thus `(SQ1)` restricts to `1/Lambda'_(S_i)(y)` on `S_i`. It is the unique
dual word of the length-five cubic evaluation code, extended by zero at
`x_i`. In particular it is a valid row combination of the parity block for
any selected agreement block containing `S_i`.

At a coordinate `y in X`,

```text
sum_i c_i mu_i(y)
 = (y sum_i c_i-sum_i c_i x_i)/Lambda'_X(y).
```

Since `X` has at least two points, the first identity in `(SQ2)` is
equivalent to

```text
sum_i c_i=0,       sum_i c_i x_i=0.                   (1)
```

The same calculation after multiplying row `i` by `gamma_i` shows that the
second identity is equivalent to

```text
sum_i c_i gamma_i=0,
sum_i c_i x_i gamma_i=0.                              (2)
```

Equations `(1)`--`(2)` prove the kernel description `(SQ4)`.

The proved six-face law supplies constants `alpha,beta,chi,delta` such that

```text
gamma_i=(alpha+beta x_i)/(chi+delta x_i)               (3)
```

on every selected face. The denominators are nonzero there. Since the
selected slopes are distinct, the fractional-linear map is nonconstant, so

```text
beta chi-alpha delta !=0.                              (4)
```

Scale column `i` of `B_X` by `chi+delta x_i`. The scaled column is the value
at `x_i` of

```text
(chi+delta X, X(chi+delta X),
 alpha+beta X, X(alpha+beta X)).                       (5)
```

All four entries lie in the three-dimensional polynomial space
`F[X]_<3`, so `rank B_X<=3`. The coefficient map from `(1,X,X^2)` to the
four polynomials in `(5)` has trivial kernel: its first and third entries
kill the constant and linear coefficients by `(4)`, and then its second and
fourth entries kill the quadratic coefficient. Hence it has rank three.
Any three distinct evaluation points are independent for `F[X]_<3`, so
`rank B_X=3`. Rank-nullity proves `(SQ3)`.

Now consider an `R=6` rank-two trade from the support atlas. Its active rows
all have weight five and their zero sets are distinct singletons. Therefore
their supports are precisely distinct faces `X\{x_i}` of their six-point
active union. A dual-cubic word with that five-point support is a scalar
multiple of `mu_i`. The two trade identities consequently put its scalar
coefficient vector in `ker B_X`. This is exactly the local syzygy space just
described.

The support atlas has three `R=6` profiles and only two profiles with larger
active union, namely `(SQ5)`. Quotienting the left kernel by the span of all
six-face spaces kills every relation in the first group. Thus any surviving
rank-two class must have `R=7` or `R=8`, proving the final assertion.
