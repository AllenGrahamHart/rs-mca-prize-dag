# E1 N=256 E=20 profile/parity/light reduction

- **status:** PROVED
- **closure:** exact finite router

For an `N=256`, folded-profile `(3,4,0)` candidate at variance `V=40`, or
energy `E=20`, the positive-half autocorrelation L1 norm satisfies `L<=12`.
Exactly seven magnitude profiles meet the energy/L1 constraints. Diameter
parity excludes the eight-odd profile `(7,1,1)` and leaves

```text
zero odd: (0,5), (0,1,0,1);
four odd: (4,4), (3,2,1), (2,0,2), (4,0,0,1).       (1)
```

The complete relevant even-parity light atlases contain 63 normalized
zero-odd supports in 6 affine odd-unit orbits and 28,800 normalized four-odd
supports in 148 orbits. The exact direct router therefore has

```text
(6+148)*binom(124,3)*64 = 3,056,582,144
```

signed vectors per engine. No cubic-Hermite cutoff is invoked.
