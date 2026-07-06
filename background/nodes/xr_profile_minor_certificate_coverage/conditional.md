# conditional: xr_profile_minor_certificate_coverage

## Predicate nodes

- `xr_triangular_minor_certificate_soundness`
- `xr_profile_minor_certificate_payload`

## Claim

Conditional on the uniform profile payload, every budget-meeting unpaid
non-boundary light profile has a nonzero maximal-minor specialization
certificate.

## Proof

The remaining predicate `xr_profile_minor_certificate_payload` supplies, for
each profile, one admissible payload record: triangular, monomial-certified,
or a complete remote table entry.

For triangular records, the proved node
`xr_triangular_minor_certificate_soundness` converts nonzero diagonal entries
into a nonzero determinant value. For monomial and remote-table records, the
payload directly asserts an admissible nonzero specialization. Therefore every
profile has the nonzero maximal-minor specialization required by this node.
