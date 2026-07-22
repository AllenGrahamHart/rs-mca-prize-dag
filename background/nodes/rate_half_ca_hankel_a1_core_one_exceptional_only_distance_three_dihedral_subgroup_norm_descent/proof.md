# Proof

## 1. Antipodal descent

Put `U=X^2`. The pair-Lagrange form and `(DSN2)` give

```text
Q(z;X)=Phi(z)E(U)+zB(X)J(z;U).                      (1)
```

Splitting `B` into its even and odd parts turns `(1)` into

```text
Q(z;X)=P(z;U)+X S(z;U),                             (2)
```

with `P,S` as in `(DSN3)`. Hence

```text
Q(z;X)Q(z;-X)=P(z;U)^2-U S(z;U)^2=V_-(z;U).        (3)
```

Negation acts freely on `mu_N`, and its orbit coordinates are exactly
`mu_(N/2)`. Taking the product of `(3)` over the `N/2` orbits gives

```text
product_(x in mu_N)Q(z;x)
 =product_(u in mu_(N/2))V_-(z;u),
```

which is `(DSN4)` by the root-product definition of the resultant. The
degree bounds in `(DSN3)` give `deg_U V_-<=2e+1`.

## 2. Constant-product descent

For an orbit `{x,c/x}` put `U=x+c/x`. Since

```text
A(X)=X^eE(X+c/X),
A(X)/D_i(X)=X^(e-1)E(U)/(U-u_i),
```

the pair-Lagrange form becomes

```text
Q(z;X)=X^(e-1)[X Phi(z)E(U)+zB(X)J(z;U)].           (4)
```

The elementary symmetric calculations

```text
B(x)B(c/x)=L_c(U),                                  (5)
xB(c/x)+(c/x)B(x)=K_c(U)                            (6)
```

follow by expanding the monic cubic `B`. Multiplying `(4)` at `x` and
`c/x`, then using `(5)--(6)`, gives exactly

```text
Q(z;x)Q(z;c/x)=V_c(z;U).                            (7)
```

The three terms in `(DSN5)` have `U`-degrees at most `2e`, `2e+1`, and
`2e+1`, respectively.

The defining Dickson recurrence gives the standard identity

```text
D_N(x+c/x,c)=x^N+(c/x)^N.                           (8)
```

Here `x in mu_N` and `c in mu_N`, so `c^N=1`. Therefore

```text
D_N(x+c/x,c)-2=(x^N-1)^2/x^N.                      (9)
```

Every nonfixed orbit contributes one double root to the left side of `(9)`.
At a fixed point `w^2=c`, the quotient map is ramified and contributes the
single root `U=2w`. Both sides of `(DSN7)` are monic of degree `N`, so their
root multiplicities prove `(DSN7)`.

Finally partition `mu_N` into its fixed points and nonfixed two-element
orbits. Multiply `(7)` over the nonfixed orbits and retain the single factor
`Q(z;w)` at each fixed point. The root-product definition of the resultant
then gives `(DSN8)`.

## 3. Split-slope equivalence

In the antipodal branch, `(3)` is the polynomial identity

```text
Q(z;X)Q(z;-X)=V_-(z;X^2).                           (10)
```

If `Q` splits over `mu_N`, the right side splits over `mu_(N/2)`. Conversely,
if the right side splits over that quotient subgroup, the product on the
left splits over `mu_N`. Every irreducible factor of `Q(z;X)` divides this
split product, hence is linear with a root in `mu_N`.

In the constant-product branch, `(7)` is the Laurent identity

```text
Q(z;X)Q(z;c/X)=V_c(z;X+c/X).                        (11)
```

Multiply `(11)` by `X^r`. Exact degree and a nonzero constant term make both
sides degree-`2r` polynomials with nonzero leading coefficient. A quotient
factor `U-u` pulls back to

```text
X^2-uX+c,
```

whose roots are the orbit represented by `u`. Therefore splitting of `V_c`
over the printed quotient set is equivalent to splitting of
`X^rQ(z;X)Q(z;c/X)` over `mu_N`. Every irreducible factor of `Q` then splits
there, and the converse follows directly from `(11)`. This proves `(DSN9)`.
QED.
