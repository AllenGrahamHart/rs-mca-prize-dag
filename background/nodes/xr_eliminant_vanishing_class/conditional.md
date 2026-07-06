# conditional: xr_eliminant_vanishing_class

## Predicate nodes

- `xr_profile_eliminant_nonvanishing`
- `xr_coordinate_hypersurface_reduction`

## Claim

Conditional on profile nonvanishing, the old identically-vanishing light
configuration class is eliminated, and the remaining coordinate-special
vanishing is reduced to a proper hypersurface.

## Proof

The proved node `xr_triangle_eliminant_form` supplies the normal-form matrix
and eliminant polynomial for light-triangle rank stagnation.

The predicate `xr_profile_eliminant_nonvanishing` says that, for every
budget-meeting light profile not already paid or boundary, at least one
maximal minor of that normal-form matrix is a nonzero polynomial. Therefore no
unpaid profile is identically vanishing.

The proved predicate `xr_coordinate_hypersurface_reduction` then applies:
inside each nonzero profile, coordinate-special vanishing is the zero set of a
nonzero bounded-degree eliminant polynomial, hence a proper hypersurface in
the aligned-support chart.

Thus the original structured-branch danger, an identically vanishing unpaid
light profile class, is gone. The remaining proper-hypersurface population is
the rationing problem already routed through `deep_link_staircase` in
`xr_light_triangle_eliminant`.
