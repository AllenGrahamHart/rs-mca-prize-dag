# Proof

Write

```text
q_r=[X^r]Q=E q_bar,          q_(r-1)=[X^(r-1)]Q,
a_top=[X^(D_0-r)]A_1=P_cl j_inf,
b_(D_0-1)=[X^(D_0-1)]B_1.                           (1)
```

The corrected complement identity is

```text
Q A_1+P_cl E B_1=P_X.                               (2)
```

The two products on the left have `X`-degree at most `D_0`, while `P_X` is
monic of degree `D_0-1`. Their `X^D_0` cancellation is the already proved
infinity identity `[X^D_0]B_1=-j_inf q_bar`.

Compare the next coefficient, at `X^(D_0-1)`. Since the coefficient of this
power in `P_X` is one, `(2)` gives

```text
q_r a_minus+q_(r-1)a_top+P_cl E b_(D_0-1)=1.        (3)
```

Insert `q_r=E q_bar`, `a_top=P_clj_inf`, and

```text
Delta_inf=j_inf q_(r-1)+E b_(D_0-1).
```

Equation `(3)` becomes exactly `(RBN2)`.

Any common irreducible factor of `P_cl` and `E q_bar` would divide the left
side of `(RBN2)` and hence divide one, proving the first coprimality in
`(RBN3)`. The same argument with `Delta_inf` in place of `P_cl` proves the
second. Finally, specialize `(RBN2)` at any root `tau` of `E q_bar`:

```text
P_cl(tau)Delta_inf(tau)=1.
```

Both factors are nonzero, and `(RBN4)` follows. QED.
