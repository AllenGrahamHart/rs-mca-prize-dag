# Proof

The energy bound gives `L<=17`. Put `Delta=17+66-4L`. The proved relaxed
slack recurrence gives

```text
L       17  16  15  14  13  12  11
Delta   15  19  23  27  31  35  39
min E   41  37  33  29  25  21  17.
```

Thus `L<=11`. Exact enumeration of `sum j^2 n_j=17` and
`sum j n_j<=11` gives

```text
(5,3) 5; (8,0,1) 9; (1,4) 1; (4,1,1) 5;
(0,2,1) 1; (1,0,0,1) 1,
```

where the second entry is the number of odd classes.

The signed-chord identity is `17=102-D_64+2C`, so `D_64` is odd.
Heavy-heavy and heavy-light diameter edges contribute even square mass;
hence the matching of diameter edges contains exactly one light-light edge.
The five remaining light-light edges generate every odd autocorrelation
class modulo two, so there are at most five. This excludes `(8,0,1)`.

The five survivors have one or five odd classes. The proved one-diameter atlas
has 264 one-odd supports in 11 affine orbits and 14,400 five-odd supports in
100 affine orbits. Each orbit leaves `binom(124,3)` heavy supports and 64
relative sign vectors, yielding the printed floor. The complete diameter
ledger is

```text
(D_64,C)=(1,-42),(5,-40),(9,-38),(17,-34),(21,-32).
```

The source-pinned Modal derivation and a separately structured checker agree
on every slack value, profile, diameter ledger, atlas count, and route total.
