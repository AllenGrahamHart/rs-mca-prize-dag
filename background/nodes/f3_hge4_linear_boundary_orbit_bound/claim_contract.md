# Claim contract

- **claim id:** `f3_hge4_linear_boundary_orbit_bound`
- **status:** `PROVED`
- **mathematical statement:** every dyadic `e=1` exact-level ordered scaling
  orbit has one uniquely forced normalized locator indexed by
  `x in mu_m\{1,-1}`; hence its count is at most `m-2`
- **scope:** `m=3h+1`, `h>1`, characteristic zero or greater than `4h`;
  every official HGE4 row satisfies this characteristic condition
- **dependency:** `f3_hge4_boundary_defect_trace_pin`
- **consumer:** `f3_hge4_norm_gate_count`
- **new open content:** the `e=2` boundary and every growing-defect width in
  the reduced exact-level aggregate
- **falsifier:** two distinct normalized ordered pairs with the same ratio
  `x`, one pair violating `(LBO1)` or `(LBO3)`, or more than `m-2` orbits
- **nonclaims:** `(LBO3)` is not sufficient for split subgroup roots; no
  count is asserted for `e>=2`
- **replay:** `python3 background/nodes/f3_hge4_linear_boundary_orbit_bound/verify.py`
  and `verify_audit.py`
