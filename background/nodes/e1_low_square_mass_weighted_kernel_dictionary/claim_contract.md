# Claim contract

## Claim

The exact weighted identity

```text
E_low=(1/2) sum_d M_ell(a(d),b(d))
```

and the six uniform sufficient oriented-vector caps in `statement.md`.

## Dependencies

- `e1_collision_square_mass_reparametrization` supplies the signed-singleton
  class model, the profile `(a,b)`, and the square-mass cutoff.
- `e1_prime_field_l2_norm_collision_radius` supplies the profile exclusions
  used only in the maximum-weight table.
- `e1_low_square_mass_plotkin_coloring_compiler` supplies the six exact edge
  budgets to which the uniform caps are calibrated.
- `e1_prize_field_floor_even_norm_exclusion` removes `S<=16` at prize
  `N=256` and `S<=4` at prize `N=512` before the maximum-weight calculation.

## Guards

1. `D_p(ell)` contains oriented folded vectors. Both `d` and `-d` occur.
2. `M_ell` counts class pairs, not raw subset representatives.
3. Orbit-normalized vector counts require exact stabilizer and weight
   restoration before entering the identity.
4. The uniform vector caps are sufficient, not necessary. Exceeding one is
   not a counterexample to the edge budget.
5. The exact weighted sum is preferable to `M_max|D|/2`; profile information
   must not be discarded after it has been proved.
6. No vector cap, collision exclusion, image bound, or prize row is proved by
   this node alone.
7. RowC retains the coarser norm floors; the prize refinement must not be
   transferred to it.

## Falsifier

A valid small class model where the formula disagrees with direct ordered
pair enumeration, an eligible official profile with weight above the printed
maximum, or failure of an exact cap inequality.
