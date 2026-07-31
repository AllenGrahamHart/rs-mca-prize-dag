# Replay

```bash
python3 verify.py
python3 verify_audit.py

tools/ramguard tiny -- timeout --foreground --signal=TERM --kill-after=5s 150s \
  /home/u2470931/.venvs/prize-flint/bin/python verify_exact.py
```

The exact wrapper runs three serial stages, each with its own 60-second cap.
