# KoalaBear m3 primitive-outer degree-two router

- **status:** PROVED
- **scope:** five residual inner-degree-three transverse types
- **dependencies:** `rate_half_kb_m4_adjacency_genus_exclusion`,
  `rate_half_kb_q6_u2_primitive_subdegree4_route_cut`,
  `rate_half_kb_decomposition_source_pencil_compiler`,
  `rate_half_kb_m6_scott_cartesian_degree2_router`,
  `rate_half_kb_m12_secondary_degree5_decomposition_exclusion`
- **consumer:** `rate_half_band_closure`

For an inner-degree-three transverse terminal, the outer map has degree 20
and the five possible outer-correspondence types are

```text
(r,delta)=(2,6),(3,4),(4,3),(6,2),(12,1).           (KBM3-1)
```

The complete primitive degree-20 catalogue consists of

```text
PSL(2,19), PGL(2,19), A20, S20.
```

Every group is two-transitive in its degree-20 action and has subdegrees
`1,19`. None can support an outer component of any size in `(KBM3-1)`.
Thus the outer map decomposes.

A proper right factor has degree `d in {2,4,5,10}`, giving the endpoint an
inner decomposition of degree `3d in {6,12,15,30}`. The degree-12 row is
empty, degree 15 is excluded by the source/Riemann--Hurwitz profile,
degree 30 refines to degree six, and every degree-six producer is impossible
or has an inner-degree-two decomposition. Therefore every inner-degree-three
producer is impossible or also has an inner-degree-two decomposition.

Inner degree three is not an independent producer. The independent
transverse frontier consists of the three degree-two types

```text
(r,delta)=(2,4),(4,2),(8,1).
```

No assertion is made that an endpoint cannot possess an additional
degree-three decomposition. No owner charge moves.

## Falsifier

A missing primitive degree-20 group, a primitive group with subdegree
`2,3,4,6`, or `12`, another proper right-factor degree, or a surviving
degree-`6,12,15,30` destination without an inner-degree-two route.
