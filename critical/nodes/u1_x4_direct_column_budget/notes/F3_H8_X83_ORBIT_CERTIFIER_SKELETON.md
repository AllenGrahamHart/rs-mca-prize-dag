# F3 h=8 x83 orbit-certifier skeleton

Status: CERTIFIER CONSTRUCTION / DRY-RUN REPLAY, NOT A FULL h=8 CERTIFICATE.

This packet converts the h=8 n=64 residual into a concrete shardable certifier
interface.  It does not run the global search and it does not close h=8.

## Pre-registration

Question:

```text
Can the non-antipodal x83 support target be scanned in safe rotation-canonical
shards with partial output, without building the blind binom(63,7) left table?
```

Success criterion:

- rank-unrank anchored 16-supports with exponent `0` included;
- exclude the antipodal branch already routed to the h=4 quotient ledger;
- canonicalize non-antipodal supports under the proved root-scaling rotation;
- test only canonical anchored representatives;
- emit partial progress before a time budget expires;
- keep the packet explicitly below certificate status.

Failure criterion:

- use exponent-unit or reflection symmetries not proved to preserve x83;
- count antipodal supports in the primitive residual;
- require a laptop-sized left/right signature table;
- claim that a dry run is a global h=8 certificate.

## Construction

The script scans anchored supports by combinatorial rank in

```text
binom(63,15)
```

possible tails.  A future Modal manifest can split this interval by:

```bash
F3_H8_ORBIT_SHARDS=<number of shards>
F3_H8_ORBIT_SHARD=<this shard index>
```

For each support, it applies the already-proved filters:

1. skip antipodal supports;
2. compute the lexicographically minimal anchored rotation among the 16 anchors
   in the support;
3. test x83 only when the current support is that canonical representative;
4. skip non-antipodal canonical supports whose high odd locator coefficients
   `c15,c13,c11,c9` all vanish.

For non-antipodal supports this is sound because
`F3_H8_NONANTIPODAL_APERIODIC.md` proves every non-antipodal rotation orbit has
size `64`, and `F3_H8_X83_SPLIT_ROTATION_EQUIVARIANCE.md` proves the x83 split
commutes with root scaling up to side swap.  The high-odd skip is sound by
`F3_H8_X83_PARITY_REDUCTION.md`: if a full-zero support has all high odd
locator coefficients zero, then it is antipodal.
The companion `F3_H8_ODD_CHART_ROUTER.md` refines this skip into a deterministic
chart route for the remaining high-odd canonical supports.

The resulting global target is therefore exactly:

```text
7,633,233,227,520 non-antipodal rotation-orbit representatives.
```

This is still too large for a blind local run.  The value of the skeleton is
that it gives a resumable, partial-output certificate runner that can be used
inside 60 second Modal jobs or replaced by a stronger obstruction-key join.

## Partial-output controls

Environment controls:

```text
F3_H8_ORBIT_P             prime row, default 4289
F3_H8_ORBIT_SHARDS        total shard count, default 1
F3_H8_ORBIT_SHARD         shard index, default 0
F3_H8_ORBIT_START_RANK    optional resume rank inside the shard
F3_H8_ORBIT_STOP_RANK     optional early stop rank inside the shard
F3_H8_ORBIT_MAX_SUPPORTS  local cap; 0 means run the whole shard
F3_H8_ORBIT_SECONDS       internal wall-clock budget; 0 means no time budget
```

For laptop safety the default run checks only the first `2048` anchored
supports in shard `0`.  A real Modal invocation should use an internal budget
below the external container timeout, for example:

```bash
F3_H8_ORBIT_SECONDS=55 F3_H8_ORBIT_MAX_SUPPORTS=0 \
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_orbit_certifier_skeleton.py
```

The script prints `next_rank`, so interrupted shards can resume from the first
unprocessed combinatorial rank by setting `F3_H8_ORBIT_START_RANK`.
It also emits one machine-readable line prefixed by `CERT_RECORD`; future
manifest tooling should consume those JSON records rather than parsing the
human-readable summary.

## Dry-run replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_orbit_certifier_skeleton.py
```

Expected digest:

```text
H8_X83_ORBIT_CERTIFIER_SKELETON_PASS
```

The dry run proves only that the sharding, antipodal filter, rotation
canonicalizer, and x83 obstruction call are wired coherently on a bounded
prefix.  The open h=8 task remains the full non-antipodal certificate or a
stronger symbolic obstruction.
