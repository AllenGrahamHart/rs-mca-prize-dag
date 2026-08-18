# The 218-plane projective direction bank

- **status:** PROVED
- **scope:** the endpoint left by the affine-plane cap 218

If an affine scalar plane contains 218 selected quotient types, let `c` be
its common received-pair core and put `k'=K-c`. Then

```text
1043551<=c<=1046532,
2044<=k'<=5025.                                      (B218-1)
```

After reversible shortening by that actual core, at least

```text
F>=28396+204k'                                       (B218-2)
```

coordinates are full affine-line fibers containing exactly 15 of the 218
types. These full fibers use between 210 and 218 distinct affine lines and
at least 210 distinct projective directions. If `z_eta` counts full
coordinates in direction `eta`, then

```text
sum_eta z_eta>=28396+204k',
z_eta<=k'-1,
sum_eta ((k'-1)-z_eta)<=14k'-28614<=41736.           (B218-3)
```

In particular, aggregate direction-root occupancy is at least

```text
1053496/1095232 = 131687/136904 > 0.9618.            (B218-4)
```

The dual line arrangement has at least 210 multiplicity-15 points and at
most 1603 line-pair intersections outside them.

## Falsifier

A 218-plane with `k'` outside `[2044,5025]`; fewer than 210 full lines or
directions; a direction with more than `k'-1` full coordinates; aggregate
deficit above 41736; or an incorrect dual pair budget.
