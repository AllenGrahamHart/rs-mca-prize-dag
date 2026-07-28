# E1 N=256 E=14 profile/parity/light reduction

- **status:** PROVED
- **closure:** proof plus exact finite classification

For an `N=256`, folded-profile `(3,4,0)` candidate at variance `V=28`, or
energy `E=14`, the positive-half autocorrelation L1 norm satisfies `L<=10`.
Exactly four magnitude profiles meet the energy/L1 and diameter-parity
constraints:

```text
(6,2), (2,3), (5,0,1), (1,1,1).                    (1)
```

The profiles in (1) have respectively six, two, six, and two odd
autocorrelation classes. They lie on the complete even-parity atlas: 288,888
normalized supports in 1,321 affine odd-unit orbits. The exact direct router
therefore has

```text
1321*binom(124,3)*64 = 26,219,123,456
```

signed vectors per engine. No cubic-Hermite cutoff is invoked.
