# aqb_family_certificate_semantics

- **status:** PROVED
- **closure:** proof

## Statement

Suppose an AQB `c=2` averaged-family certificate at
`sigma* = 8,592,912,738` supplies:

- a finite nonempty member set;
- a map from every member into the `c=2` quotient-box geometry at `sigma*`;
- shared quotient/fiber data used by all members;
- reusable box-charge data that is not paid independently for every member;
- a transfer map from every member to the list witness used by the AQB
  average-to-member argument.

If the certificate predicates verify these fields, then
`aqb_c2_average_family` holds.

## Falsifier

A verifying certificate with an empty family, a member outside the `c=2`
quotient-box geometry at `sigma*`, missing shared quotient/fiber data, or no
member-to-witness transfer.
