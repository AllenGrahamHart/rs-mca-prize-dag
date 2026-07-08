# F3 h=3 core `(0,1,46)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the forty-fifth of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,46],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,46 --tag 0146
```

Expected digest:

```text
H3_CORE_0146_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0146_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-Fo3oDk68PB7xwhSY4mt5iT
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1123 activation_exceptions=3
H3_CORE_0146_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1123 / 129766 = 0.8654%
actual common-root activation:    3 / 129766 = 0.0023%
```

Activation list:

```text
[0, 1, 46 | 3, 44, 90]    p=67777
[0, 1, 46 | 4, 45, 65]    p=18433
[0, 1, 46 | 50, 51, 93]   p=40897
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0146_census_check.py
```

Expected digest:

```text
H3_CORE_0146_CENSUS_CHECK_PASS
```
