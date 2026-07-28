# E1 N=256 E=13 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact finite classification

For an `N=256`, folded-profile `(3,4,0)` candidate at variance `V=26`, or
energy `E=13`, the positive-half autocorrelation L1 norm satisfies `L<=9`.
Exactly four magnitude profiles meet the energy/L1 and diameter-parity
constraints:

```text
(5,2), (1,3), (4,0,1), (0,1,1).                    (1)
```

The profiles in (1) have respectively five, one, five, and one odd classes.
They lie on the complete one/five-odd atlas: 14,664 normalized supports in 111
affine odd-unit orbits. The exact direct router therefore has

```text
111*binom(124,3)*64 = 2,203,120,896
```

signed vectors per engine. No cubic-Hermite cutoff is invoked.
