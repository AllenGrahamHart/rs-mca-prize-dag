# F3 h=3 repeat loose branch degree compiler

Status: PROVED ARITHMETIC COMPILER.

This packet records denominator-clearing degree bounds for the two special
loose collision branches.

## Membership Maps

On either special branch, outside the finite secondary-subcell locus, the eight
unique slope conditions have the form

```text
1 + c_i(a) X in H.
```

Write

```text
1 + c_i(a) X = P_i(a,X) / Q_i(a),
```

where `Q_i` is independent of `X`.  The branch slope-map compiler supplies the
`c_i(a)` explicitly.  This compiler records the degrees of the resulting
membership maps.

The aggregate budgets are:

```text
branch A: 8 maps, sum_a_degrees=17, sum_total_degrees=22, max_total_degree=5;
branch B: 8 maps, sum_a_degrees=19, sum_total_degrees=24, max_total_degree=7.
```

The secondary-subcell compiler isolates the remaining lower-dimensional
parameters: after stripping structural non-poles, branch A has residual degree
`24` and branch B has residual degree `29`.

## Clearing Formula

For an auxiliary

```text
Phi(a,X,Y_1,...,Y_8),
deg_a Phi < A,
deg_X Phi < C,
deg_{Y_i} Phi < B,
```

and subgroup order `n`, clear denominators with

```text
prod_i Q_i(a)^{n(B-1)}.
```

Let

```text
S_a     = sum_i max(deg_a P_i, deg_a Q_i),
S_total = sum_i max(total_deg P_i, total_deg Q_i).
```

Then the cleared substituted polynomial has degrees bounded by

```text
deg_a     <= A - 1 + n(B-1) S_a,
deg_X     <= C - 1 + 8 n(B-1),
total_deg <= A + C - 2 + n(B-1) S_total.
```

Thus:

```text
branch A: deg_a <= A-1+17n(B-1), total <= A+C-2+22n(B-1);
branch B: deg_a <= A-1+19n(B-1), total <= A+C-2+24n(B-1).
```

## Role in h=3

This is not a nonvanishing theorem.  It is the arithmetic input for a future
two-variable Stepanov/incidence argument on the special loose branches.  The
generic loose branch still has the two-parameter nine-slope target, while the
two collision branches are now explicit degree-budgeted one-parameter rational
membership problems away from a finite secondary set.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_branch_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_BRANCH_DEGREE_COMPILER_PASS
```
