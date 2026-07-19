# conditional: e1_folded_certificate_cell_256_payload

## Predicate nodes

- `e1_pocklington_250bit_exhibit_field`
- `e1_named_field_folded_cell_certificate_soundness`
- `e1_folded_no_vector_certificate_256_payload`

## Conditional proof

The proved field node supplies the named prime field and primitive `256`th
root. The proved soundness node says that a named field/root plus a complete
zero no-vector certificate satisfies the E1 folded cell schema. The remaining
predicate `e1_folded_no_vector_certificate_256_payload` supplies exactly that
complete zero certificate for the `128` folded coordinates.

Therefore the `N'=256` cell payload holds once the no-vector payload is closed.
