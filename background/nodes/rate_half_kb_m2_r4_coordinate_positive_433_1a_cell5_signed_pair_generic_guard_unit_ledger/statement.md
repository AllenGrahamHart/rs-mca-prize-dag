# KoalaBear positive 433-1a cell-5 signed-pair generic guard-unit ledger

- **status:** PROVED
- **scope:** deployed characteristic, generic `t`, cell 5, signs
  `(-1,-1)`, chart 2, five squared `DE+/DE-` residue fields
- **consumer:** exceptional-fiber and colored-edge ledger

Let `K=F_2130706433(t)` and let

```text
A_g ~= product_(j=1)^5 K[s]/(phi_j)
```

be the primitive residue decomposition.  Reconstruct the chart-2 common
coordinates `r,c` from the proved rational lift atlas.  On every one of
the five residue fields, each of the 22 declared common-chart guard factors

```text
t-1, t+1, r-1, r+1, r-iota, r+iota,
t-r, t+r, t-iota*r, t+iota*r, t-iota, t+iota,
r, t, b, c, b-1, b+1, c-1, c+1, c-b, b+c
```

is a nonzero element and therefore a unit.

The common source labels in this cell are

```text
1, t^2, r^2, -r^2, -1.
```

For each squared outside coordinate `x_j=z_j^2`, `j=0,1`, the four
necessary squared outside-incidence factors

```text
x_j, x_j-1, x_j-t^4, x_j-r^4                 (KBGU-1)
```

are likewise units in every residue field.  Thus no generic signed-pair
residue component lies entirely on one of these 30 guard hyperplanes.

This does not calculate the guard norms or their exceptional-`t` zeros,
prove that `x_j` is a square in a deployed-field specialization, restore
the unsquared signs or source-slot distinctness, append the colored `BE`
edge, cover other charts or the `DF` family, delete cell 5 or
`433-1a -> O0b`, close K3, or prove either Prize result.

## Falsifier

A residue factor on which one of the 30 printed guards is zero, a pole in
the registered regular specialization, or a failure of the chart-2
`r,c` reconstruction.
