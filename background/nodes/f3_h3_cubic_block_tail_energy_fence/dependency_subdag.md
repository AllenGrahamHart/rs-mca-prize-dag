# Dependency sub-DAG

```text
f3_h3_quotient_block_identity [PROVED]
  --req-->
f3_h3_cubic_block_tail_energy_fence [PROVED route fence]
  --ev--> f3_h3_mobius_excess_half [TARGET]
  --ev--> f3_h3_three_to_one_c36 [CONDITIONAL route ledger]

f3_h3_identity_deficit_energy_close [PROVED]
  --req--> f3_h3_cubic_block_tail_energy_fence
```

The open energy estimate is not introduced as a child. The fence removes one
insufficient marginal proof strategy and leaves the joint/truncated routes.
