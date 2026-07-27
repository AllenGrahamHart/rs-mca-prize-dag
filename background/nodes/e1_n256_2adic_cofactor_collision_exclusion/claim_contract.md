# Claim contract

## Inputs

- `e1_prime_field_l2_norm_collision_radius`, including both
  `N=256,s=5` profiles, their square masses, and `p>=2^250`;
- `collision_norm_criterion`.

## Output

Every first-band collision candidate passes the printed 2-adic multiplicity
bound: at most five in profile `(3,4,0)` and at most sixteen in profile
`(4,2,0)`.

## Guards

1. `mu` is the exact root multiplicity of the reduced folded polynomial
   at one, not merely the parity of its value.
2. The strict cofactor bounds use that an odd prime cannot equal `2^250`.
3. The valuation identity applies because `mu<128`; this follows from
   the nonzero degree-below-128 reduction.
4. Passing the multiplicity test is necessary, not sufficient, for collision.
5. The theorem does not classify the low-variance or full-conductor residuals.

## Falsifier

An excluded profile vector whose nonzero norm is divisible by a
pair-feasible row prime.
