# F3 h=3 repeat loose branch slope maps

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet writes the two normalized loose collision branches as explicit
one-parameter slope families.

## Branches

Let

```text
D(a)=a^2+a+1.
```

The two branch representatives are

```text
branch A: b = a(a+1)/D(a),
branch B: b = -(2a^2+2a+1)/D(a).
```

Substituting these formulas into the nine affine slopes produces exactly one
forced duplicate in each branch:

```text
branch A: C_b  = L_a,
branch B: C_1b = L_a.
```

Away from the secondary-collision subcells recorded in the branch
parametrization packet, each branch is therefore an eight-slope target.

## Degree Budgets

The replay emits the eight unique slope maps for each branch.  The degree
budgets are:

```text
branch A: max numerator degree 4, max denominator degree 4;
branch B: max numerator degree 6, max denominator degree 6.
```

Thus the loose-triangle special branches do not fall back into the original
degree-2 rich-curve template.  They are still explicit one-parameter rational
slope families, and the future counting theorem can target them directly.

## Role in h=3

The current `H3-NO-LOOSE-TRIANGLE` interface is:

```text
generic:  two-parameter nine-slope affine-line target;
branch A: one-parameter eight-slope target with slope degree <= 4;
branch B: one-parameter eight-slope target with slope degree <= 6.
```

Proving these three targets would close the loose-triangle obstruction in the
repeat-boundary star theorem.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_branch_slope_maps.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_BRANCH_SLOPE_MAPS_PASS
```
