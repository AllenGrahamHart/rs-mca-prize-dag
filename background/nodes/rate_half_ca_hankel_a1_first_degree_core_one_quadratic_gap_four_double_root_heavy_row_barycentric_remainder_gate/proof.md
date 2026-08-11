# Proof

Expand each monic row polynomial as

```text
P_x(t)=sum_(r=0)^m p_(r,x)t^r.                     (1)
```

The equation `Krow lambda=0` says, coefficient by coefficient, that

```text
(lambda_x p_(r,x))_(x in X) in RS[F,X,n+1].        (2)
```

Let `g_r(Y)` be the unique polynomial of degree at most `n` with these
values. Since `|X|>n`, the full-set Lagrange interpolation formula gives

```text
g_r(x_*)
 =sum_(x in X)
   L_X(x_*) lambda_x p_(r,x)/((x_*-x)L_X'(x)).     (3)
```

Summing `(3)` against `t^r` proves

```text
G(t,x_*)=R_lambda(t).                              (4)
```

The center-overlap theorem says that the required heavy row has the form

```text
G(t,x_*)=H(t)T_j(t),       deg T_j<=j.             (5)
```

Equations `(4),(5)` prove necessity of `(HRB4)`. Conversely, if `H` divides
`R_lambda`, then

```text
deg(R_lambda/H)<=m-(m-j)=j.                        (6)
```

Taking `T_j=R_lambda/H` in `(5)` shows that the biform reconstructed from
the classified rows has exactly an allowed heavy row. This proves the
equivalence.

Polynomial remainder is linear. Therefore

```text
rem_H(R_lambda)
 =sum_(x in X)lambda_x b_x rem_H(P_x),             (7)
```

which is exactly `B_H lambda`. Since `deg rem_H<m-j`, the matrix has
`m-j` coefficient rows, and `(HRB4)` is equivalent to its vanishing. The
binary-form divisibility is coordinate invariant, and an infinity outside
the finite root set of `H` makes this affine remainder test degree exact. The
first two stages of `(HRB6)` are the connected-weld and coefficient-MDS
gates; `(7)` proves the third. The center-disjoint specialization has
`j=0`, so `(6)` makes the quotient a scalar. QED.
