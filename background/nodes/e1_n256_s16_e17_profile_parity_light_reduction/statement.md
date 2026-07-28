# E1 N=256 E=17 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact finite classification

For an `N=256`, folded-profile `(3,4,0)` candidate at variance `V=34`, or
energy `E=17`, the positive-half autocorrelation L1 norm satisfies `L<=11`.
Exactly six magnitude profiles meet the energy/L1 constraints. Diameter
parity excludes the nine-odd profile `(8,0,1)` and leaves

```text
(5,3), (1,4), (4,1,1), (0,2,1), (1,0,0,1).            (1)
```

The profiles in (1) have one or five odd autocorrelation classes and lie on
the complete one-diameter one/five-odd atlas: 14,664 normalized supports in
111 affine odd-unit orbits. The exact direct router therefore has

```text
111*binom(124,3)*64 = 2,203,120,896
```

signed vectors per engine. No cubic-Hermite cutoff is invoked.
