# `A=1` distance-three dihedral trace-collision exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dihedral_pair_complement_quadratic_trace`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_external_split_design_saturation`

Retain either dihedral branch of the distance-three external split design,
and assume `e>=31`. For each external slope `gamma`, define the quadratic

```text
q_gamma(U)=
 -[U^2M_0(gamma)-2U M_1(gamma)+M_2(gamma)]/I(gamma). (TCX1)
```

Then the calibrated complement and incidence ledgers are incompatible.
Consequently no antipodal or constant-product dihedral packet satisfying the
two dependencies exists for `e>=31`.

In particular, the exclusion applies to the official row

```text
e=2^38-1.                                             (TCX2)
```

This closes the surviving dihedral distance-three external-design branch;
it does not by itself prove the full rate-half band determination.
