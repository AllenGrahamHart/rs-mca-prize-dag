# F3 h=3 core `(0,1,18)` complete census (Terminal C)

Status: PRE-REGISTERED COMPLETE CORE-SLICE CENSUS.  This is the seventeenth of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,18],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,18 --tag 0118
```

Expected digest:

```text
H3_CORE_0118_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0118_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-kVG2QhlE4iVbbvcScuiu1S
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1135 activation_exceptions=4
H3_CORE_0118_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1135 / 129766 = 0.8747%
actual common-root activation:    4 / 129766 = 0.0031%
```

Activation list:

```text
[0, 1, 18 | 6, 31, 84]    p=27361
[0, 1, 18 | 12, 30, 67]   p=27361
[0, 1, 18 | 15, 32, 65]   p=10177
[0, 1, 18 | 50, 51, 65]   p=10177
```

The full list is also stored in:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0118_census_results.json
```

Local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0118_census_check.py
```

Expected digest:

```text
H3_CORE_0118_CENSUS_CHECK_PASS
```
