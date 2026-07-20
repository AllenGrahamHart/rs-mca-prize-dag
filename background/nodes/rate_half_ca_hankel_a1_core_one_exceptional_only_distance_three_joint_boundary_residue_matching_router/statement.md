# `A=1` distance-three joint boundary/residue matching router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_matching_free_boundary_power_router`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dual_row_product_power_router`

Retain the distance-three support packet. Let

```text
G_r=F_q^*/(F_q^*)^r,       [x]_r in G_r,             (JRM1)

c_a=C(a)=P_X'(a)/(A'(a)B(a))              (a in R_A),
M=product_(t in T)C(t),
C(t)=P_X'(t)/(A(t)B'(t)).                 (t in T)   (JRM2)
```

Use the matching-free boundary values

```text
Y_a=(P_X'(a)/(B(a)^4A'(a)^4))^e,
mu=[-M]_r.                                             (JRM3)
```

Label each exceptional root by

```text
Lambda(a)=(Y_a,[c_a]_r) in F_q^* x G_r              (JRM4)
```

and define the fixed-point-free involution

```text
tau(y,g)=(-y,mu g^(-1)).                              (JRM5)
```

There exists a perfect matching of `R_A` satisfying both every boundary
`e`-th-root gate and every dual row-product `r`-th-power gate if and only if
the multiset

```text
{Lambda(a):a in R_A}
```

is invariant under `tau`. Every joint-admissible matching is reconstructed
by pairing occurrences of a label with occurrences of its `tau` image.

In particular, every survivor satisfies the matching-free aggregate
residue obstruction

```text
[product_(a in R_A)C(a)]_r=[(-M)^e]_r,               (JRM6)
```

or equivalently

```text
product_(a in R_A)C(a)/(-M)^e in (F_q^*)^r.          (JRM7)
```

Since `A,B,C` are monic and pairwise coprime, this is the compact resultant
gate

```text
Res(A,C)/(-Res(B,C))^e in (F_q^*)^r.                 (JRM8)
```

When `gcd(r,q-1)=1`, `G_r` is trivial and the router reduces to the central
symmetry theorem. Otherwise it couples the two previously separate matching
filters before any internal slopes or scalars are allocated. It remains a
necessary support gate, not a proof of the external split design.
