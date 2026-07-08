# F3 h=8 residual frontier audit

Status: AUDIT / MACHINE-CHECKED RESIDUAL MAP, NOT A FULL h=8 n=64
CERTIFICATE.

This packet records the current h=8 boundary after the T4 local replay.  It
does not launch a new search.  It verifies the complete h=8 rows that are
already banked, the explicitly partial h=8 n=64 rows, and the x83
radius-three certificates that currently define the non-antipodal attack
frontier.

## Pre-registration

Question:

```text
What exactly remains open in the h=8 n=64 row after the full n=32 certificates
and the x83 radius-three shell certificates are replayed?
```

Success criterion:

- verify all six h=8 n=32 full certificates;
- verify the two h=8 n=64 rows are still marked partial and only claim zero in
  their checked slices;
- verify both x83 radius-three shell certificates are complete, under the
  60-second shard policy, and have `full_zero = 0`;
- verify the q3 suffix profile dies at obstruction depth two;
- print the blind h=8 n=64 join size to justify why the next step must use
  x83 keys or an external/sharded signature join.

Failure criterion:

- any full h=8 n=32 row has nonzero nontoral residue or an `n^3` alarm;
- any h=8 n=64 partial row is accidentally treated as complete;
- any radius-three x83 shard is incomplete or has a full-zero support;
- the audit hides the remaining non-antipodal branch behind local shell
  evidence.

## Verified complete h=8 rows

The full h=8 anchored certificates currently cover six n=32 rows:

```text
p in {1153, 3137, 12289, 40961, 61441, 65537}
```

Each has:

```text
anchored_toral_trades = 3
anchored_nontoral_trades = 0
partial = false
complete = true
direct_n3_exceeded = false
```

These six rows account for `47,332,350` right-side probes.

## h=8 n=64 residual

The two h=8 n=64 rows remain explicitly partial:

```text
boundary_n64_h8_p193: partial=True, checked slice W=48, nontoral=0
q3_n64_h8:            partial=True, checked slice W=48, nontoral=0
```

The x83 radius-three shell certificates around the paid antipodal square-lift
branch are complete at both the boundary-style prime and the q3 prime:

```text
p=4289:   processed=67,800,320, first_obstruction_zero=16,048, full_zero=0
p=262337: processed=67,800,320, first_obstruction_zero=320,    full_zero=0
```

The q3 suffix profile is:

```text
[67800000, 320, 0, 0, 0, 0, 0, 0]
```

Thus every q3 radius-three shell candidate that reaches the first obstruction
dies at the next obstruction; no square-lambda condition is reached in that
shell.

## Why the residual is still real

A blind all-left h=8 n=64 join would need

```text
binom(63, 7) = 553,270,671
```

anchored left records.  At 32 bytes per record that is about `16.49 GiB`, before
the right-side scan

```text
binom(63, 8) = 3,872,894,697
```

is considered.  This is outside the light-local-compute policy and should not
be attempted as a laptop job.

The honest residual is therefore:

```text
certify the non-antipodal h=8 n=64 branch using the x83 obstruction keys, or
design a true external/sharded signature join that avoids the oversized blind
left table.
```

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_residual_frontier_audit.py
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Expected digests:

```text
H8_RESIDUAL_FRONTIER_AUDIT_PASS
H6_H8_BONUS_SWEEP_PASS
```
