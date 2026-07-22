# Audit - L1 polynomial-led interior cells are deeper-Q curves

## Checked axes

1. Product degree is `m+e` and the cofactor is monic degree `e`.
2. Exactly `w+e` nonleading coefficients must cancel.
3. The first `e` equations solve cofactor coefficients triangularly.
4. The next `w` equations solve locator coefficients recursively.
5. `e<=k` guarantees the requested locator prefix does not exceed degree `m`.
6. The first `e` curve coordinates are the free parameter, so slices are
   distinct.
7. The complement gcd guard is retained slice by slice.
8. The reconstructed codeword has degree below `k`.
9. The exact shell, not merely the raw support census, is decomposed.
10. Ambient density cancels `|B|^e` exactly.
11. The additive one-per-slice term remains `|B|^e`.
12. Nonconstant basis vectors and above-cap excess are not claimed.

## Route effect

All below-cap polynomial-led strict-interior exact cells join the depth-uniform
Q lane.  Independent exact BC is needed only for cells outside this normal
form or for a sharper collective treatment of the curve slices.
