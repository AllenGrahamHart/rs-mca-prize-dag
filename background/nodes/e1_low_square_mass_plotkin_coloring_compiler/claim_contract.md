# Claim contract

## Claim

A proper coloring of the low-square-mass collision graph bounds every E1
fiber by `c(ell+1)`. The six exact `c_max` values in `statement.md` are the
largest color counts for which this fiber cap alone forces more than `B*`
distinct E1 values.

## Dependencies

- `acl_count` identifies classes with signed singleton vectors of norm at
  most `ell`.
- `e1_collision_square_mass_reparametrization` proves that pairwise square
  mass is even and is the correct class-difference coordinate.
- `e1_clean_anchor_exact_collision_allowance` supplies the exact `K,B*`
  values and the direct-image payload criterion.

## Guards

1. The graph contains only pairs already colliding modulo the row prime.
2. The threshold is `S<=2ell`, including equality.
3. A color bound is row-specific. No universal three-color claim is made.
4. The compiler bypasses `P<=K-B*-1`; it does not prove that pair-incidence
   inequality.
5. The open coloring node must cover every row assigned to this supplier.

## Falsifier

A color class inside one E1 fiber with more than `ell+1` vertices, failure of
any exact integer inequality in the six-row ledger, or a row whose claimed
coloring uses more than `c_max` colors.
