# Proof

In canonical order the seven outside product records and squared sums are

```text
de, de, -de, df, sigma_o ef, bf, sigma_c cf,
(d+e)^2, (d+e)^2, (d-e)^2, (d+f)^2,
(e+sigma_o f)^2, (b+f)^2, (c+sigma_c f)^2.
```

Under `(d,e,f) -> (D,E,F)=(sigma_o e,sigma_o d,f)`, one has

```text
DE=de,                 (D+E)^2=(d+e)^2,
-DE=-de,               (D-E)^2=(d-e)^2,
DF=sigma_o ef,         (D+F)^2=(e+sigma_o f)^2,
sigma_o EF=df,         (E+sigma_o F)^2=(d+f)^2.
```

The `bf` and `sigma_c cf` rows are fixed. Thus the full seven-row atlas is
fixed except for transposing positions 3 and 4. Deleting `xi=4` before the
map and `xi=3` after it gives identical six-row lists in the same order, so
all 15 canonical perfect-matching indices and all three paired equations
are fixed. The missing-product and missing-sum equations agree as well.

The map permutes `d,e` and multiplies both by the unit `sigma_o`. It is an
involution preserving nonzero coordinates and every condition `x != +/- y`
among `(1,b,c,d,e,f)`. Its outside-edge signs return to
`DE=1, DF=1, EF=sigma_o`; the common signs and `sigma_c` are unchanged.

Finally, the 15 common role cells are assignments among the five roles
`LA,AB,AC,BC+,BC-`. The outside `D,E` operation acts trivially on this set,
so it fixes every common role cell, not only the cell-3 instance where the
transport was first used. Source signs are common-role data and are fixed.
The complete-fiber equations depend on an outside row only through the
displayed product and squared-sum records. Hence the map is the claimed
bijection in every role cell. QED.
