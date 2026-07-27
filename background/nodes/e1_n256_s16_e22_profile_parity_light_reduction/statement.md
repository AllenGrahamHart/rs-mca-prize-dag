# E1 N=256 E=22 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact finite classification

For an `N=256`, folded-profile `(3,4,0)` candidate at variance `V=44`, or
energy `E=22`, the positive-half autocorrelation L1 norm satisfies `L<=14`.
Exactly nine magnitude profiles meet the energy/L1 constraints.  Diameter
parity excludes the ten-odd profile `(9,1,1)` and leaves

```text
two odd: (2,5), (1,3,1), (0,1,2), (2,1,0,1);
six odd: (6,4), (5,2,1), (4,0,2), (6,0,0,1).          (1)
```

The complete even-parity light atlases contain 8,168 normalized two-odd
supports in 87 affine odd-unit orbits and 280,720 normalized six-odd supports
in 1,234 orbits.  The exact direct router therefore has

```text
(87+1234)*binom(124,3)*64 = 26,219,123,456
```

signed vectors per engine.  No cubic-Hermite cutoff is invoked.
