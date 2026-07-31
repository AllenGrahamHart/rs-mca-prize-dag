# Replay

```bash
python3 verify.py
python3 verify_audit.py

tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python verify_linear.py

tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python verify_exhaustive.py

tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 60s \
  /home/u2470931/.venvs/prize-flint/bin/python verify_exact.py
```

The exact commands are separated so each remains inside the mandatory local
60-second wall and RAM limits.
