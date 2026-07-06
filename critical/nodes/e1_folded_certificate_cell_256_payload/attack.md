# ATTACK - e1_folded_certificate_cell_256_payload

This cell is no longer a primitive leaf: the field-selection part is proved,
and the remaining live leaf is
`e1_folded_no_vector_certificate_256_payload`.

Needed output:

- provide a complete transcript or proof-logged certificate for the folded
  `128`-coordinate search;
- prove the transcript excludes every nonzero vector in `{-2,...,2}^{128}` in
  the kernel, except the cyclotomic zero-folding relation; and
- keep the certificate machine-checkable without running a broad local WSL
  enumeration.

The exact field and primitive root are fixed by
`e1_pocklington_250bit_exhibit_field`. The toy `N'=16` folded replay and the
Modal launcher are format evidence only. They do not close this cell.
