# E1 N=256 E=19 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact finite classification

For an `N=256`, folded-profile `(3,4,0)` candidate at variance `V=38`, or
energy `E=19`, the positive-half autocorrelation L1 norm satisfies `L<=11`.
Exactly five magnitude profiles meet the energy/L1 constraints. Diameter
parity excludes the seven-odd profile `(6,1,1)` and leaves

```text
(3,4), (2,2,1), (1,0,2), (3,0,0,1).                    (1)
```

Every profile in (1) has three odd autocorrelation classes and lies on the
complete one-diameter three-odd atlas: 960 normalized supports in 8 affine
odd-unit orbits. The exact direct router therefore has

```text
8*binom(124,3)*64 = 158,783,488
```

signed vectors per engine. No cubic-Hermite cutoff is invoked.
