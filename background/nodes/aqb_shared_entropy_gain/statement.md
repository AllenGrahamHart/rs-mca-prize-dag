# aqb_shared_entropy_gain

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For the averaged `c=2` quotient-box family supplied by
`aqb_c2_average_family`, the shared-family entropy minus all charged box,
overlap, multiplicity, and quotient/fiber normalization costs is at least
`429,645,547` bits.

This is reduced to:

- `aqb_entropy_ledger_certificate_soundness`, which proves the monotone
  interval-ledger rule; and
- `aqb_shared_entropy_gain_payload`, which remains to provide the actual
  exact or interval-certified ledger for the concrete averaged family.

## Falsifier

A certified accounting of the proposed family whose net shared entropy gain is
below `429,645,547` bits.
