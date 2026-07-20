# Claim contract

- **scope:** official distance-three pair-Lagrange external split design on
  the smooth multiplicative evaluation domain
- **input:** active-row locator `C`, external incidence design, and the
  matched exceptional pairs
- **currency:** the dual row product `(DRP2)` and one support-only
  `r`th-power residue per matched pair
- **output:** `(DRP2)--(DRP8)`
- **consumer:** `rate_half_band_closure`
- **load-bearing hypotheses:** every active row lies in exactly `e` external
  blocks, every external block has `r=2e+1` active roots, and the
  pair-Lagrange internal specializations are exact
- **nonclaim:** passing the power-residue gates does not construct internal
  slopes, fiber scalars, or external blocks
- **failure certificate:** one matched pair whose `R_i` fails `(DRP7)`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dual_row_product_power_router/verify.py`
- **upstream mapping:** exact finite SPI dual-norm/power-residue prefilter
