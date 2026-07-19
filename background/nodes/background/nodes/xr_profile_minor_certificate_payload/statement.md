# xr_profile_minor_certificate_payload

- **status:** CONDITIONAL
- **closure:** proof or certificate

## Statement

For every budget-meeting unpaid non-boundary light-triangle profile, provide
one of the following admissible payload records:

- a triangular maximal-minor specialization with nonzero diagonal;
- a monomial/noncancellation certificate proving a named maximal minor
  specializes nonzero; or
- a complete remote certificate-table record giving a nonzero maximal-minor
  specialization.

This is reduced to:

- `xr_profile_minor_record_inventory_soundness`, which proves that a complete
  inventory of accepted nonzero-minor records implies this payload; and
- `xr_profile_minor_record_inventory_payload`, which remains to construct the
  actual inventory over all budget-meeting unpaid non-boundary light profiles.

## Falsifier

A budget-meeting unpaid non-boundary light profile with no payload record, an
inadmissible specialization, or a payload whose specialized determinant is
zero.
