# F3 h=3 core `(0,1,42)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the forty-first of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,42],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,42 --tag 0142
```

Expected digest:

```text
H3_CORE_0142_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0142_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-7yZ6b03mPlo6ClweVzZj2F
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1106 activation_exceptions=3
H3_CORE_0142_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1106 / 129766 = 0.8523%
actual common-root activation:    3 / 129766 = 0.0023%
```

Activation list:

```text
[0, 1, 42 | 3, 70, 86]    p=15361
[0, 1, 42 | 6, 60, 91]    p=12289
[0, 1, 42 | 7, 36, 78]    p=12289
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0142_census_check.py
```

Expected digest:

```text
H3_CORE_0142_CENSUS_CHECK_PASS
```
