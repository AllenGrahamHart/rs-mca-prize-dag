# Proof

The clean fiber is squarefree, so the implicit root `y(t)` exists formally.
Differentiate `F(t,y(t))=0` twice. The first derivative is the preceding
first-jet formula, and the second gives `(QSJ1)`.

The proof of the full reciprocal square descent contains the polynomial
identity

```text
F V_vee+R_XW_vee=P_cl E Y^N_sq.                     (1)
```

Restrict `(1)` to the root curve of `F`:

```text
R_X(y(t))W_vee(t,y(t))
 =P_cl(t)E(t)y(t)^N_sq.                             (2)
```

At `t=gamma`, both `R_X(y)` and `P_cl(gamma)` vanish. Differentiate `(2)`
twice and evaluate there. The terms multiplied by either vanishing factor
drop out, leaving exactly `(QSJ2)`. The first-jet theorem proves that
`R_X'(y)`, `dot y`, and the field scalar `2` are nonzero, so `(QSJ2)`
determines `dot W`. Equation `(QSJ3)` then determines the partial derivative
`W_vee,t(gamma,y)`, because `w_gamma` gives `W_vee,Y(gamma,y)`.

There are `r` distinct selected roots and `deg_Y W_vee,t<=r-1`. Lagrange
interpolation therefore gives the unique `j_gamma=W_vee,t(gamma,Y)`.
Differentiate the proved interpolation normal form

```text
W_vee=W_0+P_cl(t)(t A_W+B_W)
```

with respect to `t` and specialize at a root `gamma` of `P_cl`. This gives

```text
j_gamma=W_0,t(gamma,Y)+P_cl'(gamma)(gamma A_W+B_W),
```

which is `(QSJ4)--(QSJ5)`. The clean-slope locator is squarefree, so its
derivative is nonzero. Solving the two-by-two system at distinct
`alpha,beta` proves `(QSJ6)`. Uniqueness in the unit-remainder theorem forces
the two independently reconstructed correction pairs to agree. QED.
