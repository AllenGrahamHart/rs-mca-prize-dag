# proof: e22_lower_scale_intersection_profile_counts

Fix a dyadic pair `M_i<M_j` and a subset `S` of smaller dyadic scales.

The proved node `e22_residual_profile_generating_function` supplies the raw
residual-profile universe for canonical scale-`M_i` data that are
raw-admissible at `M_j`. The proved node
`e22_lower_scale_intersection_formula_payload` supplies, for this same pair
and subset, a finite dyadic-tree coefficient formula whose atoms are in
bijection with exactly the profiles in that universe that are also admissible
at every scale in `S`.

The atom weights in that formula are the weights assigned by the proved
`dyadic_profile_evaluation` convention. Therefore
`e22_weighted_intersection_certificate_soundness` applies directly: a finite
formula with a verified bijection to the profile set and matching weights
gives the exact weighted intersection count.

Since the construction is uniform in `M_i`, `M_j`, and `S`, all lower-scale
intersection counts needed by `e22_lower_scale_filter_inclusion_exclusion`
are known.
