# E1 N=256 E=18 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact finite classification

For an `N=256`, folded-profile `(3,4,0)` candidate at variance `V=36`, or
energy `E=18`, the positive-half autocorrelation L1 norm satisfies `L<=12`.
Exactly seven magnitude profiles meet the energy/L1 constraints. Diameter
parity excludes the ten-odd profile `(9,0,1)` and leaves

```text
(6,3), (2,4), (5,1,1), (1,2,1), (0,0,2), (2,0,0,1).   (1)
```

The profiles in (1) have two or six odd autocorrelation classes and lie on
the complete even-parity light atlases: 288,888 normalized supports in
`87+1234=1321` affine odd-unit orbits. The exact direct router therefore has

```text
1321*binom(124,3)*64 = 26,219,123,456
```

signed vectors per engine. No cubic-Hermite cutoff is invoked.
