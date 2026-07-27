# Claim contract

## Inputs

- `e1_n256_s16_high_variance_collision_exclusion`, including the
  profile, exact even variance, and residual `0<V<=134`;
- `collision_norm_criterion`.

## Output

Variances `78,80,...,134` are collision-free. The unresolved
profile-`(3,4,0)` residual is positive even `V<=76`.

## Guards

1. `L` is the positive-half autocorrelation L1 norm, not the
   coefficient L1 norm of `F`.
2. The support-pair count 21 bounds the number of nonzero distance classes;
   repeated distances can only reduce that count.
3. The stronger `4L<=E+66` bound uses the profile-specific multiset of
   raw chord magnitudes: three `4`s, twelve `2`s, and six `1`s.
4. Diameter chords are removed from both raw mass ledgers before the
   classwise cancellation inequality is summed.
5. The endpoint improvements at `E=39,...,52` use the exact local
   slack classifications and a stated finite recurrence in a deliberately
   enlarged relaxation. The earlier exploratory geometry DP is not
   load-bearing.
6. The optimized majorants have exact first derivative root 14 and second
   roots from 43 through 48 as stated in the proof; they are not
   extrapolations of the mean-tangent table.
7. Every logarithmic majorant uses the row-specific ceiling `B`.
8. Endpoint and six-bit inequalities are exact rational Taylor comparisons.
9. The `V=84,82,80,78` cubic certificates use all 42, 39, 34, and 29
   integer autocorrelation profiles at `E=42,L<=24`, `E=41,L<=23`,
   `E=40,L<=22`, and `E=39,L<=21`, respectively. Their nested-layer
   counts upper-bound signed third moments and are not realizability
   classifications.
10. No claim is made for `0<V<=76` or profile `(4,2,0)`.
11. Failure of the tested cubic-Hermite family at `V=76` is only a route
    boundary, not evidence that the row is feasible.

## Falsifier

A profile-`(3,4,0)` vector in one of the excluded variance blocks whose
nonzero norm is divisible by a pair-feasible row prime.
