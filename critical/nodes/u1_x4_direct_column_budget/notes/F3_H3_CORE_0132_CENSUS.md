# F3 h=3 core `(0,1,32)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the thirty-first of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,32],  B any 3-subset of Z/96Z disjoint from A.
```

There are `binom(93,3)=129766` shapes in this oriented slice.

Deliverable:

- compute exact obstruction norms for every `B`;
- factor `gcd(N(E1),N(E2))`;
- record threshold rational norm exceptions;
- test actual common primitive-root activation for each threshold factor;
- write the full activation list to JSON.

Compute discipline:

- Modal only;
- generic runner `f3_h3_core_census_modal.py`;
- `64` shards by combination index;
- worker timeout `60s`;
- partial per-shard counts print before aggregation.

## Replay

```text
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,32 --tag 0132
```

Expected digest:

```text
H3_CORE_0132_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0132_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-GeIRA1BYqRhxdmEr9ZMpMM
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=957 activation_exceptions=14
H3_CORE_0132_CENSUS_DONE
```

Rates:

```text
rational norm exception:        957 / 129766 = 0.7375%
actual common-root activation:   14 / 129766 = 0.0108%
```

Activation list:

```text
[0, 1, 32 | 2, 33, 81]    p=10177
[0, 1, 32 | 2, 36, 50]    p=20929
[0, 1, 32 | 5, 42, 53]    p=40897
[0, 1, 32 | 8, 36, 84]    p=37633
[0, 1, 32 | 11, 54, 59]   p=207073
[0, 1, 32 | 12, 56, 60]   p=37633
[0, 1, 32 | 17, 65, 66]   p=10177
[0, 1, 32 | 18, 66, 68]   p=20929
[0, 1, 32 | 20, 42, 90]   p=67777
[0, 1, 32 | 20, 68, 72]   p=37633
[0, 1, 32 | 21, 69, 74]   p=40897
[0, 1, 32 | 24, 44, 92]   p=37633
[0, 1, 32 | 26, 74, 84]   p=67777
[0, 1, 32 | 27, 75, 86]   p=207073
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0132_census_check.py
```

Expected digest:

```text
H3_CORE_0132_CENSUS_CHECK_PASS
```
