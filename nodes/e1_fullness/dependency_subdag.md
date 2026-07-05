# dependency sub-DAG: e1_fullness

Promoted subclaims.

```text
collision_norm_criterion [PROVED]
kernel_lattice_reframing [PROVED]
graded_collision_radius [PROVED]
are_exceptional_density [PROVED]
    -> e1_exceptional_set_reduction [PROVED]

e1_folded_certificate_soundness [PROVED]
    -> e1_open_cell_route_soundness [PROVED]
    -> e1_official_typicality_or_certificate [CONDITIONAL]
    -> e1_official_prime_exception_control

official_row_primes_pinning [PROVED]
    -> e1_open_cell_route_soundness [PROVED]

e1_two_cell_folded_manifest_assembly_soundness [PROVED]
    -> e1_folded_certificate_manifest_payload [CONDITIONAL]

e1_pocklington_250bit_exhibit_field [PROVED]
    -> e1_folded_certificate_cell_128_payload [CONDITIONAL]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]

e1_named_field_folded_cell_certificate_soundness [PROVED]
    -> e1_folded_certificate_cell_128_payload [CONDITIONAL]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]

e1_folded_no_vector_certificate_128_payload [TARGET]
    -> e1_folded_certificate_cell_128_payload [CONDITIONAL]

e1_folded_no_vector_certificate_256_payload [TARGET]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]

e1_folded_certificate_cell_128_payload [CONDITIONAL]
    -> e1_folded_certificate_manifest_payload [CONDITIONAL]

e1_folded_certificate_cell_256_payload [CONDITIONAL]
    -> e1_folded_certificate_manifest_payload [CONDITIONAL]

e1_folded_certificate_manifest_payload [CONDITIONAL]
    -> e1_open_cell_control_payload [CONDITIONAL]
    -> e1_official_typicality_or_certificate [CONDITIONAL]
    -> e1_official_prime_exception_control

e1_open_cell_control_payload [CONDITIONAL]
    -> e1_official_typicality_or_certificate [CONDITIONAL]
    -> e1_official_prime_exception_control

e1_official_prime_exception_control [CONDITIONAL]
    -> e1_fullness
    -> zone_b
```

## e1_exceptional_set_reduction

Status: PROVED. This packages the norm-divisor reduction, sparse-kernel
reframing, small-radius exclusion, and almost-all-primes density statement.

## e1_official_prime_exception_control

Statement: the admissible prize row primes avoid the exceptional norm-divisor
set at the needed density, or can be certified individually by the folded
lattice procedure.

Status: CONDITIONAL. Folded-certificate soundness, route soundness, and
two-cell manifest assembly are proved. The common field/root data is also
proved. The remaining leaves are
`e1_folded_no_vector_certificate_128_payload` and
`e1_folded_no_vector_certificate_256_payload`: print complete no-vector folded
certificates for the two open cells.

The per-prime folded lattice certificate route remains an attack route inside
this predicate rather than a separate wired requirement, because it is an
alternative to proving typicality of the official primes.
