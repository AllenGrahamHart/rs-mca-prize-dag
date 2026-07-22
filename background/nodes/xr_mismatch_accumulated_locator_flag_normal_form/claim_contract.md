# Claim contract

- **claim id:** `xr_mismatch_accumulated_locator_flag_normal_form`
- **status:** `PROVED`
- **claim:** every compatible canonical nongeneric mismatch branch has the
  global lift, disjoint accumulated locator, witness factorization, prefix
  divisibility, and residual low-core invariants `(AL1)--(AL8)`
- **scope:** one selected slope and every finite prefix of its canonical
  mismatch descent
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **proved dependencies:** full external-zero canonicalization, equivalence
  with a second joint support, and invariant-excess descent
- **falsifier:** overlapping locator layers in a valid chain, a lifted pair
  of degree at least `K`, failure of `(AL4)` after one transition, a global
  support smaller than `A`, or a residual intersection above `(AL8)`
- **new open content:** count locator flags and terminal generic slope fibers
  across lifted explanations without a support-only or depth multiplier
- **nonclaims:** no branch-width, explanation-count, generic-chart, or slope
  payment
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_mismatch_accumulated_locator_flag_normal_form/verify.py`
- **audit replay:**
  `tools/ramguard tiny -- python3 background/nodes/xr_mismatch_accumulated_locator_flag_normal_form/verify_audit.py`
- **upstream mapping:** witness-exhaustive first-match atlas / residual ray
  compiler with bounded-degree locator flags
