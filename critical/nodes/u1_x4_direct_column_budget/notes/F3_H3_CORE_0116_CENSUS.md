# F3 h=3 core `(0,1,16)` complete census (Terminal C)

Status: PRE-REGISTERED COMPLETE CORE-SLICE CENSUS.  This is the fifteenth of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,16],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,16 --tag 0116
```

Expected digest:

```text
H3_CORE_0116_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0116_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-gbPBZHbKK07l5tfI7uDjzC
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1275 activation_exceptions=7
H3_CORE_0116_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1275 / 129766 = 0.9825%
actual common-root activation:    7 / 129766 = 0.0054%
```

Activation list:

```text
[0, 1, 16 | 8, 9, 41]     p=37633
[0, 1, 16 | 8, 41, 57]    p=1416317953
[0, 1, 16 | 8, 57, 89]    p=37633
[0, 1, 16 | 9, 41, 56]    p=37633
[0, 1, 16 | 9, 56, 89]    p=1416317953
[0, 1, 16 | 24, 52, 75]   p=20161
[0, 1, 16 | 56, 57, 89]   p=37633
```

The full list is also stored in:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0116_census_results.json
```

Local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0116_census_check.py
```

Expected digest:

```text
H3_CORE_0116_CENSUS_CHECK_PASS
```
