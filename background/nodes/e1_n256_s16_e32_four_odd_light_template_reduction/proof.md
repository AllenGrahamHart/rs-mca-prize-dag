# Proof

For either surviving profile, exactly four non-diameter autocorrelation
coefficients are odd. Modulo two, these are precisely the light-light distance
classes occupied an odd number of times. The parent theorem allows zero or two
light-light diameters.

Translate one light position to zero and enumerate the other three positions
in increasing order. Among the `binom(127,3)=333,375` normalized supports,
exactly 28,800 have zero or two diameters and exactly four odd non-diameter
classes. Every retained support has zero diameters. Its six distance
multiplicities are exactly

```text
2,1,1,1,1.                                           (1)
```

In every retained support, the two edges in the repeated class share a
vertex. If the repeated edges are `{x,y}` and `{y,z}`, then their circular
distances are equal, so after choosing orientations the three light vertices
form a progression around `y`. No disjoint repeated-edge matching survives.

For each support, translate each of its four vertices to zero and multiply by
each of the 64 odd units modulo 128. Taking the lexicographically least image
gives 148 canonical representatives. Their normalized orbit sizes have the
histogram (1) in the statement, whose weighted sum is

```text
4*32 + 16*64 + 40*128 + 88*256 = 28,800.             (2)
```

The independent replay enumerates positive circular gap compositions rather
than vertex triples. It constructs the normalized affine orbit of every
printed representative, proves those 148 orbits disjoint, and proves their
union equals all 28,800 valid supports. It independently checks zero
diameters, multiplicities (1), and the repeated-wedge condition.

With no light-light diameter, write `d_2,d_4` for the heavy-light and
heavy-heavy diameter counts. Matching capacity gives

```text
(d_2,d_4) in {(0,0),(1,0),(2,0),(3,0),(0,1),(1,1)}.
```

Thus `D_64=4d_2+16d_4` gives the six values in (2), and the signed-chord
identity `32=102-D_64+2C` gives the displayed cross sums. QED.
