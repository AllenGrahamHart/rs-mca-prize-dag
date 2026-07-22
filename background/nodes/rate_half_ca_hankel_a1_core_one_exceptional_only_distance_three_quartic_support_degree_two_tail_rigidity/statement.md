# `A=1` distance-three degree-two support-tail rigidity

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_degree_two_three_subgroup_reduction`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_antiweight_absorption`

Retain an exact official all-deficient packet whose common field has degree
two, and let `tau` be its antipodal or constant-product deck involution. Put

```text
L={l:P_l=c_lD_l^2 for some c_l in F^*}.             (QDTR1)
```

The exact internal-slice values imply

```text
|L|<=2.                                             (QDTR2)
```

In the non-antiweight ratio branch, fix any exceptional pair `D_m` which is
an exact nonfixed `tau`-orbit. Every off-involution pair `D_l`, with
`l notin L` and containing no fixed point of `tau`, charges a distinct zero
of the quartic `P_m`. Consequently there are at most four such pairs.

In the antiweight-derived degree-two branch, every `r_l=P_l/D_l^2` with
`l notin L` is already `tau`-invariant. Hence every off-involution pair
outside `L` contains a fixed point of `tau`; there is no four-zero escape.

Since the antipodal involution has no fixed subgroup point and the
constant-product involution has at most two, the number `t` of exceptional
pairs which are not exact nonfixed `tau`-orbits satisfies, uniformly across
both degree-two branches,

```text
t<=6       (antipodal),
t<=8       (constant product).                      (QDTR3)
```

Combined with bounded-tail row codegree, every nonidentical outside orbit
therefore has normalized-row codegree at most six or eight, respectively.
At most one outside orbit has identical normalized rows.
