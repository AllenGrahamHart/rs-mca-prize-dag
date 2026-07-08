# F3 h=3 core `(0,1,33)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the thirty-second of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,33],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,33 --tag 0133
```

Expected digest:

```text
H3_CORE_0133_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0133_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-0ZhwSTOA3QarhPpd5aIabM
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1074 activation_exceptions=32
H3_CORE_0133_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1074 / 129766 = 0.8276%
actual common-root activation:   32 / 129766 = 0.0247%
```

Activation list:

```text
[0, 1, 33 | 3, 34, 82]    p=207073
[0, 1, 33 | 4, 39, 52]    p=40897
[0, 1, 33 | 5, 35, 83]    p=27361
[0, 1, 33 | 7, 36, 84]    p=30817
[0, 1, 33 | 8, 41, 88]    p=37633
[0, 1, 33 | 8, 88, 89]    p=37633
[0, 1, 33 | 9, 37, 85]    p=37633
[0, 1, 33 | 11, 17, 23]   p=27361
[0, 1, 33 | 11, 53, 59]   p=12289
[0, 1, 33 | 12, 55, 60]   p=30817
[0, 1, 33 | 13, 17, 21]   p=37633
[0, 1, 33 | 13, 57, 61]   p=37633
[0, 1, 33 | 15, 17, 19]   p=20929
[0, 1, 33 | 16, 63, 64]   p=10177
[0, 1, 33 | 17, 35, 95]   p=12289
[0, 1, 33 | 17, 37, 93]   p=37633
[0, 1, 33 | 17, 39, 91]   p=67777
[0, 1, 33 | 17, 43, 87]   p=67777
[0, 1, 33 | 17, 45, 85]   p=37633
[0, 1, 33 | 17, 47, 83]   p=12289
[0, 1, 33 | 17, 59, 71]   p=27361
[0, 1, 33 | 17, 61, 69]   p=37633
[0, 1, 33 | 17, 63, 67]   p=20929
[0, 1, 33 | 19, 42, 90]   p=18913
[0, 1, 33 | 19, 67, 69]   p=67777
[0, 1, 33 | 20, 65, 85]   p=207073
[0, 1, 33 | 21, 43, 91]   p=20929
[0, 1, 33 | 23, 71, 77]   p=27361
[0, 1, 33 | 29, 47, 95]   p=12289
[0, 1, 33 | 30, 78, 91]   p=18913
[0, 1, 33 | 40, 41, 56]   p=37633
[0, 1, 33 | 40, 56, 89]   p=37633
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0133_census_check.py
```

Expected digest:

```text
H3_CORE_0133_CENSUS_CHECK_PASS
```
