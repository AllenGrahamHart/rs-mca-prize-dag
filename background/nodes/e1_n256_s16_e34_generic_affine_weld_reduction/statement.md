# E1 N=256 E=34 generic affine-weld reduction

- **status:** PROVED
- **closure:** proof plus two independent complete orbit classifiers

The 325,376 generic heavy-position triples form exactly 57 orbits under
translations and odd cyclotomic units. Every invariant profile, conductor,
and `M_3` question is therefore determined by 57 printed representatives.

For a representative with three distinct non-diameter heavy-heavy lengths,
let `W_1,W_2,W_3` be the light positions forming a heavy-light chord in the
corresponding class. Every residual collision satisfies

```text
L intersects W_i for i=1,2,3.
```

The 57 exact weld ledgers have only three shapes:

```text
rows  |W_i|      pair intersections  triple  union  light supports
 52    4,4,4          1,1,1             0      9       66,405
  4    3,4,4          2,1,1             0      7       72,486
  1    3,4,3          2,1,2             0      5       58,325.
```

The support counts are exact inclusion-exclusion counts among the 125
nonheavy positions. After global sign normalization, four heavy-sign and
sixteen light-sign choices give a complete representative enumeration chamber
of

```text
243,285,056 signed vectors.
```

This is an exact reduction, not an exclusion: the counted vectors still need
the `E=34`, profile `(6,7)`, conductor, and moment filters.
