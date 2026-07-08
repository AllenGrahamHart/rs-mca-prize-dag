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

## Extra-prime falsification sweep

Status: MACHINE-VERIFIED COMPLETE ROW SWEEP + HEURISTIC REPAIR.

After the zero boundary row above, the same Modal-sharded certificate was run
at six additional primes:

```text
p=4481   anchored_nontoral_trades=0
p=4673   anchored_nontoral_trades=0
p=4801   anchored_nontoral_trades=0
p=4993   anchored_nontoral_trades=6
p=5441   anchored_nontoral_trades=0
p=5569   anchored_nontoral_trades=0
```

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-OBattAeGlh1H0GoKvCs5Fo
```

The `p=4993` row is a finite falsifier for the stronger heuristic
"h=6 primitive residue is empty at every q >= n^2."  It is not a falsifier for
the direct-column floor: the count is `6`, while the direct budget is
`n^3 = 262144`, and no row has a direct `n^3` alarm.

The six decoded p4993 anchored witnesses are:

```text
[0,5,13,32,37,45]  vs [16,18,26,48,50,58]  last=(269,4061)
[0,2,10,32,34,42]  vs [16,21,29,48,53,61]  last=(932,4724)
[0,19,24,32,51,56] vs [3,5,13,35,37,45]    last=(3611,4881)
[0,22,24,32,54,56] vs [6,11,19,38,43,51]   last=(1058,2534)
[0,8,27,32,40,59]  vs [11,13,21,43,45,53]  last=(3657,2717)
[0,8,30,32,40,62]  vs [14,19,27,46,51,59]  last=(2598,4061)
```

Interpretation repair: the surviving h=6 target should be a small/budgeted
norm-gate accident statement, not a universal finite-row emptiness statement.

## Replay

```bash
~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
F3_H6_N64_MODE=extra ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_modal.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_certificate.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_extra_primes_certificate.py
```

Expected digests:

```text
H6_N64_BOUNDARY_CERTIFICATE_PASS
H6_N64_EXTRA_PRIMES_SWEEP_DONE
H6_N64_BOUNDARY_CERTIFICATE_JSON_PASS
H6_N64_EXTRA_PRIMES_SWEEP_VERIFY_PASS
```

The Modal replay writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_boundary_certificate.json
critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_n64_extra_primes_certificate.json
```
