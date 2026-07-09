# F3 h=5 central slice tangent compiler

Status: LOCAL ALGEBRAIC NORMAL FORM / ROUTE GUIDE, NOT `T4-H5-NORM-GATE`.

This packet extracts the constant and linear parts of the central weighted
slice

```text
l5 = 1,
bar_l5 = 1.
```

It does not expand the fixed-point equations.

## Tangent Graph

On the slice, the four central equations are

```text
bar_l9 = P1(l6,l7,l8,l9) / 16384
bar_l8 = P2(l6,l7,l8,l9) / 16384
bar_l7 = P3(l6,l7,l8,l9) / 256
bar_l6 = P4(l6,l7,l8,l9) / 512.
```

The compiler verifies that all four graph numerators have zero constant term
and linear part

```text
bar_l9 = (1/2) l6 + higher order terms
bar_l8 = (1/2) l7 + higher order terms
bar_l7 = (1/2) l8 + higher order terms
bar_l6 = (1/2) l9 + higher order terms.
```

Equivalently, in the orders

```text
top variables: l6,l7,l8,l9
bar variables: bar_l6,bar_l7,bar_l8,bar_l9
```

the tangent graph matrix is the anti-diagonal matrix with coefficient `1/2`.

## Fixed-Point Linearization

Conjugating the graph uses the same tangent matrix.  Therefore the tangent map
for the relaxed fixed-point operator is

```text
(1/2 J)^2 = 1/4 I,
```

so the linear part of the fixed-point equations is

```text
I - 1/4 I = 3/4 I.
```

The determinant is

```text
(3/4)^4 = 81/256.
```

Thus, away from characteristics `2` and `3`, the normalized origin is a simple
isolated fixed point of the relaxed sliced graph.  In particular, the central
slice has no infinitesimal fixed branch through that origin.

## Caveat

The normalized origin is an algebraic coefficient-space point of the relaxed
central slice.  It is not being asserted to be an official row support.
This packet only records a local normal form that a future central-chart
emptiness proof can use; it does not prove global central-chart emptiness.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_tangent.py
```

Expected digest:

```text
H5_CENTRAL_SLICE_TANGENT_PASS
```
