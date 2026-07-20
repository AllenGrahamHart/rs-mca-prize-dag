# Proof

For `s=0,1,2`, define a linear functional on moment vectors by its value on
one residual-domain column:

```text
ell_s(c(x))=x^s A(x)^2.                                (1)
```

The polynomial on the right has degree at most

```text
s+2(r-1)<=2r.
```

It therefore defines a linear functional on the full `(2r+1)`-coordinate
moment space. The source identity in the quadratic-moment theorem gives

```text
ell_s(h_1)=Theta_s.                                    (2)
```

Every column `c(a)` with `a in R_A` is killed by all three functionals, so
they descend to the quotient by `W_A`. In particular, their values do not
depend on a chosen source representation of `h_1`.

Suppose `(QDR1)` has a witness `T` of size at most two. Write, modulo `W_A`,

```text
h_1=sum_(x in T) omega_x c(x),
eta_x=omega_x A(x)^2.                                 (3)
```

Equations `(2)` and the moment pin give

```text
sum eta_x=0,       sum x eta_x=0.                     (4)
```

For one point, the first equation forces its coefficient to vanish. For two
distinct points, the `2 x 2` Vandermonde matrix in `(4)` is invertible, so
both coefficients vanish. In either case `(2)` would give
`Theta_2=sum x^2 eta_x=0`, contradicting the proved nonvanishing. This proves
`(QDR2)`.

Now suppose `delta_A(h_1)=3`, with `T={x_0,x_1,x_2}`. The kernel of

```text
[[1,1,1],[x_0,x_1,x_2]]
```

is one-dimensional. The standard barycentric vector

```text
b_i=1/product_(j!=i)(x_i-x_j)                         (5)
```

satisfies

```text
sum b_i=sum x_i b_i=0,       sum x_i^2 b_i=1.        (6)
```

The first two equalities follow by taking the coefficients of `X^2` in the
degree-at-most-one Lagrange interpolants of `1` and `X`; the last follows
from the interpolant of `X^2`. Equations `(2)` and `(6)` force

```text
eta_i=Theta_2 b_i.
```

Since `A(x_i)!=0`, division by `A(x_i)^2` proves `(QDR3)--(QDR4)`.

It remains to prove uniqueness of the triple. Suppose `T'` were a second
supporting triple. Subtract the two representations, including their
possibly different `W_A` parts. The resulting linear relation is supported
on at most

```text
|R_A|+|T union T'| <=(r-1)+6=r+5
```

distinct moment columns. In the official profile `r>=4`, so `r+5<=2r+1`.
Any at most `2r+1` distinct columns `c(x)` are linearly independent by the
Vandermonde determinant. Hence every coefficient in the difference is zero.
The nonzero coefficients in `(QDR3)` then force `T=T'`, and the quotient
coefficients agree. This proves uniqueness and the exhaustive dichotomy
`(QDR5)`. QED.
