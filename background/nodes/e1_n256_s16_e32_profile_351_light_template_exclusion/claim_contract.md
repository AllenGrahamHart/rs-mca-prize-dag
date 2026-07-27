# Claim contract

## Claim

No pair-feasible folded coefficient vector in the `N=256`, `(3,4,0)`,
`V=64` chamber has autocorrelation magnitude profile `(3,5,1)`.

## Dependencies

- `e1_n256_s16_e32_profile_parity_diameter_reduction` for the exact profile
  interface and cubic threshold `M_3=1517`;
- `e1_n256_s16_e32_four_odd_light_template_reduction` for the complete
  148-orbit light router;
- `collision_norm_criterion` for exclusion by the strict norm bound.

## Nonclaims

- no exclusion of profile `(4,7)`;
- no claim that the shared census's `(4,7)` maximum lies below 1517;
- no exclusion of another positive even variance;
- no claim about the separate first-band profile `(4,2,0)`;
- no promotion of either universal E1/unsafe target.

## Falsifier

A four-odd light support outside the 148 affine-unit orbits refutes the
router dependency. A tested profile-`(3,5,1)` vector with `M_3>1392`, a
coverage omission in either exact engine, or failure of the inherited cubic
norm certificate refutes the exclusion.
