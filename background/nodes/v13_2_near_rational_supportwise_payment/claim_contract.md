# Claim contract

- **Status:** REFUTED.
- **Claim tested:** two near-rational slopes plus `n-3w>=m` eliminate all
  support-wise MCA-bad slopes.
- **Literal falsifier:** one line satisfying the source hypotheses with two
  low-`d1`, nonzero-census slopes and at least one support-wise MCA-bad slope.
- **Witness:** the exact rate-half `mu_8 subset F_17` row in
  `refutation.md`; in fact both low-`d1` slopes are MCA-bad.
- **Retained theorem:** `v13_2_near_rational_pair_proximity` proves common
  pair proximity on `n-2w` coordinates.
- **Stronger falsifier:** the smooth `mu_16 subset F_17` witness has two bad
  slopes while every line word is within distance `w=2` of the zero
  codeword, so it refutes the printed `+1` inequality itself.
- **Replacement:**
  `v13_2_near_rational_supportwise_two_anchor_payment` proves the corrected
  uniform charge `2w` under `w>=1` and `3w<=n-K`.
