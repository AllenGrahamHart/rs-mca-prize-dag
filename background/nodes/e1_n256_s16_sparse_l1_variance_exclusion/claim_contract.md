# Claim contract

## Inputs

- `e1_n256_s16_high_variance_collision_exclusion`, including the
  profile, exact even variance, and residual `0<V<=134`;
- `collision_norm_criterion`.

## Output

Variances `84,86,...,134` are collision-free. The unresolved
profile-`(3,4,0)` residual is positive even `V<=82`.

## Guards

1. `L` is the positive-half autocorrelation L1 norm, not the
   coefficient L1 norm of `F`.
2. The support-pair count 21 bounds the number of nonzero distance classes;
   repeated distances can only reduce that count.
3. The stronger `4L<=E+66` bound uses the profile-specific multiset of
   raw chord magnitudes: three `4`s, twelve `2`s, and six `1`s.
4. Diameter chords are removed from both raw mass ledgers before the
   classwise cancellation inequality is summed.
5. The endpoint improvements at `E=43,...,52` use the exact local
   slack classifications and a stated finite recurrence in a deliberately
   enlarged relaxation. The earlier exploratory geometry DP is not
   load-bearing.
6. The optimized majorants have exact first derivative root 14 and second
   roots from 43 through 48 as stated in the proof; they are not
   extrapolations of the mean-tangent table.
7. Every logarithmic majorant uses the row-specific ceiling `B`.
8. Endpoint and six-bit inequalities are exact rational Taylor comparisons.
9. The `V=84` cubic certificate uses all 42 integer autocorrelation profiles
   with `E=42,L<=24`; its nested-layer count is an upper bound on the signed
   third moment, not a realizability classification.
10. No claim is made for `0<V<=82` or profile `(4,2,0)`.

## Falsifier

A profile-`(3,4,0)` vector in one of the excluded variance blocks whose
nonzero norm is divisible by a pair-feasible row prime.
