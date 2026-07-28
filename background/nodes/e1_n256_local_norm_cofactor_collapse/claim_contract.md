# Claim contract

## Inputs

- `e1_pair_feasible_prime_field_reduction`, specifically
  `p=1 mod 256`;
- `e1_n256_2adic_cofactor_collision_exclusion`, including the exact
  valuation and cofactor bounds;
- `e1_prize_field_floor_even_norm_exclusion`, for the prize-specific field
  floor used to reduce 419 `(4,2,0)` cofactors to eight;
- the explicit cyclotomic case of local reciprocity over `Q_2`.

## Output

The odd part of every integral local norm is one modulo 256. Collision
cofactors therefore have the exact forms printed in `statement.md`.

## Guards

1. The congruence is applied to the norm after removing its exact power of
   two.
2. The global norm is positive; no hidden sign changes the residue.
3. The congruence `p=1 mod 256` is consumed only on the proved
   pair-feasible prime-field branch.
4. The five square-mass-16 cofactor values are necessary, not sufficient.
5. No primality or interval membership of the odd norm part is asserted.
6. The eight-element refinement applies only to prize-envelope rows. The
   419-element set remains the valid RowC interface.

## Falsifier

An integral `Q_2(zeta_256)` norm whose odd part is not one modulo
256, or a live collision whose cofactor violates the printed list.
