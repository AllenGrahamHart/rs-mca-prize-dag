# Claim contract

- **claim id:** `f3_hge4_complement_separator_defect_normal_form`
- **status:** `PROVED`
- **mathematical statement:** every retained complement-third pair has an
  exact degree-`e=m-3h` separator defect satisfying `(SDN2)--(SDN4)`
- **scope:** exactly the field, split-root, disjointness, constant-difference,
  and non-full hypotheses of `f3_hge4_nonfull_complement_third_gate`
- **dependency:** `f3_hge4_nonfull_complement_third_gate`
- **consumer:** `f3_hge4_norm_gate_count`
- **new open content:** classify or uniformly count the split subgroup-root
  solutions of `(SDN4)`, beginning with `e=1,2`, and aggregate all larger
  defects within `(ERT4')`
- **falsifier:** one pair in scope for which `G=B-A` has a different degree,
  leading coefficient, or fails the differential identity
- **nonclaims:** no converse to `(SDN4)`; no primitivity, split-root, or orbit
  count follows from a formal solution; no fixed defect cap is asserted
- **replay:** `python3 background/nodes/f3_hge4_complement_separator_defect_normal_form/verify.py`
  and `verify_audit.py`
