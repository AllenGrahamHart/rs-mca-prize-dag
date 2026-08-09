# Audit

Run:

```bash
python3 verify.py
python3 verify_audit.py
```

The primary verifier checks all artifact hashes, eight eliminants, exact
agreement between factorization and Frobenius roots, 16 incompatible tower
lifts, and the 30-label scope. The hostile audit independently reconstructs
the quadratic lifts and rejects dropped rows, changed roots, invented
compatible points, and a sign-dependent kernel.
