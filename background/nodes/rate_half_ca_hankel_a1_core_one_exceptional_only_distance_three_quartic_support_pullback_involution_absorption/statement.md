# `A=1` distance-three quartic pullback involution absorption

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_four_reducible_deck_router`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_antiweight_absorption`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_two_tail_rigidity`

Every surviving quartic pullback has a subgroup-preserving deck involution

```text
tau(X)=-X       for F(X^2) or F(X^4),
tau(X)=c/X      for F(X+c/X).                       (QPIR1)
```

In the ordinary ratio-field branch, at most nine captured exceptional pairs
fail to be nonfixed `tau`-orbits in the antipodal case, and at most eleven
fail in the constant-product case. Since at least `e-148` pairs are captured,
one exact nonfixed `tau`-orbit exists. Comparing every pair against that
fixed orbit gives the global bounds

```text
t<=6       (antipodal),
t<=8       (constant product).                      (QPIR2)
```

In the antiweight-derived quartic branch the stronger bounds are `t<=2` and
`t<=4`.

Thus every degree-four pullback is absorbed into the same bounded-tail
dihedral row-codegree, Pade-circuit, relation-class, and static-gcd interface
as the degree-two branch. There is no independent quartic-pullback support
leaf and no useful `PB4` computation fleet.
