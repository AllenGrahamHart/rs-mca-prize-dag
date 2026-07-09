# F3 h=5 central slice quadratic normal form

Status: LOCAL ALGEBRAIC NORMAL FORM / ROUTE GUIDE, NOT `T4-H5-NORM-GATE`.

This packet extends the central weighted-slice tangent compiler by preserving
the graph structure and composing only through total degree two.  It does not
form the full fixed-point numerators.

## Quadratic Graph

On the slice

```text
l5 = bar_l5 = 1
```

write the free variables as

```text
l6,l7,l8,l9.
```

The graph map, ordered compatibly with conjugation, has degree-two truncation

```text
G_l6 = (2 l6 l8 + l7^2 + 2 l9)/4,
G_l7 = (4 l6 l7 + 4 l8 - l9^2)/8,
G_l8 = (l6^2 + 2 l7 - l8 l9)/4,
G_l9 = (4 l6 - 2 l7 l9 - l8^2)/8.
```

The compiler composes these graph components using simultaneous substitution;
ordinary sequential substitution gives the wrong tangent because the graph
components contain the same variables.

## Fixed-Map Normal Form

Through degree two, the relaxed fixed-point map is

```text
F_l6 = l6/4,
F_l7 = (3 l6^2 + 8 l7)/32,
F_l8 = (3 l6 l7 + 4 l8)/16,
F_l9 = (6 l6 l8 + 3 l7^2 + 8 l9)/32.
```

Thus the fixed equations are `3/4` times the triangular quadratic system

```text
l6 = 0,
l7 - l6^2/8 = 0,
l8 - l6 l7/4 = 0,
l9 - l6 l8/4 - l7^2/8 = 0.
```

This is consistent with the tangent packet: the linear fixed-equation
determinant is still

```text
81/256.
```

## Role in h=5

The central slice has no infinitesimal fixed branch through the normalized
origin, and its degree-two relaxed fixed equations are triangular.  This does
not prove global central-chart emptiness, but it gives a sharper local normal
form for any future sparse/saturated central-chart proof.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_quadratic_normal_form.py
```

Expected digest:

```text
H5_CENTRAL_SLICE_QUADRATIC_NORMAL_FORM_PASS
```
