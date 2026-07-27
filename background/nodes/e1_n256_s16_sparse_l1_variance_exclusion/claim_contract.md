# Claim contract

## Inputs

- `e1_n256_s16_high_variance_collision_exclusion`, including the
  profile, exact even variance, and residual `0<V<=134`;
- `collision_norm_criterion`.

## Output

Variances `112,114,...,134` are collision-free. The unresolved
profile-`(3,4,0)` residual is positive even `V<=110`.

## Guards

1. `L` is the positive-half autocorrelation L1 norm, not the
   coefficient L1 norm of `F`.
2. The support-pair count 21 bounds the number of nonzero distance classes;
   repeated distances can only reduce that count.
3. Every logarithmic majorant uses the row-specific ceiling `B`.
4. Endpoint and six-bit inequalities are exact rational Taylor comparisons.
5. No claim is made for `0<V<=110` or profile `(4,2,0)`.

## Falsifier

A profile-`(3,4,0)` vector in one of the excluded variance blocks whose
nonzero norm is divisible by a pair-feasible row prime.
