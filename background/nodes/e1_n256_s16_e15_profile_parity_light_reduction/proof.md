# Proof

The energy bound gives `L<=15`. Put `Delta=15+66-4L`. The proved relaxed
slack recurrence gives

```text
L       15  14  13  12  11  10   9
Delta   21  25  29  33  37  41  45
min E   39  35  31  27  23  19  15.
```

Thus `L<=9`. Exact enumeration of `sum j^2 n_j=15` and
`sum j n_j<=9` gives

```text
(3,3) 3; (6,0,1) 7; (2,1,1) 3,
```

where the second entry is the number of odd classes.

The signed-chord identity is `15=102-D_64+2C`, so `D_64` is odd. Heavy-heavy
and heavy-light diameter edges contribute even square mass, while diameter
edges form a matching. Hence exactly one light-light diameter edge occurs.
The five remaining light-light edges generate every odd autocorrelation class
modulo two, so there are at most five. This excludes `(6,0,1)`.

The two survivors have three odd classes. The proved one-diameter atlas has
960 normalized three-odd supports in eight affine orbits. Each orbit leaves
`binom(124,3)` heavy supports and 64 relative sign vectors, yielding the
printed floor. The complete diameter ledger is

```text
(D_64,C)=(1,-43),(5,-41),(9,-39),(17,-35),(21,-33).
```

The source-pinned Modal derivation and a separately structured checker agree
on every slack value, profile, diameter ledger, atlas count, and route total.
