# Proof

Represent the selected affine explanation family by parameter points in
`F^3`.  Each coordinate agreement is an affine hyperplane with a normal in
`F^3`, and every selected point lies on the `m=67474` hyperplanes indexed by
its exact support.

The support-local common-zero bound gives `z<=K-s=0`, so all incident
normals are nonzero.  If a one-dimensional normal span is fixed, the MDS
transversality step leaves at least

```text
w+s-1=67472+2-1=67473
```

incident normals outside it.  Since there are `m=67474` incident normals,
each projective class has size at most one.  The incident normals therefore
give `m` distinct projective points in `PG(2)`.  Same-support pair
noncontainment gives full incident rank, so these points are not all on one
projective line.

It remains to count independent triples in an arbitrary noncollinear set
`S` of `m` projective points.  Choose a line `L` through two points of `S`,
put `q=|S intersect L|`, and put `r=m-q`.  Then `q>=2` and `r>=1`.  A
collinear triple not contained in `L` has zero or one point on `L`.  There
are at most `C(r,3)` triples of the first type.  Every pair off `L`
determines a unique intersection with `L`, so there are at most `C(r,2)`
of the second type.  Thus the number of collinear triples is at most

```text
C(q,3)+C(r,3)+C(r,2)=C(q,3)+C(r+1,3).
```

For `q+r=m`, `q>=2`, and `r>=1`,

```text
C(m-1,3)-C(q,3)-C(r+1,3)
  =(r-1)(C(q,2)-1)+(q-2)C(r-1,2) >= 0.
```

Hence at most `C(m-1,3)` unordered triples are collinear.  The number of
ordered projective bases is therefore at least

```text
m(m-1)(m-2)-6C(m-1,3)=3(m-1)(m-2)=13657614768.
```

Three independent affine hyperplanes in `F^3` meet in at most one point,
so an ordered independent coordinate triple is owned by at most one
selected record.  There are
`n(n-1)(n-2)=1152924803143827456` ordered coordinate triples.  Double
counting gives the stated cap `84416263`, with remainder `2935655472`.
