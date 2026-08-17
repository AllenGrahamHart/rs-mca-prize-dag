# Replay

Given the captures named in `source_contract.json`, run:

```text
python3 experiments/prize_resolution/rate_half_mca_rank11_k86_ordinary_slice_check.py \
  /tmp/k86-adjacent-support-route-pilot.jsonl \
  --sha256 d343b18cfef00d6a1dff8634a2ffe8b8574d25a59cf44f43d4c3862e47c8a4d8
python3 experiments/prize_resolution/rate_half_mca_rank11_k86_raw_threshold_wave_check.py \
  /tmp/k86-raw-threshold-wave.jsonl \
  --sha256 7aa3c934e610aa717ba25b8b7acf424c0f59ad068ec294eac5b448d9abb81612
python3 experiments/prize_resolution/rate_half_mca_rank11_k86_best_single_wave_check.py \
  /tmp/k86-best-single-wave.jsonl \
  --sha256 bc67b9fa9ffa6b386d5d5f9e053e2d5a99a8451f2e9ae8d03c0095cc6f867349
```

Then run the exact component arithmetic:

```text
python3 experiments/prize_resolution/rate_half_mca_rank11_k86_component_payment.py
```

The compact node verifiers do not require raw captures; they check pinned
custody, finite coverage identities, and the exact row arithmetic.
