# Proof

The pair-Lagrange normalization and monic row normalization give, at every
active outside row `x`,

```text
Q(z;x)=q_e(x)G_x(z),       G_x(0)=A(x)/q_e(x).        (1)
```

Exact row degree makes `q_e(x)` nonzero. The support sets are disjoint, so
`A(x)B(x)` is also nonzero and hence so is `s_x`.

At an internal slope the complement-residue theorem gives

```text
G_x(0)/G_x(xi_i)=D_i(x)/(lambda_i B(x)).              (2)
```

Since `G_xH_x=P_Z`, equations `(1)--(2)` imply

```text
s_xH_x(xi_i)
 =B(x)G_x(0)P_Z(xi_i)/G_x(xi_i)
 =c_iD_i(x)
 =c_i(pi_i-sigma_i x+x^2).                            (3)
```

Interpolation at the `e` distinct roots of `I` defines the three unique
degree-less-than-`e` polynomials in `(CKL4)`. Equation `(3)` says that

```text
s_xH_x-(R_0+xR_1+x^2R_2)
```

vanishes at every root of the squarefree polynomial `I`. It is therefore
divisible by `I`. Its degree is at most `2e`, proving the unique quotient
`J_x` and its degree bound in `(CKL5)`. Because `H_x` and `I` are monic and
the `R_j` have degree less than `e`, comparison of the coefficient of
`z^(2e)` gives

```text
[z^e]J_x=s_x.                                         (4)
```

The evaluation vectors of `R_0,R_1,R_2` are obtained from the coefficient
vectors of `D_i` by multiplying row `i` by the nonzero scalar `c_i`.
Evaluation on the roots of `I` is an isomorphism for polynomials of degree
less than `e`. Consequently

```text
dim span{R_0,R_1,R_2}=dim span{D_1,...,D_e},          (5)
```

which proves the rank assertion.

Finally, external split-design saturation says that every root of `P_Z`
occurs in exactly `r=2e+1` of the monic row locators `G_x`. Therefore

```text
product_(x in C)G_x=P_Z^r.                            (6)
```

There are `6e+3` active rows, so

```text
product_(x in C)H_x
 =P_Z^(6e+3)/product_xG_x
 =P_Z^(4e+2).                                         (7)
```

Multiplying `(CKL5)` over all active rows and using `(7)` proves `(CKL6)`.
QED.
