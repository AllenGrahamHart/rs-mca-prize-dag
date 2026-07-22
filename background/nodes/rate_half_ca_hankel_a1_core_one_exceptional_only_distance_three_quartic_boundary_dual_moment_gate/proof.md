# Proof

Let `A` be monic, squarefree, and split with degree `d=2e`. For arbitrary
values `v_a` at its roots, the following are equivalent:

```text
v_a=f(a) for one polynomial f of degree at most four;

sum_(A(a)=0) a^j v_a/A'(a)=0,       0<=j<=d-6.       (1)
```

Indeed, if `v_a=f(a)`, then `X^jf` has degree at most `d-2`. Its Lagrange
interpolant has zero coefficient of `X^(d-1)`, and that coefficient is the
sum in `(1)`. Conversely, the `d-5` displayed parity checks are linearly
independent: after multiplying columns by the nonzero `A'(a)`, their matrix
is a Vandermonde matrix. Their common kernel therefore has dimension five,
and it already contains the five-dimensional evaluation code of
polynomials of degree at most four. This proves `(1)`. The same argument
applies coefficientwise to values in `F[z]`.

The exceptional CRT reconstruction gives

```text
Omega(z;a)=q_e(a)^2V_a(z)/C(a).                      (2)
```

Differentiating the smooth support partition at a root of `A` gives

```text
1/[C(a)A'(a)]
 =N^(-1)a(a-s)(a-x_0)B(a).                          (3)
```

Substitute `(2)--(3)` into `(1)`. The common nonzero scalar `N^(-1)` may
be removed, and the result is exactly `(QBM2)`. By the equivalence in the
CRT dependency, these checks are also equivalent to the global quartic weld
within the active-row design.

For each `k`, the two roots of `D_k` are the two base-field embeddings of
the split quadratic algebra `R_k`. Summing their contributions is exactly
the algebra trace. Grouping `(QBM2)` pair by pair proves `(QBM3)`. The
interpolation statement follows from `(1)--(2)` and uniqueness in the
degree-less-than-`d` Lagrange interpolation space. QED.
