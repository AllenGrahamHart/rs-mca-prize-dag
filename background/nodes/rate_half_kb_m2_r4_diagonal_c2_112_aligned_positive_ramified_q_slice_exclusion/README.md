# Replay

Run the contract and independent audit first, then each exact CAS shard
separately:

```bash
python3 verify.py
python3 verify_audit.py
python3 verify_fixed_same.py
python3 verify_fixed_swap.py
python3 verify_fixed_mixed.py
python3 verify_moving_same.py
python3 verify_moving_swap.py
python3 verify_moving_mixed.py
```

The six saturation shards each reconstruct their own ideal and must run
under the repository's `ramguard tiny` and 60-second process boundary.
