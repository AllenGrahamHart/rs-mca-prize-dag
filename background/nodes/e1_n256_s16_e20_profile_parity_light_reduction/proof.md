# Proof

The general chord inequality gives `L<=20`. Put `Delta=20+66-4L`. The proved
relaxed slack recurrence gives

```text
L       20  19  18  17  16  15  14  13  12
Delta    6  10  14  18  22  26  30  34  38
min E   52  48  44  40  36  32  28  24  20.
```

Thus `L<=12`. Exact enumeration of `sum j^2 n_j=20` and
`sum j n_j<=12` gives

```text
(4,4) 4; (7,1,1) 8; (0,5) 0; (3,2,1) 4;
(2,0,2) 4; (4,0,0,1) 4; (0,1,0,1) 0,
```

where the second entry is the number of odd classes.

The signed-chord identity is `20=102-D_64+2C`, so `D_64` is even. Diameter
edges form a matching, and the four light vertices have zero or two
light-light diameters. Two diameters make the light support two antipodal
pairs and leave zero odd classes. With no light diameter, the six light-light
edges generate every odd autocorrelation class modulo two, so there are at
most six. This excludes `(7,1,1)`.

The proved exhaustive even-parity atlases contain exactly 63 normalized
zero-odd supports in 6 affine orbits and 28,800 normalized four-odd supports
in 148 affine orbits. Each template leaves `binom(124,3)` heavy supports and
64 relative signs, yielding the printed floor. The complete diameter ledger
is

```text
d_1=0: (D_64,C)=(0,-41),(4,-39),(8,-37),(12,-35),(16,-33),(20,-31);
d_1=2: (D_64,C)=(2,-40),(18,-32).
```

The source-pinned Modal derivation and a separately structured checker agree
on every slack value, profile, diameter ledger, atlas count, and route total.
