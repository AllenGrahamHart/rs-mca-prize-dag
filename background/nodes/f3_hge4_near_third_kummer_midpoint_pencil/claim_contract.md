# Claim contract

- **claim id:** `f3_hge4_near_third_kummer_midpoint_pencil`
- **status:** `PROVED`
- **mathematical statement:** every near-third Belyi pair has complement
  `W=ZS+lambda y^c`, and its midpoint `S` divides one twisted `m`-th-power
  binomial; over a finite base field primitivity forces its uniform Kummer
  factor degree to be one, so the complete three-member pencil splits over
  the base field
- **scope:** `m=3h+e`, `0<e<h`; characteristic zero or `p>4h+e`; finite-field
  factor-degree conclusion only when the base field contains `mu_m`
- **dependency:** `f3_hge4_near_third_belyi_necklace_bound`
- **consumers:** `f3_hge4_kummer_midpoint_trace_power_gate`,
  `f3_hge4_norm_gate_count`
- **new open content:** count the resulting primitive Kummer midpoint pencils
  uniformly in the retained strip `h<2e+1`
- **falsifier:** an in-scope primitive pair for which `W-ZS` has a coefficient below
  degree `c`, `S` does not divide `1-(1-a^2lambda)y^m`, or a finite-field
  midpoint has an irreducible factor of degree greater than one
- **nonclaims:** no orbit payment; no emptiness; no assertion for `e>=h`
- **replay:** `python3 background/nodes/f3_hge4_near_third_kummer_midpoint_pencil/verify.py`
  and `verify_audit.py`
- **upstream mapping:** primitive shift-pair control / base-field-normalized
  split-pencil census
