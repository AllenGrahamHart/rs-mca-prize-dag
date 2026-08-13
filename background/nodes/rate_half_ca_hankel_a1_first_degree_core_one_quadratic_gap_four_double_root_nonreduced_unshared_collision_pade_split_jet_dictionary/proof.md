# Proof

Differentiate the defining divided difference of the Pade numerator:

```text
P_F(t,X)=Phi_t((Q(t,X)-Q(t,Z))/(X-Z)).             (1)
```

At `X=x_*`, the derivative of the inner quotient is exactly `W(t,Z)`.
This proves `(PSD4)`. At `tau`, both the value and first `X`-derivative of
`Q` vanish, so `(PSD1)` gives `(PSD2)`.

Write `P_F=b+ay+qR`. Differentiating at `y=0` gives

```text
A=a+c_1R(z,0)+c_0R_y(z,0).                        (2)
```

The contact-algebra router gives `ord c_1>=3` and `ord c_0=6`, hence
`A=a mod z^3`. This proves `(PSD5)`.

Let

```text
F_i=Phi_t(X^iU),       U_*=U(t,x_*)=Q_X(t,x_*).   (3)
```

The identity `U=U_*+(X-x_*)W` gives

```text
F_i=U_*h_i+E_(i+1)-x_*E_i.                        (4)
```

The nonreduced two-jet gate says `ord F_i>=2`. The local quadratic form
gives `ord U_*>=3`: its leading terms are `c_1` times a unit and `c_0`
times a regular derivative. Taking coefficients of orders zero and one in
`(4)`, starting with `E_0=A`, proves `(PSD6)`.

If `lambda_0=0`, equation `(PSD6)` says every entry of the specialized
moment image of `W_tau` vanishes. Differentiate the self-pairing
`Phi_t(W(t)^2)`. Terms containing `M(tau)W_tau` vanish, and the remaining
term is the coefficient vector of `W_tau` paired with `[z](E_i)_i`.
Using `(PSD6)` evaluates it as

```text
lambda_1 W_tau(x_*),                              (5)
```

which is `(PSD7)`.

Finally differentiate the Pade syzygy

```text
QB-Lambda G=LP_F                                  (6)
```

in `X` and set `X=x_*`:

```text
U_*B_*+Q_*B_X-Lambda G_X=L'F_0+LA.                (7)
```

At `tau`, the first three terms other than `G_X,A` have orders at least
three, six, and two respectively. Also `Lambda(tau)L(x_*)!=0`. Indeed
`x_*` lies outside `U_0`, so `L(x_*)!=0`. If the correction `tau` were an
assigned center, then `Q(tau,x_*)=0` would make the outside point `x_*` a
padded locator root at that center. The three-center source partition
identifies such a center as a root of `g_*`, contrary to unsharedness. The
constant coefficient of `(7)` gives `(PSD8)`. If
`lambda_0=0`, then `G_X(tau,x_*)=0`; the order-one coefficient gives
`(PSD9)` without a derivative-of-`Lambda` term. Combining these formulas
with the proved contact-algebra trichotomy gives `(PSD10)`. QED.
