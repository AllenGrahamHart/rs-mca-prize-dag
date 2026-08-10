# Proof

The four-Hankel theorem gives, for `s=0,1`,

```text
sum_x omega_x^(s)v_xv_x^T=0,
sum_x x omega_x^(s)v_xv_x^T=0.                         (1)
```

Subtracting `x_0` times the first identity from the second proves `(MSV2)`;
the coefficient of the `x_0` term is exactly zero.

The weights are the nonzero dual-column rescalings of representatives of
the two source words. If their joint support had size at most

```text
rho=4m-1,
```

that support would be a column error taking the pair to the zero codeword
pair. This contradicts column-farness. Their joint support therefore has at
least `rho+1=4m` points. Removing `x_0` loses at most one and proves the
preliminary bound `|U|>=rho`; the upper bound is immediate.

We exclude the two remaining small values using the full Hankel matrices.
Let

```text
r_x=(1,x,...,x^rho)^T,
L_s=H_(1,s)-x_0H_(0,s)
   =sum_(x!=x_0)(x-x_0)omega_x^(s)r_xr_x^T.           (2)
```

Choose a parameter `t` outside the finitely many coordinate-cancellation and
kernel-boundary values. Then `L(t)=L_0+tL_1` has support exactly `U`, with
every diagonal weight nonzero, `Q(t;X)` has degree `rho`, and the original
rectangular kernel equations give

```text
L(t)q(t)=0.                                           (3)
```

If `|U|=rho+1`, the square Vandermonde matrix
`(x^i)_(0<=i<=rho,x in U)` is invertible. Its diagonal factorization in
`(2)` makes `L(t)` invertible, contradicting `(3)`.

If `|U|=rho`, the same Vandermonde factorization has rank `rho` and its
one-dimensional radical is the coefficient vector of the fixed locator

```text
Lambda_U(X)=product_(x in U)(X-x).                    (4)
```

Equation `(3)` makes `Q(t;X)` proportional to `Lambda_U` for every generic
`t`. This would make the projective kernel curve constant, contrary to the
proved independence of the `m+1` coefficient vectors of `Q`. Therefore
`|U|>=rho+2=4m+1`, proving `(MSV4)`.

For `x in U`, put

```text
a_x=(x-x_0)omega_x^(0),       b_x=(x-x_0)omega_x^(1).                (5)
```

The pair `(a_x,b_x)` is nonzero. Over the algebraic closure, each equation

```text
alpha a_x+beta b_x=0
```

forbids one projective choice `[alpha:beta]`. There are only finitely many
`x`, so choose a projective pair outside their union. Taking that linear
combination of `(MSV2)` gives `(MSV5)` with
`lambda_x=alpha a_x+beta b_x!=0` for every `x in U`.

Expanding the outer product in `(MSV5)` identifies its `(i,j)` entry with
the coefficient of `z^i w^j` in `(MSV6)`, so the two statements are
equivalent.

Finally the clean endpoint has `d_x=m` for every `x!=x_0`. The clean norm
corollary therefore says that `Q(z;x)` has exactly `m` distinct roots, all
in the supported set. This proves the split-locator assertion and completes
the theorem. QED.
