# F3 h=5 n=128 boundary Modal certificate

Status: MACHINE-VERIFIED MODAL-SHARDED COMPLETE ROW CERTIFICATE.

This is the next scale after the complete local `n=96,h=5,p=9601`
certificate.  A local full replay would enumerate `254231775` right-side
subsets, so this probe is sharded on Modal.  Each shard recomputes the anchored
left table, then checks a disjoint slice of right subsets selected by first
right exponent modulo `32`.

## Pre-registration

Row:

```text
n = 128, h = 5, p = 17921.
```

Object:

```text
anchored same-signature h=5 trades with one side containing exponent 0,
right side avoiding 0, equal e_1..e_4, unequal e_5, and disjoint supports.
```

Gate criterion:

- run the heaviest shard first under Modal timeout `60s`;
- if that shard completes, full replay is allowed;
- if it times out, bank the timeout as the scale boundary and do not widen the
  run locally.

Certificate criterion:

- all `32` shards complete;
- total right probes equal `binom(127,5) = 254231775`;
- anchored nontoral trades equal `0`;
- no direct `n^3` alarm.

## Result

The heaviest-shard gate completed first:

```text
shard                 = 1
right probe subsets   = 13643876
anchored nontoral     = 0
elapsed               = 15.051 seconds
```

The full replay then completed all `32` shards:

```text
left anchored subsets per shard = binom(127,4) = 10334625
right probe subsets total       = binom(127,5) = 254231775
anchored toral trades           = 0
anchored nontoral trades        = 0
partial                         = false
max shard elapsed               = 17.488 seconds
direct n^3 alarm                = false
```

This extends the h=5 finite-row zero evidence to the `n=128` boundary row.  It
is still finite evidence, not a uniform h=5 no-primitive theorem.

An extra-prime follow-up replay then used the same 32-shard certificate at
`p=18049` and `p=18433`.  Both rows completed all shards:

```text
p=18049: right probes = 254231775, anchored nontoral = 0, max shard = 19.405s
p=18433: right probes = 254231775, anchored nontoral = 0, max shard = 13.729s
```

The extra-prime JSON is verified by the aggregate h4/h5 replay.

## Catch

The first Modal attempt failed before computation because Modal imports the
script at `/root`, so deriving the worktree root from `Path(__file__)` was not
portable.  The script now anchors output paths through `F3_PRIZE_ROOT`, with a
worktree default, and the remote function no longer depends on the local file
layout.

## Replay

Heaviest-shard gate:

```bash
F3_H5_N128_MODE=gate ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_modal.py
```

Full replay:

```bash
F3_H5_N128_MODE=full ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_modal.py
```

Extra-prime replay:

```bash
F3_H5_N128_MODE=extra ~/.venvs/modal/bin/modal run \
  critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_modal.py
```

Expected digests after successful runs:

```text
H5_N128_BOUNDARY_GATE_PASS
H5_N128_BOUNDARY_CERTIFICATE_PASS
H5_N128_EXTRA_PRIMES_CERTIFICATE_PASS
```

The gate writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_gate.json
```

The full replay writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_boundary_certificate.json
```

The extra-prime replay writes:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_n128_extra_primes_certificate.json
```
