# Replay

Run the lightweight contract and independent audits with:

```bash
python3 verify.py
python3 verify_audit.py
python3 verify_source.py
```

The 22 minus-branch saturation shards are `verify_classify00.py` through
`verify_classify21.py`. The terminal sextic shard first eliminates `b` by
the reciprocal-quadratic branch and replays the resulting two-variable
saturation. Full projection regeneration requires
`python-flint==0.9.0`; run the hash-pinned helper modes through
`verify_runner.py` or the source scripts under a 60-second process bound.
