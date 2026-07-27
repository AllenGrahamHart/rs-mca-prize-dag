# Claim contract

## Inputs

- `e1_prime_field_l2_norm_collision_radius`, including profile `(3,4,0)` and
  the lower field endpoint `p>=2^250`;
- `collision_norm_criterion`.

## Output

No profile `(3,4,0)` vector with `V=0` or `V>=136` collides at a named
pair-feasible anchor.

## Guards

1. `V` is the exact full odd-conjugate variance, not a sampled moment.
2. The `V=0` case is excluded by oddness of `p`, not by norm size.
3. The logarithmic majorant uses `|F|<=10`, hence `y<=100`.
4. The positive even residual `V<=134` remains open.
5. No conclusion is made for profile `(4,2,0)` or later bands.

## Falsifier

A profile `(3,4,0)` vector in one of the excluded variance ranges whose
nonzero norm is divisible by a named-interval row prime.
