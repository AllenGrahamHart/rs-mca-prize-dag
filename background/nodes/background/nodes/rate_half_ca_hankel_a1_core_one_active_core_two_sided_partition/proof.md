# Proof

The exceptional-trace theorem leaves the two systems `(ETN6)`, and the
active-core theorem gives `B_X=X_0X_1` with `z=deg X_0 in {0,1}`. Since
`G_X=P_XB_X`, identity `(ATP1)` follows.

At a clean slope, both `P` and `P_cl` vanish. The second equation of either
system `(ETN6)` therefore specializes to `(ATP2)`. The component theorem says
that `Q_gamma` is squarefree of degree `r` and splits over `D\S`. The right
side is squarefree. Hence the quotient `A_a(gamma)` is squarefree, split, and
coprime to `Q_gamma`, with degree `(ATP3)`.

The original complement has exact `X`-degree `D_0-r`. Cancelling `X_0` gives
the upper bound `D_0-r-z` for `A_a`. Every clean specialization reaches that
same degree by `(ATP3)`, proving `(ATP4)`.

At a saturated row, `P_X(x)=0`, so the universal first complement
`QV_a+P_XW_a=P` specializes to `(ATP5)`. By definition of saturation,
`Q_x` has `e_*` distinct roots in the supported set. It divides the squarefree
form `P` of degree `T`, so the quotient `V_a(x)` is squarefree, split, coprime
to `Q_x`, and has degree `T-e_*`. This is the global parameter degree already
proved for `V`; no exceptional factor is cancelled because exceptional
nonvanishing is now proved. This gives `(ATP6)`.

There are `T-D_*` clean slopes and `D_0-c` saturated rows by definition. For
a bad row, write `a_x` for its clean supported roots and `epsilon_x` for its
possible exceptional root. Then

```text
delta_x=e_*-a_x-epsilon_x.                            (1)
```

Summing `(1)` over all bad rows gives

```text
sum a_x=c e_*-C_*-E_bad.                              (2)
```

A zero-trace row has no clean root, so the left side of `(2)` may be restricted
to roots of `X_1`. Substituting `e_*=e-b` and
`C_*=e-5b-1+D_*` gives `(ATP8)`. Finally an active trace has `H_x!=0`; its
bound `deg H_x<a_x` forces `a_x>=1`. QED.
