# KoalaBear source-pencil rank and transverse compiler

- **status:** PROVED
- **scope:** residual actual KoalaBear `Q=6,s=6,u=2` decomposition branch
- **upstream:** PR `#1131`, head `e287c54252c7872e1745c7594cfef62b74a65cf5`
- **dependency:** `rate_half_kb_decomposition_source_pencil_compiler`
- **consumer:** `rate_half_band_closure`

For every supplied actual endpoint record, the six source-pencil profiles
have exactly 32,099 canonical source partitions. Each partition has a
deterministic source-rank gate and active symmetric-power membership gate;
degree 12 uses its reduced `49 x 5` rank-five, 44-syndrome gate. The number
32,099 is per supplied record, not a finite census of all endpoint records.

After routing every proper right factor, the terminal inner map is
geometrically indecomposable. The actual irreducible bidegree-`(4,4)`
component cannot then lie in the same-inner-fiber divisor: the complete
primitive-group catalogues in degrees `2,3,4,6,10,12` contain no subdegree
four.

Every terminal survivor is therefore transverse. If its image in the outer
self-correspondence has bidegree `(r,r)` and the component-to-image degree is
`delta`, then

```text
delta*r=4m,       delta<=m^2,       r<=60/m-1.       (KBTR-1)
```

The 26 exact `(r,delta)` types are obtained from:

```text
m=2:  r=2,4,8
m=3:  r=2,3,4,6,12
m=4:  r=1,2,4,8
m=6:  r=1,2,3,4,6,8
m=10: r=1,2,4,5
m=12: r=1,2,3,4
```

Exact challenge-field controls show that the source and active divisor gates
alone admit indecomposable degree-two and degree-three pencils. Thus the next
theorem must use the inherited quartic/source-star incidence or owner
semantics; another source-only rank calculation cannot close the branch.

No global endpoint census, transverse-row deletion, parameter-to-carrier
bridge, owner, charge, `u=2` close, cap `68`, adjacent certificate, or row
close is proved. Ledger movement is zero.

## Falsifier

A valid source partition rejected by the rank gates, a terminal primitive
inner monodromy group with subdegree four, a same-fiber terminal quartic, or
a transverse component violating `(KBTR-1)`.
