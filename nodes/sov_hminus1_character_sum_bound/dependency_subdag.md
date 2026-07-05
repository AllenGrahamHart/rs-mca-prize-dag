# dependency sub-DAG: sov_hminus1_character_sum_bound

```text
sov_nonconstant_affine_character_cancellation [PROVED]
    -> sov_hminus1_character_sum_bound [CONDITIONAL]
    -> sov_hminus1_coefficient_distribution [CONDITIONAL]

sov_hminus1_affine_piece_decomposition [CONDITIONAL]
    -> sov_affine_piece_partition_payload [TARGET]
    -> sov_hminus1_character_sum_bound [CONDITIONAL]
    -> sov_hminus1_coefficient_distribution [CONDITIONAL]
    -> sov_first_obstruction_value_distribution [CONDITIONAL]
    -> sov_obstruction_equidistribution [CONDITIONAL]

sov_hminus1_fiber_fourier_duality [PROVED]
    -> sov_hminus1_coefficient_distribution [CONDITIONAL]
```

The formal affine-piece cancellation is proved. The project-specific
analytic/combinatorial input is now the affine/paid-piece decomposition of
the actual conditioned anchored-core families.
