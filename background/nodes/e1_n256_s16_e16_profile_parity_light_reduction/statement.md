# E1 N=256 E=16 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact finite classification

For an `N=256`, folded-profile `(3,4,0)` candidate at variance `V=32`, or
energy `E=16`, the positive-half autocorrelation L1 norm satisfies `L<=10`.
Exactly five magnitude profiles meet the energy/L1 constraints. Diameter
parity excludes the eight-odd profile `(7,0,1)` and leaves

```text
(4,3), (0,4), (3,1,1), (0,0,0,1).                   (1)
```

The profiles in (1) have zero or four odd autocorrelation classes and lie on
the complete zero/four-odd atlas: 28,863 normalized supports in 154 affine
odd-unit orbits. The exact direct router therefore has

```text
154*binom(124,3)*64 = 3,056,582,144
```

signed vectors per engine. No cubic-Hermite cutoff is invoked.
