# F3 h=5 central slice fixed-point skeleton

Status: SPARSE DEGREE SKELETON / ROUTE WARNING, NOT `T4-H5-NORM-GATE`.

This packet profiles fixed-point compatibility after applying the central
weighted slice

```text
l5 = 1,
bar_l5 = 1.
```

It does not expand the fixed-point equations.

## Sliced Profile

The unsliced central fixed-point skeleton had total degree bounds

```text
91, 81, 71, 61.
```

After the weighted slice, the four sparse degree bounds become

```text
F1: degree <= 81,
F2: degree <= 72,
F3: degree <= 63,
F4: degree <= 54.
```

Thus the slice lowers the degree bounds by

```text
10, 9, 8, 7.
```

The pre-cancellation term upper bounds do not improve:

```text
F1 <= 1,255,488,415,957,
F2 <=    57,067,651,704,
F3 <=     2,593,979,107,
F4 <=       117,907,944.
```

## Consequence

The weighted slice is a real simplification for degree bookkeeping, but it
does not make direct fixed-point expansion viable.  A central-chart proof
should still preserve the graph structure and use sparse/saturated
compatibility, rather than form the four expanded fixed-point numerators.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_fixedpoint_skeleton.py
```

Expected digest:

```text
H5_CENTRAL_SLICE_FIXEDPOINT_SKELETON_PASS
```
