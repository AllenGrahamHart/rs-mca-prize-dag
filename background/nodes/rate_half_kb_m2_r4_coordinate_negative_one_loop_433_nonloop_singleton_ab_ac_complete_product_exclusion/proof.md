# Proof

The paired-product theorem assigns one projective involution to all six
deck-paired product rows.  Substituting the two common pairs `(KB433PX-1)`
in

```text
Gamma yz-Alpha(y+z)-Beta=0                         (KB433PX-5)
```

gives `(KB433PX-2)`.  Its determinant is nonzero by the common product
guards.  Applying the involution to the singleton `b` gives `(KB433PX-3)`;
both mates are finite, distinct from all five common products, and hence
must occur exactly once among the seven outside records.

The outside-skeleton theorem proves that every complete packet uses one of
the signed forms `S0,S1,S2`.  For each form, each sign row, each forced
record `s_j`, and each perfect matching `M` of the other six records, form
the four polynomials

```text
s_j-mate(b),
Gamma yz-Alpha(y+z)-Beta,       {y,z} in M.         (KB433PX-6)
```

These are denominator-free polynomials in `D,E,F`.  Exact Groebner
reduction over the deployed prime gives the reduced basis `[1]` in every
cell.  The counts are

```text
cell 3 and cell 6:
S0: 2 target tuples * 2 cells * 8 signs * 7 forced * 15 matchings = 3360,
S1: 2 target tuples * 2 cells *16 signs * 7 forced * 15 matchings = 6720,
S2: 2 target tuples * 2 cells * 4 signs * 7 forced * 15 matchings = 1680.
```

The primary certificate uses variable order `D,E,F`; the audit repeats all
11,760 ideals in order `F,E,D` and checks soluble and unit synthetic
controls.  Both obtain the same unit census.  Since `(KB433PX-6)` is a
necessary subset of complete negative Vieta interpolation, no common packet
has a complete lift. QED.
