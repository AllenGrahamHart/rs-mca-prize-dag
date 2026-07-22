# Proof

The pair-Lagrange formula writes `Q` as

```text
Q(z;X)=Phi(z)U_0(X)+sum_i c_i zL_i(z)U_i(X),          (1)
```

where every `c_i` is nonzero. The parameter polynomials

```text
Phi, zL_1,...,zL_e
```

are a basis of the polynomials of degree at most `e`. Hence an invertible
change of parameter-coefficient coordinates identifies the coefficient
space of `Q` with `V` in `(QLR1)`.

We first bound `V V`. The squares `U_0^2,U_i^2` and the products `U_0U_i`
already belong to the span

```text
S=span({U_0^2} union
       {U_0U_i, X U_0U_i, U_i^2:1<=i<=e}).           (2)
```

For `i!=j`, the monic quadratics `D_i,D_j` are coprime. The linear map

```text
F[X]_(<=1) x F[X]_(<=1) -> F[X]_(<=3),
(u,v) |-> uD_j+vD_i                                  (3)
```

is injective: a kernel relation would make `D_i` divide a polynomial of
degree at most one. Both sides of `(3)` have dimension four, so the map is
an isomorphism. Since `deg B=3`, there are linear polynomials `u_ij,v_ij`
with

```text
B=u_ij D_j+v_ij D_i.                                 (4)
```

Using `U_i=BA/D_i`, equation `(4)` gives

```text
U_iU_j=u_ij U_0U_i+v_ij U_0U_j.                     (5)
```

Thus every quadratic product of elements of `V` lies in `S`. The displayed
spanning family in `(2)` has `1+3e` elements, proving `(QLR2)`.

Now fix an active outside row `x`. Exact row degree and squarefreeness give
a nonzero scalar `a_x` such that

```text
Q(z;x)=a_x G_x(z).                                   (6)
```

An invertible linear change on the `e+1` coefficient coordinates induces an
invertible linear change on their quadratic monomials. Scaling one row by
`a_x^2` also leaves matrix rank unchanged. Therefore the rank of `M_2` is
the rank of the evaluations at the active rows of the products of two
coefficient polynomials of `Q`. Those products span `V V`, so `(QLR2)` gives
`rank M_2<=3e+1`.

There are `6e+3` active rows, which gives row nullity at least `3e+2`. The
space of quadrics in `e+1` coefficient variables has dimension
`binom(e+2,2)`; subtracting the rank bound gives `(QLR5)`. QED.
