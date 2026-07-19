# aqb_c2_average_family

- **status:** CONDITIONAL
- **closure:** proof

## Statement

There exists an averaged family over the `c=2` quotient-box geometry at
`sigma* = 8,592,912,738` whose members share enough quotient structure for
their list contributions to be averaged before paying the full box charge
separately for each member.

This node is reduced to:

- `aqb_family_certificate_semantics`, the proved rule that a verified
  averaged-family certificate implies this family-existence predicate; and
- `aqb_c2_family_certificate_payload`, the remaining concrete certificate for
  the actual `c=2` family.

## Falsifier

A structural theorem showing that every admissible `c=2` quotient-box family
at `sigma*` decomposes into single-word boxes with no nontrivial shared
quotient charge, or a defect in the certificate semantics.
