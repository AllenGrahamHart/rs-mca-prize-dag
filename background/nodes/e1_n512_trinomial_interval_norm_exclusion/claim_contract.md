# Claim contract

## Inputs

- `e1_prime_field_l2_norm_collision_radius`, including the exact two-profile
  classification at `N=512,s=2` and the two field intervals;
- `e1_n512_four_singleton_collision_exclusion`;
- `collision_norm_criterion`.

## Output

- profile `(1,2,0)` has no collision at any named pair-feasible anchor;
- consequently every surviving `N=512` collision has raw swap distance
  `s>=3`.

## Guards

1. The normalized state space contains all choices of two distinct singleton
   coordinates and both signs.
2. The quotient is by the full odd Galois group, and orbit sizes sum to the
   unquotiented state count.
3. Resultants are exact integers; numerical root products are not used.
4. Both full prime intervals are screened. No list of selected primes or
   named exhibits replaces the interval quantifier.
5. The cofactor-window test is exact and does not assume a factorization.
6. Swap distances `s>=3` and the total collision-pair allowance remain open.

## Falsifier

A normalized state outside the 129540-state partition, a resultant mismatch,
or an odd prime `p=1 mod 512` in either printed interval dividing one of the
746 certified norms.
