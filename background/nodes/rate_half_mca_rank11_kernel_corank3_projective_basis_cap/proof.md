# Proof

Represent the selected affine explanation family by parameter points in
`F^4`.  Each coordinate agreement is an affine hyperplane with a normal in
`F^4`, and every selected point lies on the `m=67475` hyperplanes indexed by
its exact support.

The support-local common-zero bound gives `z<=K-s=0`, so all incident
normals are nonzero.  For a one-dimensional normal span, the MDS
transversality step leaves at least

```text
w+s-1=67472+3-1=67474=m-1
```

incident normals outside it.  Hence each projective class has size at most
one.  For a two-dimensional normal span, the same step leaves at least

```text
w+s-2=67473=m-2
```

normals outside it.  Thus every projective line contains at most two
incident points: no three are collinear.  Same-support pair noncontainment
gives full incident rank, so the projective set spans `PG(3)`.

It remains to count projective bases in an arbitrary spanning set `S` of
`m` points in `PG(3)` with no three collinear.  Choose three points of `S`;
they determine a plane `H`.  Put `q=|S intersect H|` and `r=m-q`.  Then
`q>=3` and `r>=1`.

Partition coplanar unordered quadruples by their number of points in `H`.
There are `C(q,4)` with four points in `H`, and none with three points in
`H` and one outside.  For a fixed outside pair, its line meets `H` at a
point `x` outside `S`; otherwise those two outside points and `x` would be
collinear members of `S`.  Secants of `S intersect H` through `x` use
disjoint point pairs, so there are at most `floor(q/2)` coplanar inside
pairs.  This contributes at most `floor(q/2)C(r,2)`.  Each outside triple
spans a plane whose intersection with `H` is a line containing at most two
points of `S`, contributing at most `2C(r,3)`.  Finally, the all-outside
quadruples contribute at most `C(r,4)`.  Hence the number `D` of dependent
quadruples is at most

```text
B(q,r)=C(q,4)+floor(q/2)C(r,2)+2C(r,3)+C(r,4).
```

Vandermonde expansion gives the exact difference

```text
C(m-1,4)-B(q,r)
  =(q-3)C(r,3)
   +(C(q-1,2)-floor(q/2))C(r,2)
   +(r-1)C(q-1,3) >= 0.
```

Therefore `D<=C(m-1,4)`.  The number of ordered projective bases is at
least

```text
(m)_fall_4-24C(m-1,4)
  =4(m-1)(m-2)(m-3)
  =1228711865141376.
```

Four independent affine hyperplanes in `F^4` meet in at most one point.
There are

```text
(n)_fall_4=1208932737155751449985024
```

ordered coordinate quadruples.  Double counting gives the stated cap
`983902549`, with remainder `1056607358217600`.
