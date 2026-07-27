# Proof

## L1 and cubic reductions

Apply the proved sparse L1 slack dynamic program at energy 25. For candidate
positive-half L1 norms from 22 down to 11, the pairs `(Delta, relaxed minimum
energy)` are

```text
L:       22  21  20  19  18  17  16  15  14  13  12  11
Delta:    3   7  11  15  19  23  27  31  35  39  43  47
minimum: 53  49  45  41  37  33  29  25  21  17  13   9.
```

The first compatible row is `L=15`, proving `L<=15`.

For the fixed Hermite basis in the collision-norm criterion, exact
substitution at `V=50` gives opposite certified signs at

```text
M_3=13: (73183/79507, 6324/79507, -21213/491834),
M_3=14: (73185/79507, 6322/79507, -31784/737751).
```

Twelve-term rational atanh bounds independently certify the signs, so the
exact cutoff is 13. All 12 profiles exceed it in the layer-cap relaxation:

```text
cap   profile          odd classes
1310  (5,5)                 5
1190  (8,2,1)               9
1178  (1,6)                 1
1054  (4,3,1)               5
 954  (7,0,2)               9
 950  (0,4,1)               1
 846  (3,1,2)               5
 830  (9,0,0,1)             9
 714  (5,1,0,1)             5
 630  (1,2,0,1)             1
 506  (0,0,1,1)             1
 250  (0,0,0,0,1)           1.
```

## Parity, diameter, and route size

The signed-chord identity is

```text
25=102-D_64+2C.                                      (3)
```

Hence `D_64` is odd. Heavy-heavy and heavy-light diameter edges contribute
16 and 4 to `D_64`, while each light-light diameter contributes 1. Diameter
edges form a matching, so the four light vertices contain exactly one
light-light diameter.

The remaining five light-light chords generate every odd autocorrelation
class modulo two. A profile can therefore have at most five odd classes.
Deleting the three nine-odd profiles leaves exactly (1).

The proved one-diameter atlas contains 264 normalized supports in 11 orbits
with one odd class and 14,400 supports in 100 orbits with five odd classes.
These are exactly the odd counts used by (1), giving 111 affine templates and
the printed direct-census floor. The light diameter consumes two light
vertices; the remaining matching may contain one heavy-heavy diameter or up
to two heavy-light diameters. Their square-mass contributions give precisely
`D_64 in {1,5,9,17,21}`. Substitution in (3) gives (2). QED.
