# conditional: e1_folded_certificate_cell_128_payload

## Predicate nodes

- `e1_pocklington_250bit_exhibit_field`
- `e1_named_field_folded_cell_certificate_soundness`
- `e1_folded_no_vector_certificate_128_payload`

## Conditional proof

The proved field node supplies the named prime field and primitive `128`th
root. The proved soundness node says that a named field/root plus a complete
zero no-vector certificate satisfies the E1 folded cell schema. The remaining
predicate `e1_folded_no_vector_certificate_128_payload` supplies exactly that
complete zero certificate for the `64` folded coordinates.

Therefore the `N'=128` cell payload holds once the no-vector payload is closed.
