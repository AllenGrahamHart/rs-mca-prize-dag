# Proof

The exceptional-only descent gives

```text
deg_X A=D_0-r-1,       deg_X J=D_0-r,
A_1=A+P_clJ.                                          (1)
```

Hence `j_inf!=0`, and the coefficient of `X^(D_0-r)` in `A_1` is exactly
`P_cl j_inf`. Since `P_cl` has parameter degree `T-1`, this also proves both
degree assertions for `A_1` in `(EIR4)`.

The exceptional specialization `Q(gamma_0;X)` has degree `r-1`, while `Q`
has global `X`-degree `r`. Therefore its leading coefficient `q_inf`
vanishes on the linear form `E` but is not the zero form. This proves the
factorization `(EIR2)`. The parameter degree of `Q` is exactly `e`, so
`q_bar` is a nonzero form of degree `e-1`.

The corrected second complement is

```text
QA_1+PB_1=P_X,       P=P_clE.                        (2)
```

Its first product has `X`-degree at most `D_0`; the right side has degree
`D_0-1`. Thus `deg_X B_1<=D_0`, and comparison at `X^D_0` gives

```text
q_inf P_cl j_inf+P_cl E b_inf=0.
```

Cancel `P_clE` after substituting `q_inf=Eq_bar`:

```text
b_inf=-j_inf q_bar.                                  (3)
```

Both factors on the right are nonzero. Hence `deg_X B_1=D_0`. Moreover the
descent writes `B_1=(B-QJ)/E`; the numerator has parameter degree at most
`e`, so `deg_parameter B_1<=e-1`. Equation `(3)` contains the nonzero
degree-`e-1` form `q_bar`, proving equality in `(EIR4)`.

The first corrected complement retains the inherited bounds

```text
QV+P_XW=P,       deg_X V<=D_0-2,       deg_X W<=r-1. (4)
```

Since `P_X` is monic, comparison at `X^(D_0+r-2)` in `(4)` gives

```text
q_inf v_inf+w_inf=0,
w_inf=-E q_bar v_inf.                                (5)
```

Finally `WB_1-1=QK_1` gives `deg_X K_1<=D_0-1`. Compare its coefficient at
`X^(D_0+r-1)` and apply `(3),(5)`:

```text
w_inf b_inf=q_inf k_inf,
E j_inf q_bar^2v_inf=E q_bar k_inf.
```

The polynomial ring is a domain and `E q_bar!=0`, so cancellation gives

```text
k_inf=j_inf q_bar v_inf.
```

This completes `(EIR3)`. The calculation permits `v_inf=0`; no unsupported
degree equality for `V`, `W`, or `K_1` has been introduced. QED.
