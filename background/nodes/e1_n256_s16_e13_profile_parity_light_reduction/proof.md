# Proof

The energy bound gives `L<=13`. Put `Delta=13+66-4L`. The proved relaxed
slack recurrence gives

```text
L       13  12  11  10   9   8   7   6
Delta   27  31  35  39  43  47  51  55
min E   29  25  21  17  13   9   5   9.
```

Thus `L<=9`. Exact enumeration of `sum j^2 n_j=13` and
`sum j n_j<=9` gives

```text
(5,2) 5; (1,3) 1; (4,0,1) 5; (0,1,1) 1,
```

where the second entry is the number of odd classes. The signed-chord
identity is `13=102-D_64+2C`, so `D_64` is odd. Diameter edges form a matching,
and exactly one light-light diameter edge occurs. Exact matching enumeration
gives

```text
(D_64,C)=(1,-44),(5,-42),(9,-40),(17,-36),(21,-34).
```

The proved one-diameter atlas has 264 normalized one-odd supports in 11 affine
orbits and 14,400 normalized five-odd supports in 100 affine orbits. Each orbit
leaves `binom(124,3)` heavy supports and 64 relative sign vectors, yielding
the printed floor.

The source-pinned Modal derivation and a separately structured checker agree
on every slack value, profile, diameter ledger, atlas count, and route total.
