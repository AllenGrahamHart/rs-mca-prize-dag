# xr_profile_eliminant_nonvanishing

- **status:** CONDITIONAL
- **closure:** conditional

## Statement

For every budget-meeting light-triangle profile not already paid or boundary,
the normal-form matrix from `xr_triangle_eliminant_form` has at least one
maximal minor that is a nonzero polynomial in the profile coordinates.
Equivalently, there is no unpaid light profile on which the eliminant vanishes
identically.

This is now decomposed into the proved certificate-semantics node
`xr_minor_specialization_certificate_semantics` and the remaining coverage
node `xr_profile_minor_certificate_coverage`.

## Falsifier

A budget-meeting unpaid light profile for which no admissible nonzero
maximal-minor specialization can be produced.
