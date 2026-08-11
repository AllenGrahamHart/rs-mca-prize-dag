# Proof

Fix `x in M_gamma`. The light row `Qbar(t;x)` has exact parameter degree
`e` and its simple roots are the supported slopes whose actual supports
contain `x`. On the center line, `x` is absent at `gamma` and present at
the other two slopes. Thus `Qbar(t;x)` is divisible by the two line factors
other than `ell_gamma`, while `(ESP7)` gives

```text
omega_x(t)=eta_x ell_gamma(t),       eta_x!=0.      (1)
```

Therefore the product in `(DSB2)` is divisible by `Lambda_A` and its
quotient has exact degree `e-2`. Its roots are exactly the `e-2` off-line
supported slopes whose supports contain `x`. This proves `(DSB5)`.

If `d_A=0`, there is one possible exceptional coordinate `x_circ`. It is
present at all three line slopes, so its light row `Qbar(t;x_circ)` is
already divisible by `Lambda_A`. Multiplication by its linear source form
and division by `Lambda_A` again gives a polynomial of degree at most
`e-2`. Thus `(DSB2)` is polynomial for every `x in U_0`.

The fixed-line contracted source representation of the Hankel pencil is

```text
M(t)_(a,b)=sum_(x in U_0)omega_x(t)x^(a+b).          (2)
```

The global locator equation `M(t)q(t)=0` gives

```text
sum_(x in U_0)omega_x(t)Qbar(t;x)x^j=0,
0<=j<=d.                                            (3)
```

Every summand in `(3)` is divisible by `Lambda_A`. Divide by that nonzero
polynomial to obtain `(DSB3)`.

The vectors on `U_0` orthogonal to the evaluation rows
`1,x,...,x^d` form the dual GRS code of dimension

```text
n_0-(d+1)=(3p-2)-2p=p-2.                            (4)
```

For every polynomial `R` of degree at most `p-3`, the vector

```text
(R(x)/L_U0'(x))_(x in U_0)                          (5)
```

lies in this dual code: multiplying by `x^j` gives degree at most

```text
(p-3)+d=3p-4=n_0-2,                                 (6)
```

and the Lagrange leading-coefficient identity makes its coordinate sum
zero. The map `(5)` is injective and both spaces have dimension `p-2`, so
it is an isomorphism.

Apply this isomorphism coefficientwise in `t` to `(DSB3)`. It produces the
unique `G` in `(DSB4)`, and its parameter degree is at most the maximum
degree `e-2` of the `H_x`. Since every `M_gamma` is nonempty, `(DSB5)`
forces equality in the parameter degree. Equation `(ESP5)` gives the row
count `(DSB6)`.

It remains to identify the clean parameter fibers. Cycle 128 gives the
lower bound `(DSB8)`. Fix `delta in Z_clean`. Then

```text
Qbar(delta;X)
 =chi_delta A_delta(X)B_delta(X),
chi_delta!=0,                                       (7)
```

because there is no padded factor; `chi_delta` records the global biform
normalization. The Forney-barycentric gate gives

```text
omega_x(delta)B_delta(x)L_U0'(x)=kappa_delta
                                      (x in X_delta). (8)
```

For `x in X_delta`, equations `(DSB2)`, `(DSB4)`, `(7)`, and `(8)` yield

```text
G(delta,x)
 =L_U0'(x)H_x(delta)
 =[chi_delta kappa_delta/Lambda_A(delta)]
    A_delta(x).                                     (9)
```

Both sides of `(9)` vanish for `x in I_delta`, so they agree at every point
of `U_0`. Their degrees are at most `p-3`, strictly smaller than `|U_0|`.
They are therefore equal as polynomials, proving `(DSB10)` with

```text
zeta_delta
 =chi_delta kappa_delta/Lambda_A(delta)!=0.         (10)
```

Since `A_delta` is monic of degree `p-3`, one clean fiber makes the
`X`-degree of `G` exact. The official substitutions in `(DSB11)` are direct.
QED.
