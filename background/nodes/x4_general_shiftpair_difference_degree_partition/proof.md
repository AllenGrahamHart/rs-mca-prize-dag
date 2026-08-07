# Proof

The two supports have the same size, so their disjoint differences `P` and
`Q` have a common size `e`.  Locator factorization gives

```text
L_S-L_S0=L_C(L_P-L_Q).                              (1)
```

The locators `L_S` and `L_S0` are monic of degree `A`.  Equality of their
first `t` sub-leading coefficients therefore gives

```text
deg(L_S-L_S0)<=A-t-1.                               (2)
```

The supports are distinct.  Hence `P!=Q`, their monic squarefree locators
are unequal, and `H=L_P-L_Q` is nonzero.  Since `deg L_C=A-e`, equations
`(1)` and `(2)` imply

```text
A-e+deg H<=A-t-1.
```

Writing `d=deg H` proves `d<=e-t-1`.  Nonzero polynomials have nonnegative
degree, so `(DD-1)` follows.

Expand the two residual locators as

```text
L_P=X^e+sum_(j=1)^e (-1)^j e_j(P) X^(e-j),
L_Q=X^e+sum_(j=1)^e (-1)^j e_j(Q) X^(e-j).
```

Their leading terms cancel.  The difference has degree zero exactly when
the coefficients of `X^(e-1),...,X` all vanish, which is exactly
`e_j(P)=e_j(Q)` for `1<=j<=e-1`.  The constant cannot also vanish, because
that would give `L_P=L_Q` and hence `P=Q`.  This proves `(DD-2)`.

Every incident same-prefix neighbour has one uniquely determined integer
`d`, so sorting the neighbours by `d` proves `(DD-3)`.  A first-owner rule,
a primitive-scale restriction, or an earlier support-wise deletion only
replaces the ambient family by a subfamily; none changes the factorization
or the unique value of `d`.  QED.
