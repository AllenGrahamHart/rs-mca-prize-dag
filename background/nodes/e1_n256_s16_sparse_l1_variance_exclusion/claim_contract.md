# Claim contract

## Inputs

- `e1_n256_s16_high_variance_collision_exclusion`, including the
  profile, exact even variance, and residual `0<V<=134`;
- `collision_norm_criterion`.

## Output

Variances `100,102,...,134` are collision-free. The unresolved
profile-`(3,4,0)` residual is positive even `V<=98`.

## Guards

1. `L` is the positive-half autocorrelation L1 norm, not the
   coefficient L1 norm of `F`.
2. The support-pair count 21 bounds the number of nonzero distance classes;
   repeated distances can only reduce that count.
3. The stronger `4L<=E+66` bound uses the profile-specific multiset of
   raw chord magnitudes: three `4`s, twelve `2`s, and six `1`s.
4. Diameter chords are removed from both raw mass ledgers before the
   classwise cancellation inequality is summed.
5. The endpoint improvements at `E=50,51,52` use only the exact local
   slack classifications `delta=0,2`; the exploratory partition DP is not
   load-bearing.
6. The `V=100` majorant is optimized separately, with exact derivative
   roots 14 and 48; it is not an extrapolation of the mean-tangent table.
7. Every logarithmic majorant uses the row-specific ceiling `B`.
8. Endpoint and six-bit inequalities are exact rational Taylor comparisons.
9. No claim is made for `0<V<=98` or profile `(4,2,0)`.

## Falsifier

A profile-`(3,4,0)` vector in one of the excluded variance blocks whose
nonzero norm is divisible by a pair-feasible row prime.
