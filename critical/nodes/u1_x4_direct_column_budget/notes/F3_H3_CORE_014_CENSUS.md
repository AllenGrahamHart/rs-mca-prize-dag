# F3 h=3 core `(0,1,4)` complete census (Terminal C)

Status: PRE-REGISTERED COMPLETE CORE-SLICE CENSUS.  This is the third of the
91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,4],  B any 3-subset of Z/96Z disjoint from A.
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
- `64` shards by combination index;
- worker timeout `60s`;
- partial per-shard counts print before aggregation.

## Replay

```text
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_modal.py
```

Expected digest:

```text
H3_CORE_014_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-2l3BsQqnwrHBRX5d0uSYFg
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1142 activation_exceptions=5
H3_CORE_014_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1142 / 129766 = 0.8800%
actual common-root activation:    5 / 129766 = 0.0039%
```

Activation list:

```text
[0, 1, 4 | 9, 37, 60]    p=37633
[0, 1, 4 | 12, 23, 33]   p=17377
[0, 1, 4 | 40, 44, 53]   p=37633
[0, 1, 4 | 40, 61, 89]   p=37633
[0, 1, 4 | 45, 56, 60]   p=37633
```

The full list is also stored in:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_results.json
```

Local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_014_census_check.py
```

Expected digest:

```text
H3_CORE_014_CENSUS_CHECK_PASS
```
