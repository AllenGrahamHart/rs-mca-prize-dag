# F3 h=3 core `(0,1,64)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the sixty-third of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,64],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,64 --tag 0164
```

Expected digest:

```text
H3_CORE_0164_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0164_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-JcoMjUD1N4iwoCQnKj80sY
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1074 activation_exceptions=32
H3_CORE_0164_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1074 / 129766 = 0.8276%
actual common-root activation:   32 / 129766 = 0.0247%
```

Activation list:

```text
[0, 1, 64 | 2, 50, 68]    p=12289
[0, 1, 64 | 2, 62, 80]    p=12289
[0, 1, 64 | 4, 60, 80]    p=37633
[0, 1, 64 | 6, 19, 67]    p=18913
[0, 1, 64 | 6, 54, 76]    p=20929
[0, 1, 64 | 6, 58, 80]    p=67777
[0, 1, 64 | 7, 55, 78]    p=18913
[0, 1, 64 | 8, 9, 89]     p=37633
[0, 1, 64 | 8, 41, 57]    p=37633
[0, 1, 64 | 9, 56, 89]    p=37633
[0, 1, 64 | 10, 54, 80]   p=67777
[0, 1, 64 | 12, 32, 77]   p=207073
[0, 1, 64 | 12, 52, 80]   p=37633
[0, 1, 64 | 12, 60, 88]   p=37633
[0, 1, 64 | 13, 61, 90]   p=30817
[0, 1, 64 | 14, 50, 80]   p=12289
[0, 1, 64 | 14, 62, 92]   p=27361
[0, 1, 64 | 15, 63, 94]   p=207073
[0, 1, 64 | 20, 26, 74]   p=27361
[0, 1, 64 | 26, 38, 80]   p=27361
[0, 1, 64 | 28, 30, 78]   p=67777
[0, 1, 64 | 28, 36, 80]   p=37633
[0, 1, 64 | 30, 34, 80]   p=20929
[0, 1, 64 | 33, 34, 81]   p=10177
[0, 1, 64 | 36, 40, 84]   p=37633
[0, 1, 64 | 37, 42, 85]   p=30817
[0, 1, 64 | 38, 44, 86]   p=12289
[0, 1, 64 | 41, 56, 57]   p=37633
[0, 1, 64 | 45, 58, 93]   p=40897
[0, 1, 64 | 74, 80, 86]   p=27361
[0, 1, 64 | 76, 80, 84]   p=37633
[0, 1, 64 | 78, 80, 82]   p=20929
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0164_census_check.py
```

Expected digest:

```text
H3_CORE_0164_CENSUS_CHECK_PASS
```
