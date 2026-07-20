# `A=1` distance-three matching-free boundary-power router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_boundary_root_unity_router`

Retain the distance-three support packet. For every exceptional root
`a in R_A` and triple point `t in T`, define

```text
K_A(a)=P_X'(a)/(B(a)^4 A'(a)^4),
K_B(t)=P_X'(t)/(A(t)^4 B'(t)),                        (MBP1)

Y_a=K_A(a)^e,       Z_t=K_B(t)^e.                    (MBP2)
```

All values are nonzero. If `D_i=(X-a)(X-b)` is a matched exceptional pair,
then its boundary root-unity gate is exactly

```text
Y_a=-Y_b.                                             (MBP3)
```

The two independent triple gates are exactly

```text
Z_t=Z_u       for every t,u in T.                    (MBP4)
```

Consequently, before choosing a matching, define the monic value polynomial

```text
M_A(Y)=product_(a in R_A)(Y-Y_a).                    (MBP5)
```

There exists a perfect matching passing every pair gate if and only if

```text
M_A(-Y)=M_A(Y).                                       (MBP6)
```

Equivalently, the multiset `{Y_a:a in R_A}` is centrally symmetric, and all
odd coefficients of `M_A` vanish. A passing matching is reconstructed by
pairing each occurrence of `y` with one occurrence of `-y`. In particular,

```text
sum_(a in R_A) K_A(a)^(e m)=0       for every odd m. (MBP7)
```

This router removes the matching from the boundary-power decision and
replaces `e` pairwise tests by one evenness test plus the equality test on
the three `Z_t`. It does not impose the dual `r`-th-power residues or prove
the external split design.
