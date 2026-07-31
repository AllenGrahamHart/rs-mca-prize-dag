# Replay

Run each exact shard separately under the repository resource policy:

```bash
python3 verify.py
python3 verify_audit.py
python3 verify_template.py
python3 verify_xi_a.py
python3 verify_xi_tau.py
python3 verify_xi_other.py
```

The three branch shards replay both the characteristic-zero projection/fiber
certificate and the direct deployed-prime forbidden saturation.
