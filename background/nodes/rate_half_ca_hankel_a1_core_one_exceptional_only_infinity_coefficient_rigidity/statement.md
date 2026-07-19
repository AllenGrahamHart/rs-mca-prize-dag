# `A=1` core-one exceptional-only infinity-coefficient rigidity

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_factor_descent`

Retain the exceptional-only corrected square `(EFD5)--(EFD7)`. Define its
leading `X`-coefficients by

```text
q_inf=[X^r]Q,                  j_inf=[X^(D_0-r)]J,
v_inf=[X^(D_0-2)]V,           w_inf=[X^(r-1)]W,
b_inf=[X^D_0]B_1,             k_inf=[X^(D_0-1)]K_1.  (EIR1)
```

Then `j_inf!=0`, and the exceptional degree drop gives a nonzero form
`q_bar` such that

```text
q_inf=E q_bar.                                      (EIR2)
```

The complete leading-coefficient chain is

```text
[X^(D_0-r)]A_1=P_cl j_inf,
b_inf=-j_inf q_bar,
w_inf=-E q_bar v_inf,
k_inf= j_inf q_bar v_inf.                           (EIR3)
```

Consequently

```text
deg_X A_1=D_0-r,       deg_parameter A_1=T-1,
deg_X B_1=D_0,         deg_parameter B_1=e-1.       (EIR4)
```

Thus the corrected square saturates both opposite bidegree corners. The
leading coefficients of `B_1,W,K_1` are not elimination variables once
`q_bar,j_inf,v_inf` are fixed. In particular, truncating `B_1` at
`X`-degree `D_0-1` deletes every valid exceptional-only packet.

No nonvanishing of `v_inf` is claimed. If it vanishes, `(EIR3)` forces the
corresponding top coefficients of `W` and `K_1` to vanish as well. This
theorem does not classify the corrected square or close the profile.
