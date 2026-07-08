# F3 h=3 repeat slope branch assembly

Status: CONDITIONAL BRANCH ASSEMBLY, NOT `H3-SLOPE-RATIO-HIT`.

This packet records the branch decomposition of the lambda-distinct
slope-ratio gate after the generic and mixed degree compilers.

## Branches

For a lambda-distinct active edge pair, there are only two real cases:

```text
generic-generic:
  both lambdas are different from 1;

mixed:
  exactly one lambda is 1.
```

The scale-scale case is impossible for lambda-distinct pairs, because both
edges would have `lambda=1`.

The generic-generic branch is the gate

```text
H3-SLOPE-GG-HIT.
```

Its current arithmetic interface has

```text
membership S_total = 14,
hit-product total degree <= 41.
```

The mixed branch is the gate

```text
H3-SLOPE-MIXED-HIT.
```

Orienting the generic edge as source gives

```text
membership S_total = 10,
hit-product total degree <= 27.
```

## Assembly

The slope-ratio hit gate is now exactly:

```text
H3-SLOPE-GG-HIT + H3-SLOPE-MIXED-HIT
  => H3-SLOPE-RATIO-HIT.
```

This does not prove either branch.  It removes the hidden `lambda=1`
exception from the statement of the slope gate and names the two targets that
future rank/nonvanishing or incidence arguments must close.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_slope_branch_assembly.py
```

Expected digest:

```text
H3_REPEAT_SLOPE_BRANCH_ASSEMBLY_PASS
```
