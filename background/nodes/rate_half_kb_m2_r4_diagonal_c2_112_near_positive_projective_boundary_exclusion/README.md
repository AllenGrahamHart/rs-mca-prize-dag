# Replay

Run the contract and independent projective audit, then each saturation
shard separately:

```bash
python3 verify.py
python3 verify_audit.py
python3 verify_fixed_a.py
python3 verify_fixed_tau.py
python3 verify_fixed_other.py
python3 verify_moving_a.py
python3 verify_moving_tau.py
python3 verify_moving_other_plus.py
python3 verify_moving_other_minus.py
```

Every saturation process must use the repository's `ramguard tiny` and
60-second boundary.
