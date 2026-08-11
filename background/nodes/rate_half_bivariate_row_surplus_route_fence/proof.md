# Proof

The published witness has supported slopes

```text
0, 1, 2, 4, 15
```

with pairwise-disjoint root triples whose union is `F_17^* \ {14}`. Direct
evaluation of `(BRS1)` gives

```text
Q_Y(x)=q_1(x)(Y-gamma_x),
q_1(x)=4x^2+12x!=0
```

at every supported point `x`, where `gamma_x` owns its root triple. At the
omitted point `x=14`, `q_1(14)=0` and `Q_Y(14)!=0`, so that point is the
unique deficit and lies outside every pair union.

Fix two supported slopes. Solving the two minimum-weight representatives
gives the joint representation `(c_0,c_1)` on their six-point union `W`.
The matrix from `(DCK4)` consequently has

```text
(m+2)(4m+1)=15 rows,       |W|=6 columns.
```

The vector

```text
lambda=(q_1(x))_(x in W)
```

has no zero coordinate. The apolar moment identity, checked directly from
the printed syndromes, gives `M_W lambda=0`, so `rank(M_W)<=5`.

For each of the ten pairs, `certificate.json` prints five row indices, one
omitted column, and the nonzero determinant of the resulting `5 x 5` minor.
The determinants are

```text
8, 10, 15, 9, 4, 15, 1, 3, 10, 5    in F_17.
```

Hence every matrix has rank at least five. Combining both inequalities proves
`(BRS2)`. QED.
