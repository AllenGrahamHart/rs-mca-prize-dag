# F3 h=3 core `(0,1,31)` complete census (Terminal C)

Status: PRE-REGISTERED CORE-SLICE CENSUS.  This is the thirtieth of
the 91 affine/Galois core types in the `n=96` Terminal C program.

## Pre-registration

Core:

```text
A = [0,1,31],  B any 3-subset of Z/96Z disjoint from A.
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
~/.venvs/modal/bin/modal run critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_census_modal.py --core 0,1,31 --tag 0131
```

Expected digest:

```text
H3_CORE_0131_CENSUS_DONE
```

Expected result file:

```text
critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0131_census_results.json
```

## Result

Modal run:

```text
https://modal.com/apps/allengrahamhart/main/ap-Z7A1xv8N38whCXWCBuPZeO
```

Summary:

```text
TOTAL shapes=129766 norm_exceptions=1070 activation_exceptions=4
H3_CORE_0131_CENSUS_DONE
```

Rates:

```text
rational norm exception:       1070 / 129766 = 0.8246%
actual common-root activation:    4 / 129766 = 0.0031%
```

Activation list:

```text
[0, 1, 31 | 13, 18, 43]   p=27361
[0, 1, 31 | 17, 80, 82]   p=10177
[0, 1, 31 | 19, 78, 85]   p=27361
[0, 1, 31 | 46, 47, 80]   p=10177
```

The banked JSON is pinned by the local integrity replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_core_0131_census_check.py
```

Expected digest:

```text
H3_CORE_0131_CENSUS_CHECK_PASS
```
