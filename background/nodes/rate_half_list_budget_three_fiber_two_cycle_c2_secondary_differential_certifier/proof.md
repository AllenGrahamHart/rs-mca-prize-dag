# Proof

Write

```text
A-B=z^(2H) T_hat,       T_hat(0)=c.                  (1)
```

Differentiating `EA^4=1` and substituting `(1)` gives

```text
E'B+4EB'=-z^(2H-1)S,
S=(zE'+8HE)T_hat+4zE T_hat'.                         (2)
```

The left side has degree at most `2H`, so `S` is linear. Its constant term is
`8Hc`. Put `t_1=a_(2H+1)`. The coefficient recurrence at index `2H+1`, using
the two primary zeros, is

```text
(8H+4)t_1=-(8H+1)E_1c-(8H-8)E_4b.                  (3)
```

The linear coefficient of `S` is

```text
(8H+4)t_1+(8H+1)E_1c=-8(H-1)E_4b.                  (4)
```

Equations `(2)--(4)` prove `(SDC2)`.

The two-window theorem says that its secondary condition is equivalent to a
polynomial `C` as in `(SDC3)` satisfying

```text
B T_hat=cC^2 mod z^H.                                (5)
```

Here replacing `B,T_hat` by their low windows gives exactly `(SDC5)`. Set
`W=BT_hat/c mod z^H` and define

```text
mathcalL(R)=2zER'+(zE'+4HE)R.                        (6)
```

Using `(2)` and then `(SDC2)`, a direct product-rule calculation gives

```text
mathcalL(W)
 =(S/(2c))B mod z^H
 =(4H-4(H-1)kappa z)B mod z^H.                      (7)
```

The omitted exact term is `z(E'B+4EB')T_hat/(2c)`, whose order is at least
`2H`, so it vanishes modulo `z^H`.

If `(5)` holds, substitute `W=C^2` into `(6)--(7)`. Since
`(C^2)'=2CC'`, the resulting congruence is precisely `(SDC4)`. This proves
necessity.

Conversely, suppose `(SDC3)--(SDC4)` hold and put `U=C^2-W`. Equations
`(6)--(7)` give

```text
mathcalL(U)=0 mod z^H,       U(0)=0.                 (8)
```

If all coefficients of `U` below degree `n` vanish, the coefficient of
`z^n` in `(8)` is

```text
(2n+4H)[z^n]U=0.                                    (9)
```

For `0<=n<H`, one has `2n+4H<=6H-2<8H-8` on the official row, so this scalar
is nonzero in the field. Induction in `(9)` gives `U=0 mod z^H`, which is
`(5)` and hence the secondary condition. This proves sufficiency.

Finally, `deg B<=2H-3`, `deg E=4`, and `deg C<=H-3` bound every term in
`(SDC4)` by `2H-2`. Division by `z^H` therefore leaves degree at most `H-2`.
QED.
