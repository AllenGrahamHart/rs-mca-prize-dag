# ATTACK - aqb_c2_average_family

This is now an assembly node. Do not run broad local searches.

The old target was an explicit averaged family, not a count of one floor word.
That obligation has been moved to `aqb_c2_family_certificate_payload`.

Current reduction:

- `aqb_family_certificate_semantics` proves that a verified finite certificate
  with member parametrization, shared quotient/fiber data, reusable charge, and
  transfer maps implies this family predicate;
- `aqb_c2_family_certificate_payload` must provide the actual certificate.

Further work should happen at `aqb_c2_family_certificate_payload`, unless the
certificate semantics are found defective.
