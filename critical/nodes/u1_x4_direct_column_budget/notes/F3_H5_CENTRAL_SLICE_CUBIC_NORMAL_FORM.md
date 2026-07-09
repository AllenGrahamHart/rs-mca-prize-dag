# F3 h=5 central slice cubic normal form

Status: SYMBOLIC LOCAL NORMAL FORM, NOT AN h=5 CLOSURE.

This packet extends the central weighted-slice fixed-map normal form from
degree two to degree three.  It preserves the same graph/truncation discipline:
the compact central graph is truncated first, then composed simultaneously, so
the huge full fixed-point numerators are never expanded.

## Result

On the slice `l5=bar_l5=1`, with variables `l6,l7,l8,l9`, the fixed equations
`l_i - F_i(l)=0` through total degree three are:

```text
(7*l6^2*l9 - 2*l6*l7*l8 + 48*l6 - 3*l7^3)/64 = 0
-(6*l6^2 - 10*l6*l7*l9 + 3*l6*l8^2 - 7*l7^2*l8 - 48*l7)/64 = 0
(3*l6^3 - 24*l6*l7 + 20*l6*l8*l9 + 6*l7^2*l9 + 26*l7*l8^2 + 96*l8)/128 = 0
(9*l6^2*l7 - 24*l6*l8 + 26*l6*l9^2 - 12*l7^2 + 44*l7*l8*l9 + 6*l8^3 + 96*l9)/128 = 0
```

The linear determinant remains

```text
81/256.
```

The fixed equations have only `4..7` terms through degree three.  This
confirms that the central fixed-point obstruction is still sparse after one
more order and that the quadratic triangular form is not hiding a low-order
branch through the normalized origin.

## Role

This is local information only.  It does not prove central-chart emptiness and
does not assert that the normalized origin is an official finite-row support.
Its value is to give the next symbolic h=5 attack a compact cubic model rather
than the unusable fully expanded fixed-point numerators.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_slice_cubic_normal_form.py
```

Expected digest:

```text
H5_CENTRAL_SLICE_CUBIC_NORMAL_FORM_PASS
```
