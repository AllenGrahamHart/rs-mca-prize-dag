# Proof

Fix one actual degree-two outgoing component `H`. Corollary 9.28 colors a
pole-graph edge `e=(j,ell)` by `H` exactly when the horizontal root `j`
at the opposite point of the deck pair lies on `H`. Its exact color-count
formula says that a component of source degree `u` colors `2u` edges.
Here `u=2`, so `H` colors exactly four edges.

The common-five source-facet theorem says that the ten component stars over
`K` are `J-J`. The complete `eta` fiber is `I-I`. At either point over
`ell in L^c`, the outgoing root set consists of five labels in `I` and the
one exchanged neighbor in `J`. Thus a component star there has a `J`
incidence exactly when it contains that exchanged root, and then it is an
`I-J` star.

The definition of the edge coloring pairs that exchanged root with the
unique incident pole-graph edge. Therefore there is a multiplicity-
preserving bijection

```text
colored edges of H <-> J incidences outside K.      (1)
```

For a fixed `j in J`, the edges in `(1)` carrying root `j` are precisely
the colored edges incident to the left pole-graph vertex `j`. Hence

```text
c_j=deg_color(j).                                  (2)
```

The pole graph is two-regular on the left, so `(2)` gives `0<=c_j<=2`.
There are four colored edges, giving `sum_j c_j=4`. This proves
`(KBUC-1)` independently of the component stabilizer and of whether
`L=I` or `|L intersect I|=5`.

The partitions of four with every part at most two are

```text
2+2,       2+1+1,       1+1+1+1.                  (3)
```

Padding each row of `(3)` by zeros to six entries, subtracting from four,
and sorting gives exactly `(KBUC-2)`. In particular every resulting
`d_j=4-c_j` is at least two. The coordinate branch has an additional
fixed-point-free pairing on `J`, so its deficits occur in equal pairs and
only the first and third rows survive there. That extra symmetry is not
used in the universal cut. QED.
