# F3 h=5 certificate scaling frontier

Status: EXACT COST AUDIT FOR THE CURRENT CERTIFIER, NOT A NEW CERTIFICATE.

This packet quantifies how the existing h=5 anchored certificate design scales.
It launches no search and proves no new zero row.  Its purpose is to make the
h=5 residual operationally explicit: the present finite certificates are useful
evidence, but blind extension is not a clean path to a uniform theorem.

## Current Certifier Shape

For an h=5 anchored row at domain size `n`, the existing meet-in-the-middle
certifier uses:

```text
left_records  = binom(n-1,4)     # left side contains exponent 0
right_records = binom(n-1,5)     # right side avoids exponent 0
```

The banked n=128 Modal certificates use `32` shards.  Each shard rebuilds the
full left table

```text
binom(127,4) = 10,334,625
```

and the whole row probes

```text
binom(127,5) = 254,231,775
```

right sides.

## Scaling Table

Using the same row format and a 32-byte lower-bound record size for the left
table:

```text
 n     left_records       right_records     left_table_GiB   right_shards_at_n128_rate
 64        595,665          7,028,847          0.017752              1
 96      3,183,545         57,940,519          0.094877              8
128     10,334,625        254,231,775          0.307996             32
256    172,061,505      8,637,487,551          5.127832           1088
512  2,807,768,705    284,707,746,687         83.678028          35836
```

The `n=256` right side is still below the `<2000` shard count if one calibrates
only by the n=128 right-probe rate.  But with the current implementation each
of those shards would rebuild a `172,061,505`-record left table, about `16.65`
times the n=128 left table per shard and at least `5.13 GiB` before metadata.
The `n=512` row is beyond both the left-table memory envelope and the
`<2000`-shard right-probe policy for the current design.

## Consequence

The h=5 residual should not be attacked by blindly extending the current
certificate format.  A plausible certificate route needs one of:

- a persistent/shared left table or a different streaming join;
- a symbolic norm-gate incompatibility theorem;
- a new row-specific compression that avoids rebuilding `binom(n-1,4)` records
  per shard.

This is a scaling audit only.  It does not change the mathematical blocker:
exclude or certify the p-specific x83 norm-gate branch uniformly.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_scaling_frontier.py
```

Expected digest:

```text
H5_CERTIFICATE_SCALING_FRONTIER_PASS
```
