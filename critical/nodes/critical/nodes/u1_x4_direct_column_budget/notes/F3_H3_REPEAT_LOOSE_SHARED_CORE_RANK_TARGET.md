# F3 h=3 repeat loose shared-core rank target

Status: CONDITIONAL RANK-TARGET COMPILER, NOT A SHARED-CORE THEOREM AND NOT
`H3-NO-LOOSE-TRIANGLE`.

This packet applies the loose Stepanov and rank-minor compilers to the common
six-map core shared by the two clean special loose branches.

## Target

Every point on either clean special branch satisfies the six shared membership
maps recorded in `F3_H3_REPEAT_LOOSE_SHARED_CORE_DEGREE.md`.  Therefore a
future theorem for the shared core would bound both special branches before
the two private maps are used.

For the replayed sample box

```text
P=16, C=512, B=4, D=2, |Z|=1, n=32,
```

the shared-core target has

```text
maps=6, parameter_blocks=1, S_total=14.
```

The loose Stepanov compiler gives:

```text
coefficients=33554432,
conditions=1048,
X-degree=1087,
point bound=1087/2,
rank-capacity slack=40,
cleared total degree=1870.
```

The strong rank-minor sufficient condition is:

```text
rank target r=1049,
entry parameter degree=1359,
r-minor total parameter degree <= 1425591.
```

## Role in h=3

This is a possible count-route replacement for the two full special branch
gates:

```text
shared-core rank/NV theorem
  => common count bound for clean branch A and clean branch B candidates.
```

It does not prove the private tails, and it does not prove absence of loose
triangles.  Its value is that the common target has lower degree than the full
branch-A and branch-B targets, though the sample rank-capacity slack is tight.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_shared_core_rank_target.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_SHARED_CORE_RANK_TARGET_PASS
```
