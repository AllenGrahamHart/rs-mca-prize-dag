# Proof

The quotient external-product ledger proves that the row root sets in every
nonexceptional two-active-row orbit are disjoint. Both are subsets of the
roots of `P_Z`, so `(PCT1)` is a degree-`e` split squarefree polynomial.

At an internal slope `xi_i`, pair-Lagrange specialization gives

```text
Q(xi_i;x)=lambda_i B(x)A(x)/D_i(x).                 (1)
```

On the antipodal branch, `A(x)=E(u)`, `D_i(x)=u-u_i`, and

```text
B(x)B(-x)=-product_(t in T)(u-t^2).                 (2)
```

On the constant-product branch, `A=X^eE(X+c/X)` and

```text
[A(x)/D_i(x)][A(c/x)/D_i(c/x)]
 =c^(e-1)E(u)^2/(u-u_i)^2,                          (3)
B(x)B(c/x)=product_(t in T)(c+t^2-tu).              (4)
```

Divide `P_Z(xi_i)` by the product of `(1)` at the two orbit members. Equations
`(2)--(4)` give, in either branch,

```text
K_u(xi_i)=chi(u) mu_i (u-u_i)^2.                    (5)
```

The polynomial

```text
u^2M_0-2uM_1+M_2
```

takes the value `mu_i(u-u_i)^2` at `xi_i`. Since `K_u-a_uI` has degree less
than `e`, interpolation of `(5)` proves `(PCT3)`.

The three `M_j` are independent: a linear dependence, evaluated at all
`xi_i`, would give a degree-at-most-two polynomial vanishing at the `e>=3`
distinct values `u_i`. It must be zero. They have degree below `e`, while
`I` is monic of degree `e`, proving four-dimensionality. The coefficients in
`(PCT3)` immediately satisfy `(PCT5)`.

Suppose `[K_u]=[K_v]`. Evaluating a proportionality at all internal slopes
and cancelling the nonzero `mu_i,chi(u),chi(v)` gives one scalar `d` with

```text
(u-u_i)^2=d(v-u_i)^2       for every i.             (6)
```

The difference of the two sides is a degree-at-most-two polynomial in
`u_i`. It has at least three distinct roots, so it is identically zero.
Comparison of its quadratic and linear coefficients gives `d=1` and `u=v`.
Thus the projective divisors are distinct.

It remains to count them. The exceptional-pair root set of `A` is invariant
under `tau`. An orbit meeting `C` in one point either crosses the five-point
boundary `T union {s,x_0}` or is a fixed point of `tau` lying in `C`.
Therefore

```text
h=deg C_1<=5                         (antipodal),
h<=7                                 (constant product).             (7)
```

Since `2p+h=6e+3`, `(7)` gives `p>=3e-1` and `p>=3e-2`, respectively.
Deleting the zero-or-one identical-row orbit leaves the counts in `(PCT6)`.
QED.
