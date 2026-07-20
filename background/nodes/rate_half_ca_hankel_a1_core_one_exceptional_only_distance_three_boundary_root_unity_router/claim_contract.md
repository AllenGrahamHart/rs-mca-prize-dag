# Claim contract

- **scope:** official distance-three pair-Lagrange external split design on
  the smooth multiplicative evaluation domain
- **input:** exceptional root set `A`, triple `B`, omitted row `x_0`, and a
  perfect matching of the roots of `A`
- **currency:** slope-independent boundary values of the exact external norm
- **output:** one `e`th-root-of-unity gate per matched pair and the triple
  gates `(BRU3)--(BRU5)`
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** monic external product `C^e`, disjoint
  squarefree `A,B,C`, and the multiplicative-domain derivative formula
- **nonclaim:** passing the root-unity gates does not construct internal
  slopes, fiber scalars, or any external split locator
- **failure certificate:** one pair or triple ratio whose `e`th power is not
  one
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_boundary_root_unity_router/verify.py`
- **upstream mapping:** exact finite SPI boundary-norm/root-unity prefilter
