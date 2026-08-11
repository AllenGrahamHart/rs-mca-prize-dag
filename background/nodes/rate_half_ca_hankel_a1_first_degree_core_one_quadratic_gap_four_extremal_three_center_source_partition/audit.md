# Audit

1. `U` is the joint support of the residual word pair, not merely a padded
   locator union.
2. The core is removed before counting missing coordinates, giving
   `|M_gamma|=p-1+r_gamma` rather than `p+r_gamma`.
3. Pairwise disjointness uses only that a nonzero projective linear form has
   one root; no characteristic-dependent affine normalization is used.
4. The leftover count is exactly `1-d_A`, and Cycle 127 already proves
   `d_A<=1`.
5. The source factors in `(ESP7)` retain arbitrary nonzero coordinate
   scalars; no unjustified equality of error values is asserted.
