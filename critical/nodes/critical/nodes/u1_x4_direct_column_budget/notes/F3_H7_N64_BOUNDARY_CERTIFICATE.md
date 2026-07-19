# F3 h=7 n=64 boundary certificate

Status: MACHINE-VERIFIED COMPLETE ROW CERTIFICATE.

This upgrades the old `q2_n64_h7_FULL` partial artifact into a complete
rank-sharded anchor certificate at the first prime `p = 4289 >= 64^2` with
`p = 1 mod 64`.

## Pre-registration

Object:

```text
n = 64, h = 7, p = 4289.
```

The first timing gate showed that the all-left table can be built and sorted in
one Modal worker, but the old `r[0] mod 16` right sharding is too imbalanced.
The certificate therefore uses rank-balanced right sharding: every worker
enumerates the complete right-combination stream and processes combinations
whose rank is congruent to its shard index modulo `16`.

Success criterion:

- each worker builds the full anchored-left table of `67945521` records;
- the 16 workers together probe all `553270671` right subsets exactly once;
- every worker finishes under the 60-second Modal timeout;
- anchored toral trades and anchored nontoral trades are both zero;
- no `n^3` alarm fires.

Failure criterion:

- any partial shard, timeout, nonzero anchored nontoral count, or `n^3` alarm.

## Result

Modal timing gate:

```text
https://modal.com/apps/allengrahamhart/main/ap-ZAk46tL9SN1s11CFOkqlJi
```

Full Modal certificate:

```text
https://modal.com/apps/allengrahamhart/main/ap-99OG86SNtWLVrIKsovgVqI
```

Aggregate:

```text
left_records_per_shard = 67945521
probed = 553270671
shards = 16
shards_completed = 16
anchored_toral_trades = 0
anchored_nontoral_trades = 0
direct_n3_budget = 262144
direct_n3_exceeded = false
max_elapsed_sec = 55.1206
```

Interpretation: this is a complete finite-row zero certificate for
`n=64,h=7,p=4289`.  It replaces the old partial n=64 h=7 evidence at the
`q >= n^2` boundary.  It is not a uniform h=7 theorem.

## Replay

```bash
F3_H7_N64_MODE=full ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h7_n64_timing_gate_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h7_n64_boundary_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Expected digests:

```text
H7_N64_BOUNDARY_CERTIFICATE_PASS
H7_N64_BOUNDARY_CERTIFICATE_JSON_PASS
H6_H8_BONUS_SWEEP_PASS
```
