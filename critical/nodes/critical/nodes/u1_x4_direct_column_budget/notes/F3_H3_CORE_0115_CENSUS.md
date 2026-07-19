# F3 h=3 core `(0,1,15)` complete census (Terminal C)

Status: PRE-REGISTERED COMPLETE CORE-SLICE CENSUS.  This is the fourteenth of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,15],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,15 --tag 0115
```

Expected digest:

```text
H3_CORE_0115_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0115_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-QYA4kM3GHwcFB12xBgkENm
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1117 activation_exceptions=2
H3_CORE_0115_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1117 / 129766 = 0.8608%
actual common-root activation:    2 / 129766 = 0.0015%
```

Activation list:

```text
[0, 1, 15 | 21, 35, 62]   p=67777
[0, 1, 15 | 46, 47, 64]   p=10177
```

The full list is also stored in:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0115_census_results.json
```

Local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0115_census_check.py
```

Expected digest:

```text
H3_CORE_0115_CENSUS_CHECK_PASS
```
