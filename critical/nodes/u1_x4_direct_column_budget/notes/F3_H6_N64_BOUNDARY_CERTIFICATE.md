# F3 h=6 n=64 boundary certificate

Status: MACHINE-VERIFIED COMPLETE ROW CERTIFICATE.

This targets a gap in the h=6/7/8 bonus sweep: existing h=6 full rows are all
at `n=32`, while the h=7/h=8 `n=64` rows in the old sweep are partial slices.
The h=6 `n=64` anchored row was too slow for a single local replay under the
60-second rule (`timeout 60s` exited at 60.00s, max RSS 86 MB), so the complete
row certificate is Modal-sharded into 16 containers with a 60-second timeout per
shard.  The heaviest shard completed in 10.634 seconds.

## Pre-registration

Row:

```text
n = 64, h = 6, p = 4289.
```

Object:

```text
anchored same-signature h=6 trades with one side containing exponent 0,
right side avoiding 0, equal e_1..e_5, unequal e_6, and disjoint supports.
```

Success evidence:

- the compiled replay checks all `binom(63,5)` anchored left subsets and all
  `binom(63,6)` right subsets;
- the positive result sought is zero anchored nontoral trades;
- any nonzero count is banked as a finite-row falsifier for h=6 emptiness
  evidence, while still checking whether the direct `n^3` floor is exceeded.

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-9ZeZrlz8FyYuLIIJAq2TgD
```

Aggregate:

```text
hashed_per_shard = 7028847
probed = 67945521
shards = 16
shards_completed = 16
anchored_toral_trades = 0
anchored_nontoral_trades = 0
direct_n3_budget = 262144
direct_n3_exceeded = false
max_elapsed_sec = 10.634
```

Interpretation: this is a complete anchored finite-row zero certificate for
`n=64,h=6,p=4289`.  It extends the previous h=6 full-row evidence beyond
`n=32`; it is not a uniform h=6 no-primitive theorem.

## Replay

```bash
~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_certificate.py
```

Expected digests:

```text
H6_N64_BOUNDARY_CERTIFICATE_PASS
H6_N64_BOUNDARY_CERTIFICATE_JSON_PASS
```

The Modal replay writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_certificate.json
```
