# F3 h=3 repeat loose case-split interface

Status: PROVED COMPILER.

This packet composes the normalized loose affine-slope packets into the exact
case split for future counting arguments.

## Interface

A genuine normalized loose obstruction gives affine subgroup tests

```text
1 + c_i X in H.
```

The six coordinate slopes are distinct, the three lambda slopes are mutually
distinct, and all multiplicity loss comes from lambda-coordinate collisions.

The resulting case split is:

```text
Generic:
  no lambda-coordinate collision divisor vanishes;
  the affine line has nine distinct slope conditions.

Collision A:
  after S_3 relabeling, L_a = 1/b;
  b = a(a+1)/(a^2+a+1).

Collision B:
  after S_3 relabeling, L_a = -1/(1+b);
  b = -(2a^2+2a+1)/(a^2+a+1).
```

Secondary subcells inside Collision A or Collision B are exactly the
one-variable pullbacks emitted by the branch-parametrization replay.

## Role in h=3

This is the current clean interface for `H3-NO-LOOSE-TRIANGLE`.  Proving the
generic nine-slope line target and the two one-parameter collision branch
targets would remove the loose-triangle obstruction from the repeat-boundary
star theorem.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_case_split_interface.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_CASE_SPLIT_INTERFACE_PASS
```
