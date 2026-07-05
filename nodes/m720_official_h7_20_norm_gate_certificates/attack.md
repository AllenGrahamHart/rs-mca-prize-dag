# ATTACK - m720_official_h7_20_norm_gate_certificates

This is now an assembly node. Do not route it through the broad
`h4_sparse_norm_gate` / `a_closure_assembly` chain, because that chain depends
downstream on `midlarge_h_certification`, which consumes
`m720_official_exclusion`.

The payload soundness rule is proved in
`m720_official_norm_gate_certificate_soundness`.

Acceptable closures:

- prove `m720_official_h7_20_norm_gate_payload`: either a uniform
  admissible-family nonvanishing theorem for the h=7..20 norm-gate
  obstructions, or complete named-exhibit certificates excluding every unpaid
  non-toral primitive norm-gate core in h=7..20.

Calibration scans and complete small-row certificates are evidence only unless
they transfer to the official rows by a proof-grade argument.

There is no hidden list of official row primes to recover; see
`official_row_primes_pinning`.
