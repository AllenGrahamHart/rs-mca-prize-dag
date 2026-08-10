# K3 exact active-allocation inequality

- **status:** CONDITIONAL
- **gate:** all
- **unit:** distinct affine slopes under the active first-match owner

Conditional on the three wired premises, print without floating point:

```text
U_positive
U_geometry
U_K3 = U_positive + U_geometry
U_K3_allocation
U_K3 <= U_K3_allocation
```

Each integer must be bound to the exact active KoalaBear `m=2,r=4` row,
partition manifest, owner convention, and proof-certificate digest. Every
nonzero route payment must already include its exact relevant-line
multiplicity and bridge multiplicity; this node may not silently normalize or
omit either. The joint reserve `274980728110413983` is not a K3-only
allocation unless the sibling `U_Q` and `U_new` cells are proved zero.

## Falsifier

An over-budget exact total, a mismatched manifest, row, or partition cell, an
unpinned input, or any change of owner, unit, or multiplicity between payment
and allocation.
