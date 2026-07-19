# F3 h=3 core `(0,1,69)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the sixty-eighth of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,69],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,69 --tag 0169
```

Expected digest:

```text
H3_CORE_0169_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0169_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-RAHh5r5e7ez7NP0QVJRG3i
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1245 activation_exceptions=6
H3_CORE_0169_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1245 / 129766 = 0.9594%
actual common-root activation:    6 / 129766 = 0.0046%
```

Activation list:

```text
[0, 1, 69 | 9, 14, 25]    p=32833
[0, 1, 69 | 9, 20, 77]    p=37633
[0, 1, 69 | 9, 56, 60]    p=37633
[0, 1, 69 | 36, 40, 61]   p=37633
[0, 1, 69 | 45, 61, 70]   p=20161
[0, 1, 69 | 61, 76, 89]   p=37633
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0169_census_check.py
```

Expected digest:

```text
H3_CORE_0169_CENSUS_CHECK_PASS
```
