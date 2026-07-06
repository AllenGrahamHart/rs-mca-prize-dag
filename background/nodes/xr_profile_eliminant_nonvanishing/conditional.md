# conditional: xr_profile_eliminant_nonvanishing

## Predicate nodes

- `xr_triangle_eliminant_form`
- `xr_minor_specialization_certificate_semantics`
- `xr_profile_minor_certificate_coverage`

## Claim

Conditional on uniform minor-certificate coverage, every budget-meeting unpaid
non-boundary light-triangle profile has a nonzero profile eliminant.

## Proof

The proved node `xr_triangle_eliminant_form` supplies the MDS normal-form
matrix and identifies rank stagnation with the vanishing of all maximal minors
in the relevant profile chart.

The predicate `xr_profile_minor_certificate_coverage` supplies, for each
budget-meeting unpaid non-boundary light profile, a maximal minor and an
admissible chart specialization at which that determinant is nonzero.

The proved node `xr_minor_specialization_certificate_semantics` converts each
such certificate into the desired algebraic statement: the named maximal minor
is not the zero polynomial on the profile chart. Therefore not all maximal
minors vanish identically on that profile.

Thus no budget-meeting unpaid non-boundary light profile has identically
vanishing eliminant, which proves `xr_profile_eliminant_nonvanishing`
conditional on the coverage node.
