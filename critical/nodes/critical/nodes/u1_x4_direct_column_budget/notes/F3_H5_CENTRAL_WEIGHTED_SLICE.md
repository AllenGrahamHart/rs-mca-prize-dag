# F3 h=5 central weighted slice

Status: PROVED ALGEBRAIC NORMALIZATION COMPILER, NOT `T4-H5-NORM-GATE`.

This packet records a safe central-chart normalization for algebraic emptiness
proofs.  It must not be confused with the official finite-row scaling action.

## Algebraic Action

The h=5 reciprocal equations are homogeneous for the weights

```text
l5,l6,l7,l8,l9           = 5,4,3,2,1
bar_l5,bar_l6,...,bar_l9 = -5,-4,-3,-2,-1.
```

The central unit

```text
l5 * bar_l5 = 1
```

has weight zero.  Therefore, for an algebraic solution on the central chart
`l5*bar_l5 != 0`, one may pass over an algebraic extension and choose a
weighted scaling parameter with `tau^5*l5=1`.  The same action then sends
`bar_l5` to `1` as well.  Thus an emptiness proof may work on the slice

```text
l5 = 1,
bar_l5 = 1.
```

This is only an algebraic slice.  It does not replace the official-row
`mu_n` scaling action, and it must not be used for orbit counts or row
certificates.

## Central Graph Slice

On the central chart, the four equations `Cj5` solve the four conjugate
variables:

```text
C15 -> bar_l9,
C25 -> bar_l8,
C35 -> bar_l7,
C45 -> bar_l6.
```

After slicing by `l5=bar_l5=1`, the equations become

```text
P_j(l6,l7,l8,l9) - d_j * bar_l(10-j) = 0.
```

The replayed slice profile is:

```text
C15: 23 terms, degree 9,
C25: 19 terms, degree 8,
C35: 14 terms, degree 7,
C45: 11 terms, degree 6.
```

The total term count remains `67`, but the maximum central equation degree
drops from `10` in the unsliced graph to `9` on the normalized slice.

## Role in h=5

The h=5 norm gate remains open.  This packet only improves the next symbolic
attack surface:

```text
central chart target:
  prove no official-row solution exists by proving no algebraic solution
  exists on the weighted slice l5=bar_l5=1.
```

If such an algebraic contradiction is proved on the slice, it pulls back to the
original central chart.  Conversely, finite-row counting and stabilizer claims
must still use the official scaling-action packet.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_central_weighted_slice.py
```

Expected digest:

```text
H5_CENTRAL_WEIGHTED_SLICE_PASS
```
