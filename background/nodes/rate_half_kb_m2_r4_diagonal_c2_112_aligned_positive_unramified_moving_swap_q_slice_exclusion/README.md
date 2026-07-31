# Replay

Run the fast contract and source audit:

```bash
python3 verify.py
python3 verify_audit.py
```

Run the exact certificate under the repository memory guard with a Python
environment containing `python-flint==0.9.0`:

```bash
tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 150s \
  /home/u2470931/.venvs/prize-flint/bin/python verify_exact.py
```

`verify_exact.py` applies an independent 60-second timeout to each of the
three serial algebraic stages. The source reconstruction stage is expected
to take most of that allowance.
