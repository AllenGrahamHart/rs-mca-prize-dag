# Proof

The excess multistar ladder gives `m>=11` whenever `P(t)>=25`. Let `N_4,N_6`
count all distance-four and distance-six edges in the small-representation
fiber, and put

```text
W=2N_4+N_6.
```

Suppose first that the target is antipodal-free. Every small representation
is generic of squared norm three. The centroid deficit and distance-two
exclusion give

```text
W>=ceil(m(m-4)/2).                                  (1)
```

The oriented distance-four pseudoforest gives `N_4<=m`. At most six
distance-six edges have overlapping signed support. Subtracting both strata
from `(1)` proves

```text
D_6>=W-2N_4-6>=ceil(m(m-4)/2)-2m-6,
```

which is `(DSM1)`.

Now suppose the fiber contains its unique antipodal representation. Its
squared norm is one, while all `m-1` generic representations have squared
norm three. The norm-aware centroid calculation therefore improves `(1)` to

```text
W>=ceil(m(m-2)/2).                                  (2)
```

The complete distance-four cap is `N_4<=2(m-1)`. At most six overlapping
generic--generic distance-six edges and two edges incident to the antipodal
vertex remain outside the disjoint stratum. Hence

```text
D_6>=W-2N_4-8>=ceil(m(m-2)/2)-4(m-1)-8,
```

proving `(DSM2)`.

Both right sides are increasing for `m>=11`. At the endpoint,

```text
D_0(11)=39-22-6=11,
D_A(11)=50-40-8=2,
```

which proves `(DSM3)`. Eleven edges on eleven generic vertices force maximum
degree at least two. This gives the two-leaf star in the antipodal-free
class. The antipodal bound directly supplies two distinct generic--generic
edges in the other class.

All four normalized differences in `(DSM4),(DSM5)` are cyclotomic integers.
At the degree-one row-prime ideal selected by the actual subgroup root, every
represented shifted product has residue `t`. Every displayed generator
therefore lies in that prime ideal. The cross generator in `(DSM5)` enforces
that the two edge collisions occur at one target; it is redundant only when
the chosen edge centers coincide. Ideal-norm divisibility gives the asserted
factor `p`.

Finally assume `P(t)>=33`. The excess ladder gives `m>=15`. On the
antipodal-free branch, `(DSM1)` and `m>=15` imply

```text
2D_6/m >=(m^2-8m-12)/m>6,
```

because `m^2-14m-12>0` for `m>=15`. The maximum disjoint distance-six degree
is therefore at least seven. On the antipodal branch the graph has `m-1`
generic vertices, and `(DSM2)` gives

```text
2D_6/(m-1)>4,
```

since `m^2-14m-4>0` for `m>=15`. Its maximum degree is at least five.
Selecting all leaves at either center and applying the same normalized ideal
argument gives the stated pure multistars. QED.
