## Executed FPC5 Hankel/guard route probe

- **target:** `l1_fpc5_large_source_payment`
- **preregistration:** commit `468f04f1d`
- **canonical capture:** Modal app `ap-DlZD96lRzxt52OuV2msERv`
- **first run:** Modal app `ap-bXbMee2q6Gjl0eFBudI5Lo`
- **envelope:** 12 parallel workers, one CPU and 512 MB each, 60-second hard
  timeout and 54-second internal no-new-config deadline
- **completion:** 280/280 configurations and 504 fixed-background charts
- **result:** `NO_SEPARATION`; route evidence only

The rational FPC5 Hankel maxima were between `0.833` and `2.000` times the
matched random-Hankel maxima. Median untouched-petal guard survival was
between `0.917` and `1.000`. Neither preregistered alarm fired. The complete
emitted payload is pinned by SHA-256 in
`experiments/prize_resolution/fpc5_hankel_guard_probe_result.json`, and its
compact certificate has a deterministic checker with hostile mutations.

### Procedural limit

The v1 launcher returned completion counts but did not emit per-worker
elapsed times. Its conservative aggregate container ceiling is also twelve
minutes, although both parallel app runs completed in under one minute of
observed wall-clock time. It therefore remains non-load-bearing route
evidence under the strict compute rule and cannot support a `PROVED` status.
Do not rerun or enlarge it merely for audit completeness. A future theorem-
bearing campaign must preregister aggregate container-time accounting and a
full per-shard certificate before launch.
