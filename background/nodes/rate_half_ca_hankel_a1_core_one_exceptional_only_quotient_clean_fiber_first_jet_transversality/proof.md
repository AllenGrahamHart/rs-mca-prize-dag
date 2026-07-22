# Proof

Differentiate the first identity in `(QJT1)` with respect to the parameter
`t`. At `(gamma,y)`, both `P_cl(gamma)` and `F(gamma,y)` vanish, leaving

```text
F_t(gamma,y)U(gamma,y)+P_cl'(gamma)L(gamma,y)=0.
```

Evaluating the second identity in `(QJT1)` at the same point removes its
`FS` term and gives `(QJT3)`. Multiplication proves `(QJT4)`.

The clean-slope polynomial `P_cl` is squarefree and is coprime to the
exceptional factor `E`, so `P_cl'(gamma)` and `E(gamma)` are nonzero. The
domain is multiplicative, hence `y` is nonzero. Two-sided saturation makes
`F(gamma,Y)` a squarefree divisor of the squarefree locator `R_X`, with
coprime complement `U(gamma,Y)`. Therefore `U(gamma,y)` is nonzero. Equation
`(QJT4)` now forces `F_t(gamma,y)` and `W_vee(gamma,y)` to be nonzero as
well.

Finally, differentiate

```text
R_X=F(gamma,Y)U(gamma,Y)
```

in `Y` and evaluate at `y` to obtain
`R_X'(y)=F_Y(gamma,y)U(gamma,y)`. The implicit-function velocity is
`dot y=-F_t/F_Y`. Substitute this derivative identity into `(QJT4)` and
divide by the proved nonzero factors to obtain `(QJT5)`.

For the official specialization, the active-core partition removes the core
point `s` and the one zero-trace row `x_0` from the order-`M` multiplicative
domain. Before reversal its locator is

```text
P_X(X)=(X^M-1)/((X-s)(X-x_0)).
```

Reversing at degree `M-2` gives `(QJT6)`. At any remaining domain root `y`,

```text
R_X'(y)=-M y^(-1)/((1-sy)(1-x_0y)).
```

Here `M` is invertible because `M` divides `|F|-1`. Since
`n_X=M-2`, the square exponent is `N_sq=M+r-3`; hence
`y^(N_sq+1)=y^(r-2)`. Substitute these identities into `(QJT5)` to obtain
`(QJT7)`. QED.
