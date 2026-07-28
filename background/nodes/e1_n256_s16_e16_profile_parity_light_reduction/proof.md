# Proof

The energy bound gives `L<=16`. Put `Delta=16+66-4L`. The proved relaxed
slack recurrence gives

```text
L       16  15  14  13  12  11  10
Delta   18  22  26  30  34  38  42
min E   40  36  32  28  24  20  16.
```

Thus `L<=10`. Exact enumeration of `sum j^2 n_j=16` and
`sum j n_j<=10` gives

```text
(4,3) 4; (7,0,1) 8; (0,4) 0; (3,1,1) 4; (0,0,0,1) 0,
```

where the second entry is the number of odd classes.

The signed-chord identity is `16=102-D_64+2C`, so `D_64` is even. Diameter
edges form a matching on the four light vertices, hence there are zero or two
light-light diameter edges. With two, the light support is two antipodal
pairs and has no odd classes. With zero, the six light-light chords generate
every odd class modulo two, and an even number of odd classes is at most six.
This excludes `(7,0,1)`.

The four survivors have zero or four odd classes. The proved even-parity atlas
has 63 zero-odd supports in six affine orbits and 28,800 four-odd supports in
148 affine orbits. Each orbit leaves `binom(124,3)` heavy supports and 64
relative sign vectors, yielding the printed floor. The complete diameter
ledger is

```text
zero light diameters: (D_64,C)=(0,-43),(4,-41),(8,-39),
                                   (12,-37),(16,-35),(20,-33);
two light diameters:  (D_64,C)=(2,-42),(18,-34).
```

The source-pinned Modal derivation and a separately structured checker agree
on every slack value, profile, diameter ledger, atlas count, and route total.
