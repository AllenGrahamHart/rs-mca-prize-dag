# Proof

The signed-edge atlas is exhaustive for the residual multigraph: target
sign gauge leaves exactly two lanes, distinguished by the sign product on
the five-cycle.  Hence every route packet has one of those two target lanes.

The common Vieta compiler has fifteen matching cells and four root-sign rows
per cell.  The exact common root-sign symmetry theorem partitions these 60
rows as `(KBPCR-1)`: one representative for each listed cell orbit except
`[1,2]`, which has two representatives distinguished by
`epsilon_1 epsilon_2`.  Thus there are ten representatives in total.

The closure ledger is exact:

1. `cell0_generic_signed_pair_orbit_exclusion` closes `[0]` (four rows).
2. `cell1_2_common_root_sign_orbit_exclusion` closes both sign-product
   representatives of `[1,2]` (eight rows).
3. `cell3_signed_pair_guard_factorization_exclusion` closes `[3,6]`
   (eight rows).
4. `cell4_main_projection_guard_factorization_exclusion`, together with
   its dependencies, closes `[4,7]` (eight rows).
5. `cell58_complete_root_sign_orbit_exclusion` closes `[5,8]` (eight rows).
6. `cell9_signed_pair_guard_factorization_exclusion` closes `[9,10]`
   (eight rows).
7. `cell11_signed_pair_guard_factorization_exclusion` closes `[11]`
   (four rows).
8. `cell12_signed_pair_guard_factorization_exclusion` closes `[12,13]`
   (eight rows).
9. `cell14_signed_pair_guard_factorization_exclusion` closes `[14]`
   (four rows).

The cell sets are disjoint and their union is `{0,...,14}`.  Their raw-row
counts sum to 60, and their representative counts sum to ten.  Each theorem
either treats every cycle/outside case directly or contradicts a necessary
signed-pair subsystem supplied by the universal paired-product interface.
Consequently neither signed lane has a complete packet in any common row.
The route is empty. QED.
