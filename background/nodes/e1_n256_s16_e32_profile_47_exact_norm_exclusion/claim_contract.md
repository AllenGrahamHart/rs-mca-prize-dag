# Claim contract

## Claim

No pair-feasible folded coefficient vector in the `N=256`, `(3,4,0)`,
`V=64` chamber has autocorrelation magnitude profile `(4,7)`.

## Dependencies

- `e1_n256_s16_e32_profile_parity_diameter_reduction` for the exact profile
  interface;
- `e1_n256_s16_e32_four_odd_light_template_reduction` for the complete
  148-orbit light router;
- `e1_n256_proper_conductor_collision_exclusion` for every proper-conductor
  vector;
- `collision_norm_criterion` for exclusion by a nonzero norm below the row
  prime.

## Nonclaims

- no claim that the cubic-Hermite bound pays `M_3=1524`;
- no exclusion of another positive even variance;
- no claim about the separate first-band profile `(4,2,0)`;
- no promotion of either universal E1/unsafe target.

## Falsifier

A full-conductor profile-`(4,7)` vector outside the 148-orbit coverage, a
retained vector with norm greater than `N_max`, disagreement between either
exact engine, failure of `15*N_max<2^250`, or a proper-conductor vector not
covered by the conductor theorem refutes the exclusion.
