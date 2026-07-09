# F3 h=3 repeat loose branch geometry

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet records the shared geometry of the two normalized loose collision
branches.  It is not a loose rank/nonvanishing theorem; it sharpens the input
to `LOOSE-A-RANK/NV` and `LOOSE-B-RANK/NV`.

## Complement Relation

The two branch parametrizations have the same denominator

```text
D(a)=a^2+a+1
```

and satisfy the exact identity

```text
b_A(a) = a(a+1)/D(a),
b_B(a) = -(2a^2+2a+1)/D(a) = -1-b_A(a).
```

Thus the two branches are linked by a fixed-parameter complement, but this is
not enough to identify their full eight-slope targets.

## Ramification

For both branches,

```text
db/da has denominator D(a)^2
```

and the only finite derivative factor is `2a+1`, up to sign.  The compiler
also forms the full pairwise distinctness product for the six reciprocal
multipliers

```text
1, a, b, -1-a, -1-b, -a-b.
```

For each branch, `2a+1` appears in that distinctness product.  Hence the only
finite branch-map ramification point is already outside the active loose
domain, because it forces `a=-1-a`.  The point at infinity is outside the
affine parameter chart used by the finite-row target.

The replayed finite guardrails check the same conclusion over
`p=5,7,11,13,17,97`.

## Shared Slope Maps

Comparing the eight unique slope maps on the clean loci gives exactly six
shared maps:

```text
branch_A.C_1  = branch_B.C_1,
branch_A.C_a  = branch_B.C_a,
branch_A.C_b  = branch_B.C_1b,
branch_A.C_1a = branch_B.C_1a,
branch_A.C_1b = branch_B.C_b,
branch_A.L_b  = branch_B.L_b.
```

The two private maps on each branch are `C_ab` and `L_ab`.  These are the
source of the remaining difference between the branch degree budgets:

```text
branch A: S_total=22,
branch B: S_total=24.
```

## Role in h=3

This rules out a hidden branch-map singularity as the reason the loose
rank/nonvanishing gates remain open, and it explains exactly how much of a
future branch-A argument can be reused for branch B.  A proof that only uses
the six shared maps will transfer immediately; a proof using the full
eight-map target still has to handle the private `C_ab` and `L_ab` maps on
both branches.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_branch_geometry.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_BRANCH_GEOMETRY_PASS
```
