# Proof - L1 Mersenne HNF order-one Newton reciprocal reduction

Put

```text
y_i=x_i^m,       y_i^star=(x_i^star)^m.
```

Write `e_j` for the `j`th elementary symmetric function. The reduced
resultants are monic and have coefficients

```text
q_j=(-1)^j e_j(y_1,...,y_H),
q_j^star=(-1)^j e_j(y_1^star,...,y_H^star),
Ctilde=q_H=(-1)^H e_H(y).                            (1)
```

The coefficient of `Z^(H-j)` in
`Z^H Qtilde_(rho,c)(1/Z)` is `q_(H-j)`. Since

```text
e_(H-j)(y)=e_H(y)e_j(y_1^(-1),...,y_H^(-1)),         (2)
```

the equation `Ctilde*q_j^star=q_(H-j)` is, after cancelling the nonzero
`e_H(y)`, exactly

```text
e_j(y^star)=e_j(y^(-1)).                             (3)
```

The signs agree because the two exponents `H+j` and `H-j` differ by `2j`.
Equation (3) is (NRR3).

Newton's identities express each `e_j` from the first `j` power sums by
(NRR2). Here those power sums are precisely (NRR1). All integers through
`H` are invertible on the official rows because `H<h<p`. The negative power
sums are ordinary positive power sums of the inverse roots; these are the
roots of the monic reciprocal polynomial

```text
W^H L_(rho,c)(1/W)/L_(rho,c)(0).
```

Thus the first three equations require traces only through the powers in
(NRR4), and all equations remain bounded in the fixed degrees `m,h`.

For `j=H`, (3) says `e_H(y^star)=e_H(y)^(-1)`, which is exactly
`Ctilde*Ctilde_star=1`. Hence the equations for `1<=j<H` plus this endpoint
equation are equivalent to the reduced reciprocal identity. QED.
