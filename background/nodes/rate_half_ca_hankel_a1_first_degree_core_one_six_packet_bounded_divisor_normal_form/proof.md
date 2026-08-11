# Proof

The packet theorem gives one distinguished heavy row `x_*`, with

```text
d_*=I_E=e-c,
I_H=d_*+I_0=Delta-u.                                  (1)
```

Its row form has degree `e` and exactly `d_*` distinct supported roots.
Their squarefree locator `P_*` therefore divides the row form, leaving the
degree-`c` factor `K_c` in `(SBN2)`.

At every distinguished incidence, the specialized excess recurrence factor
contains `x_*`, so the residual rank loss is positive. The general
middle-Hankel adjugate theorem gives

```text
ord_gamma(D)>=c_gamma>=1.                             (2)
```

The roots of `P_*` are distinct, hence `P_*|D`. Since

```text
deg D-deg P_*=Delta-d_*=c-2=u+I_0,                   (3)
```

the adjugate factorization in `(SBN2)` follows.

The Forney numerator vanishes at every distinguished heavy incidence. Thus
the squarefree `P_*` divides `N_F(U,V;x_*)`. Its parameter degree is at most
`e+1`, leaving quotient degree at most

```text
e+1-d_*=c+1.                                         (4)
```

The quotient is nonzero. If the specialization vanished identically, the
surface numerator would contain `X-x_*`. The cancelled cube identity makes
the contact section nonzero on every mixed component, so its zero divisor
would then contain the complete degree-`e` vertical fibre. This is
impossible because the contact line bundle has degree `Delta=e-2`.

We now identify the contact divisor. Every heavy incidence is a zero of the
contact section. The `d_*` distinguished points and `I_0` ordinary points
are distinct and total

```text
d_*+I_0=Delta-u.                                      (5)
```

The section is nonzero on every component and has total zero degree
`Delta`, so its remaining zero divisor is an effective `E_u` of degree
`u`. This proves `(SBN4)`.

The vertical fibre at `x_*` has degree `e` and contains every point of
`R_*` at least once. Removing the reduced divisor leaves the effective
divisor

```text
Z_c=V_(x_*)-R_*,       deg Z_c=e-d_*=c,               (6)
```

which proves `(SBN3)`. Substitute `R_*=V_(x_*)-Z_c` into `(SBN4)`. Since
the contact line bundle is `O_C(-rho-1,e+1)` and the vertical fibre has
class `O_C(1,0)`, one obtains

```text
O_C(-rho-1,e+1)
 =O_C(1,0)(-Z_c+R_0+E_u).                             (7)
```

Rearranging gives `(SBN5)`. Finally `(SBN1)` gives
`c-I_0-u=2`, and the six packet table gives `c<=6`, `u<=2`, and `I_0<=2`.
QED.
