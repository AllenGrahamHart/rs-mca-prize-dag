# Proof

The energy bound gives `L<=19`. Put `Delta=19+66-4L`. The proved relaxed
slack recurrence gives

```text
L       19  18  17  16  15  14  13  12  11
Delta    9  13  17  21  25  29  33  37  41
min E   51  47  43  39  35  31  27  23  19.
```

Thus `L<=11`. Exact enumeration of `sum j^2 n_j=19` and
`sum j n_j<=11` gives

```text
(3,4) 3; (6,1,1) 7; (2,2,1) 3; (1,0,2) 3; (3,0,0,1) 3,
```

where the second entry is the number of odd classes.

The signed-chord identity is `19=102-D_64+2C`, so `D_64` is odd.
Heavy-heavy and heavy-light diameter edges contribute even square mass;
hence the matching of diameter edges contains exactly one light-light edge.
The five remaining light-light edges generate every odd autocorrelation
class modulo two, so there are at most five. This excludes `(6,1,1)`.

All four survivors have three odd classes. The proved one-diameter atlas has
exactly 960 such normalized supports in eight affine orbits. Each orbit
leaves `binom(124,3)` heavy supports and 64 relative sign vectors, yielding
the printed floor. The complete diameter ledger is

```text
(D_64,C)=(1,-41),(5,-39),(9,-37),(17,-33),(21,-31).
```

The source-pinned Modal derivation and a separately structured checker agree
on every slack value, profile, diameter ledger, atlas count, and route total.
