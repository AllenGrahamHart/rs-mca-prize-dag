# Claim contract

## Claim

No pair-feasible `N=256` folded-profile `(3,4,0)` vector at `V=60` has
magnitude profile `(6,6)`.

## Inputs consumed

- `e1_n256_s16_e30_profile_66_relaxation_certificate` for the exact relaxed
  exceptional set;
- `e1_n256_s16_e30_profile_66_actual_census_certificate` for the exact
  actual-vector and conductor census;
- `e1_n256_s16_e30_profile_66_primitive_norm_certificate` for the exact
  primitive norm cap;
- the proper-conductor collision exclusion;
- the collision-norm criterion.

## Output supplied

The final live profile in the exact `V=60` reduction is excluded uniformly
over every pair-feasible row prime. The E30 endpoint synthesis may therefore
advance the positive even variance frontier to `V<=58`.

## Scope exclusions

- no claim about `V<=58`;
- no claim about folded profile `(4,2,0)`;
- no claim about later `N=256` or `N=512` bands;
- no route-wide pair-incidence bound.
