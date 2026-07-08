# F3 h=3 core `(0,1,45)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the forty-fourth of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,45],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,45 --tag 0145
```

Expected digest:

```text
H3_CORE_0145_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0145_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-qADxYHfoxrjMig5PadXICz
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1113 activation_exceptions=7
H3_CORE_0145_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1113 / 129766 = 0.8577%
actual common-root activation:    7 / 129766 = 0.0054%
```

Activation list:

```text
[0, 1, 45 | 4, 41, 85]    p=37633
[0, 1, 45 | 5, 57, 92]    p=37633
[0, 1, 45 | 8, 57, 84]    p=37633
[0, 1, 45 | 12, 85, 88]   p=37633
[0, 1, 45 | 13, 44, 77]   p=207073
[0, 1, 45 | 38, 53, 56]   p=15937
[0, 1, 45 | 46, 47, 94]   p=207073
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0145_census_check.py
```

Expected digest:

```text
H3_CORE_0145_CENSUS_CHECK_PASS
```
