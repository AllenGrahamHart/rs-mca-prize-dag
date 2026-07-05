# xr_triangular_minor_certificate_soundness

- **status:** PROVED
- **closure:** proof

## Statement

For an XR light-profile normal-form matrix, suppose a certificate selects a
maximal square minor and an admissible chart specialization such that the
specialized minor matrix is triangular and every diagonal entry is nonzero.

Then the determinant at that specialization is nonzero, so the certificate is
a valid nonzero-minor specialization certificate for
`xr_minor_specialization_certificate_semantics`.

## Falsifier

A triangular specialized minor with every diagonal entry nonzero but
determinant zero.
