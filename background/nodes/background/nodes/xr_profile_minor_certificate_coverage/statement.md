# xr_profile_minor_certificate_coverage

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For every budget-meeting unpaid non-boundary light-triangle profile, produce a
maximal minor of the normal-form matrix from `xr_triangle_eliminant_form` and
an admissible specialization of the profile chart at which that determinant is
nonzero.

Combined with `xr_minor_specialization_certificate_semantics`, these
certificates imply `xr_profile_eliminant_nonvanishing`.

This is reduced to:

- `xr_triangular_minor_certificate_soundness`, which proves one accepted
  payload format; and
- `xr_profile_minor_certificate_payload`, which reduces uniform coverage to
  the actual profile record-inventory payload.

## Falsifier

A budget-meeting unpaid non-boundary light-triangle profile for which every
maximal minor vanishes at every admissible specialization.
