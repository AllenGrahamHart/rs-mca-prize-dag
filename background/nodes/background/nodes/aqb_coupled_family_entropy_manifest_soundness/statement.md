# aqb_coupled_family_entropy_manifest_soundness

- **status:** PROVED
- **closure:** proof

## Statement

Suppose a coupled AQB manifest at `sigma* = 8,592,912,738` supplies:

- the `c=2` averaged-family certificate fields required by
  `aqb_family_certificate_semantics`;
- exact or interval-certified entropy ledger entries required by
  `aqb_entropy_ledger_certificate_soundness`;
- a check that the ledger is keyed to the same family members, shared
  quotient/fiber data, and reusable charge data; and
- certified net gain at least `429,645,547` bits.

Then both payloads hold:

- `aqb_c2_family_certificate_payload`;
- `aqb_shared_entropy_gain_payload`.

## Falsifier

A verified coupled manifest that satisfies the family schema and ledger
threshold but fails either AQB payload.
