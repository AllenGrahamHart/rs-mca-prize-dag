# Claim contract

- **claim id:** `f3_hge4_quadratic_boundary_orbit_bound`
- **status:** `PROVED`
- **mathematical statement:** after two square-class normalizations, the
  `e=2` reciprocal locator is forced by `(epsilon,x,a)` and a nonzero
  degree-`h+1` endpoint polynomial bounds all ordered orbits by
  `2(m-1)(h+1)`
- **scope:** `m=3h+2`, `h>2`, field containing `mu_m`, characteristic zero
  or greater than `4h+1`; official HGE4 rows satisfy the scope
- **dependency:** `f3_hge4_boundary_defect_trace_pin`
- **consumer:** `f3_hge4_norm_gate_count`
- **new open content:** all retained defect widths `e>=4`
- **falsifier:** one in-scope pair violating the recurrence/endpoints, an
  identically zero `f_(h+1)` polynomial, or more than `2(m-1)(h+1)` orbits
- **nonclaims:** endpoint sufficiency, boundary emptiness, or any growing-
  defect count
- **replay:** `python3 background/nodes/f3_hge4_quadratic_boundary_orbit_bound/verify.py`
  and `verify_audit.py`
