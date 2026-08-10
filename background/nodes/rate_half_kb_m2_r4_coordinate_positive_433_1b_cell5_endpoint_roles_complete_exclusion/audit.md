# Audit

Run:

```bash
python3 verify.py
python3 verify_audit.py
```

The hostile audit rejects a dropped eliminant row, a nontrivial root gcd, a replayed base-field root, and a sign-dependent kernel mutation. Reviewers should confirm that the source compatibility cut is necessary before any pairing-dependent target equations are introduced.
