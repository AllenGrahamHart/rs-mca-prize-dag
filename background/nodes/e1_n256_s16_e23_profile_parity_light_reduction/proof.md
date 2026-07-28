# Proof

The general chord inequality gives `L<=22`.  With `Delta=23+66-4L`, the proved
relaxed slack recurrence gives

```text
L       22    21  20  19  18  17  16  15  14  13
Delta    1     5   9  13  17  21  25  29  33  37
min E  none   55  51  47  43  39  35  31  27  23.
```

Thus `L<=13`.  Exact enumeration of `sum j^2 n_j=23` and `sum j n_j<=13`
gives

```text
(3,5) 3; (6,2,1) 7; (2,3,1) 3; (5,0,2) 7;
(1,1,2) 3; (7,0,0,1) 7; (3,1,0,1) 3,
```

where the second entry is the number of odd classes.

The signed-chord identity is `23=102-D_64+2C`, so `D_64` is odd.  Heavy-heavy
and heavy-light diameter edges contribute even square mass; therefore the
four light vertices contain exactly one light-light diameter.  The five
remaining light-light edges generate every odd class modulo two, giving at
most five odd classes.  This removes the three seven-odd profiles.

All four survivors have three odd classes.  The proved one-diameter atlas has
exactly 960 such normalized supports in eight affine orbits.  Each orbit
leaves `binom(124,3)` heavy supports and 64 relative sign vectors, yielding the
printed floor.  The source-pinned Modal derivation and an independently
structured checker agree on every slack value, profile, atlas count, and
route total.
