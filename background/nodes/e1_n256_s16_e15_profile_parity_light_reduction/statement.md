# E1 N=256 E=15 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact finite classification

For an `N=256`, folded-profile `(3,4,0)` candidate at variance `V=30`, or
energy `E=15`, the positive-half autocorrelation L1 norm satisfies `L<=9`.
Exactly three magnitude profiles meet the energy/L1 constraints. Diameter
parity excludes the seven-odd profile `(6,0,1)` and leaves

```text
(3,3), (2,1,1).                                     (1)
```

Both profiles in (1) have three odd autocorrelation classes and lie on the
complete three-odd atlas: 960 normalized supports in eight affine odd-unit
orbits. The exact direct router therefore has

```text
8*binom(124,3)*64 = 158,783,488
```

signed vectors per engine. No cubic-Hermite cutoff is invoked.
