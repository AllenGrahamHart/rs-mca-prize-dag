# dependency sub-DAG: sov_hminus1_coefficient_distribution

```text
sov_hminus1_fiber_fourier_duality [PROVED]
    -> sov_hminus1_coefficient_distribution [CONDITIONAL]
    -> sov_first_obstruction_value_distribution [CONDITIONAL]

sov_nonconstant_affine_character_cancellation [PROVED]
    -> sov_hminus1_character_sum_bound [CONDITIONAL]
    -> sov_hminus1_coefficient_distribution [CONDITIONAL]

sov_hminus1_affine_piece_decomposition [CONDITIONAL]
    -> sov_affine_piece_partition_payload [TARGET]
    -> sov_hminus1_character_sum_bound [CONDITIONAL]
    -> sov_hminus1_coefficient_distribution [CONDITIONAL]
```

The old coefficient-distribution leaf has been split into:

- a generic finite-Fourier inversion lemma, now proved; and
- a generic affine-piece cancellation lemma, now proved; and
- the actual anchored-core affine/paid-piece decomposition theorem, still
  open.
