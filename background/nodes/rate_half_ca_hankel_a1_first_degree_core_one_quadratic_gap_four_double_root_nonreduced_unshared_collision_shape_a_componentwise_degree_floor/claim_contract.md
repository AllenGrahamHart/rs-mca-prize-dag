# Claim contract

- **Claim:** every geometric off-diagonal shape-A component is base-field
  defined, non-toral, and has image bidegree at least `39,768,216`.
- **Dependencies:** the shape-A pure-split component theorem and the audited
  positive-characteristic subgroup-curve bound used for the ordinary
  quadratic companions.
- **Output:** a componentwise degree and forgotten-parameter multiplicity
  floor.
- **Consumer:** the shape-A branch of `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of high-degree components, no shape-A closure,
  and no extension-field transport.
- **Falsifier:** a geometric component not fixed by Frobenius despite a pure
  etale fiber, a toral component compatible with the odd cover degree, or a
  component with `D<39768216` satisfying the exact subgroup count.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_shape_a_componentwise_degree_floor/verify.py`.
