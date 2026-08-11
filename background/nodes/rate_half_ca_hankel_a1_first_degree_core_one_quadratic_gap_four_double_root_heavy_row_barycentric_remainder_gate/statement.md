# `A=1` quadratic double-root heavy-row barycentric remainder gate

- **status:** PROVED
- **closure:** exact one-polynomial test for the augmented heavy row
- **consumer:** `rate_half_band_crossing_location`

Retain the separated double-root extremal profile and the classified row set
`X` of the paired scalar-weld gate. Thus

```text
G(t,X)=sum_(r=0)^m g_r(X)t^r,
m=e-2,       deg_X g_r<=n,       x_* notin X.       (HRB1)
```

Let `P_x(t)` be the monic row-root polynomial at `x in X`, and suppose the
connected weld has rank `|X|-1`, with its unique projective full-support
kernel vector `lambda`. Assume `Krow lambda=0`, so the classified rows
reconstruct one common biform. Divisibility below is intrinsically between
binary parameter forms; for the displayed remainder matrix choose a
dehomogenizing chart whose infinity is not a root of `H`. Put

```text
L_X(Y)=product_(x in X)(Y-x),
b_x=L_X(x_*)/((x_*-x)L_X'(x)),

R_lambda(t)=sum_(x in X)b_x lambda_x P_x(t).        (HRB2)
```

For the center-overlap factorization write

```text
J=gcd(Lambda,g_*S_B^2),       j=deg J<=3,
H=g_*S_B^2/J,                 deg H=m-j.            (HRB3)
```

Then the added heavy-row coefficient-MDS condition is equivalent to

```text
H(t) divides R_lambda(t).                            (HRB4)
```

Equivalently, let `B_H` be the `(m-j) x |X|` matrix whose `x`-column is
the coefficient vector of

```text
b_x rem_H(P_x).                                     (HRB5)
```

The complete staged gate is

```text
rank W=|X|                         => excluded;
rank W=|X|-1, Krow lambda!=0       => excluded;
rank W=|X|-1, Krow lambda=0,
                B_H lambda!=0      => excluded;
B_H lambda=0                       => the unique common biform passes
                                      the augmented heavy-row gate. (HRB6)
```

When `(HRB4)` holds, the quotient has degree at most `j` automatically and
is exactly the form `T_j` of the center-overlap theorem:

```text
R_lambda=H T_j,       deg T_j<=j.                  (HRB7)
```

In the center-disjoint case `J=1`, `(HRB4)` says simply that
`R_lambda` is a possibly zero scalar multiple of `g_*S_B^2`.

## Scope

This converts the augmented coefficient-MDS matrix to one explicit
univariate remainder. It does not prove that the remainder is nonzero for
every admissible Hankel/source packet, and therefore does not exclude the
separated double-root arm. Nonreduced and supported/correction-collision
loci remain outside the inherited hypotheses.
