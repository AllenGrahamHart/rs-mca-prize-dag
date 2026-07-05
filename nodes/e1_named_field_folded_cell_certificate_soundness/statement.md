# e1_named_field_folded_cell_certificate_soundness

- **status:** PROVED
- **closure:** proof

## Statement

For each `N' in {128,256}`, if:

- `e1_pocklington_250bit_exhibit_field` supplies a prime field `F_p` with
  `p = 1 mod N'` and a primitive `N'`th root;
- the corresponding no-vector payload supplies a complete folded-kernel
  certificate over that named field; and
- the certificate records zero nonzero non-cyclotomic folded vectors;

then `e1_folded_certificate_cell_N_payload` holds for that cell.

## Falsifier

A named prime field and complete zero no-vector certificate for a cell while
the cell payload still fails.
