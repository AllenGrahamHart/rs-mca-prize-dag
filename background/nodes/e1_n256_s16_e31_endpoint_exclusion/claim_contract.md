# Claim contract

## Claim

Variance `V=62` is impossible on the pair-feasible `N=256`, folded-profile
`(3,4,0)` branch; its live positive even frontier is `V<=60`.

## Dependencies

- `e1_n256_s16_e31_profile_parity_light_reduction` for exhaustive reduction;
- `e1_n256_s16_e31_three_profile_joint_exclusion` for all three profile
  exclusions.

## Nonclaims

- no exclusion of any positive even `V<=60`;
- no statement about folded profile `(4,2,0)`;
- no global collision-pair allowance or prize closure.

## Falsifier

A pair-feasible collision at `V=62`, a residual profile not named by the
reduction, or a failed profile exclusion refutes the synthesis.
