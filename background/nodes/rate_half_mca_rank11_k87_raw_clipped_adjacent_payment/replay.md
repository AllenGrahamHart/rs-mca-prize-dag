# Replay

Given the captures named in `source_contract.json`, run:

```text
python3 experiments/prize_resolution/rate_half_mca_rank11_k87_ordinary_check.py \
  /tmp/k87-ordinary.jsonl \
  --sha256 06a550c1f65be3c2a7c4d96590188f5de6ca792c1f87e638f2fa7d5163b43519
python3 experiments/prize_resolution/rate_half_mca_rank11_k87_raw_threshold_wave_check.py \
  /tmp/k87-raw-threshold-wave.jsonl \
  --sha256 2722d7811cf29e425bd67fd49a46f586efe2f21c0dda698e369dcfe4fd48b449
python3 experiments/prize_resolution/rate_half_mca_rank11_k87_clipped_wave_check.py \
  /tmp/k87-clipped-wave-combined.jsonl \
  --sha256 6f8064320850e0009c18c967e2b61ec5b4d77c51e1c2afb4bee6fc41921e5cd8
python3 experiments/prize_resolution/rate_half_mca_rank11_k87_component_payment.py
```

The compact node verifiers do not require raw captures; they check pinned
custody, finite coverage identities, raw-clipped theorem dependency, and the
exact row arithmetic.
