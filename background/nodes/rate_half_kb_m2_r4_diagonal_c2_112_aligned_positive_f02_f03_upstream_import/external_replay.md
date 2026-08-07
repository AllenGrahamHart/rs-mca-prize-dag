# External replay

Repository: `https://github.com/przchojecki/rs-mca`

Commit: `826c0e7610604d550b8dd9b772c197a4e660e525`

Command, run in a detached worktree containing that commit:

```text
python3 experimental/scripts/verify_kb_mca_v4_m2_aligned_positive_f02_f03_deletion_v1.py --check --tamper-selftest
```

Output:

```text
PASS: F02/F03 deletion cells=3 payload=51572f4d190a3bceb31494ae7ee48f6b026346413ae398d2da4f7b1da1402438
PASS: fail-closed semantic mutations 26/26
```

The upstream theorem note states that a fresh reviewer also replayed the
load-bearing Sage compiler and both Python modes. This local import did not
rerun Sage.
