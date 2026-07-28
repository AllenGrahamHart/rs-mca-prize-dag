# Claim contract

## Inputs

- `e1_n256_local_norm_cofactor_collapse` for the seven prize cofactors and the
  singleton-separation interpretation of their 2-adic valuations;
- `e1_prize_field_floor_even_norm_exclusion` for the exact prize interval;
- `collision_norm_criterion` for `p` dividing the nonzero integral norm.

## Output

Every prize-row collision in profile `(4,2,0)` obeys the six nonempty
cofactor/variance windows in `statement.md`; cofactor `1538` is impossible.

## Guards

1. `V` is the exact full odd-conjugate variance, not a sampled moment.
2. The congruence `V=2 mod 8` uses the live cofactor restriction; it is not
   asserted for an arbitrary two-singleton vector with antipodal singletons.
3. The exact `V=2` norm depends on the singleton separation's 2-adic order.
4. A residual variance window is not evidence that a vector or row prime
   realizing it exists.
5. No RowC cofactor is removed, and no later square-mass profile is controlled.
6. The aggregate weighted collision-pair budget remains open.

## Falsifier

A pair-feasible prize-envelope row and profile `(4,2,0)` collision outside the
printed window for its exact cofactor, or an arithmetic failure in the
Taylor/resultant certificates.
