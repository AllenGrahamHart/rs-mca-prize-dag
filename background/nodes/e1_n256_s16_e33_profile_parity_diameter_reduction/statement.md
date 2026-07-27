# E1 N=256 square-mass-16 E=33 profile/parity/diameter reduction

- **status:** PROVED
- **closure:** proof plus exact arithmetic

Let a pair-feasible folded-profile `(3,4,0)` collision at `N=256` have
autocorrelation variance `V=66`, or `E=V/2=33`. Then its positive-half
autocorrelation L1 norm satisfies

```text
L<=19.
```

Among the 21 integer magnitude profiles with energy 33 and `L<=19`, the
exact cubic-Hermite norm certificate excludes every profile except

```text
(5,7), (1,8), (4,5,1), (0,6,1).                       (1)
```

Their respective `(L, number of odd coefficients)` pairs are

```text
(19,5), (17,1), (17,5), (15,1).                       (2)
```

Exactly one of the six light-light support chords is a diameter. Hence

```text
D_64 in {1,5,9,17,21},
C    in {-34,-32,-30,-26,-24},
C=(D_64-69)/2.                                        (3)
```

For either five-odd profile in (1), the five non-diameter light-light chords
occupy five distinct circular distance classes. This is the diameter-Sidon
condition. The theorem is a reduction, not an exclusion of `V=66`.
