# `A=1` distance-three dihedral quotient external-product ledger

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dihedral_subgroup_norm_descent`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_saturation`

Retain a dihedral external split design and let `tau` be its antipodal or
constant-product involution on `mu_N`. Partition the `tau`-orbits meeting the
active outside-row set `C` into

```text
C_2(U)=product_(nonfixed orbits contained in C)(U-u),
C_1(U)=product_(orbits meeting C in exactly one point)(U-u). (QEP1)
```

A fixed point in `C` belongs to the second class. Put

```text
p=deg C_2,       h=deg C_1.
```

Then

```text
2p+h=6e+3,       h is odd and h>=1.                 (QEP2)
```

For each of the `3e` external slopes `z`, let `V_z(U)` be the descended
degree-`r` polynomial from the subgroup-norm descent, normalized to be monic.
Then the complete external product is

```text
product_(z external) V_z(U)=C_2(U)^(2e) C_1(U)^e.   (QEP3)
```

Every root of `V_z` has multiplicity one or two. Write

```text
d_z=#{double roots of V_z},
s_z=#{simple roots of V_z},       r=2d_z+s_z.        (QEP4)
```

For a nonfixed orbit `O={x,tau(x)}` contained in `C`, let

```text
d_O=#{external blocks containing both x and tau(x)}.
```

Every such orbit has `d_O=0`, except for at most one identical-row orbit. Its
only possible quotient coordinate is

```text
u=-sigma_2                         (antipodal),
u=sigma_1-sigma_3/c                (constant product),             (QEP5)
```

where `B=X^3-sigma_1X^2+sigma_2X-sigma_3`. Put

```text
epsilon=1 if the exceptional orbit is present in C_2, else 0.
```

Then

```text
d_O=e for that orbit and d_O=0 for every other orbit,   (QEP6)

sum_(z external) d_z=epsilon e,
sum_(z external) s_z
 =3er-2epsilon e
 =e(6e+3-2epsilon).                                    (QEP7)
```

Thus every external `V_z` is squarefree when `epsilon=0`. When `epsilon=1`,
exactly `e` external factors have one double root at the exceptional
coordinate and the other `2e` factors are squarefree.

This is a necessary multiplicity ledger for the remaining quotient
split-polynomial family. It does not exclude that family.
