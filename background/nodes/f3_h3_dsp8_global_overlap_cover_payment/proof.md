# Proof

The support-overlap theorem proves that every overlapping generic--generic
distance-six edge lies in exactly one of the two canonical covers

```text
x=2u^2/(1+u^2),       y=-u,       v=-2u/(1+u^2),   (1R)
x=(1+y^2)/(2y^2),     u=xy,       v=-1/y.          (1C)
```

The normalization is unique for each edge. In `(1R)` the parameter `u` is a
root of the first endpoint, and in `(1C)` the parameter `y` is a root of the
first endpoint, so every valid parameter belongs to `H`. Each parameter and
cover label determines at most one edge. Thus there are at most `2n` such
edges globally, before imposing the richness filter.

For every retained target, the affine coset-pair theorem gives

```text
R(t)<(51/16)n^(2/3).                                (2)
```

The class weight of a generic edge is at most `17/10`. Hence all selected
generic--generic overlapping edges contribute strictly less than

```text
(17/10)(2n)(51/16)n^(2/3)=(867/80)n^(5/3).         (3)
```

On an antipodal target, at most two additional distance-six edges are
incident to the antipodal vertex. Their class-weighted contribution is at
most

```text
(17/10)(2)S_A=(17/5)S_A.                           (4)
```

Equations `(3)--(4)` prove `(GOP1)`.

Let `D_0,D_A` be the disjoint moments and put

```text
B_(n,6)=300n^2-102Q_n.
```

The proved `E=6` compiler says that C36' follows when the complete weighted
distance-six moment is at most `B_(n,6)/8`. By `(GOP1)`, it is enough that

```text
D_0+(17/10)D_A+(867/80)n^(5/3)+(17/5)S_A
 <=B_(n,6)/8.                                      (5)
```

The primitive shift-pair adapter gives `K_25^c=2D_c`. Multiplying `(5)` by
`20` and substituting this identity gives exactly `(GOP2)`.

The antipodal quotient-mass payment gives

```text
S_A<(51/32)(n-2)n^(2/3).                           (6)
```

Therefore the available right side for the primitive-SP correlation in
`(GOP2)` is strictly greater than

```text
750n^2-255Q_n-(867/8)(n-2)n^(2/3)-(867/4)n^(5/3).
                                                               (7)
```

Since `Q_n<n^2`, `(n-2)n^(2/3)<n^(5/3)`, and every official order has
`n^(1/3)>20`, expression `(7)` is strictly greater than

```text
(495-2601/160)n^2=(76599/160)n^2.                  (8)
```

Thus `(GOP3)` implies `(GOP2)`, completing the proof. QED.
