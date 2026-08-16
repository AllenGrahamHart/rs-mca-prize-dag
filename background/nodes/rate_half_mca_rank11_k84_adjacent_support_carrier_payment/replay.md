# Replay

Given the two raw captures named in `source_contract.json`, run:

```text
python3 experiments/prize_resolution/rate_half_mca_rank11_k84_threshold_batch_check.py \
  /tmp/k84-primary-full-route-wave.jsonl \
  /tmp/k84-audit-full-route-wave.jsonl
```

Then run the exact component arithmetic:

```text
python3 experiments/prize_resolution/rate_half_mca_rank11_k84_component_payment.py
```

The compact node verifiers do not require external raw captures; they check
their pinned hashes, theorem custody, coverage contract, and exact row
arithmetic.
