# Attack

1. Start from the exact survivor region `(PF6)` in
   `l1_fpc5_large_source_exact_prefilter`; do not revisit EMPTY, singleton,
   or positive-Johnson cells.
2. Work in the exact affine locator chart supplied by
   `l1_fpc5_tpetal_saturated_slice_dimension`; do not re-prove a `t`-petal
   syzygy or dimension formula.
3. Use the anchor coordinate in `l1_fpc5_tpetal_anchor_coordinate`; do not
   enumerate cofactor pairs or independent fixed-owner pencils.
4. Use the explicit remainder inverse and root-local primitive guard in
   `l1_fpc5_tpetal_anchor_pade_chart`; do not re-derive pair reconstruction.
5. Use the joint owner in `l1_fpc5_tpetal_joint_anchor_owner`; defect and
   background overlap are one gcd stratum, while non-anchor background roots
   are affine coordinate equations. Do not sum the two owner types
   independently.
6. Use `l1_fpc5_tpetal_joint_owner_packing` for every fixed owner. Do not
   re-prove bounded co-deficiency packing or sum its per-owner charge over
   all divisors of the anchor polynomial.
   The exact small-cell Modal probe
   `experiments/prize_resolution/fpc5_joint_owner_probe_result.json` found
   that 3781/4012 realized owner groups were singletons and 905/1095 anchor
   views had an injective neighbor-to-owner map. Do not assume only a bounded
   number of owners occur; seek structure across many distinct owners.
7. Use `l1_fpc5_tpetal_joint_owner_ambient_mds_census` as a hard route fence.
   The complete monic chart realizes every degree-`r` divisor of `P_0` as a
   top owner, with `|mathbb F|-1` points per divisor. Any owner coalescence
   must retain the reconstructed-locator split predicate and all exact
   guards; owner dimension, MDS support counting, or unguarded linear
   algebra has no power.
8. Use `l1_fpc5_tpetal_joint_owner_split_pencil`: after writing `Q=DE`, work
   with `AV-CU=Lambda K` and the fixed-owner coordinate
   `K_0(C,V)=K(C_0,V_0)+T(A,U)`, where
   `deg K,deg T<=r-deg Q`. At top ownership the latter is an ordinary affine
   pencil of core-split locators. Do not identify it with a same-domain
   divisor census: its natural determinant parent is the disjoint
   touched-petal locator.
9. Seek a uniform bounded-tail dual-domain pencil census across many
   distinct owners, preserving the petal congruences and remaining affine
   background guards. Reuse Przemek's split-pencil methods only after
   proving the required domain and normalization transport.
10. Use the source equation `n-k+1=Mell+b` and the FPC6 deficit coordinates.
11. Seek a collective large-`M` incidence or first-owner inequality before
   refining individual locator tuples.
12. Price touched-petal multiplicity and source multiplicity together.
13. Keep rate-dependent lower source sizes explicit; do not reintroduce the
   strict cells removed by the small-source degree sieve.
