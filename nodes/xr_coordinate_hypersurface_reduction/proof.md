# proof: xr_coordinate_hypersurface_reduction

The proved node `xr_triangle_eliminant_form` constructs the determinantal
normal form for a light-triangle profile. In that form, rank stagnation is
equivalent to the vanishing of the relevant maximal minors of the stacked
twisted-sum matrix.

Fix a profile for which at least one such minor is a nonzero polynomial in the
aligned-support coordinates. The coordinate-special stagnation locus is
contained in the zero set of that nonzero polynomial. Since the polynomial is
nonzero in the coordinate ring of the profile chart, its zero set is a proper
hypersurface. Its degree is bounded by the degree of the determinantal minor,
which is fixed by the normal-form construction.

Therefore nonzero profile eliminants reduce coordinate-special stagnation to a
proper bounded-degree hypersurface, as claimed.
