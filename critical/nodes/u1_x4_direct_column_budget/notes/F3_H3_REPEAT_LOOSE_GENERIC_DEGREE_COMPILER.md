# F3 h=3 repeat loose generic degree compiler

Status: PROVED ARITHMETIC COMPILER.

This packet records denominator-clearing degree bounds for the generic
two-parameter loose nine-slope target.

## Membership Maps

In the generic loose case the nine affine membership tests are

```text
1 + c_i(a,b) X in H,
```

where the slopes are

```text
1, 1/a, 1/b, -1/(1+a), -1/(1+b), -1/(a+b),
1+1/a-1/(1+a),
1+1/b-1/(1+b),
1/a+1/b-1/(a+b).
```

Write

```text
1+c_i(a,b)X = P_i(a,b,X)/Q_i(a,b).
```

The replay verifies `Q_i` is independent of `X` and `deg_X P_i <= 1`.

## Degree Budget

The aggregate budgets are:

```text
9 maps,
S_a     = sum_i max(deg_a P_i, deg_a Q_i) = 7,
S_b     = sum_i max(deg_b P_i, deg_b Q_i) = 7,
S_total = sum_i max(total_deg P_i, total_deg Q_i) = 15.
```

For an auxiliary

```text
Phi(a,b,X,Y_1,...,Y_9),
deg_a Phi < A,
deg_b Phi < B0,
deg_X Phi < C,
deg_{Y_i} Phi < Y,
```

and subgroup order `n`, clearing denominators by

```text
prod_i Q_i(a,b)^{n(Y-1)}
```

gives

```text
deg_a     <= A  - 1 + 7 n(Y-1),
deg_b     <= B0 - 1 + 7 n(Y-1),
deg_X     <= C  - 1 + 9 n(Y-1),
total_deg <= A + B0 + C - 3 + 15 n(Y-1).
```

## Role in h=3

Together with the branch degree compiler, this gives degree budgets for all
three loose-line targets:

```text
generic:  two-parameter nine-map target with S_total=15;
branch A: one-parameter eight-map target with S_total=22;
branch B: one-parameter eight-map target with S_total=24.
```

This is arithmetic input only; it does not prove the required nonvanishing or
incidence theorem.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_generic_degree_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_GENERIC_DEGREE_COMPILER_PASS
```
