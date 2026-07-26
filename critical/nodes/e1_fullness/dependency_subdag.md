# dependency sub-DAG: e1_fullness

Promoted subclaims.

```text
collision_norm_criterion [PROVED]
kernel_lattice_reframing [PROVED]
graded_collision_radius [PROVED]
are_exceptional_density [PROVED]
    -> e1_exceptional_set_reduction [PROVED]

official_row_primes_pinning [PROVED]
    --evidence--> e1_official_prime_exception_control [TARGET]

e1_exceptional_set_reduction [PROVED]
e1_official_prime_exception_control [TARGET]
    -> e1_fullness [CONDITIONAL]
e1_fullness [CONDITIONAL]
    -> zone_b [CONDITIONAL]
```

## e1_exceptional_set_reduction

Status: PROVED. This packages the norm-divisor reduction, sparse-kernel
reframing, small-radius exclusion, and almost-all-primes density statement.

## e1_official_prime_exception_control

Statement: every admissible prize row meets the exceptional norm-divisor
budget required by `e1_fullness`.

Status: TARGET. The former two-cell named-exhibit certificate branch did not
cover the universal prize quantifier and now lives in `background/nodes/` with
evidence-only edges. A folded-lattice route can close this target only through
a theorem or certifier covering every admissible input.
