# xr_profile_minor_record_inventory_soundness

- **status:** PROVED
- **closure:** proof

## Statement

If an inventory covers every budget-meeting unpaid non-boundary
light-triangle profile and assigns each profile an admissible record of an
accepted nonzero-minor type, then `xr_profile_minor_certificate_payload`
holds.

Accepted record types are:

- triangular maximal-minor specializations with nonzero diagonal;
- monomial/noncancellation certificates for a named maximal minor; and
- complete remote certificate-table entries giving a nonzero maximal-minor
  specialization.

## Falsifier

A complete inventory of accepted nonzero-minor records while some required XR
profile lacks a valid payload record.
