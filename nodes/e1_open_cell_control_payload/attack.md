# ATTACK - e1_open_cell_control_payload

This node is now conditional. The live E1 leaves are
`e1_folded_certificate_cell_128_payload` and
`e1_folded_certificate_cell_256_payload`.

Two routes are acceptable:

- prove uniform admissible-family typicality for the explicit norm-divisor
  exceptional set in the cells `N' in {128,256}`;
- or provide complete folded-lattice certificates for named exhibit fields in
  those cells, with no nonzero non-cyclotomic folded vector.

The selected route is the second one. It may use
`e1_folded_certificate_soundness`, but the actual certificates must be
complete for the named fields. The toy `N'=16` folded check is not enough.

There is no hidden list of official row primes to recover; any certificate
must be either family-uniform or tied to an explicitly named exhibit field.
