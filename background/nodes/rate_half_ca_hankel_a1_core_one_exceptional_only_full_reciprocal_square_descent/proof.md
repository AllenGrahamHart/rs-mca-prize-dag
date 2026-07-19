# Proof

Reverse the corrected unit equation

```text
WB_1-1=QK_1                                           (1)
```

at the common fixed degree

```text
(r-1)+D_0=r+n_X.
```

Using `F,G,W_vee,K_vee` gives

```text
W_vee G-FK_vee=Y^(r+n_X).                           (2)
```

The reciprocal-resultant descent says `EG=YL-j_infF`. Multiply `(2)` by
`E` and substitute:

```text
Y L W_vee-F(j_infW_vee+EK_vee)=E Y^(r+n_X).         (3)
```

The infinity chain is

```text
W_vee(0)=-E q_bar v_inf,
K_vee(0)= j_inf q_bar v_inf.                        (4)
```

Thus the parenthesized polynomial in `(3)` has zero constant term and
`(FRS2)` defines a polynomial `S`. Substitute it in `(3)` and cancel `Y`:

```text
L W_vee-FS=E Y^(r+n_X-1)=E Y^N,                    (5)
```

which is `(FRS3)`.

Now reverse the inherited first complement

```text
QV+P_XW=P_clE                                       (6)
```

at degree `r+n_X-1=N`. This gives

```text
F V_vee+R_XW_vee=P_clE Y^N.                        (7)
```

Insert `R_X=FU+P_clL` from `(FRC3)` and
`LW_vee=FS+EY^N` from `(5)`:

```text
F(V_vee+UW_vee)+P_clLW_vee
 =F(V_vee+UW_vee+P_clS)+P_clEY^N
 =P_clEY^N.
```

The polynomial ring is a domain and `F!=0`, so cancellation proves
`(FRS4)`.

Equations `(FRS5)` are rearrangements of `(FRC3)`, the definition of `L`,
`(FRS2)`, and `(FRS4)`. Conversely, when all three displayed divisions are
exact and the fixed degree boxes hold, substituting the recovered forms
reverses the calculations and gives the unit equation and first complement.
The second complement follows from those identities and the corrected first
complement exactly as in the proof of `(EFD6)`; no independent search block
is needed for it. Hankel and splitting constraints were not used. QED.
