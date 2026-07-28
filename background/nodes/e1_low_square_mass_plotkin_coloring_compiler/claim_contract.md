# Claim contract

## Claim

A proper coloring of the low-square-mass collision graph bounds every E1
fiber by `c(ell+1)`. The six exact `c_max` values in `statement.md` are the
largest color counts for which this fiber cap alone forces more than `B*`
distinct E1 values. Independently, the total low-mass edge count controls the
complete fiber second moment by
`sum_y r_y^2<=(ell+1)K+(2ell+2-d0)E_low`; the six printed edge budgets are the
largest integers for which this also forces more than `B*` values.

## Dependencies

- `acl_count` identifies classes with signed singleton vectors of norm at
  most `ell`.
- `e1_collision_square_mass_reparametrization` proves that pairwise square
  mass is even and is the correct class-difference coordinate.
- `e1_prime_field_l2_norm_collision_radius` supplies `d0=16` at `N=256` and
  `d0=4` at `N=512` for RowC.
- `e1_prize_field_floor_even_norm_exclusion` sharpens the prize values to
  `d0=18` and `d0=6`.
- `e1_clean_anchor_exact_collision_allowance` supplies the exact `K,B*`
  values and the direct-image payload criterion.

## Guards

1. The graph contains only pairs already colliding modulo the row prime.
2. The threshold is `S<=2ell`, including equality.
3. A color bound is row-specific. No universal three-color claim is made.
4. The compiler bypasses `P<=K-B*-1`; it does not prove that pair-incidence
   inequality.
5. The open coloring node must cover every row assigned to this supplier.
6. `E_low` counts unordered class pairs, not coefficient vectors or Galois
   orbits.
7. The sharpened `d0` values are prize-specific and cannot be used for RowC.

## Falsifier

A color class inside one E1 fiber with more than `ell+1` vertices, failure of
any exact integer inequality in the six-row ledger, or a row whose claimed
coloring uses more than `c_max` colors; for the aggregate route, failure of
the second-moment inequality or an off-by-one edge budget.
