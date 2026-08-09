# Audit

Run:

```bash
python3 verify.py
python3 verify_audit.py
```

The primary verifier checks all 80 candidate roots, 32 finite rows, 72
independent Frobenius profile visits, the exact nine-label set, and DAG
edges. The hostile audit rejects mutations of the candidate union, replay
terminal, audit custody, and sign-independent kernel.
