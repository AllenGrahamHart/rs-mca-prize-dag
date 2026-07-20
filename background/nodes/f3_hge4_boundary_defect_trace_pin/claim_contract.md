# Claim contract

- **claim id:** `f3_hge4_boundary_defect_trace_pin`
- **status:** `PROVED`
- **mathematical statement:** at the `e=1,2` third-line boundaries, every
  separator-defect coefficient and its zero-value scalar gate are fixed by
  the first one or two locator coefficients; the `e=1` scaling orbit has the
  one-ratio normal form `(BTP5)`
- **scope:** separator-defect pairs with `h>e`, specialized to `e=1,2`; the
  official HGE4 boundary widths satisfy this condition
- **dependency:** `f3_hge4_complement_separator_defect_normal_form`
- **consumer:** `f3_hge4_norm_gate_count`
- **new open content:** classify split, disjoint, exact-level solutions of
  the pinned `e=1,2` differential equations and count all larger defects
- **falsifier:** one in-scope pair whose computed defect or zero-value gate
  differs from `(BTP1)--(BTP5)`
- **nonclaims:** no boundary emptiness, split-root converse, characteristic
  exclusion, or orbit count
- **replay:** `python3 background/nodes/f3_hge4_boundary_defect_trace_pin/verify.py`
  and `verify_audit.py`
