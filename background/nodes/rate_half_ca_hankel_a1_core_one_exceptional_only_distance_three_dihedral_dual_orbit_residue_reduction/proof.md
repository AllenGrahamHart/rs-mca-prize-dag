# Proof

The dual row-product theorem gives

```text
R_i=-P_T/(C(a_i)C(b_i)),                             (1)
C(a)=P_X'(a)/(A'(a)B(a)),
P_X'(a)=N a^(-1)/((a-s)(a-x_0)).                    (2)
```

All denominators below are nonzero by disjointness of the support classes.

## 1. Antipodal pairs

Let `b=-a`, `u=a^2`, and `A(X)=E(X^2)`. Directly from `(2)`,

```text
P_X'(a)P_X'(-a)
 =-N^2 a^(-2)/((u-s^2)(u-x_0^2)),                  (3)
A'(a)A'(-a)=-4u E'(u)^2,                            (4)
B(a)B(-a)=-product_(t in T)(u-t^2).                 (5)
```

Substituting `(3)--(5)` into `(1)` gives

```text
R_i=(4P_T/N^2)
    u^2(u-s^2)(u-x_0^2) product_t(u-t^2) E'(u)^2,
```

which is `(DOR1)--(DOR2)`.

## 2. Constant-product pairs

Let `b=c/a`, `u=a+b`, and

```text
A(X)=X^e E(X+c/X).
```

At a root of `A`, differentiation gives

```text
A'(a)A'(b)=-c^(e-1)(u^2-4c)E'(u)^2.                (6)
```

The boundary derivative and triple factors satisfy

```text
P_X'(a)P_X'(b)
 =N^2/[c(c+s^2-su)(c+x_0^2-x_0u)],                 (7)
B(a)B(b)=product_(t in T)(c+t^2-tu).                (8)
```

Substitution of `(6)--(8)` into `(1)` gives

```text
R_i=(c^eP_T/N^2)(u^2-4c)
    (c+s^2-su)(c+x_0^2-x_0u)
    product_t(c+t^2-tu) E'(u)^2,
```

which proves `(DOR3)` and the common formula `(DOR2)`.

## 3. Split-algebra form

The orbit roots `u_i` are distinct, so evaluation gives

```text
F_p[U]/(E) isomorphic to product_i F_p.
```

The condition `R_i in (F_p^*)^r` says that one may choose `y_i` with
`y_i^r=kappa W(u_i)E'(u_i)^2`. There is a unique polynomial `Y` of degree
less than `e` interpolating the `y_i`. Coordinatewise evaluation proves
`(DOR4)`, and the converse follows by evaluating `(DOR4)` at every `u_i`.

Finally multiply `(DOR2)` over all roots of `E`. Since

```text
product_i W(u_i)=Res(E,W),
product_i E'(u_i)=(-1)^(e(e-1)/2) Disc(E),
```

the product of the `R_i` is the left side of `(DOR5)`. A product of
`r`th powers is an `r`th power, proving `(DOR5)`. QED.
