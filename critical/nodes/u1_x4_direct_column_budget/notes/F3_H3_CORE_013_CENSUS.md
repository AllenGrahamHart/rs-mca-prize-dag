# F3 h=3 core `(0,1,3)` complete census (Terminal C)

Status: PRE-REGISTERED COMPLETE CORE-SLICE CENSUS.  This is the second of the
91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,3],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_013_census_modal.py
```

Expected digest:

```text
H3_CORE_013_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_013_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-PPkOFbEgdQJmer1TbRvNgV
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1224 activation_exceptions=3
H3_CORE_013_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1224 / 129766 = 0.9432%
actual common-root activation:    3 / 129766 = 0.0023%
```

Activation list:

```text
[0, 1, 3 | 9, 36, 84]    p=10273
[0, 1, 3 | 46, 47, 52]   p=40897
[0, 1, 3 | 46, 53, 55]   p=67777
```

The full list is also stored in:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_013_census_results.json
```
