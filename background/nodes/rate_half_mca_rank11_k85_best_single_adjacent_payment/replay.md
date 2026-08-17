# Replay

Given the raw captures named in `source_contract.json`, run:

```text
python3 experiments/prize_resolution/rate_half_mca_rank11_k85_route_pilot_check.py \
  /tmp/k85-adjacent-support-route-pilot.jsonl
python3 experiments/prize_resolution/rate_half_mca_rank11_k85_raw_threshold_wave_check.py \
  /tmp/k85-raw-threshold-wave-v3.jsonl
python3 experiments/prize_resolution/rate_half_mca_rank11_k85_best_single_wave_check.py \
  /tmp/k85-best-single-wave-v2.jsonl \
  --sha256 a2a47722b66ff40ed83b44c47dc725b341700ffc2c9653a61e63f7dff1fedfa8
```

Then run the exact component arithmetic:

```text
python3 experiments/prize_resolution/rate_half_mca_rank11_k85_component_payment.py
```

The compact node verifiers do not require raw captures; they check pinned
custody, finite coverage identities, and the exact row arithmetic.
