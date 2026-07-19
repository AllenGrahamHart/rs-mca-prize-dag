# F3 h=3 conic H3-ACT(4096) kernel-bundle reduction

Status: PROVED GEOMETRIC REDUCTION / RETUNED SLOPE ARITHMETIC, NOT `RC-RANK`.

This packet carries the conic kernel-bundle reduction to the retuned
`H3-ACT(4096)` exact-profile boxes.

## Setup

Use the same boxed product series as
`F3_H3_CONIC_KERNEL_BUNDLE_REDUCTION.md`:

```text
W = span{R_U^b1 R_V^b2 R_W^b3 R_Q^(M-b1-b2-b3) : 0 <= b_i < B}
    <= H0(P^1, O(d)),
d = 6H(B-1).
```

For the kernel bundle

```text
0 -> M_W -> W tensor O -> O(d) -> 0,
M_W = direct sum_i O(-e_i),
```

the exact codimension formula remains

```text
codim image(H0(O(A-1)) tensor W -> H0(O(d+A-1)))
  = sum_i max(e_i - A, 0).
```

Thus the retuned conic rank theorem is reduced to the splitting-excess bound

```text
sum_i max(e_i - A, 0) <= 2899.
```

## Retuned Official Slope Arithmetic

The `H3-ACT(4096)` exact-profile floor uses

```text
Z_4096_floor = 2112..1370944.
```

The corresponding boxes have much larger `B` than the older `H3-ACT(16)`
boxes.  If the `B^3` boxed base products are independent, then the kernel
bundle has rank `B^3-1` and total splitting degree `d`.  The replay verifies
on every official row:

```text
ceil(d/(B^3-1)) <= A.
```

The tight row is the first official row:

```text
s=13: A=2953, B=187,
      ceil(d/(B^3-1)) = 2,
      A - ceil(d/(B^3-1)) = 2951.
```

Since the retuned codimension allowance is `2899`, the tight balanced-slope
margin exceeds the allowance by `52`.

## Role

Compared with the earlier exact-profile kernel-bundle reduction, this retuned
target is a better fit for the official-row F3 objective:

```text
old exact-profile target:       excess <= 1847
H3-ACT(4096) floor target:      excess <= 2899
balanced-slope margin:          at least 2951
```

This still does not prove balanced splitting, independence of the boxed base
products, or the required excess bound.  It sharpens the theorem that would
close the conic rank/nonvanishing route under the weaker official-row
activation target.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_conic_kernel_bundle_4096_reduction.py
```

Expected digest:

```text
H3_CONIC_KERNEL_BUNDLE_4096_REDUCTION_PASS
```
