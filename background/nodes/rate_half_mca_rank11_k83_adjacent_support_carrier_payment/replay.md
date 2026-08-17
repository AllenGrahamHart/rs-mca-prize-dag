# Replay

Given the four raw captures named in `source_contract.json`, run:

```text
python3 experiments/prize_resolution/rate_half_mca_rank11_k83_threshold_batch_check.py \
  /tmp/k83-threshold-adjacent-pilot.jsonl \
  /tmp/k83-threshold-adjacent-wave-a.jsonl \
  /tmp/k83-threshold-adjacent-wave-a-repair.jsonl \
  /tmp/k83-threshold-adjacent-wave-b.jsonl
```

The compact node verifiers do not require those external raw captures; they
check their pinned hashes, theorem custody, coverage contract, and exact row
arithmetic.
