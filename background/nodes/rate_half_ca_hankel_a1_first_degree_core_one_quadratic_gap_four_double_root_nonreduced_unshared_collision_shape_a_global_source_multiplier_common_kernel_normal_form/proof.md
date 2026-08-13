# Proof

Normalize the three source forms in the chosen affine coordinate as

```text
omega_x(z)=eta_x(z-gamma)       (x in M_gamma).   (1)
```

Source interpolation gives

```text
B_src(z,x)=omega_x(z)L_U0'(x).                    (2)
```

Comparing the coefficient and constant term of `z` in `(GSM1)--(2)` gives

```text
J(x)=eta_xL_U0'(x),       K(x)=-gamma J(x).       (3)
```

All source scalars and locator derivatives are nonzero, so `J` is a unit
in `A`; equations `(GSM2)--(GSM4)` follow.

For `h in S_n`, the coefficient functional of the class map against
`f in W_X` is

```text
sum_(x in M_gamma)
 eta_x^(-1)f(x)h(x)/L_U0'(x)^2.                  (4)
```

Using `(3)`, this is exactly

```text
sum_(x in M_gamma)f(x)h(x)/[J(x)L_U0'(x)].       (5)
```

Let `e_gamma(T)` be the degree-two Lagrange polynomial which is one at
`gamma` and zero at the other two centers. Since
`e_gamma(varphi(x))` is the indicator of `M_gamma`, equations `(4)--(5)`
show that all three class maps vanish exactly when

```text
tau(fh e_gamma(varphi)/J)=0
                         (f in W_X, every gamma). (6)
```

The three indicator polynomials form a basis of `S_2(T)`. Thus `(6)` is
equivalent to `(GSM8)`, or intrinsically to

```text
h/J in E_3^perp.                                  (7)
```

Because `J` is a unit in `A`, equation `(7)` proves `(GSM7)`.

It remains to compute `dim E_3`. Suppose

```text
f_0+varphi f_1+varphi^2f_2=0       in A,          (8)
```

with `f_i in W_X`. On `M_gamma`, equation `(8)` says that the polynomial

```text
f_0+gamma f_1+gamma^2f_2 in S_n                  (9)
```

vanishes at `|M_gamma|>=n+2` distinct points. It is therefore the zero
polynomial. Applying this at the three distinct centers and inverting the
Vandermonde matrix gives `f_0=f_1=f_2=0`. Hence the sum in `(GSM5)` is
direct and `(GSM6)` follows.

Finally, `B_src=H B_prim` makes both parameter coefficients divisible by
`H`; after cancellation their ratio is unchanged. This proves the
primitive-pencil assertion. At `r=(e+1)/2`, direct substitution of

```text
R=3n+7,       n=(3e-7)/2                          (10)
```

gives `(GSM9)`. The preceding center residue-pairing theorem supplies the
necessary lower bound `(GSM10)`. QED.
