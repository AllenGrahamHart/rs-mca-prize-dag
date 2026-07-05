# dependency sub-DAG: sov_hminus1_affine_piece_decomposition

Edges are directed from dependency to consumer.

```text
sov_affine_piece_partition_certificate_soundness [PROVED]
    -> sov_hminus1_affine_piece_decomposition [CONDITIONAL]
    -> sov_hminus1_character_sum_bound [CONDITIONAL]

sov_nonconstant_affine_character_cancellation [PROVED]
    -> sov_hminus1_character_sum_bound [CONDITIONAL]

sov_affine_piece_partition_payload [TARGET]
    -> sov_hminus1_affine_piece_decomposition [CONDITIONAL]
```

The open node is now the SOV affine-piece partition payload for actual
anchored-core conditioning cells.
