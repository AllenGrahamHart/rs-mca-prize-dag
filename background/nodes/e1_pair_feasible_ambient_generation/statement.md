# E1 pair-feasible ambient generation

- **status:** PROVED
- **closure:** proof plus exact arithmetic

At any of the six named clean predecessor anchors, let `F=F_q` be the ambient
MCA slope field, let `Q` be the canonical cyclic quotient root set of order
`N in {256,512}`, and put

```text
B=F_p(Q),  b=|B|.
```

If the E1 collision-pair compiler is feasible, namely

```text
b>=b_pair_min(K,B*),
```

then

```text
B=F.
```

Indeed, every one of the six exact `b_pair_min` values is strictly larger
than `2^128` (the smallest has 134 bits). A proper subfield of an official
field `F_q` with `q<2^256` has size below `2^128`, so it cannot be
pair-feasible.

Thus the open exact pair-collision target has no generated-field transfer
axis on these anchors: it concerns quotient roots that generate the complete
ambient field. Proper generated-subfield rows remain in the direct-image-only
or direct-E1-impossible branches of the universal unsafe router.
