# Proof

Write a left-kernel coefficient vector in block groups as `eta_i`. Put

```text
lambda_i=eta_i^T H_i,
```

extended by zero outside `A_i`. The first and second halves of
`eta^T M_G=0` are exactly the two equations in (DT1). Since each `H_i` has
full row rank, not all `lambda_i` vanish. Its row space is the dual of cubic
evaluation on `A_i`, proving the remaining assertion in (DT1).

Let `A` have size `m=4+c`. For every polynomial `P` of degree `<c`, the
vector

```text
(P(x)/Lambda'_A(x))_(x in A)
```

annihilates all cubics. Indeed, for `0<=r<4`, the polynomial `X^rP(X)` has
degree at most `m-2`, and the standard Lagrange leading-coefficient identity
gives

```text
sum_(x in A) x^r P(x)/Lambda'_A(x)=0.
```

These vectors form a `c`-dimensional space, equal to the dual code. This
proves (DT2). A nonzero `P_i` has at most `c_i-1` roots in `A_i`, so

```text
wt(lambda_i) >= (4+c_i)-(c_i-1)=5.
```

Fix an active coordinate `x`. Restricting (DT1) to that coordinate gives

```text
sum_(i in I_x) lambda_i(x)=0,
sum_(i in I_x) gamma_i lambda_i(x)=0.              (DT4)
```

If `|I_x|=1`, the first equation is impossible; if `|I_x|=2`, the two by
two Vandermonde matrix in the distinct slopes is invertible. Hence
`|I_x|>=3`.

The kernel in (DT4) is the dual of degree-less-than-two evaluation on the
`t_x` distinct slopes. Applying the same Lagrange identity, now with code
dimension two, identifies it with the vectors

```text
(Q(gamma_i)/product_(j!=i)(gamma_i-gamma_j))_(i in I_x),
deg Q<t_x-2.
```

This proves (DT3). Finally choose any nonzero left-kernel vector supplied by
the Maxwell core. Removing zero block words and zero incidences gives the
claimed finite `(5,3)` active trade without increasing the core-size bounds.
