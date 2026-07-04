# Conditional proof: light-triangle eliminant

Status: CONDITIONAL on `deep_link_staircase` and
`xr_eliminant_vanishing_class`.

The proved `xr_triangle_eliminant_form` gives the promised closed normal form:
for a light triple, stagnation is the rank-jump locus of the explicit sum-map
matrix in MDS coordinates.

That leaves the standard dichotomy:

- if the eliminant is nonzero on the profile cell, the intersection of the
  aligned-support variety with that proper locus must be rationed; this is the
  deep-link staircase/rationing input;
- if the eliminant vanishes structurally, the configuration must be classified
  as paid or separately rationed by `xr_eliminant_vanishing_class`.

Therefore the light-triangle residual follows from the proved eliminant normal
form plus those two branch predicates.  It is not an independent red node once
those predicates are admitted.
