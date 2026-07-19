# Proof And Replay Certificate

`tools/run_all_verifiers.py` supplies four fail-closed layers:

1. discovery scans both node partitions and the top-level verifier tools;
2. the manifest must have exactly the discovered local/remote partition;
3. every verifier and adjacent statement/proof/conditional asset must match
   its recorded SHA-256 hash;
4. every executable verifier must return zero before the replay is complete.

The self-test constructs a temporary proof node and checks that each of six
mutations is rejected: missing manifest entry, stale entry, verifier tamper,
proof tamper, nonzero exit, and timeout. Thus the checker does not pass merely
because discovery is empty or because subprocess failures are ignored.

The full run was dispatched to Modal to avoid loading WSL:

```text
app: ap-LSUBiGJOwxv1kbJyD6YDVQ
manifest SHA-256: 529ce4599832e03e7297702bd9968d51a8fe6d9ea029150c7270265a4e1c60f4
result SHA-256: 4ad550f37cf21976fdbdf96d7e21641cc6e0446687db6afbcd3c4824b0ff7c7b
result: PASS=96, FAIL=0, TIMEOUT=0, HASH_MISMATCH=0, REMOTE_ERROR=0
```

The sole discovered Modal launcher is hashed and classified as a launcher,
not falsely reported as a locally replayed proof. `audit.py` independently
checks the current manifest, reruns all six negative controls, and checks the
complete Modal result script-by-script against the manifest.
