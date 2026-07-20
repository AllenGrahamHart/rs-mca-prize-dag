# Claim contract

- **claim id:** `f3_h3_dsp8_nodal_trace_parameter_router`
- **mathematical statement:** every singular trace fiber has the explicit
  rational form `(NTP1)`, at most three affine coset branches, point count
  `<12n^(2/3)+1`, target factorization `(NTP4)`, and weighted marginal
  envelope `(NTP5)--(NTP6)`
- **scope:** all official H3 rows and all traces with `sigma^3=27`
- **consumer:** `f3_h3_dsp8_nodal_target_divisor_pruning`
- **status:** `PROVED`
- **proved dependencies:** the unit-trace curve classification and optimized
  one-fiber affine Stepanov theorem
- **new open content:** improve the nodal constant by using the retained
  richness/disjointness/target-line correlation, or absorb it in a uniform
  smooth-plus-nodal theorem
- **falsifier:** a nonnode point absent from `(NTP1)`, a failed coset criterion
  `(NTP2)`, a target not satisfying `(NTP4)`, or violation of `(NTP5)`
- **nonclaims:** no DSP8 payment, no deletion of singular traces, and no
  transfer of the marginal envelope to the smooth elliptic fibers
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/f3_h3_dsp8_nodal_trace_parameter_router/verify.py`
