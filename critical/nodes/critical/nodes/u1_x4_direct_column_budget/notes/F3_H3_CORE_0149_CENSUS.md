# F3 h=3 core `(0,1,49)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the forty-eighth of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,49],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,49 --tag 0149
```

Expected digest:

```text
H3_CORE_0149_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0149_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-2Veov6xX4JdbgHqLM1tV0s
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1067 activation_exceptions=37
H3_CORE_0149_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1067 / 129766 = 0.8222%
actual common-root activation:   37 / 129766 = 0.0285%
```

Activation list:

```text
[0, 1, 49 | 2, 46, 47]    p=207073
[0, 1, 49 | 2, 46, 95]    p=207073
[0, 1, 49 | 3, 34, 66]    p=207073
[0, 1, 49 | 5, 34, 66]    p=40897
[0, 1, 49 | 7, 34, 66]    p=18913
[0, 1, 49 | 7, 50, 93]    p=49537
[0, 1, 49 | 9, 50, 91]    p=12289
[0, 1, 49 | 13, 34, 66]   p=30817
[0, 1, 49 | 15, 50, 85]   p=1857217
[0, 1, 49 | 17, 34, 66]   p=10177
[0, 1, 49 | 17, 50, 83]   p=300673
[0, 1, 49 | 19, 50, 81]   p=26682529
[0, 1, 49 | 23, 50, 77]   p=12097
[0, 1, 49 | 25, 50, 75]   p=1033441
[0, 1, 49 | 27, 50, 73]   p=1033441
[0, 1, 49 | 29, 50, 71]   p=12097
[0, 1, 49 | 33, 34, 66]   p=10177
[0, 1, 49 | 33, 50, 67]   p=26682529
[0, 1, 49 | 34, 37, 66]   p=30817
[0, 1, 49 | 34, 43, 66]   p=18913
[0, 1, 49 | 34, 45, 66]   p=40897
[0, 1, 49 | 34, 47, 66]   p=207073
[0, 1, 49 | 34, 51, 66]   p=207073
[0, 1, 49 | 34, 53, 66]   p=40897
[0, 1, 49 | 34, 55, 66]   p=18913
[0, 1, 49 | 34, 61, 66]   p=30817
[0, 1, 49 | 34, 65, 66]   p=10177
[0, 1, 49 | 34, 66, 81]   p=10177
[0, 1, 49 | 34, 66, 85]   p=30817
[0, 1, 49 | 34, 66, 91]   p=18913
[0, 1, 49 | 34, 66, 93]   p=40897
[0, 1, 49 | 34, 66, 95]   p=207073
[0, 1, 49 | 35, 50, 65]   p=300673
[0, 1, 49 | 37, 50, 63]   p=1857217
[0, 1, 49 | 43, 50, 57]   p=12289
[0, 1, 49 | 45, 50, 55]   p=49537
[0, 1, 49 | 48, 50, 52]   p=74209
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0149_census_check.py
```

Expected digest:

```text
H3_CORE_0149_CENSUS_CHECK_PASS
```
