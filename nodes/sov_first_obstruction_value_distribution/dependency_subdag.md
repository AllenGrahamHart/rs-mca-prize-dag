# dependency sub-DAG: sov_first_obstruction_value_distribution

Edges are directed from dependency to consumer.

```text
sov_first_obstruction_sensitivity [PROVED]
    -> sov_first_obstruction_value_distribution

sov_nonconstant_affine_character_cancellation [PROVED]
    -> sov_hminus1_character_sum_bound
    -> sov_hminus1_coefficient_distribution
    -> sov_first_obstruction_value_distribution
    -> sov_obstruction_equidistribution

sov_hminus1_affine_piece_decomposition
    -> sov_hminus1_character_sum_bound
    -> sov_hminus1_coefficient_distribution
    -> sov_first_obstruction_value_distribution
    -> sov_obstruction_equidistribution

sov_hminus1_fiber_fourier_duality [PROVED]
    -> sov_hminus1_coefficient_distribution
```

## Status

- `sov_first_obstruction_sensitivity`: PROVED. The obstruction is an affine
  translate of the `h-1` locator coefficient on forced-root fibers.
- `sov_hminus1_coefficient_distribution`: CONDITIONAL. The finite-Fourier
  fiber reduction is proved.
- `sov_nonconstant_affine_character_cancellation`: PROVED.
- `sov_hminus1_character_sum_bound`: CONDITIONAL.
- `sov_affine_piece_partition_payload`: TARGET. This is the remaining
  anchored-core affine/paid-piece decomposition theorem.
- `sov_first_obstruction_value_distribution`: CONDITIONAL.
