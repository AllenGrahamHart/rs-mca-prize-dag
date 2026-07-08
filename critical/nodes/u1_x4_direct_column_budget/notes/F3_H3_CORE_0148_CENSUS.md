# F3 h=3 core `(0,1,48)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the forty-seventh of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,48],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,48 --tag 0148
```

Expected digest:

```text
H3_CORE_0148_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0148_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-UjM6442S2oqGQ7MdXXLf9u
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1067 activation_exceptions=37
H3_CORE_0148_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1067 / 129766 = 0.8222%
actual common-root activation:   37 / 129766 = 0.0285%
```

Activation list:

```text
[0, 1, 48 | 2, 31, 63]    p=207073
[0, 1, 48 | 2, 51, 95]    p=207073
[0, 1, 48 | 4, 31, 63]    p=40897
[0, 1, 48 | 4, 47, 90]    p=49537
[0, 1, 48 | 6, 31, 63]    p=18913
[0, 1, 48 | 6, 47, 88]    p=12289
[0, 1, 48 | 12, 31, 63]   p=30817
[0, 1, 48 | 12, 47, 82]   p=1857217
[0, 1, 48 | 14, 47, 80]   p=300673
[0, 1, 48 | 16, 31, 63]   p=10177
[0, 1, 48 | 16, 47, 78]   p=26682529
[0, 1, 48 | 20, 47, 74]   p=12097
[0, 1, 48 | 22, 47, 72]   p=1033441
[0, 1, 48 | 24, 47, 70]   p=1033441
[0, 1, 48 | 26, 47, 68]   p=12097
[0, 1, 48 | 30, 47, 64]   p=26682529
[0, 1, 48 | 31, 32, 63]   p=10177
[0, 1, 48 | 31, 36, 63]   p=30817
[0, 1, 48 | 31, 42, 63]   p=18913
[0, 1, 48 | 31, 44, 63]   p=40897
[0, 1, 48 | 31, 46, 63]   p=207073
[0, 1, 48 | 31, 50, 63]   p=207073
[0, 1, 48 | 31, 52, 63]   p=40897
[0, 1, 48 | 31, 54, 63]   p=18913
[0, 1, 48 | 31, 60, 63]   p=30817
[0, 1, 48 | 31, 63, 64]   p=10177
[0, 1, 48 | 31, 63, 80]   p=10177
[0, 1, 48 | 31, 63, 84]   p=30817
[0, 1, 48 | 31, 63, 90]   p=18913
[0, 1, 48 | 31, 63, 92]   p=40897
[0, 1, 48 | 31, 63, 94]   p=207073
[0, 1, 48 | 32, 47, 62]   p=300673
[0, 1, 48 | 34, 47, 60]   p=1857217
[0, 1, 48 | 40, 47, 54]   p=12289
[0, 1, 48 | 42, 47, 52]   p=49537
[0, 1, 48 | 45, 47, 49]   p=74209
[0, 1, 48 | 50, 51, 95]   p=207073
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0148_census_check.py
```

Expected digest:

```text
H3_CORE_0148_CENSUS_CHECK_PASS
```
