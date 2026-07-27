# Proof

The heavy-template theorem says that all three generic heavy-heavy distance
classes are singleton classes and each contains a heavy-light chord. Thus the
light support meets all three corresponding weld sets.

Translations act by multiplication of the coefficient polynomial by a
monomial, and odd units act by the cyclotomic automorphisms `X->X^u` of
`Z[X]/(X^128+1)`. Reduction may change coefficient signs but preserves their
magnitudes. These affine transformations also preserve conductor,
autocorrelation magnitudes, and `M_3`. It is therefore enough to classify
generic heavy triples under this affine odd-unit action.

The primary classifier enumerates all `binom(128,3)` heavy triples, retains
the 325,376 triples having three distinct non-diameter lengths, and maps every
one to the lexicographically least image obtained by choosing a translated
heavy origin and an odd unit. The independent audit instead stores the exact
generic triple set, generates each seed's complete 8,192-element affine image
set, removes that orbit, and repeats. They agree on all 57 canonical
representatives and every orbit size.

For each representative both implementations reconstruct `W_1,W_2,W_3`
directly from circular distance. The checker independently repeats this step.
If `U` denotes union, the number of four-light supports meeting all three sets
is

```text
binom(125,4)
- sum_i binom(125-|W_i|,4)
+ sum_{i<j} binom(125-|W_i union W_j|,4)
- binom(125-|W_1 union W_2 union W_3|,4).
```

The three exact shape rows in the statement follow. No row has a triple weld
intersection, so at least two light positions pay the three classes. Summing
the exact support count times four heavy-sign and sixteen light-sign choices
over the 57 representatives gives 243,285,056. QED.
