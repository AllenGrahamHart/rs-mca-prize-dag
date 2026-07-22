# `A=1` distance-three quartic boundary CRT reconstruction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_cleared_lift_quartic_router`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_sparse_subgroup_norm_router`

Retain the exact distance-three design and all notation of the cleared-lift
quartic router. Work in

```text
R_A=F[X]/(A).
```

The pair locators are pairwise coprime and have product `A`, so there is a
unique CRT class `delta in R_A` satisfying

```text
delta=xi_i mod D_i                    (1<=i<=e).       (QBC1)
```

Put

```text
S(z;X)=sum_i D_i(X)N_i(X)L_i(z).                       (QBC2)
```

Then `z-delta` divides `S` in `R_A[z]`. Write its unique quotient as

```text
V_A(z;X)=S(z;X)/(z-delta),       deg_z V_A<=e-2.       (QBC3)
```

Let `rem_A` denote the coefficientwise canonical remainder in `X` modulo
the monic polynomial `A`. The global quartic is reconstructed from the
exceptional boundary alone by

```text
Omega_A(z;X)=rem_A(
  N^(-1) X(X-s)(X-x_0) A'(X)B(X)q_e(X)^2 V_A(z;X)
),                                                       (QBC4)

deg_X Omega_A<=4,       deg_z Omega_A<=e-2,              (QBC5)
Omega_A=Omega.                                            (QBC6)
```

Here `N` is the smooth-domain order and is nonzero in the official prime
field. Equivalently, before accepting a candidate external design, compute
the canonical remainder in `(QBC4)`: every coefficient of `X^j` for
`5<=j<2e` must vanish. This is an exact rejection gate, not a rank
diagnostic.

At a root `a` of `D_k`, the same reconstruction has the pointwise form

```text
Omega(z;a)=
 q_e(a)^2/C(a) *
 [sum_i D_i(a)N_i(a)L_i(z)]/(z-xi_k).                 (QBC7)
```

Thus any six distinct exceptional roots `Y` obey the vector-valued fifth
divided-difference identity

```text
sum_(a in Y) Omega(z;a)/product_(b in Y\{a})(a-b)=0.  (QBC8)
```

The three roots `t` of `B` give forced replay checks after exceptional CRT
reconstruction:

```text
C(t) z Omega_A(z;t)=q_e(t)^2 S(z;t),                  (QBC9)
C(t)^(-1)=N^(-1)t(t-s)(t-x_0)A(t)B'(t).              (QBC10)
```

Within the exact active-row design, the degree collapse `(QBC5)` is
equivalent to the global weld `(CLQ11)`: if the canonical exceptional
remainder has `X`-degree at most four, it is the unique `Omega` and forces
the full biform identity. Consequently a classifier need not construct the
`3e` external quartic cofactors before applying this gate.

No projective-line, fixed-quartic, splitting, or coefficient-rank bound is
asserted. A deterministic random pair-Lagrange packet at `e=3` has
`deg_X Omega_A=5`, showing that the degree-four collapse is not automatic
from pair-Lagrange interpolation or the smooth support partition alone.
