# Claim contract

- **scope:** official exceptional-only quotient-distance-three chart after
  pair-Lagrange and exact external-design normalization
- **input:** paired exceptional roots, internal slopes `xi_i`, internal
  scalars `lambda_i`, and nonzero `Theta_2`
- **currency:** contracted source coefficients and the full `2r+1` endpoint
  moment vectors
- **output:** exact formulas `(SWR3)--(SWR7)` plus the contracted Hankel
  converse `(SWR8)--(SWR9)`; no free source, moment, Hankel, rank, or
  adjugate variables remain
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** the minimum-distance circuit normalization,
  monic external locators, disjoint squarefree `A,B,G_z`, and at least two
  external slopes
- **nonclaim:** the converse assumes the required external split fibers; it
  does not construct them, impose the corrected reciprocal square, certify
  the original endpoint lift as column-far, or exclude additional split
  fibers
- **failure certificate:** a valid packet whose exceptional-root affine
  coefficient differs from `(SWR4)--(SWR6)`, whose circuit scalar differs
  from `(SWR7)`, whose reconstructed moments differ from the packet, or
  failure of `(SWR8)--(SWR9)` after the external split hypotheses hold
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_mds_source_weight_reconstruction/verify.py`
- **upstream mapping:** exact finite SPI minimum-circuit source reconstruction
