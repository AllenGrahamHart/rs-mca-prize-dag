# `A=1` core-one distance-three boundary root-unity router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_original_lift_column_far_converse`

Retain the exact external product

```text
product_(z external)G_z(X)=C(X)^e,
P_X(X)=A(X)B(X)C(X).                                  (BRU1)
```

This identity gives constraints on the support selection and matching before
the internal slopes or fiber scalars are chosen.

For one matched pair `D_i=(X-a)(X-b)`, put

```text
U_(a,b)=B(a)(A/D_i)(a) / (B(b)(A/D_i)(b)),
zeta_(a,b)=
 -P_X'(a)/P_X'(b) / U_(a,b)^4.                       (BRU2)
```

Then

```text
zeta_(a,b)^e=1.                                       (BRU3)
```

For two distinct triple points `t,u`, put

```text
V_(t,u)=A(t)/A(u),       W_(t,u)=B'(t)/B'(u),
eta_(t,u)=
 P_X'(t)/P_X'(u) / (V_(t,u)^4 W_(t,u)).              (BRU4)
```

Then

```text
eta_(t,u)^e=1.                                        (BRU5)
```

All denominators are nonzero. On the smooth multiplicative domain of size
`N=8e+8`, with stripped core `s` and omitted row `x_0`, these derivatives
are explicit:

```text
P_X'(x)=N x^(-1)/((x-s)(x-x_0))       for x in D_res\{x_0}. (BRU6)
```

Thus `(BRU3)` gives one matching-local gate per exceptional pair and
`(BRU5)` gives two independent triple gates. They involve only
`A,B,s,x_0` and the pair partition. A candidate failing any gate is rejected
before allocating `xi_i`, `lambda_i`, external slopes, or locators.

These root-unity conditions are necessary, not sufficient for the external
split design.
