# ATTACK - e1_official_prime_exception_control

Status: conditional. Use light local computation only.

The folded-certificate soundness is proved in
`e1_folded_certificate_soundness`. The old active leaf
`e1_official_typicality_or_certificate` is now conditional. The manifest
assembly has also been split, so the live leaves are
`e1_folded_no_vector_certificate_128_payload` and
`e1_folded_no_vector_certificate_256_payload`. The common field/root data is
already proved.

Possible proof routes:

- certify named exhibit fields directly with the folded lattice/kernel
  procedure described by `kernel_lattice_reframing`,
  `integer_code_distance_cert`, and `lattice_cone_certificate`.

Do not promote from birthday-scan evidence alone; the scans are useful
falsification attempts but not a proof of admissible-family avoidance of the
exceptional set.

There is no hidden list of official row primes to recover; see
`official_row_primes_pinning`.
