# Proof

The energy bound gives `L<=18`. Put `Delta=18+66-4L`. The proved relaxed
slack recurrence gives

```text
L       18  17  16  15  14  13  12
Delta   12  16  20  24  28  32  36
min E   42  38  34  30  26  22  18.
```

Thus `L<=12`. Exact enumeration of `sum j^2 n_j=18` and
`sum j n_j<=12` gives

```text
(6,3) 6; (9,0,1) 10; (2,4) 2; (5,1,1) 6;
(1,2,1) 2; (0,0,2) 2; (2,0,0,1) 2,
```

where the second entry is the number of odd classes.

The signed-chord identity is `18=102-D_64+2C`, so `D_64` is even.
Heavy-heavy and heavy-light diameter edges contribute even square mass;
hence the diameter matching contains zero or two light-light edges. With two,
the light support is two antipodal pairs and has zero odd classes. With none,
its six light-light edges generate every odd class modulo two, so there are at
most six. This excludes `(9,0,1)`.

The complete two-odd and six-odd atlases contain 8,168 and 280,720 normalized
supports in 87 and 1,234 affine orbits. Each orbit leaves `binom(124,3)` heavy
supports and 64 relative sign vectors, yielding the printed floor. The
complete diameter ledgers are

```text
zero light diameters: (D_64,C)=(0,-42),(4,-40),(8,-38),
                                (12,-36),(16,-34),(20,-32);
two light diameters:  (D_64,C)=(2,-41),(18,-33).
```

The source-pinned Modal derivation and separately structured checker agree on
every slack value, profile, matching ledger, atlas count, and route total.
