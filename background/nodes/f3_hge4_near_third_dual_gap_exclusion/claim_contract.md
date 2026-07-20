# Claim contract

- **claim id:** `f3_hge4_near_third_dual_gap_exclusion`
- **status:** `PROVED`
- **mathematical statement:** primitive non-full exact-level pairs with
  `m=3h+e`, `0<e<h`, and `h>=2e+1` do not exist
- **scope:** dyadic exact level; characteristic zero or `p>4h+e`
- **dependency:** `f3_hge4_near_third_belyi_necklace_bound`
- **consumer:** `f3_hge4_norm_gate_count`
- **new open content:** widths `h<=floor(2m/7)`, including every `e>=h`
  width and the strip `h<2e+1`
- **falsifier:** one in-scope primitive pair with `7h>=2m+1`
- **nonclaims:** no count or emptiness assertion below the `2m/7` line
- **replay:** `python3 background/nodes/f3_hge4_near_third_dual_gap_exclusion/verify.py`
  and `verify_audit.py`
- **upstream mapping:** primitive shift-pair control / residual ray compiler
