# Statement

In the complete shortened corank-one kernel chart

```text
(n,K,m)=(1048577,1,67473),
```

every selected record is incident with exactly `m` nonzero normals in a
two-dimensional normal space.  Same-support pair noncontainment forces
those normals to span the space.  Consequently every record owns at least

```text
2(m-1)=134944
```

ordered linearly independent coordinate pairs.  Since an independent pair
determines at most one parameter point, the number of records is at most

```text
floor(n(n-1)/(2(m-1)))=8147918.
```

This improves the generic support-local transversality cap `16295594` by
`8147676` records.
