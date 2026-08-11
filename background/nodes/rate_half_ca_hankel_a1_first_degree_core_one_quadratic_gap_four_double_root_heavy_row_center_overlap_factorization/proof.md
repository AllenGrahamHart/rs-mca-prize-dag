# Proof

The separated heavy-quotient theorem gives

```text
Lambda G(t,x_*)
 =g_*S_B^2 T_3,                                     (1)

T_3=a_QS_BB(t,x_*)-a_D L_U0(x_*)C_0(t),
deg T_3<=3.                                         (2)
```

Use `(HRA2)` in `(1)` and cancel `J`:

```text
Lambda_0 G(t,x_*)=H T_3.                            (3)
```

By the definition of `J`, `gcd(Lambda_0,H)=1`. Therefore
`Lambda_0|T_3`; write `T_3=Lambda_0T_j`. Since

```text
deg Lambda_0=3-j,       deg T_3<=3,                 (4)
```

one has `deg T_j<=j`. Substitute into `(2),(3)` to obtain
`(HRA3),(HRA4)`. If `J=1`, then `deg Lambda_0=3`, so `T_j` is a scalar;
this is `(HRA5)`.

Finally each coefficient polynomial `g_r(X)` in `(HRA6)` has degree at
most `n`. Its evaluation on any set of distinct field points therefore
belongs to the Reed--Solomon evaluation code of dimension `n+1` on that
set. Equation `(HRA4)` supplies the added coordinate `(HRA8)`. This proves
`(HRA7)` and the augmented gate. QED.
