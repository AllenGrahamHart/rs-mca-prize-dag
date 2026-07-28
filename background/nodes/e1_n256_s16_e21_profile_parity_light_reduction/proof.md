# Proof

Apply the proved sparse L1 slack recurrence at energy 21. For candidate
positive-half L1 norms from 21 down to 10, the pairs `(Delta, relaxed minimum
energy)` are

```text
L:       21  20  19  18  17  16  15  14  13  12  11  10
Delta:    3   7  11  15  19  23  27  31  35  39  43  47
minimum: 53  49  45  41  37  33  29  25  21  17  13   9.
```

The first compatible row is `L=13`, proving `L<=13`. Exact enumeration of
`sum j^2 n_j=21` and `sum j n_j<=13` gives

```text
(5,4) 5; (8,1,1) 9; (1,5) 1; (4,2,1) 5;
(0,3,1) 1; (3,0,2) 5; (5,0,0,1) 5; (1,1,0,1) 1,
```

where the second entry is the number of odd classes.

The signed-chord identity is

```text
21=102-D_64+2C.                                      (3)
```

Hence `D_64` is odd. Heavy-heavy and heavy-light diameter edges contribute
16 and 4 to `D_64`, while each light-light diameter contributes 1. Diameter
edges form a matching, so the four light vertices contain exactly one
light-light diameter.

The remaining five light-light chords generate every odd autocorrelation
class modulo two. A profile can therefore have at most five odd classes,
which excludes `(8,1,1)` and leaves exactly (1).

The proved one-diameter atlas contains 264 normalized supports in 11 orbits
with one odd class and 14,400 supports in 100 orbits with five odd classes.
These are exactly the odd counts used by (1), giving 111 affine templates and
the printed direct-census floor. The light diameter consumes two light
vertices; the remaining matching may contain one heavy-heavy diameter or up
to two heavy-light diameters. Their square-mass contributions give precisely
`D_64 in {1,5,9,17,21}`. Substitution in (3) gives (2). No majorant enters.
QED.
