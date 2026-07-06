# aqb_shared_entropy_gain_payload

- **status:** CONDITIONAL
- **closure:** proof or certificate

## Statement

For the averaged `c=2` quotient-box family supplied by
`aqb_c2_average_family`, provide exact or interval-certified ledger entries
for:

- shared-family entropy;
- charged box entropy;
- overlap and multiplicity normalization;
- quotient/fiber normalization;

such that the certified net lower bound is at least `429,645,547` bits.

This is reduced to:

- `aqb_coupled_family_entropy_manifest_soundness`, the proved rule that a
  coupled family-plus-ledger manifest supplies the entropy payload; and
- `aqb_coupled_family_entropy_manifest_payload`, the remaining actual coupled
  AQB manifest.

## Falsifier

A missing ledger component, an interval with the wrong rounding direction, or
a certified net lower bound below `429,645,547` bits.
