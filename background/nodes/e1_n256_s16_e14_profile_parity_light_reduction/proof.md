# Proof

The energy bound gives `L<=14`. Put `Delta=14+66-4L`. The proved relaxed
slack recurrence gives

```text
L       14  13  12  11  10   9   8   7
Delta   24  28  32  36  40  44  48  52
min E   30  26  22  18  14  10   6  10.
```

Thus `L<=10`. Exact enumeration of `sum j^2 n_j=14` and
`sum j n_j<=10` gives

```text
(6,2) 6; (2,3) 2; (5,0,1) 6; (1,1,1) 2,
```

where the second entry is the number of odd classes. The signed-chord
identity is `14=102-D_64+2C`, so `D_64` is even. Diameter edges form a
matching; exact matching enumeration gives the complete ledgers

```text
zero light diameters: (D_64,C)=(0,-44),(4,-42),(8,-40),
                                      (12,-38),(16,-36),(20,-34);
two light diameters:  (D_64,C)=(2,-43),(18,-35).
```

The resulting parity bound admits all four profiles and no profile with more
than six odd classes. The proved even-parity atlas has 8,168 normalized
two-odd supports in 87 affine orbits and 280,720 normalized six-odd supports
in 1,234 affine orbits. Each orbit leaves `binom(124,3)` heavy supports and 64
relative sign vectors, yielding the printed floor.

The source-pinned Modal derivation and a separately structured checker agree
on every slack value, profile, diameter ledger, atlas count, and route total.
