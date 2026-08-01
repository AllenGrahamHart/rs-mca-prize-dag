# Proof

With all four singleton signs negative, the outside products are

```text
-ce, -cf, -de, -df, -d^2, ef, -ef.
```

If `sigma*ef=m`, then `f=sigma*m/e`; the unforced member of the `EF` pair is
`-m`.  Remove the forced record, form factors `X-uZ`, and clear the two
occurrences of `e` in the denominator.  This gives `(KB41EP-1)`.  Since an
outside representative is nonzero, multiplication by `e^2` preserves the
guarded solution set.

Sparse quotient multiplication gives three 19-term equations for each
`sigma`.  Project each system to the two cubic common fields and replay the
six common quotient relations.  In all four `(sigma,component)` cases,
grevlex Buchberger reduction completes after 435 S-pairs.  The resulting
basis contains the monic one-term polynomial `e`.  Thus the saturation of
each ideal by `e` is the unit ideal.  No guarded product realization exists.
QED.
