# Proof

Choose one circuit `S` inside the relation class and consider its
`2(t+1)`-column matrix over `F[U]`. Its entries have `U`-degree zero in the
first block and at most two in the second block. If its rank over `F(U)` is
`r`, choose `r` pivot rows and columns and one free column. Cramer's rule
gives a nonzero kernel vector whose entries are minors. Every minor uses at
most `t+1` columns from the quadratic block, so all entries have `U`-degree
at most

```text
D=2(t+1).                                           (1)
```

The rank choice makes this vector a kernel on the whole circuit. By the
uniqueness of the primitive rational relation, after clearing denominators
and removing the common factor it represents the class relation on all of
`H_[A:B]`, with

```text
deg_U A,deg_U B<=D,       deg_Z A,deg_Z B<=t.       (2)
```

Suppose `B` depends on `U`. Choose `A,B` coprime in `F[U,Z]`. Their
`U`-resultant is nonzero and has `Z`-degree at most

```text
deg_Z Res_U(A,B)
 <=deg_U(A)deg_Z(B)+deg_U(B)deg_Z(A)
 <=2Dt=4t(t+1).                                     (3)
```

For every class point `gamma`, the relation says

```text
A(U,gamma)=-B(U,gamma)q_gamma(U).                   (4)
```

If `B(U,gamma)` is nonconstant, the two specialized polynomials in `U`
have a nonconstant gcd, so `gamma` is a root of the resultant. Thus outside
at most `4t(t+1)` class points, `B(U,gamma)` is constant in `U`.

Under `(QPSD1)` there are more than `t` such points. Every positive-
`U`-degree coefficient of `B` is a polynomial in `Z` of degree at most `t`
which vanishes at all of them. Hence all those coefficients are zero and
`B=B(Z)`.

Now `(4)` and the fact that every `q_gamma(U)` is quadratic show that each
coefficient of `A` above `U`-degree two vanishes at every class point. The
class has more than `t` points, so these degree-at-most-`t` polynomials in
`Z` vanish identically. This proves `(QPSD2)`.

Multiplying the relation by `I(gamma)` and comparing the three coefficients
of `U` proves that every class point is a common root of `(QPSD3)`. The class
roots are distinct external slopes, so `P_H` divides `P_Z` and all three
residuals. Finally

```text
4*6*7+6=174,       4*8*9+8=296,
```

and the relation-class dependency supplies `(QPSD4)--(QPSD5)`. QED.
