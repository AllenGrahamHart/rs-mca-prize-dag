# F3 h=7/h=8 n=64 certificate feasibility

Status: EXACT FEASIBILITY ARITHMETIC + NEXT-ACTION POSE.

This note records why the remaining `n=64,h=8` partial rows should not be
blindly rerun with the current all-left hash certificate.  It also separates
the still-plausible `h=7` gate from the much larger `h=8` problem.

## Pre-registration

Question:

```text
Can the current h=6 all-left-hash, right-sharded certificate pattern be
directly promoted to complete n=64 certificates for h=7 and h=8 under the
60-second/light-compute rule?
```

Failure criterion for a direct brute-force promotion:

- the left hash table alone exceeds realistic Modal memory for light tasks; or
- the exact left/right work factors are large enough that a blind full sweep
  would be a poor use of the run budget without a gate.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h7_h8_n64_feasibility.py
```

Expected digest:

```text
H7_H8_N64_FEASIBILITY_PASS
```

## Result

Using the certified h=6 n=64 p4289 row as baseline
(`7028847` anchored left records, `67945521` right probes, max shard
`10.634s`), exact combinatorics gives:

```text
h=6 left=7028847    right=67945521    mem32=214.5MiB
h=7 left=67945521   right=553270671   mem32=2073.5MiB
h=8 left=553270671  right=3872894697  mem32=16884.5MiB
```

The h=7 row is not obviously impossible on Modal memory, but the current method
would rebuild and sort a 68-million-record left table in every right shard; it
needs a one-shard timing gate before any full sweep.

The h=8 row is not a current all-left hash certificate under the light-compute
rule: the left table alone is about `16.5 GiB` at a conservative 32 bytes per
record, before sort overhead.  A full h=8 n=64 certificate should therefore use
one of:

- structural reduction by square-shift/x83 certifier keys;
- a different external/sharded join that partitions signatures without
  rebuilding the full left table per worker;
- a smaller quotient certificate that proves the only visible h=8 candidates
  are paid lifts.

## Next Action

Do not run a blind h=8 n=64 full anchor sweep.  The next safe computation is a
single h=7 n=64 Modal gate that builds and sorts one all-left table, exits with
partial timing before probing if it approaches the 60-second cap, and only then
decides whether a full h=7 certificate is worth dispatching.  For h=8, pursue
the square-shift/x83 route first.
