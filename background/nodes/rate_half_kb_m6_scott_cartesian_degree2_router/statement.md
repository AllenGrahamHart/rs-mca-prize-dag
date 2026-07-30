# KoalaBear m6 Scott-Cartesian degree-two router

- **status:** PROVED
- **scope:** residual actual KoalaBear `Q=6,s=6,u=2` decomposition branch
- **dependencies:** `rate_half_kb_source_pencil_rank_transverse_compiler`,
  `rate_half_kb_degree5_decomposition_exclusion`
- **consumer:** `rate_half_band_closure`

Every actual terminal inner-degree-six transverse producer either forces an
inner-degree-five decomposition, which is already impossible over the
challenge field, or forces an inner-degree-two decomposition. Therefore
inner degree six is not an independent producer.

For a trivial kernel on the ten original blocks, the complete transitive
degree-ten catalogue leaves four wreath-type actions and `A10,S10`.
The latter two have no primitive degree-six quotient of a point stabilizer.
In each wreath case every primitive degree-six chain has an explicit
intermediate subgroup of index five over the endpoint stabilizer, hence an
inner-degree-five decomposition.

For a nontrivial kernel, Scott strips and the two-transitive degree-six
socles make the four-point transverse orbit lie on synchronized fixed
counterparts. Their compatibility class has size five or ten. Size five
again gives the excluded degree-five row. Size ten gives a degree-ten
column fiber containing the four-point orbit; the primitive degree-ten
catalogue has no subdegree four, so this column map factors to inner
degree two or five. Only degree two can survive.

The six `m=6` types

```text
(r,delta)=(1,24),(2,12),(3,8),(4,6),(6,4),(8,3)
```

cease to be independent producers. Combined with the proved `m=12` close
and `m=10` router, the independent transverse frontier has 12 types in
degrees `2,3,4`. No destination type is paid or deleted here.

## Falsifier

A kernel-free degree-ten chain with no index-five intermediate subgroup, a
degree-six Scott compatibility class of another size that can support a
four-point orbit, or an indecomposable degree-ten column map with
subdegree four.
