# E1 prize N=256 square-mass-18 leading-profile exclusion

- **status:** PROVED
- **closure:** exact cofactor synthesis plus integer weight ledger
- **scope:** prize rate-`1/8`, `N=256`, profile `(a,b,c)=(4,2,0)`
- **dependencies:** `e1_low_square_mass_weighted_kernel_dictionary`,
  `e1_prize_n256_s18_variance_cofactor_windows`, and the six exact residual
  cofactor exclusions

The profile `(4,2,0)`, equivalently weighted-kernel profile `(a,b,S)=(4,2,18)`,
has no collision on any prize-envelope `N=256` row.

The exact local-norm classification first leaves seven prize cofactors.
The variance theorem excludes `1538`, and exhaustive proved children exclude

```text
1028, 514, 256, 16, 4, 2.
```

Thus all seven classes are empty.

On the binding prize rate-`1/8` row, removing `(4,2,18)` from the 271
norm-eligible low-square-mass profiles leaves 270. Their largest class-pair
multiplicity is attained at `(3,6,18)` and equals

```text
1386246316188473270092082114587711840.
```

Consequently the aggregate pair budget is implied by the sharpened uniform
cap

```text
|D_p(33)|<=93962.
```

This is a sufficient unweighted cap, not a proof of that vector count. The
exact profile-weighted sum remains the preferred target.
