# F3 h=3 repeat loose Stepanov compiler

Status: CONDITIONAL ARITHMETIC COMPILER, NOT A LOOSE-TRIANGLE BOUND.

This packet records the auxiliary-polynomial bookkeeping for the three
loose-triangle targets isolated by the case-split interface.

## Targets

The loose obstruction has been reduced to:

```text
generic:  two ratio parameters (a,b), nine maps 1+c_i(a,b)X in H;
branch A: one ratio parameter a, eight maps 1+c_i(a)X in H;
branch B: one ratio parameter a, eight maps 1+c_i(a)X in H.
```

The degree compilers supply:

```text
generic:  S_total=15,
branch A: S_total=22,
branch B: S_total=24.
```

## Auxiliary

For a target with `m` parameter variables and `k` membership maps, use

```text
Phi(params, X, Y_1,...,Y_k),
deg_param < P       in each parameter variable,
deg_X     < C,
deg_Y_i   < B.
```

The coefficient count is

```text
P^m C B^k.
```

For a repaired family `Z` of parameter values, fix the parameters and impose
multiplicity in the source variable `X`.  Since every map is affine in `X`,
the logarithmic jet recurrence has `k` active affine factors.  The `j<D`
conditions are over-imposed by a reduced polynomial in `X` of degree
`< C+kD`, for each parameter monomial.  Hence the sufficient reduced-condition
count is

```text
D P^m (C+kD) |Z|.
```

Thus the linear-system inequality is

```text
D P^m (C+kD) |Z| < P^m C B^k.          (LOOSE-LS)
```

The parameter box cancels from this crude count; the parameter variables matter
for the missing rank/nonvanishing theorem, not for this over-imposed
condition-count inequality.

## Degree Bound

Assuming the relevant nonvanishing gate, a fixed parameter fiber contributes
at most

```text
L_X / D,        L_X = C-1 + k n (B-1),
```

points in `X`, because the cleared substituted polynomial has `X`-degree at
most `L_X`.

The total degree of the cleared substituted polynomial is bounded by

```text
m(P-1) + (C-1) + n(B-1)S_total.
```

## Missing Gates

The compiler does not prove any loose-line theorem.  The remaining gates are:

```text
LOOSE-GEN-RANK/NV: generic two-parameter nine-map target;
LOOSE-A-RANK/NV:   branch A one-parameter eight-map target;
LOOSE-B-RANK/NV:   branch B one-parameter eight-map target.
```

Under the appropriate gate and `(LOOSE-LS)`,

```text
sum_{z in Z} T_z < |Z| (C-1+k n(B-1))/D.
```

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_stepanov_compiler.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_STEPANOV_COMPILER_PASS
```
