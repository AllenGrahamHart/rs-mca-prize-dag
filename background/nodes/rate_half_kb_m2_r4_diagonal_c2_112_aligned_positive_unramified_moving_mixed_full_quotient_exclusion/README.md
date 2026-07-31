# Replay

```bash
python3 verify.py
python3 verify_audit.py

tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python verify_exhaustive.py

tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python verify_survivors.py

tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python verify_exact.py
```

The three exact commands are separated because exhaustive regeneration and
independent equation reconstruction each use most of the mandatory local
60-second wall allowance.
