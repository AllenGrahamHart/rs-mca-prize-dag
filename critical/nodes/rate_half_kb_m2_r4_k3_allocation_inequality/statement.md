# K3 exact active-allocation inequality

- **status:** TARGET
- **unit:** distinct affine slopes under the active first-match owner

Print, without floating point,

```text
U_positive
U_sourcecover
U_K3 = U_positive + U_sourcecover
U_K3_allocation
U_K3 <= U_K3_allocation
```

Each integer must be bound to the exact active KoalaBear `m=2,r=4` row,
partition manifest, owner convention, and proof-certificate digest. Every
nonzero route payment must already include its exact relevant-line
multiplicity; this leaf may not silently normalize or omit it.

## Falsifier

An over-budget exact total, a mismatched manifest or row, an unpinned input,
or any change of owner or unit between payment and allocation.
