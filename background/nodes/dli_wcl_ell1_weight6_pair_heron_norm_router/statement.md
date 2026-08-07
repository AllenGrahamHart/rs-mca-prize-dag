# WCL `(1,6)` pair-Heron norm router

- **status:** PROVED
- **closure:** proof
- **dependency:** `dli_wcl_ell1_weight6_unsigned_sign_product_router`
- **consumer:** `dli_wcl_slot_1_6_emptiness`

Pair the six chosen square roots as `(r_1,r_2)`, `(r_3,r_4)`,
`(r_5,r_6)`. Put `y_i=r_i^2`, `t_j=r_(2j-1)r_(2j)`, and

```text
U_j(+/-)=y_(2j-1)+y_(2j) +/- 2t_j,
H(U,V,W)=U^2+V^2+W^2-2UV-2UW-2VW.             (PH1)
```

For every choice `tau=(tau_1,tau_2,tau_3) in {+1,-1}^3`, define

```text
H_tau=H(U_1(tau_1),U_2(tau_2),U_3(tau_3)).     (PH2)
```

Then the unsigned sign product satisfies the exact identity

```text
Psi_6(y_1,...,y_6)=product_(tau in {+1,-1}^3) H_tau.     (PH3)
```

Equivalently, over

```text
R=Z[y_1,...,y_6],
L=R[t_1,t_2,t_3]/(t_j^2-y_(2j-1)y_(2j)),
```

`Psi_6` is the three-quadratic norm of the six-term polynomial
`H(U_1(+),U_2(+),U_3(+))` from `L` to `R`.

In odd characteristic, `H_tau=0` if and only if one of the four signed sums
with the three prescribed internal pair signs vanishes. Thus the eight
Heron factors partition all 32 global-sign classes exactly and have the same
union of supporting rational primes as `Psi_6`. The identity holds for each
of the 15 pairings of six labels.

This is a factor router, not an exclusion. It replaces one opaque 32-factor
aggregate by eight explicit six-term factors before rational norm arithmetic;
no factor has yet been controlled at the official gate.
