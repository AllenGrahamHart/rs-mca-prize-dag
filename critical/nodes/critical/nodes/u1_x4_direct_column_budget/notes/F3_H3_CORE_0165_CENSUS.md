# F3 h=3 core `(0,1,65)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the sixty-fourth of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,65],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,65 --tag 0165
```

Expected digest:

```text
H3_CORE_0165_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0165_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-X347WzdJkDL9npXkLMuJNt
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=957 activation_exceptions=14
H3_CORE_0165_CENSUS_DONE
```

Rates:

```text
rational norm exception:        957 / 129766 = 0.7375%
actual common-root activation:   14 / 129766 = 0.0108%
```

Activation list:

```text
[0, 1, 65 | 5, 53, 73]    p=37633
[0, 1, 65 | 7, 55, 77]    p=67777
[0, 1, 65 | 11, 22, 70]   p=207073
[0, 1, 65 | 13, 23, 71]   p=67777
[0, 1, 65 | 13, 61, 89]   p=37633
[0, 1, 65 | 16, 64, 95]   p=10177
[0, 1, 65 | 23, 28, 76]   p=40897
[0, 1, 65 | 25, 29, 77]   p=37633
[0, 1, 65 | 29, 31, 79]   p=20929
[0, 1, 65 | 31, 32, 80]   p=10177
[0, 1, 65 | 37, 41, 85]   p=37633
[0, 1, 65 | 38, 43, 86]   p=207073
[0, 1, 65 | 44, 55, 92]   p=40897
[0, 1, 65 | 47, 61, 95]   p=20929
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0165_census_check.py
```

Expected digest:

```text
H3_CORE_0165_CENSUS_CHECK_PASS
```
